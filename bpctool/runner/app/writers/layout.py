"""Apply page layouts, including HtmlFieldControl groups for HTML fields."""

from __future__ import annotations

from typing import Any, Callable
from urllib.parse import quote

from ..ado_client import AdoClient, AdoError

Emit = Callable[[str, str], None]


def apply_layout(
    client: AdoClient,
    ir: dict[str, Any],
    *,
    dry_run: bool,
    emit: Emit,
    process_id: str | None = None,
) -> dict[str, Any]:
    process_name = ir["targets"]["process_name"]
    stats = {
        "wits_processed": 0,
        "html_controls": 0,
        "controls": 0,
        "fields_added": 0,
        "warnings": 0,
    }

    html_count = ir["counts"].get("html_fields", 0)
    if dry_run:
        emit(
            "layout",
            f"[dry-run] Would apply layouts for {len(ir['process']['work_item_types'])} WITs "
            f"including {html_count} HtmlFieldControl placements",
        )
        return stats

    process_id = process_id or client.get_process_id(process_name)
    if not process_id:
        raise AdoError(f'Process "{process_name}" not found for layout apply.')

    fields_by_label = {
        (f.get("label") or f.get("field_name") or "").strip(): f for f in ir["process"]["fields"]
    }
    process_wits = {str(w.get("name") or "").strip().lower(): w for w in client.list_process_wits(process_id)}

    for wit in ir["process"]["work_item_types"]:
        labels = wit.get("applicable_field_labels") or []
        if not labels:
            continue
        wit_name = wit["name"]
        process_wit = process_wits.get(wit_name.lower())
        if not process_wit:
            emit("layout", f"Skipping layout for missing WIT '{wit_name}'")
            stats["warnings"] += 1
            continue

        wit_ref = str(process_wit.get("referenceName") or "")
        wit_api_id = wit_ref
        stats["wits_processed"] += 1

        for label in labels:
            field = fields_by_label.get(label)
            if not field:
                continue
            ref = field.get("reference_name")
            if not ref:
                continue
            field_type = (field.get("field_type") or "").strip()

            # Add field to WIT
            try:
                client.post(
                    f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/fields",
                    json_body={"referenceName": ref, "required": False, "visible": True},
                    api_version="7.1-preview.2",
                )
                stats["fields_added"] += 1
            except AdoError as exc:
                if exc.status not in {400, 409}:
                    emit("layout", f"Add field {ref} on {wit_name}: {exc}")
                    stats["warnings"] += 1

            page_name = field.get("page_name") or "Details"
            group_name = field.get("group_name") or label
            section_label = field.get("group_location") or "Section1"

            try:
                layout = client.get(
                    f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout",
                    api_version="7.1-preview.1",
                )
            except AdoError as exc:
                emit("layout", f"Layout locked/unavailable for {wit_name}: {exc}")
                stats["warnings"] += 1
                break

            page = _find_page(layout, page_name)
            page_id = page.get("id") if page else None
            if not page_id:
                try:
                    created = client.post(
                        f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout/pages",
                        json_body={"label": page_name, "order": 1, "overridden": False},
                        api_version="7.1-preview.1",
                    )
                    page_id = created.get("id") if created else None
                except AdoError as exc:
                    emit("layout", f"Could not create page '{page_name}' on {wit_name}: {exc}")
                    stats["warnings"] += 1
                    continue
            if not page_id:
                continue

            layout = client.get(
                f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout",
                api_version="7.1-preview.1",
            )
            section_id = _section_id(layout, page_id, section_label)
            if not section_id:
                emit("layout", f"No section '{section_label}' on {wit_name}/{page_name}")
                stats["warnings"] += 1
                continue

            if field.get("is_html") or field_type.lower() == "html":
                ok = _add_html_control(
                    client,
                    process_id,
                    wit_api_id,
                    page_id,
                    section_id,
                    ref,
                    label,
                    group_name,
                )
                if ok:
                    stats["html_controls"] += 1
                else:
                    stats["warnings"] += 1
                continue

            group_id = _ensure_group(client, process_id, wit_api_id, page_id, section_id, layout, group_name)
            if not group_id:
                stats["warnings"] += 1
                continue
            control_type = "HtmlFieldControl" if field_type.lower() == "html" else "FieldControl"
            try:
                client.post(
                    f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout/pages/"
                    f"{page_id}/sections/{section_id}/groups/{group_id}/controls",
                    json_body={
                        "id": ref,
                        "label": label,
                        "controlType": control_type,
                        "visible": True,
                        "order": int(field.get("field_sequence") or 1) if str(field.get("field_sequence") or "").isdigit() else 1,
                    },
                    api_version="7.1-preview.1",
                )
                stats["controls"] += 1
            except AdoError as exc:
                if exc.status not in {400, 409}:
                    emit("layout", f"Control {ref}: {exc}")
                    stats["warnings"] += 1

    emit(
        "layout",
        f"Layout apply finished: {stats['wits_processed']} WITs, "
        f"{stats['html_controls']} HTML controls, {stats['controls']} other controls",
    )
    return stats


