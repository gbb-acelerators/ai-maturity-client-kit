#!/usr/bin/env python3
"""Build payload from kit data and render the 5 PDF reports.

Strategy: use sample_payload.json as the BASE STRUCTURE (provides all the
nested fields the Jinja2 templates expect — scoring_rationale, h1_initiatives,
technology_resources_per_pillar, success_metrics_per_pillar, risks_per_pillar,
horizons narrative, three_horizons technologies, branding, etc.) and OVERWRITE
only the fields we have real client data for:
  - organization (from respostas.json)
  - assessment.id / assessment.completed_date
  - scores.overall.weighted_avg / level_label / gap
  - scores.pillars[].weighted_avg / level_label / gap
  - capabilities[].current_score / current_level_label / gap (matched by id)
  - gap_analysis[] (rebuilt from gaps.json, structure mirrors sample)
  - implementation_guide_inputs (from implementation-guide-inputs.json if exists)

Capabilities, names, weights, targets, evidence, and the scoring rationale
come from framework.json and the client files. Sample facts about the demo
organization (Acme) are reset, so a client PDF never states them. Generic
kit recommendations (horizons, technologies, risks, next steps) remain and
can be edited in saida/payload.json before re-rendering.

Usage:
    python3 build_payload_and_render.py
    python3 build_payload_and_render.py --kit /path/to/kit-cliente
    python3 build_payload_and_render.py --no-render   # only build payload, skip PDFs
"""
from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

# Local imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
import branding

DEFAULT_TARGET = 3.0
DEFAULT_LOCALE = "en"
SUPPORTED_LOCALES = ("en", "es", "pt-br")

LEVEL_LABELS = {
    "en": ("No answer", "L0 Initial", "L1 Developing", "L2 Defined",
           "L3 Managed", "L4 Optimizing"),
    "es": ("Sin respuesta", "L0 Inicial", "L1 En Desarrollo",
           "L2 Definido", "L3 Gestionado", "L4 Optimizando"),
    "pt-br": ("Sem resposta", "L0 — Inicial", "L1 — Em Desenvolvimento",
              "L2 — Definido", "L3 — Gerenciado", "L4 — Otimizando"),
}

DEFAULT_ACTIONS = {
    "en": {
        "h1": "Define a baseline and establish coverage metrics.",
        "h2": "Expand the pilot to >50% of teams; instrument OKRs.",
        "h3": "Reach universal coverage and continuous optimization.",
    },
    "es": {
        "h1": "Definir la línea base y establecer métricas de cobertura.",
        "h2": "Expandir el piloto a >50% de los equipos; instrumentar OKRs.",
        "h3": "Alcanzar cobertura universal y optimización continua.",
    },
    "pt-br": {
        "h1": "Definir baseline e estabelecer métricas de cobertura.",
        "h2": "Expandir piloto para >50% das equipes; instrumentar OKRs.",
        "h3": "Atingir cobertura universal e otimização contínua.",
    },
}


