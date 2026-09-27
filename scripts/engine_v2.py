"""Scoring engine for framework v2 (9 dimensions, 61 questions).

Implements section 8 of coleta/AI-Maturity-Form-Questions_v2.md:
pooled question means, dimension and overall scores, half-open level
bands, coverage status, low-confidence, amplification-risk,
perception-gap and scope flags, evidence coverage, persona scores,
gaps, priorities and strategy recommendations.

Called by scripts/assessment_engine.py when respostas.json declares
metadata.framework_version 2.x.
"""
from __future__ import annotations

import datetime
from collections import defaultdict

PRIORITIES = ("P0", "P1", "P2", "P3")
PRIORITY_NAMES = {
    "en": ("Critical", "High", "Medium", "Low"),
    "pt-br": ("Crítico", "Alto", "Médio", "Baixo"),
    "es": ("Crítico", "Alto", "Medio", "Bajo"),
}
HORIZONS = {
    "en": ("30 days", "Next quarter", "Semester", "Backlog / monitor"),
    "pt-br": ("30 dias", "Próximo trimestre", "Semestre",
              "Backlog / monitorar"),
    "es": ("30 días", "Próximo trimestre", "Semestre",
           "Backlog / monitorear"),
}
TEXT = {
    "en": {
        "no_answer": "No answer",
        "skip_none": "no related gaps",
        "skip_low": "monitor (only low-priority gaps)",
        "first_action": "Start with {qid} ({title}). Target the L3 "
                        "anchor: {anchor}",
        "outcome": "Move {dims} toward the target level; re-assess to "
                   "confirm with evidence.",
    },
    "pt-br": {
        "no_answer": "Sem resposta",
        "skip_none": "sem gaps relacionados",
        "skip_low": "monitorar (apenas gaps de baixa prioridade)",
        "first_action": "Comece por {qid} ({title}). Meta do âncora L3: "
                        "{anchor}",
        "outcome": "Levar {dims} ao nível-alvo; reavaliar para confirmar "
                   "com evidências.",
    },
    "es": {
        "no_answer": "Sin respuesta",
        "skip_none": "sin brechas relacionadas",
        "skip_low": "monitorear (solo brechas de baja prioridad)",
        "first_action": "Empiece por {qid} ({title}). Meta del ancla L3: "
                        "{anchor}",
        "outcome": "Llevar {dims} al nivel objetivo; reevaluar para "
                   "confirmar con evidencias.",
    },
}


class InputErrorV2(ValueError):
    pass


def now_iso() -> str:
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%SZ")


def r3(value: float | None) -> float | None:
    return None if value is None else round(value, 3)


def tr(field: dict, locale: str) -> str:
    return field.get(locale) or field.get("en") or ""


def band_index(fw: dict, score: float | None) -> int | None:
    if score is None:
        return None
    bands = fw["level_bands"]
    for idx, band in enumerate(bands):
        if score < band["max"]:
            return idx
    return len(bands) - 1


def level_code(fw: dict, score: float | None) -> str | None:
    idx = band_index(fw, score)
    return None if idx is None else fw["level_bands"][idx]["level"]


def level_label(fw: dict, score: float | None, locale: str) -> str:
    code = level_code(fw, score)
    if code is None:
        return TEXT[locale]["no_answer"]
    names = fw["level_names"].get(locale) or fw["level_names"]["en"]
    return f"{code} {names[code]}"


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def weighted_mean(pairs: list[tuple[float, float]]) -> float | None:
    total = sum(w for _, w in pairs)
    return sum(v * w for v, w in pairs) / total if total > 0 else None


def question_index(fw: dict) -> dict[str, dict]:
    out = {}
    for d in fw["dimensions"]:
        for q in d["questions"]:
            out[q["id"]] = {**q, "dimension_id": d["id"]}
    return out


def respondents_of(respostas: dict) -> list[dict]:
    """Normalize to a list of respondents with profile and answers.

    A file without ``respondents`` but with ``responses`` is treated as
    one consolidated respondent (for example a workshop answer sheet).
    """
    people = respostas.get("respondents")
    if people is None:
        people = [{"id": "consolidated", "profile": {},
                   "answers": respostas.get("responses") or {}}]
    if not isinstance(people, list):
        raise InputErrorV2("respondents must be a list")
    return people


def read_answers(people: list[dict], qindex: dict) -> None:
    errors = []
    for person in people:
        for qid, entry in (person.get("answers") or {}).items():
            if qid not in qindex:
                continue
            level = entry.get("level") if isinstance(entry, dict) else None
            if level is None:
                continue
            if isinstance(level, bool) or not isinstance(
                    level, (int, float)) or not 0 <= level <= 4:
                errors.append(f"{person.get('id')}/{qid}: level "
                              f"{level!r} must be 0-4 or null")
    if errors:
        raise InputErrorV2("Invalid levels:\n  " + "\n  ".join(errors))


