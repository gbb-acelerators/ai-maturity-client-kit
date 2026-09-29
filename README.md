# AI Maturity Assessment client kit

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

A self-contained kit to run an AI-assisted SDLC maturity self-assessment without depending on a web platform. Framework v2 is the default. Framework v1 remains archived and supported for historical inputs.

Author role: Global Developer Solutions Advisor.

Current release: kit 2.1.0 with framework 2.0.2. See [CHANGELOG.md](CHANGELOG.md) for release history.

## Get the kit

- Site: <https://gbb-acelerators.github.io/ai-maturity-client-kit/> (English, Portuguese (Brazil) and Spanish).
- Download a ready-to-use package, no GitHub account needed: [English](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip), [Português (Brasil)](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-pt.zip), [Español](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip). Each package ships its language under the base file names.
- Or clone the repository: `git clone https://github.com/gbb-acelerators/ai-maturity-client-kit.git`.

Requirements:

- Python 3 (CI uses 3.12). `make install-deps` installs `jinja2`, `weasyprint`, `openpyxl` and `jsonschema`. WeasyPrint also needs the Pango libraries: `brew install pango` on macOS, or the packages CI installs on Linux and WSL (`libpango-1.0-0`, `libpangoft2-1.0-0`, `libharfbuzz-subset0`, `fonts-dejavu-core`).
- Or open the cloned repository in its dev container (`.devcontainer/`), which installs everything and runs the tests.
- For the Copilot Chat commands: VS Code with GitHub Copilot, in Agent mode.

## What is new in framework v2

