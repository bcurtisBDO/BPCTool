from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .excel_ir import build_ir
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

DEFAULT_EXCEL = (
    Path(__file__).resolve().parents[2] / "fixtures" / "ADO template guideline (July).xlsx"
)
DEFAULT_CATALOG = Path("/Users/bill/BPC Files")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/defaults")
def defaults() -> dict[str, str | None]:
    return {
        "excel_file": str(DEFAULT_EXCEL) if DEFAULT_EXCEL.exists() else None,
        "catalog_source_dir": str(DEFAULT_CATALOG) if DEFAULT_CATALOG.exists() else None,
    }


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
