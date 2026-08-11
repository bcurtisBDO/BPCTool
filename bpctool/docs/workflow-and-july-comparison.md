# BPCTool workflow & July comparison

Engine order from `STEP_ORDER` in `runner/app/planner.py`. ADO paths via runner writers + `ado_client.py` / `catalog_runtime.py`. Comparison vs Microsoft July Azure DevOps Python scripts (phases 1–6).

BPCTool does **not** spawn those scripts — it reimplements the intent with Excel → IR → plan → apply.

**Assessment date:** 2026-08-11. Catalog ops and template matrix (`X` / `H`) match July Script 2 / Phase 5 behavior as summarized below.

---

## Workflow diagram

```text
Multivalue preflight (extmgmt)
        │
        ▼
   process  →  layout  →  project  →  teams  →  backlog  →  catalog  →  report
   WITs/fields   pages     create     areas     behaviors   parallel+     local
   picklists     controls  / bind     assign    iterations  resume+       artifacts
                                                            backfill
```

| Step | Purpose |
|------|---------|
| **Preflight** | Require DevLabs Multivalue on the org (live process / layout / project only) |
| **process** | Inherited process, WITs, picklists, custom fields |
| **layout** | Pages, groups, controls (`HtmlFieldControl`, MultivalueContribution) |
| **project** | Create or bind project to process |
| **teams** | Teams + area paths (July Script 3 semantics) |
| **backlog** | Backlog behaviors, WIT assignment, iterations, team settings (July Script 4) |
| **catalog** | Import catalog workbooks: prevalidate → parent-aware parallel create → resume → parent-link backfill |
| **report** | Local HTML/JSON summary under `runner-out/` |

**Live apply only:** Multivalue preflight runs when process, layout, or project is selected and Apply dry-run is off. **Preview plan** and **Apply dry-run** skip ADO mutation (and the Multivalue UI gate). **Report** never calls ADO. Full / dependency-aware runs enforce the sequence above; selected-step mode can run a single card alone.

Recommended hard sequence (planner): `process → layout → verify → project → teams → backlog → catalog → report`.

### Execution modes (UI)

| Mode | Role |
|------|------|
| **Runner** (default) | Live Excel → IR → plan → apply via local FastAPI (`/api/jobs`) |
| **API** | Live ADO **reads** only (`/ado-proxy`) — credential proof / inventory; not process/layout/catalog apply |
| **Simulate** | Local stubs for orchestration testing |

Catalog/report have no API-mode executor; setup apply is Runner-only.

---

## Template matrix: X vs H (current assessment)

On the July **ADO template guideline** workbook, sheet **Work item types**, cells in the field-label grid (roughly `K2:FU44`) mark which fields apply to each WIT.

| Flag | July Script 2 | BPCTool (`excel_ir` / layout) |
|------|---------------|-------------------------------|
| **X** | Applicable — add field to WIT and place layout control | Same — collected into `applicable_field_labels` |
| **H** | Ignored (not `"X"`) — no add / no layout bind | Same — skipped |
| empty / other | Skipped | Skipped |

July only continues when `wit_field_flags.get(field_label) == "X"`. There is no special path for `H`. In the July guideline file, `H` is rare vs `X` and typically marks **system effort/build fields** (e.g. Completed Work, Activity, Original Estimate) as present/hidden on the type for authors — **not** an instruction for the layout script.

**Verdict:** Parity — both tools treat only `X` as actionable for process/layout field binding.

---

## Catalog Import (current assessment)

Aligned with July Phase 5 on the operational import model; still create-only for **field** updates (no WIP upsert).

| Capability | Behavior |
|------------|----------|
| **Hierarchy** | Title 1..N outline (ADO CSV / BPC guidance). Only `System.LinkTypes.Hierarchy-Reverse` is created — same as July (no Related / Predecessor / etc.) |
| **Parallelism** | Parent-aware ready queue + ThreadPool (UI **Threads** → `catalog_parallel_workers`, default 4, clamp 1–16). Children wait until the parent id exists |
| **Resume** | Load existing `ado-id-map.csv`; skip keys already imported; append new rows |
| **Parent-link backfill** | After create, `GET` relations + `PATCH` missing Hierarchy-Reverse; writes `backfill-links-report.csv` (`linked` / `already_linked` / `conflict_existing_parent` / `failed`) |
| **Failures** | If a parent never imports, children fail with `Parent not imported` (not created unlinked) |
| **Prevalidate** | Local sanitize before create (`import-prevalidate.json`): strip bad Area Path / Test Case State=New, case-insensitive picklist normalize, required-field defaults, empty Description omitted (no synthetic placeholder) |
| **Not done** | WIT `$batch` / native CSV bulk upload; HTTP connection pooling; WIP field upsert against existing work items |

