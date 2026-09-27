<!-- paulasilva-ms identity -->
<!--
  Paula Silva, Global Developer Solutions Advisor
  Building the future of software development with AI and Agentic DevOps
  Contact: LinkedIn https://linkedin.com/in/paulanunes
  Branding: paulasilva-ms Design System v1.7.0
  See referencia/branding/ for tokens, identity, and voice rules
-->

# AI Maturity Assessment Kit: Self-service with GitHub Copilot

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](kit-es/README.md)

**`🏠 INDEX`** · 📖 You are here · [» Step-by-step guide](GUIA-PASSO-A-PASSO.md) · [» Collection via Forms](coleta/INSTRUCOES-FORMS.md) · [» Wizard](wizard/README.md)

> [!TIP]
> **First time here?** Go straight to [GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md) or open Copilot Chat and type `@ai-maturity-assistant`. It guides you from installation to the final PDF.

🌐 **Public mini-site:** [paulasilvatech.github.io/ai-maturity-client-kit](https://paulasilvatech.github.io/ai-maturity-client-kit/): visual overview plus a download button (enable GitHub Pages in Settings → Pages → Source: GitHub Actions)

🌍 **Language kits:** English is the primary language of this repository (this README). PT-BR: [README.pt-br.md](README.pt-br.md) · Español: [kit-es/README.md](kit-es/README.md). The EN/ES ZIPs include translated documentation and the canonical PT-BR question banks to preserve parsing IDs.

> **For the client:** this package contains everything you need to run the **AI Maturity Assessment** without depending on the web platform. You fill in a JSON file, open GitHub Copilot Chat in VS Code, type one command, and receive a **spreadsheet, scores, gap analysis, strategy recommendations, and an executive report**. Reports default to English; set `metadata.language` in `respostas.json` to `"pt-BR"` or `"es"` for Portuguese (Brazil) or Spanish.

## 🔄 Visual pipeline

```mermaid
flowchart LR
    A[📝 respostas.json<br/>or Forms xlsx] --> B[/calcular-scores/]
    B --> C[/gap-analysis/]
    C --> D[/recomendar-estrategias/]
    D --> E{wizard<br/>filled in?}
    E -- yes --> F[/gerar-relatorio/]
    E -- no --> G[/wizard-implementacao/]
    G --> F
    F --> H[📄 5 PDFs<br/>+ auditable xlsx]
    style A fill:#FFB900,stroke:#333,color:#000
    style H fill:#7FBA00,stroke:#333,color:#000
    style F fill:#00A4EF,stroke:#333,color:#fff
```

---

## 🎯 When to use each survey (and expected ROI)

The kit has **3 complementary surveys**. Choose 1, 2, or all 3 based on your goal:

| Survey | Goal | Audience | Time | ROI |
|---|---|---|---|---|
| **🅰️ Main assessment** | Formal organizational baseline + 5 executive PDFs for leadership | Leadership / Tech Leads (1-3 people) | 60-90 min to collect + 5 min to generate | Canonical document for the board, comparable quarter over quarter |
| **🅱️ Developer Survey** | Validate real, anonymous maturity + identify dissonance vs. the assessment | ANONYMOUS individual devs (≥5, ideally 15+) | 22-28 min/dev + 3 min for insights | Surfaces gaps invisible to leadership; deterministic L0-L4 rubric across 7 dimensions |
| **🅲 Learning & Growth Survey** | Personalized capacitation roadmap with Champions + cohorts + workshops | IDENTIFIED devs (name+email) | 5-8 min/dev + 3 min for the plan | Concrete list of attendees per workshop; feeds wizard Mode D auto-fill |
| **🅳 All three (recommended for consulting)** | 360° view + cross-validation + action plan | Devs (anonymous + identified) + leadership | ~6 weeks (incl. collection) | Executive PDFs with **detected dissonances** + capacitation plan with attendees |

### When to run 1 vs. 2 vs. 3

- **Assessment only:** leadership already has good visibility (small org) or needs a formal deliverable quickly
- **Survey-devs only:** you want an anonymous team pulse without committing to a formal framework
- **Learning only:** the team is already mature in AI and the focus is now advanced capacitation
- **All 3:** serious consulting, investment decisions, before/after transformation baseline

> 📘 **Full breakdown of each flow (including the combination of all 3):** [GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md) Parts 1-11.

---

## ⚡ TL;DR: 3 steps

1. **Open this folder in VS Code** (`code .` or File → Open Folder).
2. **Fill in [`respostas.json`](respostas.json)**: for each question, set a `level` from 0 to 4 and an evidence text.
3. **In Copilot Chat (Agent mode), type `@ai-maturity-assistant`** (guided concierge) or `/pipeline-completo` (run everything directly).

Done. The concierge agent or the orchestrator prompt runs the 7 skills in sequence and generates everything in [`saida/`](saida/), including the **5 production-quality PDFs**.

> 🤖 **First time? Use the concierge agent.** Type `@ai-maturity-assistant` in Copilot Chat and it guides you from "how do I fill this in?" to "open the PDFs", without having to remember any command.

> 📘 **Using it for the first time?** Follow **[GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md)**: detailed instructions with per-OS setup, verbal screenshots, checkpoints, and expanded troubleshooting.
>
> 🧪 **Want to test before filling everything in?** The kit ships with **[respostas.json.example](respostas.json.example)**: 46 mocked answers from a fictional "Cliente Exemplo S.A.". Rename it to `respostas.json` and run `/pipeline-completo` to see the complete output in ~3 minutes.
>
> 📋 **Have a team and want to collect via Microsoft Forms?** See **[coleta/INSTRUCOES-FORMS.md](coleta/INSTRUCOES-FORMS.md)**: 3 paths (full manual Forms, lean Forms, direct Excel/SharePoint). The `/importar-respostas-excel` skill aggregates multiple respondents automatically.
>
> 🧙 **Want to customize Part 4 of the PDF (Implementation Guide)?** Use the **[wizard/](wizard/)**: standalone HTML (`implementation-guide-wizard.html`), an editable JSON template, or the `/wizard-implementacao` skill, which walks you through it in chat. 9 structured inputs (Steering Committee, RACI, ADKAR, Quick Wins, and more) populate `roadmap_part4.pdf`.
>
> 📄 **Want to see the final output before running?** The 5 real PDFs are in **[referencia/exemplo-saida/](referencia/exemplo-saida/)**, generated from `respostas.json.example` (Cliente Exemplo S.A.) with the real pipeline.
>
> 👥 **Want to hear from the devs (anonymous, behavioral)?** See **[survey-devs/](survey-devs/)**: a 75-question Developer Survey in 9 sections (GitHub Copilot + Ask/Edit/Agent modes + Coding Agent + Spaces + AI agents + Foundry + security). Skills: `/importar-survey-devs` + `/insights-developer-survey`. Anonymous, individual, behavioral. Includes a deterministic L0-L4 rubric across 7 dimensions.
>
> 🎓 **Want to build the capacitation roadmap (identified)?** See **[survey-learning/](survey-learning/)**: a Learning & Growth Survey of 32 short questions (5-8 min, IDENTIFIED with name+email) that becomes a plan of workshops + cohorts + Champions Network + mentoring. Skills: `/importar-survey-learning` + `/plano-capacitacao`.

---

## 📋 Prerequisites

- [ ] **VS Code** with the **GitHub Copilot Chat** extension installed and active
- [ ] **Copilot Pro / Business / Enterprise** plan (Free may work for skills; confirm with your org)
- [ ] **Python 3.10+** with `openpyxl` (`pip install openpyxl`), to fill in the spreadsheet
- [ ] **Agent** mode enabled in Copilot Chat (required to invoke custom skills)

> [!IMPORTANT]
> Without **Agent** mode enabled, the `/calcular-scores`, `/gap-analysis`, and other commands do not appear. See [GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md) (Part 1) for the how-to per operating system.
### Quick smoke test (optional, for contributors)

Validate that the pipeline is intact without needing WeasyPrint:

```bash
make smoke          # rapid e2e: copies respostas.json.example and validates the payload
make smoke-cross    # same + cross-survey (developer + learning)
```

Both restore the workspace at the end. Useful after editing `relatorios/scripts/build_payload_and_render.py` or any SKILL.md in the pipeline.
---

## 🗂 Kit structure

```
kit-cliente/
├── README.md                          ← you are here (English, primary)
├── README.pt-br.md                    ← Portuguese (Brazil) version
├── GUIA-PASSO-A-PASSO.md              ← detailed guide for beginners
├── respostas.json                     ← main INPUT (filled in manually)
├── respostas.json.example             ← 46 mocked answers for testing
├── framework.json                     ← Immutable: weights, capabilities, S1-S7
│
├── formularios/                       ← Visual HTMLs (reference)
│   ├── P1-produtividade-do-desenvolvedor.html
│   ├── P2-ciclo-de-vida-devops.html
│   └── P3-plataforma-de-aplicações.html
│
├── coleta/                            ← Multi-respondent collection for the main ASSESSMENT (Forms/Excel)
│   ├── INSTRUCOES-FORMS.md            ← 3 collection paths + tradeoffs
│   ├── perguntas-para-forms.md        ← 158 questions to copy/paste into Forms (canonical PT-BR)
│   ├── perguntas-para-forms.en.md     ← Same bank with English labels
│   └── template-export-forms.xlsx     ← Excel template (Forms export format)
│
├── survey-devs/                       ← Developer Survey (anonymous, behavioral, 75 q)
│   ├── README.md
│   ├── INSTRUCOES-FORMS-DEVS.md       ← How to create an anonymous Forms
│   ├── perguntas-para-forms-devs.md   ← 75 questions formatted for Forms (9 sections)
│   ├── template-export-forms-devs.xlsx ← Excel template + 5 mocked respondents
│   ├── respostas-mock-devs.json       ← Example structured JSON
│   ├── RUBRICA-MATURIDADE.md          ← Deterministic L0-L4 scoring model (7 dimensions)
│   └── scripts/                       ← rubric.py + calcular_maturidade.py
│
├── survey-learning/                   ← ★ Learning & Growth Survey (identified, capacitation, 32 q)
│   ├── README.md
│   ├── INSTRUCOES-FORMS-LEARNING.md   ← How to create an IDENTIFIED Forms
│   ├── perguntas-para-forms-learning.md  ← 32 formatted questions (7 sections)
│   ├── template-export-forms-learning.xlsx  ← Excel + 5 mocked respondents
│   └── respostas-mock-learning.json   ← Example structured JSON
│
├── wizard/                            ← ★ Implementation Guide Wizard (9 steps)
│   ├── implementation-guide-wizard.html       ← Standalone visual wizard
│   └── implementation-guide-inputs.template.json ← Alternative for direct editing
│
├── relatorios/                        ← Jinja2 templates + renderer (final PDFs)
│   ├── templates/                     ← 4 official .html.j2 + _print.css
│   │   ├── _components.html.j2
│   │   ├── _print.css
│   │   ├── score_justification.html.j2
│   │   ├── roadmap_part_pillar.html.j2  (rendered 3x: P1, P2, P3)
│   │   └── roadmap_part4.html.j2
│   ├── i18n/                          ← EN / ES / PT-BR strings
│   ├── scripts/
│   │   ├── render_reports.py          ← Jinja2 → WeasyPrint → PDF renderer
│   │   └── build_payload_and_render.py ← Merge sample + client data + render
│   └── sample_payload.json            ← Schema reference + sample data
│
├── referencia/                        ← Technical documentation
│   ├── pontuacao-e-calculo.md         ← Official algorithm
│   ├── pontuacao-e-calculo.xlsx       ← Auditable template
│   ├── calculadora-pontuacao.html     ← Interactive demo (with paulasilva-ms branding)
│   ├── P1/P2/P3-...md                 ← Documentation of the 158 questions
│   ├── branding/                      ← ★ paulasilva-ms identity (Microsoft)
│   │   ├── tokens-paulasilva-ms.css   ← Design tokens (4 MS colors + neutrals + dark mode)
│   │   ├── IDENTITY.md                ← Canonical strings, logo SVG, chrome bar
│   │   └── VOICE.md                   ← Voice, banned vocabulary, punctuation rules
│   └── exemplo-saida/                 ← ★ 5 real PDFs + example JSONs
│       ├── README.md
│       ├── score_justification.pdf
│       ├── roadmap_part_pillar_p1.pdf  (P2, P3)
│       ├── roadmap_part4.pdf
│       ├── pt-br/                     ← Same 5 PDFs in PT-BR
│       ├── scores.json · gaps.json · recomendacoes.json  (intermediate JSONs)
│       └── pontuacao-preenchida-2026-05-08.xlsx
│
├── saida/                             ← OUTPUT: everything Copilot generates
│
└── .github/
    ├── copilot-instructions.md        ← Loaded automatically into every prompt (EN)
    ├── agents/
    │   └── ai-maturity-assistant.agent.md       ← @ai-maturity-assistant (guided concierge)
    ├── prompts/
    │   └── pipeline-completo.prompt.md          ← /pipeline-completo
    └── skills/  (12 custom skills: 1 orchestrator + 6 assessment + 1 wizard + 2 survey-devs + 2 survey-learning)
        ├── importar-respostas-excel/SKILL.md    ← /importar-respostas-excel       (assessment)
        ├── preencher-planilha/SKILL.md          ← /preencher-planilha             (assessment)
        ├── calcular-scores/SKILL.md             ← /calcular-scores                (assessment)
        ├── gap-analysis/SKILL.md                ← /gap-analysis                   (assessment)
        ├── recomendar-estrategias/SKILL.md      ← /recomendar-estrategias         (assessment)
        ├── wizard-implementacao/SKILL.md        ← /wizard-implementacao           (assessment)
        ├── gerar-relatorio/SKILL.md             ← /gerar-relatorio  (5 PDFs)      (assessment)
        ├── importar-survey-devs/SKILL.md        ← /importar-survey-devs           (survey-devs)
        ├── insights-developer-survey/SKILL.md   ← /insights-developer-survey      (survey-devs)
        ├── importar-survey-learning/SKILL.md    ← /importar-survey-learning       (survey-learning)
        └── plano-capacitacao/SKILL.md           ← /plano-capacitacao              (survey-learning)
```

---

## 🎯 Commands available in Copilot Chat

Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) **in Agent mode** and type `/`:

