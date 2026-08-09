"""Prevalidate catalog drafts against template picklists / known hard-fail values."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .catalog_import import WorkItemDraft
from .mapping import TemplateMapping, normalize
from .richtext import normalize_field_value

# Test Case (and inherited TCM types) do not use Agile "New".
_TEST_CASE_INVALID_STATES = frozenset({"new"})
_INVALID_AREA_MARKERS = frozenset({"not found", "n/a", "na", "none", "#n/a"})


def _is_required(value: Any) -> bool:
    return str(value or "").strip().lower() in {"yes", "true", "1", "x"}


def _template_default(fd) -> Any | None:
    """Return a usable Fields-sheet default, or None when absent / placeholder."""
    raw = fd.default_value
    if raw is None:
        return None
    text = str(raw).strip()
    if not text or text.lower() == "none":
        return None
    return normalize_field_value(text, fd.field_type or "")


@dataclass
class PrevalidateIssue:
    key: str
    work_item_type: str
    field: str
    value: str
    kind: str
    action: str  # report | sanitize | normalize | default
    detail: str = ""


@dataclass
class PrevalidateResult:
    issues: list[PrevalidateIssue] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)
    multi_select_normalized: int = 0
    fields_stripped: int = 0
    defaults_applied: int = 0

    def bump(self, kind: str, n: int = 1) -> None:
        self.counts[kind] = self.counts.get(kind, 0) + n


def split_multi_select(value: str) -> list[str]:
    """Split semicolon-separated multi-select storage (July / DevLabs style)."""
    return [part.strip() for part in str(value).split(";") if part.strip()]


def join_multi_select(parts: list[str]) -> str:
    return "; ".join(parts)


def prevalidate_catalog_drafts(
    drafts: list[WorkItemDraft],
    ir: dict[str, Any],
    mapping: TemplateMapping,
    *,
    sanitize: bool = True,
) -> PrevalidateResult:
    """Validate drafts; optionally strip/normalize values that hard-fail create.

    Multi-select fields (Application family, Products, Industries, …) are checked
    token-by-token against the template Picklists sheet. With process
    ``isSuggested``/``isPicklistSuggested``, semicolon composites can be stored;
    prevalidate still flags unknown tokens for data quality.
    """
    result = PrevalidateResult()
    picklists = ir.get("process", {}).get("picklists") or {}
    allowed_by_label = {
        normalize(name): {str(v).strip() for v in values if str(v).strip()}
        for name, values in picklists.items()
    }
    # Map field ref → (label key, multi_select, required, is_picklist)
    field_meta: dict[str, dict[str, Any]] = {}
    for fd in mapping.fields_by_ref.values():
        ref = fd.reference_name
        if not ref:
            continue
        label_key = normalize(fd.label)
        field_meta[ref.lower()] = {
            "label_key": label_key,
            "label": fd.label,
            "multi_select": bool(fd.multi_select),
            "required": (fd.required or "").strip().lower() in {"yes", "true", "1", "x"},
            "is_picklist": "picklist" in (fd.field_type or "").lower()
            or label_key in allowed_by_label,
        }

    for draft in drafts:
        wit_norm = normalize(draft.work_item_type)
        # Area path
        area = draft.fields.get("System.AreaPath")
        if area is not None and str(area).strip():
            area_text = str(area).strip()
            if area_text.lower() in _INVALID_AREA_MARKERS:
                result.issues.append(
                    PrevalidateIssue(
                        key=draft.key,
                        work_item_type=draft.work_item_type,
                        field="System.AreaPath",
                        value=area_text,
                        kind="invalid_area_path",
                        action="sanitize" if sanitize else "report",
                        detail="Placeholder area path would fail TF401347",
                    )
                )
                result.bump("invalid_area_path")
                if sanitize:
                    del draft.fields["System.AreaPath"]
                    result.fields_stripped += 1

        # State
        state = draft.fields.get("System.State")
        if state is not None and str(state).strip():
            state_text = str(state).strip()
            if wit_norm == "test case" and state_text.lower() in _TEST_CASE_INVALID_STATES:
                result.issues.append(
                    PrevalidateIssue(
                        key=draft.key,
                        work_item_type=draft.work_item_type,
                        field="System.State",
                        value=state_text,
                        kind="invalid_state",
                        action="sanitize" if sanitize else "report",
                        detail="Test Case does not allow State 'New'",
                    )
                )
                result.bump("invalid_state")
                if sanitize:
                    del draft.fields["System.State"]
                    result.fields_stripped += 1

        for ref, value in list(draft.fields.items()):
            if value in (None, ""):
                continue
            meta = field_meta.get(ref.lower())
            if not meta or not meta["is_picklist"]:
                continue
            label_key = meta["label_key"]
            allowed = allowed_by_label.get(label_key)
            if not allowed:
                continue
            text = str(value).strip()
            if meta["multi_select"]:
                parts = split_multi_select(text)
                normalized = join_multi_select(parts)
                if sanitize and normalized != text:
                    draft.fields[ref] = normalized
                    result.multi_select_normalized += 1
                unknown = [p for p in parts if p not in allowed]
                if unknown:
                    result.issues.append(
                        PrevalidateIssue(
                            key=draft.key,
                            work_item_type=draft.work_item_type,
                            field=ref,
                            value=text,
                            kind="invalid_multi_select_token",
                            action="report",
                            detail=f"Unknown token(s): {', '.join(unknown[:5])}",
                        )
                    )
                    result.bump("invalid_multi_select_token")
            else:
                if text not in allowed:
                    result.issues.append(
                        PrevalidateIssue(
                            key=draft.key,
                            work_item_type=draft.work_item_type,
                            field=ref,
                            value=text,
                            kind="invalid_picklist_value",
                            action="sanitize" if sanitize else "report",
                            detail=f"Not in picklist '{meta['label']}'",
                        )
                    )
                    result.bump("invalid_picklist_value")
                    if sanitize:
                        del draft.fields[ref]
                        result.fields_stripped += 1

        # Required MSBPC fields empty — fill template Default value when present;
        # only when WIT matrix marks the field applicable.
        applicable = mapping.applicable_fields_by_wit.get(wit_norm)
        if applicable:
            for fd in mapping.fields_by_ref.values():
                if not _is_required(fd.required):
                    continue
                if normalize(fd.label) not in applicable:
                    continue
                ref = fd.reference_name
                if not ref or not ref.lower().startswith("msbpc."):
                    continue
                if draft.fields.get(ref) not in (None, ""):
                    continue
                default = _template_default(fd) if sanitize else None
                if default is not None:
                    draft.fields[ref] = default
                    result.defaults_applied += 1
                    result.bump("defaults_applied")
                    result.issues.append(
                        PrevalidateIssue(
                            key=draft.key,
                            work_item_type=draft.work_item_type,
                            field=ref,
                            value=str(default),
                            kind="defaults_applied",
                            action="default",
                            detail=(
                                f"Required field '{fd.label}' empty in spreadsheet; "
                                f"applied template default"
                            ),
                        )
                    )
                    continue
                result.issues.append(
                    PrevalidateIssue(
                        key=draft.key,
                        work_item_type=draft.work_item_type,
                        field=ref,
                        value="",
                        kind="required_empty",
                        action="report",
                        detail=f"Required field '{fd.label}' is empty (no template default)",
                    )
                )
                result.bump("required_empty")

    return result


def prevalidate_summary(result: PrevalidateResult) -> dict[str, Any]:
    samples: dict[str, list[dict[str, Any]]] = {}
    for issue in result.issues:
        bucket = samples.setdefault(issue.kind, [])
        if len(bucket) >= 15:
            continue
        bucket.append(
            {
                "key": issue.key,
                "workItemType": issue.work_item_type,
                "field": issue.field,
                "value": issue.value,
                "action": issue.action,
                "detail": issue.detail,
            }
        )
    return {
        "counts": dict(sorted(result.counts.items())),
        "multiSelectNormalized": result.multi_select_normalized,
        "fieldsStripped": result.fields_stripped,
        "defaultsApplied": result.defaults_applied,
        "issueTotal": len(result.issues),
        "samples": samples,
    }
