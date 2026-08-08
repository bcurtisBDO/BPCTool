# Changelog

All notable changes to BPCTool (React UI + local runner) are documented here.

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
| `catalog_import.py` | Catalog drafts, field mapping, multiline format flags |
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

- Template fixture: `fixtures/ADO template guideline (July).xlsx`
- Catalog sources default: `/Users/bill/BPC Files` (JUL 2026 package)
- Apply artifacts: `runner-out/<org>_<project>/` (gitignored)

### Tooling

- `npm run runner` / `npm run runner:install` (prefer `npm start` for day-to-day)
- Vitest frontend tests; pytest runner tests
- README + USER_GUIDE documentation

### Explicitly not done / residual risk

- Not every July script edge case is ported (e.g. DevLabs multivalue extension auto-install)
- Inherited system WIT disable via Process API can still fail (manual ADO UI fallback)
- In-memory jobs only (lost on runner restart)
- UI cancel stops client polling; does not always kill an in-flight apply thread
- Large catalog imports (~15k rows) are long-running; use `apply_dry_run` / `catalog_limit` for smoke tests

---

## Earlier baseline (pre-runner)

- React workflow cards modeling process/layout/project/teams/backlog
- Simulate executors and ADO read adapters
- Connection / policy / fingerprint foundations later reused by the runner
