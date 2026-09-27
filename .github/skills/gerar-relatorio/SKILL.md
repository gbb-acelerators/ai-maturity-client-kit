---
name: gerar-relatorio
description: Renders 5 client-ready PDF reports (Score Justification + 3 Pillar Roadmaps + Implementation Guide) by invoking relatorios/scripts/build_payload_and_render.py. The script merges sample_payload.json (rich structure) with client data from saida/scores.json + gaps.json + recomendacoes.json + respostas.json + implementation-guide-inputs.json. Output is identical-quality to the platform's production PDFs. Use when the user asks to "gerar relatório", "produzir o report executivo", "gerar PDFs", "PDF final", "consolidar resultados", "executive report", "final report", "render PDF", "generate report PDFs", "produzir o PDF executivo".
---

# Skill: Generate executive PDF reports

## What this does

Invokes the script **`relatorios/scripts/build_payload_and_render.py`** which:
1. Loads `relatorios/sample_payload.json` as **base structure** (provides all the rich nested fields the Jinja2 templates need: scoring_rationale, h1_initiatives, technology_resources, success_metrics, risks, etc.)
2. **Overrides only the fields we have client data for**:
   - `organization` ← `respostas.json::metadata`
   - `scores.overall.weighted_avg` / `level_label` / `gap` ← `saida/scores.json`
   - `scores.pillars[].weighted_avg` / `level_label` / `gap` ← `saida/scores.json`
   - `capabilities[].current_score` / `current_level_label` / `gap` ← `saida/scores.json` (matched by id)
   - `gap_analysis[]` ← rebuilt from `saida/gaps.json` (preserves sample's `recommended_actions` per cap)
   - `implementation_guide_inputs.*` ← `implementation-guide-inputs.json` if exists (output of `/wizard-implementacao`)
3. Writes merged payload to `saida/payload.json`
4. Invokes `relatorios/scripts/render_reports.py` to produce 5 PDFs in `saida/`

## When to use
- After `/calcular-scores`, `/gap-analysis`, `/recomendar-estrategias` (pipeline order).
- When client wants the final **5 production-quality PDFs**.
- After editing `implementation-guide-inputs.json` (re-renders Part 4 with personalized content).
- After manually editing `saida/payload.json` (re-renders with custom narrative).

## Inputs (from workspace root unless specified)

| File | Required | Source |
|---|---|---|
| `respostas.json` | yes | client (or `/importar-respostas-excel`) |
| `saida/scores.json` | yes | `/calcular-scores` |
| `saida/gaps.json` | yes | `/gap-analysis` |
| `saida/recomendacoes.json` | yes | `/recomendar-estrategias` |
| `implementation-guide-inputs.json` | optional | `/wizard-implementacao` |
| `saida/plano-capacitacao-<DATE>.md` | optional | `/plano-capacitacao` (Learning Survey) |
| `saida/insights-developer-survey-<DATE>.md` | optional | `/insights-developer-survey` (Survey-devs) |
| `saida/maturidade-developer-survey-<DATE>.json` | optional | `/insights-developer-survey` (rubric scores) |
| `relatorios/sample_payload.json` | yes | bundled with kit |
| `relatorios/templates/*.html.j2` | yes | bundled with kit |
| `relatorios/i18n/<locale>.json` | yes | bundled with kit |

### Cross-survey integration (when complementary survey outputs exist)

If `/insights-developer-survey` or `/plano-capacitacao` already ran, the script `build_payload_and_render.py` populates `payload.cross_survey_data` with structured pointers to the latest artifacts:

| Field in `payload.cross_survey_data` | Source artifact | Content |
|---|---|---|
| `developer_survey_maturity` | `saida/maturidade-developer-survey-<DATE>.json` | Per-dimension rubric scores (D2–D8) + respondent count |
| `developer_survey_insights` | `saida/insights-developer-survey-<DATE>.md` | Path reference (full markdown stays alongside the PDFs) |
| `learning_plan` | `saida/plano-capacitacao-<DATE>.md` | Path reference (auto-fill into Part 4 happens via `wizard/scripts/auto_fill_from_plano.py`) |

The data is always written to `saida/payload.json` for inspection. When `payload.cross_survey_data.available` is true, `score_justification.pdf` renders a dedicated "Complementary Survey Signals" section with Developer Survey maturity dimensions and source artifact references.

## Output (in `saida/`)

| File | Size (approx) | Content |
|---|---|---|
| **payload.json** | ~80 KB | Merged data the templates consumed (debug/customization) |
| **score_justification.pdf** | ~330 KB | Justification + PE Readiness + path recommendation |
| **roadmap_part_pillar_p1.pdf** | ~410 KB | Productivity pillar deep-dive |
| **roadmap_part_pillar_p2.pdf** | ~410 KB | DevOps pillar deep-dive |
| **roadmap_part_pillar_p3.pdf** | ~410 KB | Platform pillar deep-dive |
| **roadmap_part4.pdf** | ~510 KB | Implementation Guide consolidated (uses `implementation-guide-inputs.json` if present) |

## Procedure

### 1. Pre-flight checks

```python
from pathlib import Path
KIT = Path.cwd()  # workspace root

required = ["respostas.json", "saida/scores.json", "saida/gaps.json", "saida/recomendacoes.json"]
missing = [f for f in required if not (KIT / f).exists()]
if missing:
    error(f"Missing: {missing}. Run /pipeline-completo first.")
```

### 2. Confirm dependencies installed

```bash
python3 -c "import jinja2, weasyprint, openpyxl" 2>&1 \
  || python3 -m pip install --user --break-system-packages jinja2 weasyprint openpyxl
```

### 3. Invoke the script

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

Script does everything: merge → write payload.json → render 5 PDFs. Reports each step.

PDF language comes from `respostas.json::metadata.language`: `"en"` (default), `"pt-BR"`, or `"es"`. For Portuguese PDFs, set `"language": "pt-BR"` and run the same command.

### 4. Verify outputs

```python
expected = [
    "score_justification.pdf",
    "roadmap_part_pillar_p1.pdf",
    "roadmap_part_pillar_p2.pdf",
    "roadmap_part_pillar_p3.pdf",
    "roadmap_part4.pdf",
    "payload.json",
]
for name in expected:
    f = KIT / "saida" / name
    if not f.exists() or f.stat().st_size < 50_000:
        warn(f"Suspicious output: {name}")
```

## Report in chat (English by default, or the user's language)

```
✓ 5 production-quality PDFs generated in saida/:
   📄 score_justification.pdf       (331 KB): Justification + PE Readiness
   📄 roadmap_part_pillar_p1.pdf    (415 KB): Productivity pillar
   📄 roadmap_part_pillar_p2.pdf    (417 KB): DevOps pillar
   📄 roadmap_part_pillar_p3.pdf    (419 KB): Platform pillar
   📄 roadmap_part4.pdf             (516 KB): Implementation Guide

📊 Summary:
   Organization: Cliente Exemplo S.A.
   Overall: 1.99 (L2 Defined)
   Locale: en
   Threshold: OK (46/158 answered)

⚠️ Personalization:
   Sections without client data show "Not specified" or a wizard
   placeholder (never sample facts). To fill them:

   1. Run /wizard-implementacao for Part 4 (Implementation Guide)
   2. OR edit saida/payload.json directly and re-render:
        python3 relatorios/scripts/render_reports.py --payload saida/payload.json

📋 Next steps:
   1. Open saida/score_justification.pdf in Preview/Acrobat
   2. Check that Cliente Exemplo S.A. and the scores appear correctly
   3. Share the PDFs with leadership
```

## Customization patterns

### Pattern 1: Personalize Implementation Guide (Part 4)
```
/wizard-implementacao    # 9 steps, generates implementation-guide-inputs.json
/gerar-relatorio         # re-renders with personalized Part 4
```

### Pattern 2: Personalize narrative fields (capabilities, risks, etc.)
```bash
# 1. Render once to create payload.json
/gerar-relatorio

# 2. Edit saida/payload.json manually:
#    - capabilities[].scoring_rationale (generated from scores + evidence)
#    - capabilities[].h1_initiatives (empty by default; add client actions)
#    - technology_resources_per_pillar (customize tools)
#    - risks_per_pillar (real risks identified)
#    - success_metrics_per_pillar (real KPIs being tracked)

# 3. Re-render only (skip merge):
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

### Pattern 3: Different language
```bash
# Set respostas.json::metadata.language to "en" (default), "pt-BR", or "es"
/gerar-relatorio   # re-renders in selected locale
```

## Branding (paulasilva-ms)

The script automatically injects **paulasilva-ms branding** into the payload (replaces the sample's default branding block):

- `payload.branding.name` = "Paula Silva | Software Global Black Belt"
- `payload.branding.contact` = "paulasilva@microsoft.com"
- `payload.branding.tagline` = "Building the future of software development with AI and Agentic DevOps"
- `payload.branding.palette` = MS 4-color (#00A4EF, #7FBA00, #FFB900, #F25022)

The CSS used (`relatorios/templates/_print.css`) already uses the MS palette in `:root` tokens. So all 5 PDFs render with:
- Primary color = MS Blue
- Positive = MS Green · Warn = MS Yellow · Critical = MS Red
- Pillar accents: P1 = Blue, P2 = Yellow, P3 = Green
- Inter font for body, JetBrains Mono for code/labels

The branding is consistent with the chrome bar shown in the kit's interactive HTMLs (calculadora, formulários, wizard). See `referencia/branding/IDENTITY.md` for canonical strings + logo SVG.

## Constraints

- **DO NOT modify** files in `relatorios/templates/` (mirror official platform code).
- **DO NOT regenerate** payload.json structure from scratch — always start from `sample_payload.json`.
- **DO NOT skip** the script — running Jinja2 manually misses i18n + CSS + WeasyPrint setup.
- WeasyPrint must be installed: `pip install --user --break-system-packages weasyprint jinja2 openpyxl`.
- macOS may need: `brew install cairo pango gdk-pixbuf libffi`.
- Outputs in `saida/` only.

## Where each PDF field comes from

| Field | Source |
|---|---|
| Capabilities (names, weights, PE flag, audience, KPIs) | `framework.json` |
| Scores, labels, targets, gaps | `saida/scores.json` + `respostas.json::target_overrides` |
| `evidence_collected`, `h1_state_evidence` | `respostas.json` evidence text per question |
| `scoring_rationale` | Generated: weighted mean, answered count, evidence count |
| PE readiness level and path | Rubric in `score_justification.html.j2` applied to `pe_score` |
| Organization profile (industry, size, cloud, tools) | Optional keys in `respostas.json::metadata` (`industry`, `number_of_developers`, `number_of_applications`, `primary_cloud_provider`, `current_devops_tools`, `assessment_scope`, `key_business_drivers`, `timeline_for_transformation`); otherwise "Not specified" |
| Key evidence sources | Optional `respostas.json::metadata.evidence_sources` (`{"documents": [...], "dashboards": [...], "interviews": [...], "metrics": [...]}`) |
| Steering committee, TPO, RACI, communication, training, ADKAR, quick wins | `implementation-guide-inputs.json` (Markdown lists and tables are converted); otherwise a wizard placeholder |
| Success-metric "current" values | "Not specified" until the client measures them |
| Horizons, technologies, risks, next steps per pillar | Generic kit recommendations from `sample_payload.json` (edit `saida/payload.json` to tailor) |

Sample facts about the demo organization (Acme) never reach a client PDF. `make smoke` fails if they do.

## Reference example

The folder `referencia/exemplo-saida/` contains 5 PDFs generated from `respostas.json.example` (Cliente Exemplo S.A.) with the exact algorithm above. Compare these to confirm fidelity when you run `/gerar-relatorio` with your data.

## Troubleshooting

| Problem | Solution |
|---|---|
| `weasyprint not found` | `pip install --user --break-system-packages weasyprint` |
| `cairo / pango missing` (Mac) | `brew install cairo pango gdk-pixbuf libffi` |
| `StrictUndefined: 'X' is undefined` (rare) | Sample payload missing a field — open issue or add to sample |
| PDF shows "Not specified" in the organization profile | Add the optional profile keys to `respostas.json::metadata` and re-run |
| Part 4 shows wizard placeholders | Run `/wizard-implementacao` to create `implementation-guide-inputs.json` |
| PDFs show the Acme demo | `saida/scores.json` is missing: run `python3 scripts/assessment_engine.py all` first |
| Wrong language | Set `respostas.json::metadata.language` (`en`, `pt-BR`, or `es`) and re-run |
