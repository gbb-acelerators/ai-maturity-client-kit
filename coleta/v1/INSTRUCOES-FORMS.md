# How to create the Microsoft Forms for the AI Maturity Assessment

🌐 English · [Português (Brasil)](INSTRUCOES-FORMS.pt-br.md)

**`🅰️ ASSESSMENT`** · 📖 [🏠 Index](../README.md) · [« Step-by-step guide](../GUIA-PASSO-A-PASSO.md) · You are here · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md)

> [!TIP]
> This guide shows **3 paths** to create and use Microsoft Forms with the 158 questions. Choose the one that best fits the available time and the team's technical profile.

---

## ⚖️ Quick comparison of the 3 paths

| Path | Setup time | Effort | When to use |
|---|---|---|---|
| **A. Full manual Forms** | 4-6 hours | High (create 158 questions) | You want a 100% native Forms experience, with sections and branding |
| **B. Lean Forms (1 pilot capability)** | 30 minutes | Low | PoC or validation with few respondents before scaling |
| **C. Directly in Excel/SharePoint** ⭐ | 5 minutes | Minimal | **Recommended**: uses the Excel template that ships with the kit and avoids 4h of setup |

---

## 🅰️ Path A: Full manual Forms (158 questions)

### Step 1 · Create the Forms

1. Go to https://forms.office.com (sign in with your Microsoft 365 account)
2. Click **+ New Form**
3. Title: `AI Maturity Assessment - <Your organization name>`
4. Subtitle (optional):
   ```
   AI maturity assessment across 3 pillars: Productivity, DevOps, and Platform.
   158 questions on an L0-L4 scale. Estimated time: 45-90 minutes.
   Your answers are confidential and used only to generate the roadmap.
   ```

### Step 2 · Configure 3 sections

Add 3 sections (button **+ Add new** → section icon):

| Section | Title | Suggested subtitle |
|---|---|---|
| 1 | **Pillar P1: Developer Productivity** | 53 questions in 9 capabilities |
| 2 | **Pillar P2: DevOps Lifecycle** | 59 questions in 10 capabilities |
| 3 | **Pillar P3: Application Platform** | 46 questions in 9 capabilities |

### Step 3 · Add the 158 questions

For each question, add **2 elements** to the Forms:

1. **Choice (single answer)** with the question + the 6 level options
2. **Long Text** (optional) for evidence

Use [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md) as the copy/paste source: it has the 158 questions formatted with IDs (`P1-C1-Q1`, etc.) and the full text, with English labels. The canonical PT-BR bank is [`perguntas-para-forms.md`](perguntas-para-forms.md); the question wording is identical in both.

#### Fixed options for ALL questions (paste them identically)

```
L0 — Initial — No established practice
L1 — Developing — Isolated pilots (<25%)
L2 — Defined — 25-50% coverage with guidelines
L3 — Managed — >75% with impact metrics
L4 — Optimizing — Universal (>95%) with continuous automation
NA — I do not know / Not applicable
```

> ⚠️ **CRITICAL:** the `L0`, `L1`, ..., `L4`, `NA` prefix must appear **literally at the start** of each option. The import skill uses this prefix to map back to the number (0-4 or null). Do not translate or reformat it.

#### Title format for each question

```
P1-C1-Q1: <question text>
```

> ⚠️ **IMPORTANT:** the ID (`P1-C1-Q1`) must appear **literally at the start** of the question title, followed by `:`. Example from [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md) (canonical wording kept in Portuguese):
>
> `P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?`
>
> (English gloss: "To what extent does your organization use AI code completion tools, e.g. GitHub Copilot?")

#### Evidence field format

```
Evidência (P1-C1-Q1)
```

Type: **Long Text**, optional (do not mark it as required). Keep the label exactly as shown, in Portuguese: the import skill matches the `Evidência (` prefix.

### Step 4 · Configure permissions

1. **Settings** button (gear) in the top-right corner
2. **Who can fill out this form**:
   - **Only people in my organization**: recommended for internal use
   - **Anyone with the link**: for cross-company use (consulting)
3. **One response per person**: disabled (we want multiple responses to aggregate)
4. **Email notification of each response**: optional

### Step 5 · Share

1. **Send/Collect responses** button
2. Copy the link
3. Share it with the team via Email/Teams/SharePoint

