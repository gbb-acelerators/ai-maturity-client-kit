# Copilot instructions for the AI Maturity Assessment kit

This repository is the AI Maturity Assessment client kit. Framework v2 is the default flow. Framework v1 remains supported for archived inputs and historical comparisons.

## Default framework

- v2 source spec: [coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md), version 2.0.1.
- Generated model: [framework.v2.json](../framework.v2.json), schema [framework.v2.schema.json](../framework.v2.schema.json).
- Structure: 5 profile questions (`R-Q1` to `R-Q5`) plus 9 scored dimensions and 61 scored questions.
- Dimensions: D1 AI Strategy, Policy and Governance (7), D2 Enablement, Skills and Culture (6), D3 Plan, Specify and Design (6), D4 Code and Context Engineering (8), D5 Review, Quality and Testing (7), D6 Security and AI Supply Chain (7), D7 Deliver and Operate (6), D8 Engineering Foundations (AI amplifiers) (7), D9 Measurement, Value and AI FinOps (7).
- Scored IDs use `D#-Q#`. Form titles start with the ID, for example `D4-Q3: ...`.
- Levels are `L0 - Not started`, `L1 - Exploring`, `L2 - Adopting`, `L3 - Scaling`, `L4 - AI-native`, plus `NA`.
- Report groups: G1 is D1, D2, D9; G2 is D3, D4, D5; G3 is D6, D7, D8.

## v1 archive and dispatch

- Inputs without `metadata.framework_version`, or with a `1.x` version, use the v1 flow unchanged.
- v1 uses [framework.json](../framework.json), 158 questions, 3 pillars, capabilities, and archived assets under [coleta/v1/](../coleta/v1/), [formularios/v1/](../formularios/v1/), and [referencia/v1/](../referencia/v1/).
- Never migrate or reinterpret a v1 `respostas.json` by hand. Use the dispatcher scripts.

## Deterministic scripts only

Do not compute scores, gaps, recommendations, imports, workbooks, comparisons, evidence checks, or reports manually in chat. Always run or instruct the official scripts:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/merge_offline_respostas.py exports/
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
python3 scripts/compare_rounds.py BEFORE.json AFTER.json --pdf
python3 scripts/scan_repos_ai_config.py --repos ~/src
python3 scripts/import_copilot_metrics.py --metrics copilot-usage.json
```

Equivalent Make targets include `make demo`, `make merge`, `make pipeline`, `make compare`, `make scan-repos`, `make telemetry`, `make examples-v2`, `make validate-docs`, and `make test`.

## v2 scoring facts

- Question score: pooled mean of respondent values, excluding blank and `NA` (`level: null`).
- Dimension score: mean of answered question scores.
- Overall: weighted mean of dimensions. Default dimension weight is `1.0`; `respostas.json::dimension_weights` may set `0.5` to `2.0`.
- Bands are half-open: L0 `[0,0.8)`, L1 `[0.8,1.6)`, L2 `[1.6,2.4)`, L3 `[2.4,3.2)`, L4 `[3.2,4.0]`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.
- Gap: target (default `3.0`, overridable by `target_overrides`) minus score.
- Priority: `weight x gap`; P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3. Comparisons ignore floating-point noise below `1e-9`.
- Respondent divergence: flag a dimension when at least 3 respondents have a score and the standard deviation of their own dimension scores is 1.0 or more.
- Strategies `S1` to `S7` are recommended when the summed priority of mapped dimensions is at least `0.9`.

## v2 signals to preserve

Reports and skills should surface these signals when present in script output: low confidence, amplification risk, perception gap, respondent divergence, scope caveat, unverified L3/L4, persona summaries, backlog top lowest questions with L3 anchors, evidence to collect, KPI, and report groups G1, G2, and G3.

## Reports and wizard

- `make pipeline` renders 5 v2 PDFs: `v2_assessment_summary.pdf`, `v2_roadmap_g1.pdf`, `v2_roadmap_g2.pdf`, `v2_roadmap_g3.pdf`, and `v2_implementation_guide.pdf`.
- The implementation guide reads `implementation-guide-inputs.json` through `relatorios/scripts/wizard_inputs.py`.
- The wizard has 11 fields, including `dimension_owners` and `risk_register`.
- Empty wizard fields render as `to fill with the client`. Never say empty fields are replaced by examples.
- Mode D auto-fill supports `--lang en|pt-br|es` and fills 7 of 11 fields from the Learning Survey training plan.

## Evidence cross-checks

- `make scan-repos REPOS=...` or `make scan-repos ORG=...` writes `saida/repo-scan.json`. It maps repositories to RAMP L1 to L4 as a pattern-based approximation. L2+ coverage caps D4-Q4; L3+ share is shown next to D4-Q5.
- `make telemetry METRICS=... [SEATS=...]` writes `saida/telemetria.json`. It classifies adoption phases for D4-Q1 and provides evidence for D9-Q1.
- The summary PDF section 2.2 shows evidence cross-checks. The implementation guide lists mismatches as risks.

## Companion surveys

- Developer Survey dimensions are `DS-D2` to `DS-D8` in outputs.
- `framework.v2.json` contains the crosswalk from `DS-D#` to v2 questions.
- Survey results never change v2 scores.
- Survey scripts write EN, PT-BR or ES (`--lang en|pt-br|es`). The EN and ES banks translate the Developer Survey options; `survey-devs/options.json` maps every language back to the canonical option before scoring.

## Docs and links

- Main docs: [README.md](../README.md), [GUIA-PASSO-A-PASSO.md](../GUIA-PASSO-A-PASSO.md), [coleta/INSTRUCOES-FORMS.md](../coleta/INSTRUCOES-FORMS.md).
- Reference docs: [referencia/framework-v2.md](../referencia/framework-v2.md), [referencia/dimensoes/](../referencia/dimensoes/), [referencia/README.md](../referencia/README.md).
- Author role: Global Developer Solutions Advisor.

## Style

Use plain, direct, short sentences. Do not add em dashes or en dashes. Use colon, comma, parentheses, or ` - ` instead.
