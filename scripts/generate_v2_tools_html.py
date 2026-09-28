#!/usr/bin/env python3
"""Generate the v2 helper pages from framework.v2.json.

Writes, from one source and in three languages (EN, PT-BR, ES):

- wizard/implementation-guide-wizard.html (+ .pt-br.html)
  Collects the implementation guide inputs (governance, dimension
  owners, change management, risks, first 90 days) and exports
  implementation-guide-inputs.json for relatorios/scripts.
- wizard/implementation-guide-inputs.template.json
  The same fields for manual editing, with guidance in _guide and
  empty values, so no example text reaches a client report.
- referencia/calculadora-pontuacao.html (+ .pt-br.html)
  What-if calculator for section 8 of the v2 spec: dimension scores,
  weights and targets give the overall score, level, gaps, priorities,
  horizons, amplification risk and the recommended strategies.

The base file picks the browser language (or ?lang=); the .pt-br copy
opens in Portuguese. Both run offline and send nothing over the network.

Usage:
    python3 scripts/generate_v2_tools_html.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MS_LOGO = (
    '<svg viewBox="0 0 23 23" width="18" height="18" role="img" '
    'aria-label="Microsoft"><rect x="1" y="1" width="10" height="10" '
    'fill="#F25022"/><rect x="12" y="1" width="10" height="10" '
    'fill="#7FBA00"/><rect x="1" y="12" width="10" height="10" '
    'fill="#00A4EF"/><rect x="12" y="12" width="10" height="10" '
    'fill="#FFB900"/></svg>'
)
BRAND = "Paula Silva | Global Developer Solutions Advisor"
CSS = """
:root{--primary:#0078D4;--ink:#1b1b1f;--muted:#5b5b66;--line:#e3e3e8;
--bg:#f7f7f9;--ok:#107c10;--warn:#f7b500;--crit:#d13438}
*{box-sizing:border-box}body{margin:0;font-family:"Segoe UI",system-ui,
sans-serif;color:var(--ink);background:var(--bg);line-height:1.45}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid
var(--line);padding:10px 16px;z-index:5}
.bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;
max-width:980px;margin:0 auto}
.brand{display:flex;gap:8px;align-items:center;font-size:13px;
color:var(--muted)}.grow{flex:1}
main{max-width:980px;margin:0 auto;padding:16px}
section{background:#fff;border:1px solid var(--line);border-radius:8px;
padding:16px;margin:16px 0}
h1{font-size:22px;margin:8px 0}h2{font-size:18px;margin:0 0 6px}
.note{font-size:12px;color:var(--muted)}
textarea{width:100%;font:inherit;border:1px solid var(--line);
border-radius:4px;padding:8px}
input[type=number]{width:5.5em;font:inherit;padding:4px;border:1px solid
var(--line);border-radius:4px}
button,select{font:inherit;padding:6px 12px;border-radius:4px;border:1px
solid var(--primary);background:#fff;color:var(--primary);cursor:pointer}
button.primary{background:var(--primary);color:#fff}
button:disabled{opacity:.4;cursor:default}
table{border-collapse:collapse;width:100%;background:#fff;font-size:14px}
td,th{border:1px solid var(--line);padding:4px 8px;text-align:left;
vertical-align:top}th{background:var(--bg)}td.num{text-align:right}
.steps{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.steps button{font-size:12px;padding:3px 8px}
.steps button.done{border-color:var(--ok);color:var(--ok)}
.steps button.on{background:var(--primary);color:#fff}
.flag{color:var(--crit);font-weight:600}.ok{color:var(--ok)}
footer{max-width:980px;margin:0 auto;padding:16px;font-size:12px;
color:var(--muted)}
"""

WIZARD_KEYS = (
    "executive_steering_committee", "tpo", "dimension_owners",
    "raci_matrix", "communication_plan", "training_plan", "adkar_notes",
    "risk_register", "quick_wins_w1_4", "quick_wins_w5_8",
    "quick_wins_w9_12",
)

WIZARD = {
    "en": {
        "title": "Implementation guide wizard",
        "intro": "Your answers feed the implementation guide PDF "
                 "(v2_implementation_guide.pdf). Fields you leave empty "
                 "appear as \"to fill with the client\"; the report never "
                 "invents them.",
        "privacy": "Privacy: this page sends nothing over the network. "
                   "Names you type are personal data; share the exported "
                   "file only with the engagement team.",
        "step": "Step {n} of {total}", "prev": "Back", "next": "Next",
        "review": "Review", "export": "Export implementation-guide-"
        "inputs.json", "reset": "Clear all",
        "confirm": "Delete all inputs in this wizard?",
        "complete": "complete", "chars": "characters",
        "preview": "All inputs", "empty": "empty",
        "next_step": "Next: save the file in the kit root and run make "
                     "pipeline.",
        "steps": [
            ("Steering committee", "Sponsor, program lead, finance, "
             "security and change lead. One person per line: name: role.",
             "[Name]: CTO (executive sponsor)\n[Name]: VP Engineering "
             "(program lead)\n[Name]: CISO (security)\n[Name]: Finance "
             "(investment approval)"),
            ("Program office", "Program manager on the first line, then "
             "the members with their role, one per line.",
             "[Name]: program manager\n[Name]: lead architect\n[Name]: "
             "change manager"),
            ("Dimension owners", "One accountable owner for each "
             "dimension below target, one per line: D#: name, role.",
             "D5: [Name], QA lead\nD6: [Name], AppSec lead\nD8: [Name], "
             "platform lead"),
            ("RACI", "Markdown table: Activity | R | A | C | I.",
             "| Activity | R | A | C | I |\n|---|---|---|---|---|\n"
             "| Approve targets | Program office | Sponsor | Dimension "
             "owners | Engineering |"),
            ("Communication plan", "Markdown table: Audience | Channel "
             "| Frequency | Owner.",
             "| Audience | Channel | Frequency | Owner |\n"
             "|---|---|---|---|\n| All engineering | Town hall | "
             "Quarterly | Change manager |"),
            ("Enablement and training plan", "Markdown table: Audience | "
             "Format | Cadence. Build cohorts from the Learning and Growth "
             "Survey and track them in D2.",
             "| Audience | Format | Cadence |\n|---|---|---|\n| All "
             "developers | Hands-on workshop | Monthly cohorts |"),
            ("ADKAR plan", "One paragraph per stage: Awareness, Desire, "
             "Knowledge, Ability, Reinforcement.",
             "**Awareness:** ...\n\n**Desire:** ...\n\n**Knowledge:** ..."
             "\n\n**Ability:** ...\n\n**Reinforcement:** ..."),
            ("Client risk register", "Markdown table: Risk | Impact | "
             "Mitigation | Owner. The report adds the risks raised by the "
             "scoring flags.",
             "| Risk | Impact | Mitigation | Owner |\n|---|---|---|---|\n"
             "| [Risk] | High | [Mitigation] | [Name] |"),
            ("First 90 days: weeks 1 to 4", "Small, visible actions for "
             "the first month. One per line.",
             "1. [Action] (W1)\n2. [Action] (W3)"),
            ("First 90 days: weeks 5 to 8", "Second wave. One per line.",
             "1. [Action] (W5)\n2. [Action] (W8)"),
            ("First 90 days: weeks 9 to 12", "Consolidate before the next "
             "horizon. One per line.",
             "1. [Action] (W10)\n2. Re-assess and compare rounds (W12)"),
        ],
    },
    "pt-br": {
        "title": "Wizard do guia de implementação",
        "intro": "Suas respostas alimentam o PDF do guia de implementação "
                 "(v2_implementation_guide.pdf). Campos vazios aparecem "
                 "como \"a preencher com o cliente\"; o relatório nunca "
                 "os inventa.",
        "privacy": "Privacidade: esta página não envia nada pela rede. "
                   "Nomes digitados são dados pessoais; compartilhe o "
                   "arquivo exportado apenas com a equipe do projeto.",
        "step": "Passo {n} de {total}", "prev": "Voltar",
        "next": "Avançar", "review": "Revisar",
        "export": "Exportar implementation-guide-inputs.json",
        "reset": "Limpar tudo",
        "confirm": "Apagar todas as entradas deste wizard?",
        "complete": "preenchido", "chars": "caracteres",
        "preview": "Todas as entradas", "empty": "vazio",
        "next_step": "Próximo passo: salve o arquivo na raiz do kit e "
                     "rode make pipeline.",
        "steps": [
            ("Comitê diretivo", "Patrocinador, líder do programa, "
             "finanças, segurança e gestão da mudança. Uma pessoa por "
             "linha: nome: papel.",
             "[Nome]: CTO (patrocinador executivo)\n[Nome]: VP de "
             "Engenharia (líder do programa)\n[Nome]: CISO (segurança)\n"
             "[Nome]: Finanças (aprovação de investimento)"),
            ("Escritório do programa", "Gerente do programa na primeira "
             "linha e, depois, os membros com o papel, um por linha.",
             "[Nome]: gerente do programa\n[Nome]: arquiteto líder\n"
             "[Nome]: gestor da mudança"),
            ("Responsáveis por dimensão", "Um responsável para cada "
             "dimensão abaixo da meta, um por linha: D#: nome, papel.",
             "D5: [Nome], líder de QA\nD6: [Nome], líder de AppSec\n"
             "D8: [Nome], líder de plataforma"),
            ("RACI", "Tabela Markdown: Atividade | R | A | C | I.",
             "| Atividade | R | A | C | I |\n|---|---|---|---|---|\n"
             "| Aprovar metas | Escritório do programa | Patrocinador | "
             "Responsáveis por dimensão | Engenharia |"),
            ("Plano de comunicação", "Tabela Markdown: Público | Canal | "
             "Frequência | Responsável.",
             "| Público | Canal | Frequência | Responsável |\n"
             "|---|---|---|---|\n| Toda a engenharia | Town hall | "
             "Trimestral | Gestor da mudança |"),
            ("Plano de capacitação", "Tabela Markdown: Público | Formato | "
             "Cadência. Monte as turmas a partir do Learning and Growth "
             "Survey e acompanhe-as em D2.",
             "| Público | Formato | Cadência |\n|---|---|---|\n| Todos os "
             "devs | Workshop prático | Turmas mensais |"),
            ("Plano ADKAR", "Um parágrafo por etapa: Consciência, Desejo, "
             "Conhecimento, Habilidade, Reforço.",
             "**Consciência:** ...\n\n**Desejo:** ...\n\n**Conhecimento:**"
             " ...\n\n**Habilidade:** ...\n\n**Reforço:** ..."),
            ("Registro de riscos do cliente", "Tabela Markdown: Risco | "
             "Impacto | Mitigação | Responsável. O relatório acrescenta os "
             "riscos apontados pelas regras de pontuação.",
             "| Risco | Impacto | Mitigação | Responsável |\n"
             "|---|---|---|---|\n| [Risco] | Alto | [Mitigação] | "
             "[Nome] |"),
            ("Primeiros 90 dias: semanas 1 a 4", "Ações pequenas e "
             "visíveis no primeiro mês. Uma por linha.",
             "1. [Ação] (S1)\n2. [Ação] (S3)"),
            ("Primeiros 90 dias: semanas 5 a 8", "Segunda onda. Uma por "
             "linha.", "1. [Ação] (S5)\n2. [Ação] (S8)"),
            ("Primeiros 90 dias: semanas 9 a 12", "Consolidar antes do "
             "próximo horizonte. Uma por linha.",
             "1. [Ação] (S10)\n2. Reavaliar e comparar rodadas (S12)"),
        ],
    },
    "es": {
        "title": "Wizard de la guía de implementación",
        "intro": "Tus respuestas alimentan el PDF de la guía de "
                 "implementación (v2_implementation_guide.pdf). Los campos "
                 "vacíos aparecen como \"a completar con el cliente\"; el "
                 "informe nunca los inventa.",
        "privacy": "Privacidad: esta página no envía nada por la red. Los "
                   "nombres que escribas son datos personales; comparte el "
                   "archivo exportado solo con el equipo del proyecto.",
        "step": "Paso {n} de {total}", "prev": "Atrás",
        "next": "Siguiente", "review": "Revisar",
        "export": "Exportar implementation-guide-inputs.json",
        "reset": "Borrar todo",
        "confirm": "¿Borrar todas las entradas de este wizard?",
        "complete": "completo", "chars": "caracteres",
        "preview": "Todas las entradas", "empty": "vacío",
        "next_step": "Siguiente paso: guarda el archivo en la raíz del kit "
                     "y ejecuta make pipeline.",
        "steps": [
            ("Comité directivo", "Patrocinador, líder del programa, "
             "finanzas, seguridad y gestión del cambio. Una persona por "
             "línea: nombre: rol.",
             "[Nombre]: CTO (patrocinador ejecutivo)\n[Nombre]: VP de "
             "Ingeniería (líder del programa)\n[Nombre]: CISO "
             "(seguridad)\n[Nombre]: Finanzas (aprobación de inversión)"),
            ("Oficina del programa", "Gerente del programa en la primera "
             "línea y luego los miembros con su rol, uno por línea.",
             "[Nombre]: gerente del programa\n[Nombre]: arquitecto "
             "líder\n[Nombre]: gestor del cambio"),
            ("Responsables por dimensión", "Una persona responsable por "
             "cada dimensión bajo el objetivo, una por línea: D#: nombre, "
             "rol.",
             "D5: [Nombre], líder de QA\nD6: [Nombre], líder de AppSec\n"
             "D8: [Nombre], líder de plataforma"),
            ("RACI", "Tabla Markdown: Actividad | R | A | C | I.",
             "| Actividad | R | A | C | I |\n|---|---|---|---|---|\n"
             "| Aprobar objetivos | Oficina del programa | Patrocinador | "
             "Responsables por dimensión | Ingeniería |"),
            ("Plan de comunicación", "Tabla Markdown: Audiencia | Canal | "
             "Frecuencia | Responsable.",
             "| Audiencia | Canal | Frecuencia | Responsable |\n"
             "|---|---|---|---|\n| Toda la ingeniería | Town hall | "
             "Trimestral | Gestor del cambio |"),
            ("Plan de capacitación", "Tabla Markdown: Audiencia | Formato "
             "| Cadencia. Arma los grupos a partir del Learning and Growth "
             "Survey y dales seguimiento en D2.",
             "| Audiencia | Formato | Cadencia |\n|---|---|---|\n| Todos "
             "los devs | Taller práctico | Grupos mensuales |"),
            ("Plan ADKAR", "Un párrafo por etapa: Conciencia, Deseo, "
             "Conocimiento, Habilidad, Refuerzo.",
             "**Conciencia:** ...\n\n**Deseo:** ...\n\n**Conocimiento:** "
             "...\n\n**Habilidad:** ...\n\n**Refuerzo:** ..."),
            ("Registro de riesgos del cliente", "Tabla Markdown: Riesgo | "
             "Impacto | Mitigación | Responsable. El informe agrega los "
             "riesgos señalados por las reglas de puntaje.",
             "| Riesgo | Impacto | Mitigación | Responsable |\n"
             "|---|---|---|---|\n| [Riesgo] | Alto | [Mitigación] | "
             "[Nombre] |"),
            ("Primeros 90 días: semanas 1 a 4", "Acciones pequeñas y "
             "visibles en el primer mes. Una por línea.",
             "1. [Acción] (S1)\n2. [Acción] (S3)"),
            ("Primeros 90 días: semanas 5 a 8", "Segunda ola. Una por "
             "línea.", "1. [Acción] (S5)\n2. [Acción] (S8)"),
            ("Primeros 90 días: semanas 9 a 12", "Consolidar antes del "
             "siguiente horizonte. Una por línea.",
             "1. [Acción] (S10)\n2. Reevaluar y comparar rondas (S12)"),
        ],
    },
}

CALC_UI = {
    "en": {
        "title": "Scoring calculator (framework v2)",
        "intro": "What-if view of the v2 scoring rules (spec section 8). "
                 "Enter dimension scores, or load saida/scores.json, then "
                 "change weights and targets to see how the overall "
                 "score, priorities and strategies move. The official "
                 "result comes from scripts/assessment_engine.py.",
        "load": "Load scores.json", "reset": "Reset",
        "dimension": "Dimension", "score": "Score", "weight": "Weight",
        "target": "Target", "level": "Level", "gap": "Gap",
        "priority_score": "Weight × gap", "priority": "Priority",
        "horizon": "Horizon", "overall": "Overall",
        "amplification": "Amplification risk",
        "amp_none": "not flagged",
        "amp_why": "D5, D6 or D8 is at least one band below the overall "
                   "band.",
        "strategies": "Strategies",
        "strategy": "Strategy", "cumulative": "Cumulative priority",
        "recommended": "Recommended", "yes": "yes", "no": "no",
        "rules": "Rules: overall = weighted mean of the dimensions with "
                 "a score; bands are half-open; gap = target - score; "
                 "priority = weight × gap (P0 from 2.4, P1 from 1.6, P2 "
                 "from 0.9, else P3); a strategy is recommended when the "
                 "priorities of its dimensions add up to at least 0.9.",
        "bad_file": "This file has no v2 dimension scores.",
        "horizons": ["30 days", "Next quarter", "Semester",
                     "Backlog / monitor"],
        "no_score": "No score",
    },
    "pt-br": {
        "title": "Calculadora de pontuação (framework v2)",
        "intro": "Simulação das regras de pontuação v2 (seção 8 da "
                 "especificação). Informe as notas por dimensão, ou "
                 "carregue saida/scores.json, e altere pesos e metas para "
                 "ver como mudam a nota geral, as prioridades e as "
                 "estratégias. O resultado oficial vem de "
                 "scripts/assessment_engine.py.",
        "load": "Carregar scores.json", "reset": "Restaurar",
        "dimension": "Dimensão", "score": "Nota", "weight": "Peso",
        "target": "Meta", "level": "Nível", "gap": "Gap",
        "priority_score": "Peso × gap", "priority": "Prioridade",
        "horizon": "Horizonte", "overall": "Geral",
        "amplification": "Risco de amplificação",
        "amp_none": "não sinalizado",
        "amp_why": "D5, D6 ou D8 está pelo menos uma faixa abaixo da faixa "
                   "geral.",
        "strategies": "Estratégias",
        "strategy": "Estratégia", "cumulative": "Prioridade acumulada",
        "recommended": "Recomendada", "yes": "sim", "no": "não",
        "rules": "Regras: geral = média ponderada das dimensões com nota; "
                 "faixas semiabertas; gap = meta - nota; prioridade = peso "
                 "× gap (P0 a partir de 2,4, P1 a partir de 1,6, P2 a "
                 "partir de 0,9, senão P3); uma estratégia é recomendada "
                 "quando as prioridades das suas dimensões somam pelo "
                 "menos 0,9.",
        "bad_file": "Este arquivo não tem notas de dimensão v2.",
        "horizons": ["30 dias", "Próximo trimestre", "Semestre",
                     "Backlog / monitorar"],
        "no_score": "Sem nota",
    },
    "es": {
        "title": "Calculadora de puntaje (framework v2)",
        "intro": "Simulación de las reglas de puntaje v2 (sección 8 de la "
                 "especificación). Ingresa los puntajes por dimensión, o "
                 "carga saida/scores.json, y cambia pesos y objetivos para "
                 "ver cómo se mueven el puntaje general, las prioridades y "
                 "las estrategias. El resultado oficial viene de "
                 "scripts/assessment_engine.py.",
        "load": "Cargar scores.json", "reset": "Restablecer",
        "dimension": "Dimensión", "score": "Puntaje", "weight": "Peso",
        "target": "Objetivo", "level": "Nivel", "gap": "Brecha",
        "priority_score": "Peso × brecha", "priority": "Prioridad",
        "horizon": "Horizonte", "overall": "General",
        "amplification": "Riesgo de amplificación",
        "amp_none": "sin señal",
        "amp_why": "D5, D6 o D8 está al menos una banda por debajo de la "
                   "banda general.",
        "strategies": "Estrategias",
        "strategy": "Estrategia", "cumulative": "Prioridad acumulada",
        "recommended": "Recomendada", "yes": "sí", "no": "no",
        "rules": "Reglas: general = media ponderada de las dimensiones con "
                 "puntaje; bandas semiabiertas; brecha = objetivo - "
                 "puntaje; prioridad = peso × brecha (P0 desde 2,4, P1 "
                 "desde 1,6, P2 desde 0,9, si no P3); una estrategia se "
                 "recomienda cuando las prioridades de sus dimensiones "
                 "suman al menos 0,9.",
        "bad_file": "Este archivo no tiene puntajes de dimensión v2.",
        "horizons": ["30 días", "Próximo trimestre", "Semestre",
                     "Backlog / monitorear"],
        "no_score": "Sin puntaje",
    },
}

# Section 8 rules, shared by the page and by scripts/test_v2_tools.py.
CALC_JS = r"""
function bandIndex(fw, s) {
  if (s === null || s === undefined || Number.isNaN(s)) return null;
  const b = fw.level_bands, v = Math.round(s * 1e9) / 1e9;
  for (let i = 0; i < b.length; i++) if (v < b[i].max) return i;
  return b.length - 1;
}
function priorityIndex(fw, raw) {
  const c = fw.scoring.priority_cuts, v = Math.round(raw * 1e9) / 1e9;
  if (v >= c.P0) return 0;
  if (v >= c.P1) return 1;
  if (v >= c.P2) return 2;
  return 3;
}
function calc(fw, input) {
  const sc = fw.scoring;
  const dims = fw.dimensions.map((d) => {
    const x = input[d.id] || {};
    const score = (x.score === null || x.score === undefined ||
      x.score === "") ? null : Number(x.score);
    const weight = x.weight === undefined ? d.weight : Number(x.weight);
    const target = x.target === undefined ? sc.default_target :
      Number(x.target);
    return {id: d.id, score, weight, target, strategies: d.strategies};
  });
  let tw = 0, tv = 0;
  for (const d of dims) if (d.score !== null) {
    tw += d.weight; tv += d.score * d.weight;
  }
  const overall = tw > 0 ? tv / tw : null;
  const ob = bandIndex(fw, overall);
  for (const d of dims) {
    d.band = bandIndex(fw, d.score);
    d.gap = d.score === null ? null : Math.max(0, d.target - d.score);
    d.priorityScore = d.gap === null ? null : d.weight * d.gap;
    d.priority = (d.gap === null || d.gap <= 1e-9) ? null :
      priorityIndex(fw, d.priorityScore);
  }
  const amplification = dims.filter((d) =>
    sc.amplifier_dimensions.includes(d.id) && d.band !== null &&
    ob !== null && ob - d.band >= 1).map((d) => d.id);
  const strategies = fw.strategies.map((s) => {
    const rel = dims.filter((d) => d.priority !== null &&
      d.strategies.includes(s.id));
    const cum = rel.reduce((a, d) => a + d.priorityScore, 0);
    const worst = rel.length ? Math.min(...rel.map((d) => d.priority))
      : null;
    return {id: s.id, name: s.name, cumulative: cum, worst,
      count: rel.length,
      recommended: rel.length > 0 && cum >= sc.strategy_min_cumulative};
  });
  strategies.sort((a, b) => (b.recommended - a.recommended) ||
    (b.cumulative - a.cumulative) || ((a.worst ?? 9) - (b.worst ?? 9)) ||
    (b.count - a.count) || a.id.localeCompare(b.id));
  return {overall, overallBand: ob, dims, amplification, strategies};
}
"""

PAGE = """<!doctype html>
<html lang="en" data-default-lang="__DEFAULT__">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<!-- Generated by scripts/generate_v2_tools_html.py. Do not edit. -->
<style>__CSS__</style>
</head>
<body>
<header><div class="bar">
<span class="brand">__LOGO__<span>__BRAND__</span></span>
<span class="grow"></span>
<select id="lang" aria-label="Language"><option value="en">English</option>
<option value="pt-br">Português (Brasil)</option>
<option value="es">Español</option></select>
</div></header>
<main id="app"></main>
<footer>framework v__VERSION__ · __SOURCE__</footer>
<script>
const FW = __FW__;
const UI = __UI__;
__CALC__
function pickLang() {
  const q = new URLSearchParams(location.search).get("lang");
  if (q && UI[q]) return q;
  const d = document.documentElement.dataset.defaultLang;
  if (d && d !== "auto" && UI[d]) return d;
  const n = (navigator.language || "en").toLowerCase();
  return n.startsWith("pt") ? "pt-br" : n.startsWith("es") ? "es" : "en";
}
let lang = pickLang();
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({"&": "&amp;",
  "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
function download(name, text) {
  const url = URL.createObjectURL(new Blob([text],
    {type: "application/json"}));
  const a = document.createElement("a"); a.href = url; a.download = name;
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}
__APP__
$("lang").value = lang;
$("lang").onchange = (e) => { lang = e.target.value;
  document.documentElement.lang = lang; render(); };
document.documentElement.lang = lang;
render();
</script>
</body>
</html>
"""

WIZARD_APP = r"""
const KEYS = __KEYS__;
const STORE = "ai-maturity-implementation-guide-inputs-v2";
const OLD = "ai-maturity-implementation-guide-inputs-v1";
let data = {};
try { data = JSON.parse(localStorage.getItem(STORE) || "null") || {}; }
catch (e) { data = {}; }
if (!Object.keys(data).length) {
  try {
    const v1 = JSON.parse(localStorage.getItem(OLD) || "{}");
    const map = {steering_committee: "executive_steering_committee",
      technology_product_owner: "tpo"};
    for (const [k, v] of Object.entries(v1)) data[map[k] || k] = v;
  } catch (e) { data = {}; }
}
let step = 0;
const filled = (k) => (data[k] || "").trim().length > 0;
const pct = () => Math.round(100 * KEYS.filter(filled).length /
  KEYS.length);
function save() { localStorage.setItem(STORE, JSON.stringify(data)); }
function render() {
  const t = UI[lang], s = t.steps[step], k = KEYS[step];
  document.title = t.title;
  let h = "<h1>" + esc(t.title) + "</h1><p>" + esc(t.intro) +
    "</p><p class='note'>" + esc(t.privacy) + "</p>";
  h += "<div class='steps'>" + t.steps.map((x, i) =>
    "<button data-go='" + i + "' class='" + (i === step ? "on" :
    filled(KEYS[i]) ? "done" : "") + "'>" + (i + 1) + ". " +
    esc(x[0]) + "</button>").join("") + "</div>";
  h += "<section><div class='note'>" + esc(t.step.replace("{n}",
    step + 1).replace("{total}", KEYS.length)) + " · " + pct() + "% " +
    esc(t.complete) + "</div><h2>" + esc(s[0]) + "</h2><p class='note'>" +
    esc(s[1]) + "</p><textarea id='field' rows='8' placeholder='" +
    esc(s[2]) + "'>" + esc(data[k] || "") + "</textarea>" +
    "<p class='note'><span id='chars'>" + (data[k] || "").length +
    "</span> " + esc(t.chars) + "</p><p><button id='prev'" +
    (step === 0 ? " disabled" : "") + ">" + esc(t.prev) +
    "</button> <button id='next' class='primary'>" +
    esc(step === KEYS.length - 1 ? t.review : t.next) + "</button> " +
    "<button id='export'>" + esc(t.export) + "</button> " +
    "<button id='reset'>" + esc(t.reset) + "</button></p>" +
    "<p class='note'>" + esc(t.next_step) + "</p></section>";
  h += "<section id='preview'><h2>" + esc(t.preview) + "</h2><table>" +
    KEYS.map((key, i) => "<tr><th>" + esc(t.steps[i][0]) + "</th><td>" +
    (filled(key) ? esc(data[key]).replace(/\n/g, "<br>") :
    "<span class='note'>" + esc(t.empty) + "</span>") + "</td></tr>")
    .join("") + "</table></section>";
  $("app").innerHTML = h;
  $("field").oninput = (e) => { data[k] = e.target.value; save();
    $("chars").textContent = e.target.value.length; };
  $("field").onchange = () => render();
  $("prev").onclick = () => { step = Math.max(0, step - 1); render(); };
  $("next").onclick = () => {
    if (step < KEYS.length - 1) { step++; render(); }
    else $("preview").scrollIntoView({behavior: "smooth"});
  };
  $("export").onclick = () => {
    const out = {metadata: {generated_at: new Date().toISOString(),
      generator: "wizard/implementation-guide-wizard.html (framework v2)",
      completion_pct: pct(), lang},
      implementation_guide_inputs: {}};
    for (const key of KEYS) out.implementation_guide_inputs[key] =
      data[key] || "";
    download("implementation-guide-inputs.json",
      JSON.stringify(out, null, 2));
  };
  $("reset").onclick = () => { if (confirm(t.confirm)) { data = {};
    localStorage.removeItem(STORE); step = 0; render(); } };
  document.querySelectorAll("[data-go]").forEach((b) => b.onclick = () =>
    { step = Number(b.dataset.go); render(); });
}
"""

CALC_APP = r"""
let input = {};
const fmt = (v, d = 2) => (v === null || v === undefined) ? "-" :
  (lang === "en" ? v.toFixed(d) : v.toFixed(d).replace(".", ","));
function label(band) {
  if (band === null) return UI[lang].no_score;
  const code = FW.level_bands[band].level;
  return code + " " + FW.level_names[lang][code];
}
function num(id, key, value, min, max, stepv) {
  return "<input type='number' data-d='" + id + "' data-k='" + key +
    "' min='" + min + "' max='" + max + "' step='" + stepv +
    "' value='" + (value === null || value === undefined ? "" : value) +
    "'>";
}
function render() {
  const t = UI[lang];
  document.title = t.title;
  const r = calc(FW, input);
  let h = "<h1>" + esc(t.title) + "</h1><p>" + esc(t.intro) + "</p>" +
    "<p><label><button id='pick' class='primary'>" + esc(t.load) +
    "</button><input type='file' id='file' accept='.json' hidden>" +
    "</label> <button id='reset'>" + esc(t.reset) + "</button></p>";
  h += "<section><table><tr><th>" + [t.dimension, t.score, t.weight,
    t.target, t.level, t.gap, t.priority_score, t.priority, t.horizon]
    .map(esc).join("</th><th>") + "</th></tr>";
  for (const d of r.dims) {
    const fd = FW.dimensions.find((x) => x.id === d.id);
    h += "<tr><td>" + d.id + " " + esc(fd.name[lang]) + "</td><td>" +
      num(d.id, "score", input[d.id]?.score ?? "", 0, 4, 0.01) +
      "</td><td>" + num(d.id, "weight", d.weight, 0.5, 2, 0.1) +
      "</td><td>" + num(d.id, "target", d.target, 0, 4, 0.1) +
      "</td><td>" + esc(label(d.band)) + "</td><td class='num'>" +
      fmt(d.gap) + "</td><td class='num'>" + fmt(d.priorityScore) +
      "</td><td>" + (d.priority === null ? "-" : "P" + d.priority) +
      "</td><td>" + (d.priority === null ? "-" :
      esc(t.horizons[d.priority])) + "</td></tr>";
  }
  h += "<tr><th>" + esc(t.overall) + "</th><th class='num'>" +
    fmt(r.overall) + "</th><th colspan='2'></th><th colspan='5'>" +
    esc(label(r.overallBand)) + "</th></tr></table>";
  h += "<p><b>" + esc(t.amplification) + ":</b> " +
    (r.amplification.length ? "<span class='flag'>" +
    r.amplification.join(", ") + "</span>. " + esc(t.amp_why) :
    "<span class='ok'>" + esc(t.amp_none) + "</span>") + "</p></section>";
  h += "<section><h2>" + esc(t.strategies) + "</h2><table><tr><th>" +
    [t.strategy, t.cumulative, t.priority, t.recommended].map(esc)
    .join("</th><th>") + "</th></tr>" + r.strategies.map((s) =>
    "<tr><td>" + s.id + " " + esc(s.name) + "</td><td class='num'>" +
    fmt(s.cumulative) + "</td><td>" + (s.worst === null ? "-" : "P" +
    s.worst) + "</td><td>" + (s.recommended ? "<b>" + esc(t.yes) +
    "</b>" : esc(t.no)) + "</td></tr>").join("") + "</table>" +
    "<p class='note'>" + esc(t.rules) + "</p></section>";
  $("app").innerHTML = h;
  document.querySelectorAll("input[data-d]").forEach((el) =>
    el.onchange = () => {
      const x = input[el.dataset.d] = input[el.dataset.d] || {};
      x[el.dataset.k] = el.value === "" ? (el.dataset.k === "score" ?
        null : undefined) : Number(el.value);
      render();
    });
  $("pick").onclick = () => $("file").click();
  $("file").onchange = async (e) => {
    try {
      const j = JSON.parse(await e.target.files[0].text());
      if (!Array.isArray(j.dimensions)) throw new Error();
      input = {};
      for (const d of j.dimensions) input[d.id] = {score: d.score,
        weight: d.weight};
      render();
    } catch (err) { alert(t.bad_file); }
  };
  $("reset").onclick = () => { input = {}; render(); };
}
"""


def slim_framework(fw: dict, for_calc: bool) -> dict:
    out = {"version": fw["version"]}
    if for_calc:
        out.update({
            "level_bands": fw["level_bands"],
            "level_names": fw["level_names"],
            "scoring": fw["scoring"],
            "strategies": [{"id": s["id"], "name": s["name"]}
                           for s in fw["strategies"]],
            "dimensions": [{"id": d["id"], "name": d["name"],
                            "weight": d.get("weight", 1.0),
                            "strategies": d["strategies"]}
                           for d in fw["dimensions"]],
        })
    return out


def page(fw: dict, ui: dict, app: str, default: str, title: str,
         source: str, calc_js: str, for_calc: bool) -> str:
    html = PAGE
    for key, value in (
        ("__DEFAULT__", default), ("__TITLE__", title), ("__CSS__", CSS),
        ("__LOGO__", MS_LOGO), ("__BRAND__", BRAND),
        ("__VERSION__", fw["version"]), ("__SOURCE__", source),
        ("__FW__", json.dumps(slim_framework(fw, for_calc),
                              ensure_ascii=False)),
        ("__UI__", json.dumps(ui, ensure_ascii=False)),
        ("__CALC__", calc_js), ("__APP__", app),
    ):
        html = html.replace(key, value)
    return html


TEMPLATE_HELP = {
    "en": "Fill these fields by hand if you do not use the wizard, then "
          "save the file as implementation-guide-inputs.json in the kit "
          "root. Empty fields stay empty in the report (\"to fill with "
          "the client\"); do not leave the examples from _guide in the "
          "values.",
    "pt-br": "Preencha estes campos à mão se não usar o wizard e salve o "
             "arquivo como implementation-guide-inputs.json na raiz do "
             "kit. Campos vazios continuam vazios no relatório (\"a "
             "preencher com o cliente\"); não copie os exemplos de _guide "
             "para os valores.",
    "es": "Completa estos campos a mano si no usas el wizard y guarda el "
          "archivo como implementation-guide-inputs.json en la raíz del "
          "kit. Los campos vacíos siguen vacíos en el informe (\"a "
          "completar con el cliente\"); no copies los ejemplos de _guide "
          "en los valores.",
}


def template_json() -> str:
    guide = {}
    for idx, key in enumerate(WIZARD_KEYS):
        guide[key] = {lang: f"{ui['steps'][idx][0]}: "
                            f"{ui['steps'][idx][1]}\n\n"
                            f"{ui['steps'][idx][2]}"
                      for lang, ui in WIZARD.items()}
    data = {
        "_help": TEMPLATE_HELP,
        "_guide": guide,
        "metadata": {"generator": "manual edit", "completion_pct": 0},
        "implementation_guide_inputs": {k: "" for k in WIZARD_KEYS},
    }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def outputs() -> dict[Path, str]:
    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    wizard_app = WIZARD_APP.replace("__KEYS__", json.dumps(WIZARD_KEYS))
    files = {ROOT / "wizard/implementation-guide-inputs.template.json":
             template_json()}
    for suffix, default in (("", "auto"), (".pt-br", "pt-br")):
        files[ROOT / f"wizard/implementation-guide-wizard{suffix}.html"] = \
            page(fw, WIZARD, wizard_app, default,
                 WIZARD["en"]["title"], "wizard/README.md", "", False)
        files[ROOT / f"referencia/calculadora-pontuacao{suffix}.html"] = \
            page(fw, CALC_UI, CALC_APP, default, CALC_UI["en"]["title"],
                 "coleta/AI-Maturity-Form-Questions_v2.md, section 8",
                 CALC_JS, True)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if a generated file is out of date")
    args = ap.parse_args()
    stale = []
    for path, text in outputs().items():
        if args.check:
            if not path.exists() or path.read_text("utf-8") != text:
                stale.append(path.relative_to(ROOT))
            continue
        path.write_text(text, encoding="utf-8")
        print(f"✓ {path.relative_to(ROOT)}")
    if stale:
        print("✗ Out of date (run python3 scripts/generate_v2_tools_html"
              ".py):\n  " + "\n  ".join(map(str, stale)), file=sys.stderr)
        return 1
    if args.check:
        print("✓ 5 generated helper files up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
