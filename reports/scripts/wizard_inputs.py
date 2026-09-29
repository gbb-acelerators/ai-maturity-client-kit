"""Read implementation-guide-inputs.json (the Part 4 wizard output).

Each wizard field is free text or Markdown. ``wizard_value`` turns it
into the structure the report templates render: lists of table rows,
list items, or plain text. Placeholder text such as "(fill in ...)"
and empty fields become ``None`` so templates show a "to fill"
marker instead of invented content.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_ITEM_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+(.+?)\s*$")
_SEP_RE = re.compile(r"^:?-{2,}:?$")
_DIM_RE = re.compile(r"\bD([1-9])\b", re.IGNORECASE)
_PLACEHOLDER_MARKERS = ("preencher", "fill in", "completar", "rellenar")

TABLE_KEYS = {
    "raci_matrix": ("activity", "r", "a", "c", "i"),
    "communication_plan": ("audience", "channel", "frequency", "owner"),
    "training_plan": ("audience", "format", "cadence"),
    "dimension_owners": ("dimension", "owner"),
    "risk_register": ("risk", "impact", "mitigation", "owner"),
}


def is_placeholder(text: str) -> bool:
    text = text.strip().lower()
    return text.startswith("(") and any(
        m in text for m in _PLACEHOLDER_MARKERS)


def md_items(text: str) -> list[str]:
    return [m.group(1) for line in text.splitlines()
            if (m := _ITEM_RE.match(line)) and not line.lstrip()
            .startswith("|")]


def md_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(_SEP_RE.match(c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:]  # first row is the header


def split_pair(text: str) -> tuple[str, str]:
    for sep in (" — ", " – ", ": ", " - "):
        if sep in text:
            left, right = text.split(sep, 1)
            return left.strip(" *"), right.strip()
    return text.strip(" *"), ""


def cells(row: list[str], keys: tuple[str, ...]) -> dict:
    padded = row + [""] * (len(keys) - len(row))
    return dict(zip(keys, padded))


def _owners(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        match = _DIM_RE.search(row.get("dimension", ""))
        if match and row.get("owner"):
            out.append({"dimension": f"D{match.group(1)}",
                        "owner": row["owner"]})
    return out


def wizard_value(key: str, value):
    """Convert wizard Markdown into the structures the templates render."""
    if not isinstance(value, str):
        return value or None
    text = value.strip()
    if not text or is_placeholder(text):
        return None
    rows = md_rows(text)
    items = [i for i in md_items(text) if not is_placeholder(i)]
    if not rows and not items and key in ("executive_steering_committee",
                                          "tpo"):
        items = [ln.strip() for ln in text.splitlines()
                 if ln.strip() and not is_placeholder(ln)]
    if key == "executive_steering_committee":
        if rows:
            return [cells(r, ("name", "role")) for r in rows]
        members = [dict(zip(("name", "role"), split_pair(i)))
                   for i in items]
        return members or None
    if key == "tpo":
        if items:
            return {"program_manager": split_pair(items[0])[0],
                    "members": items[1:]}
        return {"program_manager": text.splitlines()[0], "members": []}
    if key in TABLE_KEYS:
        keys = TABLE_KEYS[key]
        if rows:
            parsed = [cells(r, keys) for r in rows]
        elif key == "dimension_owners":
            lines = items or [ln for ln in text.splitlines() if ln.strip()]
            parsed = [dict(zip(keys, split_pair(ln))) for ln in lines]
        else:
            parsed = [cells([i], keys) for i in items]
        if key == "dimension_owners":
            parsed = _owners(parsed)
        return parsed or None
    if key.startswith("quick_wins"):
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        return items or [ln for ln in lines if not is_placeholder(ln)]
    return text


def load_wizard(path: Path) -> dict:
    """Converted wizard fields plus metadata; empty when absent."""
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    raw = data.get("implementation_guide_inputs") or {}
    out = {"_metadata": data.get("metadata") or {}}
    for key, value in raw.items():
        converted = wizard_value(key, value)
        if converted:
            out[key] = converted
    return out
