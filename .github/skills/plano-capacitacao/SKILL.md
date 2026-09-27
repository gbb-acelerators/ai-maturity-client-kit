---
name: plano-capacitacao
description: Generates a prioritized learning and capacitation plan from the Learning and Growth Survey. Use for "plano de capacitacao", "training plan", "learning roadmap".
---

# Skill: Capacitation plan

The Learning and Growth Survey is unchanged by framework v2. Use the existing survey-learning scripts and outputs.

## Deterministic rule

Do not derive cohorts, rankings, or mentor matches by hand when scripts exist. Use the repository tooling documented under [survey-learning/](../../../survey-learning/).

## Cross-reference to v2

Connect the plan to v2 without changing v2 scores:

- D2: enablement, skills, culture.
- D5: review, quality, testing, verification culture.
- D9: measurement, value, AI FinOps.

When the Developer Survey is also mentioned, label its dimensions `DS-D#` to avoid confusion with v2 dimensions.

## Output

Reference `saida/plano-capacitacao-<date>.md`. Summarize top topics, cohorts, champions, mentor pairs, and 90 day plan when present in the generated artifact.
