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
- v2_implementation_guide.pdf  governance, phased plan by priority,
                             change management, risks from the flags,
                             success metrics and the first 90 days;
                             reads implementation-guide-inputs.json
                             (wizard) when present

Every number comes from the engine outputs; every recommendation
quotes the L3 anchor of a question and its references. Nothing is
taken from sample data.

With --payload FILE the PDFs are rendered from an existing payload (for
example referencia/exemplo-saida/payload_v2.json) without the engine
outputs, which is handy when working on the templates.

Usage:
    python3 relatorios/scripts/build_report_v2.py [--kit DIR]
        [--out DIR] [--no-render] [--payload FILE]
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import branding  # noqa: E402
import wizard_inputs  # noqa: E402

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parent / "templates"
I18N = HERE.parent / "i18n"
PRIORITY_KEYS = ("P0", "P1", "P2", "P3")


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


def crosschecks(out: Path, fw: dict, qscore: dict) -> dict:
    """Repository scan and Copilot telemetry next to D4 and D9 answers.

    Each check gives the highest level the evidence supports for one
    question; ``flag`` is set when the answers sit in a higher band.
    """
    import engine_v2 as v2  # scripts/, added to sys.path above
    result: dict = {"repo": None, "telemetry": None}

    def compare(qid: str, implied: int | None) -> dict:
        q = qscore[qid]
        band = v2.band_index(fw, q["score"])
        return {"qid": qid, "score": q["score"], "level": q["level"],
                "implied_level": None if implied is None else f"L{implied}",
                "flag": bool(band is not None and implied is not None
                             and band > implied)}

    repo_path = out / "repo-scan.json"
    if repo_path.exists():
        scan = load(repo_path)
        summ = scan["summary"]
        result["repo"] = {
            **summ,
            "source": scan["metadata"].get("source"),
            "d4q4": compare("D4-Q4", v2.coverage_level_index(
                summ["share_l2_or_higher"])),
            "d4q5": {"qid": "D4-Q5", **{k: qscore["D4-Q5"][k]
                                        for k in ("score", "level")}},
        }
    tel_path = out / "telemetria.json"
    if tel_path.exists():
        tel = load(tel_path)
        result["telemetry"] = {
            **{k: tel.get(k) for k in ("report_day", "population",
                                       "phases", "shares", "seats",
                                       "active_users")},
            "d4q1": compare("D4-Q1", v2.agentic_level_index(
                tel.get("shares") or {})),
            "d9q1": {"qid": "D9-Q1", **{k: qscore["D9-Q1"][k]
                                        for k in ("score", "level")}},
        }
    return result


def survey_context(out: Path, fw: dict, qscore: dict) -> dict | None:
    """Developer Survey results next to the v2 questions they inform.

    Reads the latest saida/maturidade-developer-survey-*.json. Older
    files keyed D2..D8 are read as DS-D2..DS-D8. Context only: survey
    results never change v2 scores.
    """
    files = sorted(out.glob("maturidade-developer-survey-*.json"),
                   reverse=True)
    if not files:
        return None
    try:
        mat = load(files[0])
    except (OSError, ValueError):
        return None
    crosswalk = fw.get("survey_crosswalk") or {}
    rows = []
    for did, entry in (mat.get("dimensions") or {}).items():
        if not isinstance(entry, dict):
            continue
        key = did if did.startswith("DS-") else f"DS-{did}"
        rows.append({
            "id": key,
            "name": entry.get("name"),
            "score": entry.get("team_score"),
            "label": entry.get("label"),
            "questions": [{"id": q, "score": qscore[q]["score"]}
                          for q in crosswalk.get(key, []) if q in qscore],
        })
    meta = mat.get("metadata") or {}
    overall = mat.get("team_overall") or {}
    return {"source": files[0].name, "rows": rows,
            "respondents": meta.get("n_respondents"),
            "overall": overall.get("score"),
            "overall_label": overall.get("label")}


