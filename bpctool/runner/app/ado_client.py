"""Azure DevOps REST client used by apply writers."""

from __future__ import annotations

import base64
import json
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from .org_url import normalize_ado_org_url, parse_ado_org_url


class AdoError(RuntimeError):
    def __init__(self, message: str, *, status: int | None = None, transient: bool = False):
        super().__init__(message)
        self.status = status
        self.transient = transient


class AdoClient:
    def __init__(self, org_url: str, pat: str, *, api_version: str = "7.1") -> None:
        parsed = parse_ado_org_url(org_url)
        if not parsed.ok:
            raise ValueError(parsed.error)
        if not pat or len(pat.strip()) < 20:
            raise ValueError("PAT is required and should be at least 20 characters.")
        self.org = parsed.org
        self.organization_url = normalize_ado_org_url(org_url)
        token = base64.b64encode(f":{pat.strip()}".encode("utf-8")).decode("ascii")
        self._auth = f"Basic {token}"
        self.api_version = api_version

    def url(self, path: str, *, project: str | None = None, api_version: str | None = None) -> str:
        version = api_version or self.api_version
        clean = path if path.startswith("/") else f"/{path}"
        if project:
            # Allow "Project/Team" style paths used by teamsettings APIs.
            encoded_project = "/".join(quote(part, safe="") for part in project.split("/") if part)
            base = f"{self.organization_url}/{encoded_project}"
        else:
            base = self.organization_url
        sep = "&" if "?" in clean else "?"
        return f"{base}{clean}{sep}{urlencode({'api-version': version})}"

    def request(
        self,
        method: str,
        path: str,
        *,
        project: str | None = None,
        api_version: str | None = None,
        json_body: Any = None,
        content_type: str | None = None,
        retry_attempts: int = 5,
        absolute_url: str | None = None,
    ) -> Any:
        url = absolute_url or self.url(path, project=project, api_version=api_version)
        data = None
        headers = {
            "Authorization": self._auth,
            "Accept": "application/json",
        }
        if json_body is not None:
            data = json.dumps(json_body).encode("utf-8")
            headers["Content-Type"] = content_type or "application/json"

        last_error: Exception | None = None
        for attempt in range(retry_attempts):
            request = Request(url, data=data, headers=headers, method=method.upper())
            try:
                with urlopen(request, timeout=120) as response:
                    raw = response.read()
                    if not raw:
                        return None
                    return json.loads(raw.decode("utf-8"))
            except HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:500]
                transient = exc.code in {429, 503}
                message = f"ADO {exc.code} {exc.reason}: {body}"
                if not transient or attempt == retry_attempts - 1:
                    raise AdoError(message, status=exc.code, transient=transient) from exc
                retry_after = exc.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else (1.5 * (attempt + 1))
                time.sleep(delay)
                last_error = exc
            except URLError as exc:
                if attempt == retry_attempts - 1:
                    raise AdoError(f"Network error talking to Azure DevOps: {exc}", transient=True) from exc
                time.sleep(1.5 * (attempt + 1))
                last_error = exc
        raise AdoError(f"ADO request failed: {last_error}", transient=True)

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, json_body: Any = None, **kwargs: Any) -> Any:
        return self.request("POST", path, json_body=json_body, **kwargs)

    def patch(self, path: str, json_body: Any = None, **kwargs: Any) -> Any:
        return self.request("PATCH", path, json_body=json_body, **kwargs)

    def put(self, path: str, json_body: Any = None, **kwargs: Any) -> Any:
        return self.request("PUT", path, json_body=json_body, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Any:
        return self.request("DELETE", path, **kwargs)

    def list_processes(self) -> list[dict[str, Any]]:
        data = self.get("/_apis/work/processes", api_version="7.1-preview.2") or {}
        return list(data.get("value") or [])

    def get_process_id(self, process_name: str) -> str | None:
        target = process_name.strip().lower()
        for proc in self.list_processes():
            if str(proc.get("name") or "").strip().lower() == target:
                return str(proc.get("typeId"))
        return None

    def get_agile_process_id(self) -> str:
        for proc in self.list_processes():
            if str(proc.get("name") or "").strip().lower() == "agile":
                return str(proc["typeId"])
        raise AdoError("Built-in Agile process not found in organization.")

    def create_process(self, process_name: str) -> str:
        existing = self.get_process_id(process_name)
        if existing:
            return existing
        payload = {
            "name": process_name,
            "description": f"Custom process based on Agile: {process_name}",
            "parentProcessTypeId": self.get_agile_process_id(),
        }
        try:
            created = self.post("/_apis/work/processes", json_body=payload, api_version="7.1-preview.2")
            return str(created["typeId"])
        except AdoError as exc:
            if exc.status == 409:
                found = self.get_process_id(process_name)
                if found:
                    return found
            raise

    def list_projects(self) -> list[dict[str, Any]]:
        data = self.get("/_apis/projects", api_version="7.1-preview.4") or {}
        return list(data.get("value") or [])

    def get_project_id(self, project_name: str) -> str | None:
        target = project_name.strip().lower()
        for project in self.list_projects():
            if str(project.get("name") or "").strip().lower() == target:
                return str(project.get("id"))
        return None

    def create_project(
        self,
        project_name: str,
        process_id: str,
        *,
        description: str = "",
    ) -> str | None:
        existing = self.get_project_id(project_name)
        if existing:
            return existing
        payload = {
            "name": project_name,
            "description": description or "",
            "capabilities": {
                "versioncontrol": {"sourceControlType": "Git"},
                "processTemplate": {"templateTypeId": process_id},
            },
        }
        self.post("/_apis/projects", json_body=payload, api_version="7.1-preview.4")
        # Creation is async (202); poll briefly.
        for _ in range(30):
            time.sleep(2)
            found = self.get_project_id(project_name)
            if found:
                return found
        return self.get_project_id(project_name)

    def update_project_description(self, project_id: str, description: str) -> None:
        self.patch(
            f"/_apis/projects/{quote(project_id, safe='')}",
            json_body={"description": description},
            api_version="7.1-preview.4",
        )

    def list_process_wits(self, process_id: str) -> list[dict[str, Any]]:
        data = (
            self.get(
                f"/_apis/work/processes/{process_id}/workitemtypes",
                api_version="7.1-preview.2",
            )
            or {}
        )
        return list(data.get("value") or [])

    def create_work_item(
        self,
        project: str,
        work_item_type: str,
        fields: dict[str, Any],
        *,
        parent_id: int | None = None,
        dry_run: bool = False,
        markdown_format_fields: list[str] | None = None,
    ) -> dict[str, Any]:
        patch: list[dict[str, Any]] = []
        # ADO Toolkit preserve path: mark large-text fields as Markdown so they
        # render correctly instead of as plain text inside HTML controls.
        for ref in markdown_format_fields or []:
            if ref and fields.get(ref) not in (None, ""):
                patch.append(
                    {
                        "op": "add",
                        "path": f"/multilineFieldsFormat/{ref}",
                        "value": "Markdown",
                    }
                )
        for ref, value in fields.items():
            if value is None or value == "":
                continue
            patch.append({"op": "add", "path": f"/fields/{ref}", "value": value})
        if parent_id:
            parent_url = self.url(f"/_apis/wit/workItems/{parent_id}", project=project)
            # strip query for relation URL
            parent_url = parent_url.split("?")[0]
            patch.append(
                {
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                        "rel": "System.LinkTypes.Hierarchy-Reverse",
                        "url": parent_url,
                        "attributes": {"comment": "Imported parent link"},
                    },
                }
            )
        if dry_run:
            return {"id": None, "workItemType": work_item_type, "patch": patch}
        # ADO create-by-type URLs require a literal "$" before the type name
        # (e.g. /workitems/$Bug). In Python f-strings "$" is literal; "{...}" interpolates.
        return self.request(
            "PATCH",
            f"/_apis/wit/workitems/${quote(work_item_type, safe='')}",
            project=project,
            json_body=patch,
            content_type="application/json-patch+json",
        )
