"""Normalize Azure DevOps organization URLs (mirror of src/adoOrgUrl.js)."""

from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class ParsedOrgUrl:
    ok: bool
    org: str = ""
    organization_url: str = ""
    error: str = ""


def parse_ado_org_url(value: str) -> ParsedOrgUrl:
    raw = (value or "").strip()
    if not raw:
        return ParsedOrgUrl(ok=False, error="Azure DevOps org URL is required.")

    if "://" not in raw:
        raw = f"https://{raw}"

    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ParsedOrgUrl(ok=False, error="Org URL must be an http(s) URL.")

    host = parsed.netloc.lower()
    parts = [p for p in parsed.path.split("/") if p]

    if host.endswith("dev.azure.com"):
        if not parts:
            return ParsedOrgUrl(ok=False, error="Org URL must include the organization segment.")
        org = parts[0]
        return ParsedOrgUrl(
            ok=True,
            org=org,
            organization_url=f"https://dev.azure.com/{org}",
        )

    if host.endswith("visualstudio.com"):
        org = host.split(".")[0]
        if not org:
            return ParsedOrgUrl(ok=False, error="Could not parse organization from visualstudio.com URL.")
        return ParsedOrgUrl(
            ok=True,
            org=org,
            organization_url=f"https://dev.azure.com/{org}",
        )

    return ParsedOrgUrl(
        ok=False,
        error="Org URL must be a dev.azure.com or *.visualstudio.com organization URL.",
    )


def normalize_ado_org_url(value: str) -> str:
    parsed = parse_ado_org_url(value)
    if not parsed.ok:
        raise ValueError(parsed.error)
    return parsed.organization_url
