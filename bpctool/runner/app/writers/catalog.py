"""Import catalog work items with HTML/markdown-normalized rich text."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Callable

from ..ado_client import AdoClient, AdoError
from ..catalog_import import load_catalog_drafts
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
) -> dict[str, Any]:
    project = ir["targets"]["project_name"]
    catalog_dir = ir["source"].get("catalog_source_dir")
    stats = {
        "drafts": 0,
        "created": 0,
        "skipped": 0,
        "failed": 0,
        "linked": 0,
        "missing_parent": 0,
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
                    "DescriptionFormat": draft.content_formats.get("System.Description", ""),
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
        emit(
            "catalog",
            f"[dry-run] Preview written ({preview_path.name}); "
            f"would import {len(drafts)} work items "
            + (
                "with markdown converted to HTML"
                if convert_markdown_to_html
                else "preserving markdown (multilineFieldsFormat=Markdown)"
            ),
        )
        stats["id_map_path"] = str(preview_path)
        return stats

    id_map: dict[str, int] = {}
    failures: list[dict[str, Any]] = []
    parent_ids: dict[str, int] = {}

    with id_map_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["Key", "WorkItemId", "WorkItemType", "Title", "ParentKey", "ParentId"],
        )
        writer.writeheader()

        for index, draft in enumerate(drafts, start=1):
            parent_id = parent_ids.get(draft.parent_key) if draft.parent_key else None
            if draft.parent_key and parent_id is None:
                stats["missing_parent"] += 1
                if stats["missing_parent"] <= 20:
                    emit(
                        "catalog",
                        f"WARNING: Title-outline parent key '{draft.parent_key}' "
                        f"has no ADO id yet for '{draft.key}' "
                        f"({draft.work_item_type}) — creating unlinked "
                        f"(parent create likely failed earlier; keys are "
                        f"Process sequence ID, not the hierarchy rule)",
                    )
            try:
                created = client.create_work_item(
                    project,
                    draft.work_item_type,
                    draft.fields,
                    parent_id=parent_id,
                    dry_run=False,
                    markdown_format_fields=draft.markdown_format_fields,
                )
                work_item_id = int(created["id"])
                id_map[draft.key] = work_item_id
                parent_ids[draft.key] = work_item_id
                if parent_id is not None:
                    stats["linked"] += 1
                writer.writerow(
                    {
                        "Key": draft.key,
                        "WorkItemId": work_item_id,
                        "WorkItemType": draft.work_item_type,
                        "Title": draft.title,
                        "ParentKey": draft.parent_key or "",
                        "ParentId": parent_id or "",
                    }
                )
                stats["created"] += 1
            except (AdoError, KeyError, TypeError, ValueError) as exc:
                stats["failed"] += 1
                failures.append(
                    {
                        "key": draft.key,
                        "workItemType": draft.work_item_type,
                        "title": draft.title,
                        "parentKey": draft.parent_key,
                        "error": str(exc),
                        "sourceFile": draft.source_file,
                        "sourceRow": draft.source_row,
                    }
                )

            if index % 100 == 0:
                emit("catalog", f"Imported {index}/{len(drafts)} work items...")

    failures_path.write_text(json.dumps(failures, indent=2), encoding="utf-8")
    stats["id_map_path"] = str(id_map_path)
    emit(
        "catalog",
        f"Catalog import finished: created {stats['created']}, "
        f"linked {stats['linked']}, missing parent {stats['missing_parent']}, "
        f"failed {stats['failed']}",
    )
    return stats
