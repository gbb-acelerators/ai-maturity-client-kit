# `reference/`: material de referencia

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Framework v2 es el modelo de referencia predeterminado. El material v1 sigue archivado.

| Ruta | Propósito |
| --- | --- |
| [framework-v2.es.md](framework-v2.es.md) | Guía del framework v2 generada con reglas de puntuación, notas de alcance, crosswalk y referencias. |
| [dimensions/](dimensions/) | Páginas generadas por dimensión para D1 a D9 en EN, PT-BR y ES. |
| [scoring-calculator.es.html](scoring-calculator.es.html) | Calculadora what-if v2 trilingüe generada, que se abre en español. En el repositorio, `scoring-calculator.html` sigue el idioma del navegador y `scoring-calculator.pt-br.html` se abre en portugués; cada paquete de idioma entrega su copia como `scoring-calculator.html`. Carga `output/scores.json`, ajusta pesos y objetivos, e inspecciona nivel, brecha, prioridad, horizonte, riesgo de amplificación y estrategias. |
| [v1/scoring-calculator.html](v1/scoring-calculator.es.html) | Calculadora v1 archivada. |
| [sample-output/](sample-output/) | Salidas v2 ilustrativas, incluidos 5 PDFs, PDF de comparación, workbook, escaneo de repo, telemetría, métricas DORA, encuestas y entradas del wizard. |
| [v1/](v1/) | Referencias y ejemplos de pilares v1 archivados. |
| [branding/](branding/) | Guía de marca y voz. |

La fuente de verdad de la puntuación v2 es el motor determinístico y [../collection/AI-Maturity-Form-Questions_v2.es.md](../collection/AI-Maturity-Form-Questions_v2.es.md). No uses páginas de pilares v1 archivadas para evaluaciones nuevas.

Usa `make examples-v2` para regenerar los ejemplos ilustrativos. Usa `make validate-docs` para revisar helpers generados y docs de paquetes.
