---
name: plano-capacitacao
description: "Generates a prioritized capacitation roadmap (plano de capacitação) from the Learning & Growth Survey responses. Reads survey-learning/respostas-learning.json (IDENTIFIED respondents with name+email) and produces saida/plano-capacitacao-<DATE>.md with: top 10 topics demanded, suggested cohorts per dimension D2-D8 (with attendee lists), Champions Network candidates, mentor↔mentee pairs, calendar of workshops, barriers to remove, capacitation roadmap, training plan. Use after /importar-survey-learning when user asks for \"plano de capacitação\", \"training roadmap\", \"Champions Network\", \"workshops priorizados\", \"treinamento\", \"capacitation plan\", \"plano-capacitacao\"."
---

# Skill: Generate Capacitation Plan from Learning Survey

## When to use
- After `/importar-survey-learning` (depends on `survey-learning/respostas-learning.json`)
- When leadership wants an **actionable plan** for training, Champions, and workshops
- Output feeds `/wizard-implementacao` (Training Plan, ADKAR, and Quick Wins steps)

## Inputs
- `survey-learning/respostas-learning.json`: identified respondents and their answers
- `survey-learning/perguntas-para-forms-learning.md`: schema reference
- (optional) `saida/maturidade-developer-survey-<DATE>.json`: cross-reference with measured maturity
- (optional) `saida/scores.json`: capabilities from the main assessment (P1-C1, etc.)

