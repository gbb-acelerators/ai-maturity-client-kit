# Changelog

🌐 English · [Português (Brasil)](CHANGELOG.pt-br.md) · [Español](CHANGELOG.es.md)

All notable changes to the AI Maturity client kit. Dates are ISO 8601.

## [Unreleased]

### Added

- DORA metrics cross-check for D9-Q2: `make dora DORA=<CSV or JSON>
  [SERVICES=N]` runs `scripts/import_dora_metrics.py` and writes
  `output/dora-metrics.json` (one row per service and period, `baseline`
  and `current`). With the number of services in scope, the share of
  services compared with a baseline caps D9-Q2 by the coverage bands.
  The summary PDF shows it in section 2.2 and the implementation guide
  lists a mismatch as a risk. It checks measurement coverage, not
  delivery performance. The examples use
  `scripts/fixtures/dora-metrics.mock.csv`.

### Fixed

- PT-BR and ES Developer Survey insights now use a decimal comma.
- The v1 scoring guide called the PE score "Production Engineering";
  the code and reports mean Platform Engineering readiness, and the
  guide now lists the flagged v1 areas.
- The Learning Survey instructions pointed to v1 report names; they now
  describe how the plan feeds the v2 implementation guide. Plan file
  names use `<date>` everywhere.
- Spanish survey questions now open with "¿".
- Several PT-BR docs linked the English copy of a page that has a PT-BR
  twin.
- The Forms import log used an em dash for empty values.
- `.github/copilot-instructions.md` showed wrong flags for the evidence
  scripts (`--repos`, `--metrics`); it now uses `--path` and the
  positional metrics file, as the Makefile does.
- The Developer Survey insights said the survey used the same L0-L4 scale
  as the main assessment. They now say it uses the v1 bands, so compare
  with v2 by score. The rubric and the Forms instructions now point to
  the v2 questions in `survey_crosswalk` instead of v1 capabilities.
- The EN and ES Developer Survey banks ended with a section in
  Portuguese, and the EN and ES Learning Survey banks had a broken code
  fence.
- Survey docs and the report script help no longer mention the old
  `kit-cliente/` folder.
- The site quick start and FAQ still described the v1 example
  (`cp responses.json.example`, Cliente Exemplo S.A.) and the v1 import
  that averages rows. They now show `make demo`, `make init`,
  `make import` and `make merge`, and the v2 import that keeps each
  respondent.
- The repository moved to `gbb-acelerators/ai-maturity-client-kit`. The
  site, its SEO tags and the docs now use
  `https://gbb-acelerators.github.io/ai-maturity-client-kit/`; the old
  Pages URL returns 404.

## [2.0.2] - 2026-09-29 (English file and folder names)

The framework (questions, scale and scoring) is unchanged: it is still 2.0.1.

### Changed

- Every file and folder name is in English. Language copies only add
  `.pt-br` or `.es` before the extension. Renames:

