# Registro de cambios

🌐 [English](CHANGELOG.md) · [Português (Brasil)](CHANGELOG.pt-br.md) · Español

Todos los cambios notables del kit de cliente AI Maturity. Las fechas están en ISO 8601.

## [2.1.0] - 2026-09-29 (cross-check de métricas DORA, framework 2.0.2)

El framework pasa a 2.0.2 (ver Cambiado). La escala y la puntuación no
cambian, y las respuestas recopiladas con 2.0.1 se siguen importando,
combinando y puntuando.

### Agregado

- Cross-check de métricas DORA para D9-Q2: `make dora DORA=<CSV o JSON>
  [SERVICES=N]` ejecuta `scripts/import_dora_metrics.py` y escribe
  `output/dora-metrics.json` (una fila por servicio y período, `baseline`
  y `current`). Con el número de servicios en el alcance, la proporción
  de servicios comparados con un baseline limita D9-Q2 por las bandas de
  cobertura. El PDF de resumen lo muestra en la sección 2.2 y la guía de
  implementación lista el desajuste como riesgo. Verifica la cobertura
  de la medición, no el desempeño de entrega. Los ejemplos usan
  `scripts/fixtures/dora-metrics.mock.csv`.

### Cambiado

- Framework 2.0.2: el ancla L4 de D1-Q3 pide una evaluación por tipo de
  tarea, como indica la sección 2.1 de la spec para Pinna et al. [49]. Se
  regeneraron `framework.v2.json`, los bancos de preguntas, los
  formularios, la calculadora, el wizard, las páginas de referencia y los
  ejemplos.
- El README explica cómo obtener el kit (sitio, ZIPs, clon, requisitos) y
  lista todas las salidas y carpetas. El sitio muestra la versión y los
  cross-checks de evidencia, y una nueva pregunta del FAQ los explica.

### Corregido

- El sitio mostraba cifras de versiones anteriores: ahora indica 25-40 min
  por persona en el assessment, 20-25 min en la Developer Survey, al menos
  5 personas en la Learning Survey y los tamaños reales de los PDFs y del
  workbook. Se corrigieron los textos en PT-BR y ES, y las instrucciones de
  la Developer Survey usan una sola estimación de tiempo.
- Los insights de la Developer Survey en PT-BR y ES ahora usan coma
  decimal.
- La guía de scoring v1 llamaba al PE score "Production Engineering";
  el código y los reportes se refieren a la preparación de Platform
  Engineering, y la guía ahora lista las áreas v1 marcadas.
- Las instrucciones de la Learning Survey apuntaban a nombres de
  reportes v1; ahora describen cómo el plan alimenta la guía de
  implementación v2. Los nombres del archivo del plan usan `<date>` en
  todas partes.
- Las preguntas de las encuestas en español ahora abren con "¿".
- Varios docs PT-BR enlazaban la copia en inglés de una página que tiene
  versión PT-BR.
- El log de importación de Forms usaba raya para valores vacíos.
- La sección 10 de la spec v2 listaba acciones de herramientas
  pendientes que el kit ya implementa; ahora nombra el script que cubre
  cada elemento.
- `.github/copilot-instructions.md` mostraba flags incorrectas en los
  scripts de evidencia (`--repos`, `--metrics`); ahora usa `--path` y el
  archivo de métricas como argumento posicional, como el Makefile.
- Los insights del Developer Survey decían que la encuesta usaba la misma
  escala L0-L4 que la evaluación principal. Ahora dicen que usa las
  bandas de v1, así que la comparación con v2 es por puntaje. La rúbrica
  y las instrucciones de Forms ahora apuntan a las preguntas v2 de
  `survey_crosswalk`, no a capacidades de v1.
- Los bancos EN y ES del Developer Survey terminaban con una sección en
  portugués, y los bancos EN y ES del Learning Survey tenían un bloque de
  código roto.
- Los docs de las encuestas y la ayuda del script de informes ya no
  mencionan la antigua carpeta `kit-cliente/`.
- El quick start y el FAQ del sitio aún describían el ejemplo v1
  (`cp responses.json.example`, Cliente Exemplo S.A.) y la importación v1
  que promedia las filas. Ahora muestran `make demo`, `make init`,
  `make import` y `make merge`, y la importación v2 que conserva a cada
  persona encuestada.
- El repositorio pasó a `gbb-acelerators/ai-maturity-client-kit`. El
  sitio, sus etiquetas SEO y los docs ahora usan
  `https://gbb-acelerators.github.io/ai-maturity-client-kit/`; la URL
  anterior de Pages devuelve 404.
