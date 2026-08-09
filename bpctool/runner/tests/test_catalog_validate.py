"""Catalog prevalidate + multi-select token checks."""

from __future__ import annotations

from app.catalog_import import WorkItemDraft
from app.catalog_validate import (
    join_multi_select,
    prevalidate_catalog_drafts,
    split_multi_select,
)
from app.mapping import FieldDef, TemplateMapping


def _mapping() -> TemplateMapping:
    mapping = TemplateMapping()
    for fd in (
        FieldDef(
            label="Application family",
            reference_name="MSBPC.applicationfamily",
            field_type="PicklistString",
            multi_select=True,
            custom_field=True,
        ),
        FieldDef(
            label="Products",
            reference_name="MSBPC.products",
            field_type="PicklistString",
            multi_select=True,
            custom_field=True,
        ),
        FieldDef(
            label="Job purpose",
            reference_name="MSBPC.jobpurpose",
            field_type="PicklistString",
            multi_select=False,
            custom_field=True,
            required="No",
        ),
        FieldDef(
            label="Data type",
            reference_name="MSBPC.datatype",
            field_type="PicklistString",
            multi_select=False,
            custom_field=True,
            required="Yes",
        ),
        FieldDef(
            label="Business process flow source",
            reference_name="MSBPC.businessprocessflowsource",
            field_type="PicklistString",
            multi_select=False,
            custom_field=True,
            required="Yes",
            default_value="Microsoft",
        ),
        FieldDef(
            label="Catalog status",
            reference_name="MSBPC.catalogstatus",
            field_type="PicklistString",
            multi_select=False,
            custom_field=True,
            required="Yes",
            default_value="10 - New",
        ),
        FieldDef(
            label="Continuous",
            reference_name="MSBPC.continuous",
            field_type="Boolean",
            multi_select=False,
            custom_field=True,
            required="Yes",
            default_value="false",
        ),
    ):
        mapping.fields_by_label[fd.label.lower()] = fd
        mapping.fields_by_ref[fd.reference_name.lower()] = fd
    mapping.applicable_fields_by_wit["migration"] = {"data type"}
    mapping.applicable_fields_by_wit["job"] = {"job purpose"}
    mapping.applicable_fields_by_wit["process"] = {
        "application family",
        "products",
        "business process flow source",
        "catalog status",
        "continuous",
    }
    mapping.applicable_fields_by_wit["test case"] = set()
    return mapping


def _ir() -> dict:
    return {
        "process": {
            "picklists": {
                "Application family": [
                    "Business Central",
                    "Finance and Operations",
                    "Customer Engagement",
                ],
                "Products": ["Business Central", "Finance", "Field Service"],
                "Job purpose": ["Integration", "Reporting"],
                "Data type": ["Master data", "Setup data"],
                "Business process flow source": ["Microsoft", "Partner", "Customer"],
                "Catalog status": ["10 - New", "20 - Review"],
            }
        }
    }


def test_split_join_multi_select() -> None:
    assert split_multi_select("Business Central; Finance and Operations") == [
        "Business Central",
        "Finance and Operations",
    ]
    assert join_multi_select(["A", "B"]) == "A; B"


def test_prevalidate_strips_bad_area_and_test_case_state() -> None:
    drafts = [
        WorkItemDraft(
            key="t1",
            parent_key=None,
            work_item_type="Test Case",
            title="Case",
            fields={"System.State": "New", "System.AreaPath": "Not found"},
            source_file="bpc.xlsx",
            source_row=2,
        )
    ]
    result = prevalidate_catalog_drafts(drafts, _ir(), _mapping(), sanitize=True)
    assert "System.State" not in drafts[0].fields
    assert "System.AreaPath" not in drafts[0].fields
    assert result.counts.get("invalid_state") == 1
    assert result.counts.get("invalid_area_path") == 1
    assert result.fields_stripped == 2


def test_prevalidate_multi_select_tokens_and_normalize() -> None:
    drafts = [
        WorkItemDraft(
            key="10.05.080.000",
            parent_key=None,
            work_item_type="Process",
            title="Depreciation",
            fields={
                "MSBPC.applicationfamily": "Business Central;  Finance and Operations",
                "MSBPC.products": "Business Central; NotAProduct",
            },
            source_file="bpc.xlsx",
            source_row=10,
        )
    ]
    result = prevalidate_catalog_drafts(drafts, _ir(), _mapping(), sanitize=True)
    assert drafts[0].fields["MSBPC.applicationfamily"] == (
        "Business Central; Finance and Operations"
    )
    assert result.multi_select_normalized >= 1
    assert result.counts.get("invalid_multi_select_token") == 1
    # Unknown token reported but value kept (suggested multi-select storage).
    assert "MSBPC.products" in drafts[0].fields


def test_prevalidate_strips_invalid_single_picklist() -> None:
    drafts = [
        WorkItemDraft(
            key="j1",
            parent_key=None,
            work_item_type="Job",
            title="Nightly",
            fields={"MSBPC.jobpurpose": "Recurring batch"},
            source_file="deliv.xlsx",
            source_row=3,
        )
    ]
    result = prevalidate_catalog_drafts(drafts, _ir(), _mapping(), sanitize=True)
    assert "MSBPC.jobpurpose" not in drafts[0].fields
    assert result.counts.get("invalid_picklist_value") == 1


def test_prevalidate_required_empty_when_applicable() -> None:
    drafts = [
        WorkItemDraft(
            key="m1",
            parent_key=None,
            work_item_type="Migration",
            title="Customers",
            fields={},
            source_file="deliv.xlsx",
            source_row=4,
        )
    ]
    result = prevalidate_catalog_drafts(drafts, _ir(), _mapping(), sanitize=True)
    # Data type is required with no template default → still reported.
    assert result.counts.get("required_empty") == 1
    assert "MSBPC.datatype" not in drafts[0].fields


def test_prevalidate_applies_template_defaults_for_required_empty() -> None:
    drafts = [
        WorkItemDraft(
            key="10.05.080.000",
            parent_key=None,
            work_item_type="Process",
            title="Depreciation",
            fields={},
            source_file="bpc.xlsx",
            source_row=10,
        )
    ]
    result = prevalidate_catalog_drafts(drafts, _ir(), _mapping(), sanitize=True)
    assert drafts[0].fields["MSBPC.businessprocessflowsource"] == "Microsoft"
    assert drafts[0].fields["MSBPC.catalogstatus"] == "10 - New"
    assert drafts[0].fields["MSBPC.continuous"] is False
    assert result.defaults_applied == 3
    assert result.counts.get("defaults_applied") == 3
    assert result.counts.get("required_empty") is None
