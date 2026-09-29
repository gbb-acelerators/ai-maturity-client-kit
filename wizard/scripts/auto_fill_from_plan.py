#!/usr/bin/env python3
"""Wizard Mode D: auto-fill implementation-guide-inputs.json from the plan.

Reads: output/training-plan-<DATE>.md (output of /training-plan),
       in English or Portuguese
Extracts: Champions, training, calendar, ADKAR knowledge, quick wins
Writes: implementation-guide-inputs.json (kit root); up to 7 of 11 fields
        are filled, the others are marked "(fill in ...)" for the report

Usage:
    python3 auto_fill_from_plan.py
    python3 auto_fill_from_plan.py --plan X --out Y --lang pt-br
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "reports" / "scripts"))
import branding  # noqa: E402

SUPPORTED_LANGS = ("en", "pt-br", "es")

# Heading patterns accept the English, Portuguese and Spanish plan.
# An optional emoji may precede the heading text.
EMOJI = r"(?:\S+ )?"
H_SUMMARY = r"1 · (?:Sumário Executivo|Executive Summary|Resumen ejecutivo)"
H_COHORTS = r"3 · (?:Cohorts sugeridos|Suggested cohorts)"
H_CHAMPIONS = r"4 · Champions Network"
H_CALENDAR = r"5 · (?:Calendário sugerido|Calendario sugerido|Suggested calendar)"
H_FORMAT = r"6 · (?:Formato e cadência|Formato y cadencia|Preferred format)"
H_BARRIERS = r"7 · (?:Barreiras|Barreras|Barriers)"
H_SCHEDULE = rf"11 · {EMOJI}(?:Cronograma|30-day schedule)"
H_ACTIVE = r"### 🥇 (?:Ativos|Activos|Active)"
H_FORMATS_SUB = r"### (?:Formatos|Formats)"
# "1. **topic** — N devs" (PT) or "1. **topic**: N devs" (EN)
TOPIC_LINE = r"^\d+\.\s+\*\*(.+?)\*\*(?: —|:) (\d+) devs"

STRINGS = {
    "en": {
        "committee_intro": "Executive Steering Committee (active "
                           "Champions identified by the Learning "
                           "Survey):",
        "person": "- {name}: Champion ({email})",
        "comm_intro": "Communication Plan derived from the suggested "
                      "calendar:\n\n",
        "comm_missing": "(see Part 5 of the training plan)",
        "training_intro": "Training Plan (cohorts per dimension derived "
                          "from the Learning Survey):\n\n",
        "training_missing": "(see Part 3 of the training plan)",
        "adkar_head": (
            "ADKAR Change Plan derived from the Learning Survey:\n\n"
            "**Awareness:** Share the consolidated training plan in an "
            "all-hands; each dev receives a personalized plan by "
            "email.\n\n"
            "**Desire:** Make it visible that workshops have "
            "pre-validated attendees (not a generic opt-in).\n\n"
            "**Knowledge:** Top 5 workshops (from the Learning "
            "Survey):\n"
        ),
        "adkar_item": "{i}. {topic} ({count} attendees)\n",
        "adkar_tail": (
            "\n**Ability:** Biweekly office hours (no fixed agenda; devs "
            "bring practical questions).\n\n"
            "**Reinforcement:** Monthly adoption metrics published; "
            "recognition for Champions; quarterly plan review with a "
            "new Learning Survey.\n"
        ),
        "no_committee": "(fill in manually: no active Champions "
                        "identified by the Learning Survey)",
        "no_tpo": "(fill in manually: the Learning Survey does not "
                  "cover the TPO. List the Program Manager, office, and "
                  "decision authority)",
        "no_raci": "(fill in manually: the Learning Survey does not "
                   "cover RACI. Use the template in "
                   "wizard/implementation-guide-inputs.template.json)",
        "comm_head": "| Audience | Channel | Frequency | Owner |",
        "train_head": "| Audience | Format | Cadence |",
        "cohort_row": "{name}: {count} devs",
        "no_owners": "(fill in manually: one owner for each dimension "
                     "below target, one per line as D#: name, role)",
        "no_risks": "(fill in manually: the client's own risks as a "
                    "table Risk | Impact | Mitigation | Owner)",
        "no_qw_1_4": "(fill in: not enough data for weeks 1-4 of the "
                     "calendar)",
        "no_qw_5_8": "(fill in: not enough data for weeks 5-8)",
        "no_qw_9_12": "(fill in: not enough data for weeks 9-12)",
        "c_missing": "❌ Training plan not found in output/.",
        "c_run": "   Run /training-plan first (after "
                 "/import-survey-learning).",
        "c_reading": "📖 Reading: {path}",
        "c_done": "\n✅ Mode D auto-fill → {path}",
        "c_filled": "\n📊 Automatically filled:",
        "c_fields": [
            "   ✓ executive_steering_committee  (active Champions)",
            "   ✓ communication_plan            (Calendar)",
            "   ✓ training_plan                 (Cohorts per dimension)",
            "   ✓ adkar_notes                   (Knowledge = Top 5 "
            "workshops)",
            "   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Schedule)",
        ],
        "c_manual": "\n⚠ You must fill in MANUALLY (not covered by the "
                    "Learning Survey):",
        "c_manual_fields": [
            "   • tpo (program office)",
            "   • raci_matrix",
            "   • dimension_owners",
            "   • risk_register",
        ],
        "c_next": "\n💡 Next: /generate-report  → 5 PDFs with a "
                  "personalized Part 4",
    },
    "pt-br": {
        "committee_intro": "Comitê Executivo Diretivo (Champions ativos "
                           "identificados pelo Learning Survey):",
        "person": "- {name}: Champion ({email})",
        "comm_intro": "Plano de Comunicação derivado do calendário "
                      "sugerido:\n\n",
        "comm_missing": "(ver Parte 5 do plano de capacitação)",
        "training_intro": "Plano de Treinamento (cohorts por dimensão "
                          "derivados do Learning Survey):\n\n",
        "training_missing": "(ver Parte 3 do plano de capacitação)",
        "adkar_head": (
            "Plano de Mudança ADKAR derivado do Learning Survey:\n\n"
            "**Awareness:** Comunicar plano de capacitação consolidado "
            "em all-hands; cada dev recebe seu plano personalizado por "
            "email.\n\n"
            "**Desire:** Tornar visível que workshops têm inscritos "
            "pré-validados (não opt-in genérico).\n\n"
            "**Knowledge:** Workshops top 5 (do Learning Survey):\n"
        ),
        "adkar_item": "{i}. {topic} ({count} inscritos)\n",
        "adkar_tail": (
            "\n**Ability:** Office hours quinzenal (sem agenda fixa, "
            "devs trazem dúvidas práticas).\n\n"
            "**Reinforcement:** Métricas de adoção mensais publicadas; "
            "reconhecimento dos Champions; revisão trimestral do plano "
            "com novo Learning Survey.\n"
        ),
        "no_committee": "(preencher manualmente: sem Champions ativos "
                        "identificados pelo Learning Survey)",
        "no_tpo": "(preencher manualmente: o Learning Survey não cobre o "
                  "escritório do programa. Liste o gerente do programa, "
                  "os membros e a autoridade de decisão)",
        "no_raci": "(preencher manualmente: o Learning Survey não cobre a "
                   "RACI. Use o modelo em "
                   "wizard/implementation-guide-inputs.template.json)",
        "comm_head": "| Público | Canal | Frequência | Responsável |",
        "train_head": "| Público | Formato | Cadência |",
        "cohort_row": "{name}: {count} devs",
        "no_owners": "(preencher manualmente: um responsável para cada "
                     "dimensão abaixo da meta, um por linha como D#: nome, "
                     "papel)",
        "no_risks": "(preencher manualmente: riscos do próprio cliente "
                    "em tabela Risco | Impacto | Mitigação | Responsável)",
        "no_qw_1_4": "(preencher: sem dados suficientes nas semanas 1-4 "
                     "do calendário)",
        "no_qw_5_8": "(preencher: sem dados suficientes nas semanas "
                     "5-8)",
        "no_qw_9_12": "(preencher: sem dados suficientes nas semanas "
                      "9-12)",
        "c_missing": "❌ Plano de capacitação não encontrado em output/.",
        "c_run": "   Rode /training-plan primeiro (após "
                 "/import-survey-learning).",
        "c_reading": "📖 Lendo: {path}",
        "c_done": "\n✅ Mode D auto-fill → {path}",
        "c_filled": "\n📊 Preenchimento automático:",
        "c_fields": [
            "   ✓ executive_steering_committee  (Champions ativos)",
            "   ✓ communication_plan            (Calendário)",
            "   ✓ training_plan                 (Cohorts por dimensão)",
            "   ✓ adkar_notes                   (Knowledge = Top 5 "
            "workshops)",
            "   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Cronograma)",
        ],
        "c_manual": "\n⚠ Você precisa preencher MANUALMENTE (Learning "
                    "Survey não cobre):",
        "c_manual_fields": [
            "   • tpo (escritório do programa)",
            "   • raci_matrix",
            "   • dimension_owners",
            "   • risk_register",
        ],
        "c_next": "\n💡 Próximo: /generate-report  → 5 PDFs com Parte 4 "
                  "personalizada",
    },
    "es": {
        "committee_intro": "Comité directivo (Champions activos "
                           "identificados por el Learning Survey):",
        "person": "- {name}: Champion ({email})",
        "comm_intro": "Plan de comunicación derivado del calendario "
                      "sugerido:\n\n",
        "comm_missing": "(ver la parte 5 del plan de capacitación)",
        "training_intro": "Plan de capacitación (grupos por dimensión "
                          "derivados del Learning Survey):\n\n",
        "training_missing": "(ver la parte 3 del plan de capacitación)",
        "adkar_head": (
            "Plan de cambio ADKAR derivado del Learning Survey:\n\n"
            "**Awareness:** Comunicar el plan de capacitación consolidado "
            "en un all-hands; cada dev recibe su plan personalizado por "
            "correo.\n\n"
            "**Desire:** Hacer visible que los talleres tienen inscritos "
            "prevalidados (no un opt-in genérico).\n\n"
            "**Knowledge:** Los 5 talleres principales (del Learning "
            "Survey):\n"
        ),
        "adkar_item": "{i}. {topic} ({count} inscritos)\n",
        "adkar_tail": (
            "\n**Ability:** Office hours quincenales (sin agenda fija; "
            "los devs traen dudas prácticas).\n\n"
            "**Reinforcement:** Métricas de adopción mensuales publicadas; "
            "reconocimiento a los Champions; revisión trimestral del plan "
            "con un nuevo Learning Survey.\n"
        ),
        "no_committee": "(completar manualmente: el Learning Survey no "
                        "identificó Champions activos)",
        "no_tpo": "(completar manualmente: el Learning Survey no cubre la "
                  "oficina del programa. Lista al gerente del programa, "
                  "los miembros y la autoridad de decisión)",
        "no_raci": "(completar manualmente: el Learning Survey no cubre "
                   "la RACI. Usa la plantilla en "
                   "wizard/implementation-guide-inputs.template.json)",
        "comm_head": "| Audiencia | Canal | Frecuencia | Responsable |",
        "train_head": "| Audiencia | Formato | Cadencia |",
        "cohort_row": "{name}: {count} devs",
        "no_owners": "(completar manualmente: una persona responsable por "
                     "cada dimensión bajo el objetivo, una por línea como "
                     "D#: nombre, rol)",
        "no_risks": "(completar manualmente: riesgos del propio cliente "
                    "en una tabla Riesgo | Impacto | Mitigación | "
                    "Responsable)",
        "no_qw_1_4": "(completar: no hay datos suficientes para las "
                     "semanas 1-4 del calendario)",
        "no_qw_5_8": "(completar: no hay datos suficientes para las "
                     "semanas 5-8)",
        "no_qw_9_12": "(completar: no hay datos suficientes para las "
                      "semanas 9-12)",
        "c_missing": "❌ No se encontró el plan de capacitación en output/.",
        "c_run": "   Ejecuta primero /training-plan (después de "
                 "/import-survey-learning).",
        "c_reading": "📖 Leyendo: {path}",
        "c_done": "\n✅ Mode D auto-fill → {path}",
        "c_filled": "\n📊 Completado automáticamente:",
        "c_fields": [
            "   ✓ executive_steering_committee  (Champions activos)",
            "   ✓ communication_plan            (Calendario)",
            "   ✓ training_plan                 (Grupos por dimensión)",
            "   ✓ adkar_notes                   (Knowledge = 5 talleres "
            "principales)",
            "   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Cronograma)",
        ],
        "c_manual": "\n⚠ Debes completar MANUALMENTE (el Learning Survey "
                    "no lo cubre):",
        "c_manual_fields": [
            "   • tpo (oficina del programa)",
            "   • raci_matrix",
            "   • dimension_owners",
            "   • risk_register",
        ],
        "c_next": "\n💡 Siguiente: /generate-report  → 5 PDFs con la guía "
                  "de implementación personalizada",
    },
}


def find_latest_plan(out_dir: Path) -> Path | None:
    """Find the most recent training-plan-*.md in output/."""
    candidates = sorted(out_dir.glob("training-plan-*.md"),
                        reverse=True)
    return candidates[0] if candidates else None


def extract_section(plan_md: str, section_header_pattern: str) -> str:
    """Extract a section body by header regex (until next ## or end)."""
    pat = re.compile(
        rf"## {section_header_pattern}.*?\n(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    m = pat.search(plan_md)
    return m.group(1).strip() if m else ""


def extract_active_people(plan_md: str) -> list[tuple[str, str]]:
    """(name, email) rows from the Active Champions table (section 4)."""
    section = extract_section(plan_md, H_CHAMPIONS)
    active_block = re.search(
        rf"{H_ACTIVE}.*?\n(.*?)(?=\n### |\Z)", section, re.DOTALL
    )
    if not active_block:
        return []
    rows = re.findall(
        r"^\|\s*([^|]+?)\s*\|\s*<?([^|@<>\s]+@[^|\s<>]+)>?\s*\|",
        active_block.group(1),
        re.MULTILINE,
    )
    return [
        (name.strip(), email.strip()) for name, email in rows
        if name.strip().lower() not in ("nome", "name", "---")
    ]


def extract_champions_active(plan_md: str, t: dict) -> str:
    people = extract_active_people(plan_md)
    if not people:
        return ""
    lines = [t["committee_intro"], ""]
    for name, email in people:
        lines.append(t["person"].format(name=name, email=email))
    return "\n".join(lines)


def extract_calendar(plan_md: str) -> str:
    """Extract the calendar table from section 5 (next 90 days)."""
    section = extract_section(plan_md, H_CALENDAR)
    if not section:
        return ""
    table_match = re.search(r"\|.*?\|.*?(?=\n\n|\Z)", section, re.DOTALL)
    return table_match.group(0).strip() if table_match else section[:500]


def extract_top_topics(plan_md: str, n=5) -> list[tuple[str, int]]:
    """Top topics from the executive summary numbered list."""
    section = extract_section(plan_md, H_SUMMARY)
    matches = re.findall(TOPIC_LINE, section, re.MULTILINE)
    return [(m[0], int(m[1])) for m in matches[:n]]


def extract_format_prefs(plan_md: str) -> str:
    """Extract the format preferences table from section 6."""
    section = extract_section(plan_md, H_FORMAT)
    table_match = re.search(
        rf"{H_FORMATS_SUB}.*?\n(\|.*?\n(?:\|.*?\n)+)", section, re.DOTALL
    )
    return table_match.group(1).strip() if table_match else ""


def extract_barriers(plan_md: str) -> str:
    """Extract the top barriers table from section 7."""
    section = extract_section(plan_md, H_BARRIERS)
    table_match = re.search(r"\|.*?\n(?:\|[-: ]+\|\n)?(\|.*?\n)+", section)
    return table_match.group(0).strip() if table_match else ""


def extract_quick_wins_calendar(plan_md: str,
                                weeks_range: tuple[int, int]) -> str:
    """Quick wins for a week range from sections 5 and 11."""
    section_5 = extract_section(plan_md, H_CALENDAR)
    section_11 = extract_section(plan_md, H_SCHEDULE)

    items = []
    for src in [section_5, section_11]:
        for line in src.split("\n"):
            m = re.search(r"W(\d+)[,\-\s]+W?(\d+)?\s*\|([^|]+)\|", line)
            if m:
                start_week = int(m.group(1))
                if weeks_range[0] <= start_week <= weeks_range[1]:
                    activity = m.group(3).strip()
                    if activity and activity != "Workshop":
                        items.append(f"- W{start_week}: {activity}")
    return "\n".join(items) if items else ""


def _table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:]


def calendar_to_comm_table(calendar: str, t: dict) -> str:
    """Week | Workshop | Audience | Champion | Format → comm plan."""
    rows = [r for r in _table_rows(calendar) if len(r) >= 5]
    if not rows:
        return ""
    lines = [t["comm_head"], "|---|---|---|---|"]
    for week, workshop, audience, champion, fmt in (r[:5] for r in rows):
        lines.append(f"| {workshop} ({audience}) | {fmt} | {week} | "
                     f"{champion} |")
    return "\n".join(lines)


def cohorts_to_training_table(section: str, t: dict) -> str:
    """### Cohort X (name) + three bullets → training plan table."""
    blocks = re.split(r"^### ", section, flags=re.MULTILINE)[1:]
    lines = []
    for block in blocks:
        head, _, body = block.partition("\n")
        bullets = [b.strip()[2:] for b in body.splitlines()
                   if b.strip().startswith("- ")]
        count = re.search(r"\d+", bullets[0]) if bullets else None
        rest = [b.split(":**", 1)[-1].strip(" *") for b in bullets[1:3]]
        rest += [""] * (2 - len(rest))
        name = head.strip().removeprefix("Cohort ").strip()
        audience = t["cohort_row"].format(
            name=name, count=count.group(0) if count else "?")
        lines.append(f"| {audience} | {rest[0]} | {rest[1]} |")
    if not lines:
        return ""
    return "\n".join([t["train_head"], "|---|---|---|"] + lines)


def build_payload(plan_md: str, plan_name: str, lang: str) -> dict:
    t = STRINGS[lang]
    champions = extract_champions_active(plan_md, t)
    calendar = extract_calendar(plan_md)
    top_topics = extract_top_topics(plan_md)
    quick_w1_4 = extract_quick_wins_calendar(plan_md, (1, 4))
    quick_w5_8 = extract_quick_wins_calendar(plan_md, (5, 8))
    quick_w9_12 = extract_quick_wins_calendar(plan_md, (9, 12))

    comm_table = calendar_to_comm_table(calendar, t)
    comm_plan = (t["comm_intro"] + comm_table if comm_table
                 else t["comm_missing"])

    cohorts_section = extract_section(plan_md, H_COHORTS)
    train_table = cohorts_to_training_table(cohorts_section, t)
    training = (t["training_intro"] + train_table if train_table
                else t["training_missing"])

    # ADKAR: the Knowledge stage lists the top topics
    adkar = t["adkar_head"]
    for i, (topic, count) in enumerate(top_topics[:5], 1):
        adkar += t["adkar_item"].format(i=i, topic=topic, count=count)
    adkar += t["adkar_tail"]

    inputs = {
        "executive_steering_committee": champions or t["no_committee"],
        "tpo": t["no_tpo"],
        "dimension_owners": t["no_owners"],
        "raci_matrix": t["no_raci"],
        "communication_plan": comm_plan,
        "training_plan": training,
        "adkar_notes": adkar,
        "risk_register": t["no_risks"],
        "quick_wins_w1_4": quick_w1_4 or t["no_qw_1_4"],
        "quick_wins_w5_8": quick_w5_8 or t["no_qw_5_8"],
        "quick_wins_w9_12": quick_w9_12 or t["no_qw_9_12"],
    }
    manual = [k for k, v in inputs.items() if v.startswith("(")]
    return {
        "metadata": {
            "generated_at": datetime.datetime.now(
                datetime.UTC).isoformat(),
            "generator": "wizard/scripts/auto_fill_from_plan.py (Mode D)",
            "source_plan": plan_name,
            "completion_pct": round(
                100 * (len(inputs) - len(manual)) / len(inputs)),
            "manual_required": manual,
            "lang": lang,
            **branding.json_metadata(),
        },
        "implementation_guide_inputs": inputs,
    }


def _display(path: Path) -> Path:
    return path.relative_to(KIT) if path.is_relative_to(KIT) else path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--plan", "--plano", dest="plan", default=None,
        help="Path to training-plan-DATE.md (default: latest in "
             "output/)",
    )
    ap.add_argument("--out",
                    default=str(KIT / "implementation-guide-inputs.json"))
    ap.add_argument("--lang", choices=SUPPORTED_LANGS, default="en",
                    help="Language of the generated text (default: en). "
                         "The plan can be in either language.")
    args = ap.parse_args()
    t = STRINGS[args.lang]

    out_path = Path(args.out)
    if args.plan:
        plan_path = Path(args.plan)
    else:
        plan_path = find_latest_plan(KIT / "output")

    if not plan_path or not plan_path.exists():
        print(t["c_missing"])
        print(t["c_run"])
        return 1

    plan_md = plan_path.read_text(encoding="utf-8")
    print(t["c_reading"].format(path=_display(plan_path)))

    payload = build_payload(plan_md, plan_path.name, args.lang)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    print(t["c_done"].format(path=_display(out_path)))
    print(t["c_filled"])
    for line in t["c_fields"]:
        print(line)
    print(t["c_manual"])
    for line in t["c_manual_fields"]:
        print(line)
    print(t["c_next"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