**Performance note:** Parallel workers cut wall time vs the former 1×N serial create loop (often several× when network-bound). Start at 2–8 workers; higher counts risk ATCPU/429. Chunked WIT `$batch` would reduce round-trips further but is not implemented.

Key modules: `writers/catalog.py`, `catalog_runtime.py`, `ado_client.create_work_item` / `get_parent_id` / `add_parent_link`.

---

## Local runner APIs

Vite proxies `/api/*` → FastAPI on `127.0.0.1:8787`.

| Endpoint | Role |
|----------|------|
| `GET /health` | Liveness + writer mtimes |
| `GET /defaults` | Discover template / catalog paths |
| `POST /plan/dry-run` | Excel → IR → plan (**Preview plan**) |
| `POST /jobs` | Start apply or apply dry-run |
| `GET /jobs/{id}` | Poll events / step results |
| `GET /fs/roots`, `GET /fs/list` | Path picker Browse… |
| `POST /ir/parse` | Full IR dump (manual; UI does not call) |

Job body field for catalog parallelism: `catalog_parallel_workers` (1–16; UI Threads).

Browser inventory reads use `/ado-proxy/{org}` → `dev.azure.com`. Extension check/install uses `/extmgmt-proxy/{org}` → `extmgmt.dev.azure.com`.

---

## Azure DevOps APIs per step

Hosts:

- `https://dev.azure.com/{org}` — Process, WIT, Project, Work
- `https://extmgmt.dev.azure.com/{org}` — Multivalue extension management

| Step | Runner entry | Primary REST surface |
|------|--------------|----------------------|
| **Preflight** | UI Connection / Run gate; `require_multivalue_extension` | `GET\|POST /_apis/extensionmanagement/installedextensionsbyname/ms-devlabs/vsts-extensions-multivalue-control` (`7.1-preview.1`) |
| **process** | `POST /api/jobs` → `apply_process` | `GET\|POST /_apis/work/processes` · WIT create/PATCH · `GET\|POST\|PUT /_apis/work/processes/lists` · `GET\|POST\|PATCH /_apis/wit/fields` |
| **layout** | `apply_layout` | GET layout · POST pages/groups/controls · POST `…/workItemTypes/{wit}/fields` · MultivalueContribution / HtmlFieldControl |
| **project** | `apply_project` | GET processes · `GET\|POST /_apis/projects` · `PATCH /_apis/projects/{id}` (description) |
| **teams** | `apply_teams` (July Script 3) | `GET\|POST …/projects/{id}/teams` · `GET\|POST` classificationnodes/Areas · `PATCH` teamsettings/teamfieldvalues |
| **backlog** | `apply_backlog` (July Script 4) | Process behaviors (GET/PUT/POST/DELETE) · WIT↔behavior · Iterations nodes · `GET\|PATCH` teamsettings · team iterations |
| **catalog** | `apply_catalog` + prevalidate + `catalog_runtime` | Parallel `PATCH …/wit/workitems/$Type` (fields + optional Markdown format + optional Hierarchy-Reverse); resume via `ado-id-map.csv`; backfill `GET …?$expand=Relations` + `PATCH …/workitems/{id}` for missing parent links |
| **report** | `apply_report` | None — writes `bpc-ado-setup-summary.json` / `.html` under `runner-out/<org>_<project>/` |

Key sources: `runner/app/planner.py`, `apply_engine.py`, `ado_client.py`, `catalog_runtime.py`, `writers/*.py`.

---

## Phase ↔ step map

| July phase script | BPCTool engine step |
|-------------------|---------------------|
| `1_ADO_Creation_Script.py` (process half) | **process** |
| `2_ADO_Page_Layout_Script_Threaded.py` | **layout** |
| `1_ADO_Creation_Script.py` (project half) | **project** (only after layout) |
| `3_ADO_Teams_Areas_Script.py` | **teams** |
| `4_ADO_Backlog_Config_Script.py` | **backlog** |
| `5_BPC_Catalog_Import.py` (+ `bpc_ado_import`) | **catalog** |
| `6_Generate_HTML_Report.py` | **report** |