### Step 6 · Export responses

When you have enough responses (recommended: ≥3 respondents to reduce bias):

1. **Responses** tab
2. **Open in Excel** button
3. Save the file as **`respostas-forms.xlsx`**
4. Move it to the root of `kit-cliente/`

### Step 7 · Import into the kit

In VS Code, open Copilot Chat (**Agent** mode) and type:

```
/importar-respostas-excel
```

The skill:
- Detects `respostas-forms.xlsx` automatically
- Backs up the current `respostas.json`
- Aggregates multiple respondents via the mean per question
- Overwrites `respostas.json`
- Generates `saida/import-log-<DATE>.md`

Then run `/pipeline-completo` as usual.

---

## 🅱️ Path B: Lean Forms (1 pilot capability)

To **validate the end-to-end flow** before investing in the full setup.

### Step 1 · Choose 1 capability

Choose 1 capability with 5-7 questions. Suggestion: **P1-C1 (AI Coding Assistants)**. It is the "hottest" topic and will spark good discussion on the team.

### Step 2 · Create the Forms with only those 5 questions

Same process as Path A, but with only **5 questions** instead of 158. Time: 15-30 min.

### Step 3 · Collect 3-5 responses

Share it with your immediate team (not the whole company). Time: 1-2 days.

### Step 4 · Import and run

Since `respostas.json` will have only 5 answered questions, the **threshold will stay at BLOCKED** (it needs ≥25). But:
- You validate that the Forms → Excel → respostas.json flow works
- You see how a capability with real data appears in the report

To generate a useful report, complete the rest manually via `respostas.json` or expand the Forms.

---

## 🅲 Path C: Directly in Excel/SharePoint ⭐ (RECOMMENDED)

Skips Forms and uses the **Excel template** that ships with the kit.

### Step 1 · Get the template

The kit ships with [`coleta/template-export-forms.xlsx`](template-export-forms.xlsx). This file:
- Has the **same format** that Forms would export
- Already has the 158 question columns + 158 evidence columns
- Comes with **3 mocked respondents** as an example (you can delete and replace them)

### Step 2 · Upload to SharePoint/OneDrive

1. Clear the 3 mocked respondent rows (rows 2, 3, 4) and keep only the header
2. Rename it: `respostas-forms.xlsx` (or another name)
3. **SharePoint:** upload it to the project library and generate an "Anyone with the link can edit" link
4. **OneDrive:** upload it and share with edit rights
5. **Teams:** attach it to the channel and pin it

### Step 3 · Each respondent fills in one row

Share these instructions:

```
Hi team!

Please fill in ONE row per person in this file:
<SharePoint link>

For each of the 158 question columns:
- Select a level L0-L4 (or leave it blank if you "do not know")
- The text must start with the code (e.g. "L3")
- Use the Evidence column right next to it to describe tool/coverage/metric

Estimated time: 45-90 min. You can pause and come back.

Questions? See the documents in referencia/P*.md (in kit-cliente).
```

### Step 4 · Download the Excel

When everyone has filled it in:
1. SharePoint → file → **Download a Copy**
2. Rename it to **`respostas-forms.xlsx`**
3. Move it to the root of `kit-cliente/`

### Step 5 · Import and run

```
/importar-respostas-excel
/pipeline-completo
```

---

## 🆚 Forms vs. direct Excel: which one to choose?

| Criterion | Microsoft Forms | Excel/SharePoint |
|---|---|---|
| **Setup time** | 4-6h (create 158 questions) | 5 min (ready-made template) |
| **Respondent UX** | Mobile-friendly, 1 question at a time | Spreadsheet (intimidating for non-technical people) |
| **Data validation** | Fixed (Choice = only 6 options) | Fragile (people can type anything) |
| **Multiple respondents** | Native | Manual (1 row per person) |
| **Later editing** | Hard (each submission is final) | Easy (anyone can change it at any time) |
| **Audit trail** | Native (timestamp per submission) | SharePoint version history |
| **License cost** | Standard Microsoft 365 | Standard Microsoft 365 |
| **Kit integration** | Identical (`/importar-respostas-excel`) | Identical |

**Practical recommendation:**
- **PoC / small team (3-5 people):** direct Excel (Path C)
- **Organization roll-out (10+ respondents):** Forms (Path A)
- **Demanding client / professional branding:** Forms (Path A)

