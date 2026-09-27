#!/usr/bin/env python3
"""Validate framework.v2.json against its schema and the v2 rules.

Checks: JSON Schema (framework.v2.schema.json, when the optional
jsonschema package is installed), question counts per dimension,
unique IDs, that every basis number exists in the references, the
v1 -> v2 traceability partition (all 158 v1 IDs exactly once),
trilingual parity, and that framework.v2.json matches the spec.

Usage:
    python3 scripts/validate_framework_v2.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"D1": 7, "D2": 6, "D3": 6, "D4": 8, "D5": 7, "D6": 7,
            "D7": 6, "D8": 7, "D9": 7}
LANGS = ("en", "pt-br", "es")
PREFIXES = ("L0 - ", "L1 - ", "L2 - ", "L3 - ", "L4 - ", "NA - ")


def v1_ids() -> set[str]:
    v1 = json.loads((ROOT / "framework.json").read_text("utf-8"))
    return {q["id"] for p in v1["pillars"] for c in p["capabilities"]
            for q in c["questions"]}


def check(fw: dict) -> tuple[list[str], int, int]:
    errors: list[str] = []
    counts = {d["id"]: len(d["questions"]) for d in fw["dimensions"]}
    if counts != EXPECTED:
        errors.append(f"question counts {counts} != {EXPECTED}")
    ids = [q["id"] for d in fw["dimensions"] for q in d["questions"]]
    ids += [p["id"] for p in fw["profile_questions"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate question IDs")
    if len(fw["profile_questions"]) != 5:
        errors.append("expected 5 profile questions")
    multi = [p["id"] for p in fw["profile_questions"] if p["multi"]]
    if multi != ["R-Q3"]:
        errors.append(f"only R-Q3 may be multiple choice, got {multi}")
    refs = {r["n"] for r in fw["references"]}
    if refs != set(range(1, 59)):
        errors.append("references must be numbered 1 to 58")
    for d in fw["dimensions"]:
        for q in d["questions"]:
            missing = set(q["basis"]) - refs
            if missing:
                errors.append(f"{q['id']}: basis {sorted(missing)} "
                              f"not in references")
    trace = fw["traceability"]
    expected = v1_ids()
    if set(trace) != expected:
        errors.append(f"traceability covers {len(trace)} IDs; missing "
                      f"{sorted(expected - set(trace))[:5]}, extra "
                      f"{sorted(set(trace) - expected)[:5]}")
    cons = sum(v["status"] == "consolidated" for v in trace.values())
    ret = sum(v["status"] == "retired" for v in trace.values())
    if cons + ret != len(expected) or any("conflict" in v
                                          for v in trace.values()):
        errors.append("traceability is not a partition")
    for lang in LANGS:
        opts = fw["options"].get(lang) or []
        if len(opts) != 6 or any(not o.startswith(p)
                                 for o, p in zip(opts, PREFIXES)):
            errors.append(f"options[{lang}] must keep L0-L4/NA prefixes")
        for d in fw["dimensions"]:
            if not d["name"].get(lang):
                errors.append(f"{d['id']}.name missing {lang}")
            for q in d["questions"]:
                fields = [q["title"], q["text"], q["evidence_examples"],
                          *q["anchors"].values()]
                if "scope_note" in q:
                    fields.append(q["scope_note"])
                if any(not f.get(lang) for f in fields):
                    errors.append(f"{q['id']} missing {lang} text")
        for p in fw["profile_questions"]:
            if len(p["options"].get(lang) or []) != \
                    len(p["options"]["en"]):
                errors.append(f"{p['id']} options missing {lang}")
    text = json.dumps(fw, ensure_ascii=False)
    if "\u2014" in text or "\u2013" in text:
        errors.append("em dash or en dash found (kit writing rules)")
    return errors, cons, ret


def schema_check(fw: dict) -> str:
    try:
        import jsonschema
    except ImportError:
        return "skipped (jsonschema not installed)"
    schema = json.loads(
        (ROOT / "framework.v2.schema.json").read_text("utf-8"))
    jsonschema.validate(fw, schema)
    return "ok"


def main() -> int:
    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    errors, cons, ret = check(fw)
    try:
        schema = schema_check(fw)
    except Exception as exc:  # jsonschema.ValidationError
        errors.append(f"schema: {exc}".splitlines()[0])
        schema = "failed"
    stale = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "spec_to_framework_v2.py"),
         "--check"], capture_output=True, text=True)
    if stale.returncode:
        errors.append(stale.stderr.strip() or "framework.v2.json stale")
    if errors:
        print("✗ framework.v2.json:")
        for e in errors:
            print(f"  - {e}")
        return 1
    n = sum(EXPECTED.values())
    print(f"✓ framework.v2.json {fw['version']}: {n} questions, 5 "
          f"profile, 58 references, traceability {cons} consolidated + "
          f"{ret} retired = {cons + ret}, 3 languages, schema {schema}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
