#!/usr/bin/env python3
"""Generate a personalized training plan from the Learning Survey.

Reads: survey-learning/responses-learning.json
       (output of /import-survey-learning)
Writes: output/training-plan-<DATE>.md
        (12 sections, with attendee names and emails)

Usage:
    python3 generate_training_plan.py
    python3 generate_training_plan.py --input X --out Y --lang pt-br
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "reports" / "scripts"))
import branding  # noqa: E402

SUPPORTED_LANGS = ("en", "pt-br", "es")

# Developer Survey dimensions, prefixed DS- so they do not collide with
# the v2 assessment dimensions D1 to D9. Forms built before the prefix
# (options such as "D8 — Security & Governance") still parse.
DIMENSION_NAMES = {
    "DS-D2": "Copilot Adoption",
    "DS-D3": "MS/GH Tooling Breadth",
    "DS-D4": "AI Dev Practices",
    "DS-D5": "Agent Concepts Mastery",
    "DS-D6": "Instructions Maturity",
    "DS-D7": "Best Practices",
    "DS-D8": "Security & Governance",
}

LEVELS = ["L0", "L1", "L2", "L3", "L4"]
DIMENSION_IDS = list(DIMENSION_NAMES)
TOPIC_QIDS = ["L4-Q1", "L4-Q2", "L4-Q3", "L4-Q4", "L4-Q5"]

SEP_2 = "| --- | --- |"
SEP_3 = "| --- | --- | --- |"
SEP_4 = "| --- | --- | --- | --- |"
SEP_5 = "| --- | --- | --- | --- | --- |"
SEP_7 = "| --- | --- | --- | --- | --- | --- | --- |"

# Section headings keep the "N · " prefix in every language;
# wizard/scripts/auto_fill_from_plan.py parses them.
STRINGS = {
    "en": {
        "title": "# AI Training Plan: Personalized Roadmap",
        "meta": "**Date:** {date}  ·  **Respondents:** {n} (identified)"
                "  ·  Survey: Learning & Growth (32 questions)",
        "author": "**Author:** {author}  ·  **Contact:** {contact}",
        "empty": "-",
        "unspecified": "(not specified)",
        "hybrid": "Hybrid",
        "self_title": "### Team-perceived AI maturity "
                      "(L2 self-assessment)",
        "self_header": "| Dimension | L0 | L1 | L2 | L3 | L4 | Median |",
        "champ_title": "### 👥 Champions Network identified",
        "champ_active": "- **{n} active** (want to be a Champion "
                        "without extra support)",
        "champ_supported": "- **{n} with support** (want to be a "
                           "Champion if training is provided)",
        "champ_maybe": "- **{n} maybe** (need to think about it)",
        "champ_refs": "- **Top 3 natural references** (named by peers "
                      "in L6-Q2):",
        "champ_ref": "  - {name} (named by {count} people)",
        "qw_title": "### ⚡ 3 recommended quick wins (next 30 days)",
        "qw_1": "1. **Workshop: {topic}** ({count} pre-validated "
                "attendees)",
        "qw_2": "2. **Champions Kickoff** (activate the {n} active "
                "Champions identified)",
        "qw_3": "3. **Remove barrier #1: '{barrier}'** (cited by "
                "{count}/{total} devs)",
        "s1": "## 1 · Executive Summary",
        "prio_title": "### 🎯 Top 3 PRIORITY dimensions to grow (L3-Q1)",
        "prio_row": "- **{did}** {name}: {count}/{total} devs "
                    "({pct:.0f}%)",
        "topics_title": "### 📚 Top 10 most requested topics (L4)",
        "topic_row": "{i}. **{topic}**: {count} devs ({pct:.0f}%)",
        "s2": "## 2 · Top 10 requested topics (with pre-validated "
              "attendees)",
        "s2_topic": "### {i}. {topic} ({count} attendees)",
        "s2_demand": "**Demand:** {count}/{total} devs ({pct:.0f}%)",
        "s2_attendees": "**Pre-validated attendees** (already confirmed "
                        "in their answers):",
        "s3": "## 3 · Suggested cohorts by rubric dimension",
        "cohort": "### Cohort {did} ({name})",
        "cohort_count": "- **{n} devs want to grow in this dimension**",
        "cohort_format": "- **Team's preferred format:** {fmt}",
        "cohort_plan": "- **Plan:** 4-6 week cohort with live sessions "
                       "and a self-paced lab",
        "s4": "## 4 · Champions Network (3 tiers)",
        "active_title": "### 🥇 Active (already want to be a Champion)",
        "active_step": "Invite to train-the-trainer",
        "active_header": "| Name | Email | Next step |",
        "active_empty": "_No dev volunteered directly. Consider "
                        "activating the 'with support' tier._",
        "supported_title": "### 🥈 With support (want to if dedicated "
                           "training is provided)",
        "supported_step": "Champion enablement workshop + materials",
        "supported_header": "| Name | Email | Support needed |",
        "none": "_(none)_",
        "mentor_title": "### 🤝 Mentor candidates (volunteered in L6-Q4)",
        "mentor_header": "| Name | Email | Topic they teach |",
        "mentee_title": "### 🎓 Mentees (want 1:1 mentoring)",
        "mentee_header": "| Name | Email |",
        "s5": "## 5 · Suggested calendar (next 90 days)",
        "cal_header": "| Week | Workshop | Audience | Champion "
                      "| Format |",
        "cal_kickoff": "| W1 | Champions Kickoff | {n} | Eng Lead "
                       "| 2h live |",
        "cal_topic": "| W{week} | {topic} | {count} | {champion} "
                     "| 4h hands-on |",
        "cal_tail": [
            "| W4 | Office hours #1 | Everyone | Champions | 1h Q&A |",
            "| W6, W8, W10, W12 | Biweekly office hours | Everyone "
            "| Champions | 1h Q&A |",
        ],
        "s6": "## 6 · Preferred format and cadence",
        "fmt_title": "### Formats (top 5, L5-Q1 multi)",
        "fmt_header": "| Format | N | % |",
        "time_title": "### Available time per week (L5-Q2)",
        "time_header": "| Time | N | % |",
        "pref_title": "### Cohort vs self-paced (L5-Q4)",
        "pref_header": "| Preference | N | % |",
        "act_time": "Block 2h/week on the calendar",
        "act_license": "Review licenses with IT, target 100%",
        "act_champion": "Activate the identified Champions Network",
        "act_start": "Create a learning path in a Copilot Space",
        "act_default": "Discuss with the team lead",
        "s7": "## 7 · Barriers to remove (prioritized)",
        "bar_header": "| Barrier | Devs affected | % "
                      "| Suggested action |",
        "quote": "> _\"{quote}\"_ (suggested by {name})",
        "s8": "## 8 · Team wishlist",
        "wish_workshops": "### Workshops suggested by the team (L7-Q2)",
        "wish_speakers": "### Suggested external speakers (L7-Q3)",
        "wish_other": "### Other suggestions (L7-Q4)",
        "s9": "## 9 · 🔗 Connection with other surveys",
        "s9_intro": "If you also ran the **Developer Survey** "
                    "(anonymous) and the **main Assessment**, compare:",
        "s9_header": "| Dimension | Self-perception (this survey, L2) "
                     "| Measured rubric (survey-devs, D-X) "
                     "| Assessment capability |",
        "s9_row": "| {did} {name} | median {median} "
                  "| (run /insights-developer-survey) "
                  "| (run /calculate-scores) |",
        "ra_workshop": "Workshop: {topic}",
        "ra_workshop_why": "{count} pre-validated attendees",
        "ra_kickoff_why": "{n} active Champions identified",
        "ra_barrier": "Remove barrier: {barrier}",
        "ra_barrier_why": "{count} devs affected",
        "ra_mentoring": "1:1 mentoring program",
        "ra_mentoring_why": "{mentors} mentors × {mentees} mentees",
        "ra_office": "Biweekly office hours",
        "ra_office_why": "Addresses all low-adoption barriers",
        "h_30": "30 days",
        "h_60": "60 days",
        "h_ongoing": "Ongoing from W2",
        "s10": "## 10 · 🎯 Top 5 prioritized actions (impact × ease)",
        "act_header": "| # | Action | Impact | Horizon |",
        "s11": "## 11 · 📅 30-day schedule",
        "sch_header": "| Week | Activities |",
        "sch_w1": "| **W1** | Champions Kickoff ({n} people) + workshop "
                  "scheduling |",
        "sch_w2": "| **W2** | Workshop {topic} ({count} attendees) |",
        "sch_tail": [
            "| **W3** | Office hours #1 + removal of the top barrier |",
            "| **W4** | Retrospective + plan review |",
        ],
        "s12": "## 12 · 📋 Appendix: Respondents (for leadership to "
               "send invites)",
        "s12_warn": "> ⚠️ This table contains names and emails. **DO "
                    "NOT share publicly.** Use it only for workshop "
                    "invites.",
        "s12_header": "| Name | Email | Wants to be a Champion? |",
        "tier_active": "Yes, active",
        "tier_supported": "Yes, with support",
        "tier_maybe": "Maybe",
        "tier_no": "No",
        "footer": "_Plan generated by the `/training-plan` skill · "
                  "{date} · Override by editing the .md manually_",
        "c_done": "\n✅ Training plan → {path}",
        "c_count": "\n📊 {n} IDENTIFIED respondents",
        "c_topics": "\n📚 Top 3 requested topics:",
        "c_topic": "   {i}. {topic}: {count} attendees",
        "c_champions": "\n👥 Champions: {a} active · {s} with support "
                       "· {m} maybe",
        "c_mentors": "\n🎓 Mentor pairs: {mentors} mentors · "
                     "{mentees} mentees",
        "c_barrier": "\n⚠ Top barrier: {barrier} ({count}/{total} devs)",
        "c_missing": "❌ {path} not found. Run /import-survey-learning "
                     "first.",
        "c_few": "⚠ Only {n} respondents. The plan will be preliminary.",
    },
    "pt-br": {
        "title": "# Plano de Capacitação IA: Roadmap Personalizado",
        "meta": "**Data:** {date}  ·  **Respondentes:** {n} "
                "(identificados)  ·  Survey: Learning & Growth "
                "(32 perguntas)",
        "author": "**Autor:** {author}  ·  **Contato:** {contact}",
        "empty": "-",
        "unspecified": "(não especificou)",
        "hybrid": "Híbrido",
        "self_title": "### Maturidade IA percebida pelo time "
                      "(auto-avaliação L2)",
        "self_header": "| Dimensão | L0 | L1 | L2 | L3 | L4 | Mediana |",
        "champ_title": "### 👥 Champions Network identificados",
        "champ_active": "- **{n} ativos** (querem ser Champion sem "
                        "precisar suporte)",
        "champ_supported": "- **{n} com suporte** (querem ser Champion "
                           "se tiver treino)",
        "champ_maybe": "- **{n} maybe** (precisam pensar)",
        "champ_refs": "- **Top 3 referências naturais** (mencionados "
                      "por colegas em L6-Q2):",
        "champ_ref": "  - {name} (mencionado por {count} pessoas)",
        "qw_title": "### ⚡ 3 quick wins recomendados (próximos 30 dias)",
        "qw_1": "1. **Workshop: {topic}**: {count} inscritos "
                "pré-validados",
        "qw_2": "2. **Champions Kickoff**: ativar os {n} Champions "
                "ativos identificados",
        "qw_3": "3. **Remover barreira #1: '{barrier}'**: citada por "
                "{count}/{total} devs",
        "s1": "## 1 · Sumário Executivo",
        "prio_title": "### 🎯 Top 3 dimensões PRIORITÁRIAS para crescer "
                      "(L3-Q1)",
        "prio_row": "- **{did}** {name}: {count}/{total} devs "
                    "({pct:.0f}%)",
        "topics_title": "### 📚 Top 10 tópicos mais demandados (L4)",
        "topic_row": "{i}. **{topic}**: {count} devs ({pct:.0f}%)",
        "s2": "## 2 · Top 10 tópicos demandados (com inscritos "
              "pré-validados)",
        "s2_topic": "### {i}. {topic}: {count} inscritos",
        "s2_demand": "**Demanda:** {count}/{total} devs ({pct:.0f}%)",
        "s2_attendees": "**Inscritos pré-validados** (já confirmados na "
                        "resposta):",
        "s3": "## 3 · Cohorts sugeridos por dimensão da rubrica",
        "cohort": "### Cohort {did} ({name})",
        "cohort_count": "- **{n} devs querem evoluir nesta dimensão**",
        "cohort_format": "- **Formato preferido pelo time:** {fmt}",
        "cohort_plan": "- **Plano:** cohort de 4-6 semanas com sessões "
                       "síncronas + lab self-paced",
        "s4": "## 4 · Champions Network (3 tiers)",
        "active_title": "### 🥇 Ativos (já querem ser Champion)",
        "active_step": "Convidar para train-the-trainer",
        "active_header": "| Nome | Email | Próximo passo |",
        "active_empty": "_Nenhum dev se candidatou diretamente. "
                        "Considere ativar tier 'com suporte'._",
        "supported_title": "### 🥈 Com suporte (querem se tiver treino "
                           "dedicado)",
        "supported_step": "Workshop de capacitação Champion + materiais",
        "supported_header": "| Nome | Email | Suporte necessário |",
        "none": "_(nenhum)_",
        "mentor_title": "### 🤝 Mentor candidates (se ofereceram em "
                        "L6-Q4)",
        "mentor_header": "| Nome | Email | Tópico que ensina |",
        "mentee_title": "### 🎓 Mentees (querem mentoria 1:1)",
        "mentee_header": "| Nome | Email |",
        "s5": "## 5 · Calendário sugerido (próximos 90 dias)",
        "cal_header": "| Semana | Workshop | Audiência | Champion "
                      "| Formato |",
        "cal_kickoff": "| W1 | Champions Kickoff | {n} | Líder Eng "
                       "| 2h síncrono |",
        "cal_topic": "| W{week} | {topic} | {count} | {champion} "
                     "| 4h hands-on |",
        "cal_tail": [
            "| W4 | Office hours #1 | Todos | Champions | 1h Q&A |",
            "| W6, W8, W10, W12 | Office hours quinzenal | Todos "
            "| Champions | 1h Q&A |",
        ],
        "s6": "## 6 · Formato e cadência preferidos",
        "fmt_title": "### Formatos (top 5: L5-Q1 multi)",
        "fmt_header": "| Formato | N | % |",
        "time_title": "### Tempo disponível por semana (L5-Q2)",
        "time_header": "| Tempo | N | % |",
        "pref_title": "### Cohort vs self-paced (L5-Q4)",
        "pref_header": "| Preferência | N | % |",
        "act_time": "Bloquear 2h/sem no calendário",
        "act_license": "Revisar licenças com TI, target 100%",
        "act_champion": "Ativar Champions Network identificados",
        "act_start": "Criar learning path em Copilot Space",
        "act_default": "Discutir com líder",
        "s7": "## 7 · Barreiras a remover (priorizado)",
        "bar_header": "| Barreira | Devs afetados | % "
                      "| Ação sugerida |",
        "quote": "> _\"{quote}\"_ (sugerido por {name})",
        "s8": "## 8 · Wishlist do time",
        "wish_workshops": "### Workshops sugeridos pelo time (L7-Q2)",
        "wish_speakers": "### Palestrantes externos sugeridos (L7-Q3)",
        "wish_other": "### Outras sugestões (L7-Q4)",
        "s9": "## 9 · 🔗 Conexão com outros surveys",
        "s9_intro": "Se você rodou também o **Developer Survey** "
                    "(anônimo) e o **Assessment principal**, compare:",
        "s9_header": "| Dimensão | Auto-perception (este survey, L2) "
                     "| Rubrica medida (survey-devs, D-X) "
                     "| Capability assessment |",
        "s9_row": "| {did} {name} | mediana {median} "
                  "| (rodar /insights-developer-survey) "
                  "| (rodar /calculate-scores) |",
        "ra_workshop": "Workshop: {topic}",
        "ra_workshop_why": "{count} inscritos pré-validados",
        "ra_kickoff_why": "{n} Champions ativos identificados",
        "ra_barrier": "Remover barreira: {barrier}",
        "ra_barrier_why": "{count} devs afetados",
        "ra_mentoring": "Programa de mentoria 1:1",
        "ra_mentoring_why": "{mentors} mentores × {mentees} mentees",
        "ra_office": "Office hours quinzenal",
        "ra_office_why": "Atende todas as barreiras de baixa adoção",
        "h_30": "30 dias",
        "h_60": "60 dias",
        "h_ongoing": "Contínuo a partir de W2",
        "s10": "## 10 · 🎯 Top 5 ações priorizadas (impacto × "
               "facilidade)",
        "act_header": "| # | Ação | Impacto | Horizonte |",
        "s11": "## 11 · 📅 Cronograma 30 dias",
        "sch_header": "| Semana | Atividades |",
        "sch_w1": "| **W1** | Champions Kickoff ({n} pessoas) + "
                  "agendamento de workshops |",
        "sch_w2": "| **W2** | Workshop {topic} ({count} inscritos) |",
        "sch_tail": [
            "| **W3** | Office hours #1 + remoção de barreira top |",
            "| **W4** | Retrospectiva + revisão do plano |",
        ],
        "s12": "## 12 · 📋 Apêndice: Respondentes (para liderança usar "
               "para convites)",
        "s12_warn": "> ⚠️ Esta tabela contém nomes/emails. **NÃO "
                    "compartilhar publicamente**: só usar para convites "
                    "de workshops.",
        "s12_header": "| Nome | Email | Quer Champion? |",
        "tier_active": "Sim ativo",
        "tier_supported": "Sim com suporte",
        "tier_maybe": "Talvez",
        "tier_no": "Não",
        "footer": "_Plano gerado pela skill `/training-plan` · "
                  "{date} · Sobrescreva editando manualmente o .md_",
        "c_done": "\n✅ Plano de capacitação → {path}",
        "c_count": "\n📊 {n} respondentes IDENTIFICADOS",
        "c_topics": "\n📚 Top 3 tópicos demandados:",
        "c_topic": "   {i}. {topic}: {count} inscritos",
        "c_champions": "\n👥 Champions: {a} ativos · {s} com suporte "
                       "· {m} maybe",
        "c_mentors": "\n🎓 Mentor pairs: {mentors} mentores · "
                     "{mentees} mentees",
        "c_barrier": "\n⚠ Top barreira: {barrier} ({count}/{total} "
                     "devs)",
        "c_missing": "❌ {path} não encontrado. Rode "
                     "/import-survey-learning primeiro.",
        "c_few": "⚠ Apenas {n} respondentes. Plano será preliminar.",
    },
    "es": {
        "title": "# Plan de capacitación en IA: roadmap personalizado",
        "meta": "**Fecha:** {date}  ·  **Encuestados:** {n} (identificados)  "
                "·  Encuesta: Learning & Growth (32 preguntas)",
        "author": "**Autor:** {author}  ·  **Contacto:** {contact}",
        "empty": "-",
        "unspecified": "(no especificado)",
        "hybrid": "Híbrido",
        "self_title": "### Madurez de IA percibida por el equipo "
                      "(autoevaluación L2)",
        "self_header": "| Dimensión | L0 | L1 | L2 | L3 | L4 | Mediana |",
        "champ_title": "### 👥 Champions Network identificada",
        "champ_active": "- **{n} activos** (quieren ser Champion sin apoyo "
                        "adicional)",
        "champ_supported": "- **{n} con apoyo** (quieren ser Champion si se "
                           "proporciona capacitación)",
        "champ_maybe": "- **{n} quizás** (necesitan pensarlo)",
        "champ_refs": "- **Top 3 referencias naturales** (nombradas por pares "
                      "en L6-Q2):",
        "champ_ref": "  - {name} (nombrado por {count} personas)",
        "qw_title": "### ⚡ 3 quick wins recomendados (próximos 30 días)",
        "qw_1": "1. **Workshop: {topic}** ({count} asistentes prevalidados)",
        "qw_2": "2. **Champions Kickoff** (activar los {n} Champions activos "
                "identificados)",
        "qw_3": "3. **Remover barrera #1: '{barrier}'** (citada por "
                "{count}/{total} devs)",
        "s1": "## 1 · Resumen ejecutivo",
        "prio_title": "### 🎯 Top 3 dimensiones PRIORITARIAS para crecer "
                      "(L3-Q1)",
        "prio_row": "- **{did}** {name}: {count}/{total} devs ({pct:.0f}%)",
        "topics_title": "### 📚 Top 10 temas más solicitados (L4)",
        "topic_row": "{i}. **{topic}**: {count} devs ({pct:.0f}%)",
        "s2": "## 2 · Top 10 temas solicitados (con asistentes prevalidados)",
        "s2_topic": "### {i}. {topic} ({count} asistentes)",
        "s2_demand": "**Demanda:** {count}/{total} devs ({pct:.0f}%)",
        "s2_attendees": "**Asistentes prevalidados** (ya confirmados en sus "
                        "respuestas):",
        "s3": "## 3 · Cohorts sugeridos por dimensión de la rúbrica",
        "cohort": "### Cohort {did} ({name})",
        "cohort_count": "- **{n} devs quieren crecer en esta dimensión**",
        "cohort_format": "- **Formato preferido del equipo:** {fmt}",
        "cohort_plan": "- **Plan:** cohort de 4-6 semanas con sesiones en "
                       "vivo y un laboratorio self-paced",
        "s4": "## 4 · Champions Network (3 niveles)",
        "active_title": "### 🥇 Activos (ya quieren ser Champion)",
        "active_step": "Invitar a train-the-trainer",
        "active_header": "| Nombre | Email | Próximo paso |",
        "active_empty": "_Ningún dev se ofreció directamente. Considera "
                        "activar el nivel 'con apoyo'._",
        "supported_title": "### 🥈 Con apoyo (quieren hacerlo si se "
                           "proporciona capacitación dedicada)",
        "supported_step": "Workshop de habilitación para Champion + "
                          "materiales",
        "supported_header": "| Nombre | Email | Apoyo necesario |",
        "none": "_(ninguno)_",
        "mentor_title": "### 🤝 Candidatos a mentor (se ofrecieron en L6-Q4)",
        "mentor_header": "| Nombre | Email | Tema que enseñan |",
        "mentee_title": "### 🎓 Mentees (quieren mentoría 1:1)",
        "mentee_header": "| Nombre | Email |",
        "s5": "## 5 · Calendario sugerido (próximos 90 días)",
        "cal_header": "| Semana | Workshop | Audiencia | Champion | Formato |",
        "cal_kickoff": "| W1 | Champions Kickoff | {n} | Líder de ingeniería "
                       "| 2h en vivo |",
        "cal_topic": "| W{week} | {topic} | {count} | {champion} | 4h "
                     "práctico |",
        "cal_tail": [
            "| W4 | Office hours #1 | Todos | Champions | 1h Q&A |",
            "| W6, W8, W10, W12 | Office hours quincenales | Todos | "
            "Champions | 1h Q&A |",
        ],
        "s6": "## 6 · Formato y cadencia preferidos",
        "fmt_title": "### Formatos (top 5, L5-Q1 multi)",
        "fmt_header": "| Formato | N | % |",
        "time_title": "### Tiempo disponible por semana (L5-Q2)",
        "time_header": "| Tiempo | N | % |",
        "pref_title": "### Cohort vs self-paced (L5-Q4)",
        "pref_header": "| Preferencia | N | % |",
        "act_time": "Bloquear 2h/semana en el calendario",
        "act_license": "Revisar licencias con TI, objetivo 100%",
        "act_champion": "Activar la Champions Network identificada",
        "act_start": "Crear una ruta de aprendizaje en un Copilot Space",
        "act_default": "Conversar con el líder del equipo",
        "s7": "## 7 · Barreras a remover (priorizadas)",
        "bar_header": "| Barrera | Devs afectados | % | Acción sugerida |",
        "quote": "> _\"{quote}\"_ (sugerido por {name})",
        "s8": "## 8 · Wishlist del equipo",
        "wish_workshops": "### Workshops sugeridos por el equipo (L7-Q2)",
        "wish_speakers": "### Ponentes externos sugeridos (L7-Q3)",
        "wish_other": "### Otras sugerencias (L7-Q4)",
        "s9": "## 9 · 🔗 Conexión con otras encuestas",
        "s9_intro": "Si también ejecutaste el **Developer Survey** (anónimo) "
                    "y la **evaluación principal**, compara:",
        "s9_header": "| Dimensión | Autopercepción (esta encuesta, L2) | "
                     "Rúbrica medida (survey-devs, D-X) | Capacidad de "
                     "evaluación |",
        "s9_row": "| {did} {name} | mediana {median} | (ejecuta "
                  "/insights-developer-survey) | (ejecuta "
                  "/calculate-scores) |",
        "ra_workshop": "Workshop: {topic}",
        "ra_workshop_why": "{count} asistentes prevalidados",
        "ra_kickoff_why": "{n} Champions activos identificados",
        "ra_barrier": "Remover barrera: {barrier}",
        "ra_barrier_why": "{count} devs afectados",
        "ra_mentoring": "Programa de mentoría 1:1",
        "ra_mentoring_why": "{mentors} mentores × {mentees} mentees",
        "ra_office": "Office hours quincenales",
        "ra_office_why": "Aborda todas las barreras de baja adopción",
        "h_30": "30 días",
        "h_60": "60 días",
        "h_ongoing": "Continuo desde W2",
        "s10": "## 10 · 🎯 Top 5 acciones priorizadas (impacto × facilidad)",
        "act_header": "| # | Acción | Impacto | Horizonte |",
        "s11": "## 11 · 📅 Cronograma de 30 días",
        "sch_header": "| Semana | Actividades |",
        "sch_w1": "| **W1** | Champions Kickoff ({n} personas) + programación "
                  "de workshops |",
        "sch_w2": "| **W2** | Workshop {topic} ({count} asistentes) |",
        "sch_tail": [
            "| **W3** | Office hours #1 + remoción de la barrera principal |",
            "| **W4** | Retrospectiva + revisión del plan |",
        ],
        "s12": "## 12 · 📋 Apéndice: encuestados (para que liderazgo envíe "
               "invitaciones)",
        "s12_warn": "> ⚠️ Esta tabla contiene nombres y emails. **NO "
                    "compartir públicamente.** Úsala solo para invitaciones a "
                    "workshops.",
        "s12_header": "| Nombre | Email | ¿Quiere ser Champion? |",
        "tier_active": "Sí, activo",
        "tier_supported": "Sí, con apoyo",
        "tier_maybe": "Quizás",
        "tier_no": "No",
        "footer": "_Plan generado por la skill `/training-plan` · {date} "
                  "· Sobrescribe editando el .md manualmente_",
        "c_done": "\n✅ Plan de capacitación → {path}",
        "c_count": "\n📊 {n} encuestados IDENTIFICADOS",
        "c_topics": "\n📚 Top 3 temas solicitados:",
        "c_topic": "   {i}. {topic}: {count} asistentes",
        "c_champions": "\n👥 Champions: {a} activos · {s} con apoyo · {m} "
                       "quizás",
        "c_mentors": "\n🎓 Pares de mentoría: {mentors} mentores · {mentees} "
                     "mentees",
        "c_barrier": "\n⚠ Barrera principal: {barrier} ({count}/{total} devs)",
        "c_missing": "❌ {path} no encontrado. Ejecuta "
                     "/import-survey-learning primero.",
        "c_few": "⚠ Solo {n} encuestados. El plan será preliminar.",
    },
}


@dataclass
class LearningAggregates:
    self_perception: dict[str, Counter]
    priorities: Counter
    topic_counts: Counter
    topic_attendees: dict[str, list[dict[str, str]]]
    formats: Counter
    time_per_week: Counter
    cohort_pref: Counter
    actives: list[dict[str, str]]
    supported: list[dict[str, str]]
    maybe: list[dict[str, str]]
    mentors: list[dict[str, str]]
    mentees: list[dict[str, str]]
    references: Counter
    barriers: Counter
    pain_quotes: list[tuple[str, str]]
    workshop_wishes: list[tuple[str, str]]
    speaker_wishes: list[tuple[str, str]]


def safe_pct(num, total):
    return round(100 * num / total, 1) if total > 0 else 0


def fold_text(value):
    """Lowercase and remove accents so PT-BR, EN, and ES options match."""
    text = str(value or "").strip().lower()
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def contains_any(value, patterns):
    folded = fold_text(value)
    return any(fold_text(pattern) in folded for pattern in patterns)


def starts_any(value, prefixes):
    folded = fold_text(value)
    return any(folded.startswith(fold_text(prefix)) for prefix in prefixes)


def mail(address):
    """Email as a Markdown autolink (no bare addresses in the report)."""
    address = str(address or "").strip()
    return f"<{address}>" if "@" in address else address


def response_value(respondent, qid):
    value = respondent.get("responses", {}).get(qid, {}).get("value", "")
    return str(value).strip()


def selected_options(responses, qid):
    raw = responses.get(qid, {}).get("value", "")
    return [option.strip() for option in str(raw).split(";")
            if option.strip()]


def is_topic_skip_option(topic):
    return contains_any(topic, [
        "Já domino",
        "Não tenho interesse",
        "Não conheço",
        "I already master",
        "I am not interested",
        "I do not know",
        "Ya domino",
        "No tengo interés",
        "No conozco",
    ])


def champion_tier(answer):
    if starts_any(answer, ["Talvez", "Maybe", "Tal vez"]):
        return "maybe"
    if contains_any(answer, [
        "quero ser Champion ativo",
        "active Champion",
        "Champion activo",
    ]):
        return "active"
    if contains_any(answer, [
        "se tiver suporte",
        "support/training",
        "soporte/entrenamiento",
    ]):
        return "supported"
    return None


def is_affirmative(answer):
    return starts_any(answer, ["Sim", "Yes", "Sí"])


def is_no_barrier_option(option):
    return contains_any(option, [
        "sem barreiras",
        "no significant barriers",
        "sin barreras significativas",
    ])


def champion_short_label(value, t):
    tier = champion_tier(value)
    if tier in ("active", "supported", "maybe"):
        return t[f"tier_{tier}"]
    return t["tier_no"]


def median_level(counts, empty="-"):
    sorted_levels = []
    for level in LEVELS:
        sorted_levels.extend([level] * counts.get(level, 0))
    if not sorted_levels:
        return empty
    return sorted_levels[len(sorted_levels) // 2]


def collect_l2_self_perception(respondents):
    """L2-Q1 -> DS-D2, L2-Q2 -> DS-D3, ..., L2-Q7 -> DS-D8."""
    dist = {}
    for index, dimension_id in enumerate(DIMENSION_IDS, start=1):
        counts = Counter()
        for respondent in respondents:
            answer = response_value(respondent, f"L2-Q{index}")
            for level in LEVELS:
                if answer.startswith(level):
                    counts[level] += 1
                    break
        dist[dimension_id] = counts
    return dist


def collect_priorities(respondents):
    counts = Counter()
    for respondent in respondents:
        responses = respondent.get("responses", {})
        for option in selected_options(responses, "L3-Q1"):
            key = option if option.startswith("DS-") else "DS-" + option
            for dimension_id in DIMENSION_IDS:
                if re.match(re.escape(dimension_id) + r"(?!\d)", key):
                    counts[dimension_id] += 1
                    break
    return counts


def iter_learning_topics(respondent):
    responses = respondent.get("responses", {})
    for qid in TOPIC_QIDS:
        for topic in selected_options(responses, qid):
            if not is_topic_skip_option(topic):
                yield topic


def _person(respondent):
    return {
        "name": respondent.get("name", "?"),
        "email": respondent.get("email", "?"),
    }


def collect_topics(respondents):
    topic_counts = Counter()
    topic_attendees = defaultdict(list)
    for respondent in respondents:
        attendee = _person(respondent)
        for topic in iter_learning_topics(respondent):
            topic_counts[topic] += 1
            topic_attendees[topic].append(attendee)
    return topic_counts, topic_attendees


def collect_format_prefs(respondents):
    formats = Counter()
    time_per_week = Counter()
    cohort_pref = Counter()
    for respondent in respondents:
        responses = respondent.get("responses", {})
        formats.update(selected_options(responses, "L5-Q1"))
        time = response_value(respondent, "L5-Q2")
        cohort = response_value(respondent, "L5-Q4")
        if time:
            time_per_week[time] += 1
        if cohort:
            cohort_pref[cohort] += 1
    return formats, time_per_week, cohort_pref


def collect_champions(respondents):
    actives, supported, maybe = [], [], []
    for respondent in respondents:
        person = _person(respondent)
        tier = champion_tier(response_value(respondent, "L6-Q1"))
        if tier == "active":
            actives.append(person)
        elif tier == "supported":
            supported.append(person)
        elif tier == "maybe":
            maybe.append(person)
    return actives, supported, maybe


def collect_mentors_mentees(respondents):
    mentees, mentors = [], []
    references = Counter()
    for respondent in respondents:
        person = _person(respondent)
        if is_affirmative(response_value(respondent, "L6-Q3")):
            mentees.append(person)
        if is_affirmative(response_value(respondent, "L6-Q4")):
            # Empty topic is rendered with a per-language placeholder
            topic = response_value(respondent, "L6-Q5")
            mentors.append({**person, "topic": topic[:80]})
        reference = response_value(respondent, "L6-Q2")
        if reference and len(reference) > 2 and "[" not in reference:
            references[reference] += 1
    return mentors, mentees, references


def collect_barriers(respondents):
    counts = Counter()
    for respondent in respondents:
        responses = respondent.get("responses", {})
        for option in selected_options(responses, "L7-Q1"):
            if not is_no_barrier_option(option):
                counts[option] += 1
    return counts


def collect_quotes(respondents, qid, max_q=5):
    quotes = []
    for respondent in respondents:
        value = response_value(respondent, qid)
        if value and len(value) > 15 and "[" not in value[:5]:
            quotes.append((value, respondent.get("name", "?")))
    return quotes[:max_q]


def collect_aggregates(respondents):
    topic_counts, topic_attendees = collect_topics(respondents)
    formats, time_per_week, cohort_pref = collect_format_prefs(respondents)
    actives, supported, maybe = collect_champions(respondents)
    mentors, mentees, references = collect_mentors_mentees(respondents)
    return LearningAggregates(
        self_perception=collect_l2_self_perception(respondents),
        priorities=collect_priorities(respondents),
        topic_counts=topic_counts,
        topic_attendees=topic_attendees,
        formats=formats,
        time_per_week=time_per_week,
        cohort_pref=cohort_pref,
        actives=actives,
        supported=supported,
        maybe=maybe,
        mentors=mentors,
        mentees=mentees,
        references=references,
        barriers=collect_barriers(respondents),
        pain_quotes=collect_quotes(respondents, "L7-Q4"),
        workshop_wishes=collect_quotes(respondents, "L7-Q2"),
        speaker_wishes=collect_quotes(respondents, "L7-Q3"),
    )


def append_intro(md, t, respondent_count, date):
    md.extend([
        branding.md_header().rstrip(),
        "",
        t["title"],
        "",
        t["meta"].format(date=date, n=respondent_count),
        t["author"].format(author=branding.META_BAR,
                           contact=f"<{branding.CONTACT}>"),
        "",
    ])


def append_self_perception(md, t, aggregates):
    md.extend([t["self_title"], "", t["self_header"], SEP_7])
    for dimension_id, name in DIMENSION_NAMES.items():
        counts = aggregates.self_perception[dimension_id]
        cells = " | ".join(str(counts.get(level, 0)) for level in LEVELS)
        median = median_level(counts, t["empty"])
        md.append(f"| **{dimension_id}** {name} | {cells} | {median} |")
    md.append("")


def append_champions_summary(md, t, aggregates):
    md.extend(["", t["champ_title"], ""])
    md.append(t["champ_active"].format(n=len(aggregates.actives)))
    md.append(t["champ_supported"].format(n=len(aggregates.supported)))
    md.append(t["champ_maybe"].format(n=len(aggregates.maybe)))
    if aggregates.references:
        md.append(t["champ_refs"])
        for name, count in aggregates.references.most_common(3):
            md.append(t["champ_ref"].format(name=name, count=count))
    md.append("")


def append_quick_wins_summary(md, t, aggregates, respondent_count):
    md.extend([t["qw_title"], ""])
    if aggregates.topic_counts:
        top_topic, top_count = aggregates.topic_counts.most_common(1)[0]
        md.append(t["qw_1"].format(topic=top_topic, count=top_count))
    if aggregates.actives:
        md.append(t["qw_2"].format(n=len(aggregates.actives)))
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        md.append(t["qw_3"].format(barrier=barrier, count=count,
                                   total=respondent_count))
    md.append("")


def append_executive_summary(md, t, aggregates, respondent_count):
    md.extend(["---", "", t["s1"], ""])
    append_self_perception(md, t, aggregates)
    md.extend([t["prio_title"], ""])
    for dimension_id, count in aggregates.priorities.most_common(3):
        md.append(t["prio_row"].format(
            did=dimension_id, name=DIMENSION_NAMES[dimension_id],
            count=count, total=respondent_count,
            pct=safe_pct(count, respondent_count),
        ))
    md.extend(["", t["topics_title"], ""])
    top10 = aggregates.topic_counts.most_common(10)
    for index, (topic, count) in enumerate(top10, 1):
        md.append(t["topic_row"].format(
            i=index, topic=topic, count=count,
            pct=safe_pct(count, respondent_count),
        ))
    append_champions_summary(md, t, aggregates)
    append_quick_wins_summary(md, t, aggregates, respondent_count)


def append_topics_section(md, t, aggregates, respondent_count):
    md.extend(["---", "", t["s2"], ""])
    top10 = aggregates.topic_counts.most_common(10)
    for index, (topic, count) in enumerate(top10, 1):
        md.extend([
            t["s2_topic"].format(i=index, topic=topic, count=count),
            "",
            t["s2_demand"].format(count=count, total=respondent_count,
                                  pct=safe_pct(count, respondent_count)),
            "",
            t["s2_attendees"],
        ])
        for attendee in aggregates.topic_attendees[topic]:
            md.append(f"- {attendee['name']} ({mail(attendee['email'])})")
        md.append("")


def append_cohorts_section(md, t, aggregates):
    md.extend(["---", "", t["s3"], ""])
    for dimension_id, name in DIMENSION_NAMES.items():
        priority_count = aggregates.priorities.get(dimension_id, 0)
        if priority_count == 0:
            continue
        if aggregates.cohort_pref:
            cohort_winning = aggregates.cohort_pref.most_common(1)[0][0]
        else:
            cohort_winning = t["hybrid"]
        md.extend([
            t["cohort"].format(did=dimension_id, name=name),
            t["cohort_count"].format(n=priority_count),
            t["cohort_format"].format(fmt=cohort_winning),
            t["cohort_plan"],
            "",
        ])


def append_people_table(md, rows, header, empty_message=None):
    if rows:
        md.extend([header, SEP_3])
        md.extend(rows)
    elif empty_message:
        md.append(empty_message)
    md.append("")


def _people_rows(people, last_cell):
    return [f"| {p['name']} | {mail(p['email'])} | {last_cell(p)} |"
            for p in people]


def append_champions_section(md, t, aggregates):
    md.extend(["---", "", t["s4"], ""])
    md.append(t["active_title"])
    rows = _people_rows(aggregates.actives, lambda p: t["active_step"])
    append_people_table(md, rows, t["active_header"], t["active_empty"])

    md.append(t["supported_title"])
    rows = _people_rows(aggregates.supported,
                        lambda p: t["supported_step"])
    append_people_table(md, rows, t["supported_header"], t["none"])

    md.append(t["mentor_title"])
    rows = _people_rows(aggregates.mentors,
                        lambda p: p["topic"] or t["unspecified"])
    append_people_table(md, rows, t["mentor_header"])

    md.append(t["mentee_title"])
    if aggregates.mentees:
        md.extend([t["mentee_header"], SEP_2])
        for person in aggregates.mentees:
            md.append(f"| {person['name']} | {mail(person['email'])} |")
    md.append("")


def append_calendar_section(md, t, aggregates):
    md.extend(["---", "", t["s5"], ""])
    md.extend([t["cal_header"], SEP_5])
    champion_count = len(aggregates.actives) + len(aggregates.supported)
    md.append(t["cal_kickoff"].format(n=champion_count))
    champion_name = (aggregates.actives[0]["name"] if aggregates.actives
                     else "TBD")
    top3 = aggregates.topic_counts.most_common(3)
    for week, (topic, count) in enumerate(top3, 2):
        md.append(t["cal_topic"].format(week=week, topic=topic,
                                        count=count,
                                        champion=champion_name))
    md.extend(t["cal_tail"])
    md.append("")


def append_counter_table(md, title, header, counter, respondent_count):
    md.extend([title, header, SEP_3])
    for key, value in counter.most_common():
        pct = safe_pct(value, respondent_count)
        md.append(f"| {key} | {value} | {pct:.0f}% |")
    md.append("")


def append_format_section(md, t, aggregates, respondent_count):
    md.extend(["---", "", t["s6"], ""])
    top_formats = Counter(dict(aggregates.formats.most_common(5)))
    append_counter_table(md, t["fmt_title"], t["fmt_header"],
                         top_formats, respondent_count)
    append_counter_table(md, t["time_title"], t["time_header"],
                         aggregates.time_per_week, respondent_count)
    append_counter_table(md, t["pref_title"], t["pref_header"],
                         aggregates.cohort_pref, respondent_count)


def barrier_action(barrier, t):
    if contains_any(barrier, ["Falta de tempo", "Lack of time",
                              "Falta de tiempo"]):
        return t["act_time"]
    if contains_any(barrier, ["licença Copilot", "Copilot license",
                              "licencia Copilot"]):
        return t["act_license"]
    if contains_any(barrier, ["Champion"]):
        return t["act_champion"]
    if contains_any(barrier, ["por onde começar", "where to start",
                              "por donde empezar"]):
        return t["act_start"]
    return t["act_default"]


def append_barriers_section(md, t, aggregates, respondent_count):
    md.extend(["---", "", t["s7"], ""])
    md.extend([t["bar_header"], SEP_4])
    for barrier, count in aggregates.barriers.most_common(8):
        pct = safe_pct(count, respondent_count)
        action = barrier_action(barrier, t)
        md.append(f"| {barrier} | {count} | {pct:.0f}% | {action} |")
    md.append("")


def append_quote_block(md, t, title, quotes):
    if not quotes:
        return
    md.append(title)
    for quote, name in quotes:
        md.append(t["quote"].format(quote=quote, name=name))
        md.append("")


def append_wishlist_section(md, t, aggregates):
    md.extend(["---", "", t["s8"], ""])
    append_quote_block(md, t, t["wish_workshops"],
                       aggregates.workshop_wishes)
    append_quote_block(md, t, t["wish_speakers"],
                       aggregates.speaker_wishes)
    append_quote_block(md, t, t["wish_other"], aggregates.pain_quotes[:3])


def append_connection_section(md, t, aggregates):
    md.extend(["---", "", t["s9"], "", t["s9_intro"], "",
               t["s9_header"], SEP_4])
    for dimension_id, name in DIMENSION_NAMES.items():
        median = median_level(aggregates.self_perception[dimension_id],
                              t["empty"])
        md.append(t["s9_row"].format(did=dimension_id, name=name,
                                     median=median))
    md.append("")


def ranked_actions(t, aggregates):
    actions = []
    if aggregates.topic_counts:
        topic, count = aggregates.topic_counts.most_common(1)[0]
        actions.append((t["ra_workshop"].format(topic=topic),
                        t["ra_workshop_why"].format(count=count),
                        t["h_30"]))
    if aggregates.actives:
        actions.append(("Champions Kickoff",
                        t["ra_kickoff_why"].format(
                            n=len(aggregates.actives)),
                        t["h_30"]))
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        actions.append((t["ra_barrier"].format(barrier=barrier),
                        t["ra_barrier_why"].format(count=count),
                        t["h_60"]))
    if aggregates.mentors and aggregates.mentees:
        actions.append((t["ra_mentoring"],
                        t["ra_mentoring_why"].format(
                            mentors=len(aggregates.mentors),
                            mentees=len(aggregates.mentees)),
                        t["h_60"]))
    actions.append((t["ra_office"], t["ra_office_why"], t["h_ongoing"]))
    return actions[:5]


def append_actions_section(md, t, aggregates):
    md.extend(["---", "", t["s10"], ""])
    md.extend([t["act_header"], SEP_4])
    actions = ranked_actions(t, aggregates)
    for index, (action, impact, horizon) in enumerate(actions, 1):
        md.append(f"| {index} | {action} | {impact} | {horizon} |")
    md.append("")


def append_30_day_schedule(md, t, aggregates):
    md.extend(["---", "", t["s11"], ""])
    md.extend([t["sch_header"], SEP_2])
    md.append(t["sch_w1"].format(n=len(aggregates.actives)))
    if aggregates.topic_counts:
        topic, count = aggregates.topic_counts.most_common(1)[0]
        md.append(t["sch_w2"].format(topic=topic, count=count))
    md.extend(t["sch_tail"])
    md.append("")


def append_respondents_appendix(md, t, respondents):
    md.extend(["---", "", t["s12"], "", t["s12_warn"], "",
               t["s12_header"], SEP_3])
    for respondent in respondents:
        name = respondent.get("name", "?")
        email = respondent.get("email", "?")
        label = champion_short_label(
            response_value(respondent, "L6-Q1"), t
        )
        md.append(f"| {name} | {mail(email)} | {label} |")
    md.append("")


def build_report(respondents, aggregates, date, lang="en"):
    t = STRINGS[lang]
    respondent_count = len(respondents)
    md = []
    append_intro(md, t, respondent_count, date)
    append_executive_summary(md, t, aggregates, respondent_count)
    append_topics_section(md, t, aggregates, respondent_count)
    append_cohorts_section(md, t, aggregates)
    append_champions_section(md, t, aggregates)
    append_calendar_section(md, t, aggregates)
    append_format_section(md, t, aggregates, respondent_count)
    append_barriers_section(md, t, aggregates, respondent_count)
    append_wishlist_section(md, t, aggregates)
    append_connection_section(md, t, aggregates)
    append_actions_section(md, t, aggregates)
    append_30_day_schedule(md, t, aggregates)
    append_respondents_appendix(md, t, respondents)
    md.extend([
        "---",
        "",
        t["footer"].format(date=date),
        branding.md_footer(lang),
    ])
    return "\n".join(md)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", default=str(KIT / "survey-learning/responses-learning.json")
    )
    parser.add_argument("--out", default=str(KIT / "output"))
    parser.add_argument("--lang", choices=SUPPORTED_LANGS, default="en",
                        help="Report language (default: en)")
    return parser.parse_args()


def load_respondents(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("respondents", [])


def print_summary(t, out_path, respondent_count, aggregates):
    display_path = (out_path.relative_to(KIT)
                    if out_path.is_relative_to(KIT) else out_path)
    print(t["c_done"].format(path=display_path))
    print(t["c_count"].format(n=respondent_count))
    if aggregates.topic_counts:
        print(t["c_topics"])
        top3 = aggregates.topic_counts.most_common(3)
        for index, (topic, count) in enumerate(top3, 1):
            print(t["c_topic"].format(i=index, topic=topic[:60],
                                      count=count))
    print(t["c_champions"].format(a=len(aggregates.actives),
                                  s=len(aggregates.supported),
                                  m=len(aggregates.maybe)))
    print(t["c_mentors"].format(mentors=len(aggregates.mentors),
                                mentees=len(aggregates.mentees)))
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        print(t["c_barrier"].format(barrier=barrier, count=count,
                                    total=respondent_count))


def main():
    args = parse_args()
    t = STRINGS[args.lang]
    input_path = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(t["c_missing"].format(path=input_path))
        return 1

    respondents = load_respondents(input_path)
    respondent_count = len(respondents)
    if respondent_count < 3:
        print(t["c_few"].format(n=respondent_count))

    date = datetime.date.today().isoformat()
    aggregates = collect_aggregates(respondents)
    out_path = out_dir / f"training-plan-{date}.md"
    report = build_report(respondents, aggregates, date, args.lang)
    out_path.write_text(branding.tidy_markdown(report), encoding="utf-8")
    print_summary(t, out_path, respondent_count, aggregates)
    return 0


if __name__ == "__main__":
    sys.exit(main())
