"""Retry and idempotency rules for AdoClient.request."""

from __future__ import annotations

import base64
import json

import pytest

from app import ado_client
from app.ado_client import AdoClient, AdoError, retry_delay_seconds

PAT = "x" * 52


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ado_client.time, "sleep", lambda _s: None)


def _client(monkeypatch: pytest.MonkeyPatch, responses: list) -> tuple[AdoClient, list]:
    client = AdoClient("https://dev.azure.com/contoso", PAT)
    calls: list[str] = []

    def fake_send(method, url, data, headers):
        calls.append(method)
        result = responses.pop(0)
        if isinstance(result, Exception):
            raise result
        return result

    monkeypatch.setattr(client, "_send", fake_send)
    return client, calls


def test_retry_delay_honors_retry_after_seconds_and_float() -> None:
    assert retry_delay_seconds("3", 0) == 3.0
    assert retry_delay_seconds("1.5", 0) == 1.5
    assert retry_delay_seconds("9999", 0) == ado_client.MAX_RETRY_DELAY_S


def test_retry_delay_backoff_is_jittered_and_bounded() -> None:
    for attempt in range(8):
        delay = retry_delay_seconds(None, attempt)
        base = min(30.0, 1.5 * (2**attempt))
        assert base * 0.75 <= delay <= base * 1.25


