from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from .excel_ir import build_ir
from .fs_browser import list_directory, list_roots
from .jobs import create_job, get_job, run_dry_run
from .models import DryRunRequest, DryRunResponse, JobCreateRequest, JobStatusResponse

app = FastAPI(
    title="BPC Runner",
    description="Local Excel→IR→plan→apply engine for BPCTool (no external July scripts)",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Template is user-supplied (not bundled). Optional discovery:
# BPCTOOL_TEMPLATE, or same file name under the catalog folder.
DEFAULT_CATALOG = Path(os.environ.get("BPCTOOL_CATALOG", "/Users/bill/BPC Files"))
_TEMPLATE_NAMES = (
    "ADO template guideline (July).xlsx",
    "ADO template guideline.xlsx",
)


def _discover_template() -> Path | None:
    env = (os.environ.get("BPCTOOL_TEMPLATE") or "").strip()
    if env:
        path = Path(env).expanduser()
        return path if path.is_file() else None
    if DEFAULT_CATALOG.is_dir():
        for name in _TEMPLATE_NAMES:
            candidate = DEFAULT_CATALOG / name
            if candidate.is_file():
                return candidate
    return None


@app.get("/health")
def health() -> dict[str, str]:
    # Include writer fingerprints so the UI/logs can detect a stale runner.
    writers = Path(__file__).resolve().parent / "writers"
    def _mtime(name: str) -> str:
        path = writers / name
        return str(int(path.stat().st_mtime)) if path.exists() else "missing"

    return {
        "status": "ok",
        "teams_writer_mtime": _mtime("teams.py"),
        "backlog_writer_mtime": _mtime("backlog.py"),
    }


@app.get("/defaults")
def defaults() -> dict[str, str | None]:
    template = _discover_template()
    return {
        "excel_file": str(template) if template else None,
        "catalog_source_dir": str(DEFAULT_CATALOG) if DEFAULT_CATALOG.exists() else None,
    }


@app.get("/fs/roots")
def fs_roots() -> dict:
    return {"roots": list_roots()}


@app.get("/fs/list")
def fs_list(
    path: str | None = Query(default=None),
    directories_only: bool = Query(default=False),
) -> dict:
    try:
        return list_directory(path, directories_only=directories_only)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/plan/dry-run", response_model=DryRunResponse)
def dry_run(request: DryRunRequest) -> DryRunResponse:
    try:
        return run_dry_run(request)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/ir/parse")
def parse_ir(request: DryRunRequest) -> dict:
    try:
        return build_ir(
            request.excel_file,
            catalog_source_dir=request.catalog_source_dir,
            workbook_version=request.workbook_version,
            process_name=request.process_name,
            project_name=request.project_name,
        )
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/jobs", response_model=JobStatusResponse)
def post_job(request: JobCreateRequest) -> JobStatusResponse:
    try:
        return create_job(request)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/jobs/{job_id}", response_model=JobStatusResponse)
def job_status(job_id: str) -> JobStatusResponse:
    try:
        return get_job(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}") from exc
