"""Shared pytest helpers. Template workbook is user-supplied (not shipped)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

_TEMPLATE_CANDIDATES = (
    "ADO template guideline (July).xlsx",
    "ADO template guideline.xlsx",
)


def resolve_template_path() -> Path | None:
    env = (os.environ.get("BPCTOOL_TEMPLATE") or "").strip()
    if env:
        path = Path(env).expanduser()
        return path if path.is_file() else None

    catalog = Path(os.environ.get("BPCTOOL_CATALOG", "/Users/bill/BPC Files")).expanduser()
    if catalog.is_dir():
        for name in _TEMPLATE_CANDIDATES:
            candidate = catalog / name
            if candidate.is_file():
                return candidate
    return None


@pytest.fixture
def template_path() -> Path:
    path = resolve_template_path()
    if path is None:
        pytest.skip(
            "ADO template guideline not found. Set BPCTOOL_TEMPLATE to the .xlsx path "
            "(or place it in the catalog folder)."
        )
    return path
