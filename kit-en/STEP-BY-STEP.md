# Step-by-step Guide · English Edition

> Complete walkthrough to run the AI Maturity Assessment kit from zero to 5 final PDFs.

🏠 [Back to README](README.md) · 🌐 [Site](https://paulasilvatech.github.io/ai-maturity-client-kit/en/) · 🇧🇷 [PT-BR](../GUIA-PASSO-A-PASSO.md) · 🇪🇸 [ES](../kit-es/PASO-A-PASO.md)

---

## Prerequisites

| Requirement | Version | Verify with |
|---|---|---|
| Python | 3.10+ | `python3 --version` |
| VS Code | latest | `code --version` |
| GitHub Copilot Chat | Pro / Business / Enterprise | Sidebar icon |
| pip packages | `jinja2`, `weasyprint`, `openpyxl` | `pip list \| grep -E "jinja2\|weasy\|openpyxl"` |

On **macOS**, WeasyPrint additionally needs `brew install pango`. On **Linux/WSL**: `sudo apt install libpango-1.0-0 libpangoft2-1.0-0`.

> [!TIP]
> Run `make smoke` after extracting the ZIP. It validates every prerequisite in 5 seconds.

## Step 1 — Get the kit

Download the ZIP from the site, extract it, and open the extracted folder in VS Code.

```bash
make install-deps   # installs jinja2 + weasyprint + openpyxl
make smoke          # validates the environment
```

Expected output: `✅ Smoke test passed (X checks).`

## Step 2 — Choose your data source

You have **3 options** to fill the 158 framework questions:

### Option A — Sample data (fastest, ~3 min)

```bash
cp respostas.json.example respostas.json
```

Uses the fictional **Cliente Exemplo S.A.** with 46 pre-filled responses. Great to validate the full pipeline before running for real.

### Option B — Manual fill

Edit `respostas.json` and set `level` (0 to 4) and `evidence` for each question. Skip questions you can't answer; the algorithm uses only answered ones.

### Option C — Microsoft Forms (multi-respondent)

1. Publish the 3 HTML forms at `formularios/` as 3 Microsoft Forms surveys (see `coleta/INSTRUCOES-FORMS.md` translated below).
2. Collect responses from leadership (3-5 respondents recommended).
3. Export the consolidated Excel to the workspace root as `respostas-forms.xlsx`.
4. Run `/importar-respostas-excel` in Copilot Chat to auto-aggregate to `respostas.json`.

## Step 3 — Run the pipeline

Open VS Code → Copilot Chat → switch to **Agent mode** (dropdown next to the icon).

### Easiest path: concierge agent

```
@ai-maturity-assistant
```

The agent reads your workspace state and asks one question at a time, invoking each skill in the correct order. Recommended for first-time users.

### Power user path: full orchestrator

```
/pipeline-completo
```

Runs the 6 steps end-to-end (auto-detects Excel and wizard inputs).

### Manual path: one skill at a time

```
/calcular-scores
/gap-analysis
/recomendar-estrategias
/wizard-implementacao
/gerar-relatorio
```

Useful when you want to inspect each intermediate JSON before continuing.

## Step 4 — Inspect outputs

Everything goes into `saida/`:

| File | Purpose |
|---|---|
| `scores-<DATE>.json` | Scores per capability / pillar / overall |
| `gaps-<DATE>.json` | Prioritized gaps P0 / P1 / P2 / P3 |
| `recomendacoes-<DATE>.json` | Strategies S1-S7 mapped to gaps + technologies |
| `pontuacao-preenchida-<DATE>.xlsx` | Auditable Excel with live formulas |
| **5 PDFs** | Score Justification + 3 Pillar Roadmaps + Implementation Guide |

PDFs are **~2 MB total**, ready to present to the board.

## Step 5 — Customize the Implementation Guide (Part 4 PDF)

The Implementation Guide PDF has 9 client-specific inputs (Steering Committee members, TPO, RACI, comms plan, training plan, ADKAR notes, 3 quick-wins waves). Fill them in 3 ways:

- **HTML wizard**: open `wizard/implementation-guide-wizard.html` in any browser, fill, download JSON.
- **JSON template**: copy `wizard/implementation-guide-inputs.template.json` and edit.
- **Chat**: run `/wizard-implementacao` and answer in conversation.

The Learning & Growth Survey auto-fills 6 of the 9 inputs if you ran survey C first.

## Troubleshooting

> [!WARNING]
> **`/calcular-scores` doesn't show up when I type `/`**
>
> You're not in Agent mode. Click the dropdown next to the Copilot icon and pick **Agent**. Then reload the window (`Cmd+Shift+P` → "Developer: Reload Window").

> [!WARNING]
> **WeasyPrint error on macOS: "no library called pango"**
>
> `brew install pango glib gobject-introspection libffi`

> [!WARNING]
> **Scores look low / many "no answer"**
>
> Coverage threshold: 40+ answered = OK, 25-39 = WARNING (preliminary), <25 = BLOCKED. Check `saida/scores-<DATE>.json::metadata::coverage`.

## Stuck on a step?

Contact Paula Silva on [LinkedIn](https://linkedin.com/in/paulanunes).

## Continue reading

| ⬅ Previous          | Next ➡                                       |
| :------------------ | -------------------------------------------: |
| [🏠 README](README.md) | [📝 Forms instructions](FORMS-INSTRUCTIONS.md) |

---

**Paula Silva** — Global Developer Solutions Advisor | [LinkedIn](https://linkedin.com/in/paulanunes)
