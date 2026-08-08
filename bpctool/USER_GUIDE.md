# BPCTool User Guide

This guide covers requirements, installation, step-by-step usage, architecture, API, and troubleshooting for the Business Process Catalog (BPC) Azure DevOps setup tool.

For a short overview, see [README.md](./README.md). For release history, see [CHANGELOG.md](./CHANGELOG.md).

---

## 1. What this tool does

BPCTool configures an Azure DevOps organization for the Microsoft Business Process Catalog pattern:

1. Create/update an **inherited process** from the July ADO template workbook
2. Apply **page layouts** (including HTML field controls) **before** any project exists
3. Create/bind a **project** to that process (optional description)
4. Upsert **teams** and **area paths** (including multi-path team assignments)
5. Configure **backlog levels**, **WIT→backlog mapping**, **iteration paths**, and **team iteration settings**
6. **Import catalog** workbooks (Business Process Catalog, Deliverables, Objectives, SbD Delivery Plan, etc.)
7. Emit an **HTML/JSON summary report**

Excel remains the authoring format. A local FastAPI runner parses workbooks into an intermediate representation (IR), builds a plan, and applies changes through Azure DevOps REST APIs.

**Important:** This app does **not** shell out to the Microsoft July Python scripts. It is a standalone React UI + local runner engine. The runner starts automatically with the UI.

---

## 2. Requirements

### Software

| Component | Requirement |
|-----------|-------------|
| Node.js | 20+ recommended (Vite 8) |
| npm | Comes with Node |
| Python | 3.11+ (3.12–3.14 tested) |
| OS | macOS / Windows / Linux with local filesystem access to Excel files |

### Azure DevOps

| Item | Notes |
|------|-------|
| Organization URL | `https://dev.azure.com/{org}`, `https://{org}.visualstudio.com`, or bare `{org}` (normalized to `https://dev.azure.com/{org}`) |
| PAT | Personal Access Token with scopes sufficient to manage processes, projects, work items, and teams. Typically: **Work Items (Read & Write)**, **Project and Team (Read & Write)**, **Identity (Read)**. Process customization may require organization-level permissions. |
| Permissions | Ability to create inherited processes and projects in the target org |

### Input files

| Input | Purpose | Example |
|-------|---------|---------|
| ADO template workbook | Process/WITs/fields/picklists/teams/areas/backlogs | `fixtures/ADO template guideline (July).xlsx` |
| Catalog source folder | Phase-5 import workbooks (`.xlsx`) | `/Users/bill/BPC Files` |

Catalog files are recognized by name hints such as *Business Process Catalog*, *Deliverables*, *Objectives*, *Delivery Plan*, *SbD* (case-insensitive). Month/year suffixes are fine — e.g. `Deliverables JUL 2026.xlsx` matches the same as `Deliverables.xlsx`. Do **not** put the ADO template guideline workbook in this folder as a catalog input (use it only as **Template workbook path**).

### Ports

| Service | Default |
|---------|---------|
| Vite UI | `http://127.0.0.1:5173` (or next free port) |
| Local runner API | `http://127.0.0.1:8787` |

Vite proxies:

- `/api/*` → runner (`8787`)
- `/ado-proxy/*` → `https://dev.azure.com`
- `/fs/*` → local filesystem browser (path picker)

---

## 3. Installation

### Recommended (no command line)

1. Install **Node.js 20+** and **Python 3.11+** once on the machine (system installers).
2. Double-click:
   - macOS: `Start BPCTool.command`
   - Windows: `Start BPCTool.bat`
3. First launch runs `npm run setup` automatically (npm packages + Python venv + runner requirements).

Manual equivalent (developers):

```bash
cd bpctool
npm run setup    # node_modules + .venv + runner requirements
npm start        # UI + auto-started runner; opens browser
```

`npm run setup` installs packages from `runner/requirements.txt` into `.venv`:

- fastapi, uvicorn, openpyxl, pydantic, python-multipart

---

## 4. Starting the application

**You do not need separate terminals for the UI and runner.**

| How | What happens |
|-----|----------------|
| Double-click `Start BPCTool.command` / `.bat` | Setup if needed → start UI → auto-start runner → open browser |
| `npm start` | Same as above (without the setup wrapper) |

The Vite process starts the FastAPI runner on `127.0.0.1:8787` via `scripts/localRunnerPlugin.js` (with `--reload`, and it replaces a stale process already bound to `8787`). Closing the start window / stopping Vite also stops the runner it started.