| Before | Now |
| --- | --- |
| `coleta/` | `collection/` |
| `formularios/` | `forms/` |
| `referencia/`, `referencia/dimensoes/`, `referencia/exemplo-saida/` | `reference/`, `reference/dimensions/`, `reference/sample-output/` |
| `relatorios/` | `reports/` |
| `saida/` | `output/` |
| `respostas.json`, `respostas.json.example`, `respostas.v2.json.example` | `responses.json`, `responses.json.example`, `responses.v2.json.example` |
| `respostas-forms.xlsx`, `respostas-survey-devs.xlsx`, `respostas-survey-learning.xlsx` | `forms-responses.xlsx`, `survey-devs-responses.xlsx`, `survey-learning-responses.xlsx` |
| `GUIA-PASSO-A-PASSO.md` | `STEP-BY-STEP.md` |
| `INSTRUCOES-FORMS.md`, `INSTRUCOES-FORMS-DEVS.md`, `INSTRUCOES-FORMS-LEARNING.md` | `FORMS-INSTRUCTIONS.md`, `FORMS-INSTRUCTIONS-DEVS.md`, `FORMS-INSTRUCTIONS-LEARNING.md` |
| `perguntas-para-forms.md` (PT-BR), `.en.md`, `.es.md` and the `-devs` and `-learning` banks | `question-bank.md` (EN), `.pt-br.md`, `.es.md` and the `-devs` and `-learning` banks |
| `RUBRICA-MATURIDADE.md` | `MATURITY-RUBRIC.md` |
| `pontuacao-e-calculo.md` and `.xlsx`, `calculadora-pontuacao.html` | `scoring-and-calculation.md` and `.xlsx`, `scoring-calculator.html` |
| v1 `P1-produtividade-do-desenvolvedor`, `P2-ciclo-de-vida-devops`, `P3-plataforma-de-aplicações` | `P1-developer-productivity`, `P2-devops-lifecycle`, `P3-application-platform` |
| `recomendacoes.json`, `telemetria.json`, `comparacao-rodadas.*` | `recommendations.json`, `telemetry.json`, `round-comparison.*` |
| `pontuacao-v2-<date>.xlsx`, `pontuacao-preenchida-<date>.xlsx` | `scoring-v2-<date>.xlsx`, `scoring-v1-<date>.xlsx` |
| `maturidade-developer-survey-<date>.json`, `plano-capacitacao-<date>.md`, `*-EXEMPLO.*` | `developer-survey-maturity-<date>.json`, `training-plan-<date>.md`, `*-EXAMPLE.*` |
| `merge_offline_respostas.py`, `calcular_maturidade.py`, `gerar_insights.py`, `gerar_plano_capacitacao.py`, `auto_fill_from_plano.py` | `merge_offline_responses.py`, `calculate_maturity.py`, `generate_insights.py`, `generate_training_plan.py`, `auto_fill_from_plan.py` |
| `/calcular-scores`, `/gerar-relatorio`, `/importar-respostas-excel`, `/importar-survey-devs`, `/importar-survey-learning` | `/calculate-scores`, `/generate-report`, `/import-responses`, `/import-survey-devs`, `/import-survey-learning` |
| `/plano-capacitacao`, `/preencher-planilha`, `/recomendar-estrategias`, `/wizard-implementacao`, `/pipeline-completo` | `/training-plan`, `/fill-workbook`, `/recommend-strategies`, `/implementation-wizard`, `/full-pipeline` |
| `make clean-saida`, `--respostas`, `--plano` | `make clean-output`, `--responses`, `--plan` (the old flags still work) |

- The question banks follow the doc convention: the base file is
  English, with `.pt-br.md` and `.es.md` copies and a language line.
  Every package still ships the three banks.
- `kit-en/`, `kit-es/` and `scripts/build_kit_docs.py` were removed:
  every package now has the same file and folder names, with its
  language under the base names.
- The code uses English names too (for example the parsed
  `responses.json` is `responses_doc`), and the wizard auto-fill writes
  `metadata.source_plan` instead of `source_plano`.

### Compatibility

- A `respostas.json` from an older kit is still read when there is no
  `responses.json` (the scripts print a note asking to rename it).
- `.gitignore` and the package builder still exclude the old client
  file names and the old `saida/` folder, so older client data is never
  committed or packaged.

## [2.0.1] - 2026-09-28 (framework v2)

### Added

- v2 implementation guide (`v2_implementation_guide.pdf`, the fifth v2
  PDF): governance, dimension owners, a phased plan by priority with the
  lowest-scoring questions, "done when" L3 anchors, evidence to collect
  and KPIs, change management, risks derived from the scoring flags plus
  the client's risk register, success metrics and the first 90 days.
  Empty wizard fields show "to fill with the client".
- Implementation guide wizard and scoring calculator regenerated from
  `framework.v2.json` by `scripts/generate_v2_tools_html.py`, trilingual
  (EN, PT-BR, ES) and offline. The wizard has 11 fields (new:
  `dimension_owners`, `risk_register`); the calculator is a what-if view
  of section 8 (weights, targets, priorities, strategies, amplification
  risk) with a parity test against the engine. The template
  `wizard/implementation-guide-inputs.template.json` keeps guidance in
  `_guide` and empty values. `auto_fill_from_plan.py` supports ES and
  converts the calendar and cohorts into tables.
- Evidence cross-checks: `scripts/scan_repos_ai_config.py`
  (`make scan-repos`) places repositories on the RAMP levels [47] and
  caps D4-Q4 by the share with committed AI configuration;
  `scripts/import_copilot_metrics.py` (`make telemetry`) reads Copilot
  usage metrics reports [6] and caps D4-Q1 by the adoption phases. The
  summary PDF shows both and flags answers above the evidence.
- Respondent divergence flag (standard deviation of respondent dimension
  scores of 1.0 or more, with at least 3 respondents).
