# BPC Azure DevOps React Runner

This app is a React baseline for a UI-driven runner around the Python scripts in:

`C:\dev\D365Patterns-MS\templates\Azure-DevOps-templates`

It also follows interaction patterns from your `ADOT-Next` app (profile-based connection setup and task-oriented workflow selection).

## Included workflows

1. `1_ADO_Creation_Script (Preview).py`
2. `2_ADO_Page_Layout_Script_Threaded (Preview).py`
3. `3_ADO_Teams_Areas_Script (Preview).py`
4. `4_ADO_Backlog_Config_Script (Preview).py`

## Current scope

- Shared Azure DevOps connection profile UI
- Workflow card selection and script mapping
- Frontend orchestration engine that preserves 4-step flow logic
- Dependency-aware execution (running step 4 can auto-run missing 1-3)
- Full-flow mode with completion cache skip optimization
- Retry policy for transient failures (throttle/network simulation)
- Inline validation and run log/error visibility
- Local persistence in browser `localStorage` for profiles and completed steps

## Backend flexibility

The flow logic is implemented in `src/workflowEngine.js` and does not require a Python backend.

You can keep this fully frontend for guided run planning, or replace simulated step execution with:

- a Node API,
- a .NET API,
- or direct Azure DevOps REST calls.

As long as `workflowDefinitions` order and orchestration contract are preserved, flow behavior stays consistent.

## Run locally

```bash
npm install
npm run dev
```
