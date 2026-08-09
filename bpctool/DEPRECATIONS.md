# Deprecation / cleanup review (2026-08)

## Removed in this pass

| Item | Reason |
|------|--------|
| Named **Save / Load profile** UI + `bpcProfiles` | Redundant with session org URL; PAT was never profiled |
| `src/assets/hero.png`, `react.svg`, `vite.svg` | Unused Vite scaffold |
| `public/icons.svg` | Unused (`favicon.svg` remains) |
| `apply_engine.plan_only` | Unused; `/plan/dry-run` uses `jobs.run_dry_run` |
| `adoApi.testConnection` | Unused; Fetch projects/processes cover credential checks |
| `.github/copilot-instructions.md` | Unused Azure Copilot boilerplate |
| `.vscode/launch.json` | Stale VS launch config (wrong port) |
| `fixtures/ADO template guideline (July).xlsx` | User-supplied input; not bundled with the app |

## Keep (still wired) — optional future retire

| Item | Notes |
|------|--------|
| **Simulate** execution mode | UI orchestration stubs; not real apply |
| **API** execution mode | Live ADO reads only; useful for PAT/inventory checks |
| `stepExecutors.runner` stub | App uses whole-job `/api/jobs`; stub keeps mode lookup stable |
| `POST /ir/parse` | Documented manual API; UI does not call it |
| UI fields `threads`, `maxRetries`, `layoutSheet`, `backlogSheet` | Used on Simulate/API path only; not sent on runner jobs |
| `npm run runner` / `runner:install` | Manual runner; day-to-day uses Vite plugin |

## Do not deprecate

- All `runner/app/writers/*`, catalog import/validate (July workbook semantics, not script shell-out)
- `Start BPCTool.*`, `localRunnerPlugin.js`, path picker, completion cache
