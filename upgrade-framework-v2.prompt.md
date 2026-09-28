---
description: Upgrade the AI Maturity Client Kit from framework v1 (3 pillars, 28 capabilities, 158 questions) to v2 (9 AI-SDLC dimensions, 61 questions) across data, collection, import, scoring, reports, skills, docs and translations.
agent: agent
---

# Upgrade the AI Maturity Client Kit to framework v2

🌐 English · [Português (Brasil)](upgrade-framework-v2.prompt.pt-br.md) · [Español](upgrade-framework-v2.prompt.es.md)

> **Status (2026-09-28): executed** on branch `feature/framework-v2`. The spec is v2.0.1 ([coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md)); decisions D-1 to D-8 and the rest of the changes are listed in [CHANGELOG.md](CHANGELOG.md). Keep this file as the record of the plan; run it again only for a new framework major version.

## Role

You are a senior engineer and technical writer upgrading the **AI Maturity Client Kit** repository to framework v2. Work carefully, in phases, with validation after each phase. Ask before any destructive or ambiguous action.

## Inputs

| Input | Location |
| --- | --- |
| v2 specification (source of truth) | `coleta/AI-Maturity-Form-Questions_v2.md` (v2.0.1) |
| Framework repository | this repository (branch `develop`) |
| Remote | `paulasilvatech/ai-maturity-client-kit` |

Read the whole v2 specification before changing anything. Treat these parts as fixed unless you flag a problem and I approve a change: question IDs and wording, the answer scale and its `L0`-`L4`/`NA` prefixes, the `Evidence (<ID>)` label pattern, the calibration anchors, the scoring rules in section 8, the v1→v2 traceability in section 9, and the references.

The working tree already has unrelated uncommitted changes (`.DS_Store` files, `docs/styles.css`, a deleted `scripts/__pycache__/*.pyc`). Do not stage, commit, revert or edit them.

## What v2 changes (summary)

- 9 scored dimensions (D1-D9) with 61 questions replace 3 pillars / 28 capabilities / 158 questions.
- New unscored respondent profile section: `R-Q1`-`R-Q5` (`R-Q3` is multiple choice).
- Redefined scale: L0 Not started, L1 Exploring (≤25%), L2 Adopting (26-50%), L3 Scaling (51-90%), L4 AI-native (>90%). Same prefixes as v1.
- Per-question L3/L4 anchors, evidence examples, basis citations and v1 lineage.
- Scoring: dimension score = mean of question scores (NA excluded); overall = mean of dimensions (equal weights by default); level bands of 0.8 width; low-confidence flag (>30% NA); amplification-risk flag (D5, D6 or D8 at least one band below overall); perception-gap flag (executives vs hands-on engineers per `R-Q1`); evidence coverage.
- Traceability: in v2.0.1, 99 v1 questions are consolidated into v2 and 59 retired from the core assessment (partition of all 158, no overlaps). The 2.0.0 draft had 97 and 61.
- 58 references, including 14 arXiv pre-prints from 2026 and the 2026 Management Science publication of Cui et al.

## Repository map (verified 2026-09-25)

