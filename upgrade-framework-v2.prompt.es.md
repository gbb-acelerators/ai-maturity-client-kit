---
description: Actualiza el AI Maturity Client Kit del framework v1 (3 pilares, 28 capacidades, 158 preguntas) a v2 (9 dimensiones AI-SDLC, 61 preguntas) en datos, recopilación, importación, puntuación, informes, skills, docs y traducciones.
agent: agent
---

# Actualiza el AI Maturity Client Kit al framework v2

🌐 [English](upgrade-framework-v2.prompt.md) · [Português (Brasil)](upgrade-framework-v2.prompt.pt-br.md) · Español

> **Estado (2026-09-28): ejecutado** en la rama `feature/framework-v2`. La especificación es v2.0.1 ([collection/AI-Maturity-Form-Questions_v2.es.md](collection/AI-Maturity-Form-Questions_v2.es.md)); las decisiones D-1 a D-8 y el resto de los cambios se listan en [CHANGELOG.es.md](CHANGELOG.es.md). Conserva este archivo como el registro del plan; ejecútalo de nuevo solo para una nueva versión mayor del framework.

## Rol

Eres un ingeniero sénior y redactor técnico que actualiza el repositorio **AI Maturity Client Kit** al framework v2. Trabaja con cuidado, por fases, con validación después de cada fase. Pregunta antes de cualquier acción destructiva o ambigua.

## Entradas

| Entrada | Ubicación |
| --- | --- |
| Especificación v2 (fuente de verdad) | `collection/AI-Maturity-Form-Questions_v2.md` (v2.0.1) |
| Repositorio del framework | este repositorio (rama `develop`) |
| Remoto | `gbb-acelerators/ai-maturity-client-kit` (transferido desde `paulasilvatech`) |

Lee toda la especificación v2 antes de cambiar cualquier cosa. Trata estas partes como fijas, a menos que señales un problema y yo apruebe un cambio: IDs y redacción de las preguntas, la escala de respuestas y sus prefijos `L0`-`L4`/`NA`, el patrón de etiqueta `Evidence (<ID>)`, los anclajes de calibración, las reglas de puntuación de la sección 8, la trazabilidad v1→v2 de la sección 9 y las referencias.

El árbol de trabajo ya tiene cambios no confirmados no relacionados (`.DS_Store` files, `docs/styles.css`, un `scripts/__pycache__/*.pyc` eliminado). No los prepares para commit, confirmes, reviertas ni edites.

## Qué cambia v2 (resumen)

- 9 dimensiones puntuadas (D1-D9) con 61 preguntas reemplazan 3 pilares / 28 capacidades / 158 preguntas.
- Nueva sección de perfil de la persona encuestada sin puntuación: `R-Q1`-`R-Q5` (`R-Q3` es de opción múltiple).
- Escala redefinida: L0 Not started, L1 Exploring (≤25%), L2 Adopting (26-50%), L3 Scaling (51-90%), L4 AI-native (>90%). Los mismos prefijos que v1.
- Anclajes L3/L4 por pregunta, ejemplos de evidencia, citas de base y linaje v1.
- Puntuación: puntaje de dimensión = media de puntajes de preguntas (se excluye NA); general = media de dimensiones (pesos iguales por defecto); bandas de nivel de ancho 0.8; indicador de baja confianza (>30% NA); indicador de riesgo de amplificación (D5, D6 o D8 al menos una banda por debajo del general); indicador de brecha de percepción (ejecutivos vs ingenieros hands-on según `R-Q1`); cobertura de evidencia.
- Trazabilidad: en v2.0.1, 99 preguntas v1 se consolidan en v2 y 59 se retiran de la evaluación central (partición de las 158, sin solapamientos). El borrador 2.0.0 tenía 97 y 61.
- 58 referencias, incluidas 14 prepublicaciones de arXiv de 2026 y la publicación de Management Science de 2026 de Cui et al.

## Mapa del repositorio (verificado 2026-09-25)

