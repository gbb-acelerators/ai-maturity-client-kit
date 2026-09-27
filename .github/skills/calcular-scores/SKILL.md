---
name: calcular-scores
description: Computes capability/pillar/overall scores from respostas.json applying the official SUMPRODUCT algorithm from the platform. Generates saida/scores.json. Use when the user asks to "calcular scores", "computar pontuação", "rodar o scoring", "compute scores", "calculate maturity scores", "run the scoring".
---

# Skill: Compute scores (official algorithm)

## When to use
- After client filled `respostas.json`.
- Whenever there's a change in `respostas.json` or `target_overrides`.
- As prerequisite for `/gap-analysis`, `/recomendar-estrategias` and `/gerar-relatorio`.

## Inputs
- `respostas.json` — `responses[qid] = {level, evidence}` + `target_overrides[cap_id]`. `level` may be `null` or any number in the inclusive range `0..4`; multi-respondent imports can produce averages such as `2.5`.
- `framework.json` — question and capability weights + cap→strategies

## Expected output
- `saida/scores.json` — full structure (see schema below)
- Brief chat message (English by default, or the user's language) with overall score + label + threshold.

## Implementation: invoke the official script

Run the deterministic engine. **DO NOT compute scores in chat**: the algorithm below documents what the script does.

```bash
python3 scripts/assessment_engine.py scores
# or scores + gaps + recommendations in one go:
python3 scripts/assessment_engine.py all
```

If the script reports invalid levels, show the listed question IDs to the client and stop. `make test` runs the golden tests that pin the engine to `referencia/exemplo-saida/`.

## Algorithm (follow EXACTLY — mirrors `referencia/pontuacao-e-calculo.md`)

### 1. Capability score
For each capability `c`:
```
wsum   = 0
wtotal = 0
for each question q in c.questions:
    if respostas[q.id].level != null:
        wsum   += respostas[q.id].level × q.weight
        wtotal += q.weight
score_c = wsum / wtotal     if wtotal > 0
        = null              otherwise (no answers)
```

### 2. Pillar score
For each pillar `p`:
```
ws = 0; wt = 0
for each capability c in p (with score_c != null):
    ws += score_c × c.weight
    wt += c.weight
score_p = ws / wt     if wt > 0
        = 0.0         otherwise
```

### 3. Overall score
```
ws = 0; wt = 0
for each capability c in ALL 28 capabilities (with score_c != null):
    ws += score_c × c.weight
    wt += c.weight
overall = ws / wt
```

**ATTENTION**: Overall is NOT mean of the 3 pillars. It's direct SUMPRODUCT over all capabilities.

### 4. Labels
Canonical label strings (Portuguese by design, shared with the platform and `build_payload_and_render.py`); keep them verbatim in `scores.json`:
```
score < 0.5  → "L0 — Inicial"
[0.5, 1.5)   → "L1 — Em Desenvolvimento"
[1.5, 2.5)   → "L2 — Definido"
[2.5, 3.5)   → "L3 — Gerenciado"
score ≥ 3.5  → "L4 — Otimizando"
```

In chat and English reports, display them as L0 Initial, L1 Developing, L2 Defined, L3 Managed, and L4 Optimizing.

### 5. Threshold
```
total_answered ≥ 40  → "OK"
25–39                → "WARNING"
< 25                 → "BLOCKED"  (still compute scores, but mark)
```

### 6. PE Score (optional — only if there are questions with `pe: true`)
- Filter questions with `pe: true` in `framework.json`.
- Reapply steps 1–3 with this subset.
- If no `pe: true` question is answered → `pe_score = null`.

## `saida/scores.json` schema

```json
{
  "metadata": {
    "computed_at": "2026-05-08T14:23:00Z",
    "respondent": "<from respostas.json::metadata>",
    "framework_version": "<from framework.json::version>"
  },
  "overall": {
    "score": 2.413,
    "label": "L2 — Definido",
    "pe_score": 1.875,
    "pe_label": "L1 — Em Desenvolvimento"
  },
  "threshold": {
    "status": "WARNING",
    "answered": 32,
    "applicable": 158
  },
  "pillars": [
    {"id": "P1", "name_pt_br": "Produtividade do Desenvolvedor", "score": 2.6, "label": "L3 — Gerenciado", "answered": 18, "applicable": 53},
    {"id": "P2", "name_pt_br": "Ciclo de Vida DevOps",          "score": 2.1, "label": "L2 — Definido",   "answered": 9,  "applicable": 59},
    {"id": "P3", "name_pt_br": "Plataforma de Aplicações",       "score": 2.4, "label": "L2 — Definido",   "answered": 5,  "applicable": 46}
  ],
  "capabilities": [
    {"id": "P1-C1", "name_pt_br": "Assistentes de Codificação IA", "weight": 1.0, "score": 2.6, "label": "L3 — Gerenciado", "answered": 5, "applicable": 5, "strategies": ["S5"]}
  ]
}
```

## Implementation hint
- Use Python with `json` stdlib. **DO NOT** use Excel/openpyxl here — this skill is pure computation.
- Rounding: none in computation. For display (chat / scores.json), use 3 decimals.
- Validate levels as numeric values in `[0, 4]` or `null`. Do not require integers.

## Report in chat (English by default, or the user's language)
```
✓ Scores computed → saida/scores.json
• Overall: 2.413 (L2 Defined)
• PE: 1.875 (L1 Developing)
• Threshold: WARNING (32/158 answered)
• Pillars: P1=2.6 L3 · P2=2.1 L2 · P3=2.4 L2
• Next: /gap-analysis
```

## Constraints
- Never round before saving (preserve `f64`).
- Never include capabilities with `score=null` in pillar/overall SUMPRODUCT.
- If `total_answered < 25`, still compute but mark `threshold.status="BLOCKED"` and warn the client (English by default, or the user's language) that the executive report shouldn't be used for decisions.

## Preflight: framework_version check

Before computing, compare `respostas.json::metadata.framework_version` against `framework.json::version`:

```python
rf = respostas.get("metadata", {}).get("framework_version")
ff = framework.get("version")
if rf and ff and rf != ff:
    warn(
        f"⚠️ respostas.json was filled against framework {rf}, "
        f"but framework.json is at version {ff}. Weights and questions may "
        f"have changed. Recommended: revalidate answers before publishing the report."
    )
```

Do not block execution — only surface the mismatch.
