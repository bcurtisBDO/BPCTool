"""Apply process shell, work item types, picklists, and custom fields."""

from __future__ import annotations

from typing import Any, Callable
from urllib.parse import quote

from ..ado_client import AdoClient, AdoError

Emit = Callable[[str, str], None]


def apply_process(
    client: AdoClient,
    ir: dict[str, Any],
    *,
    dry_run: bool,
    emit: Emit,
) -> dict[str, Any]:
    process_name = ir["targets"]["process_name"]
    stats = {
        "process_id": None,
        "wits_created": 0,
        "wits_updated": 0,
        "wits_skipped": 0,
        "picklists": 0,
        "fields_created": 0,
        "fields_updated": 0,
        "fields_skipped": 0,
    }

    if dry_run:
        emit(
            "process",
            f"[dry-run] Would ensure process '{process_name}' with "
            f"{ir['counts']['work_item_types']} WITs / {ir['counts']['fields']} fields / "
            f"{ir['counts']['html_fields']} HTML fields",
        )
        return stats

    process_id = client.create_process(process_name)
    stats["process_id"] = process_id
    emit("process", f"Process ready: {process_name} ({process_id})")

    existing = {}
    for wit in client.list_process_wits(process_id):
        name = str(wit.get("name") or "").strip().lower()
        ref = str(wit.get("referenceName") or "").strip().lower()
        if name:
            existing[name] = wit
        if ref:
            existing[ref] = wit

    for wit in ir["process"]["work_item_types"]:
        name = wit["name"]
        custom = wit.get("custom")
        inherit_from = wit.get("inherit_from") or ""
        ref_name = wit.get("reference_name") or _build_ref(process_name, name)
        color = wit.get("color") or "0078D4"
        icon = wit.get("icon") or "icon_gear"
        description = wit.get("help_text") or ""

        existing_wit = existing.get(name.lower()) or existing.get(ref_name.lower())
        if not custom and not inherit_from:
            stats["wits_skipped"] += 1
            continue

        payload = {
            "name": name,
            "description": description,
            "color": color.lstrip("#"),
            "icon": icon,
            "inheritsFrom": inherit_from or None,
            "referenceName": ref_name.split(".")[-1] if not custom else ref_name.split(".")[-1],
        }
        # Drop None inheritsFrom for custom types without parent
        if not payload["inheritsFrom"]:
            payload.pop("inheritsFrom", None)

        try:
            if existing_wit:
                full_ref = existing_wit.get("referenceName") or ref_name
                client.patch(
                    f"/_apis/work/processes/{process_id}/workitemtypes/{quote(full_ref, safe='')}",
                    json_body={
                        "description": description,
                        "color": color.lstrip("#"),
                        "icon": icon,
                    },
                    api_version="7.1-preview.2",
                )
                stats["wits_updated"] += 1
            else:
                created = client.post(
                    f"/_apis/work/processes/{process_id}/workitemtypes",
                    json_body=payload,
                    api_version="7.1-preview.2",
                )
                if created:
                    existing[name.lower()] = created
                    ref = str(created.get("referenceName") or "").lower()
                    if ref:
                        existing[ref] = created
                stats["wits_created"] += 1
        except AdoError as exc:
            emit("process", f"WIT '{name}' warning: {exc}")

    # Picklists
    lists_data = client.get("/_apis/work/processes/lists", api_version="7.1") or {}
    existing_lists = {item.get("name"): item for item in lists_data.get("value") or []}
    for label, values in ir["process"]["picklists"].items():
        payload = {
            "name": label,
            "type": "String",
            "items": values,
            "isSuggested": False,
        }
        try:
            if label in existing_lists:
                picklist_id = existing_lists[label]["id"]
                client.put(
                    f"/_apis/work/processes/lists/{picklist_id}",
                    json_body=payload,
                    api_version="7.1",
                )
            else:
                client.post("/_apis/work/processes/lists", json_body=payload, api_version="7.1")
            stats["picklists"] += 1
        except AdoError as exc:
            emit("process", f"Picklist '{label}' warning: {exc}")

    # Refresh picklist ids for field create
    lists_data = client.get("/_apis/work/processes/lists", api_version="7.1") or {}
    picklist_ids = {item.get("name"): item.get("id") for item in lists_data.get("value") or []}

    fields_data = client.get("/_apis/wit/fields", api_version="7.1") or {}
    existing_fields = {
        str(item.get("referenceName") or "").lower(): item for item in fields_data.get("value") or []
    }

    for field in ir["process"]["fields"]:
        if not field.get("custom_field"):
            stats["fields_skipped"] += 1
            continue
        reference = field.get("reference_name")
        if not reference:
            continue
        field_type = field.get("field_type") or "String"
        label = field.get("label") or field.get("field_name")
        name = field.get("field_name") or label
        description = field.get("description") or ""

        if field_type in {"PicklistString", "PicklistInteger"}:
            picklist_id = picklist_ids.get(label)
            if not picklist_id:
                emit("process", f"Skipping field '{label}' — missing picklist")
                stats["fields_skipped"] += 1
                continue
            payload = {
                "name": name,
                "referenceName": reference,
                "type": "String",
                "isPicklist": True,
                "isPicklistSuggested": bool(field.get("multi_select")),
                "picklistId": picklist_id,
                "description": description,
            }
        else:
            payload = {
                "name": name,
                "type": field_type,
                "referenceName": reference,
                "description": description,
            }

        try:
            if reference.lower() in existing_fields:
                client.patch(
                    f"/_apis/wit/fields/{quote(reference, safe='')}",
                    json_body=payload,
                    api_version="7.1",
                )
                stats["fields_updated"] += 1
            else:
                client.post("/_apis/wit/fields", json_body=payload, api_version="7.1")
                stats["fields_created"] += 1
        except AdoError as exc:
            emit("process", f"Field '{reference}' warning: {exc}")

    emit(
        "process",
        "Process apply finished: "
        f"WITs +{stats['wits_created']}/~{stats['wits_updated']}, "
        f"fields +{stats['fields_created']}/~{stats['fields_updated']}, "
        f"HTML fields in template: {ir['counts'].get('html_fields', 0)}",
    )
    return stats


def _build_ref(process_name: str, wit_name: str) -> str:
    safe_process = process_name.replace(" ", "")
    safe_name = wit_name.replace(" ", "").replace("-", "").replace("_", "")
    return f"{safe_process}.{safe_name}"
