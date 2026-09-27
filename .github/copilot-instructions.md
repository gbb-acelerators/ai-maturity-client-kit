# Copilot instructions for the AI Maturity Assessment kit

This repository is the AI Maturity Assessment client kit. Framework v2 is the default flow. Framework v1 remains supported for archived inputs and historical comparisons.

## Default framework

- v2 source spec: [coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md), version 2.0.1.
- Generated model: [framework.v2.json](../framework.v2.json), schema [framework.v2.schema.json](../framework.v2.schema.json).
- Generator and validation: `scripts/spec_to_framework_v2.py`, `scripts/validate_framework_v2.py`, `framework/v2/config.json`, `framework/v2/i18n.pt-br.json`, `framework/v2/i18n.es.json`.
- Structure: 5 profile questions (`R-Q1` to `R-Q5`) plus 9 scored dimensions and 61 scored questions.
- Dimensions: D1 AI Strategy, Policy and Governance (7), D2 Enablement, Skills and Culture (6), D3 Plan, Specify and Design (6), D4 Code and Context Engineering (8), D5 Review, Quality and Testing (7), D6 Security and AI Supply Chain (7), D7 Deliver and Operate (6), D8 Engineering Foundations (AI amplifiers) (7), D9 Measurement, Value and AI FinOps (7).
- Scored IDs use `D#-Q#`. Form titles start with the ID, for example `D4-Q3: ...`.
- Levels are `L0 - Not started`, `L1 - Exploring`, `L2 - Adopting`, `L3 - Scaling`, `L4 - AI-native`, plus `NA`.
- Localized level names: PT-BR `Nao iniciado`, `Explorando`, `Adotando`, `Escalando`, `Nativo em IA`; ES `No iniciado`, `Explorando`, `Adoptando`, `Escalando`, `Nativo en IA`.

## v1 archive and dispatch

- Inputs without `metadata.framework_version`, or with a `1.x` version, use the v1 flow unchanged.
- v1 uses [framework.json](../framework.json), 158 questions, 3 pillars (`P1` to `P3`), capabilities, and the archived assets under [coleta/v1/](../coleta/v1/), [formularios/v1/](../formularios/v1/) and [referencia/v1/](../referencia/v1/).
- Never migrate or reinterpret a v1 `respostas.json` by hand. Use the dispatcher scripts.

## Deterministic scripts only

Do not compute scores, gaps, recommendations, imports, workbooks, comparisons, or reports manually in chat. Always run or instruct the official scripts:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
python3 scripts/compare_rounds.py BEFORE.json AFTER.json
```

Equivalent Make targets are `make import XLSX=...`, `make scores`, `make workbook`, `make pipeline`, `make compare BEFORE=... [AFTER=...]`, `make validate-v2`, `make generate-v2`, and `make mock-v2`.

## v2 scoring facts

- Question score: pooled mean of respondent values, excluding blank and `NA`.
- Dimension score: mean of answered question scores.
- Overall: weighted mean of dimensions. Default dimension weight is `1.0`; `respostas.json::dimension_weights` may set `0.5` to `2.0`.
- Bands are half-open: L0 `[0,0.8)`, L1 `[0.8,1.6)`, L2 `[1.6,2.4)`, L3 `[2.4,3.2)`, L4 `[3.2,4.0]`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.
- Gap: target (default `3.0`, overridable by `target_overrides`) minus score.
- Priority: `weight x gap`; P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3.
- Strategies `S1` to `S7` are recommended when the summed priority of mapped dimensions is at least `0.9`.

## v2 signals to preserve

Reports and skills should surface these v2 signals when present in script output: low confidence, amplification risk, perception gap, scope caveat, unverified L3/L4, persona summaries, backlog top 5 lowest questions with L3 anchors, and report groups `G1` (`D1`, `D2`, `D9`), `G2` (`D3`, `D4`, `D5`), `G3` (`D6`, `D7`, `D8`).

## v2 resposta format

```json
{
  "metadata": {"framework_version": "2.0.1", "organization": "Acme", "language": "en", "assessment_date": "2026-09-27", "source": "forms"},
  "target_overrides": {"D4": 3.2},
  "dimension_weights": {"D6": 1.5},
  "respondents": [
    {"id": "r1", "name": "Name", "email": "name@example.com", "profile": {"R-Q1": "Executive (CTO, VP, Director)", "R-Q3": ["GitHub Copilot"]}, "answers": {"D1-Q1": {"level": 2, "evidence": "..."}, "D1-Q2": {"level": null, "evidence": "NA"}}}
  ]
}
```

Missing answer key means not answered. `level: null` means `NA`.

## Companion surveys

The Developer Survey and Learning and Growth Survey are unchanged. Their dimensions also use `D1` to `D7`. When a text mentions both the v2 assessment and Developer Survey dimensions, call the survey dimensions `DS-D#` to avoid collision. v2 D2, D5, and D9 cross-reference those surveys instead of duplicating their questions.

## Docs and links

- Main v2 collection assets: [coleta/INSTRUCOES-FORMS.md](../coleta/INSTRUCOES-FORMS.md), [coleta/INSTRUCOES-FORMS.pt-br.md](../coleta/INSTRUCOES-FORMS.pt-br.md), [coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md), [formularios/assessment-v2.html](../formularios/assessment-v2.html).
- v1 collection assets live under [coleta/v1/](../coleta/v1/), [formularios/v1/](../formularios/v1/), and [referencia/v1/](../referencia/v1/).
- Link to [CHANGELOG.md](../CHANGELOG.md) from main docs.
- Author role: Global Developer Solutions Advisor.

## Style

Use plain, direct, short sentences. Do not add em dashes or en dashes. Use colon, comma, parentheses, or ` - ` instead.
