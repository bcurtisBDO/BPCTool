"""Catalog parent links follow Title 1..N outline (ADO CSV import style)."""

from __future__ import annotations

from pathlib import Path

from app.catalog_import import (
    WorkItemDraft,
    _fill_title_hierarchy_parents,
    load_catalog_drafts,
)
from app.excel_ir import build_ir
from app.mapping import build_mapping_from_ir
from app.paths import bpc_files_root, resolve_release_folder

CATALOG = resolve_release_folder(bpc_files_root()) or bpc_files_root()


def test_title_hierarchy_parents_for_outline_rows() -> None:
    drafts = [
        WorkItemDraft(
            key="t1",
            parent_key=None,
            work_item_type="Tree",
            title="Root",
            fields={},
            source_file="Deliverables.xlsx",
            source_row=2,
            hierarchy_level=1,
        ),
        WorkItemDraft(
            key="f1",
            parent_key=None,
            work_item_type="Folder",
            title="Finance",
            fields={},
            source_file="Deliverables.xlsx",
            source_row=3,
            hierarchy_level=2,
        ),
        WorkItemDraft(
            key="f2",
            parent_key=None,
            work_item_type="Folder",
            title="Accounting",
            fields={},
            source_file="Deliverables.xlsx",
            source_row=4,
            hierarchy_level=3,
        ),
        WorkItemDraft(
            key="w1",
            parent_key=None,
            work_item_type="Workflow",
            title="Ledger workflow",
            fields={},
            source_file="Deliverables.xlsx",
            source_row=5,
            hierarchy_level=6,
        ),
        WorkItemDraft(
            key="f3",
            parent_key=None,
            work_item_type="Folder",
            title="HR",
            fields={},
            source_file="Deliverables.xlsx",
            source_row=6,
            hierarchy_level=2,
        ),
    ]
    _fill_title_hierarchy_parents(drafts)
    assert drafts[0].parent_key is None
    assert drafts[1].parent_key == "t1"
    assert drafts[2].parent_key == "f1"
    assert drafts[3].parent_key == "f2"
    # Sibling under Tree, not under Accounting/Workflow.
    assert drafts[4].parent_key == "t1"


def test_explicit_parent_column_wins_over_title_outline() -> None:
    drafts = [
        WorkItemDraft(
            key="root",
            parent_key=None,
            work_item_type="Tree",
            title="Root",
            fields={},
            source_file="x.xlsx",
            source_row=2,
            hierarchy_level=1,
        ),
        WorkItemDraft(
            key="child",
            parent_key="forced-parent",
            work_item_type="Scenario",
            title="Child",
            fields={},
            source_file="x.xlsx",
            source_row=3,
            hierarchy_level=5,
        ),
    ]
    _fill_title_hierarchy_parents(drafts)
    assert drafts[1].parent_key == "forced-parent"


def test_catalog_parents_use_title_outline(template_path) -> None:
    if not CATALOG.is_dir():
        return
    ir = build_ir(
        str(template_path),
        catalog_source_dir=str(CATALOG),
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )
    mapping = build_mapping_from_ir(ir)
    drafts = load_catalog_drafts(CATALOG, mapping, limit=None)
    by_key = {d.key: d for d in drafts}

    bpc = [d for d in drafts if "Business Process Catalog" in d.source_file]
    assert bpc
    # Tree root has no parent; almost everything else should.
    roots = [d for d in bpc if not d.parent_key]
    assert len(roots) >= 1
    assert all(d.hierarchy_level == 1 for d in roots)

    linked = [d for d in bpc if d.parent_key]
    assert len(linked) > 4000
    missing = [d for d in linked if d.parent_key not in by_key]
    assert missing == [], f"Unresolved Title-outline parents e.g. {missing[:5]}"

    # Scenario (Title 5) → Process (Title 4), not a process-sequence strip.
    scenarios = [d for d in bpc if d.hierarchy_level == 5 and d.parent_key]
    assert scenarios
    sample = scenarios[0]
    parent = by_key[sample.parent_key]
    assert parent.hierarchy_level == 4

    deliverables = [d for d in drafts if d.source_file.startswith("Deliverables")]
    assert deliverables
    d_linked = [d for d in deliverables if d.parent_key]
    assert len(d_linked) > 1000
    assert all(d.parent_key in by_key for d in d_linked)
