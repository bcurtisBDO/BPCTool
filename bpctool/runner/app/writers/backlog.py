"""Configure backlog behaviors and iteration paths."""

from __future__ import annotations

from typing import Any, Callable
from urllib.parse import quote

from ..ado_client import AdoClient, AdoError

Emit = Callable[[str, str], None]


def apply_backlog(
    client: AdoClient,
    ir: dict[str, Any],
    *,
    dry_run: bool,
    emit: Emit,
    process_id: str | None = None,
) -> dict[str, Any]:
    project = ir["targets"]["project_name"]
    process_name = ir["targets"]["process_name"]
    stats = {"behaviors": 0, "iterations": 0, "warnings": 0}

    if dry_run:
        emit(
            "backlog",
            f"[dry-run] Would configure {ir['counts']['backlogs']} backlogs and "
            f"{ir['counts']['iteration_paths']} iterations",
        )
        return stats

    process_id = process_id or client.get_process_id(process_name)
    if not process_id:
        raise AdoError(f'Process "{process_name}" not found for backlog apply.')

    existing = client.get(
        f"/_apis/work/processes/{process_id}/behaviors",
        api_version="7.1-preview.2",
    ) or {}
    by_name = {
        str(item.get("name") or "").strip().lower(): item for item in existing.get("value") or []
    }

    for backlog in ir["process"]["backlogs"]:
        name = backlog["name"]
        color = (backlog.get("color") or "0078D4").lstrip("#")
        payload = {
            "name": name,
            "color": color,
            "inherits": "System.PortfolioBacklogBehavior",
        }
        try:
            if name.strip().lower() in by_name:
                ref = by_name[name.strip().lower()].get("referenceName")
                if ref:
                    client.patch(
                        f"/_apis/work/processes/{process_id}/behaviors/{quote(ref, safe='')}",
                        json_body={"name": name, "color": color},
                        api_version="7.1-preview.2",
                    )
            else:
                client.post(
                    f"/_apis/work/processes/{process_id}/behaviors",
                    json_body=payload,
                    api_version="7.1-preview.2",
                )
            stats["behaviors"] += 1
        except AdoError as exc:
            emit("backlog", f"Backlog '{name}': {exc}")
            stats["warnings"] += 1

    for iteration in ir["project"]["iteration_paths"]:
        path = iteration["path"]
        parts = [p for p in path.split("\\") if p]
        if parts and parts[0].lower() == project.lower():
            parts = parts[1:]
        parent: list[str] = []
        for name in parts:
            current = parent + [name]
            if not _iteration_exists(client, project, current):
                try:
                    _create_iteration(client, project, parent, name)
                    stats["iterations"] += 1
                except AdoError as exc:
                    if exc.status != 409:
                        emit("backlog", f"Iteration {'/'.join(current)}: {exc}")
                        stats["warnings"] += 1
            parent = current

    emit(
        "backlog",
        f"Backlog apply finished: {stats['behaviors']} behaviors, {stats['iterations']} iterations",
    )
    return stats


def _iteration_exists(client: AdoClient, project: str, parts: list[str]) -> bool:
    path = "/".join(quote(p, safe="") for p in parts)
    try:
        client.get(
            f"/_apis/wit/classificationnodes/Iterations/{path}",
            project=project,
            api_version="7.1",
        )
        return True
    except AdoError as exc:
        if exc.status == 404:
            return False
        raise


def _create_iteration(client: AdoClient, project: str, parent_parts: list[str], name: str) -> None:
    if parent_parts:
        parent = "/".join(quote(p, safe="") for p in parent_parts)
        path = f"/_apis/wit/classificationnodes/Iterations/{parent}"
    else:
        path = "/_apis/wit/classificationnodes/Iterations"
    client.post(path, project=project, json_body={"name": name}, api_version="7.1")
