# `referencia/branding/`: paulasilva-ms visual identity (Microsoft)

🌐 English · [Português (Brasil)](README.pt-br.md)

This folder contains the branding assets applied to the standalone visual artifacts of this kit (interactive HTMLs). It forks the canonical design system paulasilva-ms v1.7.0.

## Files

| File | What it is for |
|---|---|
| **[tokens-paulasilva-ms.css](tokens-paulasilva-ms.css)** | Canonical design tokens: Microsoft 4-color palette (#F25022, #7FBA00, #FFB900, #00A4EF), neutrals, dark mode, accent classes (.acc-blue, .acc-green, .acc-yellow, .acc-red), typography (Inter + JetBrains Mono) |
| **[IDENTITY.md](IDENTITY.md)** | Canonical strings (name, role, contact), inline SVG logo, chrome bar, and mandatory patterns |
| **[VOICE.md](VOICE.md)** | Voice pillars, banned vocabulary, punctuation rules, and tone per audience |

## Where the branding is applied

### ✅ Applied to the kit's standalone HTMLs

The following files load `tokens-paulasilva-ms.css` and show the chrome bar:

- [`../calculadora-pontuacao.html`](../calculadora-pontuacao.html): interactive calculator
- [`../../formularios/P1-produtividade-do-desenvolvedor.html`](../../formularios/v1/P1-produtividade-do-desenvolvedor.html)
- [`../../formularios/P2-ciclo-de-vida-devops.html`](../../formularios/v1/P2-ciclo-de-vida-devops.html)
- [`../../formularios/P3-plataforma-de-aplicações.html`](../../formularios/v1/P3-plataforma-de-aplicações.html)
- [`../../wizard/implementation-guide-wizard.html`](../../wizard/implementation-guide-wizard.html)

### ❌ NOT applied to the Jinja2 PDFs

The 5 production-quality PDFs (`relatorios/templates/*.html.j2` + `_print.css`) **keep the official platform palette** (a faithful mirror of `app/src/report-service/templates/`). The paulasilva-ms branding applies to the kit's HTMLs, not to the PDFs.

Reason: the PDFs are production deliverables that must be identical to the future web platform. Modifying their CSS would break that parity.

## Attribution (every new HTML in this kit must have it)

```
Paula Silva | Global Developer Solutions Advisor
paulasilva@microsoft.com
```

No LinkedIn, no GitHub, no website. Email only.

## How to create a new aligned HTML

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../referencia/branding/tokens-paulasilva-ms.css">
  <style>
    body { font-family: var(--font-sans); color: var(--ink); background: var(--bg); }
    h1 { color: var(--accent-ink); }
    .card { background: var(--paper); border: 1px solid var(--rule); }
  </style>
</head>
<body>
  <div class="deck-brand">
    <!-- 22px logo SVG (copy from IDENTITY.md) -->
    <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
  </div>
  <!-- content here -->
</body>
</html>
```

## Full canonical skill

For the full visual showcase, deck patterns, simulations, and multi-page playbook layouts:

- Path: `/Users/paulasilva/Documents/ai-maturuty-client-platform/.github/skills/paulasilva-ms/`
- `assets/showcase.html` opens in the browser and shows all components
- `references/components.md` documents cards, badges, tables, and buttons
- `references/playbook.md` documents the multi-page playbook pattern
- `references/pdf-generation.md` documents deck → PDF via Playwright

When you need to create a new deck, playbook, or formal Microsoft material outside this kit, invoke the `paulasilva-ms` skill in Copilot Chat.
