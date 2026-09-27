# AI Maturity Assessment Kit — General Instructions

> Loaded automatically into every Copilot prompt. Defines the **context, scoring algorithm and vocabulary** used by this self-service kit.

## What this repo is

A self-contained kit with **THREE complementary surveys** to run with a client **before** the web platform is ready:

1. **AI Maturity Assessment** (158 questions, Likert L0-L4, organizational) — main flow with 5 PDFs output
2. **Developer Survey** (75 questions, behavioral, ANONYMOUS, individual) — feeds the assessment with developer voice + computes maturity per dimension D2-D8 (deterministic rubric)
3. **Learning & Growth Survey** (32 questions, IDENTIFIED with name+email) — generates personalized capacitation roadmap: workshops, cohorts, Champions Network, mentor↔mentee pairs

Contains:
- **1 concierge agent** (`@ai-maturity-assistant` in `.github/agents/`) — guided experience for new clients (offers 4 paths: assessment / survey-devs / learning / all three)
- **1 orchestrator prompt** (`/pipeline-completo` in `.github/prompts/`) — runs the maturity pipeline end-to-end
- **12 custom skills** (under `.github/skills/`) — 1 high-level orchestrator + 6 assessment pipeline skills + 1 wizard + 2 survey-devs + 2 survey-learning

**Recommend the agent for first-time clients**: `@ai-maturity-assistant` reads workspace state and guides them step-by-step. Use direct skill commands for power users.

## Critical files

| File | Role |
|---|---|
| `framework.json` | Immutable — 3 pillars × ~28 capabilities × 158 questions + weights + `cap → strategies[]` mapping + S1–S7 + technologies |
| `respostas.json` | **Client input** — fills `level` (0–4) and `evidence` per question. Not tracked in git: create it with `make init` (copies `respostas.json.example`) or `/importar-respostas-excel` |
| `scripts/assessment_engine.py` | Deterministic scoring engine behind `/calcular-scores`, `/gap-analysis`, `/recomendar-estrategias` (`python3 scripts/assessment_engine.py all`); golden tests in `scripts/test_assessment_engine.py` |
| `scripts/import_forms_excel.py` / `scripts/fill_workbook.py` | Deterministic importer (`/importar-respostas-excel`) and auditable workbook filler (`/preencher-planilha`); tests in `scripts/test_*.py` (`make test`) |
| `respostas-forms.xlsx` (optional) | Multi-respondent Excel from Microsoft Forms / SharePoint |
| `implementation-guide-inputs.json` (optional) | Output of `/wizard-implementacao` — populates Part 4 of the PDF |
| `referencia/pontuacao-e-calculo.xlsx` | Auditable workbook template; populated by `preencher-planilha` skill |
| `referencia/pontuacao-e-calculo.md` | Official algorithm reference (mirrors `app/backend/src/scoring.rs`; PT-BR copy in `.pt-br.md`) |
| `referencia/exemplo-saida/` | 5 reference PDFs + JSONs from `respostas.json.example` (Cliente Exemplo S.A.) |
| `relatorios/templates/*.html.j2` | 4 official Jinja2 templates (mirror `app/src/report-service/templates/`) |
| `relatorios/i18n/{en,es,pt-br}.json` | String catalogs |
| `relatorios/sample_payload.json` | Schema reference + base structure for payload merge |
| `relatorios/scripts/build_payload_and_render.py` | Main script invoked by `/gerar-relatorio` — merges sample + client data → renders 5 PDFs |
| `relatorios/scripts/render_reports.py` | Lower-level Jinja2 + WeasyPrint renderer |
| `wizard/implementation-guide-wizard.html` | Standalone HTML wizard (9 steps for Part 4) |
| `wizard/implementation-guide-inputs.template.json` | Pre-filled JSON template (alternative to HTML wizard) |
| `saida/` | Output folder — every generated artifact MUST go here |

## Output language convention

