export const workflowDefinitions = [
  {
    id: 'creation',
    title: '1. Project & Process Creation',
    script: '1_ADO_Creation_Script (Preview).py',
    description:
      'Create project, process shell, work item types, fields, and picklists from the workbook template.',
    inputs: ['Template workbook path', 'Project name', 'Process name'],
    durationMs: 900,
  },
  {
    id: 'layout',
    title: '2. Page Layout Setup',
    script: '2_ADO_Page_Layout_Script_Threaded (Preview).py',
    description:
      'Apply form/page layout customizations for work item types using threaded execution settings.',
    inputs: ['Threads', 'Layout worksheet name'],
    durationMs: 750,
  },
  {
    id: 'teams',
    title: '3. Teams & Areas Setup',
    script: '3_ADO_Teams_Areas_Script (Preview).py',
    description:
      'Create teams and area paths from template values to align ownership and navigation structure.',
    inputs: ['Root area path', 'Team mode'],
    durationMs: 650,
  },
  {
    id: 'backlog',
    title: '4. Backlog Configuration',
    script: '4_ADO_Backlog_Config_Script (Preview).py',
    description:
      'Configure backlog levels, visibility, and sequencing for the Business Process Catalog workflow.',
    inputs: ['Backlog worksheet name', 'Apply dry-run mode'],
    durationMs: 700,
  },
]

const stepOrder = workflowDefinitions.map((workflow) => workflow.id)
const transientErrorCodes = new Set(['ADO_THROTTLED', 'NETWORK_TIMEOUT'])

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

const buildFlowError = (code, message, transient = false) => {
  const error = new Error(message)
  error.code = code
  error.transient = transient
  return error
}

export function validateRunnerConfig(config) {
  const errors = []

  if (!config.orgUrl) {
    errors.push('Azure DevOps org URL is required.')
  } else {
    try {
      const parsed = new URL(config.orgUrl)
      const allowedHost = parsed.hostname.includes('dev.azure.com') || parsed.hostname.endsWith('.visualstudio.com')
      if (!allowedHost) {
        errors.push('Org URL must point to dev.azure.com or *.visualstudio.com.')
      }
    } catch {
      errors.push('Org URL must be a valid URL.')
    }
  }

  if (!config.pat || config.pat.length < 20) {
    errors.push('PAT is required and should be at least 20 characters.')
  }

  if (!config.templatePath || !config.templatePath.toLowerCase().endsWith('.xlsx')) {
    errors.push('Template workbook path must point to an .xlsx file.')
  }

  if (!config.projectName || config.projectName.trim().length < 3) {
    errors.push('Project name must be at least 3 characters.')
  }

  if (!config.processName || config.processName.trim().length < 3) {
    errors.push('Process name must be at least 3 characters.')
  }

  if (Number.isNaN(config.maxRetries) || config.maxRetries < 0 || config.maxRetries > 5) {
    errors.push('Retry count must be between 0 and 5.')
  }

  if (Number.isNaN(config.threads) || config.threads < 1 || config.threads > 16) {
    errors.push('Thread count must be between 1 and 16.')
  }

  return errors
}

const resolveTargetSteps = (mode, selectedWorkflowId, completedSet) => {
  if (mode === 'full') {
    return stepOrder.filter((stepId) => !completedSet.has(stepId))
  }

  const selectedIndex = stepOrder.indexOf(selectedWorkflowId)
  if (selectedIndex < 0) {
    return []
  }

  return stepOrder.slice(0, selectedIndex + 1).filter((stepId) => !completedSet.has(stepId))
}

const emit = (onEvent, event) => {
  if (typeof onEvent === 'function') {
    onEvent({
      timestamp: new Date().toISOString(),
      ...event,
    })
  }
}