Confirm health (optional):

```bash
curl http://127.0.0.1:8787/health
# {"status":"ok"}
```

Browser URL is usually `http://127.0.0.1:5173` (opened automatically). The UI content area widens with the browser window (up to ~1600px) so long paths and PATs are readable.

---

## 5. Step-by-step: first successful dry-run

This path validates Excel parsing and planning **without** mutating Azure DevOps.

### Step 0 — Launch

Double-click **Start BPCTool** and wait for the browser to open.

### Step 1 — Connection profile

1. Expand **1. Connection profile**
2. Enter:
   - **Org URL** — e.g. `https://dev.azure.com/contoso`, `https://contoso.visualstudio.com`, or `contoso`
   - **PAT** — session-only (not saved in profiles); the field uses the full panel width
3. Optionally **Save profile** (stores org URL only)
4. Confirm **Execution mode** is **Runner** (default)
5. Wait until the status chip shows **Ready**

Optional but recommended:

- **Fetch existing projects**
- **Fetch existing processes**

These populate inventory used for create-vs-update policy.

### Step 2 — Process & project names

1. Open **2. Process & project names**
2. Type the **process name** you want to create or update (free text, not select-only)
3. Type the **project name** similarly
4. Optionally enter a **project description** (Azure DevOps project overview text). On create this is what ADO stores (empty is allowed). Older builds wrote `Project for process <guid>` — that is no longer used. Re-running **Project Creation** updates an existing project’s description when this field is non-empty.
5. Choose an **update policy**:

| Policy | Behavior |
|--------|----------|
| Require confirmation before update | If process/project already exists, you must check confirm boxes |
| Always update existing targets | Proceed with update/reuse |
| Skip steps for existing targets | Skip process/project phases when targets exist |
| Create only (fail if exists) | Fail planning/apply if targets already exist |

6. If policy requires it and the name matches inventory, check **Confirm process update** / **Confirm project update**

### Step 3 — Workflow selection

1. Open **3. Workflow selection**
2. Choose a run mode (default is **Selected step only**):

| Mode | Behavior |
|------|----------|
| **Selected step only** | Re-runs just the selected card; no prerequisite gating (useful to fix backlog/teams alone) |
| **Dependency-aware** | Runs through the selected card and its incomplete prerequisites |
| **Full** | Runs all incomplete steps in engine order |

3. Select a workflow card when using Selected step only or Dependency-aware

### Step 4 — Run configuration

1. Open **4. Run configuration**
2. Click **Load runner defaults** (loads fixture template + catalog folder if present)
3. Confirm paths (use **Browse…** for the local filesystem picker, or paste absolute paths):
   - **Template workbook path** — absolute path to July guideline `.xlsx`
   - **Catalog source folder** — absolute path to BPC catalog workbooks
   - **Workbook version / revision label** — e.g. `JUL-2026` (used in fingerprinting)
4. Set options:
   - **Apply dry-run** — leave **unchecked** for live Azure DevOps changes (default). Check only to rehearse writers without mutating the org.
   - **Convert Markdown large-text fields to HTML** — leave **unchecked** unless you want HTML conversion (see §8)
5. **Root area path** defaults to the **project name** (project root); override only if needed. Area path *children* still come from the Excel Area paths sheet.

### Step 5 — Preview plan (safe)

1. Click **Preview plan (dry-run)** — this only plans; it never mutates Azure DevOps
2. Review:
   - Step order: `process → layout → project → teams → backlog → catalog → report`
   - Counts (enabled WITs, disabled WITs, fields, HTML fields, teams, backlogs, catalog rows, etc.)
   - Warnings/errors
3. Fix any blocking errors (missing sheets, confirmation required, etc.) before running

### Step 6 — Live apply

1. Keep **Execution mode = Runner**
2. Confirm **Apply dry-run** is **unchecked**
3. Choose run mode and workflow card (see Step 3)
4. Click **Run selected flow**
5. Watch the event log for real ADO progress (not `[dry-run] Would ensure…` messages)
6. On success, open artifacts under `bpctool/runner-out/<org>_<project>/`

If **Apply dry-run** is checked, steps finish quickly with `[dry-run]` log lines and **nothing is created in the org**. That run also does **not** mark steps complete for dependency tracking.

### Optional — Apply dry-run rehearsal

Check **Apply dry-run**, run the flow, and inspect preview artifacts (`import-preview.csv`, summary HTML/JSON) without mutating Azure DevOps. Uncheck it before the real apply.

