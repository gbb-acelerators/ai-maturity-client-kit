# Changelog

All notable changes to the AI Maturity client kit. Dates are ISO 8601.

## [2.0.1] - 2026-09-27 (framework v2)

### Added

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

### Changed

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

### Fixed

- Six `SKILL.md` files had invalid YAML front matter.
- `referencia/pontuacao-e-calculo.xlsx` stored explanatory text as broken
  formulas.

### Archived

- v1 question banks, instructions and template in `coleta/v1/`, the v1
  HTML forms in `formularios/v1/`, and the v1 pillar references in
  `referencia/v1/`. v1 files still score and render unchanged.

## [1.x] - 2026-05 to 2026-09

- Deterministic engine, Forms importer and workbook with golden tests;
  client PDFs without sample facts; privacy notice for the learning
  survey; English as the default language with PT-BR copies; branch
  cleanup (only `main` and `develop`).