def aggregate(fw: dict, people: list[dict], qindex: dict) -> dict:
    """Per-question values, NA counts and evidence counts."""
    stats = {qid: {"values": [], "na": 0, "evidence": 0}
             for qid in qindex}
    for person in people:
        for qid, entry in (person.get("answers") or {}).items():
            if qid not in stats or not isinstance(entry, dict):
                continue
            level = entry.get("level")
            if level is None:
                stats[qid]["na"] += 1
                continue
            stats[qid]["values"].append(float(level))
            if str(entry.get("evidence") or "").strip():
                stats[qid]["evidence"] += 1
    return stats


def dimension_scores(fw: dict, stats: dict) -> dict[str, float | None]:
    out = {}
    for d in fw["dimensions"]:
        qs = [mean(stats[q["id"]]["values"]) for q in d["questions"]]
        out[d["id"]] = mean([s for s in qs if s is not None])
    return out


def overall_score(fw: dict, dims: dict, weights: dict) -> float | None:
    pairs = [(s, weights[d]) for d, s in dims.items() if s is not None]
    return weighted_mean(pairs)


def dimension_weights(fw: dict, respostas: dict) -> dict[str, float]:
    lo, hi = fw["scoring"]["dimension_weight_range"]
    overrides = respostas.get("dimension_weights") or {}
    out = {}
    for d in fw["dimensions"]:
        w = float(overrides.get(d["id"], d.get("weight", 1.0)))
        if not lo <= w <= hi:
            raise InputErrorV2(f"dimension_weights.{d['id']}={w} is "
                               f"outside [{lo}, {hi}]")
        out[d["id"]] = w
    return out


def persona_groups(people: list[dict], fw: dict) -> dict[str, list]:
    role_q = fw["personas"]["role_question"]
    groups: dict[str, list] = defaultdict(list)
    for person in people:
        role = (person.get("profile") or {}).get(role_q)
        if role:
            groups[role].append(person)
    return groups


def perception_gap(fw: dict, people: list[dict], qindex: dict) -> dict:
    conf = fw["personas"]
    min_n = fw["scoring"]["persona_min_n"]
    execs, hands_on = [], []
    for person in people:
        prof = person.get("profile") or {}
        if prof.get(conf["role_question"]) in conf["executive_options"]:
            execs.append(person)
        elif prof.get(conf["hands_on_question"]) in \
                conf["hands_on_options"]:
            hands_on.append(person)
    result = {"executive_n": len(execs), "hands_on_n": len(hands_on),
              "min_n": min_n, "dimensions": []}
    if len(execs) < min_n or len(hands_on) < min_n:
        result["status"] = "insufficient_sample"
        return result
    result["status"] = "evaluated"
    ex = dimension_scores(fw, aggregate(fw, execs, qindex))
    ho = dimension_scores(fw, aggregate(fw, hands_on, qindex))
    for d in fw["dimensions"]:
        bi_e, bi_h = band_index(fw, ex[d["id"]]), band_index(fw, ho[d["id"]])
        if bi_e is not None and bi_h is not None and bi_e - bi_h >= 1:
            result["dimensions"].append({
                "dimension_id": d["id"],
                "executive_score": r3(ex[d["id"]]),
                "hands_on_score": r3(ho[d["id"]]),
            })
    return result


def scope_caveat(fw: dict, people: list[dict]) -> dict:
    mix: dict[str, int] = defaultdict(int)
    for person in people:
        scope = (person.get("profile") or {}).get("R-Q2")
        if scope:
            mix[scope] += 1
    total = sum(mix.values())
    single = fw["profile_questions"][1]["options"]["en"][0]
    share = mix.get(single, 0) / total if total else None
    limit = fw["scoring"]["single_team_scope_share"]
    return {"mix": dict(mix), "single_team_share": r3(share),
            "flagged": bool(share is not None and share > limit)}


def coverage_status(fw: dict, answered: int) -> str:
    sc = fw["scoring"]
    if answered >= sc["coverage_ok_min"]:
        return "OK"
    if answered >= sc["coverage_warning_min"]:
        return "WARNING"
    return "BLOCKED"