def test_get_retries_network_error_and_5xx(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(
        monkeypatch,
        [
            ConnectionResetError("reset"),
            (502, "Bad Gateway", None, b""),
            (200, "OK", None, b'{"ok": true}'),
        ],
    )
    assert client.get("/_apis/projects") == {"ok": True}
    assert calls == ["GET", "GET", "GET"]


def test_create_does_not_retry_network_error(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(monkeypatch, [ConnectionResetError("reset")])
    with pytest.raises(AdoError) as info:
        client.create_work_item("Demo", "Scenario", {"System.Title": "x"})
    assert info.value.outcome_unknown is True
    assert calls == ["PATCH"]


@pytest.mark.parametrize("status", [500, 502, 504])
def test_create_does_not_retry_5xx_and_marks_outcome_unknown(
    monkeypatch: pytest.MonkeyPatch, status: int
) -> None:
    client, calls = _client(monkeypatch, [(status, "Server Error", None, b"oops")])
    with pytest.raises(AdoError) as info:
        client.create_work_item("Demo", "Scenario", {"System.Title": "x"})
    assert info.value.status == status
    assert info.value.transient is True
    assert info.value.outcome_unknown is True
    assert "outcome unknown" in str(info.value)
    assert calls == ["PATCH"]


def test_create_400_is_not_outcome_unknown(monkeypatch: pytest.MonkeyPatch) -> None:
    client, _calls = _client(monkeypatch, [(400, "Bad Request", None, b"bad field")])
    with pytest.raises(AdoError) as info:
        client.create_work_item("Demo", "Scenario", {"System.Title": "x"})
    assert info.value.outcome_unknown is False


def test_add_parent_link_is_not_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(monkeypatch, [ConnectionResetError("reset")])
    with pytest.raises(AdoError) as info:
        client.add_parent_link("Demo", 5, 1)
    assert info.value.outcome_unknown is True
    assert calls == ["PATCH"]


def test_create_retries_throttle(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(
        monkeypatch,
        [
            (429, "Too Many Requests", {"Retry-After": "0.5"}, b""),
            (200, "OK", None, b'{"id": 42}'),
        ],
    )
    assert client.create_work_item("Demo", "Scenario", {"System.Title": "x"}) == {"id": 42}
    assert calls == ["PATCH", "PATCH"]


def test_203_sign_in_page_is_auth_error(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(
        monkeypatch, [(203, "Non-Authoritative Information", None, b"<html>sign in</html>")]
    )
    with pytest.raises(AdoError) as info:
        client.get("/_apis/projects")
    assert info.value.status == 401
    assert "PAT" in str(info.value)
    assert calls == ["GET"]


def test_pool_tunnels_https_through_env_proxy(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        ado_client, "getproxies", lambda: {"https": "http://bob:p%40ss@proxy.local:3128"}
    )
    monkeypatch.setattr(ado_client, "proxy_bypass", lambda _host: False)
    pool = ado_client._ConnectionPool(5)
    conn, http_proxy_headers = pool.get("https", "dev.azure.com")
    assert http_proxy_headers is None
    assert (conn.host, conn.port) == ("proxy.local", 3128)
    assert conn._tunnel_host == "dev.azure.com"
    assert conn._tunnel_port == 443
    expected = "Basic " + base64.b64encode(b"bob:p@ss").decode("ascii")
    assert conn._tunnel_headers["Proxy-Authorization"] == expected


def test_pool_connects_directly_when_proxy_bypassed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ado_client, "getproxies", lambda: {"https": "http://proxy.local:3128"})
    monkeypatch.setattr(ado_client, "proxy_bypass", lambda host: host == "dev.azure.com")
    conn, _ = ado_client._ConnectionPool(5).get("https", "dev.azure.com")
    assert conn.host == "dev.azure.com"
    assert getattr(conn, "_tunnel_host", None) is None


def test_non_retryable_status_raises_immediately(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _client(monkeypatch, [(400, "Bad Request", None, b"bad field")])
    with pytest.raises(AdoError) as info:
        client.get("/_apis/projects")
    assert info.value.status == 400
    assert "bad field" in str(info.value)
    assert calls == ["GET"]


def _record_sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    sleeps: list[float] = []
    monkeypatch.setattr(ado_client.time, "sleep", sleeps.append)
    return sleeps


def test_retry_after_on_success_pauses_the_next_request(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps = _record_sleeps(monkeypatch)
    client, calls = _client(
        monkeypatch,
        [
            (200, "OK", {"Retry-After": "4", "X-RateLimit-Delay": "1.2"}, b"{}"),
            (200, "OK", {}, b"{}"),
        ],
    )
    notices: list[str] = []
    client.on_throttle = notices.append
    client.get("/_apis/projects")
    assert sleeps == []
    client.get("/_apis/projects")
    assert calls == ["GET", "GET"]
    assert len(sleeps) == 1 and 3.5 < sleeps[0] <= 4.0
    assert len(notices) == 1
    assert "pausing all requests for 4 s" in notices[0]


def test_low_remaining_budget_spaces_requests(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps = _record_sleeps(monkeypatch)
    low = {"X-RateLimit-Limit": "200", "X-RateLimit-Remaining": "10"}
    client, _calls = _client(
        monkeypatch,
        [(200, "OK", low, b"{}"), (200, "OK", {}, b"{}"), (200, "OK", {}, b"{}")],
    )
    notices: list[str] = []
    client.on_throttle = notices.append
    for _ in range(3):
        client.get("/_apis/projects")
    assert len(sleeps) == 1 and 1.5 < sleeps[0] <= 2.0
    assert len(notices) == 1
    assert "nearly reached (10 of 200 left)" in notices[0]


def test_ample_budget_clears_spacing(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps = _record_sleeps(monkeypatch)
    client, _calls = _client(
        monkeypatch,
        [
            (200, "OK", {"X-RateLimit-Limit": "200", "X-RateLimit-Remaining": "30"}, b"{}"),
            (200, "OK", {}, b"{}"),
            (200, "OK", {"X-RateLimit-Limit": "200", "X-RateLimit-Remaining": "150"}, b"{}"),
            (200, "OK", {}, b"{}"),
            (200, "OK", {}, b"{}"),
        ],
    )
    for _ in range(5):
        client.get("/_apis/projects")
    # One request is spaced 0.5 s; once the budget recovers, none wait.
    assert len(sleeps) == 1 and 0.4 < sleeps[0] <= 0.5


def test_no_rate_headers_means_no_pause_or_notice(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps = _record_sleeps(monkeypatch)
    client, _calls = _client(monkeypatch, [(200, "OK", {}, b"{}"), (200, "OK", None, b"{}")])
    notices: list[str] = []
    client.on_throttle = notices.append
    client.get("/_apis/projects")
    client.get("/_apis/projects")
    assert sleeps == [] and notices == []


def test_throttle_pause_is_shared_by_every_thread(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps = _record_sleeps(monkeypatch)
    client, calls = _client(
        monkeypatch,
        [
            (429, "Too Many Requests", {"Retry-After": "3"}, b""),
            (200, "OK", {}, b"{}"),
        ],
    )
    client.get("/_apis/projects")
    assert calls == ["GET", "GET"]
    assert len(sleeps) == 1 and 2.5 < sleeps[0] <= 3.0
    # Sleep is stubbed, so the pause is still pending: another worker would wait it out too.
    client._gate.wait()
    assert len(sleeps) == 2 and 2.5 < sleeps[1] <= 3.0


def test_notice_repeats_at_most_once_a_minute() -> None:
    gate = ado_client._ThrottleGate()
    headers = {"X-RateLimit-Delay": "0.5", "X-RateLimit-Resource": "WorkItemTracking"}
    first = gate.observe(200, headers)
    assert first and "WorkItemTracking" in first
    assert gate.observe(200, headers) is None
    gate._last_notice -= ado_client._NOTICE_QUIET_S
    assert gate.observe(200, headers)


def _routed_client(monkeypatch: pytest.MonkeyPatch, routes: dict) -> tuple[AdoClient, list]:
    """``routes``: (method, path) → list of responses served in order (last one repeats)."""
    client = AdoClient("https://dev.azure.com/contoso", PAT)
    calls: list[tuple[str, str]] = []

    def fake_send(method, url, data, headers):
        path = url.split("dev.azure.com/contoso", 1)[1].split("?")[0]
        calls.append((method, path))
        queue = routes[(method, path)]
        result = queue.pop(0) if len(queue) > 1 else queue[0]
        if isinstance(result, Exception):
            raise result
        status, body = result
        return status, "", None, json.dumps(body).encode() if body is not None else b""

    monkeypatch.setattr(client, "_send", fake_send)
    return client, calls


_PROJECT = ("GET", "/_apis/projects/Demo")
_OPERATION = ("GET", "/_apis/operations/op-1")


def test_create_project_polls_the_operation_until_it_succeeds(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [(404, {}), (200, {"id": "p-1", "state": "wellFormed"})],
            ("POST", "/_apis/projects"): [(202, {"id": "op-1", "url": "https://x/_apis/operations/op-1"})],
            _OPERATION: [(200, {"status": "queued"}), (200, {"status": "inProgress"}), (200, {"status": "succeeded"})],
        },
    )
    assert client.create_project("Demo", "proc-1") == "p-1"
    assert calls == [_PROJECT, ("POST", "/_apis/projects"), _OPERATION, _OPERATION, _OPERATION, _PROJECT]


def test_create_project_is_not_retried_after_a_network_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ado_client, "PROJECT_MISSING_GRACE_S", 0)
    client, calls = _routed_client(
        monkeypatch, {_PROJECT: [(404, {})], ("POST", "/_apis/projects"): [ConnectionResetError("reset")]}
    )
    with pytest.raises(AdoError) as info:
        client.create_project("Demo", "proc-1")
    assert info.value.outcome_unknown is True
    assert "Re-run Project Creation" in str(info.value)
    assert calls.count(("POST", "/_apis/projects")) == 1


def test_create_project_reports_the_operation_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    client, _ = _routed_client(
        monkeypatch,
        {
            _PROJECT: [(404, {})],
            ("POST", "/_apis/projects"): [(202, {"id": "op-1"})],
            _OPERATION: [(200, {"status": "failed", "resultMessage": "Process is disabled."})],
        },
    )
    with pytest.raises(AdoError, match="could not create project 'Demo': Process is disabled."):
        client.create_project("Demo", "proc-1")


def test_create_project_conflict_waits_for_a_well_formed_project(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [
                (404, {}),
                (200, {"id": "p-1", "state": "createPending"}),
                (200, {"id": "p-1", "state": "wellFormed"}),
            ],
            ("POST", "/_apis/projects"): [(409, {"message": "exists"})],
        },
    )
    assert client.create_project("Demo", "proc-1") == "p-1"
    assert calls.count(_PROJECT) == 3


def test_create_project_times_out_with_a_plain_message(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ado_client, "PROJECT_CREATE_TIMEOUT_S", 6.0)
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [(404, {})],
            ("POST", "/_apis/projects"): [(202, {"id": "op-1"})],
            _OPERATION: [(200, {"status": "inProgress"})],
        },
    )
    with pytest.raises(AdoError, match="still creating project 'Demo'"):
        client.create_project("Demo", "proc-1")
    assert calls.count(_OPERATION) == ado_client._poll_count(6.0)


def test_create_project_500_looks_the_project_up(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [(404, {}), (200, {"id": "p-1", "state": "wellFormed"})],
            ("POST", "/_apis/projects"): [(500, {"message": "boom"})],
        },
    )
    assert client.create_project("Demo", "proc-1") == "p-1"
    assert calls.count(("POST", "/_apis/projects")) == 1


def test_create_project_waits_for_an_existing_project_still_being_created(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [
                (200, {"id": "p-1", "state": "createPending"}),
                (200, {"id": "p-1", "state": "createPending"}),
                (200, {"id": "p-1", "state": "wellFormed"}),
            ],
        },
    )
    assert client.create_project("Demo", "proc-1") == "p-1"
    assert calls == [_PROJECT, _PROJECT, _PROJECT]


def test_ready_project_id_times_out_while_project_is_still_being_created(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(ado_client, "PROJECT_CREATE_TIMEOUT_S", 6.0)
    client, _ = _routed_client(monkeypatch, {_PROJECT: [(200, {"id": "p-1", "state": "new"})]})
    states: list[str] = []
    with pytest.raises(AdoError, match="still creating project 'Demo'.*run again"):
        client.get_ready_project_id("Demo", on_wait=states.append)
    assert states == ["new"]


def test_ready_project_id_returns_well_formed_project_without_waiting(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client, calls = _routed_client(monkeypatch, {_PROJECT: [(200, {"id": "p-1", "state": "wellFormed"})]})
    assert client.get_ready_project_id("Demo", on_wait=lambda _s: pytest.fail("waited")) == "p-1"
    assert calls == [_PROJECT]


def test_ready_project_id_is_none_for_a_missing_project(monkeypatch: pytest.MonkeyPatch) -> None:
    client, _ = _routed_client(monkeypatch, {_PROJECT: [(404, {})]})
    assert client.get_ready_project_id("Demo") is None


def test_create_project_polling_stops_when_the_run_is_cancelled(monkeypatch: pytest.MonkeyPatch) -> None:
    client, calls = _routed_client(
        monkeypatch,
        {
            _PROJECT: [(404, {})],
            ("POST", "/_apis/projects"): [(202, {"id": "op-1"})],
            _OPERATION: [(200, {"status": "inProgress"})],
        },
    )
    cancel = {"now": False}

    def should_cancel() -> bool:
        if calls.count(_OPERATION) >= 2:
            cancel["now"] = True
        return cancel["now"]

    with pytest.raises(ado_client.RunCancelled, match="cancelled by user.*project 'Demo'"):
        client.create_project("Demo", "proc-1", should_cancel=should_cancel)
    assert calls.count(_OPERATION) == 2


def test_waiting_for_an_existing_project_stops_when_the_run_is_cancelled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client, calls = _routed_client(monkeypatch, {_PROJECT: [(200, {"id": "p-1", "state": "createPending"})]})
    with pytest.raises(ado_client.RunCancelled):
        client.get_ready_project_id("Demo", should_cancel=lambda: len(calls) >= 3)
    assert len(calls) == 3


def test_create_process_lists_processes_once(monkeypatch: pytest.MonkeyPatch) -> None:
    processes = {"value": [{"name": "Agile", "typeId": "agile-id"}, {"name": "Scrum", "typeId": "scrum-id"}]}
    client, calls = _routed_client(
        monkeypatch,
        {
            ("GET", "/_apis/work/processes"): [(200, processes)],
            ("POST", "/_apis/work/processes"): [(200, {"typeId": "new-id"})],
        },
    )
    assert client.create_process("BPC") == "new-id"
    assert calls == [("GET", "/_apis/work/processes"), ("POST", "/_apis/work/processes")]
    assert client.create_process("scrum") == "scrum-id"
