# Changelog

All notable changes to BPCTool (React UI + local runner) are documented here.

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
| `apply_engine.py` | Step orchestration for apply / apply dry-run |
| `writers/*` | process, layout, project, teams, backlog, catalog, report |
| `jobs.py` | In-memory job store; apply runs on background thread |

API surface:

- `GET /health`, `GET /defaults`
- `POST /plan/dry-run`, `POST /ir/parse`
- `POST /jobs`, `GET /jobs/{id}`

### React UI

- Connection profile (ADOToolkit-style org URL normalize, session PAT, Ready state)
- Fetch projects / Fetch processes via `/ado-proxy`
- Free-text process/project names + create/update assessment
- Update policies: require confirmation / always update / skip existing / create-only
- Workbook version fingerprinting (`bpcWorkbookApplies`)
- Collapsible sections + path picker for template/catalog
- Execution modes: **Simulate**, **API** (reads), **Runner** (full engine)
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

- `npm run runner` / `npm run runner:install`
- Vitest frontend tests; pytest runner tests (`richtext`, `excel_ir`, catalog drafts)
- README + USER_GUIDE documentation

### Explicitly not done / residual risk

- Not every July script edge case is ported (e.g. DevLabs multivalue extension auto-install)
- In-memory jobs only (lost on runner restart)
- UI cancel stops client polling; does not always kill an in-flight apply thread
- Large catalog imports (~15k rows) are long-running; use `apply_dry_run` / `catalog_limit` for smoke tests

---

## Earlier baseline (pre-runner)

- React workflow cards modeling process/layout/project/teams/backlog
- Simulate executors and ADO read adapters
- Connection / policy / fingerprint foundations later reused by the runner
