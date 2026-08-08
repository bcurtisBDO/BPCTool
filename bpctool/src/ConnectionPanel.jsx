import { useState } from 'react'

/**
 * Collapsible connection profile: profile, org URL, PAT, optional inventory fetch.
 * Process/project names to create live in a separate step.
 */
export default function ConnectionPanel({
  profileName,
  onProfileNameChange,
  profileKeys,
  onSaveProfile,
  onLoadProfile,
  orgUrl,
  onOrgUrlChange,
  pat,
  onPatChange,
  showPat,
  onToggleShowPat,
  connectionReady,
  connectionStatusText,
  fetchingProjects,
  projectsFetched,
  onFetchProjects,
  fetchingProcesses,
  processesFetched,
  onFetchProcesses,
  executionMode,
  onExecutionModeChange,
  disabled = false,
}) {
  const [expandedWhileReady, setExpandedWhileReady] = useState(false)
  const open = !connectionReady || expandedWhileReady

  return (
    <section className="panel collapsible-panel">
      <button
        type="button"
        className="panel-heading-row collapsible-trigger"
        onClick={() => {
          if (!connectionReady) {
            return
          }
          setExpandedWhileReady((value) => !value)
        }}
        aria-expanded={open}
      >
        <h2>1. Connection profile</h2>
        <span className="collapse-meta">
          <span
            className={`status-chip connection-pill ${connectionReady ? 'completed' : 'idle'}`}
          >
            {connectionReady ? 'Ready' : 'Needs URL + PAT'}
          </span>
          <span className="collapse-caret" aria-hidden="true">
            {open ? '▾' : '▸'}
          </span>
        </span>
      </button>

      {open ? (
        <div className="grid-2 collapsible-body">
          <label>
            Profile name
            <input
              value={profileName}
              onChange={(event) => onProfileNameChange(event.target.value)}
              placeholder="Dev sandbox"
              disabled={disabled}
            />
          </label>
          <div className="profile-actions">
            <button type="button" onClick={onSaveProfile} disabled={disabled}>
              Save profile
            </button>
            <select
              value=""
              onChange={(event) => onLoadProfile(event.target.value)}
              disabled={disabled}
            >
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

          <label className="field-span-full">
            Azure DevOps org URL
            <input
              value={orgUrl}
              onChange={(event) => onOrgUrlChange(event.target.value)}
              placeholder="https://dev.azure.com/org or https://org.visualstudio.com"
              disabled={disabled}
            />
          </label>

          <label className="field-span-full">
            Personal access token
            <div className="pat-row">
              <input
                type={showPat ? 'text' : 'password'}
                value={pat}
                onChange={(event) => onPatChange(event.target.value)}
                placeholder="PAT (session only, not saved)"
                autoComplete="off"
                spellCheck={false}
                disabled={disabled}
              />
              <button
                type="button"
                className="secondary-inline"
                onClick={onToggleShowPat}
                disabled={disabled}
              >
                {showPat ? 'Hide' : 'Show'}
              </button>
            </div>
          </label>

          <div className="fetch-row inventory-actions field-span-full">
            <button
              type="button"
              className={projectsFetched ? 'fetched-button' : ''}
              onClick={onFetchProjects}
              disabled={disabled || fetchingProjects || !connectionReady}
            >
              {fetchingProjects
                ? 'Loading projects...'
                : projectsFetched
                  ? 'Projects fetched'
                  : 'Fetch existing projects'}
            </button>
            <button
              type="button"
              className={processesFetched ? 'fetched-button' : ''}
              onClick={onFetchProcesses}
              disabled={disabled || fetchingProcesses || !connectionReady}
            >
              {fetchingProcesses
                ? 'Loading processes...'
                : processesFetched
                  ? 'Processes fetched'
                  : 'Fetch existing processes'}
            </button>
          </div>

          <label className="field-span-full">
            Execution mode
            <select
              value={executionMode}
              onChange={(event) => onExecutionModeChange(event.target.value)}
              disabled={disabled}
            >
              <option value="runner">Runner (local Excel→IR→apply engine)</option>
              <option value="api">API (live ADO reads via proxy)</option>
              <option value="simulate">Simulate (local stubs)</option>
            </select>
          </label>

          <div className="connection-note">
            <p>{connectionStatusText}</p>
            <p>
              Profiles store org URL only. PAT stays in this browser session. Fetching existing
              projects/processes is optional and used to validate create vs update policy.
              The local apply engine starts automatically with the app — no separate terminal.
            </p>
          </div>
        </div>
      ) : (
        <p className="collapsed-summary">
          {orgUrl || 'No org URL'} · PAT {pat ? 'set' : 'missing'} · mode {executionMode}
        </p>
      )}
    </section>
  )
}
