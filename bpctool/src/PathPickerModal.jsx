import { useEffect, useId, useRef, useState } from 'react'

/**
 * Modal path picker for workbook files or folders.
 * Uses File System Access API when available; falls back to file input + typed path.
 */
export default function PathPickerModal({
  title = 'Select path',
  mode = 'file',
  initialValue = '',
  accept = '.xlsx,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  onClose,
  onConfirm,
}) {
  const titleId = useId()
  const fileInputRef = useRef(null)
  const folderInputRef = useRef(null)
  const [draft, setDraft] = useState(initialValue)
  const [note, setNote] = useState('')

  useEffect(() => {
    const onKeyDown = (event) => {
      if (event.key === 'Escape') {
        onClose()
      }
    }

    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [onClose])

  const applyBrowserFile = (file) => {
    if (!file) {
      return
    }

    const maybePath = file.path || file.webkitRelativePath || file.name
    setDraft(maybePath)
    setNote(
      file.path
        ? 'Full path selected from the system dialog.'
        : 'Browser provided a file name only. Edit the path if your runner needs a full disk location (for example C:\\templates\\guide.xlsx).',
    )
  }

  const browseFile = async () => {
    if (typeof window.showOpenFilePicker === 'function') {
      try {
        const [handle] = await window.showOpenFilePicker({
          multiple: false,
          types: [
            {
              description: 'Excel workbook',
              accept: {
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
              },
            },
          ],
        })
        const file = await handle.getFile()
        applyBrowserFile(file)
        return
      } catch (error) {
        if (error?.name === 'AbortError') {
          return
        }
      }
    }

    fileInputRef.current?.click()
  }

  const browseFolder = async () => {
    if (typeof window.showDirectoryPicker === 'function') {
      try {
        const dir = await window.showDirectoryPicker()
        setDraft(dir.name)
        setNote(
          `Folder selected: ${dir.name}. Enter the full folder path if needed, then append your workbook file name.`,
        )
        return
      } catch (error) {
        if (error?.name === 'AbortError') {
          return
        }
      }
    }

    folderInputRef.current?.click()
  }

  return (
    <div className="modal-backdrop" role="presentation" onClick={onClose}>
      <div
        className="modal-card"
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        onClick={(event) => event.stopPropagation()}
      >
        <div className="modal-header">
          <h3 id={titleId}>{title}</h3>
          <button type="button" className="secondary-inline" onClick={onClose}>
            Close
          </button>
        </div>

        <p className="modal-help">
          Choose a {mode === 'folder' ? 'folder' : 'workbook file'} with the system picker, or type
          a full path for script execution.
        </p>

        <label>
          Path
          <input
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            placeholder={
              mode === 'folder'
                ? 'C:\\dev\\D365Patterns-MS\\templates\\Azure-DevOps-templates'
                : 'C:\\dev\\...\\ADO template guideline (Preview).xlsx'
            }
            autoFocus
          />
        </label>

        {note ? <p className="modal-note">{note}</p> : null}

        <div className="modal-actions">
          <button type="button" onClick={browseFile}>
            Browse file…
          </button>
          <button type="button" className="secondary-inline" onClick={browseFolder}>
            Browse folder…
          </button>
          <button
            type="button"
            className="run-button"
            onClick={() => onConfirm(draft.trim())}
            disabled={!draft.trim()}
          >
            Use path
          </button>
        </div>

        <input
          ref={fileInputRef}
          type="file"
          accept={accept}
          hidden
          onChange={(event) => applyBrowserFile(event.target.files?.[0])}
        />
        <input
          ref={folderInputRef}
          type="file"
          {...{ webkitdirectory: '' }}
          hidden
          onChange={(event) => {
            const first = event.target.files?.[0]
            if (!first) {
              return
            }
            const relative = first.webkitRelativePath || first.name
            const folder = relative.includes('/')
              ? relative.split('/').slice(0, -1).join('\\')
              : relative
            setDraft(folder)
            setNote(
              'Folder chosen from browser picker. Edit to a full absolute path if required by the runner.',
            )
          }}
        />
      </div>
    </div>
  )
}
