/**
 * Local FastAPI runner client (Excel → IR → plan/apply).
 */

const sleep = (ms, signal) =>
  new Promise((resolve, reject) => {
    if (signal?.aborted) {
      reject(new Error('Run cancelled.'))
      return
    }
    const timer = setTimeout(() => {
      signal?.removeEventListener('abort', onAbort)
      resolve()
    }, ms)
    const onAbort = () => {
      clearTimeout(timer)
      reject(new Error('Run cancelled.'))
    }
    signal?.addEventListener('abort', onAbort, { once: true })
  })

async function parsePayload(response) {
  const payload = await response.json().catch(() => ({}))
  if (!response.ok) {
    const detail =
      typeof payload.detail === 'string'
        ? payload.detail
        : payload.detail
          ? JSON.stringify(payload.detail)
          : `Runner error (${response.status})`
    throw new Error(detail)
  }
  return payload
}

export async function createRunnerJob(body, { signal } = {}) {
  const response = await fetch('/api/jobs', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal,
  })
  return parsePayload(response)
}

export async function getRunnerJob(jobId, { signal } = {}) {
  const response = await fetch(`/api/jobs/${encodeURIComponent(jobId)}`, { signal })
  return parsePayload(response)
}

/**
 * Create an apply/dry-run job and poll until terminal status.
 * Invokes onEvent for each new runner event.
 */
export async function runRunnerJob(body, { signal, onEvent, pollMs = 750 } = {}) {
  let job = await createRunnerJob(body, { signal })
  let seenEvents = 0

  const publish = (events = []) => {
    if (typeof onEvent !== 'function') {
      return
    }
    for (const event of events.slice(seenEvents)) {
      onEvent(event)
    }
    seenEvents = events.length
  }

  publish(job.events)

  while (job.status === 'queued' || job.status === 'running') {
    if (signal?.aborted) {
      throw new Error('Run cancelled.')
    }
    await sleep(pollMs, signal)
    job = await getRunnerJob(job.id, { signal })
    publish(job.events)
  }

  return job
}

export function buildRunnerJobBody({
  orgUrl,
  pat,
  processName,
  projectName,
  templatePath,
  catalogSourceDir,
  workbookVersion,
  updatePolicy,
  confirmProcessUpdate,
  confirmProjectUpdate,
  knownProcessExists,
  knownProjectExists,
  rootAreaPath,
  mode = 'apply',
  applyDryRun = false,
  steps = null,
  catalogLimit = null,
  convertMarkdownToHtml = false,
}) {
  return {
    org_url: orgUrl,
    pat,
    process_name: processName,
    project_name: projectName,
    excel_file: templatePath,
    catalog_source_dir: catalogSourceDir || null,
    workbook_version: workbookVersion || '',
    update_policy: updatePolicy,
    confirm_process_update: Boolean(confirmProcessUpdate),
    confirm_project_update: Boolean(confirmProjectUpdate),
    known_process_exists: Boolean(knownProcessExists),
    known_project_exists: Boolean(knownProjectExists),
    root_area_path: rootAreaPath || projectName,
    mode,
    apply_dry_run: Boolean(applyDryRun),
    steps,
    catalog_limit: catalogLimit,
    convert_markdown_to_html: Boolean(convertMarkdownToHtml),
  }
}
