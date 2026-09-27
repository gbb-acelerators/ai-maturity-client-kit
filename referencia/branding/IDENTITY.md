# paulasilva-ms visual identity (Microsoft)

🌐 English · [Português (Brasil)](IDENTITY.pt-br.md)

Identity applied to the visual artifacts of this kit. It forks the design system paulasilva-ms v1.7.0.

## Canonical strings (use exactly)

```text
Author name:     Paula Silva
Role (formal):   Global Developer Solutions Advisor
Role (full):     Paula Silva, Global Developer Solutions Advisor
Meta-bar form:   Paula Silva | Global Developer Solutions Advisor
Contact:         paulasilva@microsoft.com
Tagline (EN):    Building the future of software development with AI and Agentic DevOps
```

The role is **Global Developer Solutions Advisor** (not "GBB Americas", not "Microsoft Global Black Belt", not abbreviated). It has no organization and no region.

The contact is **email only**. No public LinkedIn, no GitHub, and no website in Microsoft material.

The tagline is **English only** in MS material. Do not translate it.

## Logo palette (4 official Microsoft colors)

| Token | Hex | Use |
|---|---|---|
| `--c-blue-500` | `#00A4EF` | Default accent, primary buttons, links |
| `--c-green-500` | `#7FBA00` | Success, confirmation, positive metrics |
| `--c-yellow-500` | `#FFB900` | Attention, highlight |
| `--c-red-500` | `#F25022` | Error, critical gap, alert |

Each color has `-50` (very light, background), `-100` (light), and `-700` (dark, text) variants. See [`tokens-paulasilva-ms.css`](tokens-paulasilva-ms.css).

## SVG logo (inline, never an external link)

22px (chrome bar):

```html
<svg viewBox="0 0 1914 1062" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="paulasilva" style="width:22px;height:auto;flex-shrink:0;">
  <title>paulasilva</title>
  <path fill="#F25022" d="M532 131 L36 462 L13 497 L13 560 L23 582 L48 604 L521 923 L539 926 L539 699 L547 680 L314 530 L527 395 L551 371 L558 347 L558 155 L547 135 Z"/>
  <path fill="#7FBA00" d="M551 681 L542 693 L540 700 L540 917 L546 930 L558 940 L571 943 L778 943 L788 941 L798 935 L809 910 L809 702 L807 694 L799 682 L784 674 L566 674 Z"/>
  <path fill="#FFB900" d="M1390 16 L1208 13 L1184 23 L1171 38 L768 1009 L768 1026 L778 1038 L957 1042 L975 1037 L995 1017 L1346 179 L1349 145 L1367 129 L1401 47 L1402 31 Z"/>
  <path fill="#00A4EF" d="M1369 131 L1350 149 L1349 355 L1354 369 L1385 399 L1592 528 L1373 667 L1354 688 L1349 703 L1349 907 L1361 924 L1377 926 L1871 595 L1893 563 L1894 501 L1885 477 L1863 456 L1398 142 Z"/>
</svg>
```

## Chrome bar (top of any standalone HTML)

```html
<div class="deck-brand">
  <!-- 22px logo SVG here -->
  <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
</div>
```

```css
.deck-brand {
  position: fixed; top: 16px; left: 32px; z-index: 50;
  display: flex; align-items: center; gap: 12px;
}
.deck-brand__text {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-3);
}
```

## Typography

- **Sans:** Inter (load from Google Fonts or a CDN)
- **Mono:** JetBrains Mono (load from Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

## Forbidden patterns (review before publishing)

- ❌ Em-dashes (`—`). Use a comma, period, colon, or semicolon.
- ❌ En-dashes (`–`) in ranges. Use a hyphen with spaces (`08:00 - 12:00`) or "to" / "a".
- ❌ Banned vocabulary: see [`VOICE.md`](VOICE.md).
- ❌ Colors outside the MS palette without an explicit token.
- ❌ A logo with colors other than the 4 official ones (`#F25022 / #7FBA00 / #FFB900 / #00A4EF`).
- ❌ "Microsoft GBB Americas", "MS Global Black Belt", or role abbreviations.
- ❌ Adding LinkedIn, GitHub, or a website to the contact. Email only.

## How to use in the kit's artifacts

1. The kit's interactive HTMLs already load `tokens-paulasilva-ms.css`:
   - [`../calculadora-pontuacao.html`](../calculadora-pontuacao.html)
   - [`../../formularios/P1-produtividade-do-desenvolvedor.html`](../../formularios/v1/P1-produtividade-do-desenvolvedor.html)
   - [`../../formularios/P2-ciclo-de-vida-devops.html`](../../formularios/v1/P2-ciclo-de-vida-devops.html)
   - [`../../formularios/P3-plataforma-de-aplicações.html`](../../formularios/v1/P3-plataforma-de-aplicações.html)
   - [`../../wizard/implementation-guide-wizard.html`](../../wizard/implementation-guide-wizard.html)

2. The Jinja2 PDFs (`relatorios/templates/*.html.j2` + `_print.css`) **keep the official platform palette** (they were not changed). MS branding applies to the kit's standalone HTMLs, not to the production PDFs.

3. To create a new aligned HTML:
   - Load Inter + JetBrains Mono via Google Fonts
   - `<link rel="stylesheet" href="referencia/branding/tokens-paulasilva-ms.css">` (relative)
   - Use tokens (`var(--c-blue-500)`, `var(--accent)`, `var(--ink)`, etc.)
   - Add the chrome bar with logo + meta-text

## Full reference

For the full detail of the design system (showcase, deck patterns, simulations, layouts), see the canonical skill:

- `/Users/paulasilva/Documents/ai-maturuty-client-platform/.github/skills/paulasilva-ms/`
- `references/identity.md`: canonical strings + logo
- `references/voice.md`: banned vocabulary + tone
- `references/components.md`: components (cards, badges, tables)
- `references/playbook.md`: multi-page playbook pattern
- `assets/showcase.html`: visual reference of all patterns