### AI Maturity Assessment (main flow)

| Command | What it does | Prerequisite |
|---|---|---|
| `@ai-maturity-assistant` | **Guided concierge**: discovers the current state, asks what is missing, invokes skills, and leads you to the 5 PDFs (recommended the first time) | none |
| `/pipeline-completo` | **Everything at once**: 6 skills in order (auto-detects Excel + wizard) | `respostas.json` or `respostas-forms.xlsx` |
| `/importar-respostas-excel` | Converts the Microsoft Forms Excel → `respostas.json` (aggregates multiple respondents) | `respostas-forms.xlsx` |
| `/preencher-planilha` | Copies the xlsx template and fills in the levels | `respostas.json` |
| `/calcular-scores` | Applies SUMPRODUCT, generates `saida/scores.json` | `respostas.json` |
| `/gap-analysis` | Computes gaps + P0-P3 priority | `saida/scores.json` |
| `/recomendar-estrategias` | Maps gaps → S1-S7 + technologies | `saida/gaps.json` |
| `/wizard-implementacao` | **9-step wizard** to customize Part 4 of the PDF (steering committee, RACI, ADKAR, quick wins, and more) | none (independent) |
| `/gerar-relatorio` | **5 production-quality PDFs** via Jinja2 + WeasyPrint (identical to the platform) | the 3 above + optional wizard |