- El sitio enlazaba la tarjeta de LinkedIn al email, llamaba "3
  encuestas" a la evaluación y las dos encuestas, y describía el wizard
  como "Parte 4" (término de v1). La tarjeta de LinkedIn ahora abre
  LinkedIn, la sección dice "Evaluación + 2 encuestas complementarias" y
  el wizard apunta a la guía de implementación.
- Los docs, skills y textos de informes en inglés decían "capacitation
  plan"; ahora dicen "training plan". Los bancos del Developer Survey
  sugerían un subtítulo de 15-25 min; ahora es 20-25 min, como el resto
  de los docs.
- Las copias en español usaban la palabra portuguesa "respondente";
  ahora dicen "encuestado".
- El informe de justificación de puntaje v1 llamaba "D2-D8" a las
  dimensiones del Developer Survey; ahora dice `DS-D2` a `DS-D8`, para
  que no parezcan dimensiones v2. El banco ES del Developer Survey
  sugería un subtítulo en español que empezaba con "Survey".

## [2.0.2] - 2026-09-29 (nombres de archivos y carpetas en inglés)

El framework (preguntas, escala y puntuación) no cambia: sigue siendo 2.0.1.

### Cambiado

- Todos los nombres de archivos y carpetas están en inglés. Las copias
  de idioma solo agregan `.pt-br` o `.es` antes de la extensión.
  Cambios de nombre:

| Antes | Ahora |
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
| `perguntas-para-forms.md` (PT-BR), `.en.md`, `.es.md` y los bancos `-devs` y `-learning` | `question-bank.md` (EN), `.pt-br.md`, `.es.md` y los bancos `-devs` y `-learning` |
| `RUBRICA-MATURIDADE.md` | `MATURITY-RUBRIC.md` |
| `pontuacao-e-calculo.md` y `.xlsx`, `calculadora-pontuacao.html` | `scoring-and-calculation.md` y `.xlsx`, `scoring-calculator.html` |
| v1 `P1-produtividade-do-desenvolvedor`, `P2-ciclo-de-vida-devops`, `P3-plataforma-de-aplicações` | `P1-developer-productivity`, `P2-devops-lifecycle`, `P3-application-platform` |
| `recomendacoes.json`, `telemetria.json`, `comparacao-rodadas.*` | `recommendations.json`, `telemetry.json`, `round-comparison.*` |
| `pontuacao-v2-<date>.xlsx`, `pontuacao-preenchida-<date>.xlsx` | `scoring-v2-<date>.xlsx`, `scoring-v1-<date>.xlsx` |
| `maturidade-developer-survey-<date>.json`, `plano-capacitacao-<date>.md`, `*-EXEMPLO.*` | `developer-survey-maturity-<date>.json`, `training-plan-<date>.md`, `*-EXAMPLE.*` |
| `merge_offline_respostas.py`, `calcular_maturidade.py`, `gerar_insights.py`, `gerar_plano_capacitacao.py`, `auto_fill_from_plano.py` | `merge_offline_responses.py`, `calculate_maturity.py`, `generate_insights.py`, `generate_training_plan.py`, `auto_fill_from_plan.py` |
| `/calcular-scores`, `/gerar-relatorio`, `/importar-respostas-excel`, `/importar-survey-devs`, `/importar-survey-learning` | `/calculate-scores`, `/generate-report`, `/import-responses`, `/import-survey-devs`, `/import-survey-learning` |
| `/plano-capacitacao`, `/preencher-planilha`, `/recomendar-estrategias`, `/wizard-implementacao`, `/pipeline-completo` | `/training-plan`, `/fill-workbook`, `/recommend-strategies`, `/implementation-wizard`, `/full-pipeline` |
| `make clean-saida`, `--respostas`, `--plano` | `make clean-output`, `--responses`, `--plan` (las flags antiguas siguen funcionando) |

- Los bancos de preguntas siguen la convención de los docs: el archivo
  base está en inglés, con copias `.pt-br.md` y `.es.md` y una línea de
  idioma. Cada paquete sigue incluyendo los tres bancos.
- Se eliminaron `kit-en/`, `kit-es/` y `scripts/build_kit_docs.py`: todos
  los paquetes ahora tienen los mismos nombres de archivos y carpetas,
  con su idioma bajo los nombres base.
- El código también usa nombres en inglés (por ejemplo, el
  `responses.json` leído es `responses_doc`), y el auto-fill del wizard
  escribe `metadata.source_plan` en lugar de `source_plano`.

### Compatibilidad

