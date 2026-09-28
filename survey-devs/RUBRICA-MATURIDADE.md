# AI Maturity Rubric: Developer Survey

🌐 English · [Português (Brasil)](RUBRICA-MATURIDADE.pt-br.md) · [Español](RUBRICA-MATURIDADE.es.md)

> **Deterministic model** that maps survey answers to L0-L4 levels across **7 dimensions**, mirroring the scale of the main maturity assessment. Scored per team (no individual scores in the report, which preserves anonymity).

**Rubric version:** 1.0 · **Date:** 2026-05-08
**Implementation:** [`scripts/rubric.py`](scripts/rubric.py) · **Runner:** [`scripts/calcular_maturidade.py`](scripts/calcular_maturidade.py)

> **About the answer signals below:** quoted answers are the canonical PT-BR option strings from [`perguntas-para-forms-devs.md`](perguntas-para-forms-devs.md), which are the strings the rubric matches on. An English gloss follows in brackets; the English bank is [`perguntas-para-forms-devs.en.md`](perguntas-para-forms-devs.en.md).

---

## 🎯 Principles

1. **Deterministic**: the same answer always produces the same level. No LLM, no randomness.
2. **Auditable**: every rule is documented in this file, and the code replicates it 1:1.
3. **Conservative**: when in doubt, the level goes down (avoids inflating declared maturity).
4. **Anonymous**: computed for each respondent individually, but **only aggregates** appear in the report (mean, distribution).
5. **v1 bands**: uses the L0-L4 bands of the v1 assessment (Initial to Optimizing). Framework v2 uses other bands (0.8 wide) and level names, so compare survey and v2 results by score and through the v2 questions listed below, not by level name.

## 🧭 Scale (v1 assessment bands)

| Range | Label | Description |
|---|---|---|
| `< 0.5` | **L0 Initial** | No practice, no knowledge, no tooling |
| `[0.5, 1.5)` | **L1 Developing** | Occasional adoption, basic knowledge |
| `[1.5, 2.5)` | **L2 Defined** | Regular use, knows key concepts |
| `[2.5, 3.5)` | **L3 Managed** | Broad adoption, knows advanced concepts, measures impact |
| `≥ 3.5` | **L4 Optimizing** | Full mastery, creates primitives, continuous optimization |

> **IDs:** the survey dimensions are `DS-D2` to `DS-D8`. The `DS-` prefix keeps them apart from the v2 assessment dimensions `D1` to `D9`, which mean different things. `survey_crosswalk` in [framework.v2.json](../framework.v2.json) lists the v2 questions each survey dimension helps validate; survey results never change v2 scores.

## 📊 The 7 dimensions

| ID | Dimension | Comes from | What it measures |
|---|---|---|---|
| **DS-D2** | **Copilot Adoption** | S2 (9 q) | Frequency + breadth of modes + features + measured gain |
| **DS-D3** | **MS/GH Tooling Breadth** | S3 (7 q) | How many advanced tools (Foundry, Spaces, Coding Agent, MCP, Spec Kit) are used |
| **DS-D4** | **AI Dev Practices** | S4 (9 q) | TDD with AI, SDD, pair programming, debugging, onboarding |
| **DS-D5** | **Agent Concepts Mastery** | S5 (11 q) | Knowledge of 9 key concepts + creation of primitives + tests |
| **DS-D6** | **Instructions Maturity** | S6 (6 q) | Use of instructions files, maintenance, shared prompt library |
| **DS-D7** | **Best Practices** | S7 (9 q) | Champion, DORA/DX metrics, community, sharing |
| **DS-D8** | **Security & Governance** | S8 (13 q) | Policy, GHAS, scanners, SBOM, JIT, red-lines, audit, training |

> **Excluded from the score:** S1 (profile, only categorizes) and S9 (free text, becomes quotes).

## ⚖️ Detailed rules per dimension

### DS-D2: Copilot Adoption

