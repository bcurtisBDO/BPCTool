from pathlib import Path

import pytest
from fastapi import HTTPException

from app.fs_browser import is_network_path, list_directory, list_roots

NETWORK_PATHS = [
    r"\\attacker\share",
    "//attacker/share",
    r"\\?\UNC\attacker\share",
    r"\\.\pipe\x",
    r"\/attacker/share",
    "  \\\\attacker\\share",
]


def test_list_roots_includes_home():
    roots = list_roots()
    assert any(r["path"] == str(Path.home().resolve()) for r in roots)


def test_list_directory_home():
    listing = list_directory(str(Path.home()))
    assert listing["path"] == str(Path.home().resolve())
    assert isinstance(listing["entries"], list)


def test_list_directory_rejects_relative():
    try:
        list_directory("BPC Files")
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "absolute" in str(exc).lower()


@pytest.mark.parametrize("path", NETWORK_PATHS)
def test_network_paths_are_detected(path):
    assert is_network_path(path)


@pytest.mark.parametrize("path", ["/Users/me", r"C:\Users\me", "C:/Users/me", "~/BPC", "/", ""])
def test_local_paths_are_not_network_paths(path):
    assert not is_network_path(path)


@pytest.mark.parametrize("path", NETWORK_PATHS)
def test_list_directory_rejects_network_paths(path, monkeypatch):
    monkeypatch.setattr(Path, "resolve", lambda self, *a, **k: pytest.fail("network path was opened"))
    with pytest.raises(ValueError, match="Network paths"):
        list_directory(path)


def test_fs_list_endpoint_answers_400_for_network_paths():
    from app.main import fs_list

    with pytest.raises(HTTPException) as caught:
        fs_list(path=r"\\attacker\share", directories_only=False)
    assert caught.value.status_code == 400
    assert "Network paths" in caught.value.detail


@pytest.mark.parametrize("root", NETWORK_PATHS)
def test_outputs_endpoint_rejects_network_root(root, monkeypatch):
    from app.main import output_file

    monkeypatch.setattr(Path, "resolve", lambda self, *a, **k: pytest.fail("network path was opened"))
    with pytest.raises(HTTPException) as caught:
        output_file("org_Proj", "import-failures.csv", root=root)
    assert caught.value.status_code == 400
    assert "Network paths" in caught.value.detail