**Cancel:** use the cancel control while a run is in progress (aborts polling / client-side flow). Background apply jobs already started on the runner may continue until that job finishes; restart the runner process if you need a hard stop.

---

## 6. UI sections reference

### 1. Connection profile

| Control | Purpose |
|---------|---------|
| Profile name / Save / Load | Persist org URL locally; PAT stays session-only |
| Org URL | Accepts `dev.azure.com/{org}`, `{org}.visualstudio.com`, or bare org; normalized for API calls |
| PAT | Full-width field; Basic auth `:${pat}` for ADO and runner apply; Show/Hide toggle |
| Fetch projects / processes | Optional inventory for update policy |
| Execution mode | Simulate / API / Runner (see §7) |

### 2. Process & project names

Free-text names for create or update, optional **project description**, and update policy. Existing targets are assessed when inventory was fetched or names match known lists.

### 3. Workflow selection

Run mode radios + seven engine step cards with status overlays (running/completed/failed/skipped). Completion is cached per org/process/project in `localStorage`.

### 4. Run configuration

Template/catalog paths (Browse…), workbook version, threads/retries, layout/backlog sheet names, root area path, dry-run, markdown conversion, preview plan, run actions, event log.

The layout uses a wide content shell and full-width rows for long values (paths, PAT, org URL) so fields are not clipped beside unused white space.

---

## 7. Execution modes

| Mode | When to use | What Run does |
|------|-------------|----------------|
| **Runner** (default) | Real setup/import | Posts `/api/jobs` to local engine; Excel → IR → plan → apply |
| **API** | Prove PAT + inventory | Live ADO **reads** via `/ado-proxy`; not full setup |
| **Simulate** | UI / orchestration testing | Local timed stubs; no ADO writes; no Excel apply |

**Preview plan** always calls the local runner (`POST /api/plan/dry-run`). The runner is started automatically with the app.

---

## 8. Rich text (HTML vs Markdown)

Catalog Excel cells (Description, Agenda, Microsoft references, etc.) may contain:

- Real **HTML** (`<div><a href=...>`)
- **Markdown-like** plain text (`* bullet`, numbered lists, blank-line paragraphs)

### Default (recommended) — preserve Markdown

Matches ADO Toolkit WIT migration:

- HTML cells → passed through unchanged
- Markdown-like cells → left as authored
- On work-item create, runner also sends:

```text
/multilineFieldsFormat/{FieldRef} = Markdown
```

so Azure DevOps renders Markdown correctly (without this, Markdown often appears as plain text in HTML controls).

### Optional — Convert Markdown large-text fields to HTML

UI checkbox / API field `convert_markdown_to_html: true`:

- Markdown-like cells are converted to HTML (`<p>`, `<ul>`, `<li>`, links)
- No `multilineFieldsFormat=Markdown` op is emitted
- Existing HTML still passes through

Use this only when the target process/org expects HTML storage instead of Markdown multiline format.

---

## 9. Workflow steps (engine)

Hard sequence for a full run:

```text
process → layout → project → teams → backlog → catalog → report
```

Project (and later project-phase steps) cannot start until process + layout succeed **unless** you use **Selected step only** to re-run a later card against an already-configured org.

| Step | ID | What it does |
|------|----|--------------|
| 1. Process Template | `process` | Create/update inherited process; WITs; picklists; custom fields; disable Excel-disabled WITs |
| 2. Page Layout | `layout` | Add fields to WITs; pages/groups/controls; `HtmlFieldControl` for HTML fields (skips disabled WITs) |
| 3. Project Creation | `project` | Create project bound to process (or reuse existing); set/update optional description |
| 4. Teams & Areas | `teams` | Create teams; area path tree; aggregate team area assignments (`includeChildren: false` unless Excel says otherwise) |
| 5. Backlog Config | `backlog` | Rename/create backlog levels; assign WITs; set defaults; iteration paths; team backlog/iteration settings |
| 6. Catalog Import | `catalog` | Import catalog rows as work items (parent links, rich text rules) |
| 7. Report | `report` | Write HTML/JSON summary under `runner-out/` |

### Template sheets that drive process & backlog