### Developer Survey (anonymous, behavioral)

| Command | What it does | Prerequisite |
|---|---|---|
| `/importar-survey-devs` | Converts `respostas-survey-devs.xlsx` (anonymous Forms) → `survey-devs/respostas-devs.json` (75 q × N respondents) | `respostas-survey-devs.xlsx` |
| `/insights-developer-survey` | **Aggregated report** + computed maturity (deterministic L0-L4 rubric across the 7 dimensions D2-D8) + gaps + recommendations linked to capabilities | `survey-devs/respostas-devs.json` |

### Learning & Growth Survey (identified, capacitation)

| Command | What it does | Prerequisite |
|---|---|---|
| `/importar-survey-learning` | Converts `respostas-survey-learning.xlsx` (identified Forms) → `survey-learning/respostas-learning.json` (32 q × N respondents with name+email) | `respostas-survey-learning.xlsx` |
| `/plano-capacitacao` | **Personalized capacitation plan**: top 10 topics with pre-validated attendees, cohorts per dimension D2-D8, Champions Network (3 tiers), mentor↔mentee pairs, 90-day calendar, prioritized barriers | `survey-learning/respostas-learning.json` |

---

## 📝 How to fill in `respostas.json`

```jsonc
{
  "metadata": {
    "respondent_name": "João Silva",
    "respondent_email": "joao@empresa.com",
    "respondent_role": "Engineering Manager",
    "audience": ["developer", "manager"],
    "organization": "Empresa Acme",
    "assessment_date": "2026-05-08",
    "language": "en"   // report language: "en" (default), "pt-BR", or "es"
  },
  "target_overrides": {
    // Optional: if you want a target different from the default 3.0 for a capability:
    "P3-C5": 4.0,   // aim for L4 in Agentic Applications
    "P2-C4": 3.5    // aim for L3+ in DevSecOps
  },
  "responses": {
    "P1-C1-Q1": {
      "level": 3,                                        // 0=L0 ... 4=L4 ... null=not answered
      "evidence": "Copilot Enterprise for 80% of devs, DORA metrics show +18% velocity.",
      "text_pt_br": "Em que medida sua organização utiliza..."  // read-only (canonical PT-BR wording)
    },
    // ... (157 more questions, identical format)
  }
}
```