- Un `respostas.json` de un kit anterior se sigue leyendo cuando no
  existe `responses.json` (los scripts muestran un aviso para
  renombrarlo).
- El `.gitignore` y el generador de paquetes siguen excluyendo los
  nombres antiguos de los archivos del cliente y la antigua carpeta
  `saida/`, así que los datos antiguos de clientes nunca entran en
  commits ni en paquetes.

## [2.0.1] - 2026-09-28 (framework v2)

### Agregado

- Guía de implementación v2 (`v2_implementation_guide.pdf`, el quinto PDF
  de v2): gobernanza, responsables de dimensión, un plan por fases según
  prioridad con las preguntas de menor puntaje, anclas L3 de "listo cuando",
  evidencia por recopilar y KPIs, gestión del cambio, riesgos derivados de las
  banderas de puntuación más el registro de riesgos del cliente, métricas de
  éxito y los primeros 90 días. Los campos vacíos del wizard muestran
  "to fill with the client".
- Wizard de guía de implementación y calculadora de puntuación regenerados a
  partir de `framework.v2.json` por `scripts/generate_v2_tools_html.py`,
  trilingües (EN, PT-BR, ES) y sin conexión. El wizard tiene 11 campos
  (nuevos: `dimension_owners`, `risk_register`); la calculadora es una vista
  what-if de la sección 8 (pesos, objetivos, prioridades, estrategias, riesgo
  de amplificación) con una prueba de paridad contra el motor. La plantilla
  `wizard/implementation-guide-inputs.template.json` mantiene orientación en
  `_guide` y valores vacíos. `auto_fill_from_plan.py` admite ES y convierte
  el calendario y las cohortes en tablas.
- Chequeos cruzados de evidencia: `scripts/scan_repos_ai_config.py`
  (`make scan-repos`) ubica los repositorios en los niveles RAMP [47] y limita
  D4-Q4 según la proporción con configuración de IA versionada;
  `scripts/import_copilot_metrics.py` (`make telemetry`) lee informes de
  métricas de uso de Copilot [6] y limita D4-Q1 según las fases de adopción.
  El PDF de resumen muestra ambos y marca respuestas por encima de la
  evidencia.
- Bandera de divergencia de personas encuestadas (desviación estándar de
  puntajes de dimensión por persona encuestada de 1.0 o más, con al menos 3
  personas encuestadas).
- PDF de comparación de rondas (`make compare` genera
  `round-comparison.pdf`).
- `make demo` genera los cinco PDFs de v2 desde el mock en `output/demo/`;
  `make merge` combina exportaciones de formularios sin conexión en
  `responses.json`; `make examples-v2` regenera los ejemplos de referencia.
- Páginas de referencia por dimensión en `reference/dimensions/` (EN, PT-BR,
  ES) y notas de alcance en la guía de referencia y el formulario sin conexión.
- `survey_crosswalk` en `framework.v2.json` vincula cada dimensión de
  Developer Survey con las preguntas de v2 que ayuda a validar; el PDF de
  resumen muestra el contexto de la encuesta cuando existe un resultado de
  encuesta.
- Workflow de CI (`.github/workflows/ci.yml`) para pruebas, archivos
  generados, paquetes, pruebas smoke y la demo.
- Developer Survey en tres idiomas: los bancos EN y ES traducen las opciones
  de respuesta, y `survey-devs/options.json` asigna cada idioma (y opciones
  anteriores en portugués con guiones) a la misma opción canónica, por lo que
  los puntajes no dependen del idioma del formulario. Los insights muestran
  opciones en el idioma del informe.
- Salida en español para los scripts de encuesta (`--lang es`) y encabezados
  de plan en español en el autocompletado del wizard; el ejemplo ES ahora
  muestra el flujo completo.

- Framework v2: 9 dimensiones, 61 preguntas y 5 preguntas de perfil
  (`R-Q1` a `R-Q5`), generado desde
  [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md)
  hacia `framework.v2.json` por `scripts/spec_to_framework_v2.py`, con las
  decisiones de diseño del kit en `framework/v2/config.json` y traducciones en
  `framework/v2/i18n.{pt-br,es}.json`. JSON Schema en
  `framework.v2.schema.json`; `scripts/validate_framework_v2.py` verifica
  conteos, IDs, citas, la partición de trazabilidad de v1, paridad de idioma y
  vigencia.
