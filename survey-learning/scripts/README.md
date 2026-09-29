# `survey-learning/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Learning Survey](../README.md)

Scripts that build the capacitation plan from the identified Learning and Growth Survey.

## Contents

| File | Purpose |
| --- | --- |
| [generate_training_plan.py](generate_training_plan.py) | Reads `survey-learning/responses-learning.json` and generates `output/training-plan-<date>.md`: requested topics, cohorts per `DS-D#`, Champions, mentor pairs, 90-day calendar, barriers, wishlist, and prioritized actions. English by default; pass `--lang pt-br` or `--lang es`. |

## Usage

```bash
python3 survey-learning/scripts/generate_training_plan.py
python3 survey-learning/scripts/generate_training_plan.py --lang pt-br
python3 survey-learning/scripts/generate_training_plan.py --lang es
```

After generating the plan, run `python3 wizard/scripts/auto_fill_from_plan.py --lang en` or use `/implementation-wizard` Mode D to populate 7 of the 11 implementation guide fields.