| Sheet | Role |
|-------|------|
| **Work item types** | WIT definitions; `Custom work item type = Disabled` for Epic / Feature / User story; `Backlog name` maps enabled WITs to levels |
| **Backlogs** | Level names, type, color, default WIT, **Rename from** (`Epic`, `Feature`, `(new)`, `(rename)`) |
| **Fields** / **Picklists** | Custom fields and lists |
| **Area paths** / **Teams** | Hierarchy + team mappings (July L1–L4 style; project column skipped) |
| **Iteration paths** | Iteration tree created and assigned to teams in the backlog step |

**July-shaped Backlogs sheet (fixture):**

| Backlog name | Type | Default WIT | Rename from |
|--------------|------|-------------|-------------|
| Highest | Portfolio | Functional area | `(new)` |
| Kanban | Portfolio | Test Case | `(new)` |
| Levels | Portfolio | Process | `Epic` |
| Lowest | Portfolio | Scenario | `Feature` |
| Deliverables | Requirements | Configuration | `(rename)` |
| Tasks | Iteration | Task | `(rename)` |

Disabled WITs remain in the IR so Process can materialize + `isDisabled`. Layout and backlog assignment skip them. If ADO rejects a disable PATCH, set **Disabled** on that WIT in Organization Settings → Process.

If an older apply created custom **Levels** / **Lowest** while leaving system **Epics** / **Features**, re-run **Backlog Config** — the engine removes the duplicate custom levels and renames the Agile behaviors to match Excel.

---

## 10. Spreadsheet deltas & fingerprints

- **Workbook version** label + file bytes produce a fingerprint
- Successful process applies can record the fingerprint in `localStorage` (`bpcWorkbookApplies`)
- When the workbook changes for the same org/process, the UI surfaces that a spreadsheet delta update is appropriate

Use a clear version label (e.g. `JUL-2026`) whenever you switch template revisions.

---

## 11. Outputs and artifacts

Root: `bpctool/runner-out/<org>_<project>/`

| Artifact | When |
|----------|------|
| `import-preview.csv` | Catalog step (including apply dry-run) |
| `ado-id-map.csv` | Live catalog import |
| `import-failures.json` | Live catalog import failures |
| `bpc-ado-setup-summary.html` | Report step |
| `bpc-ado-setup-summary.json` | Report step |

`runner-out/` is gitignored.

---

## 12. Local runner API

Base URL (direct): `http://127.0.0.1:8787`  
Via UI proxy: `/api/...`

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Liveness |
| GET | `/defaults` | Default template + catalog paths |
| POST | `/plan/dry-run` | Parse Excel → IR → plan (no mutations) |
| POST | `/ir/parse` | Return full IR JSON |
| POST | `/jobs` | Create dry-run or apply job |
| GET | `/jobs/{id}` | Poll job status/events/results |
| GET | `/fs/roots`, `/fs/list` | Local path browser used by Browse… |

### Job create body (important fields)

```json
{
  "org_url": "https://dev.azure.com/contoso",
  "pat": "<required for apply>",
  "process_name": "Business Process Catalog",
  "project_name": "Contoso-BPC",
  "project_description": "Optional overview text for the Azure DevOps project",
  "excel_file": "/absolute/path/to/ADO template guideline (July).xlsx",
  "catalog_source_dir": "/absolute/path/to/BPC Files",
  "workbook_version": "JUL-2026",
  "update_policy": "always-update",
  "confirm_process_update": false,
  "confirm_project_update": false,
  "known_process_exists": false,
  "known_project_exists": false,
  "root_area_path": "Contoso-BPC",
  "mode": "apply",
  "apply_dry_run": true,
  "convert_markdown_to_html": false,
  "steps": null,
  "catalog_limit": null
}
```

| Field | Notes |
|-------|-------|
| `project_description` | Optional; set on create; PATCH on existing project when non-empty |
| `mode` | `dry-run` = plan only; `apply` = run writers |
| `apply_dry_run` | With `mode=apply`, run writers without ADO HTTP mutations |
| `convert_markdown_to_html` | Toolkit-style override; default `false` |
| `steps` | Optional subset, e.g. `["backlog"]` or `["catalog","report"]` |
| `catalog_limit` | Cap drafts for smoke tests |
| `root_area_path` | Defaults to project name when omitted/empty in the UI |

Apply jobs run in a background thread; poll `GET /jobs/{id}` until `status` is `succeeded` or `failed`.

### Example: apply dry-run via curl

