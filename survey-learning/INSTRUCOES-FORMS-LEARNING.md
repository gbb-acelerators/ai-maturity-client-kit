# How to build the Microsoft Forms for the Learning & Growth Survey

🌐 English · [Português (Brasil)](INSTRUCOES-FORMS-LEARNING.pt-br.md)

**`🅲️ SURVEY-LEARNING`** · _identified_ · 📖 [🏠 Index](../README.md) · [« Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md) · You are here · [» Wizard](../wizard/README.md)

> [!WARNING]
> Unlike the other 2 surveys, this one is **IDENTIFIED** (name + email required). It has 32 questions in 7 sections to build the team's **personalized capacitation roadmap**: workshops, cohorts, Champions Network, and mentoring. Estimated time per developer: **5-8 min**.

**Different from the other 2 surveys:**
- Main assessment: organizational maturity (Likert L0-L4 declared by leadership)
- Developer Survey: ANONYMOUS real behavior
- **This Learning Survey: IDENTIFIED capacitation roadmap**: it needs name+email to invite the right people to the right workshops

---

## ⚠️ Why IDENTIFIED (not anonymous)?

To produce actionable value, this survey **needs to know who is who**:
- Invite **the right people** to each workshop (10 pre-validated attendees is better than "70% showed interest")
- Build a **Champions Network** with names (not anonymous)
- Map **mentor↔mentee pairs** (needs names on both sides)
- Assign an **owner** to the identified quick wins

**Honest trade-off:** some questions (e.g., "what is your level in D8 Security?") may be answered less honestly if developers feel judged. That is why:
- Leadership must **communicate clearly**: "answers are used to BUILD SKILLS, not to EVALUATE performance"
- Do not use answers in performance reviews
- Share the consolidated plan with the whole team (transparency)

If your organization prefers **pure anonymity**: run the **Developer Survey** (`survey-devs/`) in parallel and use the deterministic rubric as an "objective thermometer".

---

## 📋 The 7 topics covered

| # | Section | Focus | Q |
|---|---|---|---|
| **L1** | Identification | Name, email, role, team | 4 |
| **L2** | Self-perceived maturity | L0-L4 self-assessment in the 7 dimensions D2-D8 | 7 |
| **L3** | Where you want to grow | Top 3 priority dimensions (next 6 months) + why | 2 |
| **L4** | Specific topics | Copilot, Foundry, practices (TDD/SDD), agents, security (checkbox) | 5 |
| **L5** | Format and cadence | Hands-on workshop, cohort, self-paced, time slots, hours/week | 4 |
| **L6** | Champions and mentoring | Want to be a Champion? Mentoring? Who is a reference? | 5 |
| **L7** | Barriers and Wishlist | What gets in the way + desired workshops + speakers | 5 |
| | | **TOTAL** | **32** |

---

## 🛠️ How to build the Forms (step by step)

### Step 1 · Create the form

1. Go to <https://forms.office.com> → **+ New Form**
2. Title: `AI Learning & Growth: What do you want to learn in the next 6 months?`
3. Subtitle (paste):

```
5-8 min survey about your AI capacitation plan.

⚠️ IDENTIFIED: we will use your name+email to INVITE you to the right
workshops/cohorts. Individual answers will NOT be shared publicly,
only aggregated insights + attendee lists per workshop.

Result: personalized capacitation plan + cohorts + Champions Network.
```

### Step 2 · ⚠️ CONFIGURE as IDENTIFIED (not anonymous)

**Settings (⚙️):**

| Setting | Value |
|---|---|
| **Anonymous responses** | ☐ **UNCHECKED** (we want identification) |
| **Who can respond** | "Only people in my organization" (recommended) |
| **One response per person** | ☑ CHECKED (1 per developer) |
| **Accept responses** | ☑ CHECKED |
| **Customize thank you message** | "Thank you! You will receive workshop invitations based on your answers." |

> 🔍 **Different from the Developer Survey** (`survey-devs/INSTRUCOES-FORMS-DEVS.md`): there you turn Anonymous ON; here you leave it OFF.

### Step 3 · Create 7 sections

```
Section 1: L1 - Identification                 (4 questions)
Section 2: L2 - Self-perception (D2-D8)        (7 questions)
Section 3: L3 - Where you want to grow         (2 questions)
Section 4: L4 - Specific topics                (5 questions)
Section 5: L5 - Format and cadence             (4 questions)
Section 6: L6 - Champions and mentoring        (5 questions)
Section 7: L7 - Barriers and Wishlist          (5 questions)
```

### Step 4 · Add the 32 questions

