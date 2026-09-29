# `scripts/`: utilidades determinísticas del kit

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Estos scripts son la fuente de verdad para importación, puntuación, generación de workbook, comparación, verificaciones cruzadas de evidencia, helpers generados, ejemplos, empaquetado y validación. No calcules salidas de evaluación a mano.

## Comandos principales

| Comando | Propósito |
| --- | --- |
| `python3 scripts/import_forms_excel.py forms-responses.xlsx` | Importa exportaciones de Microsoft Forms. Detecta v2 por headers `R-Q#` y `D#-Q#` y preserva la importación v1. |
| `python3 scripts/merge_offline_responses.py exports/` | Combina exportaciones de formulario offline de una persona encuestada en `responses.json`. Rechaza archivos v1 y organizaciones mezcladas salvo que se permita explícitamente. |
| `python3 scripts/assessment_engine.py all` | Despacha v2 o v1 y escribe `output/scores.json`, `output/gaps.json`, `output/recommendations.json`. |
| `python3 scripts/fill_workbook.py` | Despacha al generador de workbook v2 o al flujo de workbook v1 archivado. |
| `python3 scripts/compare_rounds.py BEFORE AFTER --pdf` | Compara v2 con v2, v1 con v1, o v1 indicativo con v2 vía `v1_lineage`, y escribe `output/round-comparison.pdf`. |
| `python3 scripts/run_demo.py` | Renderiza los 5 PDFs v2, workbook y JSONs desde datos mock ilustrativos bajo `output/demo/` sin tocar `responses.json`. |
| `python3 scripts/scan_repos_ai_config.py` | Escribe `output/repo-scan.json` desde clones locales o una organización de GitHub. Se usa como verificación cruzada de evidencia para D4-Q4 y D4-Q5. |
| `python3 scripts/import_copilot_metrics.py` | Escribe `output/telemetry.json` desde exportaciones de métricas de uso de GitHub Copilot. Se usa como verificación cruzada de evidencia para D4-Q1 y D9-Q1. |
| `python3 scripts/import_dora_metrics.py` | Escribe `output/dora-metrics.json` desde métricas DORA por servicio (períodos `baseline` y `current`). Se usa como verificación cruzada de evidencia para D9-Q2. |
| `python3 scripts/generate_v2_collection.py` | Genera bancos de preguntas v2, formulario offline (más copias `.pt-br` y `.es` que se abren en esos idiomas) y plantilla de importación. |
| `python3 scripts/generate_v2_tools_html.py` | Genera la calculadora v2 y el wizard de guía de implementación (más copias `.pt-br` y `.es`). `make validate-docs` lo ejecuta con `--check`. |
| `python3 scripts/generate_v2_reference.py` | Genera [../reference/framework-v2.es.md](../reference/framework-v2.es.md) y [../reference/dimensions/](../reference/dimensions/). |
| `python3 scripts/sync_spec_translations.py` | Genera las secciones 6 y 7 y la lista de referencias de las copias PT-BR y ES de la especificación v2 desde `framework.v2.json`. `make validate-docs` lo ejecuta con `--check`. |
| `python3 scripts/check_language_coverage.py` | Revisa que cada doc tenga versiones EN, PT-BR y ES con los mismos headings y switcher de idioma, y lista lo que permanece en inglés por diseño. |
| `python3 scripts/build_language_kits.py` | Construye los ZIPs PT, EN y ES (`make build-kits`). Cada paquete incluye su idioma bajo los nombres de archivo base. |
| `python3 scripts/build_v2_examples.py` | Regenera ejemplos en [../reference/sample-output/](../reference/sample-output/), incluidos 5 PDFs por idioma, PDF de comparación, workbook, escaneo de repo, telemetría, métricas DORA, encuestas y muestra de entrada del wizard. |
| `python3 scripts/test_surveys.py` | Prueba parsing y convenciones de salida de Developer Survey y Learning Survey. |
| `python3 scripts/validate_framework_v2.py` | Valida `framework.v2.json` contra especificación, esquema y traducciones. |

Los fixtures para ejemplos y pruebas viven en [fixtures/](fixtures/).

## Targets de Make

Usa `make install-deps`, `make demo [DEMO_LANG=en|pt-BR|es]`, `make init`, `make init-v1`, `make import XLSX=...`, `make merge DIR=...`, `make scores`, `make workbook`, `make pipeline`, `make compare BEFORE=... AFTER=...`, `make scan-repos REPOS=...`, `make scan-repos ORG=...`, `make telemetry METRICS=...`, `make dora DORA=...`, `make examples-v2`, `make validate-v2`, `make validate-docs`, `make generate-v2`, `make mock-v2`, `make build-kits` y `make test`.
