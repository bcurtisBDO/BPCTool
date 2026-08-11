# BPCTool

React UI + local FastAPI runner that configures Azure DevOps for the Microsoft Business Process Catalog from Excel workbooks.

The app lives in [`bpctool/`](./bpctool/). This repo root is only the entry point for docs and git.

## Quick start

```text
cd bpctool
# macOS:  double-click Start BPCTool.command
# Windows: double-click Start BPCTool.bat
# or:      npm run setup && npm start
```

Prerequisites: Node.js 20+, Python 3.11+.

In the browser: set org URL + PAT → confirm **Multivalue: installed** (or install when prompted) → process/project names → template workbook path (user-provided ADO guideline `.xlsx`) + catalog folder → Preview plan → Run (Runner mode).

**Required org extension:** [Multivalue control (Microsoft DevLabs)](https://marketplace.visualstudio.com/items?itemName=ms-devlabs.vsts-extensions-multivalue-control) — needed for Multi-select fields and for process / layout / project setup. The Connection panel checks the org and can install via API when the PAT allows; otherwise install as an org admin.

UI screenshots (Connection, workflow cards, run config, Catalog Threads): see [`bpctool/README.md`](./bpctool/README.md#screenshots).

## Docs

| Doc | Purpose |
|-----|---------|
| [`bpctool/README.md`](./bpctool/README.md) | Launch, checklist, workflow, modes |
| [`bpctool/USER_GUIDE.md`](./bpctool/USER_GUIDE.md) | Full usage, API, troubleshooting |
| [`bpctool/CHANGELOG.md`](./bpctool/CHANGELOG.md) | Release history |
| [`bpctool/docs/workflow-and-july-comparison.md`](./bpctool/docs/workflow-and-july-comparison.md) | Workflow, X vs H matrix, catalog parallel/resume/backfill, July vs BPCTool |
| [`bpctool/docs/reference/`](./bpctool/docs/reference/) | Process template after creation (MSBPC Jul 2026 analysis) |

## Layout

```text
bpctool/
  src/           React UI (Vite)
  runner/        FastAPI Excel→IR→plan→apply engine
  scripts/       Env + Vite local-runner plugin
  docs/             Workflow & July comparison; reference/ post-create analysis
  Start BPCTool.*  One-click launchers
```

Template and catalog workbooks are **not** bundled — supply absolute paths (or set `BPCTOOL_TEMPLATE` / place the guideline beside the catalog folder).
