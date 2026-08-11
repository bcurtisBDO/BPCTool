"""Orchestrate IR → plan → apply/verify across engine steps."""

from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Any, Callable

from .ado_client import AdoClient
from .excel_ir import build_ir
from .models import ApplyResult, DryRunRequest, DryRunResponse
from .org_url import normalize_ado_org_url, parse_ado_org_url
from .planner import STEP_ORDER, build_dry_run_plan
from .timing import format_duration_ms, summarize_timings
from .writers import (
    apply_backlog,
    apply_catalog,
    apply_layout,
    apply_process,
    apply_project,
    apply_report,
    apply_teams,
)

Emit = Callable[[dict[str, Any]], None]


def _safe_part(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", (value or "").strip())
    return slug.strip("._-") or "ado"


def default_output_dir(org_url: str, project_name: str) -> Path:
    parsed = parse_ado_org_url(org_url)
    org = parsed.org if parsed.ok else "org"
    root = Path(__file__).resolve().parents[2] / "runner-out"
    return root / _safe_part(f"{org}_{project_name}")


def run_apply(
    request: DryRunRequest,
    *,
    pat: str,
    dry_run: bool,
    emit: Emit | None = None,
    step_filter: list[str] | None = None,
    catalog_limit: int | None = None,
) -> ApplyResult:
    events: list[dict[str, Any]] = []
    timings: list[dict[str, Any]] = []
    run_started = time.perf_counter()

    def _emit(event: dict[str, Any]) -> None:
        events.append(event)
        if emit:
            emit(event)

    def step_emit(step_id: str, message: str) -> None:
        _emit({"type": "step-progress", "stepId": step_id, "message": message})

    ir = build_ir(
        request.excel_file,
        catalog_source_dir=request.catalog_source_dir,
        workbook_version=request.workbook_version,
        process_name=request.process_name,
        project_name=request.project_name,
    )
    ir.setdefault("targets", {})["project_description"] = (
        request.project_description or ""
    ).strip()
    plan = build_dry_run_plan(
        ir,
        update_policy=request.update_policy,
        confirm_process_update=request.confirm_process_update,
        confirm_project_update=request.confirm_project_update,
        known_process_exists=request.known_process_exists,
        known_project_exists=request.known_project_exists,
        step_filter=step_filter,
    )
    if not plan.ok:
        return ApplyResult(
            ok=False,
            dry_run=dry_run,
            plan=plan,
            step_results={},
            output_dir=None,
            error="; ".join(plan.errors),
            events=events,
            duration_ms=0,
            timings=[],
        )

    org_url = normalize_ado_org_url(request.org_url)
    output_dir = default_output_dir(org_url, request.project_name)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Dry-run apply never calls Azure DevOps; client is only created for live apply.
    client = None if dry_run else AdoClient(org_url, pat)
    step_results: dict[str, Any] = {}
    process_id: str | None = None

    planned = {step["id"]: step for step in plan.steps}
    selected = step_filter or STEP_ORDER

    _emit({"type": "apply-started", "message": f"Starting {'dry-run apply' if dry_run else 'apply'}"})

    try:
        # Live process/layout/project requires DevLabs Multivalue extension (UI also preflights).
        setup_steps = {"process", "layout", "project"}
        needs_multivalue = any(
            step_id in setup_steps
            and (planned.get(step_id) or {}).get("planned_action") != "skip"
            for step_id in selected
        )
        if client is not None and needs_multivalue:
            _emit(
                {
                    "type": "preflight",
                    "message": "Checking DevLabs Multivalue control extension…",
                }
            )
            client.require_multivalue_extension()
            _emit(
                {
                    "type": "preflight",
                    "message": "DevLabs Multivalue control extension is installed.",
                }
            )

        for step_id in selected:
            step = planned.get(step_id)
            if not step:
                continue
            action = step.get("planned_action")
            if action == "skip":
                step_results[step_id] = {"skipped": True, "duration_ms": 0}
                timings.append({"stepId": step_id, "durationMs": 0, "skipped": True})
                _emit(
                    {
                        "type": "step-skipped",
                        "stepId": step_id,
                        "durationMs": 0,
                        "message": f"Skipped {step_id} by plan/policy",
                    }
                )
                continue

            _emit(
                {
                    "type": "step-started",
                    "stepId": step_id,
                    "message": f"Starting {step_id} ({action})",
                }
            )
            step_started = time.perf_counter()

            if step_id == "process":
                result = apply_process(client, ir, dry_run=dry_run, emit=step_emit)
                process_id = result.get("process_id")
                if not dry_run and client and not process_id:
                    process_id = client.get_process_id(request.process_name)
            elif step_id == "layout":
                result = apply_layout(
                    client, ir, dry_run=dry_run, emit=step_emit, process_id=process_id
                )
            elif step_id == "project":
                result = apply_project(
                    client, ir, dry_run=dry_run, emit=step_emit, process_id=process_id
                )
            elif step_id == "teams":
                root = request.root_area_path or request.project_name
                result = apply_teams(
                    client, ir, dry_run=dry_run, emit=step_emit, root_area_path=root
                )
            elif step_id == "backlog":
                result = apply_backlog(
                    client, ir, dry_run=dry_run, emit=step_emit, process_id=process_id
                )
            elif step_id == "catalog":
                result = apply_catalog(
                    client,
                    ir,
                    dry_run=dry_run,
                    emit=step_emit,
                    output_dir=output_dir,
                    limit=catalog_limit,
                    convert_markdown_to_html=bool(request.convert_markdown_to_html),
                    parallel_workers=int(
                        getattr(request, "catalog_parallel_workers", 4) or 4
                    ),
                )
            elif step_id == "report":
                result = apply_report(
                    ir,
                    step_results=step_results,
                    output_dir=output_dir,
                    org_url=org_url,
                    emit=step_emit,
                    dry_run=dry_run,
                )
            else:
                result = {"skipped": True, "reason": f"Unknown step {step_id}"}

            duration_ms = int((time.perf_counter() - step_started) * 1000)
            if isinstance(result, dict):
                result = {**result, "duration_ms": duration_ms}
            step_results[step_id] = result
            timings.append(
                {"stepId": step_id, "durationMs": duration_ms, "skipped": False}
            )
            _emit(
                {
                    "type": "step-completed",
                    "stepId": step_id,
                    "durationMs": duration_ms,
                    "message": f"Finished {step_id} ({format_duration_ms(duration_ms)})",
                    "result": result,
                }
            )

        # Ensure report exists even if filtered out mid-run
        if "report" not in step_results and (not step_filter or "report" in selected):
            step_started = time.perf_counter()
            report_result = apply_report(
                ir,
                step_results=step_results,
                output_dir=output_dir,
                org_url=org_url,
                emit=step_emit,
                dry_run=dry_run,
            )
            duration_ms = int((time.perf_counter() - step_started) * 1000)
            step_results["report"] = {**report_result, "duration_ms": duration_ms}
            timings.append(
                {"stepId": "report", "durationMs": duration_ms, "skipped": False}
            )

        total_ms = int((time.perf_counter() - run_started) * 1000)
        summary_text = summarize_timings(timings, total_ms=total_ms)
        _emit(
            {
                "type": "run-summary",
                "durationMs": total_ms,
                "timings": timings,
                "message": f"Run timing:\n{summary_text}",
            }
        )

        return ApplyResult(
            ok=True,
            dry_run=dry_run,
            plan=plan,
            step_results=step_results,
            output_dir=str(output_dir),
            error=None,
            events=events,
            duration_ms=total_ms,
            timings=timings,
        )
    except Exception as exc:  # noqa: BLE001
        total_ms = int((time.perf_counter() - run_started) * 1000)
        _emit({"type": "job-error", "message": str(exc), "durationMs": total_ms})
        if timings:
            _emit(
                {
                    "type": "run-summary",
                    "durationMs": total_ms,
                    "timings": timings,
                    "message": (
                        f"Run timing (failed after {format_duration_ms(total_ms)}):\n"
                        f"{summarize_timings(timings, total_ms=total_ms)}"
                    ),
                }
            )
        return ApplyResult(
            ok=False,
            dry_run=dry_run,
            plan=plan,
            step_results=step_results,
            output_dir=str(output_dir),
            error=str(exc),
            events=events,
            duration_ms=total_ms,
            timings=timings,
        )
