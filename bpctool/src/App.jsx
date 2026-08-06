import { useMemo, useState } from 'react'
import { useMemo, useState } from 'react'
import './App.css'
import { runWorkflowFlow, workflowDefinitions } from './workflowEngine'

const loadJson = (key, fallbackValue) => {
  try {
    return JSON.parse(localStorage.getItem(key) ?? JSON.stringify(fallbackValue))
  } catch {
    return fallbackValue
  }
}

const buildStepStatuses = (completedStepIds) => {
  const completedSet = new Set(completedStepIds)

  return Object.fromEntries(
    workflowDefinitions.map((workflow) => [
      workflow.id,
      completedSet.has(workflow.id) ? 'completed' : 'idle',
    ]),
  )
}

const statusLabelMap = {
  idle: 'Not run',
  running: 'Running',
  completed: 'Completed',
  failed: 'Failed',
}

function App() {
  const initialProfiles = loadJson('bpcProfiles', {})
  const initialCompletedSteps = loadJson('bpcCompletedSteps', [])

  const [orgUrl, setOrgUrl] = useState('')
  const [pat, setPat] = useState('')
  const [profileName, setProfileName] = useState('')
  const [selectedWorkflowId, setSelectedWorkflowId] = useState(
    workflowDefinitions[0].id,
  )
  const [runMode, setRunMode] = useState('single')
  const [templatePath, setTemplatePath] = useState(
    'C:\\dev\\D365Patterns-MS\\templates\\Azure-DevOps-templates\\ADO template guideline (Preview).xlsx',
  )
  const [projectName, setProjectName] = useState('')
  const [processName, setProcessName] = useState('Business Process Catalog')
  const [threads, setThreads] = useState(4)
  const [maxRetries, setMaxRetries] = useState(2)
  const [layoutSheet, setLayoutSheet] = useState('Page Layout')
  const [rootAreaPath, setRootAreaPath] = useState('')
  const [backlogSheet, setBacklogSheet] = useState('Backlog Config')
  const [dryRun, setDryRun] = useState(true)
  const [runMessage, setRunMessage] = useState('No action run yet.')
  const [runLogs, setRunLogs] = useState([])
  const [isRunning, setIsRunning] = useState(false)
  const [profiles, setProfiles] = useState(initialProfiles)
  const [completedStepIds, setCompletedStepIds] = useState(initialCompletedSteps)
  const [stepStatuses, setStepStatuses] = useState(() =>
    buildStepStatuses(initialCompletedSteps),
  )

  const selectedWorkflow = useMemo(
    () =>
      workflowDefinitions.find((workflow) => workflow.id === selectedWorkflowId),
    [selectedWorkflowId],
  )

  const profileKeys = Object.keys(profiles)

  const addLog = (message) => {
    const timestamp = new Date().toLocaleTimeString()
    setRunLogs((previousLogs) => [
      `[${timestamp}] ${message}`,
      ...previousLogs,
    ].slice(0, 120))
  }

  const saveProfile = () => {
    if (!profileName || !orgUrl || !pat) {
      setRunMessage('Enter profile name, org URL, and PAT before saving.')
      return
    }

    const next = { ...profiles, [profileName]: { orgUrl, pat } }
    localStorage.setItem('bpcProfiles', JSON.stringify(next))
    setProfiles(next)
    setRunMessage(`Saved profile \"${profileName}\".`)
  }

  const loadProfile = (name) => {
    const profile = profiles[name]
    if (!profile) {
      return
    }

    setProfileName(name)
    setOrgUrl(profile.orgUrl)
    setPat(profile.pat)
    setRunMessage(`Loaded profile \"${name}\".`)
  }

  const clearCompletionCache = () => {
    localStorage.removeItem('bpcCompletedSteps')
    setCompletedStepIds([])
    setStepStatuses(buildStepStatuses([]))
    setRunMessage('Completion cache cleared. All flow steps reset to Not run.')
  }

  const setStepStatus = (stepId, status) => {
    setStepStatuses((current) => ({
      ...current,
      [stepId]: status,
    }))
  }

  const runWorkflow = async () => {
    setIsRunning(true)
    setRunLogs([])
    setStepStatuses(buildStepStatuses(completedStepIds))
    setRunMessage('Running flow...')

    const runConfig = {
      orgUrl: orgUrl.trim(),
      pat: pat.trim(),
      templatePath: templatePath.trim(),
      projectName: projectName.trim(),
      processName: processName.trim(),
      threads: Number(threads),
      maxRetries: Number(maxRetries),
      dryRun,
      layoutSheet: layoutSheet.trim(),
      rootAreaPath: rootAreaPath.trim(),
      backlogSheet: backlogSheet.trim(),
    }

    const result = await runWorkflowFlow({
      mode: runMode,
      selectedWorkflowId,
      completedStepIds,
      config: runConfig,
      onEvent: (event) => {
        if (event.type === 'step-started') {
          setStepStatus(event.stepId, 'running')
          addLog(`${event.stepTitle}: ${event.message}`)
        }

        if (event.type === 'step-attempt') {
          addLog(`${event.stepTitle}: ${event.message}`)
        }

        if (event.type === 'step-error') {
          addLog(
            `${event.stepTitle}: ${event.message}${
              event.transient ? ' (transient, retrying)' : ''
            }`,
          )
        }

        if (event.type === 'step-warning') {
          addLog(`${event.stepTitle}: warning - ${event.message}`)
        }

        if (event.type === 'step-completed') {
          setStepStatus(event.stepId, 'completed')
          addLog(`${event.stepTitle}: ${event.message}`)
        }

        if (event.type === 'step-failed') {
          setStepStatus(event.stepId, 'failed')
          addLog(`${event.stepTitle}: FAILED - ${event.message}`)
        }
      },
    })

    if (result.ok) {
      setCompletedStepIds(result.completedStepIds)
      localStorage.setItem('bpcCompletedSteps', JSON.stringify(result.completedStepIds))
      setRunMessage(
        result.message ??
          `Flow completed successfully in ${runMode === 'full' ? 'full' : 'dependency-aware'} mode.`,
      )
    } else {
      setRunMessage(`Flow failed: ${result.error.message}`)
    }

    setIsRunning(false)
  }

  return (
    <main className="app-shell">
      <header className="app-header">
        <h1>BPC Azure DevOps React Runner</h1>
        <p>
          React baseline inspired by your <code>ADOT-Next</code> app and mapped to
          the four template workflow stages, with frontend orchestration logic.
        </p>
      </header>

      <section className="panel">
        <h2>Connection profile</h2>
        <div className="grid-2">
          <label>
            Profile name
            <input
              value={profileName}
              onChange={(event) => setProfileName(event.target.value)}
              placeholder="Dev sandbox"
            />
          </label>
          <div className="profile-actions">
            <button type="button" onClick={saveProfile}>
              Save profile
            </button>
            <select value="" onChange={(event) => loadProfile(event.target.value)}>
              <option value="" disabled>
                Load profile
              </option>
              {profileKeys.map((name) => (
                <option key={name} value={name}>
                  {name}
                </option>
              ))}
            </select>
          </div>
          <label>
            Azure DevOps org URL
            <input
              value={orgUrl}
              onChange={(event) => setOrgUrl(event.target.value)}
              placeholder="https://dev.azure.com/your-org"
            />
          </label>
          <label>
            Personal access token
            <input
              type="password"
              value={pat}
              onChange={(event) => setPat(event.target.value)}
              placeholder="PAT"
            />
          </label>
        </div>
      </section>

      <section className="panel">
        <h2>Workflow selection</h2>
        <div className="run-mode">
          <label className="radio-row">
            <input
              type="radio"
              checked={runMode === 'single'}
              onChange={() => setRunMode('single')}
              disabled={isRunning}
            />
            Dependency-aware run to selected step
          </label>
          <label className="radio-row">
            <input
              type="radio"
              checked={runMode === 'full'}
              onChange={() => setRunMode('full')}
              disabled={isRunning}
            />
            Full flow run (skip already completed)
          </label>
        </div>
        <div className="workflow-list">
          {workflowDefinitions.map((workflow) => (
            <button
              key={workflow.id}
              type="button"
              className={`workflow-card ${selectedWorkflowId === workflow.id ? 'active' : ''}`}
              onClick={() => setSelectedWorkflowId(workflow.id)}
              disabled={isRunning}
            >
              <strong>
                {workflow.title}
                <span className={`status-chip ${stepStatuses[workflow.id] ?? 'idle'}`}>
                  {statusLabelMap[stepStatuses[workflow.id] ?? 'idle']}
                </span>
              </strong>
              <span>{workflow.script}</span>
              <small>{workflow.description}</small>
            </button>
          ))}
        </div>
      </section>

      <section className="panel">
        <h2>Run configuration</h2>
        <div className="grid-2">
          <label>
            Template workbook path
            <input
              value={templatePath}
              onChange={(event) => setTemplatePath(event.target.value)}
            />
          </label>
          <label>
            Project name
            <input
              value={projectName}
              onChange={(event) => setProjectName(event.target.value)}
              placeholder="Contoso-BPC"
            />
          </label>
          <label>
            Process name
            <input
              value={processName}
              onChange={(event) => setProcessName(event.target.value)}
              disabled={isRunning}
            />
          </label>
          <label>
            Threads (for layout step)
            <input
              type="number"
              min="1"
              max="16"
              value={threads}
              onChange={(event) => setThreads(event.target.value)}
              disabled={isRunning}
            />
          </label>
          <label>
            Retry count
            <input
              type="number"
              min="0"
              max="5"
              value={maxRetries}
              onChange={(event) => setMaxRetries(event.target.value)}
              disabled={isRunning}
            />
          </label>
          <label>
            Layout worksheet name
            <input
              value={layoutSheet}
              onChange={(event) => setLayoutSheet(event.target.value)}
              disabled={isRunning}
            />
          </label>
          <label>
            Root area path
            <input
              value={rootAreaPath}
              onChange={(event) => setRootAreaPath(event.target.value)}
              placeholder="Project\\Business Process Catalog"
              disabled={isRunning}
            />
          </label>
          <label>
            Backlog worksheet name
            <input
              value={backlogSheet}
              onChange={(event) => setBacklogSheet(event.target.value)}
              disabled={isRunning}
            />
          </label>
          <label className="checkbox-row">
            <input
              type="checkbox"
              checked={dryRun}
              onChange={(event) => setDryRun(event.target.checked)}
              disabled={isRunning}
            />
            Dry-run backlog configuration
          </label>
          <div className="input-list">
            <p>Workflow-specific inputs</p>
            <ul>
              {(selectedWorkflow?.inputs ?? []).map((inputName) => (
                <li key={inputName}>{inputName}</li>
              ))}
            </ul>
          </div>
        </div>

        <button
          type="button"
          className="run-button"
          onClick={runWorkflow}
          disabled={isRunning}
        >
          {isRunning ? 'Running...' : 'Run selected flow'}
        </button>

        <button
          type="button"
          className="run-button secondary"
          onClick={clearCompletionCache}
          disabled={isRunning}
        >
          Clear completion cache
        </button>

        <div className="run-log" role="status" aria-live="polite">
          <p>{runMessage}</p>
          <pre>{runLogs.length > 0 ? runLogs.join('\n') : 'No execution logs yet.'}</pre>
        </div>
      </section>
    </main>
  )
}

export default App