- Round comparison PDF (`make compare` renders `round-comparison.pdf`).
- `make demo` renders the five v2 PDFs from the mock into `output/demo/`;
  `make merge` combines offline-form exports into `responses.json`;
  `make examples-v2` regenerates the reference examples.
- Per-dimension reference pages in `reference/dimensions/` (EN, PT-BR,
  ES) and scope notes in the reference guide and the offline form.
- `survey_crosswalk` in `framework.v2.json` links each Developer Survey
  dimension to the v2 questions it helps validate; the summary PDF shows
  the survey context when a survey result exists.
- CI workflow (`.github/workflows/ci.yml`) for tests, generated files,
  packages, smoke tests and the demo.
- Developer Survey in three languages: the EN and ES banks translate the
  answer options, and `survey-devs/options.json` maps every language (and
  older Portuguese options with dashes) to the same canonical option, so
  scores do not depend on the form language. The insights show options in
  the report language.
- Spanish output for the survey scripts (`--lang es`) and Spanish plan
  headings in the wizard auto-fill; the ES example now shows the full flow.

- Framework v2: 9 dimensions, 61 questions and 5 profile questions
  (`R-Q1` to `R-Q5`), generated from
  [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md)
  into `framework.v2.json` by `scripts/spec_to_framework_v2.py`, with the
  kit design choices in `framework/v2/config.json` and translations in
  `framework/v2/i18n.{pt-br,es}.json`. JSON Schema in
  `framework.v2.schema.json`; `scripts/validate_framework_v2.py` checks
  counts, IDs, citations, the v1 traceability partition, language parity
  and staleness.
- v2 engine (`scripts/engine_v2.py`), selected by
  `metadata.framework_version` in `responses.json`: per-respondent
  answers, pooled question means, dimension weights (0.5 to 2.0),
  coverage status, low-confidence, amplification-risk, perception-gap and
  scope flags, evidence coverage with unverified L3/L4 questions, a top 5
  backlog with L3 anchors, and strategy recommendations that cite the
  spec references.
- v2 collection assets from `scripts/generate_v2_collection.py`: question
  banks in PT-BR, EN and ES, the offline form
  `forms/assessment-v2.html`, and the Forms export template.
- v2 reports (`reports/scripts/build_report_v2.py`): assessment
  summary with persona heatmap and flags, plus one roadmap per group of
  dimensions (G1 to G3). `make pipeline` picks v1 or v2 automatically.
- v2 auditable workbook (`scripts/fill_workbook_v2.py`): every score is
  a formula over the raw answers, next to the engine value.
- Round comparison (`scripts/compare_rounds.py`, `make compare`):
  v2 to v2, v1 to v1, and an indicative v1 to v2 baseline through the v1
  lineage.
- Illustrative v2 mock (`responses.v2.json.example`,
  `collection/v2-mock-forms-export.xlsx`), `CHANGELOG.md` and a dev
  container.

- Complete Portuguese (Brazil) and Spanish versions of every doc, with
  English as the main language: each `X.md` has `X.pt-br.md` and
  `X.es.md` with the same headings and a three-language switcher line.
  New Spanish copies of every folder guide, `CHANGELOG.pt-br.md`,
  `CHANGELOG.es.md`, and PT-BR and ES copies of the v2 spec
  (`collection/AI-Maturity-Form-Questions_v2.pt-br.md`, `.es.md`).
- `scripts/sync_spec_translations.py` generates sections 6 and 7 and the
  reference list of the spec copies from `framework.v2.json`, and checks
  that the English sections round-trip; `make generate-v2` and
  `make validate-docs` run it.
- Copies of the offline form, the wizard and the calculator that open in
  Portuguese and Spanish (`*.pt-br.html`, `*.es.html`). The offline form
  now follows the browser language, like the wizard and the calculator.
- `scripts/test_i18n_docs.py` covers the package language swap, the spec
  copies and the docs coverage.
- The archived v1 material in the three languages: Spanish pillar
  references (`reference/v1/P1` to `P3` `.es.md`) and Forms
  instructions (`collection/v1/FORMS-INSTRUCTIONS.es.md`); English and Spanish
  copies of the v1 visual forms (`forms/v1/*.html`, `*.es.html`,
  with the Portuguese original in `*.pt-br.html`) and a Spanish v1
  calculator. The PT-BR v1 docs and forms now also translate the context
  and the suggested evidence, which were in English; KPI names stay in
  English in every version, as in `framework.json`.
