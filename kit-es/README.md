<!-- Generated from README.es.md by scripts/build_kit_docs.py. Edit the source, not this file. -->
# Kit cliente AI Maturity Assessment

Un kit autónomo para ejecutar una autoevaluación de madurez del SDLC asistido por IA sin depender de una plataforma web. Framework v2 es el valor predeterminado. Framework v1 sigue archivado y soportado para entradas históricas.

Rol de la autora: Global Developer Solutions Advisor.

Consulta [CHANGELOG.md](../CHANGELOG.es.md) para el historial de versiones.

## Qué hay de nuevo en framework v2

- Versión: 2.0.1.
- Especificación: [coleta/AI-Maturity-Form-Questions_v2.es.md](../coleta/AI-Maturity-Form-Questions_v2.es.md), traducción de la fuente en inglés [coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md).
- Modelo de máquina: [framework.v2.json](../framework.v2.json), validado por [framework.v2.schema.json](../framework.v2.schema.json) y [scripts/validate_framework_v2.py](../scripts/validate_framework_v2.py).
- 5 preguntas de perfil y 61 preguntas puntuadas.
- 9 dimensiones: D1 Estrategia, Política y Gobernanza de IA (7), D2 Habilitación, Habilidades y Cultura (6), D3 Planificar, Especificar y Diseñar (6), D4 Código e ingeniería de contexto (8), D5 Revisión, calidad y pruebas (7), D6 Seguridad y cadena de suministro de IA (7), D7 Entregar y Operar (6), D8 Fundamentos de Ingeniería (amplificadores de IA) (7), D9 Medición, Valor y AI FinOps (7).
- Los IDs usan `D#-Q#`. Los IDs de perfil usan `R-Q1` a `R-Q5`.
- Niveles: L0 No iniciado, L1 Explorando, L2 Adoptando, L3 Escalando, L4 Nativo en IA, más `NA`.
- Formulario principal: [formularios/assessment-v2.html](../formularios/assessment-v2.es.html). Se ejecuta offline, muestra la nota de alcance de cada pregunta y exporta una persona por `respostas.json`.
- Configuración de Forms: [coleta/INSTRUCOES-FORMS.md](INSTRUCCIONES-FORMS.md).
- Las páginas de referencia por dimensión están en [referencia/dimensoes/](../referencia/dimensoes/README.es.md), con páginas EN, PT-BR y ES para D1 a D9.

## Quickstart

Ruta más rápida para obtener un primer PDF después de `make install-deps`, o dentro del dev container:

```bash
make demo
open saida/demo/*.pdf
```

Usa `DEMO_LANG=en`, `DEMO_LANG=pt-BR` o `DEMO_LANG=es` para elegir el idioma de la demo. La demo escribe salidas ilustrativas en `saida/demo/` y no toca `respostas.json`.

Flujo real de evaluación:

```bash
make install-deps
# Recolecta con Microsoft Forms, o recolecta exports offline y únelos:
make merge DIR=exports/
# O importa un export de Microsoft Forms:
make import XLSX=respostas-forms.xlsx
make pipeline
# Cross-checks opcionales de evidencia:
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
# Llena implementation-guide-inputs.json con el wizard, luego renderiza de nuevo:
make pipeline
```

Los comandos directos siguen disponibles para automatización:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Salidas para v2

