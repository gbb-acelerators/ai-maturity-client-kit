# Brand Voice (paulasilva-ms)

🌐 English · [Português (Brasil)](VOICE.pt-br.md) · [Español](VOICE.es.md)

Unified voice of the design system. All content written under the Microsoft identity follows these rules.

## Three pillars

1. **Pedagogical without condescension.** Explain as if you were teaching a smart engineer who has not seen this specific topic. Do not talk as if they were a beginner who needs hand-holding.
2. **Provocative through data, not hype.** Make claims that challenge assumptions, but ground every claim in a number, a citation, or a concrete scenario. Never use a vague superlative.
3. **Personal, with named scars.** Reference real failure modes you have seen. Do not speak in the abstract when you can speak from experience.

## Banned vocabulary (never use in any output)

| Banned | Why | Alternative |
|---|---|---|
| `AI-powered` | Marketing filler | Describe what the AI does |
| `revolutionary` | Self-praise without proof | Describe the concrete change |
| `game-changer` | Cliché | Say what changed and why it matters |
| `next-generation` | Empty signal | Give the version or the new capability |
| `world-class` | Self-praise | Cite the benchmark |
| `best-in-class` | Self-praise | Cite the benchmark |
| `cutting-edge` | Vague | Name the specific technique |
| `this changes everything` | Hyperbole | List what changes and what does not |
| `the future is here` | Hype | Describe the present state |
| `obviously` | Implies the reader is dumb | Just state it |
| `as everyone knows` | Same | Just state it |
| `synergy` | Empty | Describe the specific interaction |
| `leverage` (verb) | Filler | `use`, `apply`, `build on` |
| `circle back` | Corporate filler | `revisit`, `come back to` |
| `low-hanging fruit` | Cliché | Name the opportunity |
| `I am no expert but...` | False modesty | Just state it |
| `just sharing my humble thoughts` | Same | Same |

## Punctuation

- ❌ **No em-dashes** (`—`). Use a comma, period, colon, or semicolon.
- ❌ **No en-dashes** (`–`) in ranges. Use a hyphen with spaces (`08:00 - 12:00`) or "to" / "a".
- ❌ **No double space** after a period. Single space.
- ✅ **Serial comma** (Oxford). "Specs, agents, and humans in the loop."

## Tone per audience

| Audience | Tone | Opening example |
|---|---|---|
| Executive (board, VP) | Concise, numbers first, clear actions | "3 capabilities in P0. Immediate action: invest 8 FTE in S7 (Security)." |
| Tech Lead / Architect | Explicit trade-offs, technical citations | "Foundry Agent Service GA brings native MCP. Trade-off: vendor lock-in vs. fast integration." |
| Developer | Concrete, code when useful, jargon OK | "Custom agent in `.github/agents/*.agent.md`. Frontmatter `tools:`, `handoffs:`. See the paulasilva-ms showcase." |
| External client | Pedagogical, no internal acronyms | "The AI Maturity Assessment is a 61-question evaluation that measures 9 dimensions of the AI-assisted software lifecycle." |

## Citation patterns

- Microsoft-first: cite docs.microsoft.com, learn.microsoft.com, and github.blog before other sources.
- Always give the full URL.
- Cite with a date when relevant (e.g., "GA September 2025").
- For paulasilva-ms DS concepts, reference the skill path (`.github/skills/paulasilva-ms/references/X.md`).
