# `survey-learning/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Learning Survey](../README.md)

Scripts that build the capacitation plan from the identified Learning and Growth Survey.

## Contents

| File | Purpose |
| --- | --- |
| [gerar_plano_capacitacao.py](gerar_plano_capacitacao.py) | Reads `survey-learning/respostas-learning.json` and generates `saida/plano-capacitacao-<date>.md`: requested topics, cohorts per `DS-D#`, Champions, mentor pairs, 90-day calendar, barriers, wishlist, and prioritized actions. English by default; pass `--lang pt-br` or `--lang es`. |

## Usage

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang es
```

After generating the plan, run `python3 wizard/scripts/auto_fill_from_plano.py --lang en` or use `/wizard-implementacao` Mode D to populate 7 of the 11 implementation guide fields.