| Area | Files | Expected change |
| --- | --- | --- |
| Framework data | `framework.json` (v1.0.0: `level_names`, `strategies`, `technologies_per_strategy`, `pillars` → `capabilities` → `questions` with `id`, `weight`, `pe`, `audience`, `kpi`) | Add v2 data model (see Decision D-1) |
| Response data | `respostas.json`, `respostas.json.example` (`metadata`, `target_overrides` keyed by capability, `responses` keyed by question ID with `level`, `evidence`, `text_*`) | v2 example keyed by `D#-Q#`, profile answers, `framework_version` |
| Implementation inputs | `implementation-guide-inputs.json`, `wizard/implementation-guide-inputs.template.json`, `wizard/implementation-guide-wizard.html`, `wizard/scripts/auto_fill_from_plano.py` | Map to dimensions |
| Collection (PT/EN/ES) | `coleta/perguntas-para-forms{,.en,.es}.md`, `coleta/INSTRUCOES-FORMS.md`, `coleta/README.md`, `coleta/template-export-forms.xlsx`, `kit-en/FORMS-INSTRUCTIONS.md`, `kit-es/INSTRUCCIONES-FORMS.md` | Regenerate from v2 data; 10 sections, 127 elements |
| HTML forms | `formularios/P1-*.html`, `formularios/P2-*.html`, `formularios/P3-*.html`, `formularios/README.md` | Replace with v2 forms (profile + D1-D9) |
| Scoring reference | `referencia/pontuacao-e-calculo.md`, `referencia/pontuacao-e-calculo.xlsx`, `referencia/calculadora-pontuacao.html` | v2 rules and flags (current engine: weighted capabilities, overall = SUMPRODUCT over all capabilities, weights 1.0 in [0.5, 2.0], `priority_score = peso_capability × gap_size`) |
| Pillar reference docs | `referencia/P1-*.md`, `referencia/P2-*.md`, `referencia/P3-*.md`, `referencia/README.md` | Per-dimension reference docs with research basis |
| Example outputs | `referencia/exemplo-saida/**` (scores, gaps, recommendations, payload, PDFs, XLSX, EN/ES folders) | Regenerate from a v2 mock; never edit by hand |
| Reports | `relatorios/scripts/{build_payload_and_render,render_reports,render_smoke,branding}.py`, `relatorios/templates/*.j2`, `relatorios/templates/_print.css`, `relatorios/i18n/{pt-br,en,es}.json`, `relatorios/sample_payload.json` | Dimensions, flags, persona view, evidence coverage, references |
| Copilot customization | `.github/copilot-instructions.md`, `.github/agents/ai-maturity-assistant.agent.md`, `.github/prompts/pipeline-completo.prompt.md`, `.github/skills/*/SKILL.md` (12 skills: `importar-respostas-excel`, `calcular-scores`, `gap-analysis`, `recomendar-estrategias`, `gerar-relatorio`, `ai-maturity-reports`, `preencher-planilha`, `wizard-implementacao`, `importar-survey-devs`, `insights-developer-survey`, `importar-survey-learning`, `plano-capacitacao`) | Update every pillar/capability reference and ID pattern |
| Companion surveys | `survey-devs/**` (incl. `RUBRICA-MATURIDADE.md`, `scripts/rubric.py`), `survey-learning/**` | Cross-reference only; avoid duplicate questions (see D-6) |
| Docs and site | `README.md`, `GUIA-PASSO-A-PASSO.md`, `kit-en/{README,STEP-BY-STEP}.md`, `kit-es/{README,PASO-A-PASO}.md`, `docs/{content.json,index.html,en/index.html,es/index.html,app.js,README.md}` | v2 structure, counts and flow |
| Tooling | `Makefile` (`smoke`, `smoke-cross`, `validate-docs`, `build-kits`, `pipeline`), `scripts/{smoke_test,check_language_coverage,build_language_kits}.py`, `.github/workflows/{pages,release-zips}.yml` | Extend checks for v2 |

## Additional requirements (from the 2026-09 audit)

These were missing from the first version of this plan and are part of the upgrade:

- **No sample content in client reports (C1).** Any report section without client data is omitted or marked "to fill", never filled from sample payloads.
- **Deterministic scoring (C2).** Import, scores, gaps and strategies run in Python scripts with tests; skills call the scripts instead of computing in the chat.
- **Question IDs in Forms titles (C3).** Every Forms question title starts with its ID (`D4-Q3: ...`, `R-Q1: ...`).
- **No ID collisions (C4).** Developer Survey dimensions are named `DS-D2` to `DS-D8`; `D1` to `D9` are reserved for the assessment.
- **One band rule per version (C5).** v2 uses half-open 0.8-wide bands with no gaps; the companion survey keeps the v1 bands and is compared by score.
- **Privacy (C8).** Forms carry a consent and retention notice; profile answers are personal data; outputs stay out of git (`respostas.json` and `implementation-guide-inputs.json` are not tracked).
- **Minimum sample per persona.** Persona and perception-gap results need at least 3 respondents per group; smaller groups are marked as low sample.

## Non-negotiable rules

