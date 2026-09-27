# AI Maturity Assessment client kit

English | [Português (Brasil)](README.pt-br.md)

A self-contained kit to run an AI Maturity Assessment without depending on a web platform. Framework v2 is the default. Framework v1 remains archived and supported for historical inputs.

Author role: Global Developer Solutions Advisor.

See [CHANGELOG.md](CHANGELOG.md) for release history.

## What is new in framework v2

- Version: 2.0.1.
- Source spec: [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- Machine model: [framework.v2.json](framework.v2.json), validated by [framework.v2.schema.json](framework.v2.schema.json) and [scripts/validate_framework_v2.py](scripts/validate_framework_v2.py).
- 5 profile questions and 61 scored questions.
- 9 dimensions: D1 AI Strategy, Policy and Governance (7), D2 Enablement, Skills and Culture (6), D3 Plan, Specify and Design (6), D4 Code and Context Engineering (8), D5 Review, Quality and Testing (7), D6 Security and AI Supply Chain (7), D7 Deliver and Operate (6), D8 Engineering Foundations (AI amplifiers) (7), D9 Measurement, Value and AI FinOps (7).
- IDs use `D#-Q#`. Profile IDs use `R-Q1` to `R-Q5`.
- Levels: L0 Not started, L1 Exploring, L2 Adopting, L3 Scaling, L4 AI-native, plus `NA`.
- Main form: [formularios/assessment-v2.html](formularios/assessment-v2.html).
- Forms setup: [coleta/INSTRUCOES-FORMS.md](coleta/INSTRUCOES-FORMS.md).

## Quick start

```bash
make init
# Edit respostas.json, or import a Microsoft Forms export:
make import XLSX=respostas-forms.xlsx
make scores
make workbook
make pipeline
```

Direct commands:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Outputs for v2

| Output | Purpose |
| --- | --- |
| `saida/scores.json` | Scores by question, dimension, persona, and overall where produced by the engine. |
| `saida/gaps.json` | Dimension gaps, priorities, flags, and backlog inputs. |
| `saida/recomendacoes.json` | Strategy recommendations `S1` to `S7`. |
| `saida/pontuacao-v2-<date>.xlsx` | Auditable workbook with formulas and engine cross-check. |
| `saida/payload_v2.json` | Report payload for inspection and customization. |
| `saida/v2_assessment_summary.pdf` | Executive summary. |
| `saida/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `saida/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `saida/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |

## Scoring summary

The scripts are the source of truth. Do not compute scores by hand.

- Question score: pooled mean of respondent levels, excluding blank and `NA`.
- Dimension score: mean of its question scores.
- Overall: weighted mean of dimensions.
- Dimension weights default to `1.0` and may be set from `0.5` to `2.0` in `respostas.json`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.
- Priority: `dimension weight x gap`; P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3.

## Companion surveys

The Developer Survey and Learning and Growth Survey are unchanged. When both the assessment and Developer Survey dimensions appear together, use `DS-D#` for Developer Survey dimensions. v2 cross-references the surveys in D2, D5, and D9.

## v1 archive

v1 is still supported for files without `metadata.framework_version`, or with a `1.x` version. It uses [framework.json](framework.json), 158 questions, 3 pillars, and archived assets:

- [coleta/v1/](coleta/v1/)
- [formularios/v1/](formularios/v1/)
- [referencia/v1/](referencia/v1/)

Use `make init-v1` to start a v1 input. The dispatching scripts keep v1 behavior unchanged.

## Repository map

| Path | Purpose |
| --- | --- |
| [coleta/](coleta/) | v2 form instructions, v2 spec, generated question banks, and v1 archive. |
| [formularios/](formularios/) | v2 offline form and archived v1 visual forms. |
| [referencia/](referencia/) | Reference material and examples. |
| [relatorios/](relatorios/) | Report renderer, templates, and localization. |
| [scripts/](scripts/) | Deterministic import, scoring, workbook, comparison, validation, and generation scripts. |
| [.github/skills/](.github/skills/) | Copilot custom skills that call the deterministic scripts. |

## Validation

```bash
make validate-v2
make validate-docs
make test
```
