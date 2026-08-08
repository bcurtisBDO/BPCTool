from pathlib import Path

from app.excel_ir import build_ir, is_catalog_source_file, parse_area_paths
from app.planner import build_dry_run_plan

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT.parent / "fixtures" / "ADO template guideline (July).xlsx"
CATALOG = Path("/Users/bill/BPC Files")


def test_catalog_source_file_naming():
    assert is_catalog_source_file(Path("Deliverables JUL 2026.xlsx"))
    assert is_catalog_source_file(Path("Deliverables.xlsx"))
    assert is_catalog_source_file(Path("Business Process Catalog JUL 2026.xlsx"))
    assert is_catalog_source_file(Path("Objectives JUL 2026.xlsx"))
    assert is_catalog_source_file(Path("SbD Delivery Plan JUL 2026.xlsx"))
    assert not is_catalog_source_file(Path("ADO template guideline (July).xlsx"))
    assert not is_catalog_source_file(Path("Random Notes.xlsx"))
    assert not is_catalog_source_file(Path("~$Deliverables JUL 2026.xlsx"))


def test_parse_area_paths_skips_project_column_and_keeps_hierarchy():
    areas = parse_area_paths(FIXTURE)
    assert areas
    assert all(not a["path"].startswith("Project name") for a in areas)
    assert areas[0]["path"] == "Business process catalog"
    bpc = [a for a in areas if a["team"] == "Business process catalog"]
    assert len(bpc) >= 16
    assert any(a["path"] == "Business process catalog\\Acquire to dispose" for a in bpc)
    asset = next(a for a in areas if a["team"] == "Asset financials")
    assert asset["path"] == "Functional areas\\Finance\\Accounting\\Asset financials"
    # Multi-path teams must retain every mapped row (not just the last).
    accounting = [a["path"] for a in areas if a["team"] == "Accounting"]
    assert "Functional areas\\Finance" in accounting
    assert "Functional areas\\Finance\\Accounting" in accounting


def test_build_ir_from_july_fixture_and_catalog():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        workbook_version="JUL-2026",
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )

    assert ir["counts"]["work_item_types"] >= 20
    assert ir["counts"]["disabled_work_item_types"] >= 3  # Epic, Feature, User story
    disabled = {
        w["name"] for w in ir["process"]["work_item_types"] if w.get("disabled")
    }
    assert {"Epic", "Feature", "User story"} <= disabled
    assert ir["counts"]["backlogs"] == 6
    by_backlog = {b["name"]: b for b in ir["process"]["backlogs"]}
    assert by_backlog["Levels"]["rename_from"] == "Epic"
    assert by_backlog["Lowest"]["rename_from"] == "Feature"
    assert by_backlog["Deliverables"]["rename_from"] == "(rename)"
    assert by_backlog["Highest"]["rename_from"] == "(new)"
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