### Filling tips

- **Not sure?** Leave `level: null`. The system ignores it (no penalty).
- **The more evidence, the better.** Text with tool + metric + period = "exemplary".
- **Minimum threshold: 25 answered questions** to leave BLOCKED. Ideally ≥ 40 (OK).
- **Multiple respondents:** prefer `respostas-forms.xlsx` or the Excel template in `coleta/`; the `/importar-respostas-excel` skill aggregates automatically using a simple mean per question.

### Visual alternative: use the HTMLs in `formularios/`
The HTMLs in [`formularios/`](formularios/) reproduce the platform's look. You can open them in the browser, read the rich context for each question (KPI, what/why, examples per level), and then fill in the JSON. Today there is **no automatic export** from the HTMLs to JSON, so fill in the JSON manually.

---

## 🔢 Scoring algorithm (5-line summary)

```
capability_score = Σ(level × question_weight) / Σ(question_weight)   # answered only
pillar_score     = Σ(cap_score × cap_weight) / Σ(cap_weight)         # caps in the pillar
overall_score    = Σ(cap_score × cap_weight) / Σ(cap_weight)         # ALL caps (not pillars)
gap_size         = max(0, target − current);  priority = weight × gap
threshold        = ≥40 OK · 25-39 WARNING · <25 BLOCKED
```

