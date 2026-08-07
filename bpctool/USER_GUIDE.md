# BPCTool User Guide

This guide covers requirements, installation, step-by-step usage, architecture, API, and troubleshooting for the Business Process Catalog (BPC) Azure DevOps setup tool.

For a short overview, see [README.md](./README.md). For what changed in this rebuild, see [CHANGELOG.md](./CHANGELOG.md).

---

## 1. What this tool does

BPCTool configures an Azure DevOps organization for the Microsoft Business Process Catalog pattern:

1. Create/update an **inherited process** from the July ADO template workbook
2. Apply **page layouts** (including HTML field controls) **before** any project exists
3. Create/bind a **project** to that process
4. Upsert **teams** and **area paths**
5. Configure **backlogs** and **iteration paths**
6. **Import catalog** workbooks (Business Process Catalog, Deliverables, Objectives, SbD Delivery Plan, etc.)
7. Emit an **HTML/JSON summary report**

Excel remains the authoring format. A local FastAPI runner parses workbooks into an intermediate representation (IR), builds a plan, and applies changes through Azure DevOps REST APIs.

**Important:** This app does **not** shell out to the Microsoft July Python scripts. It is a standalone React UI + local runner engine.

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
| Organization URL | `https://dev.azure.com/{org}` (or `*.visualstudio.com`) |
| PAT | Personal Access Token with scopes sufficient to manage processes, projects, work items, and teams. Typically: **Work Items (Read & Write)**, **Project and Team (Read & Write)**, **Identity (Read)**. Process customization may require organization-level permissions. |
| Permissions | Ability to create inherited processes and projects in the target org |

### Input files

| Input | Purpose | Example |
|-------|---------|---------|
| ADO template workbook | Process/WITs/fields/picklists/teams/areas/backlogs | `fixtures/ADO template guideline (July).xlsx` |
| Catalog source folder | Phase-5 import workbooks (`.xlsx`) | `/Users/bill/BPC Files` |

Catalog files are recognized by name hints such as *Business Process Catalog*, *Deliverables*, *Objectives*, *Delivery Plan*, *SbD*. Other `.xlsx` files in the folder are also accepted.

### Ports

| Service | Default |
|---------|---------|
| Vite UI | `http://127.0.0.1:5173` (or next free port) |
| Local runner API | `http://127.0.0.1:8787` |

Vite proxies:

- `/api/*` → runner (`8787`)
- `/ado-proxy/*` → `https://dev.azure.com`

---

## 3. Installation

From the `bpctool` directory:

```bash
# Frontend dependencies
npm install

# Python virtualenv + runner dependencies
python3 -m venv .venv
npm run runner:install
```

`npm run runner:install` installs packages from `runner/requirements.txt` into `.venv`:

- fastapi, uvicorn, openpyxl, pydantic, python-multipart

---

## 4. Starting the application

You need **two terminals**.

**Terminal 1 — local runner**

```bash
cd bpctool
npm run runner
```

Confirm health:

```bash
curl http://127.0.0.1:8787/health
# {"status":"ok"}
```

**Terminal 2 — UI**

```bash
cd bpctool
npm run dev
```

Open the printed local URL (usually `http://127.0.0.1:5173`).

---

## 5. Step-by-step: first successful dry-run

This path validates Excel parsing and planning **without** mutating Azure DevOps.

### Step 1 — Connection profile

1. Expand **1. Connection profile**
2. Enter:
   - **Org URL** — e.g. `https://dev.azure.com/contoso`
   - **PAT** — session-only (not saved in profiles)
3. Optionally **Save profile** (stores org URL only)
4. Set **Execution mode** to **Runner (local Excel→IR→apply engine)**
5. Wait until the status chip shows **Ready**

Optional but recommended:

- **Fetch existing projects**
- **Fetch existing processes**

These populate inventory used for create-vs-update policy.

### Step 2 — Process & project names

1. Open **2. Process & project names**
2. Type the **process name** you want to create or update (free text, not select-only)
3. Type the **project name** similarly
4. Choose an **update policy**:

| Policy | Behavior |
|--------|----------|
| Require confirmation before update | If process/project already exists, you must check confirm boxes |
| Always update existing targets | Proceed with update/reuse |
| Skip steps for existing targets | Skip process/project phases when targets exist |
| Create only (fail if exists) | Fail planning/apply if targets already exist |

