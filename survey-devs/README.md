# `survey-devs/`: Developer Survey (anonymous, behavioral, individual)

🌐 English · [Português (Brasil)](README.pt-br.md)

This folder contains a **survey separate** from the main assessment. It focuses on understanding **how each developer uses GitHub Copilot, AI agents, instructions files, Copilot Chat modes, practices (TDD/SDD), governance, and security** day to day. Anonymous.

> 💡 **Companion to this survey:** after running **survey-devs** (anonymous, measures behavior), also consider **[survey-learning](../survey-learning/)** (identified, measures what developers want to learn). Together they form a 360° view of developers: behavioral plus aspirational.

> 🔄 **Version 2.0 (updated 2026-05-08)**: terminology updated with official changes:
> - **Copilot Workspace** evolved into **Copilot Coding Agent** (GA Sep/2025)
> - **Copilot Spaces** (GA Sep/2025) replaced **Knowledge Bases** (sunset Nov/2025)
> - **Azure AI Foundry** renamed to **Microsoft Foundry** + **Foundry Agent Service** GA
> - Added questions about **MCP**, **A2A protocol**, Microsoft Agentic DevOps personas (**System Designer**, **Agent Operator**), **testing agents before using them**, **scope+red-lines**, and **JIT permissions**.

## 📐 Difference vs. the main assessment and survey-learning

| Aspect | Main assessment | Developer Survey (this one) | **survey-learning** |
|---|---|---|---|
| **Audience** | Leadership / architects / Tech Leads | **Individual developers** (any role) | Individual developers |
| **Anonymous?** | No, identified by organization | **Yes, anonymous Forms** | **No, IDENTIFIED (name+email)** |
| **Focus** | Organizational maturity (L0-L4) | Real individual adoption and practice | **What they want to LEARN** |
| **Scale** | 5-point Likert per capability | Choice/multi-choice/free text | Self-perception L0-L4 + multi |
| **Size** | 61 questions across 9 dimensions (v2) | **75 questions in 9 sections** | 32 questions in 7 sections |
| **Time per respondent** | 60-90 min | **22-28 min** | 5-8 min |
| **Multi-respondent** | Possible but not the default | **Essential** (average ≥5, ideal ≥15) | **Essential** (>50% of the team) |
| **Output** | Executive report + 5 PDFs | Insights report + computed maturity | Capacitation plan + Champions |
| **Skills** | `/calcular-scores`, `/gerar-relatorio`, etc. | `/importar-survey-devs` + `/insights-developer-survey` | [`/importar-survey-learning`](../survey-learning/) + `/plano-capacitacao` |

**The 3 are complementary:**
- This **survey-devs** measures BEHAVIOR (anonymous)
- **[survey-learning](../survey-learning/)** measures DESIRE (identified, complements this one)
- The **main assessment** measures STRATEGY (leadership)
- Together they form a 360° diagnosis.

## 📋 The 9 survey sections (v2.0, updated 2026-05-08)

