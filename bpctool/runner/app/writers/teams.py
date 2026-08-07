"""Upsert teams and area paths."""

from __future__ import annotations

from typing import Any, Callable
from urllib.parse import quote

from ..ado_client import AdoClient, AdoError

Emit = Callable[[str, str], None]


def apply_teams(
    client: AdoClient,
    ir: dict[str, Any],
    *,
    dry_run: bool,
    emit: Emit,
    root_area_path: str = "",
) -> dict[str, Any]:
    project = ir["targets"]["project_name"]
    stats = {"teams": 0, "areas": 0, "assignments": 0, "warnings": 0}
    root = (root_area_path or project).strip()

    if dry_run:
        emit(
            "teams",
            f"[dry-run] Would upsert {ir['counts']['teams']} teams and "
            f"{ir['counts']['area_paths']} area paths under '{root}'",
        )
        return stats

    project_id = client.get_project_id(project)
    if not project_id:
        raise AdoError(f'Project "{project}" not found for teams apply.')

    # Teams
    existing_teams = {}
    try:
        data = client.get(f"/_apis/projects/{quote(project_id, safe='')}/teams", api_version="7.1") or {}
        for team in data.get("value") or []:
            existing_teams[str(team.get("name") or "").strip().lower()] = team
    except AdoError as exc:
        emit("teams", f"Could not list teams: {exc}")

    for team in ir["project"]["teams"]:
        name = team["name"]
        if name.strip().lower() in existing_teams:
            stats["teams"] += 1
            continue
        try:
            client.post(
                f"/_apis/projects/{quote(project_id, safe='')}/teams",
                json_body={"name": name},
                api_version="7.1",
            )
            stats["teams"] += 1
        except AdoError as exc:
            if exc.status != 409:
                emit("teams", f"Team '{name}': {exc}")
                stats["warnings"] += 1
            else:
                stats["teams"] += 1

    # Area paths
    for area in ir["project"]["area_paths"]:
        path = area["path"]
        parts = [p for p in path.split("\\") if p]
        if parts and parts[0].lower() == project.lower():
            parts = parts[1:]
        if not parts:
            continue
        parent: list[str] = []
        for name in parts:
            current = parent + [name]
            if not _area_exists(client, project, current):
                try:
                    _create_area(client, project, parent, name)
                    stats["areas"] += 1
                except AdoError as exc:
                    if exc.status not in {409}:
                        emit("teams", f"Area {'/'.join(current)}: {exc}")
                        stats["warnings"] += 1
            parent = current

        team_name = (area.get("team") or "").strip()
        if team_name:
            relative = "\\".join(parts)
            try:
                _assign_team_area(client, project, team_name, relative)
                stats["assignments"] += 1
            except AdoError as exc:
                emit("teams", f"Assign {team_name} → {relative}: {exc}")
                stats["warnings"] += 1

    emit(
        "teams",
        f"Teams/areas finished: {stats['teams']} teams, {stats['areas']} areas, "
        f"{stats['assignments']} assignments",
    )
    return stats


def _area_exists(client: AdoClient, project: str, parts: list[str]) -> bool:
    path = "/".join(quote(p, safe="") for p in parts)
    try:
        client.get(f"/_apis/wit/classificationnodes/Areas/{path}", project=project, api_version="7.1")
        return True
    except AdoError as exc:
        if exc.status == 404:
            return False
        raise


def _create_area(client: AdoClient, project: str, parent_parts: list[str], name: str) -> None:
    if parent_parts:
        parent = "/".join(quote(p, safe="") for p in parent_parts)
        path = f"/_apis/wit/classificationnodes/Areas/{parent}"
    else:
        path = "/_apis/wit/classificationnodes/Areas"
    client.post(path, project=project, json_body={"name": name}, api_version="7.1")


def _assign_team_area(client: AdoClient, project: str, team_name: str, relative_path: str) -> None:
    default_path = f"{project}\\{relative_path}" if relative_path else project
    client.patch(
        f"/_apis/work/teamsettings/teamfieldvalues",
        project=f"{project}/{team_name}",
        json_body={
            "defaultValue": default_path,
            "values": [{"value": default_path, "includeChildren": True}],
        },
        api_version="7.1",
    )
