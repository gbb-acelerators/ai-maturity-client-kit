# `referencia/branding/`: visual identity

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

This folder contains the branding assets applied to Microsoft-facing HTML helpers and PDFs in this kit.

## Files

| File | What it is for |
| --- | --- |
| [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css) | Design tokens with the Microsoft palette, neutrals, typography, and utility classes. |
| [IDENTITY.md](IDENTITY.md) | Canonical strings, official Microsoft four-square SVG, chrome bar, and forbidden patterns. |
| [VOICE.md](VOICE.md) | Voice pillars, banned vocabulary, punctuation rules, and tone per audience. |

## Where the branding is applied

The official Microsoft four-square logo and `Paula Silva | Global Developer Solutions Advisor` appear in:

- [../calculadora-pontuacao.html](../calculadora-pontuacao.html), generated v2 calculator.
- [../../formularios/assessment-v2.html](../../formularios/assessment-v2.html), generated v2 assessment form.
- [../../wizard/implementation-guide-wizard.html](../../wizard/implementation-guide-wizard.html), generated implementation guide wizard.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.html), archived v1 calculator.
- [../../formularios/v1/](../../formularios/v1/), archived v1 forms.
- v2 PDFs rendered from [../../relatorios/templates/](../../relatorios/templates/), on the cover.

The personal `</>` logo is not used in Microsoft-facing material.

## Attribution

```text
Paula Silva | Global Developer Solutions Advisor
paulasilva@microsoft.com
```

Email only. Do not add LinkedIn, GitHub, or a website.

## Create a new aligned HTML

```html
<div class="deck-brand">
  <svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Microsoft" style="width:22px;height:22px;flex-shrink:0;">
    <rect x="1" y="1" width="10" height="10" fill="#F25022"/>
    <rect x="12" y="1" width="10" height="10" fill="#7FBA00"/>
    <rect x="1" y="12" width="10" height="10" fill="#00A4EF"/>
    <rect x="12" y="12" width="10" height="10" fill="#FFB900"/>
  </svg>
  <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
</div>
```

Load [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css), use Inter and JetBrains Mono, and follow [VOICE.md](VOICE.md).
