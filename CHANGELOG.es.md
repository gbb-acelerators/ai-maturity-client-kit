# Registro de cambios

🌐 [English](CHANGELOG.md) · [Português (Brasil)](CHANGELOG.pt-br.md) · Español

Todos los cambios notables del kit de cliente AI Maturity. Las fechas están en ISO 8601.

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
  `_guide` y valores vacíos. `auto_fill_from_plano.py` admite ES y convierte
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
  `comparacao-rodadas.pdf`).
- `make demo` genera los cinco PDFs de v2 desde el mock en `saida/demo/`;
  `make merge` combina exportaciones de formularios sin conexión en
  `respostas.json`; `make examples-v2` regenera los ejemplos de referencia.
- Páginas de referencia por dimensión en `referencia/dimensoes/` (EN, PT-BR,
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
  [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md)
  hacia `framework.v2.json` por `scripts/spec_to_framework_v2.py`, con las
  decisiones de diseño del kit en `framework/v2/config.json` y traducciones en
  `framework/v2/i18n.{pt-br,es}.json`. JSON Schema en
  `framework.v2.schema.json`; `scripts/validate_framework_v2.py` verifica
  conteos, IDs, citas, la partición de trazabilidad de v1, paridad de idioma y
  vigencia.
- Motor v2 (`scripts/engine_v2.py`), seleccionado por
  `metadata.framework_version` en `respostas.json`: respuestas por persona
  encuestada, medias agrupadas de preguntas, pesos de dimensión (0.5 a 2.0),
  estado de cobertura, baja confianza, riesgo de amplificación, brecha de
  percepción y banderas de alcance, cobertura de evidencia con preguntas L3/L4
  no verificadas, un backlog top 5 con anclas L3 y recomendaciones de
  estrategia que citan las referencias de la especificación.
- Activos de recopilación v2 desde `scripts/generate_v2_collection.py`:
  bancos de preguntas en PT-BR, EN y ES, el formulario sin conexión
  `formularios/assessment-v2.html` y la plantilla de exportación de Forms.
- Informes v2 (`relatorios/scripts/build_report_v2.py`): resumen de evaluación
  con mapa de calor de personas y banderas, más un roadmap por grupo de
  dimensiones (G1 a G3). `make pipeline` elige v1 o v2 automáticamente.
- Workbook auditable v2 (`scripts/fill_workbook_v2.py`): cada puntaje es una
  fórmula sobre las respuestas sin procesar, junto al valor del motor.
- Comparación de rondas (`scripts/compare_rounds.py`, `make compare`): v2 a
  v2, v1 a v1 y una línea base indicativa de v1 a v2 mediante el linaje de v1.
- Mock ilustrativo v2 (`respostas.v2.json.example`,
  `coleta/v2-mock-forms-export.xlsx`), `CHANGELOG.md` y un dev container.

- Versiones completas en portugués de Brasil y en español de todos los
  documentos, con el inglés como idioma principal: cada `X.md` tiene
  `X.pt-br.md` y `X.es.md` con los mismos títulos y una línea de selector
  con los tres idiomas. Nuevas copias en español de todas las guías de
  carpeta, `CHANGELOG.pt-br.md`, `CHANGELOG.es.md` y copias PT-BR y ES de
  la especificación v2 (`coleta/AI-Maturity-Form-Questions_v2.pt-br.md`,
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

### Corregido

- Las listas de referencia v2 se numeraban secuencialmente en lugar de por
  número de referencia, por lo que las citas y los números de lista no
  coincidían.
- Los paquetes EN y ES incluían sus guías raíz con enlaces `../` rotos.
- Los insights de Developer Survey enlazaban a capacidades de v1; ahora enlazan
  a preguntas de v2.
- `calcular_maturidade.py --lang pt-br` fallaba en una dimensión sin datos
  (clave de texto faltante).
- Seis archivos `SKILL.md` tenían front matter YAML no válido.
- `referencia/pontuacao-e-calculo.xlsx` almacenaba texto explicativo como
  fórmulas rotas.

### Archivado

- Bancos de preguntas, instrucciones y plantilla de v1 en `coleta/v1/`, los
  formularios HTML de v1 en `formularios/v1/`, las referencias de pilares de
  v1 y la calculadora de v1 en `referencia/v1/`. Los archivos v1 todavía se
  puntúan y se generan sin cambios.

## [1.x] - 2026-05 to 2026-09

- Motor determinista, importador de Forms y workbook con pruebas golden; PDFs
  de cliente sin datos de ejemplo; aviso de privacidad para Learning Survey;
  inglés como idioma predeterminado con copias PT-BR; limpieza de ramas (solo
  `main` y `develop`).
