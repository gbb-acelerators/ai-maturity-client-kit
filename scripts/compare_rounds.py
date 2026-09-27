#!/usr/bin/env python3
"""Compare two assessment rounds (v1 or v2 respostas.json files).

- v2 → v2: overall, dimension and question deltas (same questions).
- v1 → v2: indicative baseline through the v1 lineage in
  framework.v2.json. A v2 question gets the mean of the v1 questions it
  was consolidated from; dimensions use only questions with a lineage.
  The v2 anchors and bands are new, so the deltas are indicative, never
  a like-for-like trend.
- v1 → v1: overall, pillar and question deltas.

Writes saida/comparacao-rodadas.json and saida/comparacao-rodadas.md.

Usage:
    python3 scripts/compare_rounds.py BEFORE.json AFTER.json [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import assessment_engine as v1  # noqa: E402
import engine_v2 as v2  # noqa: E402


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def delta(before: float | None, after: float | None) -> float | None:
    if before is None or after is None:
        return None
    return round(after - before, 3)


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def v1_question_levels(respostas: dict) -> dict[str, float | None]:
    fw = load(ROOT / "framework.json")
    known = {q["id"] for p in fw["pillars"] for c in p["capabilities"]
             for q in c["questions"]}
    return v1.read_levels(respostas, known)


def v2_scores(respostas: dict) -> dict:
    fw = load(ROOT / "framework.v2.json")
    return v2.compute_scores(fw, respostas, v1.locale_of(respostas))


def compare_v2_v2(before: dict, after: dict) -> dict:
    sb, sa = v2_scores(before), v2_scores(after)
    qb = {q["id"]: q["score"] for q in sb["questions"]}
    db = {d["id"]: d["score"] for d in sb["dimensions"]}
    return {
        "mode": "v2-v2",
        "overall": {"before": sb["overall"]["score"],
                    "after": sa["overall"]["score"],
                    "delta": delta(sb["overall"]["score"],
                                   sa["overall"]["score"])},
        "units": [{"id": d["id"], "name": d["name"],
                   "before": db.get(d["id"]), "after": d["score"],
                   "delta": delta(db.get(d["id"]), d["score"])}
                  for d in sa["dimensions"]],
        "questions": [{"id": q["id"], "before": qb.get(q["id"]),
                       "after": q["score"],
                       "delta": delta(qb.get(q["id"]), q["score"])}
                      for q in sa["questions"]],
        "caveats": [],
    }


def compare_v1_v2(before: dict, after: dict) -> dict:
    fw = load(ROOT / "framework.v2.json")
    levels = v1_question_levels(before)
    sa = v2_scores(after)
    qa = {q["id"]: q["score"] for q in sa["questions"]}
    questions, units = [], []
    for d in fw["dimensions"]:
        pairs = []
        for q in d["questions"]:
            lineage = q.get("v1_lineage") or []
            values = [levels[x["id"]] for x in lineage
                      if levels.get(x["id"]) is not None]
            base = mean(values)
            partial = any(x.get("partial") for x in lineage)
            if lineage:
                questions.append({
                    "id": q["id"], "v1_ids": [x["id"] for x in lineage],
                    "partial": partial, "before": v2.r3(base),
                    "after": qa.get(q["id"]),
                    "delta": delta(base, qa.get(q["id"]))})
            if base is not None and qa.get(q["id"]) is not None:
                pairs.append((base, qa[q["id"]]))
        units.append({
            "id": d["id"], "name": v2.tr(d["name"], v1.locale_of(after)),
            "comparable_questions": len(pairs),
            "before": v2.r3(mean([b for b, _ in pairs])),
            "after": v2.r3(mean([a for _, a in pairs])),
            "delta": delta(mean([b for b, _ in pairs]),
                           mean([a for _, a in pairs]))})
    return {
        "mode": "v1-v2",
        "overall": {"before": None, "after": sa["overall"]["score"],
                    "delta": None},
        "units": units,
        "questions": questions,
        "caveats": [
            "v1 and v2 use different questions, anchors and bands; deltas "
            "are indicative only.",
            "Only v2 questions with a v1 lineage are compared; 'partial' "
            "marks a v1 question that covers only part of the v2 question.",
            "No overall delta is given across versions.",
        ],
    }


def compare_v1_v1(before: dict, after: dict) -> dict:
    fw = load(ROOT / "framework.json")
    sb = v1.compute_scores(fw, before)
    sa = v1.compute_scores(fw, after)
    lb, la = v1_question_levels(before), v1_question_levels(after)
    pb = {p["id"]: p["score"] for p in sb["pillars"]}
    return {
        "mode": "v1-v1",
        "overall": {"before": sb["overall"]["score"],
                    "after": sa["overall"]["score"],
                    "delta": delta(sb["overall"]["score"],
                                   sa["overall"]["score"])},
        "units": [{"id": p["id"], "name": p.get("name_pt_br", p["id"]),
                   "before": pb.get(p["id"]), "after": p["score"],
                   "delta": delta(pb.get(p["id"]), p["score"])}
                  for p in sa["pillars"]],
        "questions": [{"id": q, "before": lb.get(q), "after": la.get(q),
                       "delta": delta(lb.get(q), la.get(q))}
                      for q in sorted(set(lb) | set(la))],
        "caveats": [],
    }


def to_markdown(result: dict) -> str:
    def num(v):
        return "-" if v is None else f"{v:.2f}"

    def sgn(v):
        return "-" if v is None else f"{v:+.2f}"

    o = result["overall"]
    lines = [f"# Assessment round comparison ({result['mode']})", "",
             f"Overall: {num(o['before'])} → {num(o['after'])} "
             f"({sgn(o['delta'])})", ""]
    for c in result["caveats"]:
        lines.append(f"> {c}")
    if result["caveats"]:
        lines.append("")
    lines += ["| Unit | Name | Before | After | Delta |",
              "| --- | --- | ---: | ---: | ---: |"]
    for u in result["units"]:
        lines.append(f"| {u['id']} | {u['name']} | {num(u['before'])} | "
                     f"{num(u['after'])} | {sgn(u['delta'])} |")
    moved = sorted((q for q in result["questions"]
                    if q["delta"] is not None),
                   key=lambda q: q["delta"])
    if moved:
        lines += ["", "## Largest drops", "",
                  "| Question | Before | After | Delta |",
                  "| --- | ---: | ---: | ---: |"]
        for q in moved[:5]:
            lines.append(f"| {q['id']} | {num(q['before'])} | "
                         f"{num(q['after'])} | {sgn(q['delta'])} |")
        lines += ["", "## Largest gains", "",
                  "| Question | Before | After | Delta |",
                  "| --- | ---: | ---: | ---: |"]
        for q in reversed(moved[-5:]):
            lines.append(f"| {q['id']} | {num(q['before'])} | "
                         f"{num(q['after'])} | {sgn(q['delta'])} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("before")
    ap.add_argument("after")
    ap.add_argument("--out", default=str(ROOT / "saida"))
    args = ap.parse_args()
    before, after = load(Path(args.before)), load(Path(args.after))
    mb, ma = v1.framework_major(before), v1.framework_major(after)
    if mb >= 2 and ma >= 2:
        result = compare_v2_v2(before, after)
    elif mb < 2 and ma >= 2:
        result = compare_v1_v2(before, after)
    elif mb < 2 and ma < 2:
        result = compare_v1_v1(before, after)
    else:
        print("✗ The BEFORE round is newer than the AFTER round.",
              file=sys.stderr)
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "comparacao-rodadas.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    (out / "comparacao-rodadas.md").write_text(to_markdown(result),
                                               encoding="utf-8")
    print(f"✓ {out / 'comparacao-rodadas.md'} ({result['mode']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
