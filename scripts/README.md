# `scripts/`: deterministic kit utilities

These scripts are the source of truth for import, scoring, workbook generation, comparison, and validation. Do not compute assessment outputs by hand.

## Main commands

| Command | Purpose |
| --- | --- |
| `python3 scripts/import_forms_excel.py respostas-forms.xlsx` | Import Microsoft Forms exports. Detects v2 by `R-Q#` and `D#-Q#` headers and preserves v1 import. |
| `python3 scripts/assessment_engine.py all` | Dispatches v2 or v1 and writes `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`. |
| `python3 scripts/fill_workbook.py` | Dispatches to the v2 workbook generator or archived v1 workbook flow. |
| `python3 scripts/compare_rounds.py BEFORE AFTER` | Compares v2 to v2, v1 to v1, or indicative v1 to v2 via `v1_lineage`. |
| `python3 scripts/generate_v2_collection.py` | Generates v2 question banks, offline form, and import template. |
| `python3 scripts/make_v2_mock.py` | Generates illustrative v2 mock responses and Forms export. |
| `python3 scripts/validate_framework_v2.py` | Validates `framework.v2.json` against spec, schema, and translations. |

## Make targets

Use `make init`, `make init-v1`, `make import XLSX=...`, `make scores`, `make workbook`, `make pipeline`, `make validate-v2`, `make generate-v2`, `make mock-v2`, `make compare BEFORE=... [AFTER=...]`, and `make test`.