---

## 🔄 Other formats supported by the skill

The `/importar-respostas-excel` skill accepts any Excel/CSV whose question headers start with `P[1-3]-C\d+-Q\d+:`. This includes:

- ✅ **Microsoft Forms** export (official format)
- ✅ **Google Forms** export (Sheets → Download as .xlsx)
- ✅ Custom **Excel/SharePoint** (the kit template or your own)
- ✅ **CSV** (if you rename it to .xlsx or convert it)
- ⚠️ **Typeform**: works if you adjust the headers to include the IDs

---

## 💡 Practical tips

### Tip 1 · Start with 1 pillar
Do not try to collect answers for all 3 pillars at the same time. Start with P1 (Productivity), which is the most tangible for devs. Then P2 (DevOps) with SREs. Then P3 (Platform) with architects.

### Tip 2 · Pre-fill through interviews
Instead of sending the link and waiting, run a **1-hour interview per respondent** and fill it in together. You capture nuances better and generate richer evidence.

### Tip 3 · Train before launching
Run a **30-min kick-off** explaining:
- What the assessment is
- How L0-L4 are defined
- Why evidence matters
- How long it will take
- When they will receive the report

### Tip 4 · Run short cycles
Do not wait for 100% of the answers to run `/pipeline-completo`. Run it with 25 (WARNING), then 50 (OK), then 100. With each cycle, the report improves and you capture more conversations.

### Tip 5 · Versioning
Every time you import, the skill creates `respostas.json.backup-<timestamp>`. Keep these backups: they are your **evolution history** between assessment rounds.

---

## 🆘 Troubleshooting

| Problem | Diagnosis | Solution |
|---|---|---|
| Skill does not detect `respostas-forms.xlsx` | File is not at the root | Move it to `kit-cliente/respostas-forms.xlsx` (not into coleta/) |
| "No recognized header" | Excel headers do not start with `P1-C1-Q1:` etc. | Edit the headers manually to include the IDs at the start |
| A respondent appears twice | Forms allows multiple submissions from the same person | Edit the Excel manually to delete the duplicate row before importing |
| Levels turned into text | Forms exported the option WITHOUT the `L0/L1/...` prefix | Rebuild the Forms including the prefixes at the start of each Choice option |
| Excel has 158 columns but only 90 questions are recognized | Headers truncated by Forms (4000-character limit) | Shorten the question text in Forms (keep only the ID + a short summary sentence) |

---

## 📚 References

- **Full list of the 158 questions formatted for Forms:** [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md) (English labels) · canonical PT-BR: [`perguntas-para-forms.md`](perguntas-para-forms.md)
- **Ready-made Excel template (3 mocked respondents):** [`template-export-forms.xlsx`](template-export-forms.xlsx)
- **Import skill:** [`../.github/skills/importar-respostas-excel/SKILL.md`](../.github/skills/importar-respostas-excel/SKILL.md)
- **Multi-respondent aggregation algorithm:** [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md) section 6

---

**Version:** 1.0 · **Date:** 2026-05-08

---

## Stuck on any of these steps?

<details>
<summary><strong>FAQ: common questions about collecting via Forms</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| **Open in Excel** is disabled in Forms | Your account has no M365 license / Forms is in a personal account | Ask an admin to move the Forms to the organizational account |
| I have multiple respondents: how do I aggregate them? | Default skill behavior | `/importar-respostas-excel` computes an **automatic mean** per question |
| The column headers do not start with `P1-C1-Q1:` | You did not follow the pattern when creating the Forms | Edit the question titles in Forms to include the ID at the start |
| Sharing the Forms with people outside the org | Forms settings restrict access | Settings → **Anyone with the link can respond** |
| Excel arrives with extra columns (ID, Start time, ...) | Default Forms behavior | The skill ignores columns A-E automatically |
| `respostas-forms.xlsx` is not detected | The file is inside `coleta/` instead of the root | Move it to the kit **root** |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Step-by-step guide](../GUIA-PASSO-A-PASSO.md)** | **[Developer Survey (anonymous)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** |
| From zero to the executive PDF in 60-90 min. | 75 anonymous questions about Copilot, agents, governance, MCP / A2A. |

↑ [Back to the kit Index](../README.md)