1. **Factual integrity.** Do not invent metrics, benchmarks, percentages or research findings. Every data claim in docs, skills or reports must come from the v2 references (with the same link). If you need a new source, verify it on the web first, add it to the references, and tell me.
2. **Backward compatibility.** v1 response files and the existing v1 example must still import, score and render. Detect the version from `framework_version` in `respostas.json` metadata (default to v1 when absent). Archive v1 content; do not delete it.
3. **Scale and IDs.** Keep the `L0`-`L4`/`NA` option prefixes and the `Evidence (<ID>)` label pattern exactly. IDs are `D#-Q#` (scored) and `R-Q#` (profile).
4. **Single source of truth.** Generate question lists, forms, translations and templates from the v2 data file with scripts. Do not hand-maintain three language copies.
5. **Trilingual parity.** PT-BR, EN and ES must have the same questions, anchors and options. Keep the English wording from the spec as canonical; translate PT-BR and ES faithfully; `scripts/check_language_coverage.py` must pass.
6. **Branding.** Follow `referencia/branding/` (IDENTITY, VOICE, tokens). In Microsoft-facing material use the official Microsoft four-square logo and the title "Global Developer Solutions Advisor"; never the personal `</>` logo.
7. **Git safety.** Work on a new branch `feature/framework-v2` created from `develop`. Commit per phase with clear messages. Do not push, force-push, rewrite history or delete branches. Ask before deleting or moving any tracked file.
8. **Generated outputs.** Regenerate PDFs, XLSX and JSON examples with the repo scripts; never edit generated artifacts by hand.
9. **Python style.** PEP 8, type hints where the file already uses them, lines ≤ 79 characters, no new dependencies without asking.

## Phase 0: Discovery and plan (stop for approval)

1. Read the v2 spec, `framework.json`, `respostas.json.example`, `referencia/pontuacao-e-calculo.md`, every `SKILL.md`, the agent file, the pipeline prompt, `Makefile` and the report scripts.
2. Build an impact inventory: grep for `P[0-9]-C[0-9]+-Q[0-9]+`, `P1`/`P2`/`P3`, `pillar`/`pilar`, `capabilit`, `158`, `28 capabilities`, `3 pillars`, level names (`Inicial`, `Em Desenvolvimento`, `Definido`, `Gerenciado`, `Otimizando`). List each file with the change it needs.
3. Present the plan and my open decisions below, each with your recommendation and trade-offs. **Wait for my answers before Phase 1.**

Open decisions:

| ID | Decision | Recommended default |
| --- | --- | --- |
| D-1 | Data model: extend `framework.json` or add `framework.v2.json` | Add `framework.v2.json` (version 2.0.0) and a loader that picks v1/v2 by `framework_version` |
| D-2 | Scoring engine | Treat each dimension as the scoring unit (weight 1.0, allowed range [0.5, 2.0]); question weights 1.0; overall = weighted mean of dimensions, which equals the spec's equal weights by default; keep `priority_score = weight × gap` per dimension |
| D-3 | `strategies` and `technologies_per_strategy` mapping | Remap each of the 7 strategies to dimensions; show me the mapping table before writing it |
| D-4 | Question `audience` values | Derive from `R-Q1` personas and the existing audience vocabulary; show the mapping |
| D-5 | `pe` field | Explain its current meaning from the code; propose v2 values or drop it |
| D-6 | Overlap with `survey-devs` and `survey-learning` | Cross-reference (for example D2, D5-Q6, D9-Q4) instead of duplicating questions |
| D-7 | v1 archive layout | Move v1 artifacts under `v1/` paths (for example `coleta/v1/`, `formularios/v1/`) and keep links working |
| D-8 | Level names in PT-BR/ES | Propose translations for Not started / Exploring / Adopting / Scaling / AI-native |

## Phase 1: Data model

- Create `framework.v2.json` with: `version`, `level_names` (EN/PT-BR/ES), `level_bands`, `coverage_bands`, `dimensions` (id, names in 3 languages, weight, strategies, questions), `profile_questions` (options in 3 languages, `multi` flag for `R-Q3`), `references` (1-58 with URL), `traceability` (v1 ID → v2 ID or `retired` with reason).
- Each question: `id`, `weight`, `audience`, `kpi`, `text` (en/pt-br/es), `anchors.l3`, `anchors.l4` (plus `l1_l2` for D4-Q1), `evidence_examples`, `basis` (reference numbers), `v1_lineage`.
- Add a JSON Schema (`framework.v2.schema.json`) and a validator script.
- Acceptance: 61 scored questions (D1 7, D2 6, D3 6, D4 8, D5 7, D6 7, D7 6, D8 7, D9 7); 5 profile questions; unique IDs; every `basis` number exists in `references`; traceability covers all 158 v1 IDs exactly once (99 consolidated, 59 retired in v2.0.1).

