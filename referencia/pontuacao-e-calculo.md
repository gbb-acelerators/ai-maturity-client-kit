# AI Maturity Assessment Scoring and Calculation

🌐 English · [Português (Brasil)](pontuacao-e-calculo.pt-br.md)

> **Framework v1 (158 questions, 3 pillars).** For framework v2 (9 dimensions, 61 questions), see [framework-v2.md](framework-v2.md). v1 files still score with these rules.

> **Technical reference document**: describes precisely how each answer becomes a score, how capabilities/pillars/overall are aggregated, threshold rules, multi-respondent handling, gap analysis, and the PE score. The kit implements these formulas in [`scripts/assessment_engine.py`](../scripts/assessment_engine.py) (golden tests in `scripts/test_assessment_engine.py`).

**Algorithm version:** 1.0.0 · **Last code audit:** 2026-05-08

---

## Table of contents

1. [Three-layer conceptual model](#1-three-layer-conceptual-model)
2. [How each answer becomes a number](#2-how-each-answer-becomes-a-number)
3. [Official formulas](#3-official-formulas)
4. [Handling missing answers](#4-handling-missing-answers)
5. [Minimum coverage threshold](#5-minimum-coverage-threshold)
6. [Multi-respondent: aggregation](#6-multi-respondent-aggregation)
7. [Maturity labels (score mapping)](#7-maturity-labels-score-mapping)
8. [Gap analysis and prioritization](#8-gap-analysis-and-prioritization)
9. [PE Score (Production Engineering Readiness)](#9-pe-score-production-engineering-readiness)
10. [Persistence (tables and materialization)](#10-persistence-tables-and-materialization)
11. [**End-to-end example: Pillar P1**](#11-end-to-end-example-pillar-p1)
12. [**End-to-end example: Pillar P2**](#12-end-to-end-example-pillar-p2)
13. [**End-to-end example: Pillar P3**](#13-end-to-end-example-pillar-p3)
14. [Edge cases & guarantees](#14-edge-cases--guarantees)
15. [Glossary](#15-glossary)

---

## 1. Three-layer conceptual model

```
┌─────────────────────────────────────────────────────────────┐
│                    OVERALL SCORE (0–4)                      │
│    = weighted average of ALL capabilities (not pillars)     │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                  PILLAR SCORE (P1, P2, P3)                  │
│       = weighted average of the pillar's capabilities       │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                CAPABILITY SCORE (P1-C1 … P3-C9)             │
│      = weighted average of the capability's questions       │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│              QUESTION RESPONSE (L0=0 … L4=4)                │
│    = level selected by the respondent (multi → average)     │
└─────────────────────────────────────────────────────────────┘
```

**Important characteristic:** the **overall** is calculated directly over the capabilities (SUMPRODUCT); it is **not** the average of the 3 pillar scores. This prevents a pillar with few capabilities from weighing the same as one with many.

---

## 2. How each answer becomes a number

| Selected level | Label | Numeric value |
|---|---|---|
| L0 | Initial | **0** |
| L1 | Developing | **1** |
| L2 | Defined | **2** |
| L3 | Managed | **3** |
| L4 | Optimizing | **4** |

The scale is **discrete at input (integer 0-4)**, but the aggregations produce **continuous floating-point values (`f64`)**, with no rounding. Only the presentation layer (UI/report) decides the visual precision (usually 2 decimal places).

---

## 3. Official formulas

### 3.1 Capability score
> Reference code: [`scoring.rs:205-225`](../../app/backend/src/scoring.rs#L205)

$$
\text{capability\_score} = \frac{\sum_{q \in \text{respondidas}} (\text{nivel}_q \times \text{peso}_q)}{\sum_{q \in \text{respondidas}} \text{peso}_q}
$$

- Formula terms (kept as in the source): `respondidas` = answered questions, `nivel` = level, `peso` = weight, `TODAS as capabilities` = all capabilities.
- If no question in the capability was answered → `capability_score = None` (it does not enter the upper calculations).
- Default weights: **1.0**. Allowed range: **[0.5, 2.0]**.

### 3.2 Pillar score
> Reference code: [`scoring.rs:227-247`](../../app/backend/src/scoring.rs#L227)

$$
\text{pillar\_score} = \frac{\sum_{c \in \text{pillar}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{pillar}} \text{peso}_c}
$$

Only capabilities with `score = Some(_)` participate (capabilities without any answer are skipped).

### 3.3 Overall score
> Reference code: [`scoring.rs:250-263`](../../app/backend/src/scoring.rs#L250)

$$
\text{overall\_score} = \frac{\sum_{c \in \text{TODAS as capabilities}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{TODAS as capabilities}} \text{peso}_c}
$$

**Attention:** SUMPRODUCT directly over all capabilities; it is **not** `mean(P1, P2, P3)`.

---

## 4. Handling missing answers

| Situation | Behavior |
|---|---|
| Unanswered question | **Ignored**. It adds to neither `wsum` nor `wtotal`. No penalty. |
| Capability without any answer | `score = None`. It enters neither the pillar nor the overall. |
| Pillar without answered capabilities | `pillar_score = 0.0` (rare edge case). |
| Overall without answered capabilities | `overall_score = 0.0`. |

> **Golden rule:** "answered questions weigh, missing ones disappear". This encourages the respondent *not to guess* when they do not know: the system only penalizes via `threshold_status`, not via a deflated score.

---

## 5. Minimum coverage threshold

> Reference code: [`scoring.rs:351-359`](../../app/backend/src/scoring.rs#L351)

| Applicable questions | Status | Behavior |
|---|---|---|
| **≥ 40** | `Ok` | Normal scoring, no warning. |
| **25-39** | `Warning` | Scoring calculated, but the report shows the banner "Preliminary result: limited reliability". |
| **< 25** | `Blocked` | Scoring **refused**. The API responds 422 `InsufficientData`. |

"Applicable" = questions visible to the respondent's configured audience (after the `audience` filter). If a respondent is Backend, Frontend-only questions do not count.

---

## 6. Multi-respondent: aggregation

> Reference code: [`repos/scoring.rs:354-368`](../../app/backend/src/repos/scoring.rs#L354)

When more than one person answers the same assessment:

1. For each `question_id`, the system computes **`AVG(selected_level)`** over all respondents who answered that question.
2. This average value (which can be fractional, e.g., 2.67) enters as `nivel_q` in the capability score formula.
3. **There is no per-respondent weight**: every respondent counts equally.
4. **There is no stratification by audience**: if Backend and Frontend answer the same Q, the average mixes both.

**Example:** 3 respondents for Q1 with levels 2, 4, 3 → `Q1 = (2+4+3)/3 = 3.0`.

---

## 7. Maturity labels (score mapping)

> Reference code: [`scoring.rs:361-373`](../../app/backend/src/scoring.rs#L361)

Applied to any score (capability, pillar, or overall):

| Score range | Label | Color (token) |
|---|---|---|
| `score < 0.5` | **L0 Initial** | `--color-l0` (red) |
| `0.5 ≤ score < 1.5` | **L1 Developing** | `--color-l1` (amber) |
| `1.5 ≤ score < 2.5` | **L2 Defined** | `--color-l2` (blue) |
| `2.5 ≤ score < 3.5` | **L3 Managed** | `--color-l3` (green) |
| `score ≥ 3.5` | **L4 Optimizing** | `--color-l4` (purple) |

---

## 8. Gap analysis and prioritization

> Reference code: [`scoring.rs:307-349`](../../app/backend/src/scoring.rs#L307)

For each capability:

```
target_level   = target_overrides.get(capability_id) or 3.0 (default L3)
gap_size       = target_level − current_score
priority_score = peso_capability × gap_size

If gap_size ≤ 1e-9 (floating-point epsilon) → discard (target already reached)
```

### Priority classification

| `priority_score` | Label | Meaning |
|---|---|---|
| ≥ 2.4 | **P0** | Critical: address within the next 30 days |
| ≥ 1.6 and < 2.4 | **P1** | High: include in the next quarter |
| ≥ 0.9 and < 1.6 | **P2** | Medium: semester backlog |
| < 0.9 | **P3** | Low: monitor |

**Why `weight × gap`?** Capabilities with weight 2.0 and gap 1.5 (priority_score = 3.0) are more urgent than weight 1.0 and gap 2.0 (priority_score = 2.0): the weight reflects strategic impact on the overall.

---

## 9. PE Score (Production Engineering Readiness)

> Reference code: [`scoring.rs:266-304`](../../app/backend/src/scoring.rs#L266)

Sub-score calculated **only with questions flagged `pe = true`** in the seed.

- Filter → recalculate capability/pillar/overall with the subset.
- Same SUMPRODUCT.
- If no question has `pe = true` → returns `None`.
- It is shown side by side with the general overall, signaling production readiness (resilience, observability, runbooks, SLOs, etc.).

---

## 10. Persistence (tables and materialization)

> Reference migration: [`migrations/20260417000000_initial.sql`](../../app/backend/migrations/20260417000000_initial.sql)

| Table | Key columns | When it is populated |
|---|---|---|
| `assessment_scores` | `overall_score`, `pe_score`, `total_applicable`, `total_answered`, `scored_at` | `POST /api/scoring/trigger` |
| `pillar_scores` | `pillar_id`, `score` | same |
| `capability_scores` | `capability_id`, `score` (NULL if no answer), `weight` | same |
| `gap_analysis` | `capability_id`, `current_score`, `target_level`, `gap_size`, `priority`, `priority_score` | same |

`GET /api/scoring/results/{assessment_id}` reads **directly from the materialized tables**; it does not recalculate. This guarantees consistency across the generated reports and roadmaps.

---

## 11. End-to-end example: Pillar P1

### Scenario
Capability **P1-C1: AI Coding Assistants** (5 questions). Assessment answered by **2 developers** (R1 and R2). All questions have `weight = 1.0` (default).

### Real answers

| Question | Question (summarized) | R1 | R2 | **Avg** |
|---|---|---|---|---|
| `P1-C1-Q1` | Adoption of AI code completion tools | L3 (3) | L4 (4) | **3.5** |
| `P1-C1-Q2` | AI for code review and quality improvement | L2 (2) | L3 (3) | **2.5** |
| `P1-C1-Q3` | AI for test generation and maintenance | L1 (1) | L2 (2) | **1.5** |
| `P1-C1-Q4` | Prompt engineering and template management | L2 (2) | L2 (2) | **2.0** |
| `P1-C1-Q5` | Governance and security of AI tools | L3 (3) | L4 (4) | **3.5** |

### Step 1: Capability score (P1-C1)

```
wsum   = (3.5×1.0) + (2.5×1.0) + (1.5×1.0) + (2.0×1.0) + (3.5×1.0)
       = 3.5 + 2.5 + 1.5 + 2.0 + 3.5
       = 13.0

wtotal = 1.0 + 1.0 + 1.0 + 1.0 + 1.0 = 5.0

P1-C1.score = 13.0 / 5.0 = 2.60   →   Label: L3 Managed
```

### Step 2: Pillar score (P1)

Suppose P1-C1 is the only answered capability of pillar P1, with `weight_capability = 1.0`:

```
ws = 2.60 × 1.0 = 2.60
wt = 1.0
P1.score = 2.60 / 1.0 = 2.60   →   Label: L3 Managed
```

> In a real assessment, P1 has 9 capabilities. The calculation would be a SUMPRODUCT over all of them that have at least 1 answer.

### Step 3: Gap analysis

Default `target_level = 3.0`:

```
gap_size       = 3.0 − 2.60 = 0.40
priority_score = 1.0 × 0.40 = 0.40
classification = P3 (Low)   ← because 0.40 < 0.9
```

### Step 4: Threshold

5 answered questions << 25 → **`threshold_status = Blocked`** if this were the only capability assessed. In production, ≥ 40 answered questions are expected across the whole assessment.

---

## 12. End-to-end example: Pillar P2

### Scenario
Capability **P2-C1: CI/CD Pipeline Intelligence** (6 questions). Answered by **1 SRE** + **1 Platform Engineer**. Mixed weights: Q1 and Q5 with `weight = 1.5` (questions with direct impact on DORA metrics).

### Answers

| Question | Question (summarized) | Weight | SRE | PltEng | **Avg** |
|---|---|---:|---:|---:|---:|
| `P2-C1-Q1` | AI-driven CI/CD pipeline optimization | **1.5** | L4 (4) | L3 (3) | **3.5** |
| `P2-C1-Q2` | Self-healing builds and auto-correction | 1.0 | L2 (2) | L2 (2) | **2.0** |
| `P2-C1-Q3` | Predictive failure analysis | 1.0 | L1 (1) | L2 (2) | **1.5** |
| `P2-C1-Q4` | Intelligent cache optimization | 1.0 | L2 (2) | L3 (3) | **2.5** |
| `P2-C1-Q5` | DORA metrics and insights | **1.5** | L3 (3) | L4 (4) | **3.5** |
| `P2-C1-Q6` | Automated flaky test triage | 1.0 | L2 (2) | L1 (1) | **1.5** |

### Step 1: Capability score (P2-C1)

```
wsum   = (3.5×1.5) + (2.0×1.0) + (1.5×1.0) + (2.5×1.0) + (3.5×1.5) + (1.5×1.0)
       = 5.25 + 2.0 + 1.5 + 2.5 + 5.25 + 1.5
       = 18.00

wtotal = 1.5 + 1.0 + 1.0 + 1.0 + 1.5 + 1.0 = 7.0

P2-C1.score = 18.00 / 7.0 = 2.5714…   →   Label: L3 Managed
```

> **Note:** without the extra weights on Q1 and Q5, the simple average would be `(3.5+2.0+1.5+2.5+3.5+1.5)/6 = 2.4167` → it would drop to L2. The 1.5 weight reflects that these two dimensions matter more for a mature DevOps result.

### Step 2: Pillar score (P2) with 2 capabilities

Add P2-C2 (IaC) with score = 1.80, weight = 1.0:

```
ws = (2.5714 × 1.0) + (1.80 × 1.0) = 4.3714
wt = 1.0 + 1.0 = 2.0
P2.score = 4.3714 / 2.0 = 2.1857   →   Label: L2 Defined
```

### Step 3: Gap analysis (custom target)

For P2-C1, the SRE team set `target_level = 3.5` (above the default):

```
gap_size       = 3.5 − 2.5714 = 0.9286
priority_score = 1.0 × 0.9286 = 0.9286
classification = P2 (Medium)   ← because 0.9 ≤ 0.9286 < 1.6
```

---

## 13. End-to-end example: Pillar P3

### Scenario
Capability **P3-C5: Agentic Applications** (6 questions). Answered by **1 Architect** + **1 ML Engineer** + **1 Security**. Q1, Q3, and Q6 with `weight = 2.0` (maximum weights: the innovation frontier).

### Answers

| Question | Question (summarized) | Weight | Arch | ML | Sec | **Avg** |
|---|---|---:|---:|---:|---:|---:|
| `P3-C5-Q1` | Implementation of autonomous AI agents | **2.0** | L2 (2) | L3 (3) | L1 (1) | **2.0** |
| `P3-C5-Q2` | Multi-agent coordination (orchestration) | 1.0 | L1 (1) | L2 (2) | L1 (1) | **1.33** |
| `P3-C5-Q3` | Tool-use and function calling frameworks | **2.0** | L3 (3) | L4 (4) | L2 (2) | **3.0** |
| `P3-C5-Q4` | Persistent agent memory | 1.0 | L2 (2) | L2 (2) | L1 (1) | **1.67** |
| `P3-C5-Q5` | Continuous evaluation and safety guardrails | 1.0 | L1 (1) | L2 (2) | L3 (3) | **2.0** |
| `P3-C5-Q6` | Governance and auditing of agent actions | **2.0** | L1 (1) | L1 (1) | L3 (3) | **1.67** |

### Step 1: Capability score (P3-C5)

```
wsum   = (2.00×2.0) + (1.33×1.0) + (3.00×2.0) + (1.67×1.0) + (2.00×1.0) + (1.67×2.0)
       = 4.00 + 1.33 + 6.00 + 1.67 + 2.00 + 3.34
       = 18.34

wtotal = 2.0 + 1.0 + 2.0 + 1.0 + 1.0 + 2.0 = 9.0

P3-C5.score = 18.34 / 9.0 = 2.0378…   →   Label: L2 Defined
```

### Step 2: Gap analysis (strategic capability)

Leadership set `target_level = 4.0` (ambition: lead in the agentic space), and the capability has `weight = 1.5`:

```
gap_size       = 4.0 − 2.0378 = 1.9622
priority_score = 1.5 × 1.9622 = 2.9433
classification = P0 (Critical)   ← because 2.9433 ≥ 2.4
```

→ This capability **enters the roadmap for the next 30 days** with top priority.

### Step 3: Contribution to the overall

If the full assessment has 28 active capabilities, P3-C5 with `score = 2.0378` and `weight = 1.5` contributes:
- Overall numerator: `+ 2.0378 × 1.5 = +3.0567`
- Overall denominator: `+ 1.5`

→ Raising P3-C5 from 2.04 to 3.5 (practical L3 target) would add `(3.5 − 2.04) × 1.5 = 2.19` to the numerator and raise the overall by ~`2.19 / wtotal_overall` points.

---

## 14. Edge cases & guarantees

| Situation | Guarantee |
|---|---|
| `wtotal = 0` (no question answered) | Returns `None` (capability) or `0.0` (pillar/overall). Never divides by zero. |
| Score above 4.0 | Impossible by construction: all levels ∈ [0,4] and weighted averages preserve the range. |
| Score below 0.0 | Impossible: `selected_level ∈ [0,4]`. |
| Negative `gap_size` (target already exceeded) | Filtered out (does not appear in the roadmap). |
| Multi-respondent with 0 answers | Capability becomes `None`, without error. |
| Respondent outside the audience | Their answers to non-applicable questions are **ignored in scoring** but stored for auditing. |
| Reprocessing (recalculate after a new answer) | Idempotent: `POST /api/scoring/trigger` replaces the 4 materialized tables in one transaction. |

---

## 15. Glossary

| Term | Definition |
|---|---|
| **Question** | Concrete assessment item. Standard ID `P[1-3]-C[1-19]-Q[1-99]`. |
| **Capability** | Functional subdomain. Groups 5-7 questions. |
| **Pillar** | Strategic dimension. Groups 9-10 capabilities. P1, P2, or P3. |
| **Level (L0-L4)** | Maturity of an individual answer. Integer 0-4. |
| **Score** | Continuous result `f64 ∈ [0,4]` produced by aggregation. |
| **Weight** | Weight of the question (`[0.5, 2.0]`, default 1.0) or of the capability. |
| **Threshold** | Minimum coverage of answered questions: 25 (warning), 40 (ok). |
| **PE flag** | Flags questions critical for Production Engineering. They generate a parallel sub-score. |
| **Gap** | `target − current` per capability. |
| **Priority score** | `weight × gap`, which classifies the capability into P0/P1/P2/P3. |
| **Audience** | Target audiences of the question (developer, sre, security…). Filters visibility in the form. |
| **`threshold_status`** | `Ok` / `Warning` / `Blocked`, returned together with the result. |

---

**Related files:**
- 📄 `pontuacao-e-calculo.xlsx`: auditable workbook with visible SUMPRODUCT formulas (same examples as this doc)
- 🌐 `calculadora-pontuacao.html`: standalone interactive calculator (select answers, see scores live)
- 📚 `P1-…md`, `P2-…md`, `P3-…md`: real assessment questions with KPI/context/evidence per level