- Motor v2 (`scripts/engine_v2.py`), seleccionado por
  `metadata.framework_version` en `responses.json`: respuestas por persona
  encuestada, medias agrupadas de preguntas, pesos de dimensión (0.5 a 2.0),
  estado de cobertura, baja confianza, riesgo de amplificación, brecha de
  percepción y banderas de alcance, cobertura de evidencia con preguntas L3/L4
  no verificadas, un backlog top 5 con anclas L3 y recomendaciones de
  estrategia que citan las referencias de la especificación.
- Activos de recopilación v2 desde `scripts/generate_v2_collection.py`:
  bancos de preguntas en PT-BR, EN y ES, el formulario sin conexión
  `forms/assessment-v2.html` y la plantilla de exportación de Forms.
- Informes v2 (`reports/scripts/build_report_v2.py`): resumen de evaluación
  con mapa de calor de personas y banderas, más un roadmap por grupo de
  dimensiones (G1 a G3). `make pipeline` elige v1 o v2 automáticamente.
- Workbook auditable v2 (`scripts/fill_workbook_v2.py`): cada puntaje es una
  fórmula sobre las respuestas sin procesar, junto al valor del motor.
- Comparación de rondas (`scripts/compare_rounds.py`, `make compare`): v2 a
  v2, v1 a v1 y una línea base indicativa de v1 a v2 mediante el linaje de v1.
- Mock ilustrativo v2 (`responses.v2.json.example`,
  `collection/v2-mock-forms-export.xlsx`), `CHANGELOG.md` y un dev container.

- Versiones completas en portugués de Brasil y en español de todos los
  documentos, con el inglés como idioma principal: cada `X.md` tiene
  `X.pt-br.md` y `X.es.md` con los mismos títulos y una línea de selector
  con los tres idiomas. Nuevas copias en español de todas las guías de
  carpeta, `CHANGELOG.pt-br.md`, `CHANGELOG.es.md` y copias PT-BR y ES de
  la especificación v2 (`collection/AI-Maturity-Form-Questions_v2.pt-br.md`,
  `.es.md`).
- `scripts/sync_spec_translations.py` genera las secciones 6 y 7 y la
  lista de referencias de las copias de la especificación desde
  `framework.v2.json`, y verifica que las secciones en inglés hagan el
  viaje de ida y vuelta; `make generate-v2` y `make validate-docs` lo
  ejecutan.
- Copias del formulario offline, del wizard y de la calculadora que se
  abren en portugués y en español (`*.pt-br.html`, `*.es.html`). El
  formulario offline ahora sigue el idioma del navegador, como el wizard y
  la calculadora.
- `scripts/test_i18n_docs.py` cubre el cambio de idioma de los paquetes,
  las copias de la especificación y la cobertura de los documentos.
- El material archivado de v1 en los tres idiomas: referencias de los
  pilares en español (`reference/v1/P1` a `P3` `.es.md`) e instrucciones
  de Forms (`collection/v1/FORMS-INSTRUCTIONS.es.md`); copias en inglés y
  español de los formularios visuales de v1 (`forms/v1/*.html`,
  `*.es.html`, con el original en portugués en `*.pt-br.html`) y una
  calculadora v1 en español. Los docs y formularios v1 en PT-BR ahora
  también traducen el contexto y las evidencias sugeridas, que estaban en
  inglés; los nombres de KPI siguen en inglés en todas las versiones, como
  en `framework.json`.
- Copias PT-BR y ES de `upgrade-framework-v2.prompt.md`.
- Sección "Comandos de Copilot Chat" en el README, en los tres idiomas.

### Cambiado

- Las dimensiones de Developer Survey son `DS-D2` a `DS-D8` en las salidas y
  en el banco de Learning Survey, por lo que ya no colisionan con las
  dimensiones v2; los Forms creados con el texto anterior todavía se procesan.
  La rúbrica de la encuesta indica que conserva las bandas de v1.
- `kit-en/` se genera desde la documentación en inglés
  (`scripts/build_kit_docs.py`); los paquetes incluyen cada documento en su
  idioma y el build falla con enlaces relativos rotos.
- Las comparaciones de banda y prioridad ignoran ruido de punto flotante por
  debajo de 1e-9 en el motor, la calculadora y las fórmulas del workbook.
- PT-BR y ES: opciones de perfil traducidas, nombres de dimensión más claros
  (D4, D5, D6) y decimales con coma en los PDFs.
- Cada auxiliar HTML usa el logotipo de cuatro cuadrados de Microsoft.
- Los bancos de encuesta, plantillas de exportación y documentos de encuesta
  ya no usan guiones largos ni medios; el Markdown de encuesta generado pasa
  Markdown lint y muestra correos electrónicos como enlaces.
