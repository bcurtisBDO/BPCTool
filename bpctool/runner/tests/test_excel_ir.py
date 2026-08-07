from pathlib import Path

from app.excel_ir import build_ir
from app.planner import build_dry_run_plan

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT.parent / "fixtures" / "ADO template guideline (July).xlsx"
CATALOG = Path("/Users/bill/BPC Files")


def test_build_ir_from_july_fixture_and_catalog():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        workbook_version="JUL-2026",
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )

    assert ir["counts"]["work_item_types"] >= 20
    assert ir["counts"]["fields"] >= 50
    assert ir["counts"]["teams"] >= 10
    assert ir["counts"]["catalog_files"] == 4
    assert ir["counts"]["catalog_rows"] > 1000


def test_dry_run_plan_sequence():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )
    plan = build_dry_run_plan(
        ir,
        update_policy="always-update",
        confirm_process_update=False,
        confirm_project_update=False,
        known_process_exists=False,
        known_project_exists=False,
    )

    assert plan.ok
    assert [step["id"] for step in plan.steps] == [
        "process",
        "layout",
        "project",
        "teams",
        "backlog",
        "catalog",
        "report",
    ]
    assert plan.steps[2]["depends_on"] == ["process", "layout"]
