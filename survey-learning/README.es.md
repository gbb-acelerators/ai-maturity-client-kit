# `survey-learning/`: Learning and Growth Survey (identificado, capacitación)

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Esta encuesta identificada genera el plan de capacitación usado por el liderazgo y por el wizard de la guía de implementación. Complementa la evaluación principal y el Developer Survey anónimo.

## Diferencia vs. las otras encuestas

| Aspecto | Evaluación principal | Developer Survey | Learning Survey |
| --- | --- | --- | --- |
| Audiencia | Liderazgo | Desarrolladores anónimos | Desarrolladores identificados |
| Foco | Madurez organizacional, D1 a D9 | Comportamiento y práctica, `DS-D2` a `DS-D8` | Demanda de aprendizaje y Champions |
| Salida | 5 PDFs v2 | Insights y JSON de madurez | `output/training-plan-<date>.md` |
| Impacto en el puntaje | Fuente de puntajes v2 | Solo contexto | Solo contexto y auto-fill del wizard |

## IDs del Learning Survey

Las etiquetas del banco de preguntas del Learning Survey usan `L#-Q#`. Cuando una pregunta se refiere a dimensiones del Developer Survey, usa `DS-D#`, por ejemplo `L2-Q1: DS-D2 Copilot Adoption ...`. Esto evita colisiones con las dimensiones D1 a D9 de la evaluación v2.

## Archivos en esta carpeta

| Archivo | Qué es |
| --- | --- |
| [FORMS-INSTRUCTIONS-LEARNING.md](FORMS-INSTRUCTIONS-LEARNING.es.md) | Cómo crear el Microsoft Forms identificado. |
| [question-bank-learning.md](question-bank-learning.md) | Banco de preguntas en inglés. |
| [question-bank-learning.pt-br.md](question-bank-learning.pt-br.md) | Banco de preguntas en portugués (Brasil). |
| [question-bank-learning.es.md](question-bank-learning.es.md) | Banco de preguntas en español. Los scripts escriben EN, PT-BR o ES (`--lang es`). |
| [template-export-forms-learning.xlsx](template-export-forms-learning.xlsx) | Plantilla Excel. |
| [mock-responses-learning.json](mock-responses-learning.json) | JSON estructurado de ejemplo. |
| [scripts/](scripts/) | Generador del plan de capacitación. |

## Flujo de uso

```text
1. Crea el Forms con FORMS-INSTRUCTIONS-LEARNING.md.
2. Compártelo con los desarrolladores.
3. Exporta respuestas a Excel.
4. Ejecuta /import-survey-learning.
5. Ejecuta /training-plan.
6. Ejecuta /implementation-wizard Mode D, o ejecuta wizard/scripts/auto_fill_from_plan.py.
7. Ejecuta make pipeline para actualizar v2_implementation_guide.pdf.
```

## Qué contiene el plan de capacitación

`output/training-plan-<date>.md` se escribe en inglés de forma predeterminada, o en PT-BR o ES con `--lang pt-br` o `--lang es`. Incluye temas solicitados, cohorts sugeridos por `DS-D#`, Champions, pares de mentoría, un calendario de 90 días, barreras, wishlist y acciones priorizadas.

## Conexión con el wizard

Mode D llena 7 de los 11 campos de la guía de implementación a partir del plan del Learning Survey: steering committee desde Champions activos, plan de comunicación desde el calendario, plan de capacitación desde cohorts, notas ADKAR y quick wins. Los campos restantes se marcan como elementos por completar.
