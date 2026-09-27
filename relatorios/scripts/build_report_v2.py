#!/usr/bin/env python3
"""Build the v2 report payload and render the v2 PDFs.

Reads saida/scores.json, saida/gaps.json and saida/recomendacoes.json
written by scripts/assessment_engine.py for framework v2, plus
framework.v2.json and the metadata in respostas.json. Renders:

- v2_assessment_summary.pdf  overall result, flags, persona heatmap,
                             evidence coverage, backlog, strategies,
                             references
- v2_roadmap_g1.pdf .. g3    one per report group of dimensions
                             (see report_groups in framework.v2.json)

Every number comes from the engine outputs; every recommendation
quotes the L3 anchor of a question and its references. Nothing is
taken from sample data.

Usage:
    python3 relatorios/scripts/build_report_v2.py [--kit DIR]
        [--out DIR] [--no-render]
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import branding  # noqa: E402

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parent / "templates"
I18N = HERE.parent / "i18n"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def locale_of(meta: dict) -> str:
    raw = str(meta.get("language") or "en").lower().replace("_", "-")
    if raw in ("pt", "pt-br"):
        return "pt-br"
    return raw if raw in ("en", "es") else "en"


def plain_ref(text: str) -> str:
    text = re.sub(r"(?<![\w/=])_(.+?)_(?![\w])", r"\1", text)
    return re.sub(r"<(https?://[^>]+)>", r"\1", text)


def heat_class(score: float | None) -> str:
    if score is None:
        return "heat-na"
    for idx, upper in enumerate((0.8, 1.6, 2.4, 3.2)):
        if score < upper:
            return f"heat-l{idx}"
    return "heat-l4"


def build_payload(kit: Path, out: Path) -> dict:
    fw = load(kit / "framework.v2.json")
    scores = load(out / "scores.json")
    gaps = load(out / "gaps.json")
    recs = load(out / "recomendacoes.json")
    respostas = load(kit / "respostas.json")
    meta = respostas.get("metadata", {})
    loc = locale_of(meta)
    qmeta = {q["id"]: q for d in fw["dimensions"] for q in d["questions"]}
    qscore = {q["id"]: q for q in scores["questions"]}
    gap_by_dim = {g["dimension_id"]: g for g in gaps["gaps"]}
    strategies_by_dim: dict[str, list] = {}
    for s in recs["ranked_strategies"]:
        for d in s["related_dimensions"]:
            strategies_by_dim.setdefault(d["id"], []).append(s)

    cited: set[int] = set()
    dims = []
    for d in fw["dimensions"]:
        sd = next(x for x in scores["dimensions"] if x["id"] == d["id"])
        questions = []
        for q in d["questions"]:
            s = qscore[q["id"]]
            questions.append({
                "id": q["id"],
                "title": q["title"][loc],
                "text": q["text"][loc],
                "score": s["score"],
                "level": s["level"],
                "n": s["n"],
                "na": s["na"],
                "evidence_n": s["evidence_n"],
                "unverified": s["unverified"],
                "l3": q["anchors"]["l3"][loc],
                "l4": q["anchors"]["l4"][loc],
                "basis": q["basis"],
                "heat": heat_class(s["score"]),
            })
        lowest = sorted((q for q in questions if q["score"] is not None),
                        key=lambda q: (q["score"], q["id"]))[:3]
        for q in lowest:
            cited.update(q["basis"])
        dims.append({
            **sd,
            "why_it_matters": d["why_it_matters"][loc],
            "heat": heat_class(sd["score"]),
            "questions": questions,
            "lowest": lowest,
            "gap": gap_by_dim.get(d["id"]),
            "strategies": strategies_by_dim.get(d["id"], []),
        })

    role_q = next(q for q in fw["profile_questions"]
                  if q["id"] == fw["personas"]["role_question"])
    role_en = role_q["options"]["en"]
    role_loc = role_q["options"].get(loc, role_en)
    personas = [{**p, "persona": role_loc[role_en.index(p["persona"])]
                 if p["persona"] in role_en else p["persona"]}
                for p in scores["personas"]]
    heatmap = [{
        "id": d["id"], "name": d["name"], "overall": d["score"],
        "overall_heat": d["heat"],
        "cells": [{"score": p["dimension_scores"].get(d["id"]),
                   "heat": heat_class(p["dimension_scores"].get(d["id"]))}
                  for p in personas],
    } for d in dims]

    for s in recs["ranked_strategies"]:
        cited.update(s.get("references", []))
    for b in scores["backlog"]:
        cited.update(b["basis"])
    plain = [{"n": r["n"], "text": plain_ref(r["text"])}
             for r in fw["references"]]
    refs = [r for r in plain if r["n"] in cited]

    groups = []
    for g in fw["report_groups"]:
        gdims = [d for d in dims if d["id"] in g["dimensions"]]
        gref = sorted({n for d in gdims for q in d["lowest"]
                       for n in q["basis"]})
        groups.append({"id": g["id"], "name": g["name"][loc],
                       "dimensions": gdims,
                       "references": [r for r in plain
                                      if r["n"] in gref]})

    today = datetime.date.today().isoformat()
    org = meta.get("organization") or None
    return {
        "locale": loc,
        "organization": {"name": org},
        "assessment": {
            "date": meta.get("assessment_date") or today,
            "generated": today,
            "framework_version": fw["version"],
            "respondents": scores["metadata"]["respondents"],
            "source": meta.get("source"),
        },
        "branding": {
            "author": branding.AUTHOR, "role": branding.ROLE,
            "contact": branding.CONTACT,
        },
        "level_names": fw["level_names"][loc],
        "level_bands": fw["level_bands"],
        "scoring": fw["scoring"],
        "overall": scores["overall"],
        "threshold": scores["threshold"],
        "flags": scores["flags"],
        "evidence": scores["evidence"],
        "backlog": scores["backlog"],
        "dimensions": dims,
        "personas": personas,
        "heatmap": heatmap,
        "gaps_summary": gaps["summary"],
        "strategies": recs["ranked_strategies"],
        "skipped_strategies": recs["skipped_strategies"],
        "groups": groups,
        "references": refs,
    }


def render_all(payload: dict, out: Path) -> list[Path]:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
    from weasyprint import CSS, HTML

    strings = load(I18N / f"{payload['locale']}.json")
    pat = re.compile(r"\{(\w+)\}")

    def t(key: str, **kw) -> str:
        s = strings.get(key, f"⟨{key}⟩")
        return pat.sub(lambda m: str(kw.get(m.group(1), m.group(0))),
                       s) if kw else s

    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True,
                      lstrip_blocks=True)
    env.globals["t"] = t
    targets = [("v2_assessment_summary.html.j2", {},
                "v2_assessment_summary")]
    targets += [("v2_roadmap_group.html.j2", {"group": g},
                 f"v2_roadmap_{g['id'].lower()}")
                for g in payload["groups"]]
    written = []
    css = CSS(filename=str(TEMPLATES / "_print.css"))
    for tmpl, extra, label in targets:
        html = env.get_template(tmpl).render(**payload, **extra)
        (out / f"{label}.html").write_text(html, encoding="utf-8")
        pdf = out / f"{label}.pdf"
        HTML(string=html, base_url=str(TEMPLATES)).write_pdf(
            pdf, stylesheets=[css])
        written.append(pdf)
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--kit", default=str(HERE.parents[1]))
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-render", action="store_true")
    args = ap.parse_args()
    kit = Path(args.kit).resolve()
    out = Path(args.out).resolve() if args.out else kit / "saida"
    try:
        payload = build_payload(kit, out)
    except FileNotFoundError as exc:
        print(f"✗ {exc}. Run python3 scripts/assessment_engine.py all "
              f"first.", file=sys.stderr)
        return 1
    except KeyError as exc:
        print(f"✗ saida/*.json is not a v2 result ({exc}). Rerun the "
              f"engine with a v2 respostas.json.", file=sys.stderr)
        return 1
    (out / "payload_v2.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"✓ payload_v2.json ({payload['locale']})")
    if args.no_render:
        return 0
    for pdf in render_all(payload, out):
        print(f"  ✓ {pdf.name}: {pdf.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
