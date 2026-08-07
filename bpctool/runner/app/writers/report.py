"""Emit HTML/JSON setup summary artifacts."""

from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

Emit = Callable[[str, str], None]


def apply_report(
    ir: dict[str, Any],
    *,
    step_results: dict[str, Any],
    output_dir: Path,
    org_url: str,
    emit: Emit,
    dry_run: bool = False,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "orgUrl": org_url,
        "processName": ir["targets"]["process_name"],
        "projectName": ir["targets"]["project_name"],
        "workbookFingerprint": ir["source"]["fingerprint"],
        "counts": ir["counts"],
        "stepResults": step_results,
        "richText": {
            "htmlFieldsInTemplate": ir["counts"].get("html_fields", 0),
            "convertMarkdownToHtml": (step_results.get("catalog") or {}).get(
                "convert_markdown_to_html", False
            ),
            "catalogMarkdownPreserved": (step_results.get("catalog") or {}).get(
                "markdown_preserved", 0
            ),
            "catalogMarkdownConverted": (step_results.get("catalog") or {}).get(
                "markdown_converted", 0
            ),
            "catalogHtmlPassthrough": (step_results.get("catalog") or {}).get(
                "html_passthrough", 0
            ),
        },
    }

    json_path = output_dir / "bpc-ado-setup-summary.json"
    html_path = output_dir / "bpc-ado-setup-summary.html"
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    rows = "".join(
        f"<tr><td>{html.escape(step)}</td><td><pre>{html.escape(json.dumps(result, indent=2))}</pre></td></tr>"
        for step, result in step_results.items()
    )
    counts = ir["counts"]
    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>BPC ADO setup summary</title>
  <style>
    body {{ font-family: Georgia, serif; margin: 2rem; background: #f7f4ef; color: #1f1a14; }}
    h1,h2 {{ font-family: "Segoe UI", sans-serif; }}
    table {{ border-collapse: collapse; width: 100%; background: white; }}
    th, td {{ border: 1px solid #d6cfc4; padding: 0.5rem 0.75rem; vertical-align: top; }}
    th {{ background: #efe8dc; text-align: left; }}
    pre {{ white-space: pre-wrap; margin: 0; font-size: 0.85rem; }}
    .meta {{ margin-bottom: 1.5rem; }}
  </style>
</head>
<body>
  <h1>BPC Azure DevOps setup summary</h1>
  <div class="meta">
    <p><strong>Process:</strong> {html.escape(ir["targets"]["process_name"])}</p>
    <p><strong>Project:</strong> {html.escape(ir["targets"]["project_name"])}</p>
    <p><strong>Org:</strong> {html.escape(org_url)}</p>
    <p><strong>Fingerprint:</strong> {html.escape(ir["source"]["fingerprint"])}</p>
    <p><strong>Mode:</strong> {"dry-run" if dry_run else "apply"}</p>
  </div>
  <h2>Counts</h2>
  <ul>
    <li>Work item types: {counts.get("work_item_types")}</li>
    <li>Fields: {counts.get("fields")} (HTML: {counts.get("html_fields")})</li>
    <li>Teams / areas: {counts.get("teams")} / {counts.get("area_paths")}</li>
    <li>Catalog rows: {counts.get("catalog_rows")} across {counts.get("catalog_files")} files</li>
  </ul>
  <h2>Rich text handling</h2>
  <p>
    Catalog import accepts both HTML and markdown-like Excel content for large-text fields.
    Default (ADO Toolkit style): preserve markdown and set multilineFieldsFormat=Markdown.
    Optional override converts markdown to HTML. Existing HTML is always passed through.
  </p>
  <ul>
    <li>Convert markdown → HTML: {"yes" if summary["richText"]["convertMarkdownToHtml"] else "no (preserve)"}</li>
    <li>Markdown preserved: {summary["richText"]["catalogMarkdownPreserved"]}</li>
    <li>Markdown converted: {summary["richText"]["catalogMarkdownConverted"]}</li>
    <li>HTML passthrough: {summary["richText"]["catalogHtmlPassthrough"]}</li>
  </ul>
  <h2>Step results</h2>
  <table>
    <thead><tr><th>Step</th><th>Result</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>
"""
    html_path.write_text(document, encoding="utf-8")
    emit("report", f"Wrote {html_path.name} and {json_path.name} under {output_dir}")
    return {"html_path": str(html_path), "json_path": str(json_path)}