| Key answer | Signals |
|---|---|
| `S2-Q1: Não tenho licença` [no license] OR `Tenho mas não uso` [have one but do not use it] | **Hard L0** |
| `S2-Q2: Nunca` [never] | **Hard L0** |
| `S2-Q2: Raramente` [rarely] | L1 |
| `S2-Q2: Diariamente` [daily] + `S2-Q5: 2+ features` + `S2-Q3: 1+ modo` [1+ mode] | **L2** |
| Above + `S2-Q3: usa Agent ou Coding Agent` [uses Agent or Coding Agent] + `S2-Q5: 4+ features` + positive gain | **L3** |
| Above + `S2-Q3: Coding Agent` + `S2-Q5: Spaces` + `S2-Q7: ganho >40%` [gain >40%] + `S2-Q5: 5+ features` | **L4** |

### DS-D3: MS/GH Tooling Breadth

Point-by-point score: `n_tools (S3-Q1) + advanced_signals (S3-Q3, Q4, Q6, Q2)`

- `n_tools` = how many tools are checked in S3-Q1 (excluding "Nenhuma" [none])
- `advanced_signals` = +1 for each:
  - Coding Agent: "Uso ativamente" [I use it actively]
  - Spaces: "Uso e crio" [I use and create them]
  - MCP: "Uso servidores" [I use servers] or "Configurei custom" [I configured custom ones]
  - Foundry used for "MCP", "multi-agent", or "agentes autônomos" [autonomous agents]

**Mapping:**

- `score ≥ 8` → **L4** (5+ tools + 3+ advanced signals)
- `score 5-7` → **L3**
- `score 3-4` → **L2**
- `score 1-2` → **L1**
- `score 0` → **L0**

### DS-D4: AI Dev Practices

Weighted sum (max ~10 points), mapped to 0-4:

| Question | Signal | Points |
|---|---|---|
| `S4-Q1` TDD with AI | "Sempre" [always] | +2 |
|  | "Frequentemente" [frequently] | +1.5 |
|  | "Não sei TDD" [I do not know TDD] | -1 |
| `S4-Q2` SDD | "Uso ativamente" [I use it actively] | +2 |
|  | "Já testei" [I have tried it] | +1 |
|  | "Nunca ouvi falar" [never heard of it] | -0.5 |
| `S4-Q3` Moments when AI is consulted (multi) | n_moments × 0.4 (cap 2.0) | up to +2 |
| `S4-Q4` Pair programmer mindset | "Trato como par" [I treat it as a pair] | +1.5 |
|  | "Às vezes" [sometimes] | +0.5 |
| `S4-Q5` Refactoring | "Toda semana" [every week] | +1 |
| `S4-Q7` Debugging with AI first | "Pergunto Copilot" [I ask Copilot] | +0.5 |
| `S4-Q8` Onboarding with AI | "Sempre" [always] | +1 |

**Mapping:** `score / 10 × 4` → rounded.

### DS-D5: Agent Concepts Mastery

3 components:

**(a) Coverage of 9 concepts** (60% of the weight): for each one, +1.0 if "uso/explico" [I use it / I can explain it], otherwise 0:

- S5-Q1 AI agent
- S5-Q2 Copilot modes
- S5-Q3 Custom agents
- S5-Q4 Skills
- S5-Q5 Prompt files
- S5-Q6 A2A
- S5-Q7 Handoffs
- S5-Q8 Subagents
- S5-Q9 Agentic DevOps personas

**(b) Primitives created (S5-Q11 multi)** (25% of the weight): n_primitives × 0.25 (cap 1.0)

**(c) Agent tests (S5-Q10)** (15% of the weight):

- "Sempre, test suite" [always, with a test suite] → +1.0
- "Frequentemente" [frequently] → +0.5
- "Não crio agents" [I do not create agents] → 0 (neutral)

**Formula:** `(coverage × 0.6 × 4) + min(n_primitivos × 0.25, 1.0) + (test_bonus × 0.36)`. Capped at 4.0.

**Minimum coverage:** if `<5` questions are answered → returns `None` (not scored).

### DS-D6: Instructions Maturity