| Salida | Propósito |
| --- | --- |
| `saida/scores.json` | Scores por pregunta, dimensión, persona y general cuando el engine los produce. |
| `saida/gaps.json` | Gaps de dimensión, prioridades, flags, divergencia entre personas encuestadas e insumos de backlog. |
| `saida/recomendacoes.json` | Recomendaciones de estrategias `S1` a `S7`. |
| `saida/pontuacao-v2-<date>.xlsx` | Workbook auditable con fórmulas y cross-check del engine. |
| `saida/payload_v2.json` | Payload del reporte para inspección y customización. |
| `saida/v2_assessment_summary.pdf` | Resumen ejecutivo, con cross-checks de evidencia cuando están disponibles. |
| `saida/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `saida/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `saida/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |
| `saida/v2_implementation_guide.pdf` | Parte 4 para v2: gobernanza, RACI, plan por fases, gestión del cambio, riesgos, métricas, primeros 90 días y referencias. |
| `saida/comparacao-rodadas.pdf` | Reporte de comparación de `make compare BEFORE=old.json AFTER=respostas.json`. |

`make pipeline` renderiza los 5 PDFs v2. v1 sigue renderizando su conjunto archivado de 5 PDFs.

## Resumen de puntuación

Los scripts son la fuente de verdad. No calcules scores a mano.

- Score de pregunta: media agrupada de niveles de las personas encuestadas, excluyendo vacío y `NA`.
- Score de dimensión: media de los scores de sus preguntas.
- General: media ponderada de dimensiones.
- Los pesos de dimensión son `1.0` por defecto y pueden definirse de `0.5` a `2.0` en `respostas.json`.
- Cobertura: OK con 37 o más preguntas respondidas, WARNING con 25 a 36, BLOCKED por debajo de 25.
- Prioridad: `peso de dimensión x gap`; P0 en `>= 2.4`, P1 en `>= 1.6`, P2 en `>= 0.9`, si no P3. Las comparaciones de banda y prioridad ignoran ruido de punto flotante por debajo de `1e-9`.
- Divergencia entre personas encuestadas: se marca una dimensión cuando al menos 3 personas tienen score y la desviación estándar de sus propios scores de dimensión es 1,0 o más.

## Cross-checks de evidencia

Dos insumos opcionales ayudan a cuestionar respuestas demasiado confiadas. No cambian los scores.

- `make scan-repos REPOS=~/src` escanea clones locales usando solo archivos con commit. `make scan-repos ORG=<github-org>` escanea branches predeterminadas mediante la API REST de GitHub y requiere `GITHUB_TOKEN` o `GH_TOKEN`. Salida: `saida/repo-scan.json`. El scan ubica repositorios en niveles RAMP L1 a L4 como aproximación basada en patrones. La proporción de repositorios en L2+ limita D4-Q4 por bandas de cobertura, y la proporción en L3+ aparece junto a D4-Q5.
- `make telemetry METRICS=<Copilot usage metrics report JSON/NDJSON> [SEATS=200]` escribe `saida/telemetria.json`. Lee exports de métricas de uso de GitHub Copilot y clasifica fases de adopción: No Cohort, Phase 1 Code first, Phase 2 Agent first, Phase 3 Multi-agent. El export en sí es evidencia para D9-Q1.

La sección 2.2 del PDF de resumen muestra ambos cross-checks y marca respuestas por encima de lo que la evidencia soporta. La guía de implementación lista esos desajustes como riesgos. Si faltan los archivos, el reporte explica cómo producirlos.

## Surveys complementarios

Developer Survey y Learning and Growth Survey son señales complementarias. Los resultados de survey nunca cambian los scores v2.

- Las dimensiones del Developer Survey se llaman `DS-D2` a `DS-D8` en las salidas. Forms construidos con el texto antiguo `D2` todavía se parsean.
- `framework.v2.json` contiene el crosswalk desde cada `DS-D#` hacia las preguntas v2 que ayuda a validar.
- El PDF de resumen v2 muestra contexto del Developer Survey cuando existe `saida/maturidade-developer-survey-*.json`.
- La rúbrica del survey conserva las bandas v1, así que compara por score, no por nombre de nivel.
- Los scripts de survey escriben EN, PT-BR o ES (`--lang en|pt-br|es`). Los bancos del Developer Survey traducen las opciones de respuesta en todos los idiomas; `survey-devs/options.json` las asigna a las mismas opciones canónicas, así que el puntaje no depende del idioma del formulario.

## Comandos de Copilot Chat

Abre la carpeta del kit en VS Code con GitHub Copilot y usa Copilot Chat en modo Agent. El asistente responde en tu idioma (inglés, portugués de Brasil o español) y genera las salidas en el idioma del cliente (`metadata.language` en `respostas.json`, `--lang` en los scripts de las encuestas). Los archivos de instrucciones en [.github/](../.github/) quedan en inglés por diseño: los lee el modelo, no el cliente.

