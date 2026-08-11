"""Resume, parent-aware ready queue, and id-map helpers for catalog import."""

from __future__ import annotations

from pathlib import Path

from app.catalog_import import WorkItemDraft
from app.catalog_runtime import (
    clamp_parallel_workers,
    load_id_map,
    open_id_map_for_append,
    append_id_map_row,
    ready_drafts,
    import_drafts_parent_aware,
)


def _draft(
    key: str,
    *,
    parent_key: str | None = None,
    wit: str = "Scenario",
    title: str | None = None,
    row: int = 1,
) -> WorkItemDraft:
    return WorkItemDraft(
        key=key,
        parent_key=parent_key,
        work_item_type=wit,
        title=title or key,
        fields={"System.Title": title or key},
        source_file="bpc.xlsx",
        source_row=row,
    )


def test_clamp_parallel_workers() -> None:
    assert clamp_parallel_workers(None) == 4
    assert clamp_parallel_workers(0) == 1
    assert clamp_parallel_workers(99) == 16
    assert clamp_parallel_workers(8) == 8


def test_load_id_map_resume(tmp_path: Path) -> None:
    path = tmp_path / "ado-id-map.csv"
    path.write_text(
        "Key,WorkItemId,WorkItemType,Title,ParentKey,ParentId\n"
        "root,101,End to end,Root,,\n"
        "child,102,Scenario,Child,root,101\n",
        encoding="utf-8",
    )
    assert load_id_map(path) == {"root": 101, "child": 102}
    assert load_id_map(tmp_path / "missing.csv") == {}


def test_ready_drafts_parent_aware() -> None:
    pending = {
        "a": _draft("a", row=1),
        "b": _draft("b", parent_key="a", row=2),
        "c": _draft("c", parent_key="missing", row=3),
    }
    ready = ready_drafts(pending, id_map={}, limit=10)
    assert [d.key for d in ready] == ["a"]
    del pending["a"]
    ready2 = ready_drafts(pending, id_map={"a": 1}, limit=10)
    assert [d.key for d in ready2] == ["b"]


def test_import_resume_skips_existing(tmp_path: Path) -> None:
    id_map_path = tmp_path / "ado-id-map.csv"
    handle, writer = open_id_map_for_append(id_map_path)
    root = _draft("root", row=1)
    append_id_map_row(writer, handle, root, 10, None)
    handle.close()

    class FakeClient:
        def __init__(self) -> None:
            self.created: list[str] = []

        def create_work_item(self, project, wit, fields, **kwargs):
            key = fields["System.Title"]
            self.created.append(key)
            return {"id": 100 + len(self.created)}

    client = FakeClient()
    drafts = [
        _draft("root", row=1),
        _draft("child", parent_key="root", row=2, title="child"),
    ]
    events: list[str] = []
    id_map = load_id_map(id_map_path)
    id_map, failures, stats = import_drafts_parent_aware(
        client,  # type: ignore[arg-type]
        drafts,
        project="Demo",
        id_map=id_map,
        id_map_path=id_map_path,
        parallel_workers=1,
        emit=lambda _s, msg: events.append(msg),
    )
    assert stats["skipped"] == 1
    assert stats["created"] == 1
    assert id_map["root"] == 10
    assert id_map["child"] == 101
    assert client.created == ["child"]
    assert failures == []
    assert any("Resume" in e for e in events)


def test_import_parallel_waits_for_parent(tmp_path: Path) -> None:
    id_map_path = tmp_path / "ado-id-map.csv"

    class FakeClient:
        def __init__(self) -> None:
            self.order: list[str] = []

        def create_work_item(self, project, wit, fields, **kwargs):
            key = fields["System.Title"]
            self.order.append(key)
            parent_id = kwargs.get("parent_id")
            if key == "child" and parent_id is None:
                raise AssertionError("child created before parent id known")
            return {"id": {"root": 1, "child": 2, "leaf": 3}[key]}

    client = FakeClient()
    drafts = [
        _draft("leaf", parent_key="child", row=3, title="leaf"),
        _draft("child", parent_key="root", row=2, title="child"),
        _draft("root", row=1, title="root"),
    ]
    id_map, failures, stats = import_drafts_parent_aware(
        client,  # type: ignore[arg-type]
        drafts,
        project="Demo",
        id_map={},
        id_map_path=id_map_path,
        parallel_workers=4,
        emit=lambda *_: None,
    )
    assert failures == []
    assert stats["created"] == 3
    assert stats["linked"] == 2
    assert id_map == {"root": 1, "child": 2, "leaf": 3}
    assert client.order[0] == "root"
