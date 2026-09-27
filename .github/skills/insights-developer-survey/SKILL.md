---
name: insights-developer-survey
description: Generates Developer Survey insights from imported survey outputs. Use for "developer survey insights", "insights survey devs", "maturidade dos devs".
---

# Skill: Developer Survey insights

The Developer Survey is unchanged. It is a companion signal for the v2 assessment, not a scoring input.

## Deterministic rule

Use the existing survey-devs scripts and generated JSON or Markdown artifacts. Do not score responses by hand.

## Dimension naming

When both models are in the same text, call Developer Survey dimensions `DS-D#`. Reserve `D1` to `D9` for the v2 assessment.

## Cross-reference to v2

Use the insights to explain or challenge:

- v2 D2 Enablement, Skills and Culture.
- v2 D5 Review, Quality and Testing.
- v2 D9 Measurement, Value and AI FinOps.

## Output

Write or reference `saida/insights-developer-survey-<date>.md` and any maturity JSON produced by the survey scripts. In chat, summarize adoption, governance gaps, verification culture, and measurement signals.
