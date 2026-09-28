# `referencia/branding/`: identidad visual

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Esta carpeta contiene los assets de branding aplicados a helpers HTML e informes PDF orientados a Microsoft en este kit.

## Archivos

| Archivo | Para qué sirve |
| --- | --- |
| [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css) | Tokens de diseño con la paleta de Microsoft, neutros, tipografía y clases utilitarias. |
| [IDENTITY.es.md](IDENTITY.es.md) | Cadenas canónicas, SVG oficial de cuatro cuadrados de Microsoft, barra de chrome y patrones prohibidos. |
| [VOICE.es.md](VOICE.es.md) | Pilares de voz, vocabulario prohibido, reglas de puntuación y tono por audiencia. |

## Dónde se aplica el branding

El logo oficial de cuatro cuadrados de Microsoft y `Paula Silva | Global Developer Solutions Advisor` aparecen en:

- [../calculadora-pontuacao.es.html](../calculadora-pontuacao.es.html), calculadora v2 generada.
- [../../formularios/assessment-v2.es.html](../../formularios/assessment-v2.es.html), formulario de evaluación v2 generado.
- [../../wizard/implementation-guide-wizard.es.html](../../wizard/implementation-guide-wizard.es.html), wizard de guía de implementación generado.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.html), calculadora v1 archivada.
- [../../formularios/v1/](../../formularios/v1/), formularios v1 archivados.
- PDFs v2 renderizados desde [../../relatorios/templates/](../../relatorios/templates/), en la portada.

El logo personal `</>` no se usa en material orientado a Microsoft.

## Atribución

```text
Paula Silva | Global Developer Solutions Advisor
paulasilva@microsoft.com
```

Solo email. No agregues LinkedIn, GitHub ni un sitio web.

## Crear un nuevo HTML alineado

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

Carga [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css), usa Inter y JetBrains Mono, y sigue [VOICE.es.md](VOICE.es.md).
