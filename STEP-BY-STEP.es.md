# Paso a paso: AI Maturity Assessment

🌐 [English](STEP-BY-STEP.md) · [Português (Brasil)](STEP-BY-STEP.pt-br.md) · Español

Esta guía ejecuta la evaluación framework v2 desde la recolección hasta los reportes. v1 sigue disponible para entradas archivadas.

## Quickstart

Ruta más rápida para obtener un primer PDF:

```bash
make install-deps
make demo
open output/demo/*.pdf
```

Flujo real con cliente:

```bash
# Recolecta respuestas con Microsoft Forms, o con exports del HTML offline.
make merge DIR=exports/
# Si usas Microsoft Forms en vez de exports offline:
make import XLSX=forms-responses.xlsx
make pipeline
# Cross-checks opcionales de evidencia.
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
# Llena implementation-guide-inputs.json con el wizard, luego renderiza de nuevo.
make pipeline
```

## 1. Elige el flujo

Usa v2 para nuevas evaluaciones. Usa v1 solo para comparación histórica o archivos `responses.json` sin `metadata.framework_version`.

- Especificación v2: [collection/AI-Maturity-Form-Questions_v2.es.md](collection/AI-Maturity-Form-Questions_v2.es.md), traducción de la fuente en inglés [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md).
- Formulario v2: [forms/assessment-v2.html](forms/assessment-v2.es.html).
- Instrucciones Forms v2: [collection/FORMS-INSTRUCTIONS.md](collection/FORMS-INSTRUCTIONS.es.md).
- Páginas de dimensión v2: [reference/dimensions/](reference/dimensions/README.es.md).
- Archivo v1: [collection/v1/](collection/v1/), [forms/v1/](forms/v1/), [reference/v1/](reference/v1/).

## 2. Prepara entradas

```bash
make init
```

Esto copia `responses.v2.json.example` a `responses.json` si el archivo todavía no existe.

También puedes importar un export de Microsoft Forms:

```bash
make import XLSX=forms-responses.xlsx
```

También puedes usar el formulario offline. Cada persona abre [forms/assessment-v2.html](forms/assessment-v2.es.html), exporta un `responses.json` y lo envía al facilitador. Coloca los exports en una carpeta y ejecuta:

```bash
make merge DIR=exports/
```

El merge asigna IDs únicos por persona, rechaza archivos v1, rechaza organizaciones mixtas excepto con `--org` o `--allow-mixed-org`, y hace backup de un `responses.json` existente antes de escribir el archivo unido.

## 3. Entiende la estructura v2

- 5 preguntas de perfil: `R-Q1` a `R-Q5`.
- 61 preguntas puntuadas: `D#-Q#`.
- 9 dimensiones: D1 Estrategia, Política y Gobernanza de IA; D2 Habilitación, Habilidades y Cultura; D3 Planificar, Especificar y Diseñar; D4 Código e ingeniería de contexto; D5 Revisión, calidad y pruebas; D6 Seguridad y cadena de suministro de IA; D7 Entregar y Operar; D8 Fundamentos de Ingeniería; D9 Medición, Valor y AI FinOps.
- Niveles: L0 No iniciado, L1 Explorando, L2 Adoptando, L3 Escalando, L4 Nativo en IA, más `NA`.
- Las páginas de referencia D1 a D9 incluyen notas de alcance, anclas, ejemplos de evidencia, base, contexto del Developer Survey y referencias citadas.

## 4. Ejecuta scoring determinístico

```bash
make scores
```

o:

```bash
python3 scripts/assessment_engine.py all
```

No calcules scores a mano. El engine escribe:

- `output/scores.json`
- `output/gaps.json`
- `output/recommendations.json`

Cobertura es OK con 37 o más preguntas respondidas, WARNING de 25 a 36 y BLOCKED por debajo de 25. Divergencia entre personas encuestadas se marca cuando una dimensión tiene al menos 3 scores de personas encuestadas y desviación estándar de 1,0 o más.

## 5. Crea el workbook

```bash
make workbook
```

Para v2, el dispatcher escribe `output/scoring-v2-<date>.xlsx`. Incluye fórmulas y una columna de cross-check del engine. Las fórmulas redondean comparaciones a 9 decimales para que los límites de prioridad ignoren ruido de punto flotante.

## 6. Renderiza reportes

```bash
make pipeline
```

o, después de que ya existan los scores:

```bash
python3 reports/scripts/build_payload_and_render.py
```

Archivos v2:

- `output/v2_assessment_summary.pdf`
- `output/v2_roadmap_g1.pdf`, D1, D2, D9.
- `output/v2_roadmap_g2.pdf`, D3, D4, D5.
- `output/v2_roadmap_g3.pdf`, D6, D7, D8.
- `output/v2_implementation_guide.pdf`.
- `output/payload_v2.json`.

Las entradas v1 todavía producen el conjunto archivado de 5 PDFs.

## 7. Agrega cross-checks de evidencia

Ejecuta cualquiera de ellos antes del `make pipeline` final:

```bash
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
```

La salida del scan de repositorios es `output/repo-scan.json`. La salida de métricas de Copilot es `output/telemetry.json`. La salida de métricas DORA es `output/dora-metrics.json`: una fila por servicio y período (`baseline`, `current`), y `SERVICES` es el número de servicios en el alcance. El reporte de resumen muestra una sección Evidence cross-checks y marca respuestas por encima de lo que la evidencia soporta. La guía de implementación lista esas flags como riesgos. Sin los archivos, el PDF explica cómo producirlos.

## 8. Llena el wizard de la guía de implementación

Abre el wizard trilingüe generado:

```bash
open wizard/implementation-guide-wizard.html
```

Guarda 11 campos en `implementation-guide-inputs.json`: `executive_steering_committee`, `tpo`, `dimension_owners`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`, `risk_register`, `quick_wins_w1_4`, `quick_wins_w5_8` y `quick_wins_w9_12`. Los campos vacíos aparecen como `to fill with the client`, no como contenido de ejemplo.

Mode D puede llenar 7 campos desde el plan del Learning Survey:

```bash
python3 wizard/scripts/auto_fill_from_plan.py --lang es
```

Después del wizard, ejecuta `make pipeline` otra vez.

## 9. Compara rondas

```bash
make compare BEFORE=old-responses.json AFTER=responses.json
```

El script de comparación soporta deltas comparables v2 a v2, baseline indicativo v1 a v2 vía `v1_lineage`, y v1 a v1. Escribe `output/round-comparison.pdf` cuando la renderización de PDF está disponible.

## 10. Usa surveys complementarios

Developer Survey y Learning and Growth Survey aportan contexto. No cambian scores v2.

- Las dimensiones del Developer Survey son `DS-D2` a `DS-D8` en las salidas.
- El PDF de resumen v2 muestra contexto del Developer Survey cuando existe `output/developer-survey-maturity-*.json`.
- La salida del Learning Survey puede alimentar Mode D del wizard de implementación.
- Los scripts de survey escriben EN, PT-BR o ES (`--lang en|pt-br|es`) y puntúan igual los formularios creados en cualquiera de los tres idiomas.

## 11. Valida las fuentes del repositorio

```bash
make validate-v2
make validate-docs
make test
```

Consulta [CHANGELOG.md](CHANGELOG.es.md) para el historial de versiones.
