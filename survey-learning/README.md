# `survey-learning/`: Learning and Growth Survey (identified, capacitation)

🌐 English · [Português (Brasil)](README.pt-br.md)

This identified survey generates the capacitation plan used by leadership and by the implementation guide wizard. It complements the main assessment and the anonymous Developer Survey.

## Difference vs. the other surveys

| Aspect | Main assessment | Developer Survey | Learning Survey |
| --- | --- | --- | --- |
| Audience | Leadership | Anonymous developers | Identified developers |
| Focus | Organizational maturity, D1 to D9 | Behavior and practice, `DS-D2` to `DS-D8` | Learning demand and Champions |
| Output | 5 v2 PDFs | Insights and maturity JSON | `saida/plano-capacitacao-<date>.md` |
| Scoring impact | Source of v2 scores | Context only | Context and wizard auto-fill only |

## Learning Survey IDs

Learning Survey question bank labels use `L#-Q#`. Where a question refers to Developer Survey dimensions, it uses `DS-D#`, for example `L2-Q1: DS-D2 Copilot Adoption ...`. This avoids collision with v2 assessment dimensions D1 to D9.

## Files in this folder

| File | What it is |
| --- | --- |
| [INSTRUCOES-FORMS-LEARNING.md](INSTRUCOES-FORMS-LEARNING.md) | How to build the identified Microsoft Forms. |
| [perguntas-para-forms-learning.md](perguntas-para-forms-learning.md) | Canonical PT-BR question bank. |
| [perguntas-para-forms-learning.en.md](perguntas-para-forms-learning.en.md) | English question bank. |
| [perguntas-para-forms-learning.es.md](perguntas-para-forms-learning.es.md) | Spanish question bank for collection. The scripts write EN, PT-BR or ES (`--lang es`). |
| [template-export-forms-learning.xlsx](template-export-forms-learning.xlsx) | Excel template. |
| [respostas-mock-learning.json](respostas-mock-learning.json) | Sample structured JSON. |
| [scripts/](scripts/) | Capacitation plan generator. |

## Usage flow

```text
1. Build the Forms with INSTRUCOES-FORMS-LEARNING.md.
2. Share with developers.
3. Export responses to Excel.
4. Run /importar-survey-learning.
5. Run /plano-capacitacao.
6. Run /wizard-implementacao Mode D, or run wizard/scripts/auto_fill_from_plano.py.
7. Run make pipeline to refresh v2_implementation_guide.pdf.
```

## What the capacitation plan contains

`saida/plano-capacitacao-<date>.md` is written in English by default or PT-BR with `--lang pt-br`. It includes requested topics, suggested cohorts per `DS-D#`, Champions, mentor pairs, a 90-day calendar, barriers, wishlist, and prioritized actions.

## Connection with the wizard

Mode D fills 7 of the 11 implementation guide fields from the Learning Survey plan: steering committee from active Champions, communication plan from the calendar, training plan from cohorts, ADKAR notes, and quick wins. The remaining fields are marked as fill-in items.