| Question | Signal | Points |
|---|---|---|
| `S6-Q1` Files (multi) | "Nenhum" [none] or empty | **Hard L0** |
|  | 4+ types | +2 |
|  | 2-3 types | +1.5 |
|  | 1 type | +1 |
| `S6-Q2` Maintainer | "Time inteiro contribui" [the whole team contributes] | +2 |
|  | "1-2 dedicadas" [1-2 dedicated people] | +1.5 |
|  | "Ninguém mantém" [nobody maintains them] / "Não temos" [we do not have them] | -1 |
| `S6-Q3` Update freq | "Toda semana" [every week] | +1 |
|  | "Mensalmente" [monthly] | +0.7 |
|  | "Nunca" [never] | -0.5 |
| `S6-Q4` Content (multi) | n_types × 0.3 (cap 2.0) | up to +2 |
| `S6-Q5` Library shared | "Copilot Space" / "repo dedicado" [dedicated repo] | +1 |
|  | "Não compartilhamos" [we do not share] | -0.5 |

**Mapping:** `score / 9 × 4`.

### DS-D7: Best Practices

| Question | Signal | Points |
|---|---|---|
| `S7-Q1` Learning sources (multi) | n_sources × 0.3 (cap 1.5) | up to +1.5 |
| `S7-Q2` Champion | "Sim, eu sou" [yes, it is me] / "outra pessoa" [someone else] | +1.5 |
|  | "Cada um se vira" [everyone figures it out alone] | -0.5 |
| `S7-Q3` Internal channel | ">5 mensagens/sem" [>5 messages/week] | +1 |
|  | "pouco ativo" [not very active] | +0.5 |
| `S7-Q4` Metrics (multi) | DORA/DX/SPACE/Copilot count × 0.5 (cap 2.0) | up to +2 |
|  | "Não medimos" [we do not measure] | -1 |
| `S7-Q5` Iterations | "1ª tentativa" [1st attempt] / "2-3" | +1 |
|  | "7+" | -0.5 |
| `S7-Q9` Shares prompts | "Frequentemente" [frequently] | +1 |
|  | "Nunca" [never] | -0.5 |

**Mapping:** `score / 8 × 4`.

### DS-D8: Security & Governance (CRITICAL, conservative)

Largest number of rules + penalties for red flags:

| Question | Signal | Points |
|---|---|---|
| `S8-Q1` Policy + `S8-Q4` (Sec tools) | "Não temos política" [we have no policy] + "Nenhuma ferramenta" [no tools] | **Hard L0** |
| `S8-Q1` | "formal e clara" [formal and clear] | +2 |
|  | "pouco clara" [not very clear] | +1 |
|  | "informal" | +0.5 |
| `S8-Q2` Knows sensitive data | "Sei claramente" [I know clearly] | +1 |
| `S8-Q3` Forbidden (multi) | n_types × 0.2 (cap 1.0) | up to +1 |
|  | "Nenhuma restrição" [no restriction] | -1 |
| `S8-Q4` Sec tools (multi) | n_tools × 0.3 (cap 2.0) | up to +2 |
| `S8-Q5` Code scan on PR | "gate obrigatório" [mandatory gate] | +1 |
| `S8-Q6` SBOM | "automatizado" [automated] | +0.5 |
| `S8-Q7` Formal AI review | "obrigatório humano + scanner" [mandatory human + scanner] | +1 |
| `S8-Q8` Agent red-lines | "Sempre" [always] | +1 |
| `S8-Q9` JIT permissions | "JIT obrigatório" [mandatory JIT] | +1 |
| `S8-Q10` DLP | "bloqueia" [blocks] | +0.5 |
| `S8-Q11` Audit | "ativos e revisados" [active and reviewed] | +0.5 |
| `S8-Q12` Training | "obrigatório anual" [mandatory annual] | +0.5 |

**Mapping:** `score / 12 × 4`.

## 🧮 Respondent overall score

```text
overall = mean(DS-D2..DS-D8)  # only dimensions with score != None
```

## 🧮 Team aggregation

```text
team_score(D) = mean(D across all respondents)  # ignores None
team_overall  = mean(overall of all respondents)
distribution(D) = % of respondents in each L0-L4
```

