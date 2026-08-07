# BPC Azure DevOps React Runner

Standalone React UI + local FastAPI runner for Business Process Catalog Azure DevOps setup.

Excel remains the authoring format. The runner parses workbooks into an intermediate representation (IR), plans the run, and applies changes through Azure DevOps REST APIs.

**This app does not spawn the Microsoft July Python scripts.**

| Doc | Contents |
|-----|----------|
| **[USER_GUIDE.md](./USER_GUIDE.md)** | Requirements, install, step-by-step usage, modes, rich text, API, troubleshooting |
| **[CHANGELOG.md](./CHANGELOG.md)** | What changed in the standalone rebuild |

---

## Quick start

```bash
# one-time
npm install
python3 -m venv .venv
npm run runner:install

# every session — two terminals
npm run runner    # http://127.0.0.1:8787
npm run dev       # Vite UI (proxies /api → runner)
```

In the UI:

1. **Connection profile** — org URL + PAT → Ready  
2. **Execution mode** → **Runner**  
3. **Process & project names** — enter names; set update policy  
4. **Load runner defaults** — template fixture + catalog folder  
5. **Preview plan (dry-run)** — review steps/counts  
6. Keep **Apply dry-run** checked → **Run** (no ADO mutations)  
7. Uncheck **Apply dry-run** → **Run** for live apply  

Defaults:

- Template: `fixtures/ADO template guideline (July).xlsx`
- Catalog: `/Users/bill/BPC Files` (change to your path)

Artifacts: `runner-out/<org>_<project>/`

---

## Workflow order

1. Process template  
2. Page layouts (before any project)  
3. Project create/bind  
4. Teams & areas  
5. Backlog & iterations  
6. Catalog import  
7. HTML/JSON report  

## Execution modes

| Mode | Purpose |
|------|---------|
| **Simulate** | Local stubs for UI/orchestration testing |
| **API** | Live ADO **reads** via `/ado-proxy` |
| **Runner** | Full Excel→IR→apply engine (`/api/jobs`) |

## Rich text

- **HTML** from Excel → always preserved  
- **Markdown** → preserved by default (+ `multilineFieldsFormat=Markdown` on create)  
- Optional UI: **Convert Markdown large-text fields to HTML**  

Details: [USER_GUIDE.md §8](./USER_GUIDE.md#8-rich-text-html-vs-markdown).

## Tests

```bash
npm test
cd runner && ../.venv/bin/pytest -q
npm run lint && npm run build
```

## API (local runner)

Proxied as `/api/*` from Vite:

- `GET /health`, `GET /defaults`
- `POST /plan/dry-run`, `POST /ir/parse`
- `POST /jobs`, `GET /jobs/{id}`

Full request fields and curl examples: [USER_GUIDE.md §12](./USER_GUIDE.md#12-local-runner-api).
