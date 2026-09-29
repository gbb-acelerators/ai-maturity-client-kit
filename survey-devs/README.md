# `survey-devs/`: Developer Survey (anonymous, behavioral, individual)

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

This folder contains a survey separate from the main assessment. It measures how developers use GitHub Copilot, agents, instruction files, Copilot Chat modes, AI development practices, governance, and security day to day. It is anonymous.

## Difference vs. the main assessment and survey-learning

| Aspect | Main assessment | Developer Survey | survey-learning |
| --- | --- | --- | --- |
| Audience | Leadership, architects, and Tech Leads | Individual developers | Individual developers |
| Anonymous? | No | Yes | No, identified by name and email |
| Focus | Organizational maturity, v2 D1 to D9 | Real individual adoption and practice, `DS-D2` to `DS-D8` | What people want to learn |
| Output | 5 v2 PDFs, workbook, JSONs | Insights report and computed maturity JSON | Capacitation plan and Champions |
| Scoring impact | Source of v2 scores | Context only | Context and wizard auto-fill only |

Survey results never change v2 assessment scores.

## Survey dimensions

Developer Survey dimensions are now named `DS-D2` to `DS-D8` in JSON keys, insights, training plan cohorts, and cross-references. Forms built with the old `D2` style text still parse.

| ID | Focus |
| --- | --- |
| `DS-D2` | Copilot adoption and modes. |
| `DS-D3` | Microsoft and GitHub ecosystem tools. |
| `DS-D4` | AI development practices. |
| `DS-D5` | Agent concepts and structure. |
| `DS-D6` | Markdown, memory, and instructions. |
| `DS-D7` | Usability and best practices. |
| `DS-D8` | Security and governance. |

## Crosswalk to framework v2

`framework.v2.json` maps each `DS-D#` to the v2 questions it helps validate:

| Survey dimension | v2 questions |
| --- | --- |
| `DS-D2` | D4-Q1, D4-Q2, D9-Q1 |
| `DS-D3` | D4-Q3, D4-Q6, D3-Q2, D6-Q1 |
| `DS-D4` | D3-Q2, D5-Q5, D2-Q6 |
| `DS-D5` | D2-Q4, D4-Q5 |
| `DS-D6` | D4-Q4, D4-Q5 |
| `DS-D7` | D2-Q2, D9-Q4 |
| `DS-D8` | D1-Q2, D6-Q1, D6-Q4, D6-Q5, D6-Q7 |

The insights report section 12 links to v2 questions, not v1 capabilities. The v2 summary PDF shows Developer Survey context when `output/developer-survey-maturity-*.json` exists.

## Files in this folder

| File | What it is |
| --- | --- |
| [FORMS-INSTRUCTIONS-DEVS.md](FORMS-INSTRUCTIONS-DEVS.md) | Step-by-step guide to build the Microsoft Forms. |
| [question-bank-devs.md](question-bank-devs.md) | English question bank. |
| [question-bank-devs.pt-br.md](question-bank-devs.pt-br.md) | Portuguese (Brazil) question bank; its options are the canonical values in [options.json](options.json). |
| [question-bank-devs.es.md](question-bank-devs.es.md) | Spanish question bank. |
| [template-export-forms-devs.xlsx](template-export-forms-devs.xlsx) | Excel template in the Forms export format. |
| [mock-responses-devs.json](mock-responses-devs.json) | Sample structured JSON for smoke tests. |
| [MATURITY-RUBRIC.md](MATURITY-RUBRIC.md) | Deterministic rubric. It keeps the v1 score bands, so compare by score, not by level name. |
| [scripts/](scripts/) | Import, scoring, and insights scripts. |

## Usage flow

```text
1. Build the Forms with FORMS-INSTRUCTIONS-DEVS.md.
2. Collect responses anonymously.
3. Export to Excel.
4. Run /import-survey-devs.
5. Run /insights-developer-survey.
6. Re-run make pipeline if you want the v2 summary PDF to include Developer Survey context.
```

Scripts write EN by default, PT-BR with `--lang pt-br` or Spanish with `--lang es`. The EN and ES question banks translate the answer options; [options.json](options.json) maps the options of all three languages (and older Portuguese forms whose options had dashes) to the same canonical option before scoring, so the result does not depend on the form language.
