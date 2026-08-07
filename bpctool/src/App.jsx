import { useMemo, useRef, useState } from 'react'
import './App.css'
import { fetchProcesses, fetchProjects } from './adoApi'
import { normalizeAdoOrgUrl } from './adoOrgUrl'
import CollapsibleSection from './CollapsibleSection'
import ConnectionPanel from './ConnectionPanel'
import PathPickerModal from './PathPickerModal'
import {
  assessExistingTargets,
  validateTargetNames,
  workbookApplyKey,
} from './targetAssessment'
import { buildRunnerJobBody, runRunnerJob } from './runnerApi'
import {
  migrateCompletedStepIds,
  resolveTargetSteps,
  runWorkflowFlow,
  stepExecutors,
  workflowDefinitions,
} from './workflowEngine'

const PROFILES_KEY = 'bpcProfiles'
const COMPLETION_CACHE_KEY = 'bpcCompletedSteps'
const WORKBOOK_APPLIES_KEY = 'bpcWorkbookApplies'
const SESSION_ORG_URL = 'bpcSessionOrgUrl'
const SESSION_PAT = 'bpcSessionPat'
const SESSION_PROFILE = 'bpcSessionProfile'
const SESSION_PROJECT = 'bpcSessionProject'
const SESSION_PROCESS = 'bpcSessionProcess'
const SESSION_EXECUTION_MODE = 'bpcSessionExecutionMode'

const loadJson = (key, fallbackValue) => {
  try {
    return JSON.parse(localStorage.getItem(key) ?? JSON.stringify(fallbackValue))
  } catch {
    return fallbackValue
  }
}

const readSession = (key, fallback = '') => {
  try {
    return sessionStorage.getItem(key) ?? fallback
  } catch {
    return fallback
  }
}

const writeSession = (key, value) => {
  try {
    if (value) {
      sessionStorage.setItem(key, value)
    } else {
      sessionStorage.removeItem(key)
    }
  } catch {
    /* private mode / quota */
  }
}

const buildCacheKey = (orgUrl, processName, projectName) => {
  const normalized = normalizeAdoOrgUrl(orgUrl)
  const orgKey = (normalized.ok ? normalized.url : orgUrl.trim())
    .toLowerCase()
    .replace(/\/+$/, '')
  const processKey = processName.trim().toLowerCase()
  const projectKey = projectName.trim().toLowerCase()

  if (!orgKey || !processKey) {
    return null
  }

  return `${orgKey}::${processKey}::${projectKey || '__pre_project__'}`
}

const normalizeProfiles = (raw) => {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return {}
  }

  return Object.fromEntries(
    Object.entries(raw).map(([name, profile]) => {
      const rawUrl = typeof profile?.orgUrl === 'string' ? profile.orgUrl : ''
      const normalized = normalizeAdoOrgUrl(rawUrl)
      return [name, { orgUrl: normalized.ok ? normalized.url : rawUrl }]
    }),
  )
}

const normalizeCompletionCache = (raw) => {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return {}
  }

  return Object.fromEntries(
    Object.entries(raw)
      .filter(([key, value]) => typeof key === 'string' && Array.isArray(value))
      .map(([key, value]) => [key, migrateCompletedStepIds(value)]),
  )
}

const normalizeWorkbookApplies = (raw) => {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return {}
  }
  return raw
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

const parseBoundedInt = (rawValue, fallback) => {
  if (rawValue === '' || rawValue === null || rawValue === undefined) {
    return Number.NaN
  }

  const parsed = Number(rawValue)
  return Number.isFinite(parsed) ? parsed : fallback
}

const statusLabelMap = {
  idle: 'Not run',
  running: 'Running',
  completed: 'Completed',
  failed: 'Failed',
  skipped: 'Skipped',
}

