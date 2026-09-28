# `relatorios/templates/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Reports](../README.md)

Jinja2 templates for report PDFs. Coordinate changes because they affect every client who uses the kit.

## Contents

| File | Renders |
| --- | --- |
| [`v2_assessment_summary.html.j2`](v2_assessment_summary.html.j2) | `v2_assessment_summary.pdf`: executive summary, scoring, priorities, evidence cross-checks, and Developer Survey context when available. |
| [`v2_roadmap_group.html.j2`](v2_roadmap_group.html.j2) | Group roadmap PDFs G1, G2, and G3. |
| [`v2_implementation_guide.html.j2`](v2_implementation_guide.html.j2) | `v2_implementation_guide.pdf`: governance, dimension owners, RACI, phased plan, change management, risks, metrics, first 90 days, and references. |
| [`v2_round_comparison.html.j2`](v2_round_comparison.html.j2) | `comparacao-rodadas.pdf` from `scripts/compare_rounds.py --pdf`. |
| [`_v2_components.html.j2`](_v2_components.html.j2) | Shared v2 macros. |
| [`_print.css`](_print.css) | Print CSS with the Microsoft four-square visual treatment. |
| Legacy templates | Archived v1 report templates used only by v1 dispatch. |

## How to customize

> [!CAUTION]
> Editing `.html.j2` files affects all clients who use the kit. For per-client customization, edit `implementation-guide-inputs.json` or rerun the wizard, then render again.

If you change templates:

1. Run `make smoke`.
2. Run `make validate-docs`.
3. Compare with outputs under [../../referencia/exemplo-saida/](../../referencia/exemplo-saida/).

## Key variables consumed

Each template expects fields from `payload_v2.json`. The implementation guide reads normalized wizard fields from `relatorios/scripts/wizard_inputs.py`; empty values render as `to fill with the client`.

## i18n

Localizable strings live in [../i18n/](../i18n/) (`en.json`, `es.json`, `pt-br.json`). Templates read them via `{{ t('key') }}`.
