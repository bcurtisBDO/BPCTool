# Changelog

All notable changes to BPCTool (React UI + local runner) are documented here.

## 2026-08 — Docs: README UI screenshots

- Added `docs/images/` screenshots (Connection / Multivalue, workflow cards, run config, Catalog Threads + actions) linked from [`README.md`](./README.md#screenshots)

## 2026-08 — Docs: catalog parallel / resume / backfill

- [`docs/workflow-and-july-comparison.md`](./docs/workflow-and-july-comparison.md) updated for Catalog Import assessment (parallel workers, id-map resume, parent-link backfill, hierarchy-only relations, residual vs July)
- USER_GUIDE / README job field `catalog_parallel_workers`, artifacts, troubleshooting, quick reference

## 2026-08 — Catalog: parallel create, resume, parent-link backfill

- Catalog Import uses **parent-aware parallel workers** (UI **Threads**, default 4; clamp 1–16; July-style ready queue)
- **Resume** from existing `ado-id-map.csv` (skip keys already imported; append new rows)
- After create, **parent-link backfill** checks Hierarchy-Reverse and writes `backfill-links-report.csv` (link / already_linked / conflict / failed)
- Children wait until the parent id exists (no create-unlinked when parent failed — counted as `Parent not imported`)

## 2026-08 — Docs: Multivalue required + catalog notes

- Root README, app README, USER_GUIDE, and residual-risk notes state that DevLabs **Multivalue** is **required** for process / layout / project
- Documented empty Description omit, case-insensitive picklist prevalidate, `/extmgmt-proxy`, and Connection Check/Install

## 2026-08 — Catalog: no synthetic Description

- Catalog import no longer invents `System.Description` when the spreadsheet Description is empty (removed “Imported from … row N” placeholder)

## 2026-08 — Picklist case-insensitive prevalidate

- Catalog prevalidate matches single- and multi-select picklist values **case-insensitively** and rewrites to the template Picklists-sheet casing (e.g. `Organization Administration` → `Organization administration` for `MSBPC.module`)
- Counted as `picklist_case_normalized` in `import-prevalidate.json` (no longer stripped as `invalid_picklist_value`)

## 2026-08 — DevLabs Multivalue extension preflight

- Connection panel checks whether `ms-devlabs.vsts-extensions-multivalue-control` is installed on the org (via Extension Management API)
- If missing, Run prompts to install with the current PAT; decline or install failure blocks process / layout / project setup
- Live runner apply also requires the extension before those steps (defense in depth)
- Vite `/extmgmt-proxy` → `extmgmt.dev.azure.com`

## 2026-08 — Reference: post-create process analysis

- Added [`docs/reference/MSBPC-Jul26-analysis.md`](./docs/reference/MSBPC-Jul26-analysis.md) — WIT/states/fields snapshot of process `MSBPCTemplate` after template apply

## 2026-08 — Repo root cleanup

- Removed Visual Studio scaffold (`BPCTool.sln`, `bpctool.esproj`), empty root `package-lock.json`, and tracked `.DS_Store`
- Slimmed root `.gitignore` / `.gitattributes` for Node + Python
- Single changelog: this file; root [`README.md`](../README.md) is the repo entry point
- Retired `DEPRECATIONS.md` (notes folded here / USER_GUIDE §17)

## 2026-08 — Template not bundled; scaffold cleanup

- ADO **template guideline** `.xlsx` is user-supplied (removed `fixtures/`); `/defaults` may discover it via `BPCTOOL_TEMPLATE` or under the catalog folder
- Removed unused `.github/copilot-instructions.md` and `.vscode/launch.json`

## 2026-08 — Catalog required-field defaults

- When a required Fields-sheet field is empty in the catalog spreadsheet but has a **Default value**, Catalog Import / prevalidate fills that default (e.g. Business process flow source → `Microsoft`)
- Remaining required empties (no default) still report in `import-prevalidate.json`

## 2026-08 — Run timings, remove profiles, cleanup

- Apply/job runs emit **Run timing** (per-step `durationMs` + total) in the event log and on `ApplyResult` / `JobStatusResponse`
- Removed **Save / Load profile** UI and `bpcProfiles` storage (org URL + PAT remain session-only)
- Removed unused Vite scaffold assets (`src/assets/*`, `public/icons.svg`), dead `plan_only` / `testConnection` helpers
- Docs updated for connection panel rename and timing summary

## 2026-08 — Docs sync (catalog, multi-value, prevalidate)

- README / USER_GUIDE / CHANGELOG updated for Catalog Import (all matching workbooks), Title 1..N parents, multi-value picklists, prevalidate artifacts, and re-import guidance
- USER_GUIDE §9 documents catalog sources, hierarchy, keys, prevalidate actions, create-only behavior, and System.State ownership

## 2026-08 — Multi-value picklists + catalog prevalidate

- Fields marked **Multi-select** (Application family, Products, Industries, …) create July-style **suggested** picklists (`isSuggested` / `isPicklistSuggested`) so semicolon-separated values import
- Layout binds DevLabs **Multivalue** control for those fields (later: extension **required** via Connection/runner preflight — see Multivalue preflight entry above; no longer “optional fallback”)
- Catalog **prevalidate** before create: strip `Area Path=Not found`, strip Test Case `State=New`, strip invalid single picklist values, normalize multi-select tokens; writes `import-prevalidate.json` (later: case-insensitive picklist align — see picklist entry above)
- Module: `catalog_validate.py`; tests for prevalidate, multiselect labels, layout control type

## 2026-08 — Catalog parent links (Title outline)

- Parent/child links follow **Title 1..N** columns (ADO CSV import hierarchy), per [Microsoft Learn](https://learn.microsoft.com/dynamics365/guidance/business-processes/about-import-catalog-devops)
- Process sequence ID is stored on the work item / used as a key, **not** used to derive relationships
- Catalog Import loads **all** matching workbooks in the catalog folder (Business Process Catalog, Deliverables, Objectives, SbD Delivery Plan, etc.)
- Catalog import reports linked / missing-parent counts; `ado-id-map.csv` includes ParentKey/ParentId

## 2026-08 — Docs sync + UI layout

- README / USER_GUIDE rewritten for current launchers, run modes, Excel backlog/disabled WITs, project description, org URL forms, path browser, and troubleshooting
- Wider resizable content shell (~1600px); full-width PAT / org URL / long path rows; less crowded Run configuration grid

## 2026-08 — Project description

- UI field **Project description** (session-persisted) passed as `project_description` on runner jobs
- Create no longer writes `Project for process <guid>`; empty description allowed
- Re-running Project Creation PATCHes description when the field is non-empty

## 2026-08 — Disabled WITs + backlog levels from Excel

- Keep Excel-disabled WITs (Epic / Feature / User story) in IR; Process materializes then `isDisabled`
- Backlog step follows July Script 4: rename/create levels from **Backlogs** sheet, assign WITs, set defaults
- Heal prior buggy applies that created custom Levels/Lowest beside system Epics/Features (delete duplicate, rename Agile behaviors)
- Tests for rename matrix, duplicate heal, WIT assign skip-disabled, defaults

## 2026-08 — Teams, areas, iterations

- Team area paths: aggregate all Excel paths per team into one `teamfieldvalues` PATCH (`includeChildren: false` by default)
- Area paths parse July L1–L4 (skip project column); root area path UI defaults to **project name**
- Backlog step sets team `backlogIteration` from classification tree root GUID before selecting iterations (fixes blank Backlog iteration / blocked Select iteration)
- Assigns child iterations to each Teams-sheet team; optional include-children when Excel says Yes

## 2026-08 — Org URL, path picker, run modes

- Org URL normalize: `dev.azure.com/{org}`, `{org}.visualstudio.com`, bare org → `https://dev.azure.com/{org}`
- Local filesystem Browse… (`/fs` + `PathPickerModal`) for template file and catalog folder
- Run modes: **Selected step only** (default), Dependency-aware, Full — so backlog/teams can re-run without process/project confirm gates
- Launcher / Vite plugin replaces stale `:8787` and starts uvicorn with `--reload`

## 2026-08 — Zero-CLI launch

- Vite plugin auto-starts/stops the local FastAPI runner with the UI (`scripts/localRunnerPlugin.js`)
- Double-click launchers: `Start BPCTool.command` (macOS), `Start BPCTool.bat` (Windows)
- `npm run setup` / `npm start` bootstrap env and open the browser
- Default execution mode is **Runner**

## 2026-08 — Standalone July replacement (P0/P1)

### Summary

Replaced the fragile “UI wraps Microsoft July Python scripts” approach with a **standalone** control plane + execution plane:

- React UI orchestrates configuration, policy, and progress
- Local FastAPI runner owns Excel parsing, planning, and ADO apply
- No subprocess calls to July `.py` scripts

### Architecture

| Before | After |
|--------|-------|
| Shell out to six July scripts via env vars | In-process writers via Azure DevOps REST |
| Process + project created together (July phase 1) | Hard gate: **process → layout → project** |
| Excel read live during each script | Excel → IR → plan → apply → report |
| Limited UI observability | Structured job events + `runner-out/` artifacts |

Recommended engine step order:

`process → layout → project → teams → backlog → catalog → report`

### Local runner (`runner/`)

Added FastAPI app on `127.0.0.1:8787` (proxied as `/api` from Vite):

| Module | Role |
|--------|------|
| `excel_ir.py` | Parse July template sheets + catalog folder into IR |
| `planner.py` | Deterministic dry-run plan + update-policy gates |
| `richtext.py` | HTML detection; optional markdown→HTML |
| `catalog_import.py` | Catalog drafts, Title 1..N parents, multiline format flags |
| `catalog_validate.py` | Prevalidate / sanitize before catalog create |
| `mapping.py` | Catalog headers → ADO field refs (+ multi_select metadata) |
| `ado_client.py` | PAT Basic auth, retries on 429/503 |
| `org_url.py` | Org URL parse/normalize |
| `fs_browser.py` | Local path listing for Browse… |
| `apply_engine.py` | Step orchestration for apply / apply dry-run |
| `writers/*` | process, layout, project, teams, backlog, catalog, report |
| `jobs.py` | In-memory job store; apply runs on background thread |

API surface:

- `GET /health`, `GET /defaults`
- `POST /plan/dry-run`, `POST /ir/parse`
- `POST /jobs`, `GET /jobs/{id}`
- `GET /fs/roots`, `GET /fs/list`

### React UI

- Connection profile (org URL normalize, session PAT, Ready state)
- Fetch projects / Fetch processes via `/ado-proxy`
- Free-text process/project names + optional project description + create/update assessment
- Update policies: require confirmation / always update / skip existing / create-only
- Workbook version fingerprinting (`bpcWorkbookApplies`)
- Collapsible sections + path picker for template/catalog
- Execution modes: **Simulate**, **API** (reads), **Runner** (full engine)
- Workflow run modes: Selected step only / Dependency-aware / Full
- **Preview plan (dry-run)** wired to runner
- **Run** in Runner mode posts `/api/jobs` and polls events
- Workflow cards expanded to include **catalog** and **report**
- Removed dependency on July script filenames as executors (labels now `runner · <step>`)

### Rich text (ADO Toolkit parity)

| Behavior | Detail |
|----------|--------|
| Default | Preserve markdown-like Excel text; set `/multilineFieldsFormat/{field}=Markdown` on create |
| Optional | UI **Convert Markdown large-text fields to HTML** / API `convert_markdown_to_html` |
| HTML cells | Always passed through (e.g. Microsoft references) |

### Inputs / defaults

- Template: user-provided ADO guideline `.xlsx` (optional discover under catalog folder / `BPCTOOL_TEMPLATE`)
- Catalog sources default: `/Users/bill/BPC Files` (JUL 2026 package)
- Apply artifacts: `runner-out/<org>_<project>/` (gitignored)

### Tooling

- `npm run runner` / `npm run runner:install` (prefer `npm start` for day-to-day)
- Vitest frontend tests; pytest runner tests
- README + USER_GUIDE documentation

### Explicitly not done / residual risk

- **DevLabs Multivalue extension is required** for process / layout / project; UI/runner preflight + optional install via Extension Management API; Marketplace/admin if PAT cannot install
- Catalog Import: parent-aware parallel workers + id-map resume + parent-link backfill (July-aligned); still create-only (no WIP field upsert)
- Not every July script edge case is ported
- Inherited system WIT disable via Process API can still fail (manual ADO UI fallback)
- Empty catalog Description omits `System.Description` (no synthetic placeholder)
- In-memory jobs only (lost on runner restart)
- UI cancel stops client polling; does not always kill an in-flight apply thread
- Large catalog imports (~15k rows across all matching workbooks) are long-running; use `apply_dry_run` / `catalog_limit` for smoke tests; start Threads at 2–8 to limit ATCPU/429
- Process re-run may log non-fatal `MSBPC.*` field 404 warnings when org fields already exist (Update API is lock/undelete only)

### Optional surfaces still wired (not primary path)

- **Simulate** / **API** execution modes (stubs / ADO reads); Runner is the apply path
- UI fields `threads` (also Catalog Import parallel workers in Runner), `maxRetries`, `layoutSheet`, `backlogSheet` (`maxRetries` / sheet names remain Simulate/API-oriented)
- `POST /ir/parse` (manual API; UI does not call it)
- `npm run runner` / `runner:install` (prefer `npm start` + Vite plugin)

---

## Earlier baseline (pre-runner)

- React workflow cards modeling process/layout/project/teams/backlog
- Simulate executors and ADO read adapters
- Connection / policy / fingerprint foundations later reused by the runner