## Expected output
- `saida/plano-capacitacao-<DATE>.md`: full plan (12 sections, about 10 page equivalent), English by default; `--lang pt-br` for Portuguese
- Brief chat summary (English by default, or the user's language): N respondents, top 5 topics, N Champions, top 3 suggested workshops

## Procedure

### Implementation: invoke the official script

The skill should INVOKE the script that aggregates and generates the full plan:

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py

# Portuguese plan:
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
```

This script:
1. Loads `survey-learning/respostas-learning.json`
2. Aggregates: priorities (L3-Q1), topics (L4), formats (L5), Champions (L6), barriers (L7), wishlist (L7)
3. Generates a 12-section report (English by default) with:
   - Top 10 topics with attendee names+emails
   - Cohorts per dimension D2-D8
   - Champions Network (3 tiers)
   - Mentor↔mentee pairs
   - Calendar 90 days
   - 5 prioritized actions
4. Outputs: `saida/plano-capacitacao-<DATE>.md`

**DO NOT reimplement aggregation in chat**: the script handles all of it deterministically.

### Manual fallback (if user asks)

```python
import json
data = json.load(open("survey-learning/respostas-learning.json"))
n = data["metadata"]["total_respondents"]
if n < 3:
    warn(f"Only {n} respondents: the plan is preliminary.")
```

### 2. Aggregate self-perception by dimension (L2)

For each dimension D2-D8, count how many respondents are at each L0-L4. This is the "**team perceived maturity**" (different from D2-D8 measured by `/insights-developer-survey`).

```python
from collections import Counter
self_perception = {}
for did in ["D2", "D3", "D4", "D5", "D6", "D7", "D8"]:
    qid = f"L2-Q{int(did[1])-1}"   # L2-Q1 = D2, L2-Q2 = D3, ...
    counts = Counter()
    for r in data["respondents"]:
        ans = r["responses"].get(qid, {}).get("value", "")
        # Extract level from "L0 — ..." pattern
        if ans.startswith("L0"): counts["L0"] += 1
        elif ans.startswith("L1"): counts["L1"] += 1
        elif ans.startswith("L2"): counts["L2"] += 1
        elif ans.startswith("L3"): counts["L3"] += 1
        elif ans.startswith("L4"): counts["L4"] += 1
    self_perception[did] = counts
```

### 3. Aggregate priority dimensions (L3-Q1)

Count which dimensions devs want to grow MOST:

```python
priorities = Counter()
for r in data["respondents"]:
    ans = r["responses"].get("L3-Q1", {}).get("value", "")
    for d in ["D2", "D3", "D4", "D5", "D6", "D7", "D8"]:
        if d in ans:
            priorities[d] += 1
```

### 4. Aggregate desired topics (L4-Q1 to L4-Q5)

Top 10 topics most-requested across all 5 question groups:

```python
topic_counts = Counter()
topic_to_attendees = {}  # topic -> list of (name, email)
for r in data["respondents"]:
    for qid in ["L4-Q1", "L4-Q2", "L4-Q3", "L4-Q4", "L4-Q5"]:
        topics = r["responses"].get(qid, {}).get("value", "").split(";")
        for t in topics:
            t = t.strip()
            if not t or "Já domino" in t or "Não tenho interesse" in t:
                continue
            topic_counts[t] += 1
            topic_to_attendees.setdefault(t, []).append((r["name"], r["email"]))
```

### 5. Aggregate format preferences (L5)

```python
formats = Counter()
for r in data["respondents"]:
    fmts = r["responses"].get("L5-Q1", {}).get("value", "").split(";")
    for f in fmts:
        formats[f.strip()] += 1

time_per_week = Counter()
for r in data["respondents"]:
    time_per_week[r["responses"].get("L5-Q2", {}).get("value", "")] += 1

cohort_pref = Counter()
for r in data["respondents"]:
    cohort_pref[r["responses"].get("L5-Q4", {}).get("value", "")] += 1
```

### 6. Identify Champions candidates (L6-Q1)

```python
champions = []
for r in data["respondents"]:
    ans = r["responses"].get("L6-Q1", {}).get("value", "")
    if ans.startswith("Sim — quero ser Champion ativo"):
        champions.append({"name": r["name"], "email": r["email"], "tier": "active"})
    elif "Sim — mas só se tiver suporte" in ans:
        champions.append({"name": r["name"], "email": r["email"], "tier": "supported"})
    elif ans.startswith("Talvez"):
        champions.append({"name": r["name"], "email": r["email"], "tier": "maybe"})
```

### 7. Identify mentor↔mentee pairs

```python
mentees = []  # who wants mentoring
mentors = []  # who offers to mentor

for r in data["respondents"]:
    if "Sim" in r["responses"].get("L6-Q3", {}).get("value", ""):
        mentees.append({"name": r["name"], "email": r["email"]})
    if "Sim" in r["responses"].get("L6-Q4", {}).get("value", ""):
        topic = r["responses"].get("L6-Q5", {}).get("value", "")
        mentors.append({"name": r["name"], "email": r["email"], "topic": topic})

# Cross-reference people named in L6-Q2 (who they consider a reference)
references = Counter()
for r in data["respondents"]:
    ref = r["responses"].get("L6-Q2", {}).get("value", "").strip()
    if ref and len(ref) > 2:
        references[ref] += 1
```

### 8. Aggregate barriers (L7-Q1)

```python
barriers = Counter()
for r in data["respondents"]:
    bs = r["responses"].get("L7-Q1", {}).get("value", "").split(";")
    for b in bs:
        if b.strip() and "sem barreiras" not in b.lower():
            barriers[b.strip()] += 1
```

### 9. Build the report

Structure (English shown; `--lang pt-br` produces the same structure in Portuguese):

```markdown
# AI Capacitation Plan: Personalized Roadmap

**Date:** {date} · **Respondents:** {n} (identified)

---

## 1 · Executive Summary

### AI maturity as perceived by the team (L2 self-assessment)
| Dimension | L0 | L1 | L2 | L3 | L4 | Median |
|---|---|---|---|---|---|---|
| D2 Copilot | 2 | 5 | 3 | 1 | 0 | L1 |
| D3 Tooling | ... |
...

### Top 3 PRIORITY dimensions to grow (L3-Q1)
1. D5 Agent Concepts (8 votes)
2. D2 Copilot Adoption (6 votes)
3. D8 Security (5 votes)

### Top 10 most requested topics (L4)
1. Autonomous Coding Agent (10 devs)
2. SDD with Spec Kit (8 devs)
...

### Champions Network identified
- 3 active · 2 with support · 4 maybe
- Top 3 references mentioned: {names}

### 3 recommended quick wins
1. **Coding Agent workshop (4h)**: 10 pre-validated attendees
2. **Spec Kit cohort (6 weeks, self-paced)**: 8 attendees
3. **Biweekly office hours**: serves 100% of respondents

---

## 2 · Requested topics: Top 10 (with pre-validated attendee lists)

### 1. Autonomous Coding Agent (D5): 10 attendees
**Demand:** 10/12 devs (83%)
**Suggested workshop:** 4h hands-on
**Prerequisite:** L1+ in D5 (Agent Concepts)
**Pre-validated attendees** (confirmed in their answers):
- Maria Silva (maria@...)
- João Santos (joao@...)
...

**Action:** schedule the workshop within 30 days. Invite Maria as Champion (she already volunteered in L6-Q1).

### 2. SDD with Spec Kit (D4): 8 attendees
...

(Repeat for the top 10)

---

## 3 · Suggested cohorts per rubric dimension

### Cohort D5 (Agent Concepts)
- 8 devs want to grow
- Their preferred format: hands-on workshop (5/8) + cohort (4/8)
- Cadence: 4-6h/week (60%)
- **Plan:** 6-week cohort with 5 live sessions + self-paced lab
- **Topics:** custom agents, MCP, A2A, handoffs, agent testing
- **Champion candidate:** Maria Silva (already volunteered + L3 self-perceived)

(Repeat for D2, D3, D4, D6, D7, D8 according to demand)

---

## 4 · Champions Network

### Active (want to be Champions without extra support): 3 people
| Name | Email | Suggested topics | Next step |
|---|---|---|---|
| Maria | maria@... | D5 Agents, D2 Copilot | Invite to train-the-trainer |
| ...

### With support (want to be Champions if they get dedicated training): 2 people
...

### Mentor candidates (volunteered to mentor in L6-Q4 and L6-Q5)
| Name | Topic they teach | N mentee candidates |
|---|---|---|
| ...

### Mentees (want 1:1 or peer mentoring)
...

### Natural references (mentioned in L6-Q2)
- "João Santos" mentioned by 4 people: undeclared natural Champion, reach out
- ...

---

## 5 · Suggested workshop calendar (next 90 days)

| Week | Workshop | Audience | Champion | Format |
|---|---|---|---|---|
| W1 | Champions Network kickoff | 5 | You (Eng Mgr) | 2h live |
| W2 | Coding Agent workshop | 10 | Maria | 4h hands-on |
| W3 | SDD/Spec Kit cohort kickoff | 8 | TBD | 1h live |
| ...

---

## 6 · Formats and cadence preferred by the team

### Top formats
1. Hands-on workshop 3-4h (X% asked)
2. Weekly office hours (Y%)
3. Pair programming with a Champion (Z%)
...

### Time available per week (median)
2-4h/week

### Cohort vs self-paced
60% cohort · 40% self-paced (recommended: hybrid)

---

## 7 · Barriers to remove (prioritized)

1. **Lack of time** ({N}/{total} mentioned) → action: block 2h/week on the team calendar
2. **No Copilot license** ({N}) → action: review licenses with IT, target 100% by Q+1
3. **No Champion** ({N}) → action: activate the Champions Network identified in section 4
4. **Do not know where to start** ({N}) → action: publish a documented learning path in a shared Copilot Space

---

## 8 · Team wishlist and ideas (L7-Q2 to Q4)

### Workshops suggested by the team (L7-Q2)
> "{quote 1}"
> "{quote 2}"
...

### Suggested external speakers (L7-Q3)
- {name 1}: mentioned by X
- ...

### Other open suggestions (L7-Q4)
> "{relevant quote}"

---

## 9 · 🔗 Link to the other surveys

### vs. team maturity (Developer Survey, deterministic rubric)
| Dimension | Self-perception (L2) | Measured rubric (D-X) | Dissonance |
|---|---|---|---|
| D2 Copilot | median L1 | 0.80 (L1) | ✓ aligned |
| D5 Agents | median L1 | 2.56 (L3) | ⚠ underconfidence! |
| D8 Security | median L2 | 1.92 (L2) | ✓ aligned |
...

> **Insight:** the team is more mature in D5 than it perceives. Internal Champions can mentor others.

### vs. main assessment capabilities
| Capability | Assessment score | Team demand | Recommendation |
|---|---|---|---|
| P1-C1 Copilot | L3 (leader) | 6 devs want to grow | Workshop validated by the plan |
| P3-C5 Agentic Apps | L1 (gap) | 8 devs want to grow | **Strong match**: prioritize |

---

## 10 · 🎯 Top 5 prioritized actions

Ranked by impact (n_demand) × ease (cohort/Champion already mapped) × alignment with assessment gaps.

1. **Coding Agent workshop (W2)**: 10 attendees × Champion identified × addresses the P1-C1 gap
2. **SDD with Spec Kit cohort (W3-W8)**: 8 attendees × covers D4 + P3-C5
3. **Champions kickoff (W1)**: activates the network of 5 identified Champions
4. **Biweekly office hours (W2+)**: addresses the "do not know where to start" barrier
5. **License review** (IT): removes the license barrier, raises D2

---

## 11 · 📅 Next 30 days

- **Week 1:** Champions kickoff + workshop scheduling
- **Week 2:** Coding Agent workshop (Maria)
- **Week 3:** SDD cohort start + Office hours #1
- **Week 4:** Retrospective + plan adjustments

---

## 12 · 📋 Appendix: respondents (leadership only)

> ⚠️ This appendix contains names and emails. **DO NOT share publicly**; use only for workshop invitations.

| Name | Email | Role | Average self-perception | Available? | Wants to be Champion? |
|---|---|---|---|---|---|
| Maria | maria@... | Tech Lead | L2.7 | 4-6h/week | Yes, active |
...

(N respondents total)
```

### 10. Report in chat (English by default, or the user's language)

```
✓ Capacitation plan → saida/plano-capacitacao-2026-05-08.md (~10 pages)

📊 Summary:
   • 12 IDENTIFIED respondents
   • Top demand: Coding Agent (10) · SDD with Spec Kit (8) · Spaces (7)
   • Champions identified: 3 active + 2 with support
   • Mentor candidates: 4 · Mentee candidates: 6
   • Top barrier: lack of time (8/12 mentioned)

🎯 5 prioritized actions (next 30 days):
   1. Champions kickoff (W1)
   2. Coding Agent workshop (W2): 10 attendees
   3. SDD with Spec Kit cohort (W3): 8 attendees
   4. Biweekly office hours (W2+)
   5. Review Copilot licenses (IT)

📋 Next: /wizard-implementacao uses this plan in training_plan + adkar_notes + quick_wins
```

## Constraints

- The survey is **IDENTIFIED**: names and emails may appear IN THE REPORT, but only in the "Appendix: leadership only" section
- **DO NOT** send emails automatically; only list names for the leader to invite manually
- **DO NOT** invent topics beyond what was answered
- Cross-reference with `/insights-developer-survey` and `/calcular-scores` when both exist (compares perception vs reality)
- Output to `saida/plano-capacitacao-<DATE>.md` only
- If a respondent left name OR email blank, count them but mark as "anonymous (incomplete)"; do not invent
