---
name: recomendar-estrategias
description: Maps gaps per capability to the 7 strategies S1-S7 and generates prioritized action plan with specific technologies. Reads saida/gaps.json + framework.json. Generates saida/recomendacoes.json. Use when user asks to "recomendar estratégias", "mapear ações", "que iniciativas devo priorizar", "recommend strategies", "map actions", "which initiatives should we prioritize".
---

# Skill: Recommend strategies S1–S7

## When to use
- After `/gap-analysis` (depends on `saida/gaps.json`).
- When client wants an **actionable plan**, not just a diagnosis.

## Inputs
- `saida/gaps.json` — prioritized gaps
- `framework.json::strategies` — definition of the 7 strategies
- `framework.json::technologies_per_strategy` — technologies per strategy
- `framework.json::pillars[].capabilities[].strategies` — cap→strategies mapping

## Expected output
- `saida/recomendacoes.json` — grouped by strategy + ranking
- Brief chat message (English by default, or the user's language): top 3 strategies by cumulative impact.

## Implementation: invoke the official script

```bash
python3 scripts/assessment_engine.py recommendations
```

**DO NOT build recommendations in chat.** The script reads `saida/gaps.json`, applies the templates below, and writes `saida/recomendacoes.json`. `expected_outcome` is a neutral template (no invented metrics or timelines). You may explain the output to the client, but do not add numbers the data does not contain.

## Algorithm

### 1. Aggregate gaps per strategy
For each gap in `gaps.json::gaps`:
```
for each strategy_id in gap.strategies:
    estrategias[strategy_id].related_gaps.append(gap)
    estrategias[strategy_id].cumulative_priority += gap.priority_score
    estrategias[strategy_id].max_priority = max(P0, P1, P2, P3 of gaps)
```

### 2. Rank strategies
Sort by `cumulative_priority` desc. Tie → higher `max_priority` → more `related_gaps`.

### 3. Technologies and horizon
For each strategy:
- Pull `technologies_per_strategy[strategy_id]` from `framework.json`
- Determine aggregated `horizon` from the most critical gap in the group (P0=30d, P1=quarter, P2=semester)

### 4. Generate concrete actions (deterministic templates — DO NOT invent)

Use these templates based on the strategy. Write the English text by default; use the PT-BR text when `respostas.json::metadata.language` is `pt-BR` (translate faithfully for `es`).

| Strategy | Recommended initial action (`en`, default) | `pt-BR` |
|---|---|---|
| **S1** GitHub Migration | "Inventory current repositories, then plan the migration to GitHub Enterprise Cloud in 3 waves." | "Inventário de repositórios atuais → plano de migração para GitHub Enterprise Cloud em 3 ondas." |
| **S2** Foundry + SRE | "Define SLOs/SLIs for critical services; deploy Azure Monitor and Grafana dashboards." | "Definir SLOs/SLIs para serviços críticos; implantar Azure Monitor + dashboards Grafana." |
| **S3** App Modernization | "Select 1 or 2 pilot apps; replatform to Azure Container Apps with IaC in Terraform." | "Selecionar 1–2 apps piloto; replatforming para Azure Container Apps + IaC com Terraform." |
| **S4** AI Applications | "Identify 2 high-ROI use cases; build a PoC with Azure OpenAI and Prompt Flow." | "Identificar 2 casos de uso de alto ROI; PoC com Azure OpenAI + Prompt Flow." |
| **S5** Copilot Acceleration | "Roll out Copilot Enterprise to 2 pilot squads; measure adoption and DORA productivity for 8 weeks." | "Rollout Copilot Enterprise em 2 squads piloto; medir adoção e produtividade DORA por 8 semanas." |
| **S6** Agentic Activation | "Pilot Semantic Kernel for 1 internal workflow; establish guardrails and observability." | "Pilot Semantic Kernel para 1 workflow interno; estabelecer guardrails e observabilidade." |
| **S7** Security & Governance | "Enable GitHub Advanced Security on all repos; generate SBOMs for critical services." | "Habilitar GitHub Advanced Security em todos repos; gerar SBOM dos serviços críticos." |

## `saida/recomendacoes.json` schema

```json
{
  "metadata": {
    "computed_at": "2026-05-08T14:30:00Z",
    "based_on": "saida/gaps.json"
  },
  "ranked_strategies": [
    {
      "rank": 1,
      "strategy_id": "S5",
      "strategy_name": "GitHub Copilot Acceleration",
      "cumulative_priority": 8.42,
      "max_priority": "P0 — Crítico",
      "horizon": "30 days",
      "related_capabilities": [
        {"id": "P1-C1", "name_pt_br": "Assistentes de Codificação IA", "gap_size": 1.4, "priority": "P1 — Alto"},
        {"id": "P1-C8", "name_pt_br": "Medição de Produtividade", "gap_size": 1.5, "priority": "P1 — Alto"}
      ],
      "technologies": [
        {"name": "GitHub Copilot Enterprise", "purpose": "AI-assisted coding across development teams"}
      ],
      "first_action": "Roll out Copilot Enterprise to 2 pilot squads; measure adoption and DORA productivity for 8 weeks.",
      "expected_outcome": "Raise P1-C1, P1-C8 toward the target level; re-assess to confirm."
    }
  ],
  "skipped_strategies": [
    {"strategy_id": "S1", "strategy_name": "GitHub Migration", "reason": "no related gaps"}
  ]
}
```

`skipped_strategies` = strategies that **didn't appear in any gap** (client already mature in them or related capabilities not answered).

Keep the canonical priority labels (`"P0 — Crítico"`) and `name_pt_br` as stored in `gaps.json`; `horizon` uses the same language rule as `/gap-analysis`.

## Report in chat (English by default, or the user's language)

```
✓ Recommendations → saida/recomendacoes.json

Top 3 strategies by cumulative impact:
  🥇 S5 GitHub Copilot Acceleration (priority 8.42, 4 capabilities)
     → Roll out Copilot to 2 pilot squads, measure DORA for 8 weeks.
  🥈 S7 Security & Governance (priority 5.10, 2 capabilities)
     → Enable GHAS on all repos and generate SBOMs for critical services.
  🥉 S6 Agentic Activation (priority 2.94, 1 capability)
     → Pilot Semantic Kernel for 1 internal workflow.

Not recommended (no relevant gaps): S1
Next: /gerar-relatorio
```

## Constraints
- **DO NOT INVENT** actions outside the table above. If in doubt, write "Detail with a Microsoft GBB architect" (PT-BR: "Detalhar com arquiteto Microsoft GBB").
- Strategies with `cumulative_priority < 0.9` (only P3 gaps) → move to `skipped_strategies` with note "monitor" (PT-BR: "monitorar").
- Technologies must come EXCLUSIVELY from `framework.json::technologies_per_strategy`.
- Human-facing fields follow `metadata.language` (English by default); technical IDs and names stay in English.