- Especificación v2.0.1: los títulos de formulario comienzan con el ID de la
  pregunta; las reglas de puntuación se hicieron precisas (bandas semiabiertas,
  dimensiones vacías, pesos, cobertura, grupos de brecha de percepción, muestra
  mínima, salvedad de alcance, regla de evidencia); correcciones de citas y
  trazabilidad (99 consolidadas + 59 preguntas de v1 retiradas); sin guiones
  largos ni medios.
- `make init` ahora empieza desde el ejemplo v2; `make init-v1` conserva el
  flujo v1.
- Rol de autor en cada salida: "Global Developer Solutions Advisor".
- `scripts/import_forms_excel.py` detecta exportaciones v2 y conserva cada
  persona encuestada, respuestas de perfil en cualquiera de los tres idiomas y
  respuestas NA explícitas.

- El paquete ES entrega todos los documentos en español con los nombres
  base de los archivos, como el paquete PT lo hace en portugués. `kit-es/`
  se genera desde las copias `.es.md`, y ningún paquete entrega las
  carpetas `kit-en/` o `kit-es/`. La especificación v2 y los bancos de
  preguntas van en los tres idiomas en todos los paquetes.
- `scripts/check_language_coverage.py` exige las copias PT-BR y ES de cada
  documento en alcance, con los mismos títulos y líneas de selector, y
  lista lo que queda en inglés por diseño: `.github/`, el archivo congelado
  de v1 (EN y PT-BR), el plan interno de v2 y las salidas generadas.
- Los textos generados en español (banco de preguntas, guía de referencia)
  usan el registro "tú", y el banco en español enlaza las instrucciones de
  Forms en español. La referencia de puntuación en PT-BR ya no usa rayas
  (em dash ni en dash).
- El agente, las instrucciones y el prompt de pipeline de Copilot
  responden en el idioma de quien los usa y generan las salidas en el
  idioma del cliente (`metadata.language`, `--lang`); las descripciones de
  las skills también incluyen frases de activación en español. Los
  archivos de `.github/` siguen en inglés porque los lee el modelo.
- Los bancos de preguntas v1 en EN y ES traen las preguntas y los nombres
  de pilares y capabilities en su propio idioma (el importador asocia las
  columnas por ID), con opciones sin rayas.
- `check_language_coverage.py` exige los tres idiomas también para los
  docs de v1 y verifica que cada asistente HTML tenga las copias
  `.pt-br.html` y `.es.html`.

### Corregido

- Las listas de referencia v2 se numeraban secuencialmente en lugar de por
  número de referencia, por lo que las citas y los números de lista no
  coincidían.
- Los paquetes EN y ES incluían sus guías raíz con enlaces `../` rotos.
- Los insights de Developer Survey enlazaban a capacidades de v1; ahora enlazan
  a preguntas de v2.
- `calculate_maturity.py --lang pt-br` fallaba en una dimensión sin datos
  (clave de texto faltante).
- Seis archivos `SKILL.md` tenían front matter YAML no válido.
- `reference/scoring-and-calculation.xlsx` almacenaba texto explicativo como
  fórmulas rotas.
- La calculadora v1 y el banco de preguntas v1 en inglés mostraban las
  preguntas en portugués; algunas preguntas v1 en inglés listaban la
  audiencia "Arquiteto".
- Los README del ejemplo v1 en `reference/sample-output/v1/en/` y `es/`
  estaban en el idioma equivocado o apuntaban a rutas antiguas.
- La calculadora v1 nunca actualizaba los puntajes de los pilares y el
  general después de la primera respuesta (las tarjetas de los pilares
  perdían sus clases de marcado), y los formularios visuales v1 apuntaban
  a un CSS de branding inexistente.
- Los docs, el banco de preguntas, las instrucciones de Forms, los
  formularios visuales y la calculadora de v1 en portugués ya no usan
  rayas (em dash ni en dash) como separadores.

### Archivado

- Bancos de preguntas, instrucciones y plantilla de v1 en `collection/v1/`, los
  formularios HTML de v1 en `forms/v1/`, las referencias de pilares de
  v1 y la calculadora de v1 en `reference/v1/`. Los archivos v1 todavía se
  puntúan y se generan sin cambios.

## [1.x] - 2026-05 to 2026-09

- Motor determinista, importador de Forms y workbook con pruebas golden; PDFs
  de cliente sin datos de ejemplo; aviso de privacidad para Learning Survey;
  inglés como idioma predeterminado con copias PT-BR; limpieza de ramas (solo
  `main` y `develop`).
