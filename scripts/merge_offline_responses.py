#!/usr/bin/env python3
"""Merge offline-form exports into one v2 responses.json.

forms/assessment-v2.html exports one respondent per file. This
script combines those files (and any other v2 responses.json) into the
kit's responses.json, giving each respondent a unique ID. The engine then
scores all respondents together, with personas and flags.

- Accepts files or folders (every *.json inside a folder).
- Keeps the profile (R-Q#) and the answers; drops answers for unknown
  question IDs and reports them.
- Refuses v1 files and files from another organization unless
  --allow-mixed-org is given.
- Backs up an existing output file before writing it.

Usage:
    python3 scripts/merge_offline_responses.py exports/ [more.json]
        [--out responses.json] [--org NAME] [--lang pt-BR|en|es]
"""
from __future__ import annotations

import argparse
import datetime
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def framework_major(data: dict) -> int:
    raw = str((data.get("metadata") or {}).get("framework_version") or "1")
    try:
        return int(raw.split(".")[0])
    except ValueError:
        return 1


def input_files(items: list[str]) -> list[Path]:
    files: list[Path] = []
    for item in items:
        path = Path(item).expanduser()
        if path.is_dir():
            files += sorted(path.glob("*.json"))
        elif path.exists():
            files.append(path)
        else:
            raise FileNotFoundError(item)
    return files


def respondents_of(data: dict) -> list[dict]:
    people = data.get("respondents")
    if isinstance(people, list):
        return people
    if isinstance(data.get("responses"), dict):
        return [{"profile": {}, "answers": data["responses"]}]
    return []


def merge(files: list[Path], org: str | None, lang: str | None,
          allow_mixed_org: bool) -> tuple[dict, list[str]]:
    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    known = {q["id"] for d in fw["dimensions"] for q in d["questions"]}
    profile_ids = {p["id"] for p in fw["profile_questions"]}
    notes: list[str] = []
    people: list[dict] = []
    orgs: set[str] = set()
    langs: list[str] = []
    dates: list[str] = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        if framework_major(data) < 2:
            raise ValueError(f"{path.name} is not a v2 file "
                             f"(metadata.framework_version)")
        meta = data.get("metadata") or {}
        if meta.get("organization"):
            orgs.add(str(meta["organization"]).strip())
        if meta.get("language"):
            langs.append(meta["language"])
        if meta.get("assessment_date"):
            dates.append(str(meta["assessment_date"]))
        for person in respondents_of(data):
            answers = {}
            for qid, entry in (person.get("answers") or {}).items():
                if qid in known and isinstance(entry, dict):
                    answers[qid] = {"level": entry.get("level"),
                                    "evidence": entry.get("evidence")
                                    or ""}
                elif qid not in known:
                    notes.append(f"{path.name}: unknown question {qid} "
                                 f"dropped")
            profile = {k: v for k, v in (person.get("profile") or {})
                       .items() if k in profile_ids}
            people.append({"name": person.get("name") or "",
                           "email": person.get("email") or "",
                           "profile": profile, "answers": answers,
                           "_file": path.name})
    if len(orgs) > 1 and not allow_mixed_org and not org:
        raise ValueError("files come from different organizations: "
                         + ", ".join(sorted(orgs)) + " (use --org or "
                         "--allow-mixed-org)")
    for idx, person in enumerate(people, start=1):
        person["id"] = f"R{idx:02d}"
        if not person["name"] or person["name"].startswith("Respondent "):
            person["name"] = f"Respondent {idx:02d}"
        notes.append(f"{person['id']} ← {person.pop('_file')} "
                     f"({len(person['answers'])} answers)")
    today = datetime.date.today().isoformat()
    merged = {
        "metadata": {
            "framework_version": fw["version"],
            "organization": org or (sorted(orgs)[0] if orgs else None),
            "language": lang or (langs[0] if langs else "en"),
            "assessment_date": max(dates) if dates else today,
            "source": f"offline-html merge ({len(files)} files)",
        },
        "target_overrides": {},
        "dimension_weights": {},
        "respondents": [{k: p[k] for k in ("id", "name", "email",
                                           "profile", "answers")}
                        for p in people],
    }
    return merged, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("inputs", nargs="+", help="files or folders")
    ap.add_argument("--out", default=str(ROOT / "responses.json"))
    ap.add_argument("--org", help="organization name for the result")
    ap.add_argument("--lang", choices=("pt-BR", "en", "es"))
    ap.add_argument("--allow-mixed-org", action="store_true")
    args = ap.parse_args()
    out = Path(args.out)
    try:
        files = [f for f in input_files(args.inputs)
                 if f.resolve() != out.resolve()]
        if not files:
            raise ValueError("no input files")
        merged, notes = merge(files, args.org, args.lang,
                              args.allow_mixed_org)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"✗ {exc}", file=sys.stderr)
        return 1
    if out.exists():
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = out.with_name(f"{out.name}.backup-{stamp}")
        shutil.copy(out, backup)
        print(f"  backup: {backup.name}")
    out.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    for note in notes:
        print(f"  {note}")
    print(f"✓ {out}: {len(merged['respondents'])} respondent(s) from "
          f"{len(files)} file(s). Next: make pipeline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
