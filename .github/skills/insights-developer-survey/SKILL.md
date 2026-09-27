---
name: insights-developer-survey
description: "Generates aggregated insights report from imported Developer Survey responses. Reads survey-devs/respostas-devs.json and produces saida/insights-developer-survey-<DATE>.md with: respondent demographics, Copilot adoption + mode usage, agent/MCP awareness, governance gaps, pain points (anonymized quotes), and prioritized recommendations linked to the maturity assessment capabilities (P1-C1, P1-C5, P1-C8, P2-C4, P3-C6). Use after /importar-survey-devs, or when the user asks for \"developer survey insights\", \"survey report\", \"team AI maturity\", \"insights do survey\", \"relatório do survey de devs\"."
---

# Skill: Generate Developer Survey Insights Report

## When to use
- After `/importar-survey-devs` (depends on `survey-devs/respostas-devs.json`)
- When the team wants to see aggregated insights from the developer survey
- To inform `/wizard-implementacao` (Implementation Guide of the maturity assessment) with real developer voice

## Inputs
- `survey-devs/respostas-devs.json` — all respondents and answers (output of `/importar-survey-devs`)
- `survey-devs/perguntas-para-forms-devs.md` — schema reference (for question text + types)
- `survey-devs/scripts/calcular_maturidade.py` — **invoke first** to compute team maturity scores per dimension (D2-D8) using deterministic rubric. Output: `saida/maturidade-developer-survey-<DATE>.json`
- `survey-devs/RUBRICA-MATURIDADE.md` — rubric documentation (read for explanations to include in the report)
- (optional) `saida/scores.json` — to cross-reference with maturity assessment scores (P1-C1, etc.)