def compute_scores(fw: dict, respostas: dict, locale: str) -> dict:
    qindex = question_index(fw)
    people = respondents_of(respostas)
    read_answers(people, qindex)
    stats = aggregate(fw, people, qindex)
    weights = dimension_weights(fw, respostas)
    dims = dimension_scores(fw, stats)
    overall = overall_score(fw, dims, weights)
    sc = fw["scoring"]

    questions_out = []
    unverified = []
    ev_answered = ev_with = 0
    for qid, q in qindex.items():
        st = stats[qid]
        score = mean(st["values"])
        n = len(st["values"])
        ev_answered += n
        ev_with += st["evidence"]
        share = st["evidence"] / n if n else None
        is_unverified = bool(
            score is not None and band_index(fw, score) >= 3
            and share < sc["unverified_evidence_share"])
        if is_unverified:
            unverified.append(qid)
        questions_out.append({
            "id": qid,
            "dimension_id": q["dimension_id"],
            "score": r3(score),
            "level": level_code(fw, score),
            "n": n,
            "na": st["na"],
            "evidence_n": st["evidence"],
            "unverified": is_unverified,
        })

    dims_out, low_conf = [], []
    overall_band = band_index(fw, overall)
    amplification = []
    for d in fw["dimensions"]:
        answers = sum(len(stats[q["id"]]["values"]) + stats[q["id"]]["na"]
                      for q in d["questions"])
        na = sum(stats[q["id"]]["na"] for q in d["questions"])
        na_share = na / answers if answers else None
        low = bool(answers == 0 or na_share > sc["low_confidence_na_share"])
        if low:
            low_conf.append(d["id"])
        answered_q = sum(1 for q in d["questions"]
                         if stats[q["id"]]["values"])
        score = dims[d["id"]]
        bi = band_index(fw, score)
        if (d["id"] in sc["amplifier_dimensions"] and bi is not None
                and overall_band is not None and overall_band - bi >= 1):
            amplification.append({"dimension_id": d["id"],
                                  "level": level_code(fw, score),
                                  "overall_level": level_code(fw, overall)})
        dims_out.append({
            "id": d["id"],
            "name": tr(d["name"], locale),
            "group": d["group"],
            "weight": weights[d["id"]],
            "score": r3(score),
            "level": level_code(fw, score),
            "label": level_label(fw, score, locale),
            "answered": answered_q,
            "applicable": len(d["questions"]),
            "na_share": r3(na_share),
            "low_confidence": low,
            "strategies": d["strategies"],
        })

    personas_out = []
    min_n = sc["persona_min_n"]
    for role, members in sorted(persona_groups(people, fw).items()):
        pdims = dimension_scores(fw, aggregate(fw, members, qindex))
        personas_out.append({
            "persona": role,
            "n": len(members),
            "low_sample": len(members) < min_n,
            "dimension_scores": {k: r3(v) for k, v in pdims.items()},
        })

    scored_q = [q for q in questions_out if q["score"] is not None]
    scored_q.sort(key=lambda q: (q["score"], q["id"]))
    backlog = [{
        "question_id": q["id"],
        "dimension_id": q["dimension_id"],
        "title": tr(qindex[q["id"]]["title"], locale),
        "score": q["score"],
        "l3_anchor": tr(qindex[q["id"]]["anchors"]["l3"], locale),
        "basis": qindex[q["id"]]["basis"],
    } for q in scored_q[:sc["backlog_size"]]]

    pe_vals = [mean(stats[q]["values"]) for q in qindex
               if qindex[q].get("pe")]
    pe = mean([v for v in pe_vals if v is not None])
    answered_total = len(scored_q)
    meta = respostas.get("metadata", {})
    return {
        "metadata": {
            "computed_at": now_iso(),
            "organization": meta.get("organization"),
            "framework_version": fw["version"],
            "respondents": len(people),
            "language": locale,
        },
        "overall": {
            "score": r3(overall),
            "level": level_code(fw, overall),
            "label": level_label(fw, overall, locale),
            "pe_score": r3(pe),
            "pe_label": level_label(fw, pe, locale),
        },
        "threshold": {
            "status": coverage_status(fw, answered_total),
            "answered": answered_total,
            "applicable": len(qindex),
        },
        "dimensions": dims_out,
        "questions": questions_out,
        "personas": personas_out,
        "flags": {
            "low_confidence": low_conf,
            "amplification_risk": amplification,
            "perception_gap": perception_gap(fw, people, qindex),
            "scope_caveat": scope_caveat(fw, people),
        },
        "evidence": {
            "answered": ev_answered,
            "with_evidence": ev_with,
            "share": r3(ev_with / ev_answered) if ev_answered else None,
            "unverified_questions": unverified,
        },
        "backlog": backlog,
    }


def priority_of(fw: dict, value: float) -> int:
    cuts = fw["scoring"]["priority_cuts"]
    for idx, key in enumerate(("P0", "P1", "P2")):
        if value >= cuts[key]:
            return idx
    return 3


