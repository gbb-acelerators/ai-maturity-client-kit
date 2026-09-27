# `relatorios/`: official Jinja2 templates + Python renderer (final PDFs)

🌐 English · [Português (Brasil)](README.pt-br.md)

This folder contains the **pipeline that generates the 5 production-quality PDFs**, a faithful mirror of the web platform. The templates are copied from `app/src/report-service/templates/` (same version as the production code).

> ⚠️ **Do not modify** the `templates/` and `i18n/` files: any change breaks parity with the platform. To customize branding or content, edit the `payload.json` generated in `saida/` before re-rendering.

## Structure

```
relatorios/
├── templates/                          ← 4 official .html.j2 + print CSS
│   ├── _components.html.j2             (reusable components: tables, badges, headers)
│   ├── _print.css                      (branding + pagination + L0-L4 colors + responsive)
│   ├── score_justification.html.j2     (PDF #1: score justification + PE Readiness)
│   ├── roadmap_part_pillar.html.j2     (PDF #2/#3/#4: rendered 3x, 1 per pillar)
│   └── roadmap_part4.html.j2           (PDF #5: consolidated implementation guide)
│
├── i18n/                               ← Strings for the 3 supported languages
│   ├── en.json                         (~21 KB)
│   ├── es.json                         (~22 KB)
│   └── pt-br.json                      (~22 KB)
│
├── scripts/
│   ├── build_payload_and_render.py     ⭐ Main script, invoked by /gerar-relatorio
│   ├── render_reports.py               (pure Jinja2 + WeasyPrint renderer)
│   └── render_smoke.py                 (smoke test of the original template, reference)
│
└── sample_payload.json                 (~66 KB, schema reference + Acme sample data)
```

## How the pipeline works

```
┌─ INPUTS ────────────────────────────────────────────────┐
│  respostas.json                                          │
│  saida/scores.json + gaps.json + recomendacoes.json     │
│  implementation-guide-inputs.json (optional)             │
│  relatorios/sample_payload.json (base structure)         │
└─────────────────┬───────────────────────────────────────┘
                  ↓
   build_payload_and_render.py:
   1. Loads sample_payload.json (complete, rich structure)
   2. OVERWRITES only the fields we have data for:
      • organization, scores, capabilities, gap_analysis
      • implementation_guide_inputs (if the wizard ran)
   3. RESETS sample (Acme) facts; builds capabilities from
      framework.json, evidence and rationale from respostas.json,
      and Part 4 from implementation-guide-inputs.json. Generic
      recommendations (risks, technologies, next steps) remain.
   4. Writes saida/payload.json (debug/customization)
   5. Invokes render_reports.py
                  ↓
   render_reports.py:
   1. Loads payload + i18n[locale] + 4 Jinja2 templates
   2. Renders 5 templates with WeasyPrint (HTML+CSS → PDF)
   3. Output: saida/*.pdf
                  ↓
┌─ OUTPUTS (saida/) ──────────────────────────────────────┐
│  payload.json                                            │
│  score_justification.pdf       (~330 KB)                 │
│  roadmap_part_pillar_p1.pdf    (~410 KB)                 │
│  roadmap_part_pillar_p2.pdf    (~410 KB)                 │
│  roadmap_part_pillar_p3.pdf    (~410 KB)                 │
│  roadmap_part4.pdf             (~510 KB)                 │
└──────────────────────────────────────────────────────────┘
```

## Running it manually (without Copilot)

```bash
# 1. Install dependencies (once)
python3 -m pip install --user --break-system-packages jinja2 weasyprint openpyxl
# Mac: brew install cairo pango gdk-pixbuf libffi

# 2. Full pipeline (needs respostas.json + saida/scores.json+gaps.json+recomendacoes.json)
python3 relatorios/scripts/build_payload_and_render.py

# 3. OR: re-render only (after editing saida/payload.json by hand)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida

# 4. OR: switch locale (en / es / pt-br)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --locale pt-br --out saida/pt-br
```

## Customization

### Pattern 1: Implementation Guide (Part 4)
```
/wizard-implementacao    # 9 steps fill in committees, RACI, ADKAR, quick wins
/gerar-relatorio         # re-renders with a personalized Part 4
```

### Pattern 2: Deep narrative (per capability)
```bash
# After the first render:
code saida/payload.json   # edit fields:
                          # • capabilities[].scoring_rationale
                          # • capabilities[].h1_initiatives, h1_state_evidence
                          # • technology_resources_per_pillar
                          # • risks_per_pillar, success_metrics_per_pillar

# Re-render (skips the merge):
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

### Pattern 3: Change the language
PDFs are rendered in English by default. Set `respostas.json::metadata.language` to `"pt-BR"` or `"es"` (or `"en"`) and run `/gerar-relatorio`. Level labels, capability names in the gap analysis, and default recommended actions follow the locale.

## Template version

The templates in `templates/` mirror **`app/src/report-service/templates/`** as of the app version when the kit was created. When the platform evolves its templates, update this folder by copying from the source of truth.

## Related documentation

- Scoring algorithm → [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md)
- Payload schema → see `sample_payload.json`
- Skill that invokes it → [`../.github/skills/gerar-relatorio/SKILL.md`](../.github/skills/gerar-relatorio/SKILL.md)
- Example PDFs → [`../referencia/exemplo-saida/`](../referencia/exemplo-saida/)
