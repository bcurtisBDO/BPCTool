# BPC Azure DevOps React Runner

Standalone React UI + local FastAPI runner for Business Process Catalog Azure DevOps setup.

Excel remains the authoring format. The runner parses workbooks into an intermediate representation (IR), plans the run, and applies changes through Azure DevOps REST APIs.

**This app does not spawn the Microsoft July Python scripts.**  
**The local runner starts automatically with the UI** — no second terminal.

| Doc | Contents |
|-----|----------|
| **[USER_GUIDE.md](./USER_GUIDE.md)** | Requirements, install, step-by-step usage, modes, Excel sheets, API, troubleshooting |
| **[CHANGELOG.md](./CHANGELOG.md)** | What changed in the standalone rebuild and later releases |

---

## Launch (no command line)

**macOS:** double-click `Start BPCTool.command`  
**Windows:** double-click `Start BPCTool.bat`

First launch installs npm + Python dependencies if needed, then starts the UI and local runner and opens your browser. Leave that window open while you work; close it to stop.

Prerequisites (installed once on the machine):

- Node.js 20+
- Python 3.11+

---

## Optional: developers

```bash
npm run setup   # ensure node_modules + .venv
npm start       # UI + auto-started runner (opens browser)
```

Advanced: `npm run runner` still starts only the API if you need it alone. Prefer `npm start` so Vite replaces a stale process on port `8787` and enables `--reload`.

---

## First-run checklist (in the browser)

1. **Connection** — org URL + PAT (session-only) → Ready (PAT field spans the full content width)
2. **Execution mode** → **Runner** (default)
3. **Process & project names** — enter names; optional **project description**; set update policy
4. **Workflow selection** — default **Selected step only**, or Dependency-aware / Full
5. **Run configuration** — set **Template workbook path** (your ADO guideline `.xlsx`) and **Catalog source folder**; **Load runner defaults** fills catalog (and template if found beside it / via `BPCTOOL_TEMPLATE`)
6. **Preview plan (dry-run)** — review steps/counts (never mutates ADO)
7. Confirm **Apply dry-run** is unchecked → **Run selected flow** for live apply
8. Optional: check **Apply dry-run** only to rehearse without org changes

Defaults:

- Template: **not bundled** — provide the July ADO template guideline path (Browse…); often kept next to catalog files
- Catalog: `/Users/bill/BPC Files` (change to your path)
- Root area path: project name (project root)

Artifacts: `runner-out/<org>_<project>/`

---

## Workflow order

1. Process template (WITs, picklists, fields; multi-select → suggested lists; disables Excel-disabled types such as Epic / Feature / User story)
2. Page layouts (before any project; DevLabs multivalue control for Multi-select fields)
3. Project create/bind (optional user description)
4. Teams & areas (multi-path team assignments)
5. Backlog & iterations (levels from **Backlogs** sheet + WIT mapping + team iterations)
6. Catalog import (all matching workbooks in the catalog folder — BPC, Deliverables, Objectives, SbD, etc.)
7. HTML/JSON report

## Execution modes

| Mode | Purpose |
|------|---------|
| **Runner** (default) | Full Excel→IR→apply engine (auto-started locally) |
| **API** | Live ADO **reads** via `/ado-proxy` |
| **Simulate** | Local stubs for UI/orchestration testing |

## Run modes (workflow selection)

| Mode | Behavior |
|------|----------|
| **Selected step only** (default) | Re-run the selected card alone (no prerequisite gating) |
| **Dependency-aware** | Selected card plus incomplete prerequisites |
| **Full** | All incomplete steps in engine order |

## Excel → Azure DevOps (highlights)

- **Backlogs** sheet: rename/create levels (Epic→Levels, Feature→Lowest, Stories→Deliverables, new Highest/Kanban), set default WITs, assign enabled WITs from **Work item types**
- **Disabled** WIT rows stay in IR so Process can disable them in ADO
- Duplicate custom backlog levels left by older applies are healed on re-run (system Epics/Features preferred)
- **Multi-select** fields (Application family, Products, Industries, …): suggested picklists + DevLabs multivalue form control so `A; B` values import
- **Catalog Import** loads every matching `.xlsx` in the catalog folder (not only Business Process Catalog); parent links follow **Title 1..N** (ADO CSV outline), not Process sequence ID
- Catalog **prevalidate** strips common hard-fail values and writes `import-prevalidate.json` before create
- Org URL accepts `dev.azure.com/{org}`, `{org}.visualstudio.com`, or bare org name

## Rich text

- **HTML** from Excel → always preserved  
- **Markdown** → preserved by default (+ `multilineFieldsFormat=Markdown` on create)  
- Optional UI: **Convert Markdown large-text fields to HTML**  

Details: [USER_GUIDE.md §8](./USER_GUIDE.md#8-rich-text-html-vs-markdown).

## Catalog & artifacts (quick)

Catalog is **create-only** (no in-place upsert). Typical outputs under `runner-out/<org>_<project>/`:

| File | Role |
|------|------|
| `import-preview.csv` | Sample drafts (also on apply dry-run) |
| `import-prevalidate.json` | Picklist / area / state preflight counts |
| `ado-id-map.csv` | Created ids + `ParentKey` / `ParentId` |
| `import-failures.json` | Per-row ADO create errors |

Full usage and troubleshooting: [USER_GUIDE.md §9](./USER_GUIDE.md#9-workflow-steps-engine) and [§15](./USER_GUIDE.md#15-troubleshooting).

## Tests

```bash
npm test
cd runner && ../.venv/bin/pytest -q
npm run lint && npm run build
```

## API (local runner)

Auto-started on `127.0.0.1:8787`, proxied as `/api/*` from Vite:

- `GET /health`, `GET /defaults`
- `POST /plan/dry-run`, `POST /ir/parse`
- `POST /jobs`, `GET /jobs/{id}`

Full request fields (including `project_description`) and curl examples: [USER_GUIDE.md §12](./USER_GUIDE.md#12-local-runner-api).
