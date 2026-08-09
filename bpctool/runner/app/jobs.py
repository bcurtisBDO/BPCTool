"""In-memory job store for dry-run and apply jobs."""

from __future__ import annotations

import threading
import time
import uuid
from datetime import datetime, timezone
from typing import Any

from .apply_engine import run_apply
from .excel_ir import build_ir
from .models import (
    ApplyResult,
    DryRunRequest,
    DryRunResponse,
    JobCreateRequest,
    JobStatusResponse,
)
from .planner import build_dry_run_plan
from .timing import format_duration_ms

_lock = threading.Lock()
_jobs: dict[str, dict[str, Any]] = {}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_dry_run(request: DryRunRequest) -> DryRunResponse:
    ir = build_ir(
        request.excel_file,
        catalog_source_dir=request.catalog_source_dir,
        workbook_version=request.workbook_version,
        process_name=request.process_name,
        project_name=request.project_name,
    )
    return build_dry_run_plan(
        ir,
        update_policy=request.update_policy,
        confirm_process_update=request.confirm_process_update,
        confirm_project_update=request.confirm_project_update,
        known_process_exists=request.known_process_exists,
        known_project_exists=request.known_project_exists,
        step_filter=request.steps,
    )


def create_job(request: JobCreateRequest) -> JobStatusResponse:
    if request.mode == "apply" and not (request.pat or "").strip():
        raise ValueError("PAT is required for apply mode.")

    job_id = uuid.uuid4().hex[:12]
    created = _now()
    record = {
        "id": job_id,
        "status": "queued",
        "mode": request.mode,
        "created_at": created,
        "updated_at": created,
        "started_at": None,
        "finished_at": None,
        "duration_ms": None,
        "result": None,
        "apply_result": None,
        "error": None,
        "events": [
            {
                "timestamp": created,
                "type": "job-created",
                "message": f"Job created in {request.mode} mode",
            }
        ],
        "request": request,
    }
    with _lock:
        _jobs[job_id] = record

    if request.mode == "dry-run":
        _execute_job(job_id)
        return get_job(job_id)

    # Apply runs in a background thread so the API can return immediately for polling.
    thread = threading.Thread(target=_execute_job, args=(job_id,), daemon=True)
    thread.start()
    return get_job(job_id)


def _append_event(job_id: str, event: dict[str, Any]) -> None:
    with _lock:
        job = _jobs[job_id]
        payload = {"timestamp": _now(), **event}
        job["events"].append(payload)
        job["updated_at"] = payload["timestamp"]


def _execute_job(job_id: str) -> None:
    job_t0 = time.perf_counter()
    with _lock:
        job = _jobs[job_id]
        request: JobCreateRequest = job["request"]
        started = _now()
        job["status"] = "running"
        job["started_at"] = started
        job["updated_at"] = started
        job["events"].append(
            {
                "timestamp": started,
                "type": "job-started",
                "message": "Parsing Excel and building plan",
            }
        )

    try:
        if request.mode == "dry-run":
            result = run_dry_run(request)
            finished = _now()
            duration_ms = int((time.perf_counter() - job_t0) * 1000)
            with _lock:
                job = _jobs[job_id]
                job["result"] = result
                job["status"] = "succeeded" if result.ok else "failed"
                job["error"] = None if result.ok else "; ".join(result.errors)
                job["finished_at"] = finished
                job["duration_ms"] = duration_ms
                job["updated_at"] = finished
                job["events"].append(
                    {
                        "timestamp": finished,
                        "type": "job-finished",
                        "durationMs": duration_ms,
                        "message": (
                            f"Dry-run plan ready ({format_duration_ms(duration_ms)})"
                            if result.ok
                            else f"Dry-run blocked after {format_duration_ms(duration_ms)}: {job['error']}"
                        ),
                    }
                )
            return

        def on_event(event: dict[str, Any]) -> None:
            _append_event(job_id, event)

        apply_result: ApplyResult = run_apply(
            request,
            pat=request.pat or "",
            dry_run=bool(request.apply_dry_run),
            emit=on_event,
            step_filter=request.steps,
            catalog_limit=request.catalog_limit,
        )

        finished = _now()
        # Prefer apply-engine total (step wall time); fall back to job wall clock.
        duration_ms = apply_result.duration_ms
        if duration_ms is None:
            duration_ms = int((time.perf_counter() - job_t0) * 1000)

        with _lock:
            job = _jobs[job_id]
            job["apply_result"] = apply_result
            job["result"] = apply_result.plan
            job["status"] = "succeeded" if apply_result.ok else "failed"
            job["error"] = apply_result.error
            job["finished_at"] = finished
            job["duration_ms"] = duration_ms
            job["updated_at"] = finished
            job["events"].append(
                {
                    "timestamp": finished,
                    "type": "job-finished",
                    "durationMs": duration_ms,
                    "timings": apply_result.timings,
                    "message": (
                        f"Apply {'dry-run ' if apply_result.dry_run else ''}finished "
                        f"({format_duration_ms(duration_ms)})"
                        if apply_result.ok
                        else f"Apply failed after {format_duration_ms(duration_ms)}: {apply_result.error}"
                    ),
                }
            )
    except Exception as exc:  # noqa: BLE001 - surface to job status
        finished = _now()
        duration_ms = int((time.perf_counter() - job_t0) * 1000)
        with _lock:
            job = _jobs[job_id]
            job["status"] = "failed"
            job["error"] = str(exc)
            job["finished_at"] = finished
            job["duration_ms"] = duration_ms
            job["updated_at"] = finished
            job["events"].append(
                {
                    "timestamp": finished,
                    "type": "job-error",
                    "durationMs": duration_ms,
                    "message": f"{exc} (after {format_duration_ms(duration_ms)})",
                }
            )


def get_job(job_id: str) -> JobStatusResponse:
    with _lock:
        job = _jobs.get(job_id)
        if not job:
            raise KeyError(job_id)
        return JobStatusResponse(
            id=job["id"],
            status=job["status"],
            mode=job["mode"],
            created_at=job["created_at"],
            updated_at=job["updated_at"],
            started_at=job.get("started_at"),
            finished_at=job.get("finished_at"),
            duration_ms=job.get("duration_ms"),
            result=job["result"],
            apply_result=job["apply_result"],
            error=job["error"],
            events=list(job["events"]),
        )
