"""Catalog import runtime: resume id-map, parent-aware parallel create, backfill."""

from __future__ import annotations

import csv
import threading
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from pathlib import Path
from typing import Any, Callable

from .ado_client import AdoClient, AdoError
from .catalog_import import WorkItemDraft

Emit = Callable[[str, str], None]

ID_MAP_FIELDS = [
    "Key",
    "WorkItemId",
    "WorkItemType",
    "Title",
    "ParentKey",
    "ParentId",
]


def clamp_parallel_workers(value: int | None, *, default: int = 4) -> int:
    try:
        workers = int(value) if value is not None else default
    except (TypeError, ValueError):
        workers = default
    return max(1, min(workers, 16))


def load_id_map(path: Path) -> dict[str, int]:
    """Load Key → ADO work item id from ado-id-map.csv (resume)."""
    if not path.is_file():
        return {}
    mapping: dict[str, int] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            key = str(row.get("Key") or "").strip()
            raw_id = str(row.get("WorkItemId") or "").strip()
            if not key or not raw_id:
                continue
            try:
                mapping[key] = int(raw_id)
            except ValueError:
                continue
    return mapping


def open_id_map_for_append(path: Path) -> tuple[Any, csv.DictWriter]:
    """Open id-map CSV for append, writing header only when creating a new file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.is_file() or path.stat().st_size == 0
    handle = path.open("a", encoding="utf-8", newline="")
    writer = csv.DictWriter(handle, fieldnames=ID_MAP_FIELDS)
    if write_header:
        writer.writeheader()
        handle.flush()
    return handle, writer


def append_id_map_row(
    writer: csv.DictWriter,
    handle: Any,
    draft: WorkItemDraft,
    work_item_id: int,
    parent_id: int | None,
    *,
    lock: threading.Lock | None = None,
) -> None:
    row = {
        "Key": draft.key,
        "WorkItemId": work_item_id,
        "WorkItemType": draft.work_item_type,
        "Title": draft.title,
        "ParentKey": draft.parent_key or "",
        "ParentId": parent_id or "",
    }

    def _write() -> None:
        writer.writerow(row)
        handle.flush()

    if lock is None:
        _write()
    else:
        with lock:
            _write()


def ready_drafts(
    pending: dict[str, WorkItemDraft],
    id_map: dict[str, int],
    limit: int,
) -> list[WorkItemDraft]:
    """Drafts whose parent is already imported (or have no parent)."""
    if limit <= 0:
        return []
    ready = [
        draft
        for draft in pending.values()
        if not draft.parent_key or draft.parent_key in id_map
    ]
    ready.sort(key=lambda d: (d.source_file, d.source_row, d.key))
    return ready[:limit]


def import_drafts_parent_aware(
    client: AdoClient,
    drafts: list[WorkItemDraft],
    *,
    project: str,
    id_map: dict[str, int],
    id_map_path: Path,
    parallel_workers: int,
    emit: Emit,
) -> tuple[dict[str, int], list[dict[str, Any]], dict[str, int]]:
    """
    Create drafts with resume + parent-aware parallelism.

    Returns (id_map, failures, stats) where stats has created/skipped/linked/failed/
    missing_parent (stuck without parent).
    """
    workers = clamp_parallel_workers(parallel_workers)
    stats = {
        "created": 0,
        "skipped": 0,
        "linked": 0,
        "failed": 0,
        "missing_parent": 0,
    }
    failures: list[dict[str, Any]] = []

    already = [d for d in drafts if d.key in id_map]
    stats["skipped"] = len(already)
    if already:
        emit(
            "catalog",
            f"Resume: skipping {len(already)} work item(s) already in {id_map_path.name}",
        )

    pending = {d.key: d for d in drafts if d.key not in id_map}
    if not pending:
        emit("catalog", "Resume: nothing left to create")
        return id_map, failures, stats

    emit(
        "catalog",
        f"Creating {len(pending)} work item(s) with {workers} parent-aware worker(s)",
    )

    handle, writer = open_id_map_for_append(id_map_path)
    lock = threading.Lock()
    try:
        if workers == 1:
            _import_serial(
                client,
                pending,
                drafts,
                project=project,
                id_map=id_map,
                writer=writer,
                handle=handle,
                lock=lock,
                failures=failures,
                stats=stats,
                emit=emit,
            )
        else:
            _import_parallel(
                client,
                pending,
                drafts,
                project=project,
                id_map=id_map,
                writer=writer,
                handle=handle,
                lock=lock,
                failures=failures,
                stats=stats,
                workers=workers,
                emit=emit,
            )
    finally:
        handle.close()

    return id_map, failures, stats


def _failure(draft: WorkItemDraft, error: str) -> dict[str, Any]:
    return {
        "key": draft.key,
        "workItemType": draft.work_item_type,
        "title": draft.title,
        "parentKey": draft.parent_key,
        "error": error,
        "sourceFile": draft.source_file,
        "sourceRow": draft.source_row,
    }


def _create_one(
    client: AdoClient,
    draft: WorkItemDraft,
    *,
    project: str,
    parent_id: int | None,
) -> tuple[int, bool]:
    created = client.create_work_item(
        project,
        draft.work_item_type,
        draft.fields,
        parent_id=parent_id,
        dry_run=False,
        markdown_format_fields=draft.markdown_format_fields,
    )
    work_item_id = int(created["id"])
    return work_item_id, parent_id is not None


def _import_serial(
    client: AdoClient,
    pending: dict[str, WorkItemDraft],
    drafts: list[WorkItemDraft],
    *,
    project: str,
    id_map: dict[str, int],
    writer: csv.DictWriter,
    handle: Any,
    lock: threading.Lock,
    failures: list[dict[str, Any]],
    stats: dict[str, int],
    emit: Emit,
) -> None:
    total = len(drafts)
    done_count = stats["skipped"]
    while pending:
        batch = ready_drafts(pending, id_map, len(pending))
        if not batch:
            for draft in list(pending.values()):
                stats["missing_parent"] += 1
                stats["failed"] += 1
                failures.append(
                    _failure(draft, f"Parent not imported: {draft.parent_key}")
                )
            pending.clear()
            break
        for draft in batch:
            del pending[draft.key]
            parent_id = id_map.get(draft.parent_key) if draft.parent_key else None
            try:
                work_item_id, linked = _create_one(
                    client, draft, project=project, parent_id=parent_id
                )
                with lock:
                    id_map[draft.key] = work_item_id
                append_id_map_row(
                    writer,
                    handle,
                    draft,
                    work_item_id,
                    parent_id,
                    lock=lock,
                )
                stats["created"] += 1
                if linked:
                    stats["linked"] += 1
            except (AdoError, KeyError, TypeError, ValueError) as exc:
                stats["failed"] += 1
                failures.append(_failure(draft, str(exc)))
            done_count += 1
            if done_count % 100 == 0:
                emit(
                    "catalog",
                    f"Imported {done_count}/{total} work items "
                    f"(created {stats['created']}, skipped {stats['skipped']})...",
                )


def _import_parallel(
    client: AdoClient,
    pending: dict[str, WorkItemDraft],
    drafts: list[WorkItemDraft],
    *,
    project: str,
    id_map: dict[str, int],
    writer: csv.DictWriter,
    handle: Any,
    lock: threading.Lock,
    failures: list[dict[str, Any]],
    stats: dict[str, int],
    workers: int,
    emit: Emit,
) -> None:
    total = len(drafts)
    done_count = stats["skipped"]
    in_flight: dict[Future, tuple[WorkItemDraft, int | None]] = {}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        while pending or in_flight:
            slots = workers - len(in_flight)
            for draft in ready_drafts(pending, id_map, slots):
                parent_id = id_map.get(draft.parent_key) if draft.parent_key else None
                future = executor.submit(
                    _create_one,
                    client,
                    draft,
                    project=project,
                    parent_id=parent_id,
                )
                in_flight[future] = (draft, parent_id)
                del pending[draft.key]

            if not in_flight:
                if pending:
                    for draft in list(pending.values()):
                        stats["missing_parent"] += 1
                        stats["failed"] += 1
                        failures.append(
                            _failure(draft, f"Parent not imported: {draft.parent_key}")
                        )
                    pending.clear()
                break

            completed, _ = wait(in_flight, return_when=FIRST_COMPLETED)
            for future in completed:
                draft, parent_id = in_flight.pop(future)
                try:
                    work_item_id, linked = future.result()
                    with lock:
                        id_map[draft.key] = work_item_id
                    append_id_map_row(
                        writer,
                        handle,
                        draft,
                        work_item_id,
                        parent_id,
                        lock=lock,
                    )
                    stats["created"] += 1
                    if linked:
                        stats["linked"] += 1
                except (AdoError, KeyError, TypeError, ValueError) as exc:
                    stats["failed"] += 1
                    failures.append(_failure(draft, str(exc)))
                done_count += 1
                if done_count % 100 == 0:
                    emit(
                        "catalog",
                        f"Imported {done_count}/{total} work items "
                        f"(created {stats['created']}, skipped {stats['skipped']})...",
                    )


def backfill_parent_links(
    client: AdoClient,
    drafts: list[WorkItemDraft],
    id_map: dict[str, int],
    *,
    project: str,
    output_dir: Path,
    emit: Emit,
) -> dict[str, int]:
    """
    For created items with a known parent id, ensure Hierarchy-Reverse exists.
    Writes backfill-links-report.csv (July-compatible statuses).
    """
    candidates = [
        draft
        for draft in drafts
        if draft.key in id_map and draft.parent_key and draft.parent_key in id_map
    ]
    counts = {
        "linked": 0,
        "already_linked": 0,
        "conflict_existing_parent": 0,
        "failed": 0,
        "candidates": len(candidates),
    }
    if not candidates:
        emit("catalog", "Parent-link backfill: no candidates")
        return counts

    emit(
        "catalog",
        f"Parent-link backfill: checking {len(candidates)} work item(s)…",
    )
    report_path = output_dir / "backfill-links-report.csv"
    rows: list[dict[str, Any]] = []

    for index, draft in enumerate(candidates, start=1):
        child_id = id_map[draft.key]
        expected_parent_id = id_map[draft.parent_key or ""]
        status = "planned"
        message = ""
        try:
            current_parent_id = client.get_parent_id(project, child_id)
            if current_parent_id == expected_parent_id:
                status = "already_linked"
                counts["already_linked"] += 1
            elif current_parent_id is not None:
                status = "conflict_existing_parent"
                message = (
                    f"Existing parent {current_parent_id}; "
                    f"expected {expected_parent_id}"
                )
                counts["conflict_existing_parent"] += 1
            else:
                client.add_parent_link(project, child_id, expected_parent_id)
                status = "linked"
                counts["linked"] += 1
        except (AdoError, KeyError, TypeError, ValueError) as exc:
            status = "failed"
            message = str(exc)
            counts["failed"] += 1

        rows.append(
            {
                "Key": draft.key,
                "Parent Key": draft.parent_key or "",
                "ADO ID": child_id,
                "Parent ADO ID": expected_parent_id,
                "Work Item Type": draft.work_item_type,
                "Title": draft.title,
                "Status": status,
                "Message": message,
            }
        )
        if index % 200 == 0:
            emit("catalog", f"Parent-link backfill: {index}/{len(candidates)}…")

    with report_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "Key",
                "Parent Key",
                "ADO ID",
                "Parent ADO ID",
                "Work Item Type",
                "Title",
                "Status",
                "Message",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    summary = ", ".join(
        f"{k}={v}"
        for k, v in sorted(counts.items())
        if k != "candidates" and v
    )
    emit(
        "catalog",
        f"Parent-link backfill finished: {summary or 'no changes'}; "
        f"wrote {report_path.name}",
    )
    return counts
