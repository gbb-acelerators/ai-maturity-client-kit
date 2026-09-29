# `survey-learning/scripts/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Learning Survey](../README.es.md)

Scripts que construyen el plan de capacitación desde el Learning and Growth Survey identificado.

## Contenido

| Archivo | Propósito |
| --- | --- |
| [generate_training_plan.py](generate_training_plan.py) | Lee `survey-learning/responses-learning.json` y genera `output/training-plan-<date>.md`: temas solicitados, cohorts por `DS-D#`, Champions, pares de mentoría, calendario de 90 días, barreras, wishlist y acciones priorizadas. Inglés por defecto; pasa `--lang pt-br` o `--lang es`. |

## Uso

```bash
python3 survey-learning/scripts/generate_training_plan.py
python3 survey-learning/scripts/generate_training_plan.py --lang pt-br
python3 survey-learning/scripts/generate_training_plan.py --lang es
```

Después de generar el plan, ejecuta `python3 wizard/scripts/auto_fill_from_plan.py --lang en` o usa `/implementation-wizard` Modo D para poblar 7 de los 11 campos de la guía de implementación.
