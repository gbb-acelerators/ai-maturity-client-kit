#!/usr/bin/env python3
"""Generate the illustrative v2 mock (multi-persona) used for tests.

Writes responses.v2.json.example and a Microsoft Forms shaped export
(collection/v2-mock-forms-export.xlsx) with the same answers, so the
importer, engine and reports can be tested end to end. Every value is
synthetic and labelled as illustrative; it describes no real client.

Usage:
    python3 scripts/make_v2_mock.py
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 2026
ORG = "Contoso Engineering (illustrative mock)"

# Dimension baselines chosen so that every flag is exercised:
# D8 lags (amplification risk), executives rate higher than hands-on
# engineers (perception gap), and D6 has many NA answers (low
# confidence).
BASE = {"D1": 2.6, "D2": 2.0, "D3": 1.8, "D4": 2.4, "D5": 1.9,
        "D6": 1.7, "D7": 1.6, "D8": 0.9, "D9": 1.4}
PEOPLE = [
    ("Executive (CTO, VP, Director)", "The whole organization",
     "More than 10", "Less than 20%", 0.8, 3),
    ("Engineering manager / tech lead", "Several teams in one business "
     "unit", "6-10", "20-50%", 0.4, 2),
    ("Software engineer / developer", "A single team", "2-5",
     "More than 80%", 0.0, 5),
    ("Platform / DevOps / SRE engineer", "One business unit", "6-10",
     "51-80%", 0.1, 2),
    ("Security / AppSec", "The whole organization", "More than 10",
     "51-80%", -0.1, 1),
    ("Product / program manager", "One business unit", "2-5",
     "Less than 20%", 0.6, 1),
]
TOOLS = [
    "GitHub Copilot in the IDE (completions, chat, agent mode)",
    "GitHub Copilot cloud agent / code review / CLI",
    "Claude Code or Claude in other clients",
    "Internal or self-hosted models",
]


def build() -> dict:
    rng = random.Random(SEED)
    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    respondents = []
    n = 0
    for role, scope, years, hands_on, bias, count in PEOPLE:
        for _ in range(count):
            n += 1
            answers = {}
            for d in fw["dimensions"]:
                for q in d["questions"]:
                    na_rate = 0.45 if d["id"] == "D6" else 0.05
                    if rng.random() < na_rate:
                        answers[q["id"]] = {"level": None, "evidence": ""}
                        continue
                    raw = BASE[d["id"]] + bias + rng.uniform(-0.9, 0.9)
                    level = max(0, min(4, round(raw)))
                    ev = ""
                    if rng.random() < 0.4:
                        ev = ("Illustrative mock: "
                              + q["evidence_examples"]["en"])
                    answers[q["id"]] = {"level": level, "evidence": ev}
            tools = rng.sample(TOOLS, k=rng.randint(1, 3))
            respondents.append({
                "id": f"R{n:02d}",
                "name": f"Respondent {n:02d} (mock)",
                "email": "",
                "profile": {"R-Q1": role, "R-Q2": scope, "R-Q3": tools,
                            "R-Q4": years, "R-Q5": hands_on},
                "answers": answers,
            })
    return {
        "_comment": "Illustrative mock for framework v2. Synthetic data; "
                    "not a real client. Regenerate with "
                    "scripts/make_v2_mock.py.",
        "metadata": {
            "organization": ORG,
            "assessment_date": "2026-09-27",
            "language": "en",
            "source": "illustrative-mock",
            "framework_version": fw["version"],
        },
        "target_overrides": {},
        "dimension_weights": {},
        "respondents": respondents,
    }


def write_forms_export(data: dict, path: Path) -> None:
    import openpyxl

    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    options = fw["options"]["en"]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    header = ["ID", "Start time", "Completion time", "Email", "Name"]
    for p in fw["profile_questions"]:
        header.append(f"{p['id']}: {p['text']['en']}")
    qs = [q for d in fw["dimensions"] for q in d["questions"]]
    for q in qs:
        header += [f"{q['id']}: {q['text']['en']}",
                   f"Evidence ({q['id']})"]
    ws.append(header)
    for idx, r in enumerate(data["respondents"], start=1):
        row = [idx, "2026-09-20 09:00", "2026-09-20 09:25", r["email"],
               r["name"]]
        for p in fw["profile_questions"]:
            val = r["profile"][p["id"]]
            row.append(";".join(val) + ";" if isinstance(val, list)
                       else val)
        for q in qs:
            ans = r["answers"].get(q["id"])
            if ans is None:
                row += [None, None]
                continue
            lvl = ans["level"]
            row += [options[5] if lvl is None else options[lvl],
                    ans["evidence"] or None]
        ws.append(row)
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def main() -> int:
    data = build()
    out = ROOT / "responses.v2.json.example"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    xlsx = ROOT / "collection" / "v2-mock-forms-export.xlsx"
    write_forms_export(data, xlsx)
    print(f"✓ {out.name}: {len(data['respondents'])} mock respondents")
    print(f"✓ {xlsx.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