| # | Section | Focus | Q |
|---|---|---|---|
| **S1** | Profile | Role, experience, stack, work model | 7 |
| **S2** | GitHub Copilot: Adoption and Modes | License, frequency, **Ask / Edit / Agent / Coding Agent (autonomous)**, features (incl. **Spaces**), gains | 9 |
| **S3** | Other Microsoft / GitHub tools | **Microsoft Foundry** (formerly Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, Spec Kit, **MCP** | 7 |
| **S4** | AI Development Practices | TDD with AI, **SDD with Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Agent Concepts and Structure | Agent vs assistant, Copilot modes, custom agents/skills/prompts, **A2A**, handoffs, subagents, **Microsoft Agentic DevOps personas** (System Designer / Agent Operator), **TESTING agents before using them** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions in **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usability and Best Practices | How they learned (incl. MS Build / GitHub Universe), Champion, DORA/DX metrics, iterations, trust | 9 |
| **S8** | Security and Governance | Policy, sensitive data, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **agent scope+red-lines**, **JIT permissions**, training | 13 |
| **S9** | Pain Points & Wishlist | Frustrations, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

## 🗂️ Files in this folder

| File | What it is |
|---|---|
| **[INSTRUCOES-FORMS-DEVS.md](INSTRUCOES-FORMS-DEVS.md)** | Step-by-step guide to build the Microsoft Forms (with anonymity settings + collection best practices) |
| **[perguntas-para-forms-devs.en.md](perguntas-para-forms-devs.en.md)** | The 75 questions in English, formatted for copy/paste into Forms (types, options, IDs). The canonical PT-BR bank is [perguntas-para-forms-devs.md](perguntas-para-forms-devs.md) |
| **[template-export-forms-devs.xlsx](template-export-forms-devs.xlsx)** | Excel template in the Forms export format + 5 mock respondents (varied profiles) |
| **[respostas-mock-devs.json](respostas-mock-devs.json)** | Sample structured JSON (to test the `/insights-developer-survey` skill) |
| **[RUBRICA-MATURIDADE.md](RUBRICA-MATURIDADE.md)** ⭐ | **Scoring model**: deterministic rubric that maps answers → L0-L4 levels in 7 dimensions. Mirrors the main assessment scale |
| **[scripts/rubric.py](scripts/rubric.py)** | Python implementation of the rubric (hardcoded rules per dimension) |
| **[scripts/calcular_maturidade.py](scripts/calcular_maturidade.py)** | CLI script that applies the rubric → `saida/maturidade-developer-survey-DATE.json` |

## 🚀 Usage flow (3 paths)

### Path A: Microsoft Forms (recommended for 10+ developers)

```
1. Build the Forms following INSTRUCOES-FORMS-DEVS.md (~30-45 min)
2. Share the link with the team (Slack/Teams/Email)
3. Wait 2 weeks (periodic reminders)
4. Responses → Open in Excel
5. Save as respostas-survey-devs.xlsx at the root of kit-cliente/
6. /importar-survey-devs       → survey-devs/respostas-devs.json
7. /insights-developer-survey  → saida/insights-developer-survey-DATE.md
```

### Path B: Shared Excel/SharePoint (fast for 3-5 developers)

```
1. cp survey-devs/template-export-forms-devs.xlsx respostas-survey-devs.xlsx
2. Clear the mock rows (rows 2-6)
3. Upload to SharePoint with edit permission
4. Each developer fills in one row
5. Download and move to the root
6. /importar-survey-devs + /insights-developer-survey
```

### Path C: Immediate smoke test (no real collection)

```
1. cp survey-devs/respostas-mock-devs.json survey-devs/respostas-devs.json
2. /insights-developer-survey  → see what the report looks like with 5 mocks
```

Useful to show the client "what it will look like" before collecting.

## 📊 What the insights report contains

`saida/insights-developer-survey-<DATE>.md` (generated by the skill) is written in **English by default**; run the scripts with `--lang pt-br` to get it in Portuguese (Brazil). It contains:

1. **Executive summary**: 3 insights + 3 gaps + perceived maturity
2. **Demographics** (S1): who answered, distribution
3. **Copilot adoption** (S2): % of licenses, **adoption by mode (Ask/Edit/Agent)**, active features, perceived gain
4. **MS/GitHub ecosystem** (S3): adoption table
5. **AI + dev practices** (S4): TDD, SDD, debugging, onboarding + anonymized quotes
6. **Agent knowledge** (S5): "knows+uses / knows / does not know" matrix for 8 concepts
7. **Instructions files** (S6): who uses, maintains, and updates them
8. **Usability** (S7): Champion, metrics, trust, iterations
9. **Security** (S8): policy, scanners, DLP, audit + **governance score 0-100**
10. **Pain points** (S9): top 5 frustrations + wishlist (quotes)
11. **Prioritized recommendations**: quick wins, next quarter, semester
12. **Connection to the main assessment**: capability by capability

## 🔗 How the survey informs the main assessment

If you ran both:

| Assessment capability | Survey signal | Validation |
|---|---|---|
| **P1-C1** AI Coding Assistants | S2-Q1, Q2, Q7 | Declared score vs. real adoption |
| **P1-C2** DevEx Platform | S6-Q5, S7-Q2 | Is there shared tooling? |
| **P1-C5** Onboarding and Training | S7-Q1, Q2 | How did developers learn? Are there Champions? |
| **P1-C8** Productivity Measurement | S7-Q4 | Are DORA/DX/SPACE really measured? |
| **P2-C4** DevSecOps | S8-Q4, Q5, Q11 | Active scanners vs. vulnerabilities seen |
| **P2-C10** Supply Chain | S8-Q4, Q6 | SBOM, secret scanning, DLP |
| **P3-C5** Agentic Applications | S5-Q3, Q6, Q9 | Custom agents, MCP: technical sophistication |
| **P3-C6** Identity and Access | S8-Q1, Q8, Q9 | Policy, DLP, audit |

> 💡 **Classic use case:** leadership rates P1-C1 as L3, but the survey reveals that 60% of developers rarely use it. That is a real adoption gap, not a licensing gap.

## 🔐 About anonymity

- Microsoft Forms has an "Anonymous responses" option: **CHECKING it is mandatory** for this survey
- Without it, Forms captures the respondent's MS365 account email (breaks anonymity)
- The `/importar-survey-devs` skill validates that the Email/Name columns are empty and warns if they are not
- Quotes in the report are cited by **question ID** (e.g., "Answer S9-Q1"), never by respondent_id or role

## 📅 Suggested cadence

- **First time:** before defining the AI strategy for engineering (baseline)
- **After a Copilot Enterprise rollout:** 30 days later
- **Quarterly:** measure evolution
- **After workshops/training:** validate absorption

## 📚 Related documentation

### Other kit folders
- **Companion survey (identified, capacitation):** [`../survey-learning/`](../survey-learning/): Learning & Growth Survey (32 q, 5-8 min, IDENTIFIED). Generates a personalized capacitation plan with a Champions Network and a workshop calendar. Use it AFTER this Developer Survey to move from "measured behavior" to "action plan"
- **Main assessment (organizational):** [`../README.md`](../README.md): 61 L0-L4 questions in 9 dimensions (framework v2), generates 4 PDFs
- **Multi-respondent collection for the main assessment:** [`../coleta/INSTRUCOES-FORMS.md`](../coleta/INSTRUCOES-FORMS.md)
- **Wizard that consolidates into the executive PDF:** [`../wizard/`](../wizard/): feeds Part 4 of the PDF with data from this survey + the learning survey

### Skills for this survey
- Skill that imports Excel → JSON: [`../.github/skills/importar-survey-devs/SKILL.md`](../.github/skills/importar-survey-devs/SKILL.md)
- Skill that generates the report + maturity: [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)

### How the 3 surveys connect (recommended order)

```
1. Survey-devs (anonymous, THIS ONE) → measures real behavior + computed maturity
2. Survey-learning (identified)      → measures desire + barriers + Champions
3. Main assessment                   → leadership rates INFORMED by the 2 above
4. /wizard-implementacao             → consolidates everything
5. /gerar-relatorio                  → 5 production-quality PDFs
```

## 🔗 Validated official sources (v2.0, 2026-05-08)

All survey terminology and concepts were cross-checked with official documentation. Use these sources to answer developer questions about what each term means:

### GitHub Copilot
- **Copilot Spaces** (GA Sep/2025): <https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/>
- **Official Spaces docs**: <https://docs.github.com/en/copilot/concepts/context/spaces>
- **Knowledge Bases sunset → Spaces** (Nov/2025): <https://github.blog/changelog/2025-10-17-copilot-knowledge-bases-can-now-be-converted-to-copilot-spaces/>
- **Copilot Coding Agent** (successor to Workspace, GA Sep/2025): assign an issue, it opens a PR on its own

### Microsoft Foundry (formerly Azure AI Foundry)
- **Foundry Agent Service overview**: <https://learn.microsoft.com/en-us/azure/foundry/agents/overview>
- **What's new Mar/2026** (MCP, A2A, multi-agent): <https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/>
- **Connectors (1,400+ business systems)**: <https://learn.microsoft.com/en-us/connectors/azureagentservice/>

### Agentic DevOps (Microsoft terminology)
- **DevOps Playbook for the Agentic Era**: <https://devblogs.microsoft.com/all-things-azure/agentic-devops-practices-principles-strategic-direction/>
- **Reimagining the developer lifecycle**: <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle>
- **Personas (System Designer, Agent Operator)**: <https://learn.microsoft.com/en-us/azure/well-architected/ai/personas>
- **Microsoft Reactor: Agentic DevOps Live**: <https://developer.microsoft.com/en-us/reactor/series/s-1625/>
- **Azure Agentic DevOps Solutions**: <https://azure.microsoft.com/en-us/solutions/devops>

### Spec-Driven Development
- **GitHub Spec Kit**: <https://github.com/github/spec-kit>

### Applicability to the main assessment
- The maturity assessment in the parent folder uses the 7 strategies S1-S7 (GitHub Migration, Foundry+SRE, App Modernization, AI Apps, Copilot Acceleration, Agentic Activation, Security & Governance), aligned with the Microsoft **Agentic DevOps** framework.
- The 8 profiles (full-stack, backend-api, platform-eng, security-ops, frontend, data-ml, devops-sre, legacy) cover the Agentic DevOps personas.
