---
name: recomendar-estrategias
description: Maps deterministic v2 dimension priorities, or archived v1 capability gaps, to strategies S1-S7 by invoking scripts/assessment_engine.py. Use for "recommend strategies", "recomendar estrategias", "which initiatives should we prioritize".
---

# Skill: Recommend strategies

Do not map strategies by hand. Run the official engine.

## Command

```bash
python3 scripts/assessment_engine.py all
```

## v2 strategy rules

- Strategies are `S1` to `S7`.
- The engine sums priority for mapped dimensions.
- A strategy is recommended when the summed priority is at least `0.9`.
- Strategy recommendations should preserve links to the contributing dimensions and questions from `saida/recomendacoes.json`.

## v2 context

Report groups for PDFs are:

- G1: D1, D2, D9, direction, people, and value.
- G2: D3, D4, D5, plan, code, review, and quality.
- G3: D6, D7, D8, security, delivery, and foundations.

## v1 behavior

v1 inputs still use the archived capability to strategy mapping from `framework.json`.

## Chat response

List recommended strategies in priority order with contributing dimensions or capabilities, priority total, and first actions. State that the values came from `saida/recomendacoes.json`.