| Área | Archivos | Cambio esperado |
| --- | --- | --- |
| Datos del framework | `framework.json` (v1.0.0: `level_names`, `strategies`, `technologies_per_strategy`, `pillars` → `capabilities` → `questions` con `id`, `weight`, `pe`, `audience`, `kpi`) | Agregar modelo de datos v2 (ver Decisión D-1) |
| Datos de respuestas | `responses.json`, `responses.json.example` (`metadata`, `target_overrides` con clave por capacidad, `responses` con clave por ID de pregunta con `level`, `evidence`, `text_*`) | Ejemplo v2 con clave por `D#-Q#`, respuestas de perfil, `framework_version` |
| Entradas de implementación | `implementation-guide-inputs.json`, `wizard/implementation-guide-inputs.template.json`, `wizard/implementation-guide-wizard.html`, `wizard/scripts/auto_fill_from_plan.py` | Mapear a dimensiones |
| Recopilación (PT/EN/ES) | `collection/question-bank{,.pt-br,.es}.md`, `collection/FORMS-INSTRUCTIONS.md`, `collection/README.md`, `collection/template-export-forms.xlsx` | Regenerar desde datos v2; 10 secciones, 127 elementos |
| Formularios HTML | `forms/P1-*.html`, `forms/P2-*.html`, `forms/P3-*.html`, `forms/README.md` | Reemplazar con formularios v2 (perfil + D1-D9) |
| Referencia de puntuación | `reference/scoring-and-calculation.md`, `reference/scoring-and-calculation.xlsx`, `reference/scoring-calculator.html` | Reglas e indicadores v2 (motor actual: capacidades ponderadas, general = SUMPRODUCT sobre todas las capacidades, pesos 1.0 en [0.5, 2.0], `priority_score = peso_capability × gap_size`) |
| Docs de referencia de pilares | `reference/P1-*.md`, `reference/P2-*.md`, `reference/P3-*.md`, `reference/README.md` | Docs de referencia por dimensión con base de investigación |
| Salidas de ejemplo | `reference/sample-output/**` (scores, gaps, recommendations, payload, PDFs, XLSX, carpetas EN/ES) | Regenerar desde un mock v2; nunca editar a mano |
| Informes | `reports/scripts/{build_payload_and_render,render_reports,render_smoke,branding}.py`, `reports/templates/*.j2`, `reports/templates/_print.css`, `reports/i18n/{pt-br,en,es}.json`, `reports/sample_payload.json` | Dimensiones, indicadores, vista por persona, cobertura de evidencia, referencias |
| Personalización de Copilot | `.github/copilot-instructions.md`, `.github/agents/ai-maturity-assistant.agent.md`, `.github/prompts/full-pipeline.prompt.md`, `.github/skills/*/SKILL.md` (12 skills: `import-responses`, `calculate-scores`, `gap-analysis`, `recommend-strategies`, `generate-report`, `ai-maturity-reports`, `fill-workbook`, `implementation-wizard`, `import-survey-devs`, `insights-developer-survey`, `import-survey-learning`, `training-plan`) | Actualizar cada referencia a pilar/capacidad y patrón de ID |
| Encuestas complementarias | `survey-devs/**` (incl. `MATURITY-RUBRIC.md`, `scripts/rubric.py`), `survey-learning/**` | Solo referencias cruzadas; evitar preguntas duplicadas (ver D-6) |
| Docs y sitio | `README.md`, `STEP-BY-STEP.md`, `docs/{content.json,index.html,en/index.html,es/index.html,app.js,README.md}` | Estructura, conteos y flujo v2 |
| Herramientas | `Makefile` (`smoke`, `smoke-cross`, `validate-docs`, `build-kits`, `pipeline`), `scripts/{smoke_test,check_language_coverage,build_language_kits}.py`, `.github/workflows/{pages,release-zips}.yml` | Extender las comprobaciones para v2 |

## Requisitos adicionales (de la auditoría 2026-09)