## 📤 Output

`saida/maturidade-developer-survey-<DATE>.json`:

```jsonc
{
  "metadata": {
    "computed_at": "2026-05-08T12:00:00Z",
    "n_respondents": 12,
    "rubric_version": "1.0 (deterministic)",
    "anonymous": true,
    "scope": "team aggregate (no individual scores in output)"
  },
  "team_overall": {
    "score": 2.22,
    "label": "L2: Definido",
    "respondents_with_overall": 12
  },
  "dimensions": {
    "DS-D2": {
      "name": "Copilot Adoption",
      "team_score": 0.80,
      "label": "L1: Em Desenvolvimento",
      "respondents_with_score": 12,
      "distribution_count": {"L0": 5, "L1": 5, "L2": 2, "L3": 0, "L4": 0},
      "distribution_pct": {"L0": 41.7, "L1": 41.7, "L2": 16.7, "L3": 0, "L4": 0}
    },
    "DS-D3": {...}, "DS-D4": {...}, "DS-D5": {...},
    "DS-D6": {...}, "DS-D7": {...}, "DS-D8": {...}
  },
  "ranking": {
    "top": [["DS-D7", "Best Practices", 2.91], ...],
    "bottom": [["DS-D2", "Copilot Adoption", 0.80], ...]
  }
}
```

The sample above shows the PT-BR labels. Human-readable output (the insights report) is now generated in **English by default**, with PT-BR and ES available via `--lang pt-br` and `--lang es` on the scripts.

## 🔄 How to run

### Via skill in Copilot Chat

```text
/insights-developer-survey   # invokes the script automatically
```

### Via CLI

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output:
#   - saida/maturidade-developer-survey-DATE.json
#   - summary on stdout (overall + table per dimension + ranking)
```

## 🔗 Cross-reference with the main assessment

Individual maturity (from the survey) **feeds and validates** the capabilities of the organizational assessment:

| Survey dimension | Assessment capability | What to validate |
|---|---|---|
| **DS-D2** Copilot Adoption | `P1-C1` AI Coding Assistants | Declared score vs. real adoption declared by developers |
| **DS-D3** MS/GH Tooling | `P3-C3` AI Applications + `P3-C5` Agentic Apps | Technical sophistication in AI |
| **DS-D4** AI Dev Practices | `P1-C2` DevEx + `P1-C8` Productivity Metrics | Structured practices |
| **DS-D5** Agent Concepts | `P3-C5` Agentic Apps | Advanced knowledge |
| **DS-D6** Instructions | `P1-C7` Automated documentation | Maintenance of AI context |
| **DS-D7** Best Practices | `P1-C5` Onboarding + `P1-C8` Metrics | Adoption culture |
| **DS-D8** Security & Governance | `P2-C4` DevSecOps + `P2-C10` Supply Chain | Real governance |

> 💡 **Classic pattern:** leadership rates P1-C1 as L3, but survey DS-D2 shows L1 (60% of developers rarely use it) → **dissonance** between strategy and practice. The `/insights-developer-survey` skill highlights this in section 12 of the report.

## 📊 Rubric calibration and review

This is **version 1.0**. Review it quarterly based on:

- Cases where the score seems under- or over-estimated (calibrate weights)
- Ecosystem changes (e.g., Copilot launches a new mode → add it to S2-Q3 + update DS-D2)
- Respondent feedback ("this question was ambiguous")

**How to propose a change:**

1. Edit `scripts/rubric.py` with the updated rule
2. Document the reason in this file
3. Increment `RUBRIC_VERSION` and rerun with previous data to compare

## 🔐 Anonymity policy in scoring

The rubric computes a score FOR EACH respondent individually, but the JSON output and the report:

- ✅ Show **team aggregate scores** (mean, % distribution)
- ✅ Show **distribution by level** (% of developers in each L0-L4)
- ❌ Do NOT show a score per respondent_id
- ❌ Do NOT show role/profile together with a score (aggregation by role only if ≥3 developers share the same role)

This preserves the survey's anonymity pact while still producing useful insights for the team.