See `referencia/pontuacao-e-calculo.md` for the full formulas, edge cases, and 3 end-to-end examples.

---

## 🎨 The 7 strategies (S1-S7)

| ID | Name | When it appears in recommendations |
|---|---|---|
| S1 | GitHub Migration | Gaps in SCM/collaboration-related capabilities |
| S2 | Foundry + SRE | Gaps in observability, SLO, platform |
| S3 | App Modernization | Gaps in IaC, containers, cloud-native |
| S4 | AI Applications | Gaps in AI features / Azure OpenAI |
| S5 | GitHub Copilot Acceleration | Gaps in developer productivity |
| S6 | Agentic Activation | Gaps in agentic workflows |
| S7 | Security & Governance | Gaps in DevSecOps, supply chain |

The `/recomendar-estrategias` skill computes `cumulative_priority` per strategy (the sum of the `priority_score` of the gaps it addresses) and returns the ranked strategies with specific technologies and initial actions.

---

## ❓ Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| Copilot Chat does not show `/pipeline-completo` in the menu | Agent mode disabled | Switch to "Agent" in the chat dropdown |
| Custom skills do not appear | `.github/skills/` folder not detected | Reopen the workspace or run **Developer: Reload Window** |
| `respostas.json: Unexpected token` | Invalid JSON (extra comma, missing quotes) | Validate at jsonlint.com or run `python -m json.tool respostas.json` |
| Spreadsheet does not recalculate in Excel | Excel in "manual calculation" mode | Excel → Formulas → Calculate Now (F9) |
| `openpyxl` not installed | Missing Python dependency | `pip install openpyxl` |
| Threshold always BLOCKED | < 25 answered questions | Fill in 25+ more, spread across P1, P2, P3 |

