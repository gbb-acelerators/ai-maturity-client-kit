# Salidas de ejemplo

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Cada archivo aquí es generado por `python3 scripts/build_v2_examples.py` a partir de entradas ilustrativas: el mock `respostas.v2.json.example` (14 personas encuestadas, Contoso Engineering), los mocks de encuestas complementarias, repositorios fixture generados y `scripts/fixtures/copilot-usage-organization-28-day.mock.json`. Nada de esto es dato real de cliente. No edites estos archivos a mano.

La raíz de la carpeta contiene el ejemplo PT-BR. [en/](en/) y [es/](es/) contienen los mismos PDFs en inglés y español. El ejemplo v1 archivado está en [v1/](v1/).

## Informes v2 (PDF)

| Archivo | Contenido |
| --- | --- |
| `v2_assessment_summary.pdf` | Resultado general, alertas, heatmap de personas, verificaciones cruzadas de evidencia, contexto del Developer Survey, backlog, estrategias, referencias |
| `v2_roadmap_g1.pdf` | G1: D1, D2, D9 |
| `v2_roadmap_g2.pdf` | G2: D3, D4, D5 |
| `v2_roadmap_g3.pdf` | G3: D6, D7, D8 |
| `v2_implementation_guide.pdf` | Gobernanza, plan faseado por prioridad, gestión del cambio, riesgos de las alertas, métricas de éxito y los primeros 90 días |
| `comparacao-rodadas.pdf` | Comparación de rondas desde el ejemplo v1 al mock v2 (baseline indicativo mediante el linaje v1) |

Las guías de implementación en los tres idiomas usan entradas del wizard llenadas por `wizard/scripts/auto_fill_from_plano.py` desde el mock de Learning and Growth Survey. Para los ejemplos EN y ES, los mocks de encuesta se responden como si los formularios se hubieran construido en ese idioma (opciones traducidas mediante los bancos y `survey-devs/options.json`); las respuestas de texto libre permanecen como fueron escritas.

## Archivos de datos

| Archivo | Contenido |
| --- | --- |
| `scores.json`, `gaps.json`, `recomendacoes.json` | Salidas del motor (EN) |
| `payload_v2.json` | Payload del informe (EN) |
| `repo-scan.json` | `scripts/scan_repos_ai_config.py` en 12 repositorios fixture (niveles RAMP [47]) |
| `telemetria.json` | `scripts/import_copilot_metrics.py` sobre el mock de métricas de uso de Copilot |
| `comparacao-rodadas.json` | Resultado de `scripts/compare_rounds.py` detrás del PDF de comparación |
| `pontuacao-v2-EXEMPLO.xlsx` | Workbook auditable de fórmulas (PT-BR) |
| `maturidade-developer-survey-EXEMPLO.json`, `insights-developer-survey-EXEMPLO.md` | Salidas de Developer Survey (PT-BR), dimensiones `DS-D2` a `DS-D8` |
| `plano-capacitacao-EXEMPLO.md` | Plan de capacitación de Learning and Growth Survey (PT-BR) |
| `implementation-guide-inputs-EXEMPLO.json` | Entradas del wizard llenadas automáticamente desde el plan de capacitación (PT-BR) |

Grupos de informe: G1 = D1, D2, D9; G2 = D3, D4, D5; G3 = D6, D7, D8.

## Archivo v1

[v1/](v1/) conserva el layout v1 archivado y ejemplos para el framework de 158 preguntas y 3 pilares.