## Expected output
- `saida/insights-developer-survey-<DATE>.md`: full report (English by default; `--lang pt-br` for Portuguese) with sections, tables, charts (ASCII), and citations
- Brief chat summary (English by default, or the user's language): N respondents, top 3 insights, top 3 gaps

## Procedure

### Implementation: invoke the official script

The skill should INVOKE the script that does both maturity calculation AND insights generation in one go:

```bash
python3 survey-devs/scripts/gerar_insights.py

# Portuguese report:
python3 survey-devs/scripts/gerar_insights.py --lang pt-br
```

This script:
1. Loads `survey-devs/respostas-devs.json`
2. Computes maturity per respondent + aggregates team scores via `rubric.py`
3. Generates descriptive aggregations (% adoption, top tools, pain quotes)
4. Outputs:
   - `saida/maturidade-developer-survey-<DATE>.json` (rubric scores)
   - `saida/insights-developer-survey-<DATE>.md` (12-section report, English by default)

**DO NOT reimplement aggregation in chat**: the script handles all of it deterministically.

### Optional: maturity only (without report)

If user wants just the maturity scores (without the full report):

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output: saida/maturidade-developer-survey-<DATE>.json only
# Portuguese labels and console text: add --lang pt-br
```

### 1. Load and validate

```python
import json
from pathlib import Path
KIT = Path.cwd()

data = json.load(open(KIT / "survey-devs/respostas-devs.json"))
maturity = json.load(open(KIT / f"saida/maturidade-developer-survey-{date}.json"))
n = data["metadata"]["total_respondents"]
if n < 3:
    warn(f"Only {n} respondents: insights are unreliable. Recommended ≥5.")
```

### 2. Compute aggregations per question

For each question, group answers and count:

```python
from collections import Counter

def aggregate(qid, q_type):
    """Returns ordered list of (option, count, percent)."""
    counts = Counter()
    total = 0
    for r in data["respondents"]:
        if qid not in r["responses"]:
            continue
        val = r["responses"][qid]["value"]
        if q_type == "multi":
            for opt in val.split(";"):
                counts[opt.strip()] += 1
                total += 1
        elif q_type == "text":
            continue  # quotes handled separately
        else:  # choice
            counts[val] += 1
            total += 1
    return sorted(
        [(opt, n, round(100 * n / total, 1) if total else 0) for opt, n in counts.items()],
        key=lambda x: x[1],
        reverse=True,
    )
```

### 3. Generate ASCII bar charts

```python
def bar(pct, width=30):
    filled = int(round(pct * width / 100))
    return "█" * filled + "░" * (width - filled)
```

### 4. Build the report

Structure (English shown; `--lang pt-br` produces the same structure in Portuguese):

```markdown
# Developer Survey: Insights Report

**Date:** {date}
**Respondents:** {n} (anonymous)
**Coverage:** {pct}% of questions answered on average

{#if n < 5}
> ⚠️ Only {n} respondents: insights are preliminary. Consider collecting more responses (≥15 recommended for team representativeness).
{/if}

---

## 1 · Executive Summary

### 🎯 Team AI Maturity (deterministic rubric)

> **Overall: {team_overall_score} ({team_overall_label})**
> Based on {n_respondents} respondents, 7 dimensions, L0-L4 scale (same as the maturity assessment).

| Dimension | Score | Label | % devs at L3+L4 |
|---|---|---|---|
| D2 Copilot Adoption | {d2.team_score} | {d2.label} | {d2.pct_l3_l4}% |
| D3 MS/GH Tooling Breadth | {d3.team_score} | {d3.label} | {d3.pct_l3_l4}% |
| D4 AI Dev Practices | {d4.team_score} | {d4.label} | {d4.pct_l3_l4}% |
| D5 Agent Concepts Mastery | {d5.team_score} | {d5.label} | {d5.pct_l3_l4}% |
| D6 Instructions Maturity | {d6.team_score} | {d6.label} | {d6.pct_l3_l4}% |
| D7 Best Practices | {d7.team_score} | {d7.label} | {d7.pct_l3_l4}% |
| D8 Security & Governance | {d8.team_score} | {d8.label} | {d8.pct_l3_l4}% |

### 🏆 3 strongest dimensions
- {ranking.top_1}: {score}
- {ranking.top_2}: {score}
- {ranking.top_3}: {score}

### ⚠️ 3 largest gaps (roadmap opportunities)
- 🔴 {ranking.bottom_1}: {score}, {suggested action}
- 🟠 {ranking.bottom_2}: {score}, {suggested action}
- 🟡 {ranking.bottom_3}: {score}, {suggested action}

### 💡 3 key insights
- {insight_1, derived from maturity + descriptive data}
- {insight_2}
- {insight_3}

---

## 2 · Demographics (S1)

### Distribution by role
| Role | N | % | Visual |
|---|---|---|---|
| Backend | 4 | 33% | █████████░░ |
| Frontend | 3 | 25% | ██████░░░░░ |
| ...

### Years of experience
{table}

### Stack
{table}

---

## 3 · GitHub Copilot: Adoption and Modes (S2)

### License coverage (S2-Q1)
| Type | N | % |
| Enterprise | 5 | 42% |
| Business | 3 | 25% |
| Pro (individual) | 2 | 17% |
| Free | 1 | 8% |
| No license | 1 | 8% |

### Usage frequency (S2-Q2)
{table}

### 🆕 Copilot Chat modes used (S2-Q3, multi-select)
| Mode | N users | % | Visual |
|---|---|---|---|
| Ask | 10 | 83% | ████████████████░░░░ |
| Edit | 8 | 67% | █████████████░░░░░░░ |
| Agent | 6 | 50% | ██████████░░░░░░░░░░ |
| Workspace | 3 | 25% | █████░░░░░░░░░░░░░░░ |
| Plan | 1 | 8% | ██░░░░░░░░░░░░░░░░░░ |
| **Not familiar** | 2 | 17% | ⚠️ |

**Insight:** {e.g., "50% already use Agent mode, high sophistication for a team this size"}

### MOST used mode (S2-Q4)
{table}

### Active features (S2-Q5, multi-select): Top 8
{table}

### Where they use it (S2-Q6)
{table}

### Perceived productivity gain (S2-Q7)
{table}

### Where Copilot helps most vs. does NOT help
- ✅ Top 3 tasks Copilot accelerates
- ❌ Top 3 where it does NOT help (based on S2-Q9 quotes)

---

## 4 · Other Microsoft tools (S3)

### Adoption (% using)
| Tool | N | % |
| GitHub Codespaces | ... |
| GitHub Advanced Security | ... |
| Azure OpenAI direct | ... |
| Azure AI Foundry | ... |
| Microsoft 365 Copilot | ... |

### Spec Kit / GitHub Models
{awareness}

---

## 5 · AI Development Practices (S4)

### TDD with AI (S4-Q1)
{table}

### SDD awareness (S4-Q2)
{table}

### When they consult AI (S4-Q3, multi-select)
{table}

### Treat AI as a pair? (S4-Q4)
{table}

### Onboarding with AI (S4-Q8)
{table}

### Practices that changed productivity (S4-Q9, anonymized quotes)
> "{quote 1}"
> "{quote 2}"
> "{quote 3}"

---

## 6 · Agent Concepts and Structure (S5)

### Concept awareness
| Concept | Knows + uses | Knows | Does not know |
|---|---|---|---|
| AI agent (vs assistant) | 4 | 5 | 3 |
| Ask/Edit/Agent modes | 6 | 4 | 2 |
| Custom agents (.agent.md) | 2 | 4 | 6 |
| Custom skills (SKILL.md) | 1 | 3 | 8 |
| Prompt files (.prompt.md) | 3 | 4 | 5 |
| MCP (Model Context Protocol) | 1 | 5 | 6 |
| Handoffs between agents | 0 | 3 | 9 |
| Subagents | 0 | 4 | 8 |

**Main gap:** {e.g., "Advanced concepts (MCP, handoffs, subagents) are unknown to >70%: workshop opportunity"}

### Primitives ALREADY CREATED (S5-Q9)
{table of what each respondent has created}

---

## 7 · Markdown / Memory / Instructions (S6)

### Who uses instructions files (S6-Q1)
{table}

### Who maintains them (S6-Q2)
{table}

### Update frequency (S6-Q3)
{table with alert if "nunca" (never) > 30%}

### Instructions content (S6-Q4)
{top 3}

### Shared prompt library (S6-Q5)
{table}

---

## 8 · Usability and Best Practices (S7)

### How they learned (S7-Q1)
{top 3}

### Is there a Champion on the team? (S7-Q2)
{distribution}

### Productivity metrics (S7-Q4)
{table}

### Typical iterations (S7-Q5)
{table}

### Trust in AI code without review (S7-Q6)
{table with alert if "quase sempre" (almost always) > 30%}

### Hallucinations detected (S7-Q7)
{table}

### Learning: more or less? (S7-Q8)
{table}

---

## 9 · 🔒 Security and Governance (S8)

### Documented policy (S8-Q1)
{table with alert if "não temos" (we do not have one) > 30%}

### Awareness of sensitive data (S8-Q2)
{table}

### Active security tools (S8-Q4)
{coverage per tool}

### Code Scanning on AI code (S8-Q5)
{table}

### SBOM (S8-Q6)
{table}

### Formal review of AI code (S8-Q7)
{table}

### DLP / Audit / Training (S8-Q8 to Q10)
{consolidated table}

### Vulnerabilities in AI code (S8-Q11)
{table}

**Governance Score:** {0-100 based on answers}
{interpretation}

---

## 10 · Pain Points and Wishlist (S9)

### Top 5 frustrations (S9-Q1, anonymized)
1. > "{quote 1}"
2. > "{quote 2}"
...

### Top 3 changes that would double productivity (S9-Q2)
1. > "{quote}"
...

### Top 3 desired features (S9-Q3)
1. > "{quote}"
...

---

## 11 · 🎯 Prioritized Recommendations

Based on the gaps above, ranked by impact × ease.

### Quick wins (next 30 days)
1. **{action}**: serves {N respondents} who mentioned {gap}
2. ...

### Next quarter
1. ...

### Strategic (semester)
1. ...

---

## 12 · 🔗 Link to the Maturity Assessment

If you ran the main assessment (`/calcular-scores`), this survey's answers relate to it as follows:

| Assessment capability | Signal from this survey | What it means |
|---|---|---|
| **P1-C1** AI Coding Assistants | S2-Q1 (% licensed), S2-Q2 (frequency), S2-Q7 (gain) | Real score vs. leadership perception |
| **P1-C5** Developer Onboarding and Training | S7-Q1 (how they learned), S7-Q2 (Champions) | Effectiveness of the training program |
| **P1-C8** Developer Productivity Measurement | S7-Q4 (DORA/DX/SPACE) | Measurement maturity |
| **P2-C4** DevSecOps | S8-Q4, S8-Q5, S8-Q11 | Real scanner coverage |
| **P3-C5** Agentic Applications | S5-Q3 (custom agents), S5-Q6 (MCP) | Technical sophistication in AI |

**Recommendation:** if an assessment capability is L3+ but the survey shows weak adoption, there is **dissonance between leadership and practice**: investigate.

---

## Appendix: Raw data

- Total respondents: {n}
- Average coverage: {pct}%
- Generated: {ISO date}
- Source: `survey-devs/respostas-devs.json`
- Imported from: {original_file}
```

### 5. Build the "3 key insights" automatically

Use heuristics:
- **Adoption insight:** "X% use Copilot daily, Y% only weekly": highlights the dominant pattern
- **Mode insight:** "The MOST used mode is {X}, Y% never tried mode {Z}": exploration gap
- **Concept insight:** "Only X% know {concept Y}" if < 30%: opportunity
- **Governance insight:** "X% have no AI policy" if no-policy > 50%: risk

### 6. Build the "3 gaps" automatically

Use thresholds (quoted values are the Portuguese Forms answer options the data contains):
- 🔴 P0 (Critical): missing governance (S8-Q1 "não temos" > 50%) OR frequent vulnerabilities (S8-Q11 "diariamente" + "semanalmente" > 30%)
- 🟠 P1 (High): unknown concepts (MCP/handoffs > 70% "não conhece") OR no instructions (S6-Q1 "nenhum" > 50%)
- 🟡 P2 (Medium): partial adoption (S2-Q2 "raro" + "nunca" > 40%) OR no Champion (S7-Q2 "não tem" > 50%)

## Report in chat (English by default, or the user's language)

```
✓ Maturity computed → saida/maturidade-developer-survey-2026-05-08.json
✓ Insights generated → saida/insights-developer-survey-2026-05-08.md (~14 page equivalent)

🎯 TEAM MATURITY: 2.22 (L2 Defined)
   Based on 12 anonymous respondents, 7 dimensions, deterministic rubric

📊 By dimension:
   D2 Copilot Adoption       0.80  L1 (40% L0, 40% L1)  ⚠️
   D3 MS/GH Tooling          2.40  L2
   D4 AI Dev Practices       2.68  L3
   D5 Agent Concepts         2.56  L3
   D6 Instructions           2.31  L2
   D7 Best Practices         2.91  L3 ✨
   D8 Security & Governance  1.92  L2

🏆 Strengths: D7 (Best Practices) · D4 (AI Practices) · D5 (Agents)
⚠️ Opportunities: D2 (Copilot Adoption) · D8 (Security) · D6 (Instructions)

📋 Next steps:
   1. To raise D2 → Copilot workshop + license review
   2. To raise D8 → formal policy + JIT permissions
   3. /wizard-implementacao to fold this into the Implementation Guide
```

## Constraints

- **NEVER cite respondents by name**: the survey is anonymous. Quotes are attributed by question (e.g., "Answer to S9-Q1"), not by person.
- **NEVER infer beyond what the data says**: if N=3 respondents, do not claim "the team"; say "3 respondents".
- **DO NOT** modify `survey-devs/respostas-devs.json` (read-only).
- Output to `saida/insights-developer-survey-<DATE>.md` only.
- Always include the date and respondent count prominently (data-driven, not opinion).
- If respondent count < 3, refuse to generate the full report; only show raw aggregations with a disclaimer.