## Phase 2: Collection

- Write a generator that produces `coleta/perguntas-para-forms{,.en,.es}.md` from `framework.v2.json`, following the spec's layout (Section 0 profile, then D1-D9, anchors in the question subtitle, evidence field per question).
- Update Forms instructions in PT/EN/ES: 10 sections, 127 elements, the six options in order, respondent guidance (≥3 respondents per persona).
- Update `coleta/template-export-forms.xlsx` to the v2 export shape (profile columns, `D#-Q#` answer columns, `Evidence (D#-Q#)` columns).
- Replace `formularios/*.html` with v2 forms; keep v1 under the archive path from D-7.
- Create a v2 `respostas.json.example` and a realistic multi-persona mock for testing. Label all mock data as illustrative.

## Phase 3: Import and scoring

- `importar-respostas-excel`: detect v1 vs v2 by column IDs; parse `D#-Q#` and `R-Q#`; support `R-Q3` multi-select; map option prefixes to 0-4/null; aggregate by respondent and by persona; write `framework_version` into `respostas.json`.
- `calcular-scores` plus `referencia/pontuacao-e-calculo.{md,xlsx}` and `calculadora-pontuacao.html`: implement section 8 of the spec (dimension scores, overall, bands, low-confidence, amplification-risk and perception-gap flags, evidence coverage, per-persona scores). Keep the v1 path working.
- `gap-analysis` and `recomendar-estrategias`: work per dimension; recommendations start from the lowest-scoring questions and quote their L3 anchors; recommendations must cite spec references, not invented benchmarks.

## Phase 4: Reports

- Update `build_payload_and_render.py`, templates and i18n files for dimensions, flags, persona heatmap (dimensions × personas), evidence coverage and a references appendix.
- Replace the per-pillar roadmap template with a per-dimension (or grouped) template; propose the grouping before building it.
- Regenerate `relatorios/sample_payload.json` and all of `referencia/exemplo-saida/**` (PT/EN/ES) from the v2 mock. Keep the v1 example under the archive path.

## Phase 5: Copilot customization and docs

- Update `.github/copilot-instructions.md`, the agent, `pipeline-completo.prompt.md` and all 12 skills. Follow the existing pattern: lean agent with the workflow, domain knowledge in the skills.
- Update `wizard-implementacao` and the wizard inputs; link `plano-capacitacao` to D2; make `insights-developer-survey` cross-reference D2/D5/D9 instead of duplicating.
- Replace `referencia/P1..P3-*.md` with per-dimension reference docs that include the "why it matters" text, anchors and research basis from the spec.
- Update `README.md`, `GUIA-PASSO-A-PASSO.md`, `kit-en/*`, `kit-es/*`, and the docs site (`docs/content.json` and the three `index.html`) with v2 counts and flow. Add a changelog entry (ask where if there is no CHANGELOG).

## Phase 6: Validation (must all pass)

1. `make smoke`, `make smoke-cross`, `make validate-docs`, `make build-kits`.
2. `python3 scripts/check_language_coverage.py` with zero gaps across PT-BR/EN/ES.
3. The schema validator and the traceability check (158 = 99 + 59, no overlap, no gaps).
4. End-to-end `make pipeline` twice: with the v2 mock and with the v1 example. Both must produce scores and reports.
5. Open the regenerated PDFs and check page breaks, fonts, logo, flags and persona heatmap.
6. Grep for stale v1 wording (`158`, `28 capabilities`, `3 pillars`, `P1-C`, old level names) outside the v1 archive and the changelog; list anything left and why.
7. Markdown lint and internal link check on all changed docs.

## Final report

Reply with:

- The decisions taken (D-1 to D-8) and what you implemented for each.
- A table of changed, added and archived files grouped by phase.
- The output of every validation command.
- Open items, risks and anything you did not change, with the reason.