Use the English bank [`perguntas-para-forms-learning.en.md`](perguntas-para-forms-learning.en.md) as the copy/paste source. The canonical question bank is the PT-BR version, [`perguntas-para-forms-learning.md`](perguntas-para-forms-learning.md); use it if your respondents answer in Portuguese.

**For each question:**

1. Type:
   - `choice` (Single answer) → **Choice**
   - `multi` (Multiple answers) → **Choice** with Multiple answers CHECKED
   - `text-short` (Short Text, 1 line) → **Short answer**
   - `text` (Long Text) → **Long answer**

2. **The TITLE ALWAYS starts with the ID + colon**:
   ```
   L4-Q1: Which GitHub Copilot topics do you want to master?
   ```

3. **Required**: mark **L1-Q1 (name) + L1-Q2 (email)** as required. Leave the rest optional (developers can skip them).

### Step 5 · Customize L1-Q4 (squad list)

Question L1-Q4 ("Team / Squad") has a placeholder (`[Customize with the organization's team list]` in the English bank, `[Lista a customizar pela org]` in the PT-BR bank). Replace it with the real squad names in your organization. Example:

```
- Payments Squad
- Onboarding Squad
- Platform Squad
- SRE Core
- Data Platform
- Other / I do not belong to a fixed squad
```

### Step 6 · Share

1. **+ Send / Collect responses** → **Link**
2. Share with **ALL developers**:
   - Email from the engineering leader: "Over the next 2 weeks, we want to hear what you want to learn about AI: a 5-8 min IDENTIFIED survey. Result: a personalized capacitation plan."
   - Slack/Teams channel #engineering
   - All-hands (present the link)

3. **Deadline:** 2 weeks. Reminders on D+7 and D+12.

### Step 7 · Track responses

- The **Responses** tab shows the count in real time
- Recommended: **at least 5 developers**, ideally **>50% of the team**
- Because it is identified, you can see "X of Y developers have not answered yet" and follow up 1-on-1

### Step 8 · Export

1. **Responses → Open in Excel**
2. Save as **`respostas-survey-learning.xlsx`**
3. Move to the **root of `kit-cliente/`**
4. Check: columns D (Email) and E (Name) must be FILLED IN

### Step 9 · Analyze with the kit

In Copilot Chat (Agent mode):

```
/importar-survey-learning
```

Generates `survey-learning/respostas-learning.json` (structured).

```
/plano-capacitacao
```

Generates `saida/plano-capacitacao-<DATE>.md` (in **English by default**; the script accepts `--lang pt-br` for Portuguese (Brazil)) with:
- Top 10 requested topics (with a list of pre-validated attendees)
- Suggested cohorts per dimension D2-D8
- Identified Champions Network (3 tiers)
- Mentor ↔ mentee pairs
- Workshop calendar (next 90 days)
- Prioritized barriers
- 5 prioritized actions (impact × ease)
- Connection with /insights-developer-survey + /calcular-scores

### Step 10 · ⭐ Wizard auto-fill (Mode D)

After generating the plan, running `/wizard-implementacao` makes the Copilot Agent **automatically detect** `saida/plano-capacitacao-*.md` and offer **Mode D: Auto-fill**, which fills **6 of the 9** wizard inputs automatically:

| Wizard input (Part 4 of the PDF) | Comes from |
|---|---|
| `executive_steering_committee` | Champions Network "active" |
| `communication_plan` | Workshop calendar |
| `training_plan` | Cohorts per dimension |
| `adkar_notes` | Top 5 workshops (Knowledge stage) |
| `quick_wins_w1_4` / `quick_wins_w5_8` / `quick_wins_w9_12` | 90-day calendar |

You only need to fill in manually: **TPO** + **RACI Matrix** (which the learning survey does not cover).

**Estimated savings:** 30-45 min of manual wizard work. And the data is REAL data from your team, not placeholders from the sample.

### Step 11 · Re-render the PDFs with the plan + wizard auto-fill

```
/gerar-relatorio
```

The skill detects:
- ✅ `implementation-guide-inputs.json` (from wizard Mode D auto-fill) → populates Part 4 with your Champions and workshops
- ✅ `saida/plano-capacitacao-*.md` (from this survey) → enriches roadmap_part4.pdf
- ✅ `saida/insights-developer-survey-*.md` (if you ran it) → cross-references in the appendix
- ✅ `saida/maturidade-developer-survey-*.json` (if you ran it) → score_justification.pdf includes "maturity vs declared"

**Output:** 5 production-quality PDFs with REAL learning survey data embedded.

---

## 🅱️ Alternative path: Excel/SharePoint directly

For small teams (3-5 developers):