5. If policy requires it and the name matches inventory, check **Confirm process update** / **Confirm project update**

### Step 3 — Run configuration

1. Open **3. Run configuration**
2. Click **Load runner defaults** (loads fixture template + catalog folder if present)
3. Confirm paths:
   - **Template workbook path** — absolute path to July guideline `.xlsx`
   - **Catalog source folder** — absolute path to BPC catalog workbooks
   - **Workbook version / revision label** — e.g. `JUL-2026` (used in fingerprinting)
4. Set options:
   - **Apply dry-run** — **checked** for first run (no ADO mutations)
   - **Convert Markdown large-text fields to HTML** — leave **unchecked** unless you want HTML conversion (see §8)
5. Set root area path if needed (defaults to project name when empty)

### Step 4 — Preview plan

1. Click **Preview plan (dry-run)**
2. Review:
   - Step order: `process → layout → project → teams → backlog → catalog → report`
   - Counts (WITs, fields, HTML fields, teams, catalog rows, etc.)
   - Warnings/errors
3. Fix any blocking errors (missing sheets, confirmation required, etc.) before running

### Step 5 — Run (apply dry-run)

1. Choose run mode:
   - **Single / dependency-aware** — runs through the selected workflow card (and its prerequisites)
   - **Full** — runs all incomplete steps
2. Select a workflow card if using dependency-aware mode
3. Click **Run selected flow**
4. Watch the event log for step progress
5. On success, open artifacts under:

```text
bpctool/runner-out/<org>_<project>/
```

Typical files after a dry-run apply:

| File | Contents |
|------|----------|
| `import-preview.csv` | Sample catalog rows + description format |
| `bpc-ado-setup-summary.html` | Human-readable summary |
| `bpc-ado-setup-summary.json` | Machine-readable summary |

### Step 6 — Live apply (when ready)

1. Keep **Execution mode = Runner**
2. Uncheck **Apply dry-run**
3. Confirm org/PAT/process/project/update policy
4. Prefer **Preview plan** again
5. Run **Full** mode (or step through cards)
6. Re-check `runner-out/` for `ado-id-map.csv`, failures JSON, and the summary report

**Cancel:** use the cancel control while a run is in progress (aborts polling / client-side flow). Background apply jobs already started on the runner may continue until that job finishes; restart the runner process if you need a hard stop.

---

## 6. UI sections reference

### 1. Connection profile

| Control | Purpose |
|---------|---------|
| Profile name / Save / Load | Persist org URL locally; PAT stays session-only |
| Org URL | Normalized to `https://dev.azure.com/{org}` |
| PAT | Basic auth `:${pat}` for ADO and runner apply |
| Fetch projects / processes | Optional inventory for update policy |
| Execution mode | Simulate / API / Runner (see §7) |

### 2. Process & project names

Free-text names for create or update. Existing targets are assessed when inventory was fetched or names match known lists.

### 3. Run configuration

Paths, workbook version, threads/retries (used by simulate/API adapters), layout/backlog sheet names, dry-run, markdown conversion, preview plan, run.

### Workflow cards

Seven engine steps (see §9). Status overlays show running/completed/failed/skipped during a run. Completion is cached per org/process/project in `localStorage`.

---

## 7. Execution modes

| Mode | When to use | What Run does |
|------|-------------|----------------|
| **Simulate** | UI / orchestration testing | Local timed stubs; no ADO writes; no Excel apply |
| **API** | Prove PAT + inventory | Live ADO **reads** via `/ado-proxy`; not full setup |
| **Runner** | Real setup/import | Posts `/api/jobs` to local engine; Excel → IR → plan → apply |

**Preview plan** always calls the local runner (`POST /api/plan/dry-run`), regardless of execution mode. You still need `npm run runner` for preview.

For production setup/import, use **Runner**.

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

Hard sequence:

```text
process → layout → verify → project → teams → backlog → catalog → report
```

Project (and later project-phase steps) cannot start until process + layout succeed.