```bash
curl -s -X POST http://127.0.0.1:8787/jobs \
  -H 'Content-Type: application/json' \
  -d '{
    "org_url": "https://dev.azure.com/contoso",
    "pat": "012345678901234567890123456789",
    "process_name": "Business Process Catalog",
    "project_name": "Contoso-BPC",
    "project_description": "BPC sandbox project",
    "excel_file": "'"$PWD"'/fixtures/ADO template guideline (July).xlsx",
    "catalog_source_dir": "/Users/bill/BPC Files",
    "update_policy": "always-update",
    "mode": "apply",
    "apply_dry_run": true,
    "convert_markdown_to_html": false,
    "catalog_limit": 25
  }'
```

Then poll `/jobs/{id}` from the response.

---

## 13. Architecture (for operators)

```text
React UI (Vite)
  ├─ /ado-proxy  → Azure DevOps (browser reads)
  ├─ /fs         → Local filesystem browser
  └─ /api        → Local runner :8787
                      ├─ excel_ir.py      Excel → IR (keeps disabled WITs)
                      ├─ planner.py       IR → dry-run plan
                      ├─ richtext.py      HTML detect / optional MD→HTML
                      ├─ catalog_import.py Drafts + multiline format flags
                      ├─ ado_client.py    REST client + retries
                      ├─ org_url.py       Org URL normalize/parse
                      ├─ fs_browser.py    Path picker backend
                      ├─ apply_engine.py  Step orchestration
                      └─ writers/*        process…report
```

Key design rules:

- Browser never owns long write jobs; runner does
- Process + layout before project (full/dependency runs)
- Excel is authoring; IR is the run source of truth
- No subprocess calls to July scripts
- Launcher replaces stale `:8787` and starts uvicorn with `--reload`

---

## 14. Testing

```bash
# Frontend unit tests
npm test

# Runner unit/integration tests (uses fixture + /Users/bill/BPC Files when present)
cd runner && ../.venv/bin/pytest -q

# Lint / production build
npm run lint
npm run build
```

Notable runner coverage includes Excel IR (disabled WITs, backlogs), backlog rename/heal + WIT assignment, team area aggregation, team iterations / backlogIteration GUID, org URL normalize, layout booleans, and project description.

---

## 15. Troubleshooting

### Runner unreachable / Preview plan fails

**Symptom:** “Failed to reach local runner” or fetch to `/api/...` errors.

**Fix:**

1. Quit the Start BPCTool window and relaunch (or `npm start`)
2. On first use, wait for setup to finish creating `.venv`
3. Confirm `curl http://127.0.0.1:8787/health`
4. Ensure nothing else owns port `8787`
5. Run `npm run setup` once if the venv was never created

### Port already in use

```bash
# find / stop prior uvicorn, then relaunch the app
lsof -i :8787
pkill -f 'uvicorn app.main:app'
# Double-click Start BPCTool, or: npm start
```

### Template missing sheets

**Symptom:** `Excel template is missing required sheets: ...`

Required sheets:

- Work item types
- Fields
- Picklists
- Area paths
- Teams
- Backlogs
- Iteration paths

Use the July **ADO template guideline** workbook, not a catalog file, as the template path.

### Catalog folder empty / 0 rows

**Symptom:** Catalog step skipped or warning about missing sources.

**Fix:**

- Point **Catalog source folder** at the folder containing the JUL catalog `.xlsx` files
- Paths must be absolute and readable by the Python process (not only the browser)
- Close Excel if files are locked (`~$` temp files are ignored)

### Update confirmation required

**Symptom:** Dry-run blocked because process/project exists.

**Fix:** Check confirm boxes, or switch policy to **Always update** / **Skip existing**.

### PAT / 401 / 403 on live apply

**Fix:**

- Regenerate PAT with process + project + work item scopes
- Confirm org URL matches the org the PAT belongs to
- Use **API** mode + Fetch projects as a quick credential check before Runner apply

### Throttling (429 / 503)

Runner retries with backoff. Reduce parallelism / rerun failed steps. Catalog import recovers by key where possible on retry-style failures during create.

### Markdown shows as plain text in ADO

You likely converted incorrectly, or multiline format was not applied:

1. Prefer **default preserve** (checkbox off)
2. Re-import affected items, or manually set field format to Markdown in ADO
3. If you intentionally converted to HTML, content should contain `<p>` / `<ul>` tags

### Layout / HTML controls fail

Some inherited WIT layouts can be locked. Check runner events for layout warnings. Ensure process step created/customized WITs before layout.

### Project create hangs

ADO project creation is asynchronous. The runner polls for several seconds. If it times out, verify the project in the org UI and rerun with **skip-existing** or **always-update**.