Estos faltaban en la primera versión de este plan y forman parte de la actualización:

- **Sin contenido de muestra en informes de clientes (C1).** Cualquier sección del informe sin datos del cliente se omite o se marca como "por completar", nunca se completa desde payloads de muestra.
- **Puntuación determinista (C2).** La importación, los puntajes, las brechas y las estrategias se ejecutan en scripts Python con pruebas; las skills llaman a los scripts en vez de calcular en el chat.
- **IDs de pregunta en títulos de Forms (C3).** Cada título de pregunta de Forms empieza con su ID (`D4-Q3: ...`, `R-Q1: ...`).
- **Sin colisiones de ID (C4).** Las dimensiones de Developer Survey se llaman `DS-D2` a `DS-D8`; `D1` a `D9` están reservados para la evaluación.
- **Una regla de bandas por versión (C5).** v2 usa bandas semiabiertas de ancho 0.8 sin huecos; la encuesta complementaria mantiene las bandas v1 y se compara por puntaje.
- **Privacidad (C8).** Forms lleva un aviso de consentimiento y retención; las respuestas de perfil son datos personales; las salidas quedan fuera de git (`responses.json` y `implementation-guide-inputs.json` no tienen seguimiento).
- **Muestra mínima por persona.** Los resultados por persona y brecha de percepción necesitan al menos 3 personas encuestadas por grupo; los grupos más pequeños se marcan como muestra baja.

## Reglas no negociables

1. **Integridad factual.** No inventes métricas, benchmarks, porcentajes ni hallazgos de investigación. Toda afirmación de datos en docs, skills o informes debe venir de las referencias v2 (con el mismo enlace). Si necesitas una fuente nueva, verifícala primero en la web, agrégala a las referencias y avísame.
2. **Compatibilidad hacia atrás.** Los archivos de respuestas v1 y el ejemplo v1 existente aún deben importarse, puntuarse y renderizarse. Detecta la versión desde `framework_version` en los metadatos de `responses.json` (por defecto v1 cuando no exista). Archiva el contenido v1; no lo elimines.
3. **Escala e IDs.** Mantén exactamente los prefijos de opción `L0`-`L4`/`NA` y el patrón de etiqueta `Evidence (<ID>)`. Los IDs son `D#-Q#` (puntuadas) y `R-Q#` (perfil).
4. **Fuente única de verdad.** Genera listas de preguntas, formularios, traducciones y plantillas desde el archivo de datos v2 con scripts. No mantengas a mano tres copias de idioma.
5. **Paridad trilingüe.** PT-BR, EN y ES deben tener las mismas preguntas, anclajes y opciones. Mantén la redacción en inglés de la especificación como canónica; traduce PT-BR y ES fielmente; `scripts/check_language_coverage.py` debe pasar.
6. **Branding.** Sigue `reference/branding/` (IDENTITY, VOICE, tokens). En material orientado a Microsoft usa el logotipo oficial de cuatro cuadrados de Microsoft y el título "Global Developer Solutions Advisor"; nunca el logotipo personal `</>`.
7. **Seguridad de git.** Trabaja en una rama nueva `feature/framework-v2` creada desde `develop`. Haz commit por fase con mensajes claros. No hagas push, force-push, reescritura de historial ni elimines ramas. Pregunta antes de eliminar o mover cualquier archivo con seguimiento.
8. **Salidas generadas.** Regenera PDFs, XLSX y ejemplos JSON con los scripts del repo; nunca edites artefactos generados a mano.
9. **Estilo Python.** PEP 8, type hints donde el archivo ya los use, líneas ≤ 79 caracteres, sin nuevas dependencias sin preguntar.

## Fase 0: Descubrimiento y plan (detente para aprobación)

