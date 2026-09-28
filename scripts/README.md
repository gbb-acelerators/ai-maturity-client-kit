# `scripts/`: deterministic kit utilities

🌐 English · [Português (Brasil)](README.pt-br.md)

These scripts are the source of truth for import, scoring, workbook generation, comparison, evidence cross-checks, generated helpers, examples, packaging, and validation. Do not compute assessment outputs by hand.

## Main commands

| Command | Purpose |
| --- | --- |
| `python3 scripts/import_forms_excel.py respostas-forms.xlsx` | Import Microsoft Forms exports. Detects v2 by `R-Q#` and `D#-Q#` headers and preserves v1 import. |
| `python3 scripts/merge_offline_respostas.py exports/` | Merge one-respondent offline form exports into `respostas.json`. Refuses v1 files and mixed organizations unless explicitly allowed. |
| `python3 scripts/assessment_engine.py all` | Dispatches v2 or v1 and writes `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`. |
| `python3 scripts/fill_workbook.py` | Dispatches to the v2 workbook generator or archived v1 workbook flow. |
| `python3 scripts/compare_rounds.py BEFORE AFTER --pdf` | Compares v2 to v2, v1 to v1, or indicative v1 to v2 via `v1_lineage`, and writes `saida/comparacao-rodadas.pdf`. |
| `python3 scripts/run_demo.py` | Renders the 5 v2 PDFs, workbook, and JSONs from illustrative mock data under `saida/demo/` without touching `respostas.json`. |
| `python3 scripts/scan_repos_ai_config.py` | Writes `saida/repo-scan.json` from local clones or a GitHub organization. Used as an evidence cross-check for D4-Q4 and D4-Q5. |
| `python3 scripts/import_copilot_metrics.py` | Writes `saida/telemetria.json` from GitHub Copilot usage metrics exports. Used as an evidence cross-check for D4-Q1 and D9-Q1. |
| `python3 scripts/generate_v2_collection.py` | Generates v2 question banks, offline form, and import template. |
| `python3 scripts/generate_v2_tools_html.py` | Generates the v2 calculator and implementation guide wizard. `make validate-docs` runs it with `--check`. |
| `python3 scripts/generate_v2_reference.py` | Generates [../referencia/framework-v2.md](../referencia/framework-v2.md) and [../referencia/dimensoes/](../referencia/dimensoes/). |
| `python3 scripts/build_kit_docs.py` | Generates [../kit-en/](../kit-en/) from the English source docs and checks package docs. |
| `python3 scripts/build_v2_examples.py` | Regenerates [../referencia/exemplo-saida/](../referencia/exemplo-saida/) examples, including 5 PDFs per language, comparison PDF, workbook, repo scan, telemetry, surveys, and wizard input sample. |
| `python3 scripts/test_surveys.py` | Tests Developer Survey and Learning Survey parsing and output conventions. |
| `python3 scripts/validate_framework_v2.py` | Validates `framework.v2.json` against spec, schema, and translations. |

Fixtures for examples and tests live in [fixtures/](fixtures/).

## Make targets

Use `make install-deps`, `make demo [DEMO_LANG=en|pt-BR|es]`, `make init`, `make init-v1`, `make import XLSX=...`, `make merge DIR=...`, `make scores`, `make workbook`, `make pipeline`, `make compare BEFORE=... AFTER=...`, `make scan-repos REPOS=...`, `make scan-repos ORG=...`, `make telemetry METRICS=...`, `make examples-v2`, `make validate-v2`, `make validate-docs`, `make generate-v2`, `make mock-v2`, and `make test`.