| Step | ID | What it does |
|------|----|--------------|
| 1. Process Template | `process` | Create/update inherited process; WITs; picklists; custom fields |
| 2. Page Layout | `layout` | Add fields to WITs; pages/groups/controls; `HtmlFieldControl` for HTML fields |
| 3. Project Creation | `project` | Create project bound to process (or reuse existing) |
| 4. Teams & Areas | `teams` | Create teams; area path tree; team area assignments |
| 5. Backlog Config | `backlog` | Process backlog behaviors; iteration paths |
| 6. Catalog Import | `catalog` | Import catalog rows as work items (parent links, rich text rules) |
| 7. Report | `report` | Write HTML/JSON summary under `runner-out/` |

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

### Job create body (important fields)

```json
{
  "org_url": "https://dev.azure.com/contoso",
  "pat": "<required for apply>",
  "process_name": "Business Process Catalog",
  "project_name": "Contoso-BPC",
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
| `mode` | `dry-run` = plan only; `apply` = run writers |
| `apply_dry_run` | With `mode=apply`, run writers without ADO HTTP mutations |
| `convert_markdown_to_html` | Toolkit-style override; default `false` |
| `steps` | Optional subset, e.g. `["catalog","report"]` |
| `catalog_limit` | Cap drafts for smoke tests |

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
  └─ /api        → Local runner :8787
                      ├─ excel_ir.py      Excel → IR
                      ├─ planner.py       IR → dry-run plan
                      ├─ richtext.py      HTML detect / optional MD→HTML
                      ├─ catalog_import.py Drafts + multiline format flags
                      ├─ ado_client.py    REST client + retries
                      ├─ apply_engine.py  Step orchestration
                      └─ writers/*        process…report
```

Key design rules:

- Browser never owns long write jobs; runner does
- Process + layout before project
- Excel is authoring; IR is the run source of truth
- No subprocess calls to July scripts

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

---

## 15. Troubleshooting

### Runner unreachable / Preview plan fails

**Symptom:** “Failed to reach local runner” or fetch to `/api/...` errors.

**Fix:**

1. Start `npm run runner`
2. Confirm `curl http://127.0.0.1:8787/health`
3. Ensure nothing else owns port `8787`
4. Restart Vite after proxy/config changes

### Port already in use

```bash
# find / stop prior uvicorn
lsof -i :8787
pkill -f 'uvicorn app.main:app'
npm run runner
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

### Browser path picker only gave a file name

Enter the **full absolute path** the runner can read on disk (UI notes this for browsers that do not expose full paths).

### Apply dry-run still seemed to call ADO

Current engine creates no ADO client when `apply_dry_run` is true. If you see ADO traffic, confirm the job body has `"apply_dry_run": true` and restart the runner to pick up code changes (`--reload` is enabled via `npm run runner`).

### Completion cache looks wrong

Completion is stored per org/process/project key in `localStorage`. Clear site data for localhost, or change process/project names, if you need a clean slate.

---

## 16. Security notes

- PAT is kept in **sessionStorage** only (not in saved profiles)
- Prefer least-privilege PATs and rotate after bulk imports
- Runner binds to `127.0.0.1` by default (local only)
- Do not commit `.venv/`, `runner-out/`, or files containing PATs

---

## 17. Known limitations

- Apply writers are robust for the July-shaped workbook but are not a line-for-line port of every July script edge case (DevLabs multivalue extension install, every backlog behavior rename path, etc.)
- Catalog import of ~15k rows is long-running; use apply dry-run + `catalog_limit` for smoke tests
- Job store is in-memory; restarting the runner clears job history
- Cancel in the UI stops client polling; it does not always hard-kill an in-flight apply thread

---

## 18. Quick reference card

```bash
# Setup (once)
npm install && python3 -m venv .venv && npm run runner:install

# Every session
npm run runner    # terminal 1
npm run dev       # terminal 2

# UI
Execution mode = Runner
Load runner defaults
Enter process + project names
Preview plan (dry-run)
Apply dry-run checked → Run
Uncheck Apply dry-run → Run for live ADO
```

Defaults:

- Template: `fixtures/ADO template guideline (July).xlsx`
- Catalog: `/Users/bill/BPC Files` (override to your machine path)
- Markdown: preserved unless “Convert Markdown…to HTML” is checked