1. Lee la especificación v2, `framework.json`, `responses.json.example`, `reference/scoring-and-calculation.md`, cada `SKILL.md`, el archivo del agent, el prompt de pipeline, `Makefile` y los scripts de informes.
2. Crea un inventario de impacto: grep para `P[0-9]-C[0-9]+-Q[0-9]+`, `P1`/`P2`/`P3`, `pillar`/`pilar`, `capabilit`, `158`, `28 capabilities`, `3 pillars`, nombres de nivel (`Inicial`, `Em Desenvolvimento`, `Definido`, `Gerenciado`, `Otimizando`). Lista cada archivo con el cambio que necesita.
3. Presenta el plan y mis decisiones abiertas abajo, cada una con tu recomendación y trade-offs. **Espera mis respuestas antes de la Fase 1.**

Decisiones abiertas:

| ID | Decisión | Valor predeterminado recomendado |
| --- | --- | --- |
| D-1 | Modelo de datos: extender `framework.json` o agregar `framework.v2.json` | Agregar `framework.v2.json` (versión 2.0.0) y un cargador que elija v1/v2 por `framework_version` |
| D-2 | Motor de puntuación | Tratar cada dimensión como la unidad de puntuación (peso 1.0, rango permitido [0.5, 2.0]); pesos de preguntas 1.0; general = media ponderada de dimensiones, que equivale a los pesos iguales de la especificación por defecto; mantener `priority_score = weight × gap` por dimensión |
| D-3 | Mapeo de `strategies` y `technologies_per_strategy` | Remapear cada una de las 7 estrategias a dimensiones; muéstrame la tabla de mapeo antes de escribirla |
| D-4 | Valores `audience` de preguntas | Derivar de personas `R-Q1` y del vocabulario de audiencia existente; mostrar el mapeo |
| D-5 | Campo `pe` | Explicar su significado actual desde el código; proponer valores v2 o quitarlo |
| D-6 | Solapamiento con `survey-devs` y `survey-learning` | Referencias cruzadas (por ejemplo D2, D5-Q6, D9-Q4) en vez de duplicar preguntas |
| D-7 | Diseño de archivo v1 | Mover artefactos v1 bajo rutas `v1/` (por ejemplo `collection/v1/`, `forms/v1/`) y mantener los enlaces funcionando |
| D-8 | Nombres de niveles en PT-BR/ES | Proponer traducciones para Not started / Exploring / Adopting / Scaling / AI-native |

## Fase 1: Modelo de datos

- Crear `framework.v2.json` con: `version`, `level_names` (EN/PT-BR/ES), `level_bands`, `coverage_bands`, `dimensions` (id, nombres en 3 idiomas, peso, estrategias, preguntas), `profile_questions` (opciones en 3 idiomas, bandera `multi` para `R-Q3`), `references` (1-58 con URL), `traceability` (ID v1 → ID v2 o `retired` con razón).
- Cada pregunta: `id`, `weight`, `audience`, `kpi`, `text` (en/pt-br/es), `anchors.l3`, `anchors.l4` (más `l1_l2` para D4-Q1), `evidence_examples`, `basis` (números de referencia), `v1_lineage`.
- Agregar un JSON Schema (`framework.v2.schema.json`) y un script validador.
- Aceptación: 61 preguntas puntuadas (D1 7, D2 6, D3 6, D4 8, D5 7, D6 7, D7 6, D8 7, D9 7); 5 preguntas de perfil; IDs únicos; cada número `basis` existe en `references`; la trazabilidad cubre los 158 IDs v1 exactamente una vez (99 consolidados, 59 retirados en v2.0.1).

## Fase 2: Recopilación

- Escribir un generador que produzca `collection/question-bank{,.pt-br,.es}.md` desde `framework.v2.json`, siguiendo el diseño de la especificación (Sección 0 perfil, luego D1-D9, anclajes en el subtítulo de la pregunta, campo de evidencia por pregunta).
- Actualizar instrucciones de Forms en PT/EN/ES: 10 secciones, 127 elementos, las seis opciones en orden, guía para personas encuestadas (≥3 personas encuestadas por persona).
- Actualizar `collection/template-export-forms.xlsx` a la forma de exportación v2 (columnas de perfil, columnas de respuesta `D#-Q#`, columnas `Evidence (D#-Q#)`).
- Reemplazar `forms/*.html` con formularios v2; conservar v1 bajo la ruta de archivo de D-7.
- Crear un `responses.json.example` v2 y un mock realista multipersona para pruebas. Etiquetar todos los datos mock como ilustrativos.

