from pathlib import Path

from app.catalog_import import load_catalog_drafts
from app.excel_ir import build_ir
from app.mapping import build_mapping_from_ir

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT.parent / "fixtures" / "ADO template guideline (July).xlsx"
CATALOG = Path("/Users/bill/BPC Files")


def test_catalog_drafts_preserve_markdown_by_default():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )
    mapping = build_mapping_from_ir(ir)
    drafts = load_catalog_drafts(CATALOG, mapping, limit=200)
    assert len(drafts) >= 50

    preserved = [
        d
        for d in drafts
        if d.content_formats.get("System.Description") == "markdown"
        and "System.Description" in d.markdown_format_fields
    ]
    assert preserved, "Expected markdown descriptions preserved with multiline format flag"
    sample = preserved[0].fields["System.Description"]
    assert "<ul>" not in sample
    assert "<p>" not in sample


def test_catalog_drafts_convert_markdown_when_requested():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )
    mapping = build_mapping_from_ir(ir)
    drafts = load_catalog_drafts(
        CATALOG, mapping, limit=200, convert_markdown_to_html=True
    )
    converted = [
        d
        for d in drafts
        if d.content_formats.get("System.Description") == "markdown→html"
    ]
    assert converted
    sample = converted[0].fields["System.Description"]
    assert "<p>" in sample or "<ul>" in sample or "<div>" in sample
    assert converted[0].markdown_format_fields == []


def test_ir_counts_html_fields():
    ir = build_ir(
        str(FIXTURE),
        catalog_source_dir=str(CATALOG),
        process_name="Business Process Catalog",
        project_name="Contoso-BPC",
    )
    assert ir["counts"]["html_fields"] >= 10
