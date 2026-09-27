#!/usr/bin/env python3
"""Deterministic scoring engine for the AI Maturity Assessment (v1).

Implements referencia/pontuacao-e-calculo.md: capability, pillar, and
overall scores (SUMPRODUCT), coverage threshold, PE score, gap analysis,
and strategy recommendations. The skills /calcular-scores, /gap-analysis,
and /recomendar-estrategias call this script instead of computing in chat.

Usage:
    python3 scripts/assessment_engine.py all
    python3 scripts/assessment_engine.py scores
    python3 scripts/assessment_engine.py gaps
    python3 scripts/assessment_engine.py recommendations
    python3 scripts/assessment_engine.py all --respostas X.json --out DIR
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = 3.0
GAP_EPSILON = 1e-9

# Canonical labels stored in the JSON outputs (shared with the platform).
LEVEL_LABELS = (
    "L0 — Inicial",
    "L1 — Em Desenvolvimento",
    "L2 — Definido",
    "L3 — Gerenciado",
    "L4 — Otimizando",
)
PRIORITY_LABELS = (
    "P0 — Crítico",
    "P1 — Alto",
    "P2 — Médio",
    "P3 — Baixo",
)
HORIZONS = {
    "en": ("30 days", "Next quarter", "Semester", "Backlog / monitor"),
    "pt-br": ("30 dias", "Próximo trimestre", "Semestre",
              "Backlog / monitorar"),
    "es": ("30 días", "Próximo trimestre", "Semestre",
           "Backlog / monitorear"),
}
FIRST_ACTIONS = {
    "en": {
        "S1": "Inventory current repositories, then plan the migration "
              "to GitHub Enterprise Cloud in 3 waves.",
        "S2": "Define SLOs/SLIs for critical services; deploy Azure "
              "Monitor and Grafana dashboards.",
        "S3": "Select 1 or 2 pilot apps; replatform to Azure Container "
              "Apps with IaC in Terraform.",
        "S4": "Identify 2 high-ROI use cases; build a PoC with Azure "
              "OpenAI and Prompt Flow.",
        "S5": "Roll out Copilot Enterprise to 2 pilot squads; measure "
              "adoption and DORA productivity for 8 weeks.",
        "S6": "Pilot Semantic Kernel for 1 internal workflow; establish "
              "guardrails and observability.",
        "S7": "Enable GitHub Advanced Security on all repos; generate "
              "SBOMs for critical services.",
    },
    "pt-br": {
        "S1": "Inventário de repositórios atuais → plano de migração "
              "para GitHub Enterprise Cloud em 3 ondas.",
        "S2": "Definir SLOs/SLIs para serviços críticos; implantar "
              "Azure Monitor + dashboards Grafana.",
        "S3": "Selecionar 1–2 apps piloto; replatforming para Azure "
              "Container Apps + IaC com Terraform.",
        "S4": "Identificar 2 casos de uso de alto ROI; PoC com Azure "
              "OpenAI + Prompt Flow.",
        "S5": "Rollout Copilot Enterprise em 2 squads piloto; medir "
              "adoção e produtividade DORA por 8 semanas.",
        "S6": "Pilot Semantic Kernel para 1 workflow interno; "
              "estabelecer guardrails e observabilidade.",
        "S7": "Habilitar GitHub Advanced Security em todos repos; "
              "gerar SBOM dos serviços críticos.",
    },
}
FALLBACK_ACTION = {
    "en": "Detail with a Microsoft GBB architect.",
    "pt-br": "Detalhar com arquiteto Microsoft GBB.",
}
OUTCOME = {
    "en": "Raise {caps} toward the target level; re-assess to confirm.",
    "pt-br": "Elevar {caps} em direção ao nível-alvo; reavaliar para "
             "confirmar.",
}
SKIP_REASON = {
    "en": {"none": "no related gaps", "low": "monitor (only P3 gaps)"},
    "pt-br": {"none": "sem gaps relacionados",
              "low": "monitorar (apenas gaps P3)"},
}


class InputError(ValueError):
    pass


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def now_iso() -> str:
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%SZ")


def locale_of(respostas: dict) -> str:
    raw = str(respostas.get("metadata", {}).get("language") or "en")
    raw = raw.lower().replace("_", "-")
    if raw in ("pt", "pt-br"):
        return "pt-br"
    return raw if raw in ("en", "es") else "en"


def text_locale(locale: str) -> str:
    # Templates exist in EN and PT-BR; ES falls back to EN.
    return "pt-br" if locale == "pt-br" else "en"


def level_label(score: float | None) -> str:
    if score is None:
        return "Sem resposta"
    for idx, upper in enumerate((0.5, 1.5, 2.5, 3.5)):
        if score < upper:
            return LEVEL_LABELS[idx]
    return LEVEL_LABELS[4]


def priority_label(priority_score: float) -> str:
    for idx, lower in enumerate((2.4, 1.6, 0.9)):
        if priority_score >= lower:
            return PRIORITY_LABELS[idx]
    return PRIORITY_LABELS[3]


def priority_index(label: str) -> int:
    return PRIORITY_LABELS.index(label)


def threshold_status(answered: int) -> str:
    if answered >= 40:
        return "OK"
    if answered >= 25:
        return "WARNING"
    return "BLOCKED"


def r3(value: float | None, precise: bool = False) -> float | None:
    if value is None or precise:
        return value
    return round(value, 3)


def read_levels(respostas: dict, known_ids: set[str]) -> dict:
    levels: dict[str, float | None] = {}
    errors = []
    for qid, entry in (respostas.get("responses") or {}).items():
        if qid not in known_ids:
            continue
        level = entry.get("level") if isinstance(entry, dict) else None
        if level is None:
            levels[qid] = None
            continue
        if isinstance(level, bool) or not isinstance(level, (int, float)):
            errors.append(f"{qid}: level {level!r} is not numeric")
            continue
        if not 0 <= level <= 4:
            errors.append(f"{qid}: level {level} is outside 0-4")
            continue
        levels[qid] = float(level)
    if errors:
        raise InputError("Invalid levels:\n  " + "\n  ".join(errors))
    return levels


def weighted_mean(pairs: list[tuple[float, float]]) -> float | None:
    total = sum(weight for _, weight in pairs)
    if total <= 0:
        return None
    return sum(value * weight for value, weight in pairs) / total


def capability_score(cap: dict, levels: dict, pe_only: bool) -> tuple:
    pairs = []
    applicable = 0
    for q in cap["questions"]:
        if pe_only and not q.get("pe"):
            continue
        applicable += 1
        level = levels.get(q["id"])
        if level is not None:
            pairs.append((level, float(q.get("weight", 1.0))))
    return weighted_mean(pairs), len(pairs), applicable


def compute_scores(
    framework: dict, respostas: dict, precise: bool = False
) -> dict:
    known = {
        q["id"]
        for p in framework["pillars"]
        for c in p["capabilities"]
        for q in c["questions"]
    }
    levels = read_levels(respostas, known)
    caps_out, pillars_out = [], []
    all_pairs, pe_pairs = [], []
    total_answered = 0
    for pillar in framework["pillars"]:
        pillar_pairs = []
        p_answered = p_applicable = 0
        for cap in pillar["capabilities"]:
            weight = float(cap.get("weight", 1.0))
            score, answered, applicable = capability_score(
                cap, levels, pe_only=False)
            pe_score, _, pe_applicable = capability_score(
                cap, levels, pe_only=True)
            if score is not None:
                pillar_pairs.append((score, weight))
                all_pairs.append((score, weight))
            if pe_applicable and pe_score is not None:
                pe_pairs.append((pe_score, weight))
            p_answered += answered
            p_applicable += applicable
            caps_out.append({
                "id": cap["id"],
                "name_pt_br": cap.get("name_pt_br", cap.get("name")),
                "pillar_id": pillar["id"],
                "weight": weight,
                "score": r3(score, precise),
                "label": level_label(score),
                "answered": answered,
                "applicable": applicable,
                "strategies": cap.get("strategies", []),
            })
        p_score = weighted_mean(pillar_pairs)
        p_score = 0.0 if p_score is None else p_score
        total_answered += p_answered
        pillars_out.append({
            "id": pillar["id"],
            "name_pt_br": pillar.get("name_pt_br", pillar.get("name")),
            "score": r3(p_score),
            "label": level_label(p_score),
            "answered": p_answered,
            "applicable": p_applicable,
        })
    overall = weighted_mean(all_pairs)
    pe_overall = weighted_mean(pe_pairs)
    meta = respostas.get("metadata", {})
    return {
        "metadata": {
            "computed_at": now_iso(),
            "respondent": meta.get("respondent_name")
            or meta.get("organization"),
            "framework_version": framework.get("version"),
        },
        "overall": {
            "score": r3(overall),
            "label": level_label(overall),
            "pe_score": r3(pe_overall),
            "pe_label": level_label(pe_overall),
        },
        "threshold": {
            "status": threshold_status(total_answered),
            "answered": total_answered,
            "applicable": len(known),
        },
        "pillars": pillars_out,
        "capabilities": caps_out,
    }


def compute_gaps(precise_scores: dict, respostas: dict) -> dict:
    """Gap math uses unrounded capability scores (see scoring.rs)."""
    targets = respostas.get("target_overrides") or {}
    horizons = HORIZONS[locale_of(respostas)]
    gaps = []
    for cap in precise_scores["capabilities"]:
        if cap["score"] is None:
            continue
        target = float(targets.get(cap["id"], DEFAULT_TARGET))
        gap_size = max(0.0, target - cap["score"])
        if gap_size <= GAP_EPSILON:
            continue
        priority_score = cap["weight"] * gap_size
        label = priority_label(priority_score)
        gaps.append({
            "capability_id": cap["id"],
            "capability_name_pt_br": cap["name_pt_br"],
            "pillar_id": cap["pillar_id"],
            "current_score": r3(cap["score"]),
            "current_label": cap["label"],
            "target_level": target,
            "gap_size": r3(gap_size),
            "weight": cap["weight"],
            "priority_score": r3(priority_score),
            "priority": label,
            "horizon_suggested": horizons[priority_index(label)],
            "strategies": cap["strategies"],
        })
    gaps.sort(key=lambda g: (-g["priority_score"], g["capability_id"]))
    summary = {f"P{i}": 0 for i in range(4)}
    for rank, gap in enumerate(gaps, start=1):
        gap["rank"] = rank
        summary[gap["priority"].split(" ")[0]] += 1
    ordered = [
        {"rank": g.pop("rank"), **g} for g in gaps
    ]
    return {
        "metadata": {
            "computed_at": now_iso(),
            "default_target": DEFAULT_TARGET,
            "total_capabilities_with_gap": len(ordered),
        },
        "summary": summary,
        "gaps": ordered,
    }


def compute_recommendations(
    gaps: dict, framework: dict, respostas: dict
) -> dict:
    locale = locale_of(respostas)
    tloc = text_locale(locale)
    horizons = HORIZONS[locale]
    names = {s["id"]: s["name"] for s in framework.get("strategies", [])}
    techs = framework.get("technologies_per_strategy", {})
    groups: dict[str, dict] = {}
    for gap in gaps["gaps"]:
        for sid in gap["strategies"]:
            grp = groups.setdefault(sid, {"gaps": [], "cum": 0.0})
            grp["gaps"].append(gap)
            grp["cum"] += gap["priority_score"]
    ranked, skipped = [], []
    for sid in names:
        grp = groups.get(sid)
        if not grp:
            skipped.append({
                "strategy_id": sid,
                "strategy_name": names[sid],
                "reason": SKIP_REASON[tloc]["none"],
            })
            continue
        if grp["cum"] < 0.9:
            skipped.append({
                "strategy_id": sid,
                "strategy_name": names[sid],
                "reason": SKIP_REASON[tloc]["low"],
            })
            continue
        worst = min(priority_index(g["priority"]) for g in grp["gaps"])
        cap_ids = ", ".join(g["capability_id"] for g in grp["gaps"])
        ranked.append({
            "strategy_id": sid,
            "strategy_name": names[sid],
            "cumulative_priority": r3(grp["cum"]),
            "max_priority": PRIORITY_LABELS[worst],
            "horizon": horizons[worst],
            "related_capabilities_count": len(grp["gaps"]),
            "related_capabilities": [
                {
                    "id": g["capability_id"],
                    "name_pt_br": g["capability_name_pt_br"],
                    "gap_size": g["gap_size"],
                    "priority": g["priority"],
                }
                for g in grp["gaps"]
            ],
            "technologies": techs.get(sid, []),
            "first_action": FIRST_ACTIONS[tloc].get(
                sid, FALLBACK_ACTION[tloc]),
            "expected_outcome": OUTCOME[tloc].format(caps=cap_ids),
        })
    ranked.sort(key=lambda s: (
        -s["cumulative_priority"],
        priority_index(s["max_priority"]),
        -s["related_capabilities_count"],
        s["strategy_id"],
    ))
    return {
        "metadata": {
            "computed_at": now_iso(),
            "based_on": "saida/gaps.json",
        },
        "ranked_strategies": [
            {"rank": i, **s} for i, s in enumerate(ranked, start=1)
        ],
        "skipped_strategies": skipped,
    }


def run(step: str, respostas_path: Path, out_dir: Path) -> int:
    framework = load_json(ROOT / "framework.json")
    respostas = load_json(respostas_path)
    rf = respostas.get("metadata", {}).get("framework_version")
    if rf and rf != framework.get("version"):
        print(f"⚠️ respostas.json targets framework {rf}, framework.json "
              f"is {framework.get('version')}. Revalidate answers.")
    if step in ("scores", "all"):
        scores = compute_scores(framework, respostas)
        write_json(out_dir / "scores.json", scores)
        o, t = scores["overall"], scores["threshold"]
        print(f"✓ scores.json: overall {o['score']} ({o['label']}), "
              f"threshold {t['status']} ({t['answered']}/"
              f"{t['applicable']})")
        if t["status"] == "BLOCKED":
            print("⚠️ Fewer than 25 answers: do not use the report for "
                  "decisions.")
    if step in ("gaps", "all"):
        precise = compute_scores(framework, respostas, precise=True)
        gaps = compute_gaps(precise, respostas)
        write_json(out_dir / "gaps.json", gaps)
        total = gaps["metadata"]["total_capabilities_with_gap"]
        print(f"✓ gaps.json: {total} capabilities with gap "
              f"{gaps['summary']}")
    if step in ("recommendations", "all"):
        gaps = load_json(out_dir / "gaps.json")
        recs = compute_recommendations(gaps, framework, respostas)
        write_json(out_dir / "recomendacoes.json", recs)
        top = [s["strategy_id"] for s in recs["ranked_strategies"][:3]]
        print(f"✓ recomendacoes.json: top strategies {top}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("step", choices=("scores", "gaps", "recommendations",
                                     "all"))
    ap.add_argument("--respostas", default=str(ROOT / "respostas.json"))
    ap.add_argument("--out", default=str(ROOT / "saida"))
    args = ap.parse_args()
    try:
        return run(args.step, Path(args.respostas), Path(args.out))
    except (InputError, FileNotFoundError) as exc:
        print(f"✗ {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