## Fase 3: Importación y puntuación

- `import-responses`: detectar v1 vs v2 por IDs de columnas; analizar `D#-Q#` y `R-Q#`; soportar selección múltiple `R-Q3`; mapear prefijos de opción a 0-4/null; agregar por persona encuestada y por persona; escribir `framework_version` en `responses.json`.
- `calculate-scores` más `reference/scoring-and-calculation.{md,xlsx}` y `scoring-calculator.html`: implementar la sección 8 de la especificación (puntajes de dimensión, general, bandas, indicadores de baja confianza, riesgo de amplificación y brecha de percepción, cobertura de evidencia, puntajes por persona). Mantener la ruta v1 funcionando.
- `gap-analysis` y `recommend-strategies`: trabajar por dimensión; las recomendaciones comienzan por las preguntas con menor puntaje y citan sus anclajes L3; las recomendaciones deben citar referencias de la especificación, no benchmarks inventados.

## Fase 4: Informes

- Actualizar `build_payload_and_render.py`, plantillas y archivos i18n para dimensiones, indicadores, heatmap de persona (dimensiones × personas), cobertura de evidencia y un apéndice de referencias.
- Reemplazar la plantilla de roadmap por pilar con una plantilla por dimensión (o agrupada); proponer la agrupación antes de construirla.
- Regenerar `reports/sample_payload.json` y todo `reference/sample-output/**` (PT/EN/ES) desde el mock v2. Conservar el ejemplo v1 bajo la ruta de archivo.

## Fase 5: Personalización de Copilot y docs

- Actualizar `.github/copilot-instructions.md`, el agent, `full-pipeline.prompt.md` y las 12 skills. Sigue el patrón existente: agent ligero con el flujo de trabajo, conocimiento de dominio en las skills.
- Actualizar `implementation-wizard` y las entradas del wizard; vincular `training-plan` con D2; hacer que `insights-developer-survey` haga referencia cruzada a D2/D5/D9 en vez de duplicar.
- Reemplazar `reference/P1..P3-*.md` con docs de referencia por dimensión que incluyan el texto de "por qué importa", anclajes y base de investigación de la especificación.
- Actualizar `README.md`, `STEP-BY-STEP.md` y el sitio de docs (`docs/content.json` y los tres `index.html`) con conteos y flujo v2. Agregar una entrada de changelog (pregunta dónde si no hay CHANGELOG).

## Fase 6: Validación (todo debe pasar)

1. `make smoke`, `make smoke-cross`, `make validate-docs`, `make build-kits`.
2. `python3 scripts/check_language_coverage.py` con cero brechas entre PT-BR/EN/ES.
3. El validador de schema y la comprobación de trazabilidad (158 = 99 + 59, sin solapamientos, sin huecos).
4. `make pipeline` de extremo a extremo dos veces: con el mock v2 y con el ejemplo v1. Ambos deben producir puntajes e informes.
5. Abrir los PDFs regenerados y revisar saltos de página, fuentes, logotipo, indicadores y heatmap de persona.
6. Grep para redacción v1 obsoleta (`158`, `28 capabilities`, `3 pillars`, `P1-C`, nombres de nivel antiguos) fuera del archivo v1 y el changelog; listar cualquier cosa que quede y por qué.
7. Markdown lint y comprobación de enlaces internos en todos los docs cambiados.

## Informe final

Responde con:

- Las decisiones tomadas (D-1 a D-8) y lo que implementaste para cada una.
- Una tabla de archivos cambiados, agregados y archivados agrupados por fase.
- La salida de cada comando de validación.
- Elementos abiertos, riesgos y cualquier cosa que no cambiaste, con la razón.