---

## Microsoft July scripts vs BPCTool

| Area | July scripts | BPCTool | Verdict |
|------|--------------|---------|---------|
| **Orchestration** | `setup_wizard` shells out to six `.py` scripts via env vars (subprocess) | In-process writers in local FastAPI runner; React UI posts `/api/jobs` and polls events | Improved / ported |
| **Sequence** | Phase 1 creates process + project together; layout is a later phase | Hard gate **process → layout → project** (layout before any project on full runs) | Improved / ported |
| **Excel handling** | Each script re-reads Excel during mutation | Parse once to IR → plan → apply; fingerprint + dry-run plan preview | Improved / ported |
| **WIT×field matrix (`X`/`H`)** | Script 2: only `X` adds field/layout; `H` ignored | IR/`applicable_field_labels`: only `X`; `H` ignored | Parity |
| **Multivalue extension** | Layout binds Multivalue; install often assumed / Marketplace-manual | **Required** for process/layout/project; Connection check + optional API install; dry-run skips gate | Stricter |
| **Process / fields / picklists** | Script 1 creates inherited process, WITs, fields, picklists | Ported via `apply_process`; multi-select → suggested picklists (`isSuggested`) | Improved / ported |
| **Page layout** | Script 2 threaded layout + DevLabs MultivalueContribution | `apply_layout` mirrors Script 2 patterns (HTML group create, control retries) | Improved / ported |
| **Teams & areas** | Script 3 teams, L1–L4 areas, `set_team_area` | `apply_teams` — July semantics (first-row default area, `includeChildren` false by default) | Improved / ported |
| **Backlog & iterations** | Script 4 Parts 1–4: behaviors, WIT assign, defaults, team iterations | `apply_backlog` — rename/heal levels, WIT↔behavior, iterations, team settings | Improved / ported |
| **Catalog hierarchy** | Parent-child Hierarchy-Reverse only | Same — Title 1..N; no other WIT relation types | Parity |
| **Catalog parallelism** | `--catalog-parallel-workers` parent-aware pool | UI **Threads** / `catalog_parallel_workers` parent-aware pool | Improved / ported |
| **Catalog resume** | Skip keys in `ado-id-map.csv` on rerun | Same append/skip resume model | Improved / ported |
| **Catalog parent backfill** | `backfill-links` CLI (+ statuses) | Automatic post-create backfill → `backfill-links-report.csv` | Improved / ported |
| **Catalog prevalidate** | Phase 5 sanitizes / maps before create | Local prevalidate + case-insensitive picklist rewrite; empty Description omitted | Improved / ported |
| **Catalog field updates** | Create/import mode; limited recovery updates | Create-only fields (no WIP upsert) | Near parity / residual |
| **Report** | Script 6 HTML summary from artifacts | Local HTML/JSON under `runner-out/` (no ADO calls) | Improved / ported |
| **UI execution modes** | N/A (CLI scripts) | Runner = apply; API = reads only; Simulate = stubs | Improved / ported |
| **Edge-case parity** | Full script surface + many ADO quirk workarounds | July-shaped, not line-for-line; residual: system WIT disable fragility, field 404 on re-run, Deliverables picklist mismatches | Gap / residual |
| **Observability / UX** | Per-script console/files; limited structured UI | Job events, Run timing, plan preview, prevalidate / failures / id-map / backfill artifacts | Improved / ported |

### Known residual vs July

- Not every July quirk is ported (state recovery paths, deprecated/deleted cascade filters, print/recovery-field options, etc.).
- Catalog fields remain **create-only** (no bulk WIP upsert). Resume skips existing keys; it does not refresh field values.
- No WIT `$batch` or native Boards CSV bulk path yet (further throughput option). No HTTP connection pooling on the runner client yet.
- Inherited system WIT disable can still fail in the Process API (manual ADO UI fallback).
- Re-run Process may log non-fatal `MSBPC.*` field 404s when org fields already exist (Update API is lock/undelete only).

See also: [USER_GUIDE.md](../USER_GUIDE.md) (usage), [CHANGELOG.md](../CHANGELOG.md) (standalone July replacement + residual risk), [reference/MSBPC-Jul26-analysis.md](./reference/MSBPC-Jul26-analysis.md) (post-create process snapshot).
