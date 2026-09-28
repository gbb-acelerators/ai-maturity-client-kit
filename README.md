# AI Maturity Assessment client kit

🌐 English · [Português (Brasil)](README.pt-br.md)

A self-contained kit to run an AI-assisted SDLC maturity self-assessment without depending on a web platform. Framework v2 is the default. Framework v1 remains archived and supported for historical inputs.

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
- Main form: [formularios/assessment-v2.html](formularios/assessment-v2.html). It runs offline, shows each question scope note, and exports one respondent per `respostas.json`.
- Forms setup: [coleta/INSTRUCOES-FORMS.md](coleta/INSTRUCOES-FORMS.md).
- Dimension reference pages live in [referencia/dimensoes/](referencia/dimensoes/) with EN, PT-BR, and ES pages for D1 to D9.

## Quickstart

Fastest path to a first PDF after `make install-deps`, or inside the dev container:

```bash
make demo
open saida/demo/*.pdf
```

Use `DEMO_LANG=en`, `DEMO_LANG=pt-BR`, or `DEMO_LANG=es` to choose the demo language. The demo writes illustrative outputs under `saida/demo/` and does not touch `respostas.json`.

Real assessment flow:

```bash
make install-deps
# Collect with Microsoft Forms, or collect offline exports and merge them:
make merge DIR=exports/
# Or import a Microsoft Forms export:
make import XLSX=respostas-forms.xlsx
make pipeline
# Optional evidence cross-checks:
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
# Fill implementation-guide-inputs.json with the wizard, then render again:
make pipeline
```

Direct commands remain available for automation:

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
| `saida/gaps.json` | Dimension gaps, priorities, flags, respondent divergence, and backlog inputs. |
| `saida/recomendacoes.json` | Strategy recommendations `S1` to `S7`. |
| `saida/pontuacao-v2-<date>.xlsx` | Auditable workbook with formulas and engine cross-check. |
| `saida/payload_v2.json` | Report payload for inspection and customization. |
| `saida/v2_assessment_summary.pdf` | Executive summary, including evidence cross-checks when available. |
| `saida/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `saida/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `saida/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |
| `saida/v2_implementation_guide.pdf` | Part 4 for v2: governance, RACI, phased plan, change management, risks, metrics, first 90 days, and references. |
| `saida/comparacao-rodadas.pdf` | Comparison report from `make compare BEFORE=old.json AFTER=respostas.json`. |

`make pipeline` renders the 5 v2 PDFs. v1 still renders its archived 5 PDF set.

## Scoring summary

The scripts are the source of truth. Do not compute scores by hand.

- Question score: pooled mean of respondent levels, excluding blank and `NA`.
- Dimension score: mean of its question scores.
- Overall: weighted mean of dimensions.
- Dimension weights default to `1.0` and may be set from `0.5` to `2.0` in `respostas.json`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.
- Priority: `dimension weight x gap`; P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3. Band and priority comparisons ignore floating-point noise below `1e-9`.
- Respondent divergence: a dimension is flagged when at least 3 respondents have a score and the standard deviation of their own dimension scores is 1.0 or more.

## Evidence cross-checks

Two optional inputs help challenge overconfident answers. They do not change scores.

- `make scan-repos REPOS=~/src` scans local clones using committed files only. `make scan-repos ORG=<github-org>` scans default branches through the GitHub REST API and requires `GITHUB_TOKEN` or `GH_TOKEN`. Output: `saida/repo-scan.json`. The scan places repositories on RAMP levels L1 to L4 as a pattern-based approximation. The share of repositories at L2+ caps D4-Q4 by coverage bands, and the share at L3+ is shown next to D4-Q5.
- `make telemetry METRICS=<Copilot usage metrics report JSON/NDJSON> [SEATS=200]` writes `saida/telemetria.json`. It reads GitHub Copilot usage metrics exports and classifies adoption phases: No Cohort, Phase 1 Code first, Phase 2 Agent first, Phase 3 Multi-agent. The export itself is evidence for D9-Q1.

The summary PDF section 2.2 shows both cross-checks and flags answers above what the evidence supports. The implementation guide lists those mismatches as risks. If the files are missing, the report explains how to produce them.

## Companion surveys

The Developer Survey and Learning and Growth Survey are companion signals. Survey results never change v2 scores.

- Developer Survey dimensions are named `DS-D2` to `DS-D8` in outputs. Forms built with the old `D2` text still parse.
- `framework.v2.json` contains the survey crosswalk from each `DS-D#` to the v2 questions it helps validate.
- The v2 summary PDF shows Developer Survey context when `saida/maturidade-developer-survey-*.json` exists.
- The survey rubric keeps the v1 score bands, so compare by score, not by level name.
- Survey scripts write EN or PT-BR only.

## v1 archive

v1 is still supported for files without `metadata.framework_version`, or with a `1.x` version. It uses [framework.json](framework.json), 158 questions, 3 pillars, and archived assets:

- [coleta/v1/](coleta/v1/)
- [formularios/v1/](formularios/v1/)
- [referencia/v1/](referencia/v1/)

Use `make init-v1` to start a v1 input. The dispatching scripts keep v1 behavior unchanged.

## Repository map

| Path | Purpose |
| --- | --- |
| [coleta/](coleta/) | v2 form instructions, v2 spec, generated question banks, offline merge guidance, and v1 archive. |
| [formularios/](formularios/) | v2 offline form and archived v1 visual forms. |
| [referencia/](referencia/) | Framework guide, v2 calculator, per-dimension pages, branding, and examples. |
| [relatorios/](relatorios/) | Report renderer, templates, localization, comparison PDF, and wizard input parser. |
| [scripts/](scripts/) | Deterministic import, scoring, workbook, comparison, validation, demo, evidence, packaging, and generation scripts. |
| [wizard/](wizard/) | Generated trilingual implementation guide wizard and auto-fill script. |
| [.github/skills/](.github/skills/) | Copilot custom skills that call the deterministic scripts. |

## Validation

```bash
python3 scripts/build_kit_docs.py
python3 scripts/build_kit_docs.py --check
make validate-docs
make test
```

CI is configured for tests, documentation validation, smoke rendering, and demo checks on push and pull requests to `main` and `develop`. GitHub Actions may be blocked by repository billing, so treat local validation as required.
