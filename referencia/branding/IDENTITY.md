# paulasilva-ms visual identity (Microsoft)

🌐 English · [Português (Brasil)](IDENTITY.pt-br.md) · [Español](IDENTITY.es.md)

Identity applied to Microsoft-facing visual artifacts in this kit.

## Canonical strings (use exactly)

```text
Author name:     Paula Silva
Role (formal):   Global Developer Solutions Advisor
Role (full):     Paula Silva, Global Developer Solutions Advisor
Meta-bar form:   Paula Silva | Global Developer Solutions Advisor
Contact:         paulasilva@microsoft.com
```

The role is **Global Developer Solutions Advisor**. It has no organization and no region. The contact is **email only**. Do not add LinkedIn, GitHub, or a website to Microsoft-facing material.

## Official Microsoft four-square logo

Use the official Microsoft four-square mark for Microsoft-facing HTML helpers and PDFs. Do not use the personal `</>` logo in Microsoft-facing material.

```html
<svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Microsoft" style="width:22px;height:22px;flex-shrink:0;">
  <rect x="1" y="1" width="10" height="10" fill="#F25022"/>
  <rect x="12" y="1" width="10" height="10" fill="#7FBA00"/>
  <rect x="1" y="12" width="10" height="10" fill="#00A4EF"/>
  <rect x="12" y="12" width="10" height="10" fill="#FFB900"/>
</svg>
```

## Logo palette

| Token | Hex | Use |
| --- | --- | --- |
| `--c-red-500` | `#F25022` | Microsoft red square, critical gaps. |
| `--c-green-500` | `#7FBA00` | Microsoft green square, success. |
| `--c-blue-500` | `#00A4EF` | Microsoft blue square, links and primary accent. |
| `--c-yellow-500` | `#FFB900` | Microsoft yellow square, attention. |

See [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css).

## Chrome bar

```html
<div class="deck-brand">
  <!-- Microsoft four-square SVG here -->
  <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
</div>
```

## Where the branding is applied

- [../calculadora-pontuacao.html](../calculadora-pontuacao.html), generated v2 calculator.
- [../../formularios/assessment-v2.html](../../formularios/assessment-v2.html), generated v2 offline assessment form.
- [../../wizard/implementation-guide-wizard.html](../../wizard/implementation-guide-wizard.html), generated v2 implementation guide wizard.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.html), archived v1 calculator.
- [../../formularios/v1/](../../formularios/v1/), archived v1 HTML forms.
- v2 PDFs rendered from [../../relatorios/templates/](../../relatorios/templates/) carry the four-square logo on the cover.

## Forbidden patterns

- Em-dashes. Use a comma, period, colon, or semicolon.
- En-dashes in ranges. Use a hyphen with spaces, or `to`.
- The personal `</>` logo in Microsoft-facing material.
- Colors outside the Microsoft palette without an explicit token.
- Role abbreviations or alternate role names.
- LinkedIn, GitHub, or a website as contact in Microsoft material. Email only.