- **Client-facing output defaults to English**: reports, slide outlines, log messages, error summaries, agent menus, and handoff labels.
- **PT-BR and ES on request**: PDFs follow `respostas.json::metadata.language` (`"en"` default, `"pt-BR"`, `"es"`); survey reports (`gerar_insights.py`, `gerar_plano_capacitacao.py`) and `auto_fill_from_plano.py` accept `--lang pt-br`. In chat, reply in the user's language when they write in Portuguese or Spanish.
- **Docs language**: every human-facing doc `X.md` (and the calculator/wizard HTMLs) is English; the Portuguese version lives next to it as `X.pt-br.md` / `X.pt-br.html`. ES package docs live in `kit-es/`. Keep both versions in sync when editing.
- **Stays Portuguese on purpose**: canonical question wording in `framework.json`, Forms answer options (`L0 — Inicial` ... `NA — Não sei`), rubric match strings, IDs, file and folder names (`saida/`, `respostas.json`), and skill names.
- Technical KPI strings can remain in English (universal terms like "MTTR", "lead time", "% adoption").

## Visual identity & branding (paulasilva-ms)

This kit is signed under the **Microsoft identity** of Paula Silva, Software Global Black Belt. Visual artifacts (HTMLs) follow the [paulasilva-ms Design System](../../../../.github/skills/paulasilva-ms/) v1.7.0.

