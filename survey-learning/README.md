# `survey-learning/`: Learning and Growth Survey (identified, training)

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

This identified survey generates the training plan used by leadership and by the implementation guide wizard. It complements the main assessment and the anonymous Developer Survey.

## Difference vs. the other surveys

| Aspect | Main assessment | Developer Survey | Learning Survey |
| --- | --- | --- | --- |
| Audience | Leadership | Anonymous developers | Identified developers |
| Focus | Organizational maturity, D1 to D9 | Behavior and practice, `DS-D2` to `DS-D8` | Learning demand and Champions |
| Output | 5 v2 PDFs | Insights and maturity JSON | `output/training-plan-<date>.md` |
| Scoring impact | Source of v2 scores | Context only | Context and wizard auto-fill only |

## Learning Survey IDs

Learning Survey question bank labels use `L#-Q#`. Where a question refers to Developer Survey dimensions, it uses `DS-D#`, for example `L2-Q1: DS-D2 Copilot Adoption ...`. This avoids collision with v2 assessment dimensions D1 to D9.

## Files in this folder

| File | What it is |
| --- | --- |
| [FORMS-INSTRUCTIONS-LEARNING.md](FORMS-INSTRUCTIONS-LEARNING.md) | How to build the identified Microsoft Forms. |
| [question-bank-learning.md](question-bank-learning.md) | English question bank. |
| [question-bank-learning.pt-br.md](question-bank-learning.pt-br.md) | Portuguese (Brazil) question bank. |
| [question-bank-learning.es.md](question-bank-learning.es.md) | Spanish question bank. The scripts write EN, PT-BR or ES (`--lang es`). |
| [template-export-forms-learning.xlsx](template-export-forms-learning.xlsx) | Excel template. |
| [mock-responses-learning.json](mock-responses-learning.json) | Sample structured JSON. |
| [scripts/](scripts/) | Training plan generator. |

## Usage flow

```text
1. Build the Forms with FORMS-INSTRUCTIONS-LEARNING.md.
2. Share with developers.
3. Export responses to Excel.
4. Run /import-survey-learning.
5. Run /training-plan.
6. Run /implementation-wizard Mode D, or run wizard/scripts/auto_fill_from_plan.py.
7. Run make pipeline to refresh v2_implementation_guide.pdf.
```

## What the training plan contains

`output/training-plan-<date>.md` is written in English by default, or in PT-BR or ES with `--lang pt-br` or `--lang es`. It includes requested topics, suggested cohorts per `DS-D#`, Champions, mentor pairs, a 90-day calendar, barriers, wishlist, and prioritized actions.

## Connection with the wizard

Mode D fills 7 of the 11 implementation guide fields from the Learning Survey plan: steering committee from active Champions, communication plan from the calendar, training plan from cohorts, ADKAR notes, and quick wins. The remaining fields are marked as fill-in items.
