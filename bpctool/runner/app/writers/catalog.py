"""Import catalog work items with HTML/markdown-normalized rich text."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Callable

from ..ado_client import AdoClient
from ..catalog_import import load_catalog_drafts
from ..catalog_runtime import (
    Progress,
    ShouldCancel,
    backfill_parent_links,
    clamp_parallel_workers,
    import_drafts_parent_aware,
    load_id_map,
    load_id_map_parents,
)
from ..catalog_validate import prevalidate_catalog_drafts, prevalidate_summary
from ..mapping import build_mapping_from_ir

Emit = Callable[[str, str], None]


def apply_catalog(
    client: AdoClient,
    ir: dict[str, Any],
    *,
    dry_run: bool,
    emit: Emit,
    output_dir: Path,
    limit: int | None = None,
    convert_markdown_to_html: bool = False,
    parallel_workers: int | None = None,
    progress: Progress | None = None,
    should_cancel: ShouldCancel | None = None,
) -> dict[str, Any]:
    project = ir["targets"]["project_name"]
    catalog_dir = ir["source"].get("catalog_source_dir")
    workers = clamp_parallel_workers(parallel_workers)
    stats: dict[str, Any] = {
        "drafts": 0,
        "created": 0,
        "skipped": 0,
        "failed": 0,
        "linked": 0,
        "missing_parent": 0,
        "cancelled": 0,
        "backfill": {},
        "parallel_workers": workers,
        "prevalidate": {},
        "html_fields_normalized": 0,
        "markdown_preserved": 0,
        "markdown_converted": 0,
        "html_passthrough": 0,
        "convert_markdown_to_html": convert_markdown_to_html,
        "id_map_path": None,
    }

    if not catalog_dir or not ir["counts"].get("catalog_rows"):
        emit("catalog", "No catalog sources — skipped")
        return stats

    mapping = build_mapping_from_ir(ir)
    drafts = load_catalog_drafts(
        catalog_dir,
        mapping,
        limit=limit,
        convert_markdown_to_html=convert_markdown_to_html,
    )
    stats["drafts"] = len(drafts)

    for draft in drafts:
        for ref, kind in draft.content_formats.items():
            stats["html_fields_normalized"] += 1
            if kind == "markdown":
                stats["markdown_preserved"] += 1
            elif kind == "markdown→html":
                stats["markdown_converted"] += 1
            elif kind == "html":
                stats["html_passthrough"] += 1

    mode_label = (
        f"markdown→HTML {stats['markdown_converted']}"
        if convert_markdown_to_html
        else f"markdown preserved {stats['markdown_preserved']}"
    )
    emit(
        "catalog",
        f"Prepared {len(drafts)} drafts "
        f"({mode_label}, HTML passthrough {stats['html_passthrough']})",
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    id_map_path = output_dir / "ado-id-map.csv"
    failures_path = output_dir / "import-failures.json"
    preview_path = output_dir / "import-preview.csv"

    # Always write a preview sample showing normalized rich text.
    with preview_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "Key",
                "WorkItemType",
                "Title",
                "DescriptionFormat",
                "DescriptionSample",
                "SourceFile",
                "SourceRow",
            ],
        )
        writer.writeheader()
        for draft in drafts[:50]:
            description = str(draft.fields.get("System.Description") or "")
            writer.writerow(
                {
                    "Key": draft.key,
                    "WorkItemType": draft.work_item_type,
                    "Title": draft.title,
                    "DescriptionFormat": draft.content_formats.get(
                        "System.Description", ""
                    ),
                    "DescriptionSample": description[:240],
                    "SourceFile": draft.source_file,
                    "SourceRow": draft.source_row,
                }
            )

    with_parent = sum(1 for d in drafts if d.parent_key)
    emit(
        "catalog",
        f"Hierarchy: {with_parent}/{len(drafts)} drafts have a parent key "
        f"(Title 1..N outline / ADO CSV style)",
    )

    pre = prevalidate_catalog_drafts(drafts, ir, mapping, sanitize=True)
    summary = prevalidate_summary(pre)
    stats["prevalidate"] = summary
    prevalidate_path = output_dir / "import-prevalidate.json"
    prevalidate_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    counts = summary.get("counts") or {}
    if (
        counts
        or summary.get("fieldsStripped")
        or summary.get("multiSelectNormalized")
        or summary.get("defaultsApplied")
    ):
        parts = [f"{k}={v}" for k, v in sorted(counts.items())]
        emit(
            "catalog",
            "Prevalidate: "
            + (", ".join(parts) if parts else "ok")
            + f"; stripped {summary.get('fieldsStripped', 0)} field values, "
            f"defaults applied {summary.get('defaultsApplied', 0)}, "
            f"normalized {summary.get('multiSelectNormalized', 0)} multi-select; "
            f"wrote {prevalidate_path.name}",
        )
    else:
        emit("catalog", f"Prevalidate: no issues ({prevalidate_path.name})")

    if dry_run:
        existing = load_id_map(id_map_path)
        remaining = sum(1 for d in drafts if d.key not in existing)
        emit(
            "catalog",
            f"[dry-run] Preview written ({preview_path.name}); "
            f"would import {remaining} of {len(drafts)} work items "
            f"({len(existing)} already in id-map) with {workers} worker(s), "
            + (
                "markdown→HTML, "
                if convert_markdown_to_html
                else "preserving markdown (multilineFieldsFormat=Markdown), "
            )
            + "then parent-link backfill",
        )
        stats["skipped"] = len(existing)
        stats["id_map_path"] = str(preview_path)
        return stats

    id_map = load_id_map(id_map_path)
    id_map, failures, create_stats = import_drafts_parent_aware(
        client,
        drafts,
        project=project,
        id_map=id_map,
        id_map_path=id_map_path,
        parallel_workers=workers,
        emit=emit,
        progress=progress,
        should_cancel=should_cancel,
    )
    stats.update(create_stats)
    failures_path.write_text(json.dumps(failures, indent=2), encoding="utf-8")
    stats["id_map_path"] = str(id_map_path)

    if should_cancel is not None and should_cancel():
        emit("catalog", "Cancelled before parent-link backfill; re-run to resume and backfill")
        stats["backfill"] = {"skipped": "cancelled"}
    else:
        backfill_stats = backfill_parent_links(
            client,
            drafts,
            id_map,
            project=project,
            output_dir=output_dir,
            emit=emit,
            recorded_parents=load_id_map_parents(id_map_path),
            parallel_workers=workers,
            progress=progress,
            should_cancel=should_cancel,
        )
        stats["backfill"] = backfill_stats
        # Count backfill links toward linked when create missed the relation.
        stats["linked"] = int(stats.get("linked") or 0) + int(
            backfill_stats.get("linked") or 0
        )

    emit(
        "catalog",
        f"Catalog import finished: created {stats['created']}, "
        f"skipped {stats['skipped']}, linked {stats['linked']}, "
        f"missing parent {stats['missing_parent']}, failed {stats['failed']}"
        + (f", cancelled {stats['cancelled']}" if stats.get("cancelled") else "")
        + (f", reconciled {stats['reconciled']}" if stats.get("reconciled") else "")
        + f", workers {workers}",
    )
    return stats