def _find_page(layout: dict[str, Any] | None, label: str) -> dict[str, Any] | None:
    if not layout:
        return None
    target = label.strip().lower()
    for page in layout.get("pages") or []:
        if str(page.get("label") or "").strip().lower() == target:
            return page
    return None


def _section_id(layout: dict[str, Any] | None, page_id: str, section_label: str) -> str | None:
    page = None
    for candidate in (layout or {}).get("pages") or []:
        if candidate.get("id") == page_id:
            page = candidate
            break
    if not page:
        return None
    sections = page.get("sections") or []
    if not sections:
        return None
    target = section_label.strip().lower()
    for section in sections:
        if str(section.get("id") or "").lower() == target or str(section.get("label") or "").lower() == target:
            return section.get("id")
    # Section1 / Section2 style ids
    for section in sections:
        sid = str(section.get("id") or "")
        if sid.lower() == target.replace(" ", ""):
            return sid
    return sections[0].get("id")


def _ensure_group(
    client: AdoClient,
    process_id: str,
    wit_api_id: str,
    page_id: str,
    section_id: str,
    layout: dict[str, Any] | None,
    group_label: str,
) -> str | None:
    for page in (layout or {}).get("pages") or []:
        if page.get("id") != page_id:
            continue
        for section in page.get("sections") or []:
            for group in section.get("groups") or []:
                if str(group.get("label") or "").strip().lower() == group_label.strip().lower():
                    return group.get("id")
    try:
        created = client.post(
            f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout/pages/"
            f"{page_id}/sections/{section_id}/groups",
            json_body={"label": group_label, "order": 1, "visible": True, "controls": []},
            api_version="7.1-preview.1",
        )
        return created.get("id") if created else None
    except AdoError:
        return None


def _add_html_control(
    client: AdoClient,
    process_id: str,
    wit_api_id: str,
    page_id: str,
    section_id: str,
    ref: str,
    label: str,
    group_name: str,
) -> bool:
    """HTML controls must live in their own group (July layout behavior)."""
    try:
        group = client.post(
            f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout/pages/"
            f"{page_id}/sections/{section_id}/groups",
            json_body={"label": group_name or label, "order": 1, "visible": True, "controls": []},
            api_version="7.1-preview.1",
        )
        group_id = group.get("id") if group else None
        if not group_id:
            return False
        client.post(
            f"/_apis/work/processes/{process_id}/workitemtypes/{quote(wit_api_id, safe='')}/layout/pages/"
            f"{page_id}/sections/{section_id}/groups/{group_id}/controls",
            json_body={
                "id": ref,
                "label": label,
                "controlType": "HtmlFieldControl",
                "visible": True,
                "height": 250,
            },
            api_version="7.1-preview.1",
        )
        return True
    except AdoError as exc:
        if exc.status in {400, 409}:
            return True
        return False