def compute_gaps(fw: dict, respostas: dict, locale: str) -> dict:
    scores = compute_scores(fw, respostas, locale)
    targets = respostas.get("target_overrides") or {}
    default = fw["scoring"]["default_target"]
    qindex = question_index(fw)
    qscores = {q["id"]: q for q in scores["questions"]}
    raw = dimension_scores(
        fw, aggregate(fw, respondents_of(respostas), qindex))
    gaps = []
    for d in scores["dimensions"]:
        score = raw[d["id"]]
        if score is None:
            continue
        target = float(targets.get(d["id"], default))
        gap = max(0.0, target - score)
        if gap <= 1e-9:
            continue
        prio = d["weight"] * gap
        pidx = priority_of(fw, prio)
        lowest = sorted(
            (qscores[q["id"]] for q in _dim(fw, d["id"])["questions"]
             if qscores[q["id"]]["score"] is not None),
            key=lambda q: (q["score"], q["id"]))[:3]
        gaps.append({
            "dimension_id": d["id"],
            "dimension_name": d["name"],
            "group": d["group"],
            "current_score": r3(score),
            "current_level": d["level"],
            "current_label": d["label"],
            "target_level": target,
            "gap_size": r3(gap),
            "weight": d["weight"],
            "priority_score": r3(prio),
            "priority": f"{PRIORITIES[pidx]} "
                        f"{PRIORITY_NAMES[locale][pidx]}",
            "horizon_suggested": HORIZONS[locale][pidx],
            "strategies": d["strategies"],
            "low_confidence": d["low_confidence"],
            "lowest_questions": [
                {"id": q["id"], "score": q["score"],
                 "l3_anchor": tr(qindex[q["id"]]["anchors"]["l3"], locale)}
                for q in lowest
            ],
        })
    gaps.sort(key=lambda g: (-g["priority_score"], g["dimension_id"]))
    summary = {p: 0 for p in PRIORITIES}
    for g in gaps:
        summary[g["priority"].split(" ")[0]] += 1
    return {
        "metadata": {
            "computed_at": now_iso(),
            "framework_version": fw["version"],
            "default_target": default,
            "total_dimensions_with_gap": len(gaps),
        },
        "summary": summary,
        "gaps": [{"rank": i, **g} for i, g in enumerate(gaps, start=1)],
    }


def _dim(fw: dict, did: str) -> dict:
    return next(d for d in fw["dimensions"] if d["id"] == did)


def compute_recommendations(fw: dict, gaps: dict, respostas: dict,
                            locale: str) -> dict:
    text = TEXT[locale]
    names = {s["id"]: s["name"] for s in fw["strategies"]}
    techs = fw.get("technologies_per_strategy", {})
    qindex = question_index(fw)
    groups: dict[str, dict] = {}
    for gap in gaps["gaps"]:
        for sid in gap["strategies"]:
            grp = groups.setdefault(sid, {"gaps": [], "cum": 0.0})
            grp["gaps"].append(gap)
            grp["cum"] += gap["priority_score"]
    minimum = fw["scoring"]["strategy_min_cumulative"]
    ranked, skipped = [], []
    for sid, name in names.items():
        grp = groups.get(sid)
        if not grp or grp["cum"] < minimum:
            skipped.append({"strategy_id": sid, "strategy_name": name,
                            "reason": text["skip_low" if grp
                                           else "skip_none"]})
            continue
        worst = min(PRIORITIES.index(g["priority"].split(" ")[0])
                    for g in grp["gaps"])
        start = sorted(
            (q for g in grp["gaps"] for q in g["lowest_questions"]),
            key=lambda q: (q["score"], q["id"]))
        first = start[0] if start else None
        refs = sorted({n for q in start[:3]
                       for n in qindex[q["id"]]["basis"]})
        ranked.append({
            "strategy_id": sid,
            "strategy_name": name,
            "cumulative_priority": r3(grp["cum"]),
            "max_priority": f"{PRIORITIES[worst]} "
                            f"{PRIORITY_NAMES[locale][worst]}",
            "horizon": HORIZONS[locale][worst],
            "related_dimensions_count": len(grp["gaps"]),
            "related_dimensions": [
                {"id": g["dimension_id"], "name": g["dimension_name"],
                 "gap_size": g["gap_size"], "priority": g["priority"]}
                for g in grp["gaps"]
            ],
            "start_with": start[:3],
            "technologies": techs.get(sid, []),
            "first_action": text["first_action"].format(
                qid=first["id"],
                title=tr(qindex[first["id"]]["title"], locale),
                anchor=first["l3_anchor"]) if first else "",
            "expected_outcome": text["outcome"].format(
                dims=", ".join(g["dimension_id"] for g in grp["gaps"])),
            "references": refs,
        })
    ranked.sort(key=lambda s: (-s["cumulative_priority"],
                               s["max_priority"],
                               -s["related_dimensions_count"],
                               s["strategy_id"]))
    return {
        "metadata": {"computed_at": now_iso(),
                     "framework_version": fw["version"],
                     "based_on": "saida/gaps.json"},
        "ranked_strategies": [{"rank": i, **s}
                              for i, s in enumerate(ranked, start=1)],
        "skipped_strategies": skipped,
    }