function App() {
  const [orgUrl, setOrgUrlState] = useState(() => readSession(SESSION_ORG_URL))
  const [pat, setPatState] = useState(() => readSession(SESSION_PAT))
  const [profileName, setProfileNameState] = useState(() => readSession(SESSION_PROFILE))
  const [showPat, setShowPat] = useState(false)
  const [selectedWorkflowId, setSelectedWorkflowId] = useState(
    workflowDefinitions[0].id,
  )
  const [runMode, setRunMode] = useState('single')
  const [executionMode, setExecutionModeState] = useState(() => {
    const stored = readSession(SESSION_EXECUTION_MODE, 'simulate')
    return ['api', 'runner', 'simulate'].includes(stored) ? stored : 'simulate'
  })
  const [templatePath, setTemplatePath] = useState(
    '/Users/bill/dev/BPCTool/bpctool/fixtures/ADO template guideline (July).xlsx',
  )
  const [catalogSourceDir, setCatalogSourceDir] = useState('/Users/bill/BPC Files')
  const [pathPickerOpen, setPathPickerOpen] = useState(false)
  const [pathPickerMode, setPathPickerMode] = useState('file')
  const [pathPickerTarget, setPathPickerTarget] = useState('template')
  const [workbookVersion, setWorkbookVersion] = useState('JUL-2026')
  const [planResult, setPlanResult] = useState(null)
  const [planLoading, setPlanLoading] = useState(false)
  const [planError, setPlanError] = useState('')
  const [updatePolicy, setUpdatePolicy] = useState('require-confirmation')
  const [confirmProcessUpdate, setConfirmProcessUpdate] = useState(false)
  const [confirmProjectUpdate, setConfirmProjectUpdate] = useState(false)
  const [projectName, setProjectNameState] = useState(() => readSession(SESSION_PROJECT))
  const [processName, setProcessNameState] = useState(() => readSession(SESSION_PROCESS))
  const [threads, setThreads] = useState(4)
  const [maxRetries, setMaxRetries] = useState(2)
  const [layoutSheet, setLayoutSheet] = useState('Page Layout')
  const [rootAreaPath, setRootAreaPath] = useState('')
  const [backlogSheet, setBacklogSheet] = useState('Backlog Config')
  const [dryRun, setDryRun] = useState(true)
  const [convertMarkdownToHtml, setConvertMarkdownToHtml] = useState(false)
  const [runMessage, setRunMessage] = useState('No action run yet.')
  const [runLogs, setRunLogs] = useState([])
  const [isRunning, setIsRunning] = useState(false)
  const [profiles, setProfiles] = useState(() => {
    const scrubbed = normalizeProfiles(loadJson(PROFILES_KEY, {}))
    localStorage.setItem(PROFILES_KEY, JSON.stringify(scrubbed))
    return scrubbed
  })
  const [completionCache, setCompletionCache] = useState(() => {
    const scoped = normalizeCompletionCache(loadJson(COMPLETION_CACHE_KEY, {}))
    localStorage.setItem(COMPLETION_CACHE_KEY, JSON.stringify(scoped))
    return scoped
  })
  const [workbookApplies, setWorkbookApplies] = useState(() =>
    normalizeWorkbookApplies(loadJson(WORKBOOK_APPLIES_KEY, {})),
  )
  const [runOverlay, setRunOverlay] = useState({ key: null, statuses: {} })
  const [projects, setProjects] = useState([])
  const [fetchingProjects, setFetchingProjects] = useState(false)
  const [projectsFetched, setProjectsFetched] = useState(false)
  const [processes, setProcesses] = useState([])
  const [fetchingProcesses, setFetchingProcesses] = useState(false)
  const [processesFetched, setProcessesFetched] = useState(false)
  const [apiStatusText, setApiStatusText] = useState(
    'Fetch projects to validate the PAT against Azure DevOps.',
  )

  const isRunningRef = useRef(false)
  const abortControllerRef = useRef(null)

  const loadRunnerDefaults = async () => {
    try {
      const response = await fetch('/api/defaults')
      if (!response.ok) {
        throw new Error(`Runner defaults unavailable (${response.status})`)
      }
      const defaults = await response.json()
      if (defaults.excel_file) {
        setTemplatePath(defaults.excel_file)
      }
      if (defaults.catalog_source_dir) {
        setCatalogSourceDir(defaults.catalog_source_dir)
      }
      setRunMessage('Loaded template/catalog defaults from local runner.')
    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : 'Failed to reach local runner. Start it with npm run runner.'
      setRunMessage(`Could not load runner defaults: ${message}`)
    }
  }

  const setOrgUrl = (value) => {
    setOrgUrlState(value)
    writeSession(SESSION_ORG_URL, value)
    setProjects([])
    setProjectsFetched(false)
    setProcesses([])
    setProcessesFetched(false)
  }

  const setPat = (value) => {
    setPatState(value)
    writeSession(SESSION_PAT, value)
    setProjectsFetched(false)
    setProcessesFetched(false)
  }

  const setProfileName = (value) => {
    setProfileNameState(value)
    writeSession(SESSION_PROFILE, value)
  }

  const setProjectName = (value) => {
    setProjectNameState(value)
    writeSession(SESSION_PROJECT, value)
    setConfirmProjectUpdate(false)
    if (value && !rootAreaPath) {
      setRootAreaPath(`${value}\\Business Process Catalog`)
    }
  }

  const setProcessName = (value) => {
    setProcessNameState(value)
    writeSession(SESSION_PROCESS, value)
    setConfirmProcessUpdate(false)
  }

  const setExecutionMode = (value) => {
    const next = ['api', 'runner'].includes(value) ? value : 'simulate'
    setExecutionModeState(next)
    writeSession(SESSION_EXECUTION_MODE, next)
  }

  const effectiveOrgUrl = useMemo(() => {
    const normalized = normalizeAdoOrgUrl(orgUrl)
    return normalized.ok ? normalized.url : orgUrl.trim()
  }, [orgUrl])

  const connectionReady = Boolean(effectiveOrgUrl && pat.trim())

  const cacheKey = useMemo(
    () => buildCacheKey(effectiveOrgUrl, processName, projectName),
    [effectiveOrgUrl, processName, projectName],
  )

  const lastAppliedWorkbook = useMemo(() => {
    const key = workbookApplyKey(effectiveOrgUrl, processName)
    return workbookApplies[key] ?? null
  }, [workbookApplies, effectiveOrgUrl, processName])

  const targetAssessment = useMemo(
    () =>
      assessExistingTargets({
        processName,
        projectName,
        knownProcesses: processes,
        knownProjects: projects,
        templatePath,
        workbookVersion,
        lastAppliedWorkbook,
      }),
    [
      processName,
      projectName,
      processes,
      projects,
      templatePath,
      workbookVersion,
      lastAppliedWorkbook,
    ],
  )

  const nameValidation = useMemo(
    () =>
      validateTargetNames({
        processName,
        projectName,
        assessment: targetAssessment,
        updatePolicy,
        confirmProcessUpdate,
        confirmProjectUpdate,
        requireProjectName: true,
      }),
    [
      processName,
      projectName,
      targetAssessment,
      updatePolicy,
      confirmProcessUpdate,
      confirmProjectUpdate,
    ],
  )

  const completedStepIds = useMemo(
    () => (cacheKey ? migrateCompletedStepIds(completionCache[cacheKey] ?? []) : []),
    [cacheKey, completionCache],
  )

  const plannedStepIds = useMemo(
    () => resolveTargetSteps(runMode, selectedWorkflowId, completedStepIds),
    [runMode, selectedWorkflowId, completedStepIds],
  )

  const stepStatuses = useMemo(() => {
    const base = buildStepStatuses(completedStepIds)
    if (runOverlay.key !== cacheKey) {
      return base
    }

    return { ...base, ...runOverlay.statuses }
  }, [completedStepIds, runOverlay, cacheKey])

  const selectedWorkflow = useMemo(
    () =>
      workflowDefinitions.find((workflow) => workflow.id === selectedWorkflowId),
    [selectedWorkflowId],
  )

  const runPlanLabel = useMemo(() => {
    if (plannedStepIds.length === 0) {
      return runMode === 'full'
        ? 'Will run: nothing new (all steps already completed for this org/project).'
        : 'Will run: nothing new (selected flow already completed for this org/project).'
    }

    const titles = plannedStepIds.map((stepId) => {
      const step = workflowDefinitions.find((workflow) => workflow.id === stepId)
      return step?.title ?? stepId
    })

    return `Will run: ${titles.join(' → ')}`
  }, [plannedStepIds, runMode])

  const profileKeys = Object.keys(profiles)

  const persistCompletionCache = (updater) => {
    setCompletionCache((previous) => {
      const nextCache = typeof updater === 'function' ? updater(previous) : updater
      localStorage.setItem(COMPLETION_CACHE_KEY, JSON.stringify(nextCache))
      return nextCache
    })
  }

  const addLog = (message) => {
    const timestamp = new Date().toLocaleTimeString()
    setRunLogs((previousLogs) => [
      `[${timestamp}] ${message}`,
      ...previousLogs,
    ].slice(0, 120))
  }

  const saveProfile = () => {
    if (!profileName || !orgUrl.trim()) {
      setRunMessage('Enter profile name and org URL before saving.')
      return
    }

    const normalized = normalizeAdoOrgUrl(orgUrl)
    if (!normalized.ok) {
      setRunMessage(`Cannot save profile: ${normalized.error}`)
      return
    }

    const next = { ...profiles, [profileName]: { orgUrl: normalized.url } }
    localStorage.setItem(PROFILES_KEY, JSON.stringify(next))
    setProfiles(next)
    setOrgUrl(normalized.url)
    setRunMessage(
      `Saved profile "${profileName}" (org URL only; PAT stays in this browser session).`,
    )
  }

  const loadProfile = (name) => {
    const profile = profiles[name]
    if (!profile) {
      return
    }

    setProfileName(name)
    setOrgUrl(profile.orgUrl)
    setPat('')
    setProjects([])
    setProjectsFetched(false)
    setProcesses([])
    setProcessesFetched(false)
    setApiStatusText(`Loaded profile "${name}". Re-enter the PAT, then fetch projects.`)
    setRunMessage(`Loaded profile "${name}". Re-enter the PAT for this session.`)
  }

  const handleFetchProjects = async () => {
    if (!connectionReady) {
      return
    }

    setFetchingProjects(true)
    setProjectsFetched(false)
    setProjects([])
    setApiStatusText('Fetching projects...')

    try {
      const list = await fetchProjects(effectiveOrgUrl, pat.trim())
      setProjects(list)
      setProjectsFetched(true)
      setApiStatusText(
        `Connected. Found ${list.length} project${list.length === 1 ? '' : 's'}.`,
      )
      setRunMessage(`Fetched ${list.length} project${list.length === 1 ? '' : 's'} from Azure DevOps.`)
      addLog(`API: fetched ${list.length} projects`)
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch projects'
      setProjectsFetched(false)
      setApiStatusText(message)
      setRunMessage(`Fetch projects failed: ${message}`)
      addLog(`API error: ${message}`)
    } finally {
      setFetchingProjects(false)
    }
  }

  const handleFetchProcesses = async () => {
    if (!connectionReady) {
      return
    }

    setFetchingProcesses(true)
    setProcessesFetched(false)
    setProcesses([])
    setApiStatusText('Fetching processes...')

    try {
      const list = await fetchProcesses(effectiveOrgUrl, pat.trim())
      setProcesses(list)
      setProcessesFetched(true)
      setApiStatusText(
        `Fetched ${list.length} process${list.length === 1 ? '' : 'es'}.`,
      )
      setRunMessage(`Fetched ${list.length} process${list.length === 1 ? '' : 'es'} from Azure DevOps.`)
      addLog(`API: fetched ${list.length} processes`)
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch processes'
      setProcessesFetched(false)
      setApiStatusText(message)
      setRunMessage(`Fetch processes failed: ${message}`)
      addLog(`API error: ${message}`)
    } finally {
      setFetchingProcesses(false)
    }
  }

  const clearCompletionCache = () => {
    if (!cacheKey) {
      setRunOverlay({ key: null, statuses: {} })
      setRunMessage('Enter org URL and process name to clear a scoped completion cache.')
      return
    }

    persistCompletionCache((previous) => {
      const nextCache = { ...previous }
      delete nextCache[cacheKey]
      return nextCache
    })
    setRunOverlay({ key: cacheKey, statuses: {} })
    setRunMessage('Completion cache cleared for this org/process/project. Steps reset to Not run.')
  }

  const persistWorkbookApply = (applied) => {
    if (!applied?.fingerprint || !applied.processName) {
      return
    }

    const key = workbookApplyKey(effectiveOrgUrl, applied.processName)
    const next = {
      ...workbookApplies,
      [key]: {
        fingerprint: applied.fingerprint,
        templatePath: templatePath.trim(),
        workbookVersion: workbookVersion.trim(),
        appliedAt: new Date().toISOString(),
      },
    }
    localStorage.setItem(WORKBOOK_APPLIES_KEY, JSON.stringify(next))
    setWorkbookApplies(next)
  }

  const setStepStatus = (stepId, status) => {
    setRunOverlay((current) => ({
      key: cacheKey,
      statuses: {
        ...(current.key === cacheKey ? current.statuses : {}),
        [stepId]: status,
      },
    }))
  }

  const cancelWorkflow = () => {
    abortControllerRef.current?.abort()
  }

  const openPathPicker = (target, mode) => {
    setPathPickerTarget(target)
    setPathPickerMode(mode)
    setPathPickerOpen(true)
  }

  const previewPlan = async () => {
    if (!connectionReady) {
      setPlanError('Set org URL and PAT in the connection profile first.')
      return
    }
    if (!nameValidation.ok) {
      setPlanError(nameValidation.messages.join(' '))
      return
    }

    setPlanLoading(true)
    setPlanError('')
    setPlanResult(null)
    setRunMessage('Requesting dry-run plan from local runner...')

    try {
      const response = await fetch('/api/plan/dry-run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          org_url: effectiveOrgUrl,
          process_name: processName.trim(),
          project_name: projectName.trim(),
          excel_file: templatePath.trim(),
          catalog_source_dir: catalogSourceDir.trim() || null,
          workbook_version: workbookVersion.trim(),
          update_policy: updatePolicy,
          confirm_process_update: confirmProcessUpdate,
          confirm_project_update: confirmProjectUpdate,
          known_process_exists: targetAssessment.process.exists,
          known_project_exists: targetAssessment.project.exists,
        }),
      })

      const payload = await response.json().catch(() => ({}))
      if (!response.ok) {
        throw new Error(payload.detail || `Runner error (${response.status})`)
      }

      setPlanResult(payload)
      setRunMessage(
        payload.ok
          ? `Dry-run plan ready: ${payload.actions?.length ?? 0} actions from ${payload.summary?.counts?.catalog_rows ?? 0} catalog rows.`
          : `Dry-run blocked: ${(payload.errors || []).join(' ')}`,
      )
      addLog(
        `Runner dry-run: fingerprint ${payload.workbook_fingerprint}; steps ${
          payload.steps?.map((step) => step.id).join(' → ') || 'none'
        }`,
      )
    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : 'Failed to reach local runner. Start it with npm run runner.'
      setPlanError(message)
      setRunMessage(`Dry-run failed: ${message}`)
    } finally {
      setPlanLoading(false)
    }
  }

  const runWorkflow = async () => {
    if (isRunningRef.current) {
      return
    }

    if (!connectionReady) {
      setRunMessage('Set org URL and PAT in the connection profile first.')
      return
    }

    if (!nameValidation.ok) {
      setRunMessage(`Name/policy validation failed: ${nameValidation.messages.join(' ')}`)
      return
    }

    isRunningRef.current = true
    const abortController = new AbortController()
    abortControllerRef.current = abortController

    setIsRunning(true)
    setRunLogs([])
    setRunOverlay({ key: cacheKey, statuses: {} })
    setRunMessage(
      executionMode === 'runner'
        ? dryRun
          ? 'Running local runner apply dry-run (no ADO mutations)...'
          : 'Running local runner apply against Azure DevOps...'
        : executionMode === 'api'
          ? 'Running flow (live Azure DevOps API reads)...'
          : 'Running flow (simulation)...',
    )

    const runConfig = {
      orgUrl: effectiveOrgUrl,
      pat: pat.trim(),
      templatePath: templatePath.trim(),
      catalogSourceDir: catalogSourceDir.trim(),
      workbookVersion: workbookVersion.trim(),
      projectName: projectName.trim(),
      processName: processName.trim(),
      threads: parseBoundedInt(threads, Number.NaN),
      maxRetries: parseBoundedInt(maxRetries, Number.NaN),
      dryRun,
      layoutSheet: layoutSheet.trim(),
      rootAreaPath: rootAreaPath.trim() || projectName.trim(),
      backlogSheet: backlogSheet.trim(),
      updatePolicy,
      confirmProcessUpdate,
      confirmProjectUpdate,
      knownProcesses: processes,
      knownProjects: projects,
      lastAppliedWorkbook,
      assessment: targetAssessment,
      executionMode,
    }

    try {
      if (executionMode === 'runner') {
        const plannedSteps = resolveTargetSteps(runMode, selectedWorkflowId, completedStepIds)
        const job = await runRunnerJob(
          buildRunnerJobBody({
            orgUrl: runConfig.orgUrl,
            pat: runConfig.pat,
            processName: runConfig.processName,
            projectName: runConfig.projectName,
            templatePath: runConfig.templatePath,
            catalogSourceDir: runConfig.catalogSourceDir,
            workbookVersion: runConfig.workbookVersion,
            updatePolicy,
            confirmProcessUpdate,
            confirmProjectUpdate,
            knownProcessExists: targetAssessment.process.exists,
            knownProjectExists: targetAssessment.project.exists,
            rootAreaPath: runConfig.rootAreaPath,
            mode: 'apply',
            applyDryRun: dryRun,
            steps: plannedSteps.length ? plannedSteps : null,
            convertMarkdownToHtml,
          }),
          {
            signal: abortController.signal,
            onEvent: (event) => {
              if (abortController.signal.aborted) {
                return
              }
              const stepId = event.stepId
              const message = event.message || event.type
              if (event.type === 'step-started' && stepId) {
                setStepStatus(stepId, 'running')
              }
              if (event.type === 'step-completed' && stepId) {
                setStepStatus(stepId, 'completed')
              }
              if (event.type === 'step-skipped' && stepId) {
                setStepStatus(stepId, 'skipped')
              }
              if ((event.type === 'step-failed' || event.type === 'job-error') && stepId) {
                setStepStatus(stepId, 'failed')
              }
              addLog(stepId ? `${stepId}: ${message}` : message)
            },
          },
        )

        const activeCacheKey = buildCacheKey(
          runConfig.orgUrl,
          runConfig.processName,
          runConfig.projectName,
        )
        const applyOk = job.status === 'succeeded' && (job.apply_result?.ok ?? false)
        if (applyOk) {
          const finished = Object.keys(job.apply_result?.step_results || {})
          const nextCompleted = Array.from(new Set([...completedStepIds, ...finished]))
          if (activeCacheKey) {
            persistCompletionCache((previous) => ({
              ...previous,
              [activeCacheKey]: nextCompleted,
            }))
          }
          if (finished.includes('process') && job.result?.workbook_fingerprint) {
            persistWorkbookApply({
              fingerprint: job.result.workbook_fingerprint,
              processName: runConfig.processName,
            })
          }
          setRunOverlay({ key: activeCacheKey, statuses: {} })
          const out = job.apply_result?.output_dir
          setRunMessage(
            dryRun
              ? `Runner apply dry-run succeeded${out ? ` — artifacts in ${out}` : ''}.`
              : `Runner apply succeeded${out ? ` — artifacts in ${out}` : ''}.`,
          )
        } else {
          setRunMessage(`Runner job failed: ${job.error || 'unknown error'}`)
        }
      } else {
        const result = await runWorkflowFlow({
          mode: runMode,
          selectedWorkflowId,
          completedStepIds,
          config: runConfig,
          signal: abortController.signal,
          executeStep: stepExecutors[executionMode] ?? stepExecutors.simulate,
          onEvent: (event) => {
            if (abortController.signal.aborted) {
              return
            }

            if (event.type === 'target-assessment') {
              addLog(
                `Assessment: process ${event.assessment.process.recommendedAction}, project ${event.assessment.project.recommendedAction}. ${event.assessment.workbook.message}`,
              )
            }

            if (event.type === 'step-skipped') {
              setStepStatus(event.stepId, 'skipped')
              addLog(`Skipped ${event.stepId}: ${event.message}`)
            }

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

        const nextCompleted = Array.isArray(result.completedStepIds)
          ? result.completedStepIds
          : completedStepIds

        const activeCacheKey = buildCacheKey(
          runConfig.orgUrl,
          runConfig.processName,
          runConfig.projectName,
        )
        if (activeCacheKey) {
          persistCompletionCache((previous) => ({
            ...previous,
            [activeCacheKey]: nextCompleted,
          }))
        }

        if (result.appliedWorkbook) {
          persistWorkbookApply(result.appliedWorkbook)
        }

        if (result.ok) {
          setRunOverlay({ key: activeCacheKey, statuses: {} })
          setRunMessage(
            result.message ??
              `Flow completed successfully in ${runMode === 'full' ? 'full' : 'dependency-aware'} mode (${executionMode}).`,
          )
        } else if (result.error?.code === 'ABORTED') {
          setRunOverlay((current) => {
            const statuses =
              current.key === activeCacheKey
                ? Object.fromEntries(
                    Object.entries(current.statuses).filter(
                      ([, status]) => status === 'failed' || status === 'completed',
                    ),
                  )
                : {}
            return { key: activeCacheKey, statuses }
          })
          setRunMessage('Flow cancelled.')
          addLog('Run cancelled by user.')
        } else {
          setRunOverlay((current) => {
            const statuses =
              current.key === activeCacheKey
                ? Object.fromEntries(
                    Object.entries(current.statuses).filter(
                      ([, status]) =>
                        status === 'failed' || status === 'skipped' || status === 'completed',
                    ),
                  )
                : {}
            return { key: activeCacheKey, statuses }
          })
          setRunMessage(`Flow failed: ${result.error.message}`)
        }
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Unexpected runner error.'
      setRunMessage(`Flow failed: ${message}`)
      addLog(`Runner error: ${message}`)
    } finally {
      isRunningRef.current = false
      abortControllerRef.current = null
      setIsRunning(false)
    }
  }

  return (
    <main className="app-shell">
      <header className="app-header">
        <h1>BPC Azure DevOps React Runner</h1>
        <p>
          Process and page layout finish first; project creation runs only after those
          complete. Existing process/project selections are verified before updates, and
          later spreadsheets can apply as process-template deltas.
        </p>
        <p className="mode-banner">
          Execution mode:{' '}
          <strong>
            {executionMode === 'runner'
              ? 'Runner'
              : executionMode === 'api'
                ? 'API'
                : 'simulation'}
          </strong>
          {executionMode === 'runner'
            ? ' — local Excel→IR→apply engine (HTML + markdown catalog fields); start with npm run runner.'
            : executionMode === 'api'
              ? ' — live ADO reads via /ado-proxy (credential proof + inventory checks).'
              : ' — local timed stubs; use Runner mode for real apply.'}
        </p>
      </header>

      <ConnectionPanel
        profileName={profileName}
        onProfileNameChange={setProfileName}
        profileKeys={profileKeys}
        onSaveProfile={saveProfile}
        onLoadProfile={loadProfile}
        orgUrl={orgUrl}
        onOrgUrlChange={setOrgUrl}
        pat={pat}
        onPatChange={setPat}
        showPat={showPat}
        onToggleShowPat={() => setShowPat((value) => !value)}
        connectionReady={connectionReady}
        connectionStatusText={apiStatusText}
        fetchingProjects={fetchingProjects}
        projectsFetched={projectsFetched}
        onFetchProjects={handleFetchProjects}
        fetchingProcesses={fetchingProcesses}
        processesFetched={processesFetched}
        onFetchProcesses={handleFetchProcesses}
        executionMode={executionMode}
        onExecutionModeChange={setExecutionMode}
        disabled={isRunning}
      />

      <CollapsibleSection
        title="2. Process & project names"
        defaultOpen
        summary={
          [
            processName.trim() || 'No process name',
            projectName.trim() || 'No project name',
            updatePolicy,
          ].join(' · ')
        }
      >
        <p className="section-lead">
          Type the names to create. Optionally fetch existing inventory in the connection
          profile to detect collisions; suggestions appear as you type.
        </p>
        <div className="grid-2">
          <label>
            Process name to create
            <input
              list="process-name-suggestions"
              value={processName}
              onChange={(event) => setProcessName(event.target.value)}
              placeholder="e.g. Business Process Catalog"
              disabled={isRunning}
            />
            <datalist id="process-name-suggestions">
              {processes.map((process) => (
                <option key={process.id} value={process.name} />
              ))}
            </datalist>
            {nameValidation.errors.processName.map((message) => (
              <small key={message} className="field-error">
                {message}
              </small>
            ))}
            {processName.trim() && nameValidation.errors.processName.length === 0 ? (
              <small className="field-hint">
                {targetAssessment.process.exists
                  ? `Matches existing process → ${targetAssessment.process.recommendedAction}`
                  : 'New process → will be created'}
              </small>
            ) : null}
          </label>

          <label>
            Project name to create
            <input
              list="project-name-suggestions"
              value={projectName}
              onChange={(event) => setProjectName(event.target.value)}
              placeholder="e.g. Contoso-BPC"
              disabled={isRunning}
            />
            <datalist id="project-name-suggestions">
              {projects.map((project) => (
                <option key={project.id} value={project.name} />
              ))}
            </datalist>
            {nameValidation.errors.projectName.map((message) => (
              <small key={message} className="field-error">
                {message}
              </small>
            ))}
            {projectName.trim() && nameValidation.errors.projectName.length === 0 ? (
              <small className="field-hint">
                {targetAssessment.project.exists
                  ? `Matches existing project → ${targetAssessment.project.recommendedAction}`
                  : 'New project → created after process + layout'}
              </small>
            ) : null}
          </label>
        </div>

        <div className="assessment-grid name-policy-block">
          <label>
            Existing target policy
            <select
              value={updatePolicy}
              onChange={(event) => setUpdatePolicy(event.target.value)}
              disabled={isRunning}
            >
              <option value="require-confirmation">Require confirmation before update</option>
              <option value="always-update">Always update existing targets</option>
              <option value="skip-existing">Skip steps for existing targets</option>
              <option value="create-only">Create only (fail if exists)</option>
            </select>
          </label>
          {updatePolicy === 'require-confirmation' && targetAssessment.process.exists ? (
            <label className="checkbox-row">
              <input
                type="checkbox"
                checked={confirmProcessUpdate}
                onChange={(event) => setConfirmProcessUpdate(event.target.checked)}
                disabled={isRunning}
              />
              Confirm updating existing process / applying spreadsheet changes
            </label>
          ) : null}
          {updatePolicy === 'require-confirmation' && targetAssessment.project.exists ? (
            <label className="checkbox-row">
              <input
                type="checkbox"
                checked={confirmProjectUpdate}
                onChange={(event) => setConfirmProjectUpdate(event.target.checked)}
                disabled={isRunning}
              />
              Confirm updating / reusing existing project
            </label>
          ) : null}
          {nameValidation.errors.policy.map((message) => (
            <small key={message} className="field-error">
              {message}
            </small>
          ))}
          <p className="field-hint">{targetAssessment.workbook.message}</p>
        </div>
      </CollapsibleSection>

      <CollapsibleSection
        title="3. Workflow selection"
        defaultOpen
        summary={`${runMode === 'full' ? 'Full flow' : 'Dependency-aware'} · ${runPlanLabel}`}
      >
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
        <p className="run-plan" role="status">
          {runPlanLabel}
        </p>
        <div className="workflow-list">
          {workflowDefinitions.map((workflow) => {
            const isPlanned = plannedStepIds.includes(workflow.id)
            const isCachedSkip =
              completedStepIds.includes(workflow.id) &&
              (runMode === 'full' ||
                workflowDefinitions.findIndex((item) => item.id === workflow.id) <=
                  workflowDefinitions.findIndex(
                    (item) => item.id === selectedWorkflowId,
                  ))
            const cardActive =
              runMode === 'full' ? isPlanned || isCachedSkip : selectedWorkflowId === workflow.id

            return (
              <button
                key={workflow.id}
                type="button"
                className={`workflow-card ${cardActive ? 'active' : ''} ${
                  runMode === 'full' && isPlanned ? 'planned' : ''
                }`}
                onClick={() => {
                  if (runMode === 'full') {
                    return
                  }
                  setSelectedWorkflowId(workflow.id)
                }}
                disabled={isRunning || runMode === 'full'}
                aria-disabled={runMode === 'full'}
              >
                <strong>
                  {workflow.title}
                  <span className={`status-chip ${stepStatuses[workflow.id] ?? 'idle'}`}>
                    {statusLabelMap[stepStatuses[workflow.id] ?? 'idle']}
                  </span>
                </strong>
                <span>{workflow.script}</span>
                <small>{workflow.description}</small>
                {runMode === 'full' && isCachedSkip && !isPlanned ? (
                  <small className="plan-hint">Cached — will skip</small>
                ) : null}
                {runMode === 'full' && isPlanned ? (
                  <small className="plan-hint">In this run</small>
                ) : null}
              </button>
            )
          })}
        </div>
      </CollapsibleSection>

      <section className="panel">
        <h2>4. Run configuration</h2>
        <div className="grid-2">
          <label>
            Template workbook path
            <div className="path-picker-row">
              <input
                value={templatePath}
                onChange={(event) => {
                  setTemplatePath(event.target.value)
                  setConfirmProcessUpdate(false)
                }}
                disabled={isRunning}
              />
              <button
                type="button"
                className="secondary-inline"
                onClick={() => openPathPicker('template', 'file')}
                disabled={isRunning}
              >
                Browse…
              </button>
            </div>
          </label>
          <label>
            Catalog source folder
            <div className="path-picker-row">
              <input
                value={catalogSourceDir}
                onChange={(event) => setCatalogSourceDir(event.target.value)}
                placeholder="/Users/bill/BPC Files"
                disabled={isRunning}
              />
              <button
                type="button"
                className="secondary-inline"
                onClick={() => openPathPicker('catalog', 'folder')}
                disabled={isRunning}
              >
                Browse…
              </button>
            </div>
          </label>
          <label>
            Workbook version / revision label
            <input
              value={workbookVersion}
              onChange={(event) => {
                setWorkbookVersion(event.target.value)
                setConfirmProcessUpdate(false)
              }}
              placeholder="e.g. 2026.08 or sprint-42"
              disabled={isRunning}
            />
          </label>
          <label>
            Threads (for layout step)
            <input
              type="number"
              min="1"
              max="16"
              value={Number.isNaN(threads) ? '' : threads}
              onChange={(event) =>
                setThreads(parseBoundedInt(event.target.value, Number.NaN))
              }
              disabled={isRunning}
            />
          </label>
          <label>
            Retry count
            <input
              type="number"
              min="0"
              max="5"
              value={Number.isNaN(maxRetries) ? '' : maxRetries}
              onChange={(event) =>
                setMaxRetries(parseBoundedInt(event.target.value, Number.NaN))
              }
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
            {executionMode === 'runner'
              ? 'Apply dry-run (plan writers, no ADO mutations)'
              : 'Dry-run backlog configuration'}
          </label>
          <div className="stack-field">
            <label className="checkbox-row">
              <input
                type="checkbox"
                checked={convertMarkdownToHtml}
                onChange={(event) => setConvertMarkdownToHtml(event.target.checked)}
                disabled={isRunning}
              />
              Convert Markdown large-text fields to HTML
            </label>
            <small className="field-hint">
              Default preserves markdown (ADO Toolkit style) and sets
              multilineFieldsFormat=Markdown. Enable only to store HTML instead.
            </small>
          </div>
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
          className="run-button secondary"
          onClick={loadRunnerDefaults}
          disabled={isRunning || planLoading}
        >
          Load runner defaults
        </button>

        <button
          type="button"
          className="run-button"
          onClick={previewPlan}
          disabled={planLoading || isRunning || !connectionReady || !nameValidation.ok}
        >
          {planLoading ? 'Building plan...' : 'Preview plan (dry-run)'}
        </button>

        <button
          type="button"
          className="run-button"
          onClick={runWorkflow}
          disabled={
            isRunning ||
            !connectionReady ||
            !nameValidation.ok
          }
        >
          {isRunning ? 'Running...' : 'Run selected flow'}
        </button>

        <button
          type="button"
          className="run-button secondary"
          onClick={cancelWorkflow}
          disabled={!isRunning}
        >
          Cancel run
        </button>

        <button
          type="button"
          className="run-button secondary"
          onClick={clearCompletionCache}
          disabled={isRunning}
        >
          Clear completion cache
        </button>

        {planError ? <p className="field-error">{planError}</p> : null}

        {planResult ? (
          <div className="plan-preview">
            <h3>Dry-run plan</h3>
            <p className="field-hint">
              IR {planResult.ir_version} · fingerprint {planResult.workbook_fingerprint}
            </p>
            <p className="field-hint">
              Counts: {planResult.summary?.counts?.work_item_types ?? 0} WITs,{' '}
              {planResult.summary?.counts?.fields ?? 0} fields,{' '}
              {planResult.summary?.counts?.teams ?? 0} teams,{' '}
              {planResult.summary?.counts?.area_paths ?? 0} areas,{' '}
              {planResult.summary?.counts?.catalog_rows ?? 0} catalog rows
            </p>
            <ol className="plan-step-list">
              {(planResult.steps || []).map((step) => (
                <li key={step.id}>
                  <strong>
                    {step.title} ({step.planned_action})
                  </strong>
                  <span> — {step.summary}</span>
                </li>
              ))}
            </ol>
            {(planResult.warnings || []).length > 0 ? (
              <ul className="plan-warnings">
                {planResult.warnings.map((warning) => (
                  <li key={warning}>{warning}</li>
                ))}
              </ul>
            ) : null}
            {(planResult.errors || []).length > 0 ? (
              <ul className="plan-errors">
                {planResult.errors.map((error) => (
                  <li key={error}>{error}</li>
                ))}
              </ul>
            ) : null}
          </div>
        ) : null}

        <div className="run-log" role="status" aria-live="polite">
          <p>{runMessage}</p>
          <pre>{runLogs.length > 0 ? runLogs.join('\n') : 'No execution logs yet.'}</pre>
        </div>
      </section>

      {pathPickerOpen ? (
        <PathPickerModal
          key={`${pathPickerTarget}:${pathPickerMode}:${pathPickerTarget === 'template' ? templatePath : catalogSourceDir}`}
          title={
            pathPickerTarget === 'catalog'
              ? 'Select catalog source folder'
              : 'Select template workbook or folder'
          }
          mode={pathPickerMode}
          initialValue={
            pathPickerTarget === 'catalog' ? catalogSourceDir : templatePath
          }
          onClose={() => setPathPickerOpen(false)}
          onConfirm={(nextPath) => {
            if (pathPickerTarget === 'catalog') {
              setCatalogSourceDir(nextPath)
            } else {
              setTemplatePath(nextPath)
              setConfirmProcessUpdate(false)
            }
            setPathPickerOpen(false)
          }}
        />
      ) : null}
    </main>
  )
}

export default App
