# `survey-devs/`: Developer Survey (anónimo, conductual, individual)

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Esta carpeta contiene una encuesta separada de la evaluación principal. Mide cómo los desarrolladores usan GitHub Copilot, agentes, instruction files, modos de Copilot Chat, prácticas de desarrollo con IA, gobernanza y seguridad en el día a día. Es anónima.

## Diferencia vs. la evaluación principal y survey-learning

| Aspecto | Evaluación principal | Developer Survey | survey-learning |
| --- | --- | --- | --- |
| Audiencia | Liderazgo, arquitectos y Tech Leads | Desarrolladores individuales | Desarrolladores individuales |
| ¿Anónima? | No | Sí | No, identificada por nombre y email |
| Foco | Madurez organizacional, v2 D1 a D9 | Adopción y práctica individual real, `DS-D2` a `DS-D8` | Lo que las personas quieren aprender |
| Salida | 5 PDFs v2, workbook, JSONs | Informe de insights y JSON de madurez calculada | Plan de capacitación y Champions |
| Impacto en el puntaje | Fuente de puntajes v2 | Solo contexto | Solo contexto y auto-fill del wizard |

Los resultados de la encuesta nunca cambian los puntajes de la evaluación v2.

## Dimensiones de la encuesta

Las dimensiones del Developer Survey ahora se llaman `DS-D2` a `DS-D8` en las claves JSON, insights, cohortes del plan de capacitación y referencias cruzadas. Los Forms creados con el texto antiguo de estilo `D2` todavía se interpretan.

| ID | Foco |
| --- | --- |
| `DS-D2` | Adopción y modos de Copilot. |
| `DS-D3` | Herramientas del ecosistema Microsoft y GitHub. |
| `DS-D4` | Prácticas de desarrollo con IA. |
| `DS-D5` | Conceptos y estructura de agentes. |
| `DS-D6` | Markdown, memory e instructions. |
| `DS-D7` | Usabilidad y best practices. |
| `DS-D8` | Seguridad y gobernanza. |

## Crosswalk al framework v2

`framework.v2.json` mapea cada `DS-D#` a las preguntas v2 que ayuda a validar:

| Dimensión de la encuesta | Preguntas v2 |
| --- | --- |
| `DS-D2` | D4-Q1, D4-Q2, D9-Q1 |
| `DS-D3` | D4-Q3, D4-Q6, D3-Q2, D6-Q1 |
| `DS-D4` | D3-Q2, D5-Q5, D2-Q6 |
| `DS-D5` | D2-Q4, D4-Q5 |
| `DS-D6` | D4-Q4, D4-Q5 |
| `DS-D7` | D2-Q2, D9-Q4 |
| `DS-D8` | D1-Q2, D6-Q1, D6-Q4, D6-Q5, D6-Q7 |

La sección 12 del informe de insights enlaza a preguntas v2, no a capacidades v1. El PDF de resumen v2 muestra contexto del Developer Survey cuando existe `output/developer-survey-maturity-*.json`.

## Archivos en esta carpeta

| Archivo | Qué es |
| --- | --- |
| [FORMS-INSTRUCTIONS-DEVS.es.md](FORMS-INSTRUCTIONS-DEVS.es.md) | Guía paso a paso para construir el Microsoft Forms. |
| [question-bank-devs.md](question-bank-devs.md) | Banco de preguntas en inglés. |
| [question-bank-devs.pt-br.md](question-bank-devs.pt-br.md) | Banco de preguntas en portugués (Brasil); sus opciones son los valores canónicos de [options.json](options.json). |
| [question-bank-devs.es.md](question-bank-devs.es.md) | Banco de preguntas en español. |
| [template-export-forms-devs.xlsx](template-export-forms-devs.xlsx) | Plantilla Excel en el formato de exportación de Forms. |
| [mock-responses-devs.json](mock-responses-devs.json) | JSON estructurado de ejemplo para smoke tests. |
| [MATURITY-RUBRIC.es.md](MATURITY-RUBRIC.es.md) | Rúbrica determinística. Mantiene las bandas v1, así que compara por puntaje, no por nombre de nivel. |
| [scripts/](scripts/) | Scripts de importación, puntuación e insights. |

## Flujo de uso

```text
1. Construye el Forms con FORMS-INSTRUCTIONS-DEVS.es.md.
2. Recopila respuestas de forma anónima.
3. Exporta a Excel.
4. Ejecuta /import-survey-devs.
5. Ejecuta /insights-developer-survey.
6. Vuelve a ejecutar make pipeline si quieres que el PDF de resumen v2 incluya contexto del Developer Survey.
```

Los scripts escriben EN por defecto, PT-BR con `--lang pt-br` o español con `--lang es`. Los bancos EN y ES traducen las opciones de respuesta; [options.json](options.json) mapea las opciones de los tres idiomas (y de formularios antiguos en portugués cuyas opciones tenían guiones) a la misma opción canónica antes de puntuar, así que el resultado no depende del idioma del formulario.
