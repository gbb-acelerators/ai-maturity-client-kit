# AI Maturity Assessment Kit · English Edition

> Self-service kit to run the AI Maturity Assessment with GitHub Copilot.
> **3 complementary surveys · 5 production-quality PDFs · personalized capacitation roadmap.**

[![Site](https://img.shields.io/badge/site-paulasilvatech.github.io-00A4EF)](https://paulasilvatech.github.io/ai-maturity-client-kit/en/)
[![Download ZIP](https://img.shields.io/badge/download-EN%20kit.zip-7FBA00)](https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip)

---

## What this is

A **self-contained kit** to run an end-to-end AI maturity assessment **without depending on a web platform**. It includes:

- **158-question framework** organized in 3 pillars × 28 capabilities × 7 strategies
- **3 complementary surveys**: organizational Assessment + anonymous Developer Survey + identified Learning & Growth Survey
- **12 custom Copilot Chat skills + 1 prompt + 1 concierge agent** that orchestrate the full pipeline
- **5 executive PDFs** rendered with paulasilva-ms branding (Microsoft 4-color palette) — already localized in EN via `relatorios/i18n/en.json`
- **Auditable Excel workbook** with native SUMPRODUCT formulas
- **Capacitation plan** with attendee names + emails

## ⚠ Important note on language

The English ZIP package follows a deliberate language split:

1. **Copilot customization files stay in English** — `.github/copilot-instructions.md`, `.github/agents/`, `.github/prompts/`, and `.github/skills/` are the agent runtime and are intentionally shared across all language packages.
2. **Client-facing documentation is English** — `README.md`, `STEP-BY-STEP.md`, `FORMS-INSTRUCTIONS.md`, and `PACKAGE-LANGUAGE-NOTES.md` are placed at the ZIP root.
3. **Shared runtime assets are language-neutral** — JSON schemas, scripts, templates, workbooks, and scoring IDs are reused. Canonical question IDs and some internal field names remain in Portuguese where required by the scoring framework and production platform mapping.
4. **PDFs render in English** via `relatorios/i18n/en.json` — set `metadata.language: "en"` in `respostas.json` and the 5 PDFs come out in English.

If you need the framework JSON fully translated, contact Paula Silva on [LinkedIn](https://linkedin.com/in/paulanunes).

## Quick start

```bash
# 1. Download the ZIP from the site, extract it, and open the folder in VS Code

# 2. Validate prerequisites
make smoke

# 3. Copy the sample data and run the full pipeline
cp respostas.json.example respostas.json

# Open VS Code, then in Copilot Chat (Agent mode):
#   @ai-maturity-assistant
# or:
#   /pipeline-completo
```

Output appears in `saida/` (5 PDFs + scores.json + gaps.json + recomendacoes.json + auditable Excel).

## The 3 surveys

| Survey | Audience | Questions | Time | Output |
| --- | --- | --- | --- | --- |
| 🅰️ **AI Maturity Assessment** | Leadership / org | 158 | 60-90 min | 5 executive PDFs |
| 🅱️ **Developer Survey** | Anonymous devs | 75 | 22-28 min/dev | Behavioral insights + L0-L4 maturity per dimension |
| 🅲 **Learning & Growth** | Identified devs | 32 | 5-8 min/dev | Capacitation roadmap with attendee lists |

Recommended order for serious consulting: **B (anonymous) → C (identified) → A (leadership)**. Each survey informs the next; the concierge agent cross-validates results automatically.

## Pipeline in one line

```text
INPUT (respostas.json or Forms .xlsx)
  → /calcular-scores          (3-layer SUMPRODUCT)
  → /gap-analysis             (P0 / P1 / P2 / P3 priorities)
  → /recomendar-estrategias   (S1 to S7 + technologies)
  → /wizard-implementacao     (9 inputs for Part 4 PDF)
  → /gerar-relatorio          (Jinja2 + WeasyPrint)
OUTPUT (5 PDFs + auditable XLSX)
```

## What's translated in this folder

| File | Status |
| --- | --- |
| [README.md](README.md) | ✅ Translated |
| [GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md) | ✅ Translated as `STEP-BY-STEP.md` |
| [INSTRUCOES-FORMS.md](INSTRUCOES-FORMS.md) | ✅ Translated as `FORMS-INSTRUCTIONS.md` |
| Copilot customizations under `.github/` | ✅ Included, intentionally in English |
| Shared JSON, scripts, templates, workbooks | ✅ Included as runtime assets |
| PDF reports | ✅ Already EN via `relatorios/i18n/en.json` |

## Continue reading

| ⬅ Previous | Next ➡ |
| :--- | ---: |
| [🏠 Main site (multi-language)](https://paulasilvatech.github.io/ai-maturity-client-kit/) | [📘 Detailed step-by-step](STEP-BY-STEP.md) |

---

**Paula Silva** — Global Developer Solutions Advisor | [LinkedIn](https://linkedin.com/in/paulanunes)
*Building the future of software development with AI and Agentic DevOps*