```bash
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx
# Clear the mock rows (rows 2-6)
# Upload to SharePoint with edit permission
# Each developer fills in one row (including name+email)
# Download and move to the root
/importar-survey-learning + /plano-capacitacao
```

---

## 💡 Best practices

### Commitment to ethical use of the data
Communicate before launching:

> "Your answers will be used to: (1) build our capacitation roadmap, (2) invite you to the specific workshops you asked for, and (3) build the Champions Network. They will **NOT** be used for performance review, comparison between developers, or shared with external clients."

### Privacy and data protection (LGPD / GDPR)

This survey processes personal data (name, email, role, squad, self-assessment). Agree on the points below with your privacy or legal team before launch; this checklist is not legal advice.

- **Purpose and legal basis:** document why the data is collected (training plan, invitations, Champions Network) and the legal basis your team chooses.
- **Privacy notice:** include the notice from `perguntas-para-forms-learning.en.md` (step 3) in the form, with controller, access, retention, and contact filled in.
- **Minimization:** collect only the identification questions in L1; do not add fields such as employee ID or manager.
- **Storage and access:** keep `respostas-survey-learning.xlsx`, `survey-learning/respostas-learning.json`, and `saida/plano-capacitacao-*.md` on managed storage with restricted access. These paths are in `.gitignore`; never commit them.
- **Leadership-only appendix:** the plan's respondent appendix contains names and emails. Share it only with the people who send invitations.
- **Retention and deletion:** delete the Forms responses, the `.xlsx`, the JSON, and the plan appendix when the retention period ends.
- **Individual requests:** name an owner for access, correction, and deletion requests.

### Relaunch cadence
- **Every 6 months** or after major events (Copilot rollout, stack change, etc.)
- **Compare evolution**: a developer who was L1 in D5 now self-rates L3? A natural Champion

### Plan transparency
- Present `plano-capacitacao-DATE.md` at an all-hands
- People who asked for workshop X receive an invitation: close the loop
- Identified Champions are recognized publicly (with consent)

---

## 🆘 Troubleshooting

| Problem | Solution |
|---|---|
| Skill does not detect the file | Move it to the root of `kit-cliente/` |
| Email/Name empty in some rows | Forms config: Anonymous OFF + L1-Q1/Q2 required |
| Headers not recognized | Make sure each question starts with `L[1-7]-Q\d+:` |
| Developer refused to identify | Accept the partial answer; redirect to `survey-devs` (anonymous) |
| Low participation (< 50% of the team) | The engineering leader must ENDORSE it explicitly |

---

## 📚 References

- **The 32 formatted questions (English):** [`perguntas-para-forms-learning.en.md`](perguntas-para-forms-learning.en.md) (canonical PT-BR bank: [`perguntas-para-forms-learning.md`](perguntas-para-forms-learning.md))
- **Ready Excel template:** [`template-export-forms-learning.xlsx`](template-export-forms-learning.xlsx)
- **Sample structured JSON:** [`respostas-mock-learning.json`](respostas-mock-learning.json)
- **Import skill:** [`../.github/skills/importar-survey-learning/SKILL.md`](../.github/skills/importar-survey-learning/SKILL.md)
- **Plan skill:** [`../.github/skills/plano-capacitacao/SKILL.md`](../.github/skills/plano-capacitacao/SKILL.md)
- **Cross-reference with the Developer Survey** (anonymous): [`../survey-devs/`](../survey-devs/)

---

**Version:** 1.0 · **Date:** 2026-05-08

---

## Stuck on one of these steps?

<details>
<summary><strong>FAQ: common questions about the Learning & Growth Survey (identified)</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| Excel arrives without name/email | **Anonymous responses** is checked (this survey must be identified) | Forms Settings → ❌ UNcheck **Anonymous responses** |
| How do I use the plan to invite people? | The plan lists name+email per workshop | Copy the attendee list from the Markdown → paste into an Outlook/Teams meeting invite |
| Champions Network is empty in the generated plan | Nobody answered "yes" in L6-Q1 | No self-declared Champions: use the per-dimension ranking as a proxy |
| Cohorts are empty in some dimensions | Fewer than 3 respondents per dimension | Ask for more participation or accept smaller cohorts |
| Can I rerun the plan if more answers arrive? | Yes, it is idempotent | Re-export Excel → `/importar-survey-learning` → `/plano-capacitacao` |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Developer Survey (anonymous)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** | **[Wizard: Part 4](../wizard/README.md)** |
| 75 anonymous questions: Copilot, agents, governance. | Customize the Steering Committee, RACI, ADKAR, and Quick Wins of the executive PDF. |

↑ [Back to the kit Index](../README.md)
