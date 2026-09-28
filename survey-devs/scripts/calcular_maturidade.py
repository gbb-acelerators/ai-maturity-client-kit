#!/usr/bin/env python3
"""Compute developer AI maturity from the survey answers.

Reads: survey-devs/respostas-devs.json (output of /importar-survey-devs)
Applies: rubric.py (deterministic L0-L4 rules per dimension)
Writes:
  - saida/maturidade-developer-survey-<DATE>.json (structured)
  - Summary on stdout

Usage:
    python3 calcular_maturidade.py
    python3 calcular_maturidade.py --input survey-devs/respostas-devs.json
    python3 calcular_maturidade.py --out saida/ --lang pt-br
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

# Allow running from any directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from rubric import (  # noqa: E402
    DIMENSIONS,
    SUPPORTED_LANGS,
    aggregate_team,
    label_for,
    score_respondent,
)

STRINGS = {
    "en": {
        "missing": "❌ Input not found: {path}",
        "run_import": "   Run /importar-survey-devs first.",
        "computing": "\n📊 Computing AI maturity: {n} respondents "
                     "(anonymous)\n",
        "none": "❌ No respondents.",
        "output": "✓ Output: {path}\n",
        "title": "TEAM AI MATURITY (n={n} anonymous devs)",
        "overall": "\n🎯 Overall: {score:.2f} ({label})\n",
        "no_overall": "\n⚠ Not enough coverage to compute overall.\n",
        "col_dim": "Dimension",
        "col_label": "Label",
        "col_dist": "Distribution (% devs)",
        "no_data": "No data",
        "empty": "-",
        "top": "🏆 Top 3 strongest dimensions:",
        "bottom": "⚠ Top 3 weakest dimensions (opportunities):",
        "rank_item": "   {i}. {did} {name}: {score:.2f} ({label})",
        "next": "Next: /insights-developer-survey generates the full "
                "report.",
    },
    "pt-br": {
        "missing": "❌ Input não encontrado: {path}",
        "run_import": "   Rode /importar-survey-devs primeiro.",
        "computing": "\n📊 Calculando maturidade IA: {n} respondentes "
                     "(anônimos)\n",
        "none": "❌ Nenhum respondente.",
        "output": "✓ Output: {path}\n",
        "title": "MATURIDADE IA DO TIME (n={n} devs anônimos)",
        "overall": "\n🎯 Overall: {score:.2f} ({label})\n",
        "no_overall": "\n⚠ Sem cobertura suficiente para calcular "
                      "overall.\n",
        "col_dim": "Dimensão",
        "col_label": "Rótulo",
        "col_dist": "Distribuição (% devs)",
        "no_data": "Sem dados",
        "top": "🏆 Top 3 dimensões mais fortes:",
        "bottom": "⚠ Top 3 dimensões mais fracas (oportunidades):",
        "rank_item": "   {i}. {did} {name}: {score:.2f} ({label})",
        "next": "Próximo: /insights-developer-survey gera o relatório "
                "completo em PT-BR.",
    },
}


def _display(path: Path, root: Path) -> Path:
    return path.relative_to(root) if path.is_relative_to(root) else path


def main():
    ap = argparse.ArgumentParser()
    kit_root = SCRIPT_DIR.parent.parent
    ap.add_argument(
        "--input",
        default=str(kit_root / "survey-devs/respostas-devs.json"),
        help="Path to respostas-devs.json",
    )
    ap.add_argument("--out", default=str(kit_root / "saida"),
                    help="Output directory")
    ap.add_argument("--lang", choices=SUPPORTED_LANGS, default="en",
                    help="Output language for labels and console text")
    args = ap.parse_args()
    lang = args.lang
    t = STRINGS[lang]

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(t["missing"].format(path=inp))
        print(t["run_import"])
        return 1

    data = json.loads(inp.read_text(encoding="utf-8"))
    respondents = data.get("respondents", [])
    n = len(respondents)
    print(t["computing"].format(n=n))

    if n == 0:
        print(t["none"])
        return 1

    # Individual scores stay internal; only aggregates are written
    individual_scores = [
        score_respondent(r["responses"], lang) for r in respondents
    ]
    team = aggregate_team(individual_scores, lang)

    date = datetime.date.today().isoformat()
    ranking = _ranking(team["dimensions"])
    output = {
        "metadata": {
            "computed_at": datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": str(_display(inp, kit_root)),
            "n_respondents": n,
            "rubric_version": "1.0 (deterministic)",
            "anonymous": True,
            "scope": "team aggregate (no individual scores in output)",
            "lang": lang,
        },
        "team_overall": {
            "score": team["team_overall_score"],
            "label": team["team_overall_label"],
            "respondents_with_overall": team["n_with_overall"],
        },
        "dimensions": team["dimensions"],
        "ranking": ranking,
    }

    out_path = out_dir / f"maturidade-developer-survey-{date}.json"
    out_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(t["output"].format(path=_display(out_path, kit_root)))

    print("═" * 60)
    print(t["title"].format(n=n))
    print("═" * 60)
    if team["team_overall_score"] is not None:
        print(t["overall"].format(
            score=team["team_overall_score"],
            label=team["team_overall_label"],
        ))
    else:
        print(t["no_overall"])

    print(f"{t['col_dim']:<10} {'Score':<8} {t['col_label']:<28} "
          f"{t['col_dist']:<35}")
    print("-" * 90)
    for did, _, _, _ in DIMENSIONS:
        d = team["dimensions"][did]
        if d["team_score"] is None:
            print(f"{did:<10} {t['empty']:<8} {t['no_data']:<28}")
            continue
        dist = d["distribution_pct"]
        dist_str = " ".join(
            f"{lvl}={dist[lvl]}%" for lvl in ("L0", "L1", "L2", "L3", "L4")
        )
        score_str = f"{d['team_score']:.2f}"
        print(f"{did:<10} {score_str:<8} {d['label']:<28} {dist_str:<35}")
    print()

    for key, items in (("top", ranking["top"]),
                       ("bottom", ranking["bottom"])):
        print(t[key])
        for i, (did, name, score) in enumerate(items, 1):
            print(t["rank_item"].format(
                i=i, did=did, name=name, score=score,
                label=label_for(score, lang),
            ))
        print()

    print(t["next"])
    return 0


def _ranking(dims: dict) -> dict:
    """Top/bottom 3 dimensions by team score."""
    scored = [
        (did, d["name"], d["team_score"])
        for did, d in dims.items()
        if d["team_score"] is not None
    ]
    sorted_desc = sorted(scored, key=lambda x: x[2], reverse=True)
    bottom = (
        list(reversed(sorted_desc[-3:])) if len(sorted_desc) >= 3
        else sorted_desc
    )
    return {"top": sorted_desc[:3], "bottom": bottom}


if __name__ == "__main__":
    sys.exit(main())
