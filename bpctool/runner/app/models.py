from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class DryRunRequest(BaseModel):
    org_url: str = Field(min_length=3)
    process_name: str = Field(min_length=3)
    project_name: str = Field(min_length=3)
    project_description: str = Field(
        default="",
        description="Optional Azure DevOps project description set on create/update",
    )
    excel_file: str = Field(min_length=3, description="Path to ADO template guideline .xlsx")
    catalog_source_dir: str | None = Field(
        default=None,
        description="Folder with BPC catalog source workbooks (phase 5 inputs)",
    )
    workbook_version: str = ""
    update_policy: Literal[
        "require-confirmation",
        "always-update",
        "skip-existing",
        "create-only",
    ] = "require-confirmation"
    confirm_process_update: bool = False
    confirm_project_update: bool = False
    known_process_exists: bool | None = None
    known_project_exists: bool | None = None
    root_area_path: str = ""
    pat: str | None = Field(
        default=None,
        description="PAT required for apply mode; never logged",
    )
    steps: list[str] | None = Field(
        default=None,
        description="Optional subset of engine steps to run",
    )
    catalog_limit: int | None = Field(
        default=None,
        description="Optional cap on catalog drafts (useful for smoke applies)",
    )
    convert_markdown_to_html: bool = Field(
        default=False,
        description=(
            "ADO Toolkit-style override: convert markdown-like large-text Excel "
            "content to HTML. Default false preserves markdown and sets "
            "multilineFieldsFormat=Markdown on create."
        ),
    )


class PlanAction(BaseModel):
    step_id: str
    action: Literal["create", "update", "skip", "verify", "import", "report"]
    entity_type: str
    entity_name: str
    detail: str
    count: int = 1


class DryRunResponse(BaseModel):
    ok: bool
    ir_version: str
    excel_file: str
    catalog_source_dir: str | None
    workbook_fingerprint: str
    summary: dict[str, Any]
    steps: list[dict[str, Any]]
    actions: list[PlanAction]
    errors: list[str] = []
    warnings: list[str] = []


class ApplyResult(BaseModel):
    ok: bool
    dry_run: bool
    plan: DryRunResponse | None = None
    step_results: dict[str, Any] = {}
    output_dir: str | None = None
    error: str | None = None
    events: list[dict[str, Any]] = []


class JobCreateRequest(DryRunRequest):
    mode: Literal["dry-run", "apply"] = "dry-run"
    apply_dry_run: bool = Field(
        default=False,
        description="When mode=apply, run writers without ADO mutations (preview artifacts only)",
    )


class JobStatusResponse(BaseModel):
    id: str
    status: Literal["queued", "running", "succeeded", "failed"]
    mode: str
    created_at: str
    updated_at: str
    result: DryRunResponse | None = None
    apply_result: ApplyResult | None = None
    error: str | None = None
    events: list[dict[str, Any]] = []