- PT-BR and ES copies of `upgrade-framework-v2.prompt.md`.
- "Copilot Chat commands" section in the README, in the three languages.

### Changed

- Developer Survey dimensions are `DS-D2` to `DS-D8` in outputs and in
  the Learning Survey bank, so they no longer collide with the v2
  dimensions; Forms built with the old text still parse. The survey
  rubric states that it keeps the v1 bands.
- `kit-en/` is generated from the English docs (`scripts/build_kit_docs.py`);
  packages ship every doc in their language and the build fails on broken
  relative links.
- Band and priority comparisons ignore floating-point noise below 1e-9 in
  the engine, the calculator and the workbook formulas.
- PT-BR and ES: translated profile options, clearer dimension names (D4,
  D5, D6) and comma decimals in the PDFs.
- Every HTML helper uses the Microsoft four-square logo.
- Survey banks, export templates and survey docs no longer use em or en
  dashes; generated survey Markdown passes Markdown lint and shows emails
  as links.
- Spec v2.0.1: form titles start with the question ID; scoring rules made
  precise (half-open bands, empty dimensions, weights, coverage,
  perception-gap groups, minimum sample, scope caveat, evidence rule);
  citation and traceability fixes (99 consolidated + 59 retired v1
  questions); no em or en dashes.
- `make init` now starts from the v2 example; `make init-v1` keeps the
  v1 flow.
- Author role in every output: "Global Developer Solutions Advisor".
- `scripts/import_forms_excel.py` detects v2 exports and keeps each
  respondent, profile answers in any of the three languages, and explicit
  NA answers.

- The ES package ships every doc in Spanish under the base file names,
  as the PT package does in Portuguese. `kit-es/` is generated from the
  `.es.md` copies, and no package ships the `kit-en/` or `kit-es/`
  folders. The v2 spec and the question banks ship in the three languages
  in every package.
- `scripts/check_language_coverage.py` requires the PT-BR and ES copies of
  every doc in scope, with matching headings and switcher lines, and lists
  what stays in English by design: `.github/`, the frozen v1 archive
  (EN and PT-BR), the internal v2 plan and generated outputs.
- Spanish generated texts (question bank, reference guide) use the "tú"
  register, and the Spanish bank links the Spanish Forms instructions.
  The PT-BR scoring reference no longer uses em or en dashes.
- The Copilot agent, instructions and pipeline prompt answer in the
  user's language and render outputs in the client's language
  (`metadata.language`, `--lang`); skill descriptions also list Spanish
  trigger phrases. The `.github/` files stay in English because the model
  reads them.
- The v1 EN and ES question banks carry the questions, pillar and
  capability names in their own language (the importer maps columns by
  ID), with dash-free options.
- `check_language_coverage.py` requires the three languages for the v1
  docs too and checks that every HTML helper has `.pt-br.html` and
  `.es.html` copies.

### Fixed

- v2 reference lists numbered sequentially instead of by reference
  number, so citations and list numbers did not match.
- EN and ES packages shipped their root guides with broken `../` links.
- The Developer Survey insights linked to v1 capabilities; they now link
  to v2 questions.
- `calculate_maturity.py --lang pt-br` failed on a dimension without data
  (missing text key).
- Six `SKILL.md` files had invalid YAML front matter.
- `reference/scoring-and-calculation.xlsx` stored explanatory text as broken
  formulas.
- The v1 EN calculator and EN question bank showed the Portuguese
  question texts; some v1 EN questions listed the audience "Arquiteto".
- The v1 example READMEs in `reference/sample-output/v1/en/` and `es/`
  were in the wrong language or pointed to old paths.
- The v1 calculator never updated the pillar and overall scores after the
  first answer (the pillar cards lost their marker classes), and the v1
  visual forms pointed to a missing branding CSS file.
- The Portuguese v1 docs, question bank, Forms instructions, visual forms
  and calculator no longer use em or en dashes as separators.

### Archived

- v1 question banks, instructions and template in `collection/v1/`, the v1
  HTML forms in `forms/v1/`, the v1 pillar references and the v1
  calculator in `reference/v1/`. v1 files still score and render
  unchanged.

## [1.x] - 2026-05 to 2026-09

- Deterministic engine, Forms importer and workbook with golden tests;
  client PDFs without sample facts; privacy notice for the learning
  survey; English as the default language with PT-BR copies; branch
  cleanup (only `main` and `develop`).
