# `survey-learning/scripts/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Learning Survey](../README.es.md)

Scripts que construyen el plan de capacitación desde el Learning and Growth Survey identificado.

## Contenido

| Archivo | Propósito |
| --- | --- |
| [gerar_plano_capacitacao.py](gerar_plano_capacitacao.py) | Lee `survey-learning/respostas-learning.json` y genera `saida/plano-capacitacao-<date>.md`: temas solicitados, cohorts por `DS-D#`, Champions, pares de mentoría, calendario de 90 días, barreras, wishlist y acciones priorizadas. Inglés por defecto; pasa `--lang pt-br` o `--lang es`. |

## Uso

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang es
```

Después de generar el plan, ejecuta `python3 wizard/scripts/auto_fill_from_plano.py --lang en` o usa `/wizard-implementacao` Modo D para poblar 7 de los 11 campos de la guía de implementación.
