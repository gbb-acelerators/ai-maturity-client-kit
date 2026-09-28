# Changelog

🌐 English · [Português (Brasil)](CHANGELOG.pt-br.md) · [Español](CHANGELOG.es.md)

All notable changes to the AI Maturity client kit. Dates are ISO 8601.

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
  `_guide` and empty values. `auto_fill_from_plano.py` supports ES and
  converts the calendar and cohorts into tables.
- Evidence cross-checks: `scripts/scan_repos_ai_config.py`
  (`make scan-repos`) places repositories on the RAMP levels [47] and
  caps D4-Q4 by the share with committed AI configuration;
  `scripts/import_copilot_metrics.py` (`make telemetry`) reads Copilot
  usage metrics reports [6] and caps D4-Q1 by the adoption phases. The
  summary PDF shows both and flags answers above the evidence.
- Respondent divergence flag (standard deviation of respondent dimension
  scores of 1.0 or more, with at least 3 respondents).
- Round comparison PDF (`make compare` renders `comparacao-rodadas.pdf`).
- `make demo` renders the five v2 PDFs from the mock into `saida/demo/`;
  `make merge` combines offline-form exports into `respostas.json`;
  `make examples-v2` regenerates the reference examples.
- Per-dimension reference pages in `referencia/dimensoes/` (EN, PT-BR,
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
  [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md)
  into `framework.v2.json` by `scripts/spec_to_framework_v2.py`, with the
  kit design choices in `framework/v2/config.json` and translations in
  `framework/v2/i18n.{pt-br,es}.json`. JSON Schema in
  `framework.v2.schema.json`; `scripts/validate_framework_v2.py` checks
  counts, IDs, citations, the v1 traceability partition, language parity
  and staleness.
- v2 engine (`scripts/engine_v2.py`), selected by
  `metadata.framework_version` in `respostas.json`: per-respondent
  answers, pooled question means, dimension weights (0.5 to 2.0),
  coverage status, low-confidence, amplification-risk, perception-gap and
  scope flags, evidence coverage with unverified L3/L4 questions, a top 5
  backlog with L3 anchors, and strategy recommendations that cite the
  spec references.
- v2 collection assets from `scripts/generate_v2_collection.py`: question
  banks in PT-BR, EN and ES, the offline form
  `formularios/assessment-v2.html`, and the Forms export template.
- v2 reports (`relatorios/scripts/build_report_v2.py`): assessment
  summary with persona heatmap and flags, plus one roadmap per group of
  dimensions (G1 to G3). `make pipeline` picks v1 or v2 automatically.
- v2 auditable workbook (`scripts/fill_workbook_v2.py`): every score is
  a formula over the raw answers, next to the engine value.
- Round comparison (`scripts/compare_rounds.py`, `make compare`):
  v2 to v2, v1 to v1, and an indicative v1 to v2 baseline through the v1
  lineage.
- Illustrative v2 mock (`respostas.v2.json.example`,
  `coleta/v2-mock-forms-export.xlsx`), `CHANGELOG.md` and a dev
  container.

- Complete Portuguese (Brazil) and Spanish versions of every doc, with
  English as the main language: each `X.md` has `X.pt-br.md` and
  `X.es.md` with the same headings and a three-language switcher line.
  New Spanish copies of every folder guide, `CHANGELOG.pt-br.md`,
  `CHANGELOG.es.md`, and PT-BR and ES copies of the v2 spec
  (`coleta/AI-Maturity-Form-Questions_v2.pt-br.md`, `.es.md`).
- `scripts/sync_spec_translations.py` generates sections 6 and 7 and the
  reference list of the spec copies from `framework.v2.json`, and checks
  that the English sections round-trip; `make generate-v2` and
  `make validate-docs` run it.
- Copies of the offline form, the wizard and the calculator that open in
  Portuguese and Spanish (`*.pt-br.html`, `*.es.html`). The offline form
  now follows the browser language, like the wizard and the calculator.
- `scripts/test_i18n_docs.py` covers the package language swap, the spec
  copies and the docs coverage.

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

### Fixed

- v2 reference lists numbered sequentially instead of by reference
  number, so citations and list numbers did not match.
- EN and ES packages shipped their root guides with broken `../` links.
- The Developer Survey insights linked to v1 capabilities; they now link
  to v2 questions.
- `calcular_maturidade.py --lang pt-br` failed on a dimension without data
  (missing text key).
- Six `SKILL.md` files had invalid YAML front matter.
- `referencia/pontuacao-e-calculo.xlsx` stored explanatory text as broken
  formulas.

### Archived

- v1 question banks, instructions and template in `coleta/v1/`, the v1
  HTML forms in `formularios/v1/`, the v1 pillar references and the v1
  calculator in `referencia/v1/`. v1 files still score and render
  unchanged.

## [1.x] - 2026-05 to 2026-09

- Deterministic engine, Forms importer and workbook with golden tests;
  client PDFs without sample facts; privacy notice for the learning
  survey; English as the default language with PT-BR copies; branch
  cleanup (only `main` and `develop`).
