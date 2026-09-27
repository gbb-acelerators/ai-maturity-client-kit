---
name: gap-analysis
description: Computes v2 dimension gaps and priorities, or archived v1 capability gaps, by invoking scripts/assessment_engine.py. Use for "gap analysis", "analise de gaps", "prioritize gaps", "where are my gaps".
---

# Skill: Gap analysis

Always use the deterministic engine. Do not calculate gaps manually.

## Command

```bash
python3 scripts/assessment_engine.py all
```

`make scores` is also acceptable because it runs the same engine target through the Makefile.

## v2 rules documented by the script

- Gap is `target - score`.
- Default target is `3.0`.
- `target_overrides` can override per dimension, for example `{"D6": 3.5}`.
- Priority score is `dimension_weight x gap`.
- Priority bands: P0 at `>= 2.4`, P1 at `>= 1.6`, P2 at `>= 0.9`, else P3.
- Low confidence, amplification risk, perception gap, scope caveat, unverified L3/L4, persona summaries, and backlog items should be reported when present in `saida/gaps.json` or related engine output.

## v2 output

- `saida/gaps.json`
- Top gaps by dimension and by question.
- Backlog: top 5 lowest questions with L3 anchors.

## v1 behavior

If the input is v1, the dispatcher keeps the archived capability gap flow based on `framework.json` and the 158 question model.

## Chat response

Summarize the P0 to P3 distribution, the top 5 priorities, coverage status, and any flags. Include the next command: `python3 relatorios/scripts/build_payload_and_render.py` after recommendations are ready.