async function simulateStepExecution(step, config) {
  await sleep(step.durationMs)

  if (config.orgUrl.includes('throttle-test') && step.id === 'layout') {
    throw buildFlowError(
      'ADO_THROTTLED',
      'Azure DevOps rate limit reached while applying layouts.',
      true,
    )
  }

  if (step.id === 'creation' && config.projectName.trim().toLowerCase() === 'invalid') {
    throw buildFlowError('INVALID_PROJECT', 'Project name is not valid for creation.', false)
  }

  const warnings = []

  if (step.id === 'layout' && config.threads > 8) {
    warnings.push('High thread count can trigger ADO throttling; 2-8 is recommended.')
  }

  if (step.id === 'backlog' && config.dryRun) {
    warnings.push('Dry-run enabled. Backlog changes are evaluated but not committed.')
  }

  return {
    details: `${step.script} completed for project ${config.projectName}.`,
    warnings,
  }
}

async function runStepWithRetry(step, config, onEvent) {
  const maxAttempts = config.maxRetries + 1

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    emit(onEvent, {
      type: 'step-attempt',
      stepId: step.id,
      stepTitle: step.title,
      attempt,
      maxAttempts,
      message: `Attempt ${attempt}/${maxAttempts}`,
    })

    try {
      const result = await simulateStepExecution(step, config)
      return { ok: true, ...result }
    } catch (error) {
      const isTransient = transientErrorCodes.has(error.code) || error.transient === true
      const isLastAttempt = attempt === maxAttempts

      emit(onEvent, {
        type: 'step-error',
        stepId: step.id,
        stepTitle: step.title,
        attempt,
        maxAttempts,
        transient: isTransient,
        message: error.message,
      })

      if (!isTransient || isLastAttempt) {
        return { ok: false, error }
      }

      await sleep(250 * attempt)
    }
  }

  return {
    ok: false,
    error: buildFlowError('UNKNOWN', 'Step failed with an unknown error.', false),
  }
}

export async function runWorkflowFlow({
  mode,
  selectedWorkflowId,
  completedStepIds,
  config,
  onEvent,
}) {
  const validationErrors = validateRunnerConfig(config)
  if (validationErrors.length > 0) {
    return {
      ok: false,
      completedStepIds,
      error: buildFlowError('VALIDATION', validationErrors.join(' '), false),
    }
  }

  const completedSet = new Set(completedStepIds)
  const targetStepIds = resolveTargetSteps(mode, selectedWorkflowId, completedSet)

  if (targetStepIds.length === 0) {
    return {
      ok: true,
      completedStepIds,
      message: 'No new steps required. Selected flow is already complete.',
    }
  }

  const nextCompletedSet = new Set(completedStepIds)

  for (const stepId of targetStepIds) {
    const step = workflowDefinitions.find((workflow) => workflow.id === stepId)
    if (!step) {
      return {
        ok: false,
        completedStepIds: Array.from(nextCompletedSet),
        error: buildFlowError('MISSING_STEP', `Workflow step not found: ${stepId}`, false),
      }
    }

    emit(onEvent, {
      type: 'step-started',
      stepId: step.id,
      stepTitle: step.title,
      message: `Starting ${step.script}`,
    })

    const result = await runStepWithRetry(step, config, onEvent)

    if (!result.ok) {
      emit(onEvent, {
        type: 'step-failed',
        stepId: step.id,
        stepTitle: step.title,
        message: result.error.message,
      })

      return {
        ok: false,
        completedStepIds: Array.from(nextCompletedSet),
        error: result.error,
      }
    }

    nextCompletedSet.add(step.id)

    emit(onEvent, {
      type: 'step-completed',
      stepId: step.id,
      stepTitle: step.title,
      message: result.details,
      warnings: result.warnings,
    })

    if (result.warnings.length > 0) {
      for (const warning of result.warnings) {
        emit(onEvent, {
          type: 'step-warning',
          stepId: step.id,
          stepTitle: step.title,
          message: warning,
        })
      }
    }
  }

  return {
    ok: true,
    completedStepIds: Array.from(nextCompletedSet),
  }
}
