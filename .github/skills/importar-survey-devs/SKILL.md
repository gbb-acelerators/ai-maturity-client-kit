---
name: importar-survey-devs
description: Imports Developer Survey Microsoft Forms exports using the existing survey-devs tooling. Use for "import survey-devs", "importar survey de devs", "developer survey import".
---

# Skill: Import Developer Survey

The Developer Survey is unchanged by framework v2. Use its existing scripts and question bank. Do not mix its dimensions into assessment scoring.

## Rule for dimension names

When the Developer Survey appears beside the v2 assessment, call its dimensions `DS-D#` to avoid collision with assessment dimensions `D1` to `D9`.

## Procedure

Run the repository script or Make target documented under [survey-devs/](../../../survey-devs/). Keep outputs in `saida/` and report respondent count, warnings, and next step.

## Cross-reference to v2

Use Developer Survey insights to contextualize v2 D2, D5, and D9. Do not recompute v2 scores from survey answers.