def plan_risks(scores: dict, checks: dict | None = None) -> list[dict]:
    """Risks implied by the scoring flags, in reading order."""
    flags, thr = scores["flags"], scores["threshold"]
    checks = checks or {}
    risks = []
    if thr["status"] != "OK":
        risks.append({"kind": "coverage", "items": [],
                      "status": thr["status"], "answered": thr["answered"],
                      "applicable": thr["applicable"]})
    if flags["amplification_risk"]:
        risks.append({"kind": "amplification", "items": [
            a["dimension_id"] for a in flags["amplification_risk"]]})
    pg = flags["perception_gap"]
    if pg["status"] == "insufficient_sample":
        risks.append({"kind": "perception_sample", "items": [],
                      "min_n": pg["min_n"]})
    elif pg["dimensions"]:
        risks.append({"kind": "perception", "items": [
            d["dimension_id"] for d in pg["dimensions"]]})
    if flags.get("respondent_divergence"):
        risks.append({"kind": "divergence", "items": [
            d["dimension_id"] for d in flags["respondent_divergence"]]})
    if flags["low_confidence"]:
        risks.append({"kind": "low_confidence",
                      "items": flags["low_confidence"]})
    if scores["evidence"]["unverified_questions"]:
        risks.append({"kind": "unverified",
                      "items": scores["evidence"]["unverified_questions"]})
    if flags["scope_caveat"]["flagged"]:
        risks.append({"kind": "scope", "items": []})
    repo, tel = checks.get("repo"), checks.get("telemetry")
    if repo and repo["d4q4"]["flag"]:
        risks.append({"kind": "repo_gap", "items": ["D4-Q4"]})
    if tel and tel["d4q1"]["flag"]:
        risks.append({"kind": "telemetry_gap", "items": ["D4-Q1"]})
    keys = ("status", "answered", "applicable", "min_n")
    return [{**{k: None for k in keys}, **r} for r in risks]


def strategy_groups(strategies: list[dict]) -> list[dict]:
    """Strategies that share a first action, listed once."""
    groups: list[dict] = []
    for s in strategies:
        name = f"{s['strategy_id']} {s['strategy_name']}"
        for g in groups:
            if g["action"] == s["first_action"]:
                g["names"].append(name)
                break
        else:
            groups.append({"names": [name], "action": s["first_action"]})
    return groups


WIZARD_KEYS = (
    "executive_steering_committee", "tpo", "dimension_owners",
    "raci_matrix", "communication_plan", "training_plan", "adkar_notes",
    "risk_register", "quick_wins_w1_4", "quick_wins_w5_8",
    "quick_wins_w9_12",
)


def implementation_plan(kit: Path, dims: list[dict], scores: dict,
                        strategies: list[dict],
                        checks: dict | None = None) -> dict:
    """Part 4 content: phases by priority plus the wizard inputs."""
    wiz = wizard_inputs.load_wizard(kit / "implementation-guide-inputs.json")
    owners = {o["dimension"]: o["owner"]
              for o in wiz.get("dimension_owners") or []}
    phases = []
    for key in PRIORITY_KEYS:
        pdims = [d for d in dims
                 if d["gap"] and d["gap"]["priority"].split()[0] == key]
        if not pdims:
            continue
        phases.append({
            "priority": key,
            "horizon": pdims[0]["gap"]["horizon_suggested"],
            "dimensions": [{**d, "owner": owners.get(d["id"])}
                           for d in pdims],
            "strategy_groups": strategy_groups(
                [s for s in strategies
                 if s["max_priority"].split()[0] == key]),
        })
    with_gap = [d for d in dims if d["gap"]]
    meta = wiz.pop("_metadata", {})
    return {
        "wizard": {k: wiz.get(k) for k in WIZARD_KEYS},
        "wizard_present": bool(meta) or bool(wiz),
        "wizard_completion": meta.get("completion_pct"),
        "owners": owners,
        "with_gap": [{**d, "owner": owners.get(d["id"])}
                     for d in with_gap],
        "phases": phases,
        "risks": plan_risks(scores, checks),
        "d2": next(d for d in dims if d["id"] == "D2"),
    }


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
                "evidence_examples": q["evidence_examples"][loc],
                "unit": q["unit"],
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
    checks = crosschecks(out, fw, qscore)
    if checks["repo"]:
        cited.add(47)
    if checks["telemetry"]:
        cited.add(6)
    if scores["flags"]["amplification_risk"]:
        cited.add(3)
    if scores["flags"]["perception_gap"]["dimensions"]:
        cited.add(35)
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

    impl = implementation_plan(kit, dims, scores, recs["ranked_strategies"],
                               checks)
    plans = sorted(out.glob("plano-capacitacao-*.md"), reverse=True)
    impl["learning_plan"] = plans[0].name if plans else None
    impl_cited = {n for d in impl["with_gap"] for q in d["lowest"]
                  for n in q["basis"]}
    impl_cited.add(6)
    if checks["repo"]:
        impl_cited.add(47)
    if any(r["kind"] == "amplification" for r in impl["risks"]):
        impl_cited.add(3)
    impl["references"] = [r for r in plain if r["n"] in impl_cited]

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
        "impl": impl,
        "survey": survey_context(out, fw, qscore),
        "checks": checks,
    }