| Comando | Qué hace |
| --- | --- |
| `@ai-maturity-assistant` | Agente concierge: revisa el workspace y ejecuta o sugiere el siguiente paso. |
| `/pipeline-completo` | Pipeline completo, desde `respostas.json` hasta el workbook y los PDFs. |
| `/ai-maturity-reports` | Wrapper del pipeline de informes (v2 por defecto, entradas v1 archivadas soportadas). |
| `/importar-respostas-excel` | Importa una exportación de Microsoft Forms o combina exportaciones del formulario offline en `respostas.json`. |
| `/calcular-scores` | Calcula los puntajes con el engine determinístico. |
| `/gap-analysis` | Calcula brechas y prioridades de P0 a P3. |
| `/recomendar-estrategias` | Asocia las prioridades con las estrategias S1 a S7. |
| `/preencher-planilha` | Llena el workbook auditable. |
| `/wizard-implementacao` | Recoge las 11 entradas de la guía de implementación (wizard, manual o auto-fill). |
| `/gerar-relatorio` | Genera los informes en PDF. |
| `/importar-survey-devs` | Importa el Developer Survey anónimo. |
| `/insights-developer-survey` | Genera el informe de insights del Developer Survey. |
| `/importar-survey-learning` | Importa el Learning and Growth Survey. |
| `/plano-capacitacao` | Genera el plan de capacitación a partir del Learning Survey. |

## Archivo v1

v1 sigue soportado para archivos sin `metadata.framework_version`, o con versión `1.x`. Usa [framework.json](../framework.json), 158 preguntas, 3 pilares y activos archivados:

- [coleta/v1/](../coleta/v1/)
- [formularios/v1/](../formularios/v1/)
- [referencia/v1/](../referencia/v1/)

Usa `make init-v1` para iniciar una entrada v1. Los scripts de despacho mantienen el comportamiento v1 sin cambios.

## Mapa del repositorio

| Ruta | Propósito |
| --- | --- |
| [coleta/](../coleta/) | Instrucciones v2, especificación v2, bancos generados, guía de merge offline y archivo v1. |
| [formularios/](../formularios/) | Formulario offline v2 y formularios visuales v1 archivados. |
| [referencia/](../referencia/) | Guía del framework, calculadora v2, páginas por dimensión, branding y ejemplos. |
| [relatorios/](../relatorios/) | Renderer, templates, localización, PDF de comparación y parser de entradas del wizard. |
| [scripts/](../scripts/) | Scripts determinísticos de importación, scoring, workbook, comparación, validación, demo, evidencia, empaquetado y generación. |
| [wizard/](../wizard/) | Wizard trilingüe generado de la guía de implementación y script de auto-fill. |
| [.github/skills/](../.github/skills/) | Skills custom de Copilot que llaman scripts determinísticos. |

## Idiomas

El inglés es el idioma principal. Cada documento tiene una copia en portugués de Brasil (`X.pt-br.md`) y una en español (`X.es.md`), enlazadas en la línea de idioma del inicio. Los bancos de preguntas, la especificación v2, los asistentes HTML (formulario offline, wizard y calculadora), los informes y las salidas de las encuestas funcionan en EN, PT-BR y ES. Los paquetes PT y ES entregan todos los documentos en su idioma con los nombres base de los archivos. El material archivado de v1 (docs de referencia, instrucciones de Forms, bancos de preguntas, formularios visuales y calculadora) y el registro del plan de actualización a v2 también están en los tres idiomas. Solo los archivos de customización de Copilot en `.github/` quedan en inglés, por diseño; aun así el asistente responde en el idioma de quien lo usa (ver [Comandos de Copilot Chat](#comandos-de-copilot-chat)). `make validate-docs` falla si falta una copia o si sus títulos se apartan del documento en inglés.

## Validación

```bash
python3 scripts/build_kit_docs.py
python3 scripts/build_kit_docs.py --check
make validate-docs
make test
```

CI está configurado para tests, validación de documentación, smoke rendering y demo en push y pull requests a `main` y `develop`. GitHub Actions puede estar bloqueado por billing en el repositorio, así que trata la validación local como obligatoria.
