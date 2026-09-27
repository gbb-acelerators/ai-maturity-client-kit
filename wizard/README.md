# `wizard/`: Implementation Guide Wizard (PDF Part 4)

🌐 English · [Português (Brasil)](README.pt-br.md)

**`🧙 WIZARD`** · _Custom Part 4_ · 📖 [🏠 Index](../README.md) · [« Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md) · You are here

This folder offers **3 ways** to fill in the 9 structured inputs that populate **Part 4 of `roadmap_part4.pdf`** (the consolidated Implementation Guide: committees, RACI, ADKAR, quick wins, and more). It mirrors the React wizard of the web platform (`app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`).

> [!NOTE]
> **Output in every mode:** `implementation-guide-inputs.json` at the **root of kit-cliente/** (not in this folder). The `/gerar-relatorio` skill detects it automatically and merges it into the payload.

## The 9 inputs

| # | Input | What it is |
|---|---|---|
| 1 | **Steering Committee** | 5-8 names: Sponsor, Program Lead, CFO, CISO, Change Champion |
| 2 | **TPO** (Technology Product Owner) | Program Manager + office (3-5 people) + decision authority |
| 3 | **RACI Matrix** | 5-8 activities × R/A/C/I |
| 4 | **Communication Plan** | Audience × channel × frequency × owner |
| 5 | **Training Plan** | Cohort × format × cadence × criteria |
| 6 | **ADKAR** | Awareness · Desire · Knowledge · Ability · Reinforcement |
| 7 | **Quick Wins W1-4** | 4-6 initiatives for the first month |
| 8 | **Quick Wins W5-8** | Second wave |
| 9 | **Quick Wins W9-12** | Third wave |

## The 3 modes

### A. Standalone HTML wizard (recommended for a visual flow)

```bash
open wizard/implementation-guide-wizard.html
```

- The browser opens a page with 9 steps (each with helper text and a large textarea)
- Saves automatically to `localStorage`, so you can pause and come back later
- The stepper at the top shows progress (green ✓ when filled in)
- At the end: click **💾 Download JSON** and move `implementation-guide-inputs.json` to the root

A Portuguese (Brazil) UI ships in the PT-BR package under the same file name (in the repository it is `implementation-guide-wizard.pt-br.html`).

**Time:** 30-60 min to fill in all 9 in detail (15 min for a draft).

### B. Editable JSON template (recommended for developers)

```bash
cp wizard/implementation-guide-inputs.template.json implementation-guide-inputs.json
code implementation-guide-inputs.json
```

The template has rich placeholders with inline instructions (`_help`, `_dicas`, examples per field). Delete the examples and replace them with your own data.

### C. Conversation in Copilot Chat (recommended for a collaborative draft)

In Copilot Chat (Agent mode):

```
/wizard-implementacao
```

Select mode **C** when Copilot asks. It will:
1. Ask 9 questions, one at a time
2. Let you answer in free text
3. At the end, build the JSON and ask you to confirm before saving

## Files

| File | Size | Purpose |
|---|---|---|
| **[implementation-guide-wizard.html](implementation-guide-wizard.html)** | ~22 KB | Mode A: standalone visual wizard (Tailwind + JavaScript, saves to localStorage) |
| `implementation-guide-wizard.pt-br.html` (repository only; the PT-BR package ships it as `implementation-guide-wizard.html`) | ~22 KB | Mode A, Portuguese (Brazil) UI |
| **[implementation-guide-inputs.template.json](implementation-guide-inputs.template.json)** | ~12 KB | Mode B: JSON template with the 9 fields prefilled with instructions and examples |

## After filling in

```bash
# Check that the JSON is at the kit root
ls implementation-guide-inputs.json

# Re-render the PDFs with the custom Part 4
/gerar-relatorio                 # via Copilot Chat
# or
python3 relatorios/scripts/build_payload_and_render.py   # via CLI
```

## Skipping and reuse

- Skipping is fine: `/gerar-relatorio` uses professional placeholders from `sample_payload.json` (with names from "Acme Insurance Group"). The client can run the wizard later and regenerate at any time.
- You can fill in only some of the 9 inputs; empty fields keep their placeholders.
- Rerunning the wizard overwrites only the fields you fill in again.

## Related documentation

- Orchestrating skill → [`../.github/skills/wizard-implementacao/SKILL.md`](../.github/skills/wizard-implementacao/SKILL.md)
- Original wizard (React/TS) that this mirrors → `app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`
- How the JSON reaches the PDF → [`../relatorios/templates/roadmap_part4.html.j2`](../relatorios/templates/roadmap_part4.html.j2) (search for `wiz.`)

---

## Stuck on one of these steps?

<details>
<summary><strong>FAQ: common Wizard questions</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| `implementation-guide-inputs.json` does not show up in the PDF | The file is in `wizard/` instead of the root | Move it to the kit **root** (same folder as `respostas.json`) |
| Mode D (auto-fill) fails | You have not run `/plano-capacitacao` yet | Run the Learning Survey first; it generates the input for mode D |
| The HTML wizard does not save progress | `localStorage` disabled / private browsing | Open a normal window or use mode B (edit the JSON) |
| Do I need to fill in all 9 inputs? | No, mode D fills in 6 of them automatically | You fill in only **TPO** and **RACI Matrix** manually |
| The generated PDF has generic placeholders | You skipped the wizard | Rerun `/wizard-implementacao` → `/gerar-relatorio` |
| Can I edit the JSON after generating? | Yes, and re-render | Edit `implementation-guide-inputs.json` → `make pipeline` |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Learning & Growth Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)** | **[🏠 Kit index](../README.md)** 🎉 |
| 32 identified questions: personalized capacitation plan. | You have completed the flow. Go back to the hub to revisit any step. |

↑ [Back to the kit index](../README.md)