### Project description still shows “Project for process …”

That text came from older creates. Enter the desired text in **Project description** and re-run **Project Creation** (Selected step only). New creates never use the process GUID string.

### Browser path picker only gave a file name

Use **Browse…** (local runner filesystem picker) or paste a **full absolute path**. System/browser dialogs often return only a short name like `BPC Files`, which the runner then resolves relative to its own folder and fails.

### Apply dry-run still seemed to call ADO

Current engine creates no ADO client when `apply_dry_run` is true. If you see ADO traffic, confirm the job body has `"apply_dry_run": true` and relaunch Start BPCTool / `npm start` to pick up code changes.

### Teams step reported 0 assignments / Areas show no Teams

1. Confirm **Apply dry-run** is **unchecked** for a live run. Dry-run never PATCHes `teamfieldvalues` (event log will say `No Azure DevOps teamfieldvalues were changed`).
2. Quit and relaunch Start BPCTool / `npm start` after pulling code changes — the UI replaces any stale process on port `8787` and starts the runner with `--reload`.
3. Re-run the **Teams & areas** card only. The log should show many `Assigned team '…' → …` lines and finish with `N team area assignments` (fixture ≈ 47).

### Team iteration paths empty in Azure DevOps

Iteration **nodes** are created in the backlog step; **team** iteration membership (and backlog iteration / bug behavior) is also applied there (July Script 4).

If the team Iterations page shows **Default iteration = @CurrentIteration** but **Backlog iteration** is blank (and Select iteration is blocked), the backlog step set the macro without a root iteration GUID. Re-run **Backlog configuration** with **Selected step only** after relaunching the app so the runner reloads. Expect:

- `Iteration root GUID … (N child iteration(s) to assign)`
- `Updated team settings for '…': … (backlogIteration=<guid>)`
- `Added N iterations to team '…'`

### Backlog levels wrong / leftover “Epics” or “Features”

Excel expects **Levels** / **Lowest** (renamed from Epic/Feature), not a parallel custom level beside system Epics/Features.

1. Relaunch the app so the runner reloads
2. Re-run **Backlog Config** with **Selected step only**
3. Expect logs like `Removing duplicate custom backlog 'Levels'…` and `Renamed behavior 'Epics' → 'Levels'`
4. Confirm Process → Backlog levels matches the **Backlogs** sheet (Highest, Kanban, Levels, Lowest, Deliverables, Tasks)

### Epic / Feature / User story still enabled

Process attempts to materialize then disable Excel-disabled WITs. If the API rejects disable, set **Disabled** manually in Organization Settings → Process. Layout/backlog do not treat them as active types.

### Completion cache looks wrong

Completion is stored per org/process/project key in `localStorage`. Use **Clear completion cache**, clear site data for localhost, or change process/project names if you need a clean slate. **Selected step only** ignores completion for the selected card.

---

## 16. Security notes

- PAT is kept in **sessionStorage** only (not in saved profiles)
- Prefer least-privilege PATs and rotate after bulk imports
- Runner binds to `127.0.0.1` by default (local only)
- Do not commit `.venv/`, `runner-out/`, or files containing PATs

---

## 17. Known limitations

- Apply writers follow the July-shaped workbook closely, but are not a line-for-line port of every July edge case (e.g. DevLabs multivalue extension auto-install)
- Disabling inherited system WITs via the public Process API can fail; manual disable in the ADO UI may still be required
- Catalog import of ~15k rows is long-running; use apply dry-run + `catalog_limit` for smoke tests
- Job store is in-memory; restarting the runner clears job history
- Cancel in the UI stops client polling; it does not always hard-kill an in-flight apply thread

---

## 18. Quick reference card

```text
Double-click: Start BPCTool.command  (macOS)
           or Start BPCTool.bat      (Windows)

In the browser:
  1. Connection profile → Ready (Runner mode)
  2. Process + project names (+ optional description)
  3. Workflow: Selected step only / Dependency-aware / Full
  4. Load runner defaults → Preview plan
  Apply dry-run UNCHECKED → Run for live ADO
```

Developer equivalent: `npm run setup` once, then `npm start` each session.

Defaults:

- Template: `fixtures/ADO template guideline (July).xlsx`
- Catalog: `/Users/bill/BPC Files` (override to your machine path)
- Root area path: project name
- Markdown: preserved unless “Convert Markdown…to HTML” is checked
- Run mode: Selected step only
