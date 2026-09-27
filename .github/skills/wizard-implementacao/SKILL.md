---
name: wizard-implementacao
description: Guides the client through the 9-step Implementation Guide Wizard (steering committee, TPO, RACI, comms plan, training plan, ADKAR, 3 quick-wins waves) by either pointing to the standalone HTML wizard OR conducting the conversation in chat. Output is implementation-guide-inputs.json that feeds Roadmap Part 4 PDF. Use when the user asks for "wizard", "implementation guide", "guia de implementação", "preencher parte 4", "TPO", "steering committee", "RACI", "ADKAR", "quick wins", "fill Part 4", "implementation wizard".
argument-hint: "optional \"chat\" to force conversation mode (default: offer both options)"
---

# Skill: Implementation Guide Wizard

## What this is

The platform's Implementation Guide Wizard (`app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`) collects 9 structured inputs that feed **Part 4 of the PDF report** (Implementation Guide consolidated). This kit provides **4 ways** to fill the same 9 inputs (mode D is automatic from Learning Survey):

| Mode | Best for | UX |
|---|---|---|
| **A. HTML wizard** (`wizard/implementation-guide-wizard.html`) | Visual users | Browser, step-by-step, saves localStorage, exports JSON |
| **B. JSON template** (`wizard/implementation-guide-inputs.template.json`) | Devs / power users | Direct edit in VS Code |
| **C. Chat conversation** (this skill in chat mode) | Quick draft / iteration | Copilot conducts 9 questions in chat |
| **D. Auto-fill from Learning Survey** ⭐ | When `/plano-capacitacao` already ran | Auto-extract from `saida/plano-capacitacao-<DATE>.md` |

All four produce the same artifact: **`implementation-guide-inputs.json`** at the workspace root.

## ⭐ Mode D — Auto-fill from Learning Survey output (REAL implementation)

**Implementation:** invoke the official script that parses `saida/plano-capacitacao-<DATE>.md` and generates `implementation-guide-inputs.json` with 6 of 9 fields auto-filled:

```bash
python3 wizard/scripts/auto_fill_from_plano.py
# Auto-detects latest plano-capacitacao-*.md in saida/ (English or Portuguese plan)
# Output: implementation-guide-inputs.json at root (67% complete, 6/9 fields)

# Portuguese text in the generated fields:
python3 wizard/scripts/auto_fill_from_plano.py --lang pt-br
```

**What it auto-fills (6 of 9):**
- `executive_steering_committee` ← active Champions (section 4 of the plan)
- `communication_plan` ← suggested calendar (section 5)
- `training_plan` ← cohorts by dimension (section 3)
- `adkar_notes` ← Knowledge stage uses the plan's Top 5 workshops
- `quick_wins_w1_4` / `w5_8` / `w9_12` ← 90-day calendar

