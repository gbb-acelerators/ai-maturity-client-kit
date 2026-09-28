# Identidad visual paulasilva-ms (Microsoft)

🌐 [English](IDENTITY.md) · [Português (Brasil)](IDENTITY.pt-br.md) · Español

Identidad aplicada a artefactos visuales orientados a Microsoft en este kit.

## Cadenas canónicas (usa exactamente)

```text
Author name:     Paula Silva
Role (formal):   Global Developer Solutions Advisor
Role (full):     Paula Silva, Global Developer Solutions Advisor
Meta-bar form:   Paula Silva | Global Developer Solutions Advisor
Contact:         paulasilva@microsoft.com
```

El rol es **Global Developer Solutions Advisor**. No tiene organización ni región. El contacto es **solo email**. No agregues LinkedIn, GitHub ni un sitio web al material orientado a Microsoft.

## Logo oficial de cuatro cuadrados de Microsoft

Usa la marca oficial de cuatro cuadrados de Microsoft para helpers HTML y PDFs orientados a Microsoft. No uses el logo personal `</>` en material orientado a Microsoft.

```html
<svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Microsoft" style="width:22px;height:22px;flex-shrink:0;">
  <rect x="1" y="1" width="10" height="10" fill="#F25022"/>
  <rect x="12" y="1" width="10" height="10" fill="#7FBA00"/>
  <rect x="1" y="12" width="10" height="10" fill="#00A4EF"/>
  <rect x="12" y="12" width="10" height="10" fill="#FFB900"/>
</svg>
```

## Paleta del logo

| Token | Hex | Uso |
| --- | --- | --- |
| `--c-red-500` | `#F25022` | Cuadrado rojo de Microsoft, brechas críticas. |
| `--c-green-500` | `#7FBA00` | Cuadrado verde de Microsoft, éxito. |
| `--c-blue-500` | `#00A4EF` | Cuadrado azul de Microsoft, links y acento primario. |
| `--c-yellow-500` | `#FFB900` | Cuadrado amarillo de Microsoft, atención. |

Consulta [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css).

## Barra de chrome

```html
<div class="deck-brand">
  <!-- Microsoft four-square SVG here -->
  <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
</div>
```

## Dónde se aplica el branding

- [../calculadora-pontuacao.es.html](../calculadora-pontuacao.es.html), calculadora v2 generada.
- [../../formularios/assessment-v2.es.html](../../formularios/assessment-v2.es.html), formulario offline de evaluación v2 generado.
- [../../wizard/implementation-guide-wizard.es.html](../../wizard/implementation-guide-wizard.es.html), wizard de guía de implementación v2 generado.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.es.html), calculadora v1 archivada.
- [../../formularios/v1/](../../formularios/v1/), formularios HTML v1 archivados.
- Los PDFs v2 renderizados desde [../../relatorios/templates/](../../relatorios/templates/) llevan el logo de cuatro cuadrados en la portada.

## Patrones prohibidos

- Em-dashes. Usa coma, punto, dos puntos o punto y coma.
- En-dashes en rangos. Usa un guion con espacios, o `to`.
- El logo personal `</>` en material orientado a Microsoft.
- Colores fuera de la paleta de Microsoft sin un token explícito.
- Abreviaturas del rol o nombres de rol alternativos.
- LinkedIn, GitHub o un sitio web como contacto en material de Microsoft. Solo email.
