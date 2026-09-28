#!/usr/bin/env python3
"""Generate the Developer Survey insights report.

Reads: survey-devs/respostas-devs.json (output of /importar-survey-devs)
Applies: rubric.py (L0-L4 maturity across 7 dimensions)
Adds: descriptive aggregation (% adoption, top tools, pain points)
Writes:
  - saida/maturidade-developer-survey-<DATE>.json
  - saida/insights-developer-survey-<DATE>.md (full report)

Usage:
    python3 gerar_insights.py
    python3 gerar_insights.py --input X --out Y
    python3 gerar_insights.py --lang pt-br
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "relatorios" / "scripts"))
from rubric import (  # noqa: E402
    DIMENSIONS,
    SUPPORTED_LANGS,
    aggregate_team,
    canonical_responses,
    display_option,
    fold,
    label_for,
    score_respondent,
)
from calcular_maturidade import _ranking  # noqa: E402
import branding  # noqa: E402

SEP_2 = "|---|---|"
SEP_3 = "|---|---|---|"
SEP_4 = "|---|---|---|---|"

STRINGS = {
    "en": {
        "missing": "❌ {path} not found. Run /importar-survey-devs first.",
        "few": "⚠ Only {n} respondents. Insights will be preliminary.",
        "title": "# Developer Survey: Insights Report",
        "meta": "**Date:** {date}  ·  **Respondents:** {n} (anonymous)"
                "  ·  **Rubric version:** 1.0",
        "author": "**Author:** {author}  ·  **Contact:** {contact}",
        "prelim": "> ⚠️ **Preliminary result:** only {n} respondents. "
                  "Consider collecting more answers (15 or more is "
                  "recommended for a representative team view).",
        "s1": "## 1 · Executive Summary",
        "maturity": "### 🎯 Team AI Maturity (deterministic rubric)",
        "overall": "> **Overall: {score} ({label})**",
        "based_on": "> Based on {n} respondents, 7 dimensions, and the "
                    "L0-L4 scale (same as the main assessment)",
        "dim_header": "| Dimension | Score | Label | % devs at L3+L4 |",
        "dim_empty": "| {did} {name} | - | No data | - |",
        "dim_row": "| {did} {name} | **{score:.2f}** | {label} | "
                   "{pct:.0f}% |",
        "strong": "### 🏆 3 strongest dimensions",
        "strong_row": "- **{did}** {name}: score **{score:.2f}** "
                      "({label})",
        "gaps": "### ⚠️ 3 largest gaps (roadmap opportunities)",
        "gap_row": "- 🔴 **{did}** {name}: score **{score:.2f}** "
                   "({label})",
        "ins_policy": "**Critical governance risk:** {pct:.0f}% of devs "
                      "are not aware of a documented AI policy (S8-Q1). "
                      "It needs to be formalized",
        "ins_champion": "**Missing Champions:** {pct:.0f}% of devs have "
                        "no AI Champion on their team (S7-Q2). This is "
                        "an opportunity to build a Champions Network",
        "ins_daily": "**High Copilot adoption:** {pct:.0f}% use it daily "
                     "(S2-Q2). The team is ready to move to advanced "
                     "modes (Agent, Coding Agent, and Spaces)",
        "ins_coding": "**Coding Agent underutilization:** only "
                      "{pct:.0f}% know or use the autonomous Coding "
                      "Agent (S2-Q3). This is an urgent workshop topic",
        "ins_mcp": "**Advanced concepts unknown:** only {pct:.0f}% know "
                   "MCP/A2A. This is a technical skills gap",
        "top_insights": "### 💡 3 key insights",
        "s2": "## 2 · Demographics (S1)",
        "by_role": "### Distribution by role",
        "h_role": "| Role | N | % |",
        "s3": "## 3 · GitHub Copilot: Adoption and Modes (S2)",
        "licenses": "### License coverage (S2-Q1)",
        "h_type": "| Type | N | % |",
        "frequency": "### Usage frequency (S2-Q2)",
        "h_freq": "| Frequency | N | % |",
        "modes": "### 🆕 Copilot Chat modes used (S2-Q3, multi-select)",
        "h_mode": "| Mode | N users | % devs |",
        "features": "### Active features (S2-Q5, multi-select): Top 8",
        "h_feature": "| Feature | N | % devs |",
        "gain": "### Perceived productivity gain (S2-Q7)",
        "h_range": "| Range | N | % |",
        "s4": "## 4 · Other Microsoft / GitHub AI tools (S3)",
        "adoption": "### Adoption (S3-Q1, multi-select)",
        "h_tool_users": "| Tool | N users | % devs |",
        "s5": "## 5 · AI Development Practices (S4)",
        "tdd": "### TDD with AI (S4-Q1)",
        "sdd": "### SDD (Spec-Driven Development) (S4-Q2)",
        "h_knowledge": "| Knowledge | N | % |",
        "s6": "## 6 · Agent Concepts (S5)",
        "by_concept": "### Knowledge by concept",
        "h_concept": "| Concept | Distribution |",
        "mcp_insight": "**Insight:** only {pct:.0f}% know MCP. Most of "
                       "the team does not know the advanced concepts "
                       "(A2A, handoffs, subagents, and personas). This "
                       "is an opportunity for a technical workshop.",
        "s7": "## 7 · Markdown / Memory / Instructions (S6)",
        "instr_files": "### Instructions files used (S6-Q1, multi)",
        "h_file": "| File | N users | % |",
        "s8": "## 8 · Usability and Best Practices (S7)",
        "champions": "### Champions on the team (S7-Q2)",
        "h_answer": "| Answer | N | % |",
        "metrics": "### Productivity metrics (S7-Q4, multi)",
        "h_framework": "| Framework | N | % |",
        "s9": "## 9 · 🔒 Security and Governance (S8)",
        "policy": "### Documented policy (S8-Q1)",
        "no_policy": "> 🚨 **{pct:.0f}% without a clear policy: high "
                     "governance risk.**",
        "sec_tools": "### Active security tools (S8-Q4, multi)",
        "h_tool": "| Tool | N | % |",
        "s10": "## 10 · Pain Points & Wishlist (S9, anonymized)",
        "pains": "### Top frustrations (S9-Q1)",
        "changes": "### Top changes that would double productivity "
                   "(S9-Q2)",
        "wishlist": "### Microsoft/GitHub feature wishlist (S9-Q3)",
        "s11": "## 11 · 🎯 Prioritized Recommendations",
        "rec_policy": "Document a formal AI usage policy",
        "why_policy": "{pct:.0f}% without a policy",
        "rec_coding": "Coding Agent workshop (autonomous on GitHub.com)",
        "why_coding": "only {pct:.0f}% know it",
        "rec_mcp": "Advanced technical training: MCP, A2A, and custom "
                   "agents",
        "why_mcp": "only {pct:.0f}% know MCP",
        "rec_champion": "Build a Champions Network (3-5 devs per team)",
        "why_champion": "{pct:.0f}% without a Champion",
        "h_recs": "| Priority | Action | Rationale |",
        "learning_tip": "> 💡 For a detailed capacitation plan with "
                        "Champions, cohorts, and a calendar, also run "
                        "the **Learning & Growth Survey** "
                        "(`survey-learning/`) and the "
                        "`/plano-capacitacao` skill.",
        "s12": "## 12 · 🔗 Connection with the Maturity Assessment",
        "compare": "If you ran the main assessment, compare:",
        "h_link": "| Survey dimension | v2 assessment questions "
                  "| Validate |",
        "link_rows": {
            "DS-D2": "Declared depth of use vs. the developers' own use",
            "DS-D3": "Breadth of tools in daily use",
            "DS-D4": "Structured practices in daily work",
            "DS-D5": "Advanced knowledge behind the agent practices",
            "DS-D6": "Instructions that are maintained, not set once",
            "DS-D7": "Adoption culture",
            "DS-D8": "Governance in practice",
        },
        "pattern": "> **Look for dissonance:** if the assessment scores "
                   "D4-Q1 at L3 but the Developer Survey shows DS-D2 at "
                   "L1, strategy and practice disagree. Discuss it before "
                   "presenting either result. Survey results never change "
                   "v2 scores.",
        "footer": "_Report generated by the `/insights-developer-survey` "
                  "skill · Deterministic rubric v1.0 · {date}_",
        "c_outputs": "\n✅ Outputs generated:",
        "c_maturity": "\n🎯 Team maturity: {score} ({label}), "
                      "{n} respondents",
        "c_insights": "\n💡 Top insights:",
        "concepts": {
            "S5-Q1": "AI agent",
            "S5-Q3": "Custom agents (.agent.md)",
            "S5-Q4": "Skills (SKILL.md)",
            "S5-Q5": "Prompt files (.prompt.md)",
            "S5-Q6": "A2A protocol",
            "S5-Q9": "Agentic DevOps personas",
        },
    },
    "pt-br": {
        "missing": "❌ {path} não encontrado. Rode /importar-survey-devs "
                   "primeiro.",
        "few": "⚠ Apenas {n} respondentes. Insights serão preliminares.",
        "title": "# Developer Survey: Relatório de Insights",
        "meta": "**Data:** {date}  ·  **Respondentes:** {n} (anônimos)"
                "  ·  **Versão da rubrica:** 1.0",
        "author": "**Autor:** {author}  ·  **Contato:** {contact}",
        "prelim": "> ⚠️ **Resultado preliminar**: apenas {n} "
                  "respondentes. Considere buscar mais respostas "
                  "(recomendado ≥15 para representatividade do time).",
        "s1": "## 1 · Sumário Executivo",
        "maturity": "### 🎯 Maturidade IA do Time (rubrica determinística)",
        "overall": "> **Overall: {score} ({label})**",
        "based_on": "> Baseado em {n} respondentes, 7 dimensões, escala "
                    "L0-L4 (mesma do assessment principal)",
        "dim_header": "| Dimensão | Score | Rótulo | % devs em L3+L4 |",
        "dim_empty": "| {did} {name} | - | Sem dados | - |",
        "dim_row": "| {did} {name} | **{score:.2f}** | {label} | "
                   "{pct:.0f}% |",
        "strong": "### 🏆 3 dimensões mais fortes",
        "strong_row": "- **{did}** {name}: score **{score:.2f}** "
                      "({label})",
        "gaps": "### ⚠️ 3 maiores gaps (oportunidades de roadmap)",
        "gap_row": "- 🔴 **{did}** {name}: score **{score:.2f}** "
                   "({label})",
        "ins_policy": "**Risco de governança crítico:** {pct:.0f}% dos "
                      "devs não conhecem política de IA documentada "
                      "(S8-Q1): precisa formalizar",
        "ins_champion": "**Falta de Champions:** {pct:.0f}% dos devs não "
                        "têm AI Champion no time (S7-Q2): oportunidade "
                        "de criar Champions Network",
        "ins_daily": "**Adoção alta de Copilot:** {pct:.0f}% usa "
                     "diariamente (S2-Q2): pronto para mover para modos "
                     "avançados (Agent, Coding Agent, Spaces)",
        "ins_coding": "**Underutilization de Coding Agent:** apenas "
                      "{pct:.0f}% conhece/usa Coding Agent autônomo "
                      "(S2-Q3): tópico de workshop urgente",
        "ins_mcp": "**Conceitos avançados desconhecidos:** apenas "
                   "{pct:.0f}% conhece MCP/A2A: gap de capacitação "
                   "técnica",
        "top_insights": "### 💡 3 insights principais",
        "s2": "## 2 · Demografia (S1)",
        "by_role": "### Distribuição por cargo",
        "h_role": "| Cargo | N | % |",
        "s3": "## 3 · GitHub Copilot: Adoção e Modos (S2)",
        "licenses": "### Cobertura de licenças (S2-Q1)",
        "h_type": "| Tipo | N | % |",
        "frequency": "### Frequência de uso (S2-Q2)",
        "h_freq": "| Frequência | N | % |",
        "modes": "### 🆕 Modos do Copilot Chat usados (S2-Q3, "
                 "multi-select)",
        "h_mode": "| Modo | N usuários | % devs |",
        "features": "### Features ativas (S2-Q5, multi-select): Top 8",
        "h_feature": "| Feature | N | % devs |",
        "gain": "### Ganho de produtividade percebido (S2-Q7)",
        "h_range": "| Faixa | N | % |",
        "s4": "## 4 · Outras ferramentas Microsoft / GitHub AI (S3)",
        "adoption": "### Adoção (S3-Q1, multi-select)",
        "h_tool_users": "| Ferramenta | N usuários | % devs |",
        "s5": "## 5 · Práticas de Desenvolvimento com IA (S4)",
        "tdd": "### TDD com IA (S4-Q1)",
        "sdd": "### SDD (Spec-Driven Development) (S4-Q2)",
        "h_knowledge": "| Conhecimento | N | % |",
        "s6": "## 6 · Conceitos de Agentes (S5)",
        "by_concept": "### Conhecimento por conceito",
        "h_concept": "| Conceito | Distribuição |",
        "mcp_insight": "**Insight:** apenas {pct:.0f}% conhece MCP: "
                       "conceitos avançados (A2A, handoffs, subagentes, "
                       "personas) são desconhecidos pela maioria. "
                       "Oportunidade de workshop técnico.",
        "s7": "## 7 · Markdown / Memory / Instructions (S6)",
        "instr_files": "### Arquivos de instruções usados (S6-Q1, multi)",
        "h_file": "| Arquivo | N usuários | % |",
        "s8": "## 8 · Usabilidade e Best Practices (S7)",
        "champions": "### Champions no time (S7-Q2)",
        "h_answer": "| Resposta | N | % |",
        "metrics": "### Métricas de produtividade (S7-Q4, multi)",
        "h_framework": "| Framework | N | % |",
        "s9": "## 9 · 🔒 Segurança e Governança (S8)",
        "policy": "### Política documentada (S8-Q1)",
        "no_policy": "> 🚨 **{pct:.0f}% sem política clara: risco de "
                     "governança alto.**",
        "sec_tools": "### Ferramentas de segurança ativas (S8-Q4, multi)",
        "h_tool": "| Ferramenta | N | % |",
        "s10": "## 10 · Pain Points & Wishlist (S9, anonimizadas)",
        "pains": "### Top frustrações (S9-Q1)",
        "changes": "### Top mudanças que dobrariam produtividade (S9-Q2)",
        "wishlist": "### Wishlist de features Microsoft/GitHub (S9-Q3)",
        "s11": "## 11 · 🎯 Recomendações Priorizadas",
        "rec_policy": "Documentar política formal de uso de IA",
        "why_policy": "{pct:.0f}% sem política",
        "rec_coding": "Workshop de Coding Agent (autônomo no GitHub.com)",
        "why_coding": "apenas {pct:.0f}% conhece",
        "rec_mcp": "Treinamento técnico avançado: MCP, A2A, custom agents",
        "why_mcp": "apenas {pct:.0f}% conhece MCP",
        "rec_champion": "Formar Champions Network (3-5 devs por time)",
        "why_champion": "{pct:.0f}% sem Champion",
        "h_recs": "| Prioridade | Ação | Justificativa |",
        "learning_tip": "> 💡 Para plano de capacitação detalhado com "
                        "Champions, cohorts e calendário, rode também o "
                        "**Learning & Growth Survey** (`survey-learning/`)"
                        " e a skill `/plano-capacitacao`.",
        "s12": "## 12 · 🔗 Conexão com Assessment de Maturidade",
        "compare": "Se você rodou o assessment principal, compare:",
        "h_link": "| Dimensão do survey | Perguntas do assessment v2 "
                  "| Validar |",
        "link_rows": {
            "DS-D2": "Profundidade de uso declarada vs. uso real dos devs",
            "DS-D3": "Amplitude de ferramentas no dia a dia",
            "DS-D4": "Práticas estruturadas no trabalho diário",
            "DS-D5": "Conhecimento avançado por trás das práticas com "
                     "agentes",
            "DS-D6": "Instructions mantidas, não criadas uma vez só",
            "DS-D7": "Cultura de adoção",
            "DS-D8": "Governança na prática",
        },
        "pattern": "> **Procure dissonâncias:** se o assessment dá L3 para "
                   "D4-Q1 mas o Developer Survey mostra DS-D2 em L1, "
                   "estratégia e prática discordam. Discuta isso antes de "
                   "apresentar qualquer um dos resultados. O survey nunca "
                   "altera as notas do v2.",
        "footer": "_Relatório gerado pela skill "
                  "`/insights-developer-survey` · Rubrica determinística "
                  "v1.0 · {date}_",
        "c_outputs": "\n✅ Outputs gerados:",
        "c_maturity": "\n🎯 Maturidade do time: {score} ({label}), "
                      "{n} respondentes",
        "c_insights": "\n💡 Top insights:",
        "concepts": {
            "S5-Q1": "AI agent",
            "S5-Q3": "Custom agents (.agent.md)",
            "S5-Q4": "Skills (SKILL.md)",
            "S5-Q5": "Prompt files (.prompt.md)",
            "S5-Q6": "A2A protocol",
            "S5-Q9": "Personas Agentic DevOps",
        },
    },
    "es": {
        "missing": "❌ {path} no encontrado. Ejecuta /importar-survey-devs "
                   "primero.",
        "few": "⚠ Solo {n} encuestados. Los insights serán preliminares.",
        "title": "# Developer Survey: Informe de insights",
        "meta": "**Fecha:** {date}  ·  **Encuestados:** {n} (anónimos)  ·  "
                "**Versión de la rúbrica:** 1.0",
        "author": "**Autor:** {author}  ·  **Contacto:** {contact}",
        "prelim": "> ⚠️ **Resultado preliminar:** solo {n} encuestados. "
                  "Considera recopilar más respuestas (se recomiendan 15 o "
                  "más para una vista representativa del equipo).",
        "s1": "## 1 · Resumen ejecutivo",
        "maturity": "### 🎯 Madurez de IA del equipo (rúbrica determinística)",
        "overall": "> **General: {score} ({label})**",
        "based_on": "> Basado en {n} encuestados, 7 dimensiones y la escala "
                    "L0-L4 (la misma que la evaluación principal)",
        "dim_header": "| Dimensión | Puntaje | Etiqueta | % devs en L3+L4 |",
        "dim_empty": "| {did} {name} | - | Sin datos | - |",
        "dim_row": "| {did} {name} | **{score:.2f}** | {label} | {pct:.0f}% |",
        "strong": "### 🏆 3 dimensiones más fuertes",
        "strong_row": "- **{did}** {name}: puntaje **{score:.2f}** ({label})",
        "gaps": "### ⚠️ 3 brechas más grandes (oportunidades de roadmap)",
        "gap_row": "- 🔴 **{did}** {name}: puntaje **{score:.2f}** ({label})",
        "ins_policy": "**Riesgo crítico de gobernanza:** {pct:.0f}% de los "
                      "devs no conoce una política de IA documentada (S8-Q1). "
                      "Debe formalizarse",
        "ins_champion": "**Faltan Champions:** {pct:.0f}% de los devs no "
                        "tiene un Champion de IA en su equipo (S7-Q2). Esta "
                        "es una oportunidad para crear una Champions Network",
        "ins_daily": "**Alta adopción de Copilot:** {pct:.0f}% lo usa "
                     "diariamente (S2-Q2). El equipo está listo para pasar a "
                     "modos avanzados (Agent, Coding Agent y Spaces)",
        "ins_coding": "**Coding Agent subutilizado:** solo {pct:.0f}% conoce "
                      "o usa el Coding Agent autónomo (S2-Q3). Este es un "
                      "tema urgente de workshop",
        "ins_mcp": "**Conceptos avanzados desconocidos:** solo {pct:.0f}% "
                   "conoce MCP/A2A. Esta es una brecha de habilidades "
                   "técnicas",
        "top_insights": "### 💡 3 insights clave",
        "s2": "## 2 · Demografía (S1)",
        "by_role": "### Distribución por rol",
        "h_role": "| Rol | N | % |",
        "s3": "## 3 · GitHub Copilot: adopción y modos (S2)",
        "licenses": "### Cobertura de licencias (S2-Q1)",
        "h_type": "| Tipo | N | % |",
        "frequency": "### Frecuencia de uso (S2-Q2)",
        "h_freq": "| Frecuencia | N | % |",
        "modes": "### 🆕 Modos de Copilot Chat usados (S2-Q3, selección "
                 "múltiple)",
        "h_mode": "| Modo | N usuarios | % devs |",
        "features": "### Funcionalidades activas (S2-Q5, selección múltiple): "
                    "Top 8",
        "h_feature": "| Funcionalidad | N | % devs |",
        "gain": "### Ganancia de productividad percibida (S2-Q7)",
        "h_range": "| Rango | N | % |",
        "s4": "## 4 · Otras herramientas de IA de Microsoft / GitHub (S3)",
        "adoption": "### Adopción (S3-Q1, selección múltiple)",
        "h_tool_users": "| Herramienta | N usuarios | % devs |",
        "s5": "## 5 · Prácticas de desarrollo con IA (S4)",
        "tdd": "### TDD con IA (S4-Q1)",
        "sdd": "### SDD (Spec-Driven Development) (S4-Q2)",
        "h_knowledge": "| Conocimiento | N | % |",
        "s6": "## 6 · Conceptos de agentes (S5)",
        "by_concept": "### Conocimiento por concepto",
        "h_concept": "| Concepto | Distribución |",
        "mcp_insight": "**Insight:** solo {pct:.0f}% conoce MCP. La mayoría "
                       "del equipo no conoce los conceptos avanzados (A2A, "
                       "handoffs, subagentes y personas). Esta es una "
                       "oportunidad para un workshop técnico.",
        "s7": "## 7 · Markdown / Memory / Instructions (S6)",
        "instr_files": "### Archivos de instrucciones usados (S6-Q1, "
                       "selección múltiple)",
        "h_file": "| Archivo | N usuarios | % |",
        "s8": "## 8 · Usabilidad y buenas prácticas (S7)",
        "champions": "### Champions en el equipo (S7-Q2)",
        "h_answer": "| Respuesta | N | % |",
        "metrics": "### Métricas de productividad (S7-Q4, selección múltiple)",
        "h_framework": "| Framework | N | % |",
        "s9": "## 9 · 🔒 Seguridad y gobernanza (S8)",
        "policy": "### Política documentada (S8-Q1)",
        "no_policy": "> 🚨 **{pct:.0f}% sin una política clara: alto riesgo de "
                     "gobernanza.**",
        "sec_tools": "### Herramientas de seguridad activas (S8-Q4, selección "
                     "múltiple)",
        "h_tool": "| Herramienta | N | % |",
        "s10": "## 10 · Puntos de dolor y wishlist (S9, anonimizado)",
        "pains": "### Principales frustraciones (S9-Q1)",
        "changes": "### Principales cambios que duplicarían la productividad "
                   "(S9-Q2)",
        "wishlist": "### Wishlist de funcionalidades de Microsoft/GitHub "
                    "(S9-Q3)",
        "s11": "## 11 · 🎯 Recomendaciones priorizadas",
        "rec_policy": "Documentar una política formal de uso de IA",
        "why_policy": "{pct:.0f}% sin una política",
        "rec_coding": "Workshop de Coding Agent (autónomo en GitHub.com)",
        "why_coding": "solo {pct:.0f}% lo conoce",
        "rec_mcp": "Capacitación técnica avanzada: MCP, A2A y agentes "
                   "personalizados",
        "why_mcp": "solo {pct:.0f}% conoce MCP",
        "rec_champion": "Crear una Champions Network (3-5 devs por equipo)",
        "why_champion": "{pct:.0f}% sin un Champion",
        "h_recs": "| Prioridad | Acción | Justificación |",
        "learning_tip": "> 💡 Para un plan de capacitación detallado con "
                        "Champions, cohorts y calendario, ejecuta también el "
                        "**Learning & Growth Survey** (`survey-learning/`) y "
                        "la skill `/plano-capacitacao`.",
        "s12": "## 12 · 🔗 Conexión con la evaluación de madurez",
        "compare": "Si ejecutaste la evaluación principal, compara:",
        "h_link": "| Dimensión de la encuesta | Preguntas de la evaluación v2 "
                  "| Validar |",
        "link_rows": {
            "DS-D2": "Profundidad declarada de uso vs. uso propio de los "
                     "desarrolladores",
            "DS-D3": "Amplitud de herramientas en uso diario",
            "DS-D4": "Prácticas estructuradas en el trabajo diario",
            "DS-D5": "Conocimiento avanzado detrás de las prácticas con "
                     "agentes",
            "DS-D6": "Instrucciones que se mantienen, no se configuran una "
                     "sola vez",
            "DS-D7": "Cultura de adopción",
            "DS-D8": "Gobernanza en la práctica",
        },
        "pattern": "> **Busca disonancia:** si la evaluación puntúa D4-Q1 en "
                   "L3 pero el Developer Survey muestra DS-D2 en L1, la "
                   "estrategia y la práctica no coinciden. Discútelo antes de "
                   "presentar cualquiera de los resultados. Los resultados de "
                   "la encuesta nunca cambian los puntajes v2.",
        "footer": "_Informe generado por la skill "
                  "`/insights-developer-survey` · Rúbrica determinística v1.0 "
                  "· {date}_",
        "c_outputs": "\n✅ Outputs generados:",
        "c_maturity": "\n🎯 Madurez del equipo: {score} ({label}), {n} "
                      "encuestados",
        "c_insights": "\n💡 Top insights:",
        "concepts": {
            "S5-Q1": "Agente de IA",
            "S5-Q3": "Agentes personalizados (.agent.md)",
            "S5-Q4": "Skills (SKILL.md)",
            "S5-Q5": "Archivos de prompts (.prompt.md)",
            "S5-Q6": "Protocolo A2A",
            "S5-Q9": "Personas de Agentic DevOps",
        },
    },
}


def safe_pct(num, total):
    return round(100 * num / total, 1) if total > 0 else 0


def aggregate_responses(respondents, qid, multi=False):
    """Counter of options for a given question."""
    counts = Counter()
    total_responses = 0
    for r in respondents:
        ans = r["responses"].get(qid, {}).get("value", "")
        if not ans:
            continue
        if multi:
            for opt in str(ans).split(";"):
                opt = opt.strip()
                if opt:
                    counts[opt] += 1
                    total_responses += 1
        else:
            counts[str(ans).strip()] += 1
            total_responses += 1
    return counts, total_responses


def collect_quotes(respondents, qid, max_q=5):
    """Free-text quotes, anonymized (no respondent_id)."""
    placeholders = ("[texto livre", "[resposta livre")
    quotes = []
    for r in respondents:
        v = r["responses"].get(qid, {}).get("value", "").strip()
        low = v.lower()
        if v and len(v) > 20 and not any(p in low for p in placeholders):
            quotes.append(v)
    return quotes[:max_q]


def bar(pct, width=20):
    filled = int(round(pct * width / 100))
    return "█" * filled + "░" * (width - filled)


def count_folded(counter, *options):
    """Sum the counts of the options, ignoring dashes, case and accents."""
    wanted = {fold(o) for o in options}
    return sum(c for k, c in counter.items() if fold(k) in wanted)


def counter_table(md, title, header, counter, n, limit=None, qid=None,
                  lang="en"):
    md.append(title)
    md.append(header)
    md.append(SEP_3)
    for k, v in counter.most_common(limit):
        label = display_option(qid, k, lang) if qid else k
        md.append(f"| {label} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")


def crosswalk_rows(t, kit):
    """Rows linking each DS-D# dimension to the v2 questions it informs.

    The question lists come from survey_crosswalk in framework.v2.json.
    """
    path = kit / "framework.v2.json"
    crosswalk = {}
    if path.exists():
        crosswalk = json.loads(path.read_text("utf-8")).get(
            "survey_crosswalk", {})
    rows = []
    for did, name, _, _ in DIMENSIONS:
        qids = ", ".join(crosswalk.get(did, [])) or "-"
        rows.append(f"| **{did}** {name} | {qids} | "
                    f"{t['link_rows'].get(did, '')} |")
    return rows


def section(md, heading):
    md.extend(["---", "", heading, ""])


def _display(path, kit):
    return path.relative_to(kit) if path.is_relative_to(kit) else path


def main():
    ap = argparse.ArgumentParser()
    kit = SCRIPT_DIR.parent.parent
    ap.add_argument("--input",
                    default=str(kit / "survey-devs/respostas-devs.json"))
    ap.add_argument("--out", default=str(kit / "saida"))
    ap.add_argument("--lang", choices=SUPPORTED_LANGS, default="en",
                    help="Report language (default: en)")
    args = ap.parse_args()
    lang = args.lang
    t = STRINGS[lang]

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(t["missing"].format(path=inp))
        return 1

    data = json.loads(inp.read_text(encoding="utf-8"))
    # Answers from the EN or ES Forms (or older PT Forms) are mapped to the
    # canonical options first; tables show them in the report language.
    respondents = [{**r, "responses": canonical_responses(
        r.get("responses", {}))} for r in data.get("respondents", [])]
    n = len(respondents)
    date = datetime.date.today().isoformat()

    if n < 3:
        print(t["few"].format(n=n))

    # Maturity per respondent + team aggregate
    individual_scores = [
        score_respondent(r["responses"], lang) for r in respondents
    ]
    team = aggregate_team(individual_scores, lang)

    # Same schema as calcular_maturidade.py output
    maturity_path = out_dir / f"maturidade-developer-survey-{date}.json"
    maturity_data = {
        "metadata": {
            "computed_at": datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": str(inp.name),
            "n_respondents": n,
            "rubric_version": "1.0 (deterministic)",
            "anonymous": True,
            "scope": "team aggregate (no individual scores in output)",
            "lang": lang,
            **branding.json_metadata(),
        },
        "team_overall": {
            "score": team["team_overall_score"],
            "label": team["team_overall_label"],
            "respondents_with_overall": team["n_with_overall"],
        },
        "dimensions": team["dimensions"],
        "ranking": _ranking(team["dimensions"]),
    }
    maturity_path.write_text(
        json.dumps(maturity_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Descriptive aggregations used in the report
    agg = aggregate_responses
    s2_q1 = agg(respondents, "S2-Q1")[0]                # license
    s2_q2 = agg(respondents, "S2-Q2")[0]                # frequency
    s2_q3, _ = agg(respondents, "S2-Q3", multi=True)    # modes
    s2_q5, _ = agg(respondents, "S2-Q5", multi=True)    # features
    s2_q7 = agg(respondents, "S2-Q7")[0]                # gain
    s3_q1, _ = agg(respondents, "S3-Q1", multi=True)    # MS/GH tools
    s4_q1 = agg(respondents, "S4-Q1")[0]                # TDD
    s4_q2 = agg(respondents, "S4-Q2")[0]                # SDD

    # S5: knowledge of agent concepts
    s5_concepts = {
        qid: (name, agg(respondents, qid)[0])
        for qid, name in t["concepts"].items()
    }

    s6_q1, _ = agg(respondents, "S6-Q1", multi=True)    # instructions
    s7_q2 = agg(respondents, "S7-Q2")[0]                # Champion?
    s7_q4, _ = agg(respondents, "S7-Q4", multi=True)    # metrics
    s8_q1 = agg(respondents, "S8-Q1")[0]                # AI policy
    s8_q4, _ = agg(respondents, "S8-Q4", multi=True)    # security tools

    s9_pain = collect_quotes(respondents, "S9-Q1")
    s9_change = collect_quotes(respondents, "S9-Q2")
    s9_wishlist = collect_quotes(respondents, "S9-Q3")

    # Threshold checks; match strings are the Portuguese form options
    no_policy = sum(
        c for k, c in s8_q1.items()
        if fold("Não temos política") in fold(k) or fold("Não sei") in fold(k)
    )
    pct_no_policy = safe_pct(no_policy, n)

    no_champion = count_folded(s7_q2, "Não, cada um se vira",
                               "Não, mas precisava ter")
    pct_no_champion = safe_pct(no_champion, n)

    daily_copilot = count_folded(s2_q2, "Diariamente (várias horas)",
                                 "Diariamente (esporádico)")
    pct_daily = safe_pct(daily_copilot, n)

    uses_coding_agent = sum(
        c for k, c in s2_q3.items() if "Coding Agent" in k
    )
    pct_coding_agent = safe_pct(uses_coding_agent, n)

    a2a = s5_concepts["S5-Q6"][1]
    knows_mcp_strong = count_folded(a2a, "Uso (ex.: Foundry A2A Tool)",
                                    "Conheço o conceito")
    pct_mcp = safe_pct(knows_mcp_strong, n)

    # Build report
    md = []
    md.append(branding.md_header().rstrip())
    md.append("")
    md.append(t["title"])
    md.append("")
    md.append(t["meta"].format(date=date, n=n))
    md.append(t["author"].format(author=branding.META_BAR,
                                 contact=f"<{branding.CONTACT}>"))
    md.append("")

    if n < 5:
        md.append(t["prelim"].format(n=n))
        md.append("")

    section(md, t["s1"])

    overall = team["team_overall_score"]
    overall_str = f"{overall:.2f}" if overall is not None else "N/A"
    md.append(t["maturity"])
    md.append("")
    md.append(t["overall"].format(score=overall_str,
                                  label=team["team_overall_label"]))
    md.append(t["based_on"].format(n=n))
    md.append("")
    md.append(t["dim_header"])
    md.append(SEP_4)
    for did, name, _, _ in DIMENSIONS:
        d = team["dimensions"][did]
        if d["team_score"] is None:
            md.append(t["dim_empty"].format(did=did, name=name))
            continue
        dist = d["distribution_pct"]
        pct_l3l4 = dist["L3"] + dist["L4"]
        md.append(t["dim_row"].format(
            did=did, name=name, score=d["team_score"],
            label=d["label"], pct=pct_l3l4,
        ))
    md.append("")

    rk = _ranking(team["dimensions"])
    md.append(t["strong"])
    for did, name, score in rk["top"]:
        md.append(t["strong_row"].format(
            did=did, name=name, score=score, label=label_for(score, lang)
        ))
    md.append("")
    md.append(t["gaps"])
    for did, name, score in rk["bottom"]:
        md.append(t["gap_row"].format(
            did=did, name=name, score=score, label=label_for(score, lang)
        ))
    md.append("")

    insights = []
    if pct_no_policy > 30:
        insights.append(t["ins_policy"].format(pct=pct_no_policy))
    if pct_no_champion > 50:
        insights.append(t["ins_champion"].format(pct=pct_no_champion))
    if pct_daily > 70:
        insights.append(t["ins_daily"].format(pct=pct_daily))
    if pct_coding_agent < 30:
        insights.append(t["ins_coding"].format(pct=pct_coding_agent))
    if pct_mcp < 20:
        insights.append(t["ins_mcp"].format(pct=pct_mcp))

    md.append(t["top_insights"])
    for i, ins in enumerate(insights[:3], 1):
        md.append(f"{i}. {ins}")
    md.append("")

    section(md, t["s2"])
    s1_q1 = agg(respondents, "S1-Q1")[0]
    counter_table(md, t["by_role"], t["h_role"], s1_q1, n, limit=10,
                  qid="S1-Q1", lang=lang)

    section(md, t["s3"])
    counter_table(md, t["licenses"], t["h_type"], s2_q1, n,
                  qid="S2-Q1", lang=lang)
    counter_table(md, t["frequency"], t["h_freq"], s2_q2, n,
                  qid="S2-Q2", lang=lang)
    counter_table(md, t["modes"], t["h_mode"], s2_q3, n,
                  qid="S2-Q3", lang=lang)
    counter_table(md, t["features"], t["h_feature"], s2_q5, n, limit=8,
                  qid="S2-Q5", lang=lang)
    counter_table(md, t["gain"], t["h_range"], s2_q7, n,
                  qid="S2-Q7", lang=lang)

    section(md, t["s4"])
    counter_table(md, t["adoption"], t["h_tool_users"], s3_q1, n,
                  qid="S3-Q1", lang=lang)

    section(md, t["s5"])
    counter_table(md, t["tdd"], t["h_freq"], s4_q1, n,
                  qid="S4-Q1", lang=lang)
    counter_table(md, t["sdd"], t["h_knowledge"], s4_q2, n,
                  qid="S4-Q2", lang=lang)

    section(md, t["s6"])
    md.append(t["by_concept"])
    md.append(t["h_concept"])
    md.append(SEP_2)
    for qid, (name, counts) in s5_concepts.items():
        top = ", ".join(f"{display_option(qid, k, lang)}={v}"
                        for k, v in counts.most_common(3))
        md.append(f"| **{qid}** {name} | {top} |")
    md.append("")
    md.append(t["mcp_insight"].format(pct=pct_mcp))
    md.append("")

    section(md, t["s7"])
    counter_table(md, t["instr_files"], t["h_file"], s6_q1, n,
                  qid="S6-Q1", lang=lang)

    section(md, t["s8"])
    counter_table(md, t["champions"], t["h_answer"], s7_q2, n,
                  qid="S7-Q2", lang=lang)
    counter_table(md, t["metrics"], t["h_framework"], s7_q4, n,
                  qid="S7-Q4", lang=lang)

    section(md, t["s9"])
    md.append(t["policy"])
    md.append(t["h_answer"])
    md.append(SEP_3)
    for k, v in s8_q1.most_common():
        md.append(f"| {display_option('S8-Q1', k, lang)} | {v} | "
                  f"{safe_pct(v, n):.0f}% |")
    if pct_no_policy > 30:
        md.append("")
        md.append(t["no_policy"].format(pct=pct_no_policy))
    md.append("")
    counter_table(md, t["sec_tools"], t["h_tool"], s8_q4, n,
                  qid="S8-Q4", lang=lang)

    section(md, t["s10"])
    for key, quotes in (("pains", s9_pain), ("changes", s9_change),
                        ("wishlist", s9_wishlist)):
        if quotes:
            md.append(t[key])
            for q in quotes:
                md.append(f"> {q}")
                md.append("")

    section(md, t["s11"])
    recs = []
    if pct_no_policy > 30:
        recs.append(("🔴 P0", t["rec_policy"],
                     t["why_policy"].format(pct=pct_no_policy)))
    if pct_coding_agent < 30:
        recs.append(("🟠 P1", t["rec_coding"],
                     t["why_coding"].format(pct=pct_coding_agent)))
    if pct_mcp < 20:
        recs.append(("🟠 P1", t["rec_mcp"],
                     t["why_mcp"].format(pct=pct_mcp)))
    if pct_no_champion > 50:
        recs.append(("🟡 P2", t["rec_champion"],
                     t["why_champion"].format(pct=pct_no_champion)))

    md.append(t["h_recs"])
    md.append(SEP_3)
    for pri, action, why in recs[:5]:
        md.append(f"| {pri} | {action} | {why} |")
    md.append("")
    md.append(t["learning_tip"])
    md.append("")

    section(md, t["s12"])
    md.append(t["compare"])
    md.append("")
    md.append(t["h_link"])
    md.append(SEP_3)
    md.extend(crosswalk_rows(t, kit))
    md.append("")
    md.append(t["pattern"])
    md.append("")

    md.append("---")
    md.append("")
    md.append(t["footer"].format(date=date))
    md.append(branding.md_footer(lang))

    insights_path = out_dir / f"insights-developer-survey-{date}.md"
    insights_path.write_text(branding.tidy_markdown("\n".join(md)),
                             encoding="utf-8")

    print(t["c_outputs"])
    print(f"   📊 {_display(maturity_path, kit)}")
    print(f"   📄 {_display(insights_path, kit)}")
    print(t["c_maturity"].format(score=overall_str,
                                 label=team["team_overall_label"], n=n))
    print(t["c_insights"])
    for i, ins in enumerate(insights[:3], 1):
        short = ins.split("**")[1] if "**" in ins else ins[:50]
        print(f"   {i}. {short}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
