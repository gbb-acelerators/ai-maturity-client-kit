#!/usr/bin/env python3
"""Build framework.v2.json from the v2 question bank (single source).

The English text comes from coleta/AI-Maturity-Form-Questions_v2.md.
PT-BR and ES text comes from framework/v2/i18n.<lang>.json. Kit design
choices (units, audiences, strategies, report groups, level names) are
in framework/v2/config.json.

Usage:
    python3 scripts/spec_to_framework_v2.py          # write the file
    python3 scripts/spec_to_framework_v2.py --check  # fail if stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "coleta" / "AI-Maturity-Form-Questions_v2.md"
CONF_DIR = ROOT / "framework" / "v2"
OUT = ROOT / "framework.v2.json"
LANGS = ("pt-br", "es")

DIM_RE = re.compile(r"^### (D\d): (.+)$", re.M)
Q_RE = re.compile(r"^#### `((?:D\d|R)-Q\d+)`: (.+)$", re.M)
FIELD_RE = re.compile(r"^- \*\*(.+?):\*\* (.*)$", re.M)
REF_RE = re.compile(r"^(\d+)\. (.+)$", re.M)
URL_RE = re.compile(r"<(https?://[^>]+)>")
PROFILE_RE = re.compile(r"^### Question `(R-Q\d+)`: (.+)$", re.M)
V1_RE = re.compile(r"P\d-C\d+-Q\d+")


def section(text: str, start: str, end: str | None) -> str:
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


def blocks(text: str, regex: re.Pattern) -> list[tuple]:
    found = list(regex.finditer(text))
    out = []
    for k, m in enumerate(found):
        stop = found[k + 1].start() if k + 1 < len(found) else len(text)
        out.append((m, text[m.end():stop]))
    return out


def quote(body: str) -> str:
    m = re.search(r"^> \*\*(.+?)\*\*\s*$", body, re.M)
    if not m:
        raise ValueError("question text not found")
    return m.group(1).strip()


def basis_numbers(raw: str) -> list[int]:
    return sorted({int(n) for n in re.findall(r"\[(\d+)\]", raw)})


def parse_question(qid: str, title: str, body: str) -> dict:
    fields = {m.group(1): m.group(2).strip()
              for m in FIELD_RE.finditer(body)}
    anchors = {"l3": fields["L3 looks like"],
               "l4": fields["L4 looks like"]}
    if "L1 to L2 look like" in fields:
        anchors["l1_l2"] = fields["L1 to L2 look like"]
    lineage_raw = fields["v1 lineage"]
    lineage = [] if lineage_raw == "New" else [
        {"id": m.group(0),
         "partial": "(partial)" in lineage_raw[m.end():m.end() + 11]}
        for m in V1_RE.finditer(lineage_raw)
    ]
    out = {
        "id": qid,
        "title": {"en": title.strip()},
        "text": {"en": quote(body)},
        "anchors": {k: {"en": v} for k, v in anchors.items()},
        "evidence_examples": {"en": fields["Evidence examples"]},
        "basis": basis_numbers(fields["Basis"]),
        "basis_text": fields["Basis"],
        "v1_lineage": lineage,
    }
    if "Scope note" in fields:
        out["scope_note"] = {"en": fields["Scope note"]}
    return out


def parse_profile(qid: str, title: str, body: str) -> dict:
    options = [ln[2:].strip() for ln in body.splitlines()
               if ln.startswith("- ")]
    return {
        "id": qid,
        "title": {"en": title.strip()},
        "text": {"en": quote(body)},
        "multi": "multiple answers" in body,
        "options": {"en": options},
    }


def parse_retired(spec: str) -> dict[str, str]:
    table = section(spec, "## 9. Traceability", "## 10.")
    retired: dict[str, str] = {}
    for line in table.splitlines():
        m = re.match(r"^\| (P\d-C\d+) ([^|]+)\|[^|]*\| (.+) \|$", line)
        if not m or m.group(3).strip() == "None":
            continue
        cap, cell = m.group(1), m.group(3).strip()
        nums: list[int] = []
        for a, b in re.findall(r"Q(\d+) to Q(\d+)", cell):
            nums.extend(range(int(a), int(b) + 1))
        cleaned = re.sub(r"Q\d+ to Q\d+", "", cell)
        nums.extend(int(n) for n in re.findall(r"Q(\d+)", cleaned))
        for n in nums:
            retired[f"{cap}-Q{n}"] = cell
    return retired


def parse_references(spec: str) -> list[dict]:
    refs = section(spec, "## References", None)
    out = []
    for m in REF_RE.finditer(refs):
        url = URL_RE.search(m.group(2))
        out.append({"n": int(m.group(1)), "text": m.group(2).strip(),
                    "url": url.group(1) if url else None})
    return out


def parse_spec(spec: str) -> dict:
    bank = section(spec, "## 7. Scored question bank", "## 8.")
    dims = []
    for dm, dbody in blocks(bank, DIM_RE):
        why = re.search(r"Why it matters: (.+?)_\s*$", dbody, re.M)
        qs = [parse_question(qm.group(1), qm.group(2), qbody)
              for qm, qbody in blocks(dbody, Q_RE)]
        dims.append({"id": dm.group(1), "name": {"en": dm.group(2)},
                     "why_it_matters": {"en": why.group(1).strip()},
                     "questions": qs})
    prof = section(spec, "## 6. Section 0", "## 7.")
    profile = [parse_profile(m.group(1), m.group(2), b)
               for m, b in blocks(prof, PROFILE_RE)]
    scale = section(spec, "## 4. Answer scale", "How to read the scale")
    options = re.findall(r"^- \*\*((?:L[0-4]|NA) - .+?)\*\*$", scale, re.M)
    version = re.search(r"\| Version \| ([\d.]+) \|", spec).group(1)
    return {"version": version, "dimensions": dims, "profile": profile,
            "options": options, "retired": parse_retired(spec),
            "references": parse_references(spec)}


def merge_lang(fw: dict, lang: str, tr: dict) -> list[str]:
    """Copy translations into the framework; return missing keys."""
    missing: list[str] = []

    def put(target: dict, value, key: str) -> None:
        if value in (None, "", []):
            missing.append(key)
        else:
            target[lang] = value

    put(fw["options"], tr.get("options"), "options")
    for d in fw["dimensions"]:
        td = tr.get("dimensions", {}).get(d["id"], {})
        put(d["name"], td.get("name"), f"{d['id']}.name")
        put(d["why_it_matters"], td.get("why_it_matters"),
            f"{d['id']}.why_it_matters")
        for q in d["questions"]:
            tq = tr.get("questions", {}).get(q["id"], {})
            put(q["title"], tq.get("title"), f"{q['id']}.title")
            put(q["text"], tq.get("text"), f"{q['id']}.text")
            for k in q["anchors"]:
                put(q["anchors"][k], tq.get(k), f"{q['id']}.{k}")
            put(q["evidence_examples"], tq.get("evidence_examples"),
                f"{q['id']}.evidence_examples")
            if "scope_note" in q:
                put(q["scope_note"], tq.get("scope_note"),
                    f"{q['id']}.scope_note")
    for p in fw["profile_questions"]:
        tp = tr.get("profile", {}).get(p["id"], {})
        put(p["title"], tp.get("title"), f"{p['id']}.title")
        put(p["text"], tp.get("text"), f"{p['id']}.text")
        opts = tp.get("options")
        if opts and len(opts) != len(p["options"]["en"]):
            missing.append(f"{p['id']}.options (count)")
        else:
            put(p["options"], opts, f"{p['id']}.options")
    return missing


def build() -> tuple[dict, list[str]]:
    spec = parse_spec(SPEC.read_text(encoding="utf-8"))
    conf = json.loads((CONF_DIR / "config.json").read_text("utf-8"))
    dims = []
    for d in spec["dimensions"]:
        dc = conf["dimensions"][d["id"]]
        for q in d["questions"]:
            qc = conf["questions"].get(q["id"], {})
            unit = qc.get("unit", dc["default_unit"])
            q.update({
                "weight": 1.0,
                "unit": unit,
                "audience": qc.get("audience", dc["audience"]),
                "pe": q["id"] in conf["pe_questions"],
                "kpi": conf["kpi_by_unit"][unit],
            })
        dims.append({
            "id": d["id"],
            "name": d["name"],
            "why_it_matters": d["why_it_matters"],
            "weight": 1.0,
            "group": dc["group"],
            "strategies": dc["strategies"],
            "questions": d["questions"],
        })
    consolidated: dict[str, list[str]] = {}
    for d in dims:
        for q in d["questions"]:
            for item in q["v1_lineage"]:
                consolidated.setdefault(item["id"], []).append(q["id"])
    trace = {}
    for v1_id, into in consolidated.items():
        trace[v1_id] = {"status": "consolidated", "into": into}
    for v1_id, reason in spec["retired"].items():
        trace[v1_id] = trace.get(v1_id) or {
            "status": "retired", "reason": reason}
        if trace[v1_id]["status"] != "retired":
            trace[v1_id]["conflict"] = "also listed as retired"
    fw = {
        "$schema": "./framework.v2.schema.json",
        "version": spec["version"],
        "source": "coleta/AI-Maturity-Form-Questions_v2.md",
        "level_names": conf["level_names"],
        "level_bands": conf["level_bands"],
        "coverage_bands": conf["coverage_bands"],
        "scoring": conf["scoring"],
        "options": {"en": spec["options"]},
        "strategies": conf["strategies"],
        "technologies_per_strategy": conf["technologies_per_strategy"],
        "report_groups": conf["report_groups"],
        "personas": conf["personas"],
        "profile_questions": spec["profile"],
        "dimensions": dims,
        "references": spec["references"],
        "traceability": dict(sorted(trace.items(), key=_v1_key)),
    }
    missing = []
    for lang in LANGS:
        path = CONF_DIR / f"i18n.{lang}.json"
        tr = json.loads(path.read_text("utf-8")) if path.exists() else {}
        missing += [f"{lang}:{k}" for k in merge_lang(fw, lang, tr)]
    return fw, missing


def _v1_key(item: tuple) -> tuple:
    p, c, q = re.findall(r"\d+", item[0])
    return int(p), int(c), int(q)


def dump(fw: dict) -> str:
    return json.dumps(fw, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--allow-missing", action="store_true",
                    help="write even when translations are missing")
    args = ap.parse_args()
    fw, missing = build()
    if missing and not args.allow_missing:
        print(f"✗ {len(missing)} missing translations, first: "
              f"{missing[:5]}", file=sys.stderr)
        return 1
    text = dump(fw)
    if args.check:
        if not OUT.exists() or OUT.read_text("utf-8") != text:
            print("✗ framework.v2.json is stale; run "
                  "scripts/spec_to_framework_v2.py", file=sys.stderr)
            return 1
        print("✓ framework.v2.json is up to date")
        return 0
    OUT.write_text(text, encoding="utf-8")
    n = sum(len(d["questions"]) for d in fw["dimensions"])
    print(f"✓ framework.v2.json {fw['version']}: {len(fw['dimensions'])} "
          f"dimensions, {n} questions, {len(fw['references'])} refs"
          + (f", {len(missing)} missing translations" if missing else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