RATIONALE = {
    "en": {
        "score": "Weighted mean of {answered} of {total} questions: "
                 "{score} ({label}).",
        "evidence": "Evidence was provided for {n} question(s), listed above.",
        "no_evidence": "No evidence was provided, so treat this score as "
                       "self-reported.",
        "none": "No questions in this capability were answered.",
    },
    "es": {
        "score": "Media ponderada de {answered} de {total} preguntas: "
                 "{score} ({label}).",
        "evidence": "Se aportó evidencia en {n} pregunta(s), listada arriba.",
        "no_evidence": "No se aportó evidencia; trate este score como "
                       "autodeclarado.",
        "none": "No se respondió ninguna pregunta de esta capacidad.",
    },
    "pt-br": {
        "score": "Média ponderada de {answered} de {total} perguntas: "
                 "{score} ({label}).",
        "evidence": "Houve evidência em {n} pergunta(s), listada acima.",
        "no_evidence": "Nenhuma evidência foi informada; trate este score "
                       "como autodeclarado.",
        "none": "Nenhuma pergunta desta capability foi respondida.",
    },
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def label_from_score(
    score: float | None, locale: str = DEFAULT_LOCALE
) -> str:
    labels = LEVEL_LABELS.get(locale, LEVEL_LABELS[DEFAULT_LOCALE])
    if score is None:
        return labels[0]
    for idx, upper in enumerate((0.5, 1.5, 2.5, 3.5), start=1):
        if score < upper:
            return labels[idx]
    return labels[5]


def priority_from_ps(ps: float) -> str:
    if ps >= 2.4: return "P0 Critical"
    if ps >= 1.6: return "P1 High"
    if ps >= 0.9: return "P2 Medium"
    return "P3 Low"


def build_payload(kit: Path) -> dict:
    """Merge sample_payload.json (structure) with client data (overrides)."""
    sample = load_json(kit / "relatorios/sample_payload.json")
    payload = copy.deepcopy(sample)
    _merge_branding(payload)

    scores_path = kit / "saida/scores.json"
    if not scores_path.exists():
        print("⚠️ saida/scores.json not found: rendering PDFs with "
              "sample data (Acme).")
        print("   To use your own data, run /pipeline-completo first.\n")
        _attach_cross_survey(payload, kit)
        return payload

    respostas, scores, gaps = _load_client_pipeline_data(kit)
    meta = respostas.get("metadata", {})
    framework = load_json(kit / "framework.json")

    _apply_locale(payload, meta)
    na = _not_specified(kit, _locale(payload))
    _reset_sample_content(payload, meta, na)
    payload["capabilities"] = _client_capabilities(
        framework, respostas, _locale(payload), na)
    _apply_organization(payload, meta)
    _apply_assessment(payload, scores, meta)
    _apply_capability_scores(payload, scores, respostas)
    _apply_overall_scores(payload, scores)
    _apply_pillar_scores(payload, scores, framework)
    _apply_pe_readiness(payload, scores)
    _apply_gap_analysis(payload, gaps, kit)
    _merge_implementation_guide_inputs(
        payload, kit / "implementation-guide-inputs.json")
    _attach_cross_survey(payload, kit)
    _strip_private_keys(payload)

    return payload

def _merge_branding(payload: dict) -> None:
    """Merge paulasilva-ms branding while preserving sample-only fields."""
    payload.setdefault("branding", {}).update({
        "primary_color": branding.MS_BLUE,
        "author": branding.AUTHOR,
        "role": branding.ROLE,
        "author_name": branding.META_BAR,
        "contact": branding.CONTACT,
        "tagline": branding.TAGLINE,
        "design_system": branding.DESIGN_SYSTEM,
        "palette_red": branding.MS_RED,
        "palette_green": branding.MS_GREEN,
        "palette_yellow": branding.MS_YELLOW,
        "palette_blue": branding.MS_BLUE,
    })


def _load_client_pipeline_data(kit: Path) -> tuple[dict, dict, dict]:
    respostas_path = kit / "respostas.json"
    scores_path = kit / "saida/scores.json"
    gaps_path = kit / "saida/gaps.json"
    return (
        load_json(respostas_path) if respostas_path.exists() else {},
        load_json(scores_path),
        load_json(gaps_path) if gaps_path.exists() else {"gaps": [], "summary": {}},
    )


def _apply_locale(payload: dict, meta: dict) -> None:
    locale = str(meta.get("language") or DEFAULT_LOCALE)
    locale = locale.lower().replace("_", "-")
    if locale == "pt":
        locale = "pt-br"
    if locale not in SUPPORTED_LOCALES:
        locale = DEFAULT_LOCALE
    payload["locale"] = locale


def _locale(payload: dict) -> str:
    return payload.get("locale", DEFAULT_LOCALE)


def _capability_names(kit: Path) -> dict[str, dict[str, str]]:
    path = kit / "framework.json"
    if not path.exists():
        return {}
    names = {}
    for pillar in load_json(path).get("pillars", []):
        for cap in pillar.get("capabilities", []):
            names[cap["id"]] = {
                "en": cap.get("name", ""),
                "pt-br": cap.get("name_pt_br", ""),
            }
    return names


def _apply_organization(payload: dict, meta: dict) -> None:
    org = payload["organization"]
    org["name"] = meta.get("organization") or org["name"]
    if meta.get("respondent_role"):
        org["primary_contact_role"] = meta["respondent_role"]


def _not_specified(kit: Path, locale: str) -> str:
    path = kit / "relatorios" / "i18n" / f"{locale}.json"
    try:
        return load_json(path).get("label.not_specified", "—")
    except (OSError, ValueError):
        return "—"


def _reset_sample_content(payload: dict, meta: dict, na: str) -> None:
    """Drop sample (Acme) facts so client PDFs only show client data.

    Generic recommendations (horizons, technologies, risks, next steps)
    stay; any field that states a fact about the organization is reset.
    """
    org = payload["organization"]
    for key in org:
        if key != "name":
            org[key] = meta.get(key) or na
    org["name"] = meta.get("organization") or na
    payload["assessment"]["name"] = (
        meta.get("assessment_name") or "AI Maturity Assessment")
    sources = meta.get("evidence_sources")
    payload["key_evidence_sources"] = (
        sources if isinstance(sources, dict) else {})
    for pillar_metrics in payload.get(
            "success_metrics_per_pillar", {}).values():
        for metrics in pillar_metrics.values():
            for metric in metrics:
                metric["current"] = na
    for pillar in payload["scores"]["pillars"]:
        pillar["current_state_metrics"] = []
    pe = payload["scores"]["pe_readiness"]
    pe["three_horizons_verdict"] = None
    pe["agentic_platform_engineering"] = {
        "destination_label": "Agentic Platform Engineering",
        "recommended_path": None,
        "recommended_path_label": None,
        "recommended_idp": None,
        "rationale": None,
    }
    payload["gap_analysis"] = []
    payload["implementation_guide_inputs"] = {}


def _capability_code(cap_id: str) -> str:
    pillar, cap = cap_id.split("-")
    return f"{pillar[1:]}.{cap[1:]}"


def _client_capabilities(
    framework: dict, respostas: dict, locale: str, na: str
) -> list[dict]:
    """Build capability entries from framework.json (not the sample)."""
    responses = respostas.get("responses") or {}
    tmpl = RATIONALE.get(locale, RATIONALE[DEFAULT_LOCALE])
    caps = []
    for pillar in framework.get("pillars", []):
        for cap in pillar.get("capabilities", []):
            questions = cap.get("questions", [])
            evidence = []
            for q in questions:
                entry = responses.get(q["id"]) or {}
                text = str(entry.get("evidence") or "").strip()
                if text:
                    evidence.append(f"{q['id']}: {text[:280]}")
            audience = sorted({
                a for q in questions for a in q.get("audience", [])
            }) or ["all"]
            kpis = []
            for q in questions:
                kpi = q.get("kpi")
                if kpi and kpi not in kpis:
                    kpis.append(kpi)
            is_pe = any(q.get("pe") for q in questions)
            name = cap.get("name_pt_br") if locale == "pt-br" else None
            caps.append({
                "id": cap["id"],
                "code": _capability_code(cap["id"]),
                "name": name or cap.get("name", cap["id"]),
                "pillar_id": pillar["id"],
                "is_pe_indicator": is_pe,
                "weight": float(cap.get("weight", 1.0)),
                "pe_weight": 1.0 if is_pe else 0.0,
                "audience": audience,
                "evidence_collected": evidence[:6],
                "h1_state_evidence": evidence[:3],
                "evidence_count": len(evidence),
                "question_count": len(questions),
                "scoring_rationale": "",
                "h1_initiatives": [],
                "h2_key_enabler": None,
                "h3_target_label": None,
                "h1_success_metrics": [
                    {"metric": k, "current": na, "h1_target": na}
                    for k in kpis[:3]
                ],
                "_rationale": tmpl,
            })
    return caps


def _apply_assessment(payload: dict, scores: dict, meta: dict) -> None:
    assess = payload["assessment"]
    assess["id"] = scores.get("metadata", {}).get("respondent", assess.get("id", "—"))
    assess["completed_date"] = meta.get("assessment_date", assess["completed_date"])
    assess["generated_date"] = datetime.date.today().isoformat()
    assess["framework_version"] = scores.get("metadata", {}).get(
        "framework_version", assess["framework_version"]
    )


def _weighted_target(caps: list[dict]) -> float:
    answered = [c for c in caps if c.get("_answered")]
    total = sum(c["weight"] for c in answered)
    if not total:
        return DEFAULT_TARGET
    return sum(c["target_score"] * c["weight"] for c in answered) / total


def _apply_overall_scores(payload: dict, scores: dict) -> None:
    overall_score = scores["overall"]["score"]
    overall = payload["scores"]["overall"]
    target = _weighted_target(payload["capabilities"])
    overall["target"] = round(target, 2)
    if overall_score is None:
        overall["weighted_avg"] = 0.0
        overall["level_label"] = label_from_score(None, _locale(payload))
        overall["gap"] = 0
        return
    overall["weighted_avg"] = round(overall_score, 2)
    overall["level_label"] = label_from_score(
        overall_score, _locale(payload))
    overall["gap"] = max(0, round(target - overall_score, 2))


def _apply_pillar_scores(
    payload: dict, scores: dict, framework: dict
) -> None:
    locale = _locale(payload)
    names = {
        p["id"]: (p.get("name_pt_br") if locale == "pt-br" else None)
        or p.get("name", p["id"])
        for p in framework.get("pillars", [])
    }
    sample_pillars_by_id = {p["id"]: p for p in payload["scores"]["pillars"]}
    for p_client in scores.get("pillars", []):
        pid = p_client["id"]
        sample_p = sample_pillars_by_id.get(pid)
        if not sample_p:
            continue
        caps = [c for c in payload["capabilities"] if c["pillar_id"] == pid]
        scored = [c for c in caps if c.get("_answered")]
        weights = sum(c["weight"] for c in scored)
        wsum = sum(c["_score"] * c["weight"] for c in scored)
        target = _weighted_target(caps)
        sample_p["name"] = names.get(pid, sample_p.get("name"))
        sample_p["weighted_avg"] = round(p_client["score"], 2)
        sample_p["level_label"] = label_from_score(p_client["score"], locale)
        sample_p["target"] = round(target, 2)
        sample_p["gap"] = max(0, round(target - p_client["score"], 2))
        sample_p["capabilities_count"] = len(caps)
        sample_p["weights_sum"] = weights
        sample_p["weighted_sum_calc"] = round(wsum, 2)


def _pe_level(score: float) -> tuple[str, str]:
    # Mirrors the PE rubric table in score_justification.html.j2.
    if score < 1.0:
        return "NOT READY", "build_foundation_first"
    if score < 2.0:
        return "LOW", "build_foundation_first"
    if score < 3.0:
        return "MEDIUM", "open_horizons"
    return "HIGH", "either"


def _apply_pe_readiness(payload: dict, scores: dict) -> None:
    pe_score = scores["overall"].get("pe_score")
    pe = payload["scores"]["pe_readiness"]
    if pe_score is None:
        pe["weighted_score"] = None
        pe["level"] = None
        return
    level, path = _pe_level(pe_score)
    pe["weighted_score"] = round(pe_score, 2)
    pe["level"] = level
    pe["agentic_platform_engineering"]["recommended_path"] = path


def _apply_capability_scores(
    payload: dict, scores: dict, respostas: dict
) -> None:
    target_overrides = respostas.get("target_overrides", {})
    by_id = {c["id"]: c for c in payload["capabilities"]}
    for c_client in scores.get("capabilities", []):
        cap = by_id.get(c_client["id"])
        if cap:
            _apply_single_capability_score(
                cap, c_client, target_overrides, _locale(payload))
    for cap in payload["capabilities"]:
        tmpl = cap.pop("_rationale", None)
        if tmpl and "current_score" in cap:
            cap["scoring_rationale"] = _rationale(tmpl, cap)


def _rationale(tmpl: dict, cap: dict) -> str:
    if not cap.get("_answered"):
        return tmpl["none"]
    text = tmpl["score"].format(
        answered=cap["answered"],
        total=cap["question_count"],
        score=f"{cap['_score']:.2f}",
        label=cap["current_level_label"],
    )
    if cap["evidence_count"]:
        return text + " " + tmpl["evidence"].format(n=cap["evidence_count"])
    return text + " " + tmpl["no_evidence"]


GAP_PRIORITY = {"P0": "CRITICAL", "P1": "HIGH", "P2": "MEDIUM", "P3": "LOW"}


def _apply_single_capability_score(
    sample_c: dict,
    c_client: dict,
    target_overrides: dict,
    locale: str = DEFAULT_LOCALE,
) -> None:
    cid = c_client["id"]
    score = c_client.get("score")
    target = float(target_overrides.get(cid, DEFAULT_TARGET))
    sample_c["_answered"] = score is not None
    sample_c["_score"] = score if score is not None else 0.0
    sample_c["answered"] = c_client.get("answered", 0)
    sample_c["current_score"] = round(score, 2) if score is not None else 0.0
    sample_c["current_level_label"] = label_from_score(score, locale)
    sample_c["target_score"] = round(target, 2)
    sample_c["target_level_label"] = label_from_score(target, locale)
    base = score if score is not None else 0.0
    sample_c["h1_target_score"] = round(min(target, base + 1.0), 1)
    sample_c["h2_target_score"] = round(target, 1)
    sample_c["h3_target_score"] = 4.0
    if score is None:
        sample_c["gap"] = 0
        sample_c["gap_priority"] = "LOW"
        return
    sample_c["gap"] = max(0, round(target - score, 2))
    ps = sample_c["weight"] * max(0.0, target - score)
    code = priority_from_ps(ps).split(" ")[0]
    sample_c["gap_priority"] = GAP_PRIORITY[code]


def _apply_gap_analysis(payload: dict, gaps: dict, kit: Path) -> None:
    names = _capability_names(kit)
    new_gap_analysis = [
        _gap_payload_entry(payload, gap, names)
        for gap in gaps.get("gaps", [])
    ]
    payload["gap_analysis"] = new_gap_analysis


def _gap_payload_entry(
    payload: dict, gap: dict, names: dict[str, dict[str, str]]
) -> dict:
    locale = _locale(payload)
    existing = next(
        (item for item in payload["gap_analysis"]
         if item.get("capability_code") == gap["capability_id"]),
        None,
    )
    recommended_actions = (
        existing.get("recommended_actions", {})
        if existing
        else dict(DEFAULT_ACTIONS.get(locale, DEFAULT_ACTIONS[DEFAULT_LOCALE]))
    )
    pt_name = gap["capability_name_pt_br"]
    # framework.json has no Spanish names; ES keeps the canonical PT-BR name
    name_key = "en" if locale == "en" else "pt-br"
    cap_name = names.get(gap["capability_id"], {}).get(name_key) or pt_name
    return {
        "pillar_id": gap["pillar_id"],
        "capability_code": gap["capability_id"],
        "capability_name": cap_name,
        "current": round(gap["current_score"], 2),
        "target": round(gap["target_level"], 2),
        "gap": round(gap["gap_size"], 2),
        "priority": gap["priority"].split(" ")[0],
        "recommended_actions": recommended_actions,
    }


_ITEM_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+(.+?)\s*$")
_SEP_RE = re.compile(r"^:?-{2,}:?$")
_PLACEHOLDER_MARKERS = ("preencher", "fill in", "completar", "rellenar")


def _is_placeholder(text: str) -> bool:
    text = text.strip().lower()
    return text.startswith("(") and any(
        m in text for m in _PLACEHOLDER_MARKERS)


def _md_items(text: str) -> list[str]:
    return [m.group(1) for line in text.splitlines()
            if (m := _ITEM_RE.match(line)) and not line.lstrip()
            .startswith("|")]


def _md_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(_SEP_RE.match(c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:]  # first row is the header


def _split_pair(text: str) -> tuple[str, str]:
    for sep in (" — ", " – ", ": ", " - "):
        if sep in text:
            left, right = text.split(sep, 1)
            return left.strip(" *"), right.strip()
    return text.strip(" *"), ""


def _cells(row: list[str], keys: tuple[str, ...]) -> dict:
    padded = row + [""] * (len(keys) - len(row))
    return dict(zip(keys, padded))


def _wizard_value(key: str, value):
    """Convert wizard Markdown into the structures the templates render."""
    if not isinstance(value, str):
        return value or None
    text = value.strip()
    if not text or _is_placeholder(text):
        return None
    rows = _md_rows(text)
    items = [i for i in _md_items(text) if not _is_placeholder(i)]
    if key == "executive_steering_committee":
        if rows:
            return [_cells(r, ("name", "role")) for r in rows]
        members = [dict(zip(("name", "role"), _split_pair(i)))
                   for i in items]
        return members or None
    if key == "tpo":
        people = [_split_pair(i)[0] for i in items]
        if people:
            return {"program_manager": people[0], "members": people[1:]}
        return {"program_manager": text.splitlines()[0], "members": []}
    table_keys = {
        "raci_matrix": ("activity", "r", "a", "c", "i"),
        "communication_plan": ("audience", "channel", "frequency", "owner"),
        "training_plan": ("audience", "format", "cadence"),
    }
    if key in table_keys:
        keys = table_keys[key]
        if rows:
            return [_cells(r, keys) for r in rows]
        return [_cells([i], keys) for i in items] or None
    if key.startswith("quick_wins"):
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        return items or [ln for ln in lines if not _is_placeholder(ln)]
    return text


def _merge_implementation_guide_inputs(payload: dict, ig_path: Path) -> None:
    if not ig_path.exists():
        return
    ig = load_json(ig_path)
    wizard_inputs = ig.get("implementation_guide_inputs", {})
    if not wizard_inputs:
        return

    current_ig = payload.get("implementation_guide_inputs", {})
    for key, value in wizard_inputs.items():
        converted = _wizard_value(key, value)
        if converted:
            current_ig[key] = converted
        if isinstance(value, str) and value.strip():
            current_ig[f"{key}_raw_markdown"] = value
    payload["implementation_guide_inputs"] = current_ig
    print(f"✓ Merged implementation-guide-inputs.json "
          f"({ig.get('metadata', {}).get('completion_pct', 0)}% complete)")


def _strip_private_keys(payload: dict) -> None:
    for cap in payload.get("capabilities", []):
        for key in [k for k in cap if k.startswith("_")]:
            del cap[key]


def _attach_cross_survey(payload: dict, kit: Path) -> None:
    """Detect optional survey artifacts and attach them to ``payload``."""
    cross = collect_cross_survey_data(kit)
    if not cross:
        return
    payload["cross_survey_data"] = cross
    bits = []
    if "developer_survey_maturity" in cross:
        n = cross["developer_survey_maturity"].get("respondents") or "?"
        bits.append(f"survey-devs maturity (n={n})")
    if "developer_survey_insights" in cross:
        bits.append("survey-devs insights")
    if "learning_plan" in cross:
        bits.append("learning plan")
    print(f"✓ cross_survey_data attached: {', '.join(bits)}")


def collect_cross_survey_data(kit: Path) -> dict | None:
    """Detect optional outputs from the two complementary surveys and
    expose them as ``payload.cross_survey_data`` for downstream consumption.

    The score justification template renders this field when available, and
    surfacing it in ``payload.json`` keeps the data inspectable for audits.
    """
    out_dir = kit / "saida"
    if not out_dir.exists():
        return None

    cross: dict = {"available": False}

    maturity = _collect_developer_maturity(kit, out_dir)
    if maturity:
        cross["developer_survey_maturity"] = maturity
        cross["available"] = True

    insights = _latest_artifact(kit, out_dir, "insights-developer-survey-*.md")
    if insights:
        cross["developer_survey_insights"] = insights
        cross["available"] = True

    learning_plan = _latest_artifact(kit, out_dir, "plano-capacitacao-*.md")
    if learning_plan:
        cross["learning_plan"] = learning_plan
        cross["available"] = True

    return cross if cross["available"] else None


def _latest_artifact(kit: Path, out_dir: Path, pattern: str) -> dict | None:
    candidates = sorted(out_dir.glob(pattern), reverse=True)
    if not candidates:
        return None
    return {"source_file": str(candidates[0].relative_to(kit))}


def _collect_developer_maturity(kit: Path, out_dir: Path) -> dict | None:
    candidates = sorted(out_dir.glob("maturidade-developer-survey-*.json"), reverse=True)
    if not candidates:
        return None
    try:
        mat = load_json(candidates[0])
    except (OSError, ValueError):
        return None

    meta = mat.get("metadata", {}) or {}
    team_overall = mat.get("team_overall", {}) or {}
    return {
        "source_file": str(candidates[0].relative_to(kit)),
        "respondents": meta.get("n_respondents") or meta.get("total_respondents"),
        "overall_score": team_overall.get("score"),
        "overall_label": team_overall.get("label"),
        "dimensions": _developer_maturity_dimensions(mat.get("dimensions") or {}),
    }


def _developer_maturity_dimensions(raw_dims: dict) -> list[dict]:
    dims = []
    for did, entry in raw_dims.items():
        if not isinstance(entry, dict):
            continue
        score = entry.get("team_score", entry.get("score"))
        if score is None:
            continue
        score_float = float(score)
        dims.append({
            "dimension": did,
            "name": entry.get("name"),
            "score": round(score_float, 2),
            "label": entry.get("label") or label_from_score(score_float),
            "respondents": entry.get("respondents_with_score"),
        })
    return dims


def render_pdfs(payload_path: Path, out_dir: Path, kit: Path) -> int:
    """Invoke render_reports.py to produce the 5 PDFs."""
    script = kit / "relatorios/scripts/render_reports.py"
    cmd = [sys.executable, str(script), "--payload", str(payload_path), "--out", str(out_dir)]
    print(f"\n→ Rendering 5 PDFs with {payload_path.name}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("STDERR:", result.stderr, file=sys.stderr)
    return result.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", default=str(Path(__file__).resolve().parent.parent.parent),
                    help="Path to kit-cliente/")
    ap.add_argument("--out", default=None, help="Output dir (default: <kit>/saida/)")
    ap.add_argument("--no-render", action="store_true", help="Only build payload, skip PDF rendering")
    args = ap.parse_args()

    kit = Path(args.kit).resolve()
    out_dir = Path(args.out).resolve() if args.out else kit / "saida"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Kit:     {kit}")
    print(f"Out:     {out_dir}")
    print()

    respostas_path = kit / "respostas.json"
    if respostas_path.exists():
        meta = json.loads(respostas_path.read_text(encoding="utf-8")).get("metadata", {})
        if str(meta.get("framework_version") or "1").split(".")[0] not in ("0", "1"):
            import build_report_v2
            argv = ["--kit", str(kit), "--out", str(out_dir)]
            if args.no_render:
                argv.append("--no-render")
            sys.argv = [sys.argv[0], *argv]
            return build_report_v2.main()

    # Build payload (merge sample + client data)
    payload = build_payload(kit)
    payload_path = out_dir / "payload.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Payload merged: {payload_path} ({payload_path.stat().st_size:,} bytes)")
    print(f"  Locale:  {payload.get('locale')}")
    print(f"  Org:     {payload['organization']['name']}")
    print(f"  Overall: {payload['scores']['overall']['weighted_avg']} ({payload['scores']['overall']['level_label']})")

    if args.no_render:
        return 0

    return render_pdfs(payload_path, out_dir, kit)


if __name__ == "__main__":
    sys.exit(main())