- Version: 2.0.2 (see the [spec changelog](collection/AI-Maturity-Form-Questions_v2.md#changelog)).
- Source spec: [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md), translated in [PT-BR](collection/AI-Maturity-Form-Questions_v2.pt-br.md) and [ES](collection/AI-Maturity-Form-Questions_v2.es.md).
- Machine model: [framework.v2.json](framework.v2.json), validated by [framework.v2.schema.json](framework.v2.schema.json) and [scripts/validate_framework_v2.py](scripts/validate_framework_v2.py).
- 5 profile questions and 61 scored questions.
- 9 dimensions: D1 AI Strategy, Policy and Governance (7), D2 Enablement, Skills and Culture (6), D3 Plan, Specify and Design (6), D4 Code and Context Engineering (8), D5 Review, Quality and Testing (7), D6 Security and AI Supply Chain (7), D7 Deliver and Operate (6), D8 Engineering Foundations (AI amplifiers) (7), D9 Measurement, Value and AI FinOps (7).
- IDs use `D#-Q#`. Profile IDs use `R-Q1` to `R-Q5`.
- Levels: L0 Not started, L1 Exploring, L2 Adopting, L3 Scaling, L4 AI-native, plus `NA`.
- Main form: [forms/assessment-v2.html](forms/assessment-v2.html). It runs offline, shows each question scope note, and exports one respondent per `responses.json`.
- Forms setup: [collection/FORMS-INSTRUCTIONS.md](collection/FORMS-INSTRUCTIONS.md).
- Dimension reference pages live in [reference/dimensions/](reference/dimensions/) with EN, PT-BR, and ES pages for D1 to D9.

## Quickstart

Fastest path to a first PDF after `make install-deps`, or inside the dev container:

```bash
make demo
open output/demo/*.pdf
```

Use `DEMO_LANG=en`, `DEMO_LANG=pt-BR`, or `DEMO_LANG=es` to choose the demo language. The demo writes illustrative outputs under `output/demo/` and does not touch `responses.json`.

Real assessment flow:

```bash
make install-deps
# Collect with Microsoft Forms, or collect offline exports and merge them:
make merge DIR=exports/
# Or import a Microsoft Forms export:
make import XLSX=forms-responses.xlsx
make pipeline
# Optional evidence cross-checks:
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
# Fill implementation-guide-inputs.json with the wizard, then render again:
make pipeline
```

Direct commands remain available for automation:

```bash
python3 scripts/import_forms_excel.py forms-responses.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 reports/scripts/build_payload_and_render.py
```

## Outputs for v2

| Output | Purpose |
| --- | --- |
| `output/scores.json` | Scores by question, dimension, persona, and overall where produced by the engine. |
| `output/gaps.json` | Dimension gaps, priorities, flags, respondent divergence, and backlog inputs. |
| `output/recommendations.json` | Strategy recommendations `S1` to `S7`. |
| `output/scoring-v2-<date>.xlsx` | Auditable workbook with formulas and engine cross-check. |
| `output/payload_v2.json` | Report payload for inspection and customization. |
| `output/v2_assessment_summary.pdf` | Executive summary, including evidence cross-checks when available. |
| `output/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `output/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `output/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |
| `output/v2_implementation_guide.pdf` | Part 4 for v2: governance, RACI, phased plan, change management, risks, metrics, first 90 days, and references. |
| `output/round-comparison.pdf` | Comparison report from `make compare BEFORE=old.json AFTER=responses.json`. |
| `output/repo-scan.json` | Repository scan for the D4 cross-check (`make scan-repos`). |
| `output/telemetry.json` | Copilot usage metrics summary for the D4-Q1 and D9-Q1 cross-checks (`make telemetry`). |
| `output/dora-metrics.json` | DORA metrics coverage for the D9-Q2 cross-check (`make dora`). |
| `output/developer-survey-maturity-<date>.json`, `output/insights-developer-survey-<date>.md` | Developer Survey maturity and insights. |
| `output/training-plan-<date>.md` | Training plan from the Learning and Growth Survey. |

`make pipeline` renders the 5 v2 PDFs. v1 still renders its archived 5 PDF set.

## Scoring summary

The scripts are the source of truth. Do not compute scores by hand.

- Question score: pooled mean of respondent levels, excluding blank and `NA`.
- Dimension score: mean of its question scores.
- Overall: weighted mean of dimensions.
- Dimension weights default to `1.0` and may be set from `0.5` to `2.0` in `responses.json`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.
- Priority: `dimension weight x gap`; P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3. Band and priority comparisons ignore floating-point noise below `1e-9`.
- Respondent divergence: a dimension is flagged when at least 3 respondents have a score and the standard deviation of their own dimension scores is 1.0 or more.

## Evidence cross-checks

Three optional inputs help challenge overconfident answers. They do not change scores.

- `make scan-repos REPOS=~/src` scans local clones using committed files only. `make scan-repos ORG=<github-org>` scans default branches through the GitHub REST API and requires `GITHUB_TOKEN` or `GH_TOKEN`. Output: `output/repo-scan.json`. The scan places repositories on RAMP levels L1 to L4 as a pattern-based approximation. The share of repositories at L2+ caps D4-Q4 by coverage bands, and the share at L3+ is shown next to D4-Q5.
- `make telemetry METRICS=<Copilot usage metrics report JSON/NDJSON> [SEATS=200]` writes `output/telemetry.json`. It reads GitHub Copilot usage metrics exports and classifies adoption phases: No Cohort, Phase 1 Code first, Phase 2 Agent first, Phase 3 Multi-agent. The export itself is evidence for D9-Q1.
- `make dora DORA=<CSV or JSON> [SERVICES=40]` writes `output/dora-metrics.json`. It reads one row per service and period (`baseline` before AI adoption, `current`) with deployment frequency, lead time, change failure rate and time to restore. With `SERVICES`, the share of services compared with a baseline caps D9-Q2 by coverage bands. It checks measurement coverage, not delivery performance.

The summary PDF section 2.2 shows the cross-checks and flags answers above what the evidence supports. The implementation guide lists those mismatches as risks. If the files are missing, the report explains how to produce them.

## Companion surveys

The Developer Survey and Learning and Growth Survey are companion signals. Survey results never change v2 scores.

- Developer Survey dimensions are named `DS-D2` to `DS-D8` in outputs. Forms built with the old `D2` text still parse.
- `framework.v2.json` contains the survey crosswalk from each `DS-D#` to the v2 questions it helps validate.
- The v2 summary PDF shows Developer Survey context when `output/developer-survey-maturity-*.json` exists.
- The survey rubric keeps the v1 score bands, so compare by score, not by level name.
- Survey scripts write EN, PT-BR or ES (`--lang en|pt-br|es`). The Developer Survey banks translate the answer options in every language; `survey-devs/options.json` maps them back to the same canonical options, so scores do not depend on the form language.

## Copilot Chat commands

Open the kit folder in VS Code with GitHub Copilot and use Copilot Chat in Agent mode. The assistant answers in your language (English, Portuguese (Brazil) or Spanish) and renders client outputs in the client's language (`metadata.language` in `responses.json`, `--lang` in the survey scripts). Its instruction files in [.github/](.github/) stay in English by design: they are read by the model, not by the client.

| Command | What it does |
| --- | --- |
| `@ai-maturity-assistant` | Concierge agent: checks the workspace and runs or suggests the next step. |
| `/full-pipeline` | Full pipeline, from `responses.json` to the workbook and the PDFs. |
| `/ai-maturity-reports` | Reporting pipeline wrapper (v2 by default, v1 archived inputs supported). |
| `/import-responses` | Imports a Microsoft Forms export or merges offline form exports into `responses.json`. |
| `/calculate-scores` | Computes the scores with the deterministic engine. |
| `/gap-analysis` | Computes gaps and P0 to P3 priorities. |
| `/recommend-strategies` | Maps the priorities to the strategies S1 to S7. |
| `/fill-workbook` | Fills the auditable workbook. |
| `/implementation-wizard` | Collects the 11 implementation guide inputs (wizard, manual or auto-fill). |
| `/generate-report` | Renders the PDF reports. |
| `/import-survey-devs` | Imports the anonymous Developer Survey. |
| `/insights-developer-survey` | Writes the Developer Survey insights report. |
| `/import-survey-learning` | Imports the Learning and Growth Survey. |
| `/training-plan` | Writes the training plan from the Learning Survey. |

## v1 archive

v1 is still supported for files without `metadata.framework_version`, or with a `1.x` version. It uses [framework.json](framework.json), 158 questions, 3 pillars, and archived assets:

- [collection/v1/](collection/v1/)
- [forms/v1/](forms/v1/)
- [reference/v1/](reference/v1/)

Use `make init-v1` to start a v1 input. The dispatching scripts keep v1 behavior unchanged.

## Repository map

| Path | Purpose |
| --- | --- |
| [collection/](collection/) | v2 form instructions, v2 spec, generated question banks, offline merge guidance, and v1 archive. |
| [forms/](forms/) | v2 offline form and archived v1 visual forms. |
| [framework/v2/](framework/v2/) | PT-BR and ES translations and the kit design choices that `make generate-v2` merges into `framework.v2.json`. |
| [reference/](reference/) | Framework guide, v2 calculator, per-dimension pages, branding, and examples. |
| [reports/](reports/) | Report renderer, templates, localization, comparison PDF, and wizard input parser. |
| [scripts/](scripts/) | Deterministic import, scoring, workbook, comparison, validation, demo, evidence, packaging, and generation scripts. |
| [survey-devs/](survey-devs/) | Anonymous Developer Survey: question banks, Forms instructions, rubric, scripts, and mock. |
| [survey-learning/](survey-learning/) | Identified Learning and Growth Survey: question banks, Forms instructions, scripts, and mock. |
| [wizard/](wizard/) | Generated trilingual implementation guide wizard and auto-fill script. |
| [.github/](.github/) | Copilot agent, prompt and skills that call the deterministic scripts. The repository also keeps the CI, Pages and release workflows here. |
| `docs/` | GitHub Pages site (repository only): landing page in EN, PT-BR and ES, and the public ZIP downloads built at deploy time. |
| `output/` | Generated files. Git ignores them and the packages leave them out. |

## Languages

English is the main language. Every doc has a Portuguese (Brazil) copy (`X.pt-br.md`) and a Spanish copy (`X.es.md`), linked from the language line at the top. The question banks, the v2 spec, the HTML helpers (offline form, wizard and calculator), the reports and the survey outputs work in EN, PT-BR and ES. The PT and ES packages ship every doc in their language under the base file names. The archived v1 material (reference docs, Forms instructions, question banks, visual forms and calculator) and the record of the v2 upgrade plan are in the three languages too. Only the Copilot customization files in `.github/` stay in English, by design; the assistant still answers in the user's language (see [Copilot Chat commands](#copilot-chat-commands)). `make validate-docs` fails if a copy is missing or its headings drift from the English doc. Every file and folder name is in English; a language copy only adds `.pt-br` or `.es` before the extension. Kits before 2.0.2 used Portuguese names (for example `coleta/` and `respostas.json`): the [CHANGELOG](CHANGELOG.md) lists every rename, and a `respostas.json` from an older kit is still read.

## Validation

```bash
make validate-docs
make test
make smoke
make smoke-cross
```

CI runs the tests, the documentation and generated-file checks, the v1 and v2 smoke tests and the demo on every push and pull request to `main` and `develop`. Every push to `main` also deploys the site with fresh ZIP downloads, and a push that changes kit files publishes a `kits-<run>` release with the same ZIPs. Run the checks locally before you push.