**When generating new HTML or visual content for this kit:**
- Load `referencia/branding/tokens-paulasilva-ms.css` (relative path)
- Load Inter + JetBrains Mono fonts via Google Fonts CDN
- Use MS 4-color palette tokens: `--c-blue-500` (#00A4EF), `--c-green-500` (#7FBA00), `--c-yellow-500` (#FFB900), `--c-red-500` (#F25022)
- Add `<div class="deck-brand">` chrome bar with the 22px logo SVG
- Sign with: **Paula Silva | Software Global Black Belt** + paulasilva@microsoft.com (single channel, no socials)
- See `referencia/branding/IDENTITY.md` for canonical strings + logo SVG markup

**Voice rules** (see `referencia/branding/VOICE.md`):
- ❌ NO em-dashes (`—`). Use comma, period, colon, or semicolon.
- ❌ NO en-dashes (`–`) in ranges. Use hyphen with spaces or "to" / "a".
- ❌ NO banned vocabulary (revolutionary, world-class, leverage as verb, etc.)
- ✅ Oxford comma, single space after period, pedagogical without condescension

**What this branding does NOT cover:**
- The 5 Jinja2 PDF templates (`relatorios/templates/*.html.j2` + `_print.css`) — these mirror the production platform CSS and stay unchanged.
- Markdown documentation files — they follow standard markdown without special branding.
- Output language of skills (see Output language convention).

## Scoring algorithm (summary)

Authoritative reference: `referencia/pontuacao-e-calculo.md`. The `/calcular-scores` skill contains executable pseudocode. Keep this section short so the automatic prompt context stays lean.

### Layer 1 — Capability score

```
capability_score = Σ(level_q × weight_q) / Σ(weight_q)
                   ↑ only answered questions (level != null)
```

### Layer 2 — Pillar score

```
pillar_score = Σ(capability_score × cap_weight) / Σ(cap_weight)
               ↑ only capabilities with score (not None)
```

### Layer 3 — Overall score

```
overall_score = Σ(capability_score × cap_weight) / Σ(cap_weight)
                ↑ OVER ALL 28 capabilities (NOT mean of pillars)
```

### Score → label mapping

| Range | Label |
|---|---|
| `< 0.5` | L0 — Inicial |
| `[0.5, 1.5)` | L1 — Em Desenvolvimento |
| `[1.5, 2.5)` | L2 — Definido |
| `[2.5, 3.5)` | L3 — Gerenciado |
| `≥ 3.5` | L4 — Otimizando |

### Coverage threshold

| Answered | Status |
|---|---|
| ≥ 40 | OK |
| 25–39 | WARNING (preliminary) |
| < 25 | BLOCKED (refused) |

### Gap analysis

```
gap_size       = max(0, target_level − current_score)
priority_score = cap_weight × gap_size
```

| `priority_score` | Priority |
|---|---|
| ≥ 2.4 | P0 — Crítico (30 days) |
| ≥ 1.6 | P1 — Alto (next quarter) |
| ≥ 0.9 | P2 — Médio (semester) |
| < 0.9 | P3 — Baixo (monitor) |

`target_level` = `respostas.json::target_overrides[cap_id]` if present, else **3.0** (default L3).

## The 7 strategies (S1–S7)

| ID | Name | Focus |
|---|---|---|
| **S1** | GitHub Migration | Consolidate SCM + collaboration on GitHub Enterprise |
| **S2** | Foundry + SRE | Platform engineering + SRE practices with Azure Foundry |
| **S3** | App Modernization | Modernize legacy apps to cloud-native |
| **S4** | AI Applications | Build AI features with Azure AI |
| **S5** | GitHub Copilot Acceleration | Accelerate dev productivity with Copilot |
| **S6** | Agentic Activation | Enable autonomous agents in apps/workflows |
| **S7** | Security & Governance | Strengthen security and supply-chain governance |

Each capability has `strategies: ["S1", "S5", ...]` in `framework.json`. Use this to map gaps → priority strategies and specific technologies (`technologies_per_strategy`).

## Developer Survey dimensions (D2-D8)

The Developer Survey computes behavioral maturity in 7 dimensions. D1 is profile metadata and is not scored.

| ID | Dimension | Main signal | Related assessment area |
|---|---|---|---|
| **D2** | Copilot Adoption | License, frequency, modes, features, perceived gain | P1-C1, P1-C8, S5 |
| **D3** | MS/GH Tooling Breadth | Foundry, Spaces, Coding Agent, MCP, Spec Kit, GHAS | S1, S2, S4, S7 |
| **D4** | AI Dev Practices | TDD with AI, SDD, pair programming, debugging, onboarding | P1-C5, P2-C1 |
| **D5** | Agent Concepts Mastery | Agents, MCP, A2A, handoffs, subagents, custom agents | P3-C5, S6 |
| **D6** | Instructions Maturity | `copilot-instructions.md`, prompt libraries, Spaces, memory | P1-C3, P1-C5 |
| **D7** | Best Practices | Champions, DORA/DX/SPACE metrics, community, trust | P1-C8, P2-C8 |
| **D8** | Security & Governance | Policy, GHAS, CodeQL, SBOM, DLP, audit, red-lines | P2-C4, P2-C10, S7 |

See `survey-devs/RUBRICA-MATURIDADE.md` for the deterministic L0-L4 rubric.

## Output conventions

- **All generated outputs go in `saida/`** except persistent inputs such as `respostas.json`, `survey-devs/respostas-devs.json`, `survey-learning/respostas-learning.json`, and `implementation-guide-inputs.json`.
- **DO NOT modify** `framework.json`, `referencia/`, or files in `formularios/` and `coleta/`.
- **DO NOT modify** `respostas.json` except to fill `level` and `evidence` when explicitly asked, or via the `importar-respostas-excel` skill.
- Client-facing output text defaults to **English** unless `metadata.language` (or `--lang`) selects PT-BR or ES.
- Never invent data: if a question wasn't answered, declare "sem resposta" — don't guess.

## Idempotency

Use two output patterns:

- **Canonical pipeline outputs overwrite the same filename:** `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`, `saida/payload.json`, and the 5 final PDFs.
- **Audit/time-series outputs keep a date in the filename:** populated spreadsheets, import logs, developer survey insights, maturity JSONs, and capacitation plans.

Rerunning with the same inputs should preserve the same computed values. Timestamps in metadata may change.

## Smoke test (for contributors)

Run before opening a PR that touches the pipeline:

```bash
make test         # engine, importer and workbook tests
make smoke        # assessment pipeline without full PDF dependency checks
make smoke-cross  # assessment + developer survey + learning survey enrichment
```

Recommended additional validation for localization or packaging changes:

```bash
python3 -m json.tool docs/content.json >/dev/null
python3 scripts/build_language_kits.py --out dist-test --clean
```

## When the client asks "how do I…?"

Direct them to `README.md` (root) or `GUIA-PASSO-A-PASSO.md` (detailed); Portuguese readers use the `.pt-br.md` versions. For algorithm questions, point to `referencia/pontuacao-e-calculo.md`. For Microsoft Forms collection, point to `coleta/INSTRUCOES-FORMS.md`. For personalizing the Implementation Guide (Part 4 PDF), point to `wizard/` or invoke `/wizard-implementacao`.

## Available skills (12) + 1 prompt + 1 agent

### Maturity Assessment (main flow)

| Command | Type | Purpose |
|---|---|---|
| `@ai-maturity-assistant` | **agent** | Concierge — reads state, guides client end-to-end, invokes skills via handoffs (English by default, mirrors PT-BR/ES users) |
| `/ai-maturity-reports` | skill (orchestrator) | High-level wrapper that produces all 5 PDFs + XLSX. Mirror of the global skill `~/.github/skills/ai-maturity-reports/`. Use when client wants the full bundle |
| `/pipeline-completo` | prompt | Orchestrates 6 steps end-to-end (auto-detects Excel + wizard) |
| `/importar-respostas-excel` | skill | Microsoft Forms `.xlsx` → `respostas.json` (multi-respondent mean aggregation; floats are preserved) |
| `/preencher-planilha` | skill | `respostas.json` → `saida/pontuacao-preenchida-<DATE>.xlsx` |
| `/calcular-scores` | skill | `respostas.json` → `saida/scores.json` (SUMPRODUCT 3 layers) |
| `/gap-analysis` | skill | `saida/scores.json` → `saida/gaps.json` (P0/P1/P2/P3 priorities) |
| `/recomendar-estrategias` | skill | `saida/gaps.json` → `saida/recomendacoes.json` (S1–S7 ranked + technologies) |
| `/wizard-implementacao` | skill | 9-step wizard for Part 4 (3 modes: HTML / JSON / chat) → `implementation-guide-inputs.json` |
| `/gerar-relatorio` | skill | All inputs → invokes `build_payload_and_render.py` → **5 PDFs** in `saida/` |

### Developer Survey (anonymous, behavioral)

| Command | Type | Purpose |
|---|---|---|
| `/importar-survey-devs` | skill | Microsoft Forms `respostas-survey-devs.xlsx` → `survey-devs/respostas-devs.json` (75 questions × N anonymous respondents) |
| `/insights-developer-survey` | skill | Invokes `calcular_maturidade.py` (deterministic rubric → maturity scores per D2-D8) + generates `saida/insights-developer-survey-<DATE>.md` (aggregated insights + governance score + recommendations linked to maturity capabilities) |

### Learning & Growth Survey (identified, capacitation)

| Command | Type | Purpose |
|---|---|---|
| `/importar-survey-learning` | skill | Microsoft Forms `respostas-survey-learning.xlsx` → `survey-learning/respostas-learning.json` (32 questions × N IDENTIFIED respondents with name+email) |
| `/plano-capacitacao` | skill | `survey-learning/respostas-learning.json` → `saida/plano-capacitacao-<DATE>.md` (top 10 topics demanded, cohorts per dimension, Champions Network, mentor↔mentee pairs, calendar of workshops, barriers to remove) |

### When to use which

- **Maturity Assessment** (org level): organizational baseline, leadership-driven, produces 5 executive PDFs
- **Developer Survey** (anonymous): behavioral baseline, surfaces real adoption + gaps. Outputs feed `/wizard-implementacao` and validate maturity capability scores
- **Learning Survey** (identified): aspirational + capacitation roadmap. Generates concrete training plan with attendee lists. Output feeds `/wizard-implementacao::training_plan + adkar_notes + quick_wins`
- **All three together** (recommended for serious consulting): run in this order: survey-devs (anonymous, behavioral) → learning survey (identified aspirational) → assessment (leadership informed) → wizard consolidates everything

## Multi-respondent aggregation

When `respostas-forms.xlsx` contains multiple respondents, `/importar-respostas-excel` aggregates levels by **simple average per question** across respondents who answered that question. Do not round; a question may have `level: 2.5`. Evidence is concatenated with `[respondent name]:` prefix. Scoring accepts numeric levels in the inclusive range 0-4.
