# `scripts/`: deterministic kit utilities

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

These scripts are the source of truth for import, scoring, workbook generation, comparison, evidence cross-checks, generated helpers, examples, packaging, and validation. Do not compute assessment outputs by hand.

## Main commands

| Command | Purpose |
| --- | --- |
| `python3 scripts/import_forms_excel.py forms-responses.xlsx` | Import Microsoft Forms exports. Detects v2 by `R-Q#` and `D#-Q#` headers and preserves v1 import. |
| `python3 scripts/merge_offline_responses.py exports/` | Merge one-respondent offline form exports into `responses.json`. Refuses v1 files and mixed organizations unless explicitly allowed. |
| `python3 scripts/assessment_engine.py all` | Dispatches v2 or v1 and writes `output/scores.json`, `output/gaps.json`, `output/recommendations.json`. |
| `python3 scripts/fill_workbook.py` | Dispatches to the v2 workbook generator or archived v1 workbook flow. |
| `python3 scripts/compare_rounds.py BEFORE AFTER --pdf` | Compares v2 to v2, v1 to v1, or indicative v1 to v2 via `v1_lineage`, and writes `output/round-comparison.pdf`. |
| `python3 scripts/run_demo.py` | Renders the 5 v2 PDFs, workbook, and JSONs from illustrative mock data under `output/demo/` without touching `responses.json`. |
| `python3 scripts/scan_repos_ai_config.py` | Writes `output/repo-scan.json` from local clones or a GitHub organization. Used as an evidence cross-check for D4-Q4 and D4-Q5. |
| `python3 scripts/import_copilot_metrics.py` | Writes `output/telemetry.json` from GitHub Copilot usage metrics exports. Used as an evidence cross-check for D4-Q1 and D9-Q1. |
| `python3 scripts/import_dora_metrics.py` | Writes `output/dora-metrics.json` from per-service DORA metrics (`baseline` and `current` periods). Used as an evidence cross-check for D9-Q2. |
| `python3 scripts/generate_v2_collection.py` | Generates v2 question banks, offline form (plus `.pt-br` and `.es` copies that open in those languages), and import template. |
| `python3 scripts/generate_v2_tools_html.py` | Generates the v2 calculator and implementation guide wizard (plus `.pt-br` and `.es` copies). `make validate-docs` runs it with `--check`. |
| `python3 scripts/generate_v2_reference.py` | Generates [../reference/framework-v2.md](../reference/framework-v2.md) and [../reference/dimensions/](../reference/dimensions/). |
| `python3 scripts/sync_spec_translations.py` | Generates sections 6 and 7 and the reference list of the PT-BR and ES copies of the v2 spec from `framework.v2.json`. `make validate-docs` runs it with `--check`. |
| `python3 scripts/check_language_coverage.py` | Checks that every doc has EN, PT-BR and ES versions with the same headings and language switcher, and lists what stays English by design. |
| `python3 scripts/build_language_kits.py` | Builds the PT, EN and ES ZIPs (`make build-kits`). Each package ships its language under the base file names. |
| `python3 scripts/build_v2_examples.py` | Regenerates [../reference/sample-output/](../reference/sample-output/) examples, including 5 PDFs per language, comparison PDF, workbook, repo scan, telemetry, DORA metrics, surveys, and wizard input sample. |
| `python3 scripts/test_surveys.py` | Tests Developer Survey and Learning Survey parsing and output conventions. |
| `python3 scripts/validate_framework_v2.py` | Validates `framework.v2.json` against spec, schema, and translations. |

Fixtures for examples and tests live in [fixtures/](fixtures/).

## Make targets

Use `make install-deps`, `make demo [DEMO_LANG=en|pt-BR|es]`, `make init`, `make init-v1`, `make import XLSX=...`, `make merge DIR=...`, `make scores`, `make workbook`, `make pipeline`, `make compare BEFORE=... AFTER=...`, `make scan-repos REPOS=...`, `make scan-repos ORG=...`, `make telemetry METRICS=...`, `make dora DORA=...`, `make examples-v2`, `make validate-v2`, `make validate-docs`, `make generate-v2`, `make mock-v2`, `make build-kits`, and `make test`.
