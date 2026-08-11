# BPCTool workflow & July comparison

Engine order from `STEP_ORDER` in `runner/app/planner.py`. ADO paths via runner writers + `ado_client.py`. Comparison vs Microsoft July Azure DevOps Python scripts (phases 1–6).

BPCTool does **not** spawn those scripts — it reimplements the intent with Excel → IR → plan → apply.

---

## Workflow diagram

```text
Multivalue preflight (extmgmt)
        │
        ▼
   process  →  layout  →  project  →  teams  →  backlog  →  catalog  →  report
   WITs/fields   pages     create     areas     behaviors   create-only   local
   picklists     controls  / bind     assign    iterations  work items    artifacts
```

| Step | Purpose |
|------|---------|
| **Preflight** | Require DevLabs Multivalue on the org (live process / layout / project only) |
| **process** | Inherited process, WITs, picklists, custom fields |
| **layout** | Pages, groups, controls (`HtmlFieldControl`, MultivalueContribution) |
| **project** | Create or bind project to process |
| **teams** | Teams + area paths (July Script 3 semantics) |
| **backlog** | Backlog behaviors, WIT assignment, iterations, team settings (July Script 4) |
| **catalog** | Import catalog workbooks (create-only) |
| **report** | Local HTML/JSON summary under `runner-out/` |

**Live apply only:** Multivalue preflight runs when process, layout, or project is selected and Apply dry-run is off. **Preview plan** and **Apply dry-run** skip ADO mutation (and the Multivalue UI gate). **Report** never calls ADO. Full / dependency-aware runs enforce the sequence above; selected-step mode can run a single card alone.

Recommended hard sequence (planner): `process → layout → verify → project → teams → backlog → catalog → report`.

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
| **catalog** | `apply_catalog` + prevalidate | `PATCH /{project}/_apis/wit/workitems/${type}` (JSON Patch + optional Markdown format + parent relation) |
| **report** | `apply_report` | None — writes `bpc-ado-setup-summary.json` / `.html` under `runner-out/<org>_<project>/` |

Key sources: `runner/app/planner.py`, `apply_engine.py`, `ado_client.py`, `writers/*.py`.

---

## Phase ↔ step map

| July phase script | BPCTool engine step |
|-------------------|---------------------|
| `1_ADO_Creation_Script.py` (process half) | **process** |
| `2_ADO_Page_Layout_Script_Threaded.py` | **layout** |
| `1_ADO_Creation_Script.py` (project half) | **project** (only after layout) |
| `3_ADO_Teams_Areas_Script.py` | **teams** |
| `4_ADO_Backlog_Config_Script.py` | **backlog** |
| `5_BPC_Catalog_Import.py` | **catalog** |
| `6_Generate_HTML_Report.py` | **report** |

---

## Microsoft July scripts vs BPCTool

| Area | July scripts | BPCTool | Verdict |
|------|--------------|---------|---------|
| **Orchestration** | `setup_wizard` shells out to six `.py` scripts via env vars (subprocess) | In-process writers in local FastAPI runner; React UI posts `/api/jobs` and polls events | Improved / ported |
| **Sequence** | Phase 1 creates process + project together; layout is a later phase | Hard gate **process → layout → project** (layout before any project on full runs) | Improved / ported |
| **Excel handling** | Each script re-reads Excel during mutation | Parse once to IR → plan → apply; fingerprint + dry-run plan preview | Improved / ported |
| **Multivalue extension** | Layout binds Multivalue; install often assumed / Marketplace-manual | **Required** for process/layout/project; Connection check + optional API install; dry-run skips gate | Stricter |
| **Process / fields / picklists** | Script 1 creates inherited process, WITs, fields, picklists | Ported via `apply_process`; multi-select → suggested picklists (`isSuggested`) | Improved / ported |
| **Page layout** | Script 2 threaded layout + DevLabs MultivalueContribution | `apply_layout` mirrors Script 2 patterns (HTML group create, control retries) | Improved / ported |
| **Teams & areas** | Script 3 teams, L1–L4 areas, `set_team_area` | `apply_teams` — July semantics (first-row default area, `includeChildren` false by default) | Improved / ported |
| **Backlog & iterations** | Script 4 Parts 1–4: behaviors, WIT assign, defaults, team iterations | `apply_backlog` — rename/heal levels, WIT↔behavior, iterations, team settings | Improved / ported |
| **Catalog import** | Script 5 resumable ID map / retries (strongest July ops pattern) | All matching `.xlsx`; Title 1..N parents; prevalidate; **create-only** (no WIP upsert) | Gap / residual |
| **Report** | Script 6 HTML summary from artifacts | Local HTML/JSON under `runner-out/` (no ADO calls) | Improved / ported |
| **Edge-case parity** | Full script surface + many ADO quirk workarounds | July-shaped, not line-for-line; residual: system WIT disable fragility, field 404 on re-run, Deliverables picklist mismatches | Gap / residual |
| **Observability / UX** | Per-script console/files; limited structured UI | Job events, Run timing, plan preview, `import-prevalidate` / failures / id-map artifacts | Improved / ported |

### Known residual vs July

- Not every July quirk is ported.
- Catalog is **create-only** (July Script 5 resume/upsert patterns are only partially mirrored via id-map artifacts).
- Inherited system WIT disable can still fail in the Process API (manual ADO UI fallback).
- Re-run Process may log non-fatal `MSBPC.*` field 404s when org fields already exist (Update API is lock/undelete only).

See also: [USER_GUIDE.md](../USER_GUIDE.md) (usage), [CHANGELOG.md](../CHANGELOG.md) (standalone July replacement + residual risk), [reference/MSBPC-Jul26-analysis.md](./reference/MSBPC-Jul26-analysis.md) (post-create process snapshot).