def make_env(locale: str):
    """Jinja environment with t(), fmt() and interval() for a locale."""
    from jinja2 import Environment, FileSystemLoader, StrictUndefined

    strings = load(I18N / f"{locale}.json")
    pat = re.compile(r"\{(\w+)\}")

    def t(key: str, **kw) -> str:
        s = strings.get(key, f"⟨{key}⟩")
        return pat.sub(lambda m: str(kw.get(m.group(1), m.group(0))),
                       s) if kw else s

    comma = locale in ("pt-br", "es")

    def fmt(value, digits: int = 2) -> str:
        if value is None:
            return "-"
        text = f"{value:.{digits}f}"
        return text.replace(".", ",") if comma else text

    def interval(low: float, high: float, closed: bool) -> str:
        sep = "; " if comma else ", "
        end = "]" if closed else ")"
        return f"[{fmt(low, 1)}{sep}{fmt(high, 1)}{end}"

    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True,
                      lstrip_blocks=True)
    env.globals.update(t=t, fmt=fmt, interval=interval)
    return env


def render_pdf(env, template: str, context: dict, out: Path,
               label: str) -> Path:
    """Render one template to out/label.html and out/label.pdf."""
    from weasyprint import CSS, HTML

    html = env.get_template(template).render(**context)
    (out / f"{label}.html").write_text(html, encoding="utf-8")
    pdf = out / f"{label}.pdf"
    HTML(string=html, base_url=str(TEMPLATES)).write_pdf(
        pdf, stylesheets=[CSS(filename=str(TEMPLATES / "_print.css"))])
    return pdf


def render_all(payload: dict, out: Path) -> list[Path]:
    env = make_env(payload["locale"])
    targets = [("v2_assessment_summary.html.j2", {},
                "v2_assessment_summary")]
    targets += [("v2_roadmap_group.html.j2", {"group": g},
                 f"v2_roadmap_{g['id'].lower()}")
                for g in payload["groups"]]
    targets.append(("v2_implementation_guide.html.j2", {},
                    "v2_implementation_guide"))
    return [render_pdf(env, tmpl, {**payload, **extra}, out, label)
            for tmpl, extra, label in targets]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--kit", default=str(HERE.parents[1]))
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-render", action="store_true")
    ap.add_argument("--payload", help="render from this payload_v2.json")
    args = ap.parse_args()
    kit = Path(args.kit).resolve()
    out = Path(args.out).resolve() if args.out else kit / "saida"
    if args.payload:
        out.mkdir(parents=True, exist_ok=True)
        for pdf in render_all(load(Path(args.payload)), out):
            print(f"  ✓ {pdf.name}: {pdf.stat().st_size:,} bytes")
        return 0
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
