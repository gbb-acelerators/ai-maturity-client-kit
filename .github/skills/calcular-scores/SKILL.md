---
name: calcular-scores
description: Computes v2 dimension and overall scores, or archived v1 scores, by invoking scripts/assessment_engine.py. Use for "calcular scores", "computar pontuacao", "rodar scoring", "compute scores", "calculate maturity scores".
---

# Skill: Compute scores

Always invoke the deterministic engine. Do not compute scores in chat or Excel.

## Inputs

- `respostas.json` at the workspace root.
- v2 inputs have `metadata.framework_version` such as `2.0.1` and use `respondents[].answers["D#-Q#"]`.
- v1 inputs have no `metadata.framework_version`, or a `1.x` version, and use the archived `framework.json` flow.

## Command

```bash
python3 scripts/assessment_engine.py all
```

Use `all` so `scores.json`, `gaps.json`, and `recomendacoes.json` stay consistent. `make scores` is equivalent.

## v2 scoring facts

- Question score is the pooled mean of respondent values, excluding blank and `NA` (`level: null`).
- Dimension score is the mean of its question scores.
- Overall score is the weighted mean of dimensions.
- Default dimension weight is `1.0`; `dimension_weights` may set values from `0.5` to `2.0`.
- Levels: L0 Not started, L1 Exploring, L2 Adopting, L3 Scaling, L4 AI-native.
- Bands: L0 `[0,0.8)`, L1 `[0.8,1.6)`, L2 `[1.6,2.4)`, L3 `[2.4,3.2)`, L4 `[3.2,4.0]`.
- Coverage: OK at 37 or more answered questions, WARNING at 25 to 36, BLOCKED below 25.

## v2 model

- 9 dimensions, 61 scored questions.
- IDs: `D#-Q#`; profile IDs: `R-Q1` to `R-Q5`.
- Dimensions: D1 Strategy and Governance, D2 Enablement and Culture, D3 Plan and Design, D4 Code and Context Engineering, D5 Review and Quality, D6 Security and AI Supply Chain, D7 Deliver and Operate, D8 Engineering Foundations, D9 Measurement and AI FinOps.

## Output

- `saida/scores.json`
- Also refreshed by `all`: `saida/gaps.json`, `saida/recomendacoes.json`

## Chat response

Report the framework detected, overall score and band, coverage status, key flags surfaced by the script, and next step. If the script lists invalid levels or schema issues, stop and show those IDs.