**What user MUST fill manually (Learning Survey doesn't cover):**
- `tpo` (Technology Product Owner)
- `raci_matrix`

After running auto_fill, the user can edit `implementation-guide-inputs.json` to fill the 2 missing fields, then run `/gerar-relatorio` to render PDFs with personalized Part 4.



If `saida/plano-capacitacao-<DATE>.md` exists (output of `/plano-capacitacao`), the data ALREADY contains:

| Wizard input | Data in plano-capacitacao (EN heading / PT-BR heading) |
|---|---|
| `executive_steering_committee` | Champions Network "Active" / "Ativos" (3-5 people with name+email) |
| `tpo` | (not in learning survey; keep manual or sample) |
| `raci_matrix` | (not in learning survey; keep manual or sample) |
| `communication_plan` | "Suggested calendar" / "Calendário sugerido" (audience, channel, and cadence) |
| `training_plan` | "Suggested cohorts by rubric dimension" / "Cohorts sugeridos por dimensão" (audience × format × cadence × Champion) |
| `adkar_notes` | Top 5 recommendations from learning survey (Knowledge stage = top 5 workshops) |
| `quick_wins_w1_4` | First 4 weeks of the suggested calendar |
| `quick_wins_w5_8` | Weeks 5-8 |
| `quick_wins_w9_12` | Weeks 9-12 + barrier removal actions |

**How to invoke Mode D:**

When user runs `/wizard-implementacao` and `saida/plano-capacitacao-*.md` exists, OFFER as first option:

```
🎓 Found saida/plano-capacitacao-2026-05-08.md (from the Learning Survey).
   I can EXTRACT automatically: Champions, training_plan, calendar, and quick wins.
   You only need to fill in: TPO + RACI Matrix (the learning survey does not cover them).

   [a] Auto-fill (Mode D, recommended: fills 6 of the 9 inputs)
   [b] HTML / JSON / Chat mode (fill everything manually)
```

## When to use this skill
- Client asked about "wizard" / "implementation guide" / "Part 4" / "guia de implementação"
- Before `/gerar-relatorio` if `implementation-guide-inputs.json` doesn't exist yet (or is incomplete)
- When client wants to iterate on the implementation plan without re-rendering everything

## Procedure

### Step 1: choose the best mode

Before showing manual modes, check if a latest `saida/plano-capacitacao-*.md` exists.

- If it exists, offer **Mode D** first and recommend it.
- If it does not exist, offer modes A/B/C.

Mode D is the default recommendation after `/plano-capacitacao` because it fills 6 of 9 fields automatically and leaves only `tpo` and `raci_matrix` for manual completion.

### Default behavior without Learning Survey output

When invoked without arguments, present the 3 options and let the user choose. Reply in English by default, or in the user's language:

```
🧙 Implementation Guide Wizard: 9 inputs feed Part 4 of the PDF

How would you like to fill it in?

  📋 [A] Visual mode (standalone HTML)
       Open wizard/implementation-guide-wizard.html in the browser.
       9 steps, saves to localStorage, exports JSON at the end.
       👉 Best for: the same visual experience as the web app.

  📝 [B] Direct mode (edit JSON in VS Code)
       Copy wizard/implementation-guide-inputs.template.json to
       the kit root, rename it to implementation-guide-inputs.json,
       and fill in each field.
       👉 Best for: developers who prefer code.

  💬 [C] Conversation mode (I guide you here in chat)
       I ask the 9 questions one by one. Answer freely.
       At the end I save implementation-guide-inputs.json automatically.
       👉 Best for: a quick draft and interactive iteration.

Which do you prefer? Type A, B, or C.
```

### If user picks A or B
- Confirm the path and finish. (Nothing else to do in chat.)

### If user picks C (chat mode): conduct the 9 questions

For each step, ask ONE question at a time, wait for the answer, validate (non-empty), move on.

**Questions to ask (English by default, or the user's language):**

#### 1/9: Executive Steering Committee
> Who are the 5-8 members of the Executive Steering Committee? Include: Sponsor, Program Lead, Finance Lead, Security Lead, and Change Champion. Free format, for example a list of "Name, Title (Role)".

#### 2/9: Technology Product Owner (TPO)
> Who is the Technology Product Owner, and how is the office structured? List: Program Manager (name + % dedication), members (3-5 people), key responsibilities, and decision authority (what they approve without escalating).

#### 3/9: RACI Matrix
> What are the 5-8 main activities and their RACI roles (Responsible, Accountable, Consulted, Informed)? Free text or a table.

#### 4/9: Communication Plan
> How will you communicate the transformation to each audience? For each one (all Engineering, Working Groups, Steering, Champions, external stakeholders), give: channel, frequency, and owner.

#### 5/9: Training Plan
> What is the training plan? For each audience (Developers, Champions, Engineering Managers, SREs, and so on), list: format, cadence, and completion criteria.

#### 6/9: ADKAR Change Management
> For each ADKAR stage (Awareness, Desire, Knowledge, Ability, Reinforcement), list 1-3 concrete interventions you will run.

#### 7/9: Quick Wins, Weeks 1-4
> 4-6 quick wins for the first month: small initiatives with a visible result within 30 days. Suggest a week for each.

#### 8/9: Quick Wins, Weeks 5-8
> 4-6 quick wins for the second wave: expanding the pilots. Suggest a week for each.

#### 9/9: Quick Wins, Weeks 9-12
> 4-6 quick wins for the third wave: consolidating before scaling to H2.

### After the 9 answers (chat mode)

1. Show a summary of all 9 fields collected
2. Ask: "Does everything look right? Can I save it as `implementation-guide-inputs.json`?"
3. If yes:
   - Build the JSON with the schema below
   - Write to `implementation-guide-inputs.json` at workspace root
   - Confirm: `✓ Saved to implementation-guide-inputs.json (X% complete). Next: /gerar-relatorio`

## Schema (output `implementation-guide-inputs.json`)

```json
{
  "metadata": {
    "generated_at": "ISO-8601 UTC",
    "generator": "wizard-implementacao skill v1.0 (chat mode)",
    "completion_pct": 100
  },
  "implementation_guide_inputs": {
    "executive_steering_committee": "...",
    "tpo": "...",
    "raci_matrix": "...",
    "communication_plan": "...",
    "training_plan": "...",
    "adkar_notes": "...",
    "quick_wins_w1_4": "...",
    "quick_wins_w5_8": "...",
    "quick_wins_w9_12": "..."
  }
}
```

The 9 keys mirror exactly `sample_payload.json::implementation_guide_inputs` and the wizard React component schema.

## Constraints

- **DO NOT** invent answers if the user gives short/vague input — ask for more detail or accept and mark as "minimal".
- **DO** allow markdown (tables, lists, bold) in answers — they render in the PDF.
- **DO** validate at the end: if any field is empty, warn but allow saving (placeholders kick in at render time).
- **NEVER** modify `framework.json`, `respostas.json`, or files in `relatorios/templates/`.
- Output JSON to workspace root (NOT to `saida/`) so the file persists across pipeline runs and serves as **input**, not output.

## Integration with other skills

- After this skill runs, `/gerar-relatorio` will **automatically detect** `implementation-guide-inputs.json` at the root and merge it into the payload before rendering the 5 PDFs.
- If client edits `implementation-guide-inputs.json` manually later (e.g., updates RACI), they just rerun `/gerar-relatorio` — no need to redo the wizard.

## Reference example

The folder `wizard/` contains:
- `implementation-guide-wizard.html` — full HTML wizard (mode A)
- `implementation-guide-inputs.template.json` — pre-filled JSON template with rich placeholders (mode B starting point)

Both produce JSONs with the same schema described above.