---

## 🔁 Migration to the web platform (future)

When the web app is ready, migration is straightforward:

1. This kit's `respostas.json` follows **the same schema** that the platform API accepts (`POST /api/responses/bulk`).
2. The 5 skills become native app operations (buttons instead of `/` commands).
3. The reports in `saida/` remain as a historical archive; the app becomes the source of truth.

You do not lose data: just upload the JSON when the app is available.

---

## 📞 Support

- **Technical questions about the algorithm:** see `referencia/pontuacao-e-calculo.md`
- **Questions about a specific question:** see `referencia/P1-…md`, `P2-…md`, or `P3-…md`
- **Bugs in the kit:** open an issue in the main repo or contact Microsoft GBB

---

**Framework version:** 1.0.0 · **Kit date:** 2026-05-08 · **Language:** EN (primary; PT-BR in [README.pt-br.md](README.pt-br.md))

---

## Stuck on any of these steps?

<details>
<summary><strong>FAQ: common questions on first contact with the kit</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| I do not know which survey to run first | You have not decided the consulting scope yet | Use the agent: `@ai-maturity-assistant` presents the 4 paths (A/B/C/D) and helps you choose |
| `@ai-maturity-assistant` does not appear in chat | Copilot Chat is not in **Agent mode** | Click the dropdown next to the Copilot icon → choose **Agent** |
| Does `respostas.json.example` work as a real test? | Yes, it is Cliente Exemplo S.A. with 46 mocked answers | `cp respostas.json.example respostas.json` and run `/pipeline-completo` |
| Does Copilot Free work? | It works for skills, but with message limits | **Pro/Business/Enterprise** recommended for the full flow |
| Can I run without WeasyPrint? | Yes, but it will not generate PDFs | `make smoke` validates everything up to `payload.json` without needing WeasyPrint |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| _(you are at the hub)_ | **[Step-by-step guide](GUIA-PASSO-A-PASSO.md)** |
| You are already at the kit's main index. | Detailed installation, filling in, and execution, from zero to the executive PDF in 60-90 min. |

---

<sub>**Paula Silva** | Global Developer Solutions Advisor · [LinkedIn](https://linkedin.com/in/paulanunes)</sub>
<sub>Building the future of software development with AI and Agentic DevOps</sub>
<sub>Visual identity: [paulasilva-ms Design System v1.7.0](referencia/branding/) · Microsoft 4-color palette applied to the interactive HTMLs and the 5 production-quality PDFs</sub>
