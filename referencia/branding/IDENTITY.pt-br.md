# Identidade visual paulasilva-ms (Microsoft)

🌐 [English](IDENTITY.md) · Português (Brasil) · [Español](IDENTITY.es.md)

Identidade aplicada aos artefatos visuais voltados para Microsoft neste kit.

## Strings canônicas (use exatamente)

```text
Nome da autora:  Paula Silva
Papel (formal):  Global Developer Solutions Advisor
Papel (completo): Paula Silva, Global Developer Solutions Advisor
Meta-bar:        Paula Silva | Global Developer Solutions Advisor
Contato:         paulasilva@microsoft.com
```

O papel é **Global Developer Solutions Advisor**. Ele não tem organização nem região. O contato é **somente email**. Não adicione LinkedIn, GitHub ou site a material voltado para Microsoft.

## Logo oficial Microsoft de quatro quadrados

Use a marca oficial Microsoft de quatro quadrados nos helpers HTML e PDFs voltados para Microsoft. Não use o logo pessoal `</>` em material voltado para Microsoft.

```html
<svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Microsoft" style="width:22px;height:22px;flex-shrink:0;">
  <rect x="1" y="1" width="10" height="10" fill="#F25022"/>
  <rect x="12" y="1" width="10" height="10" fill="#7FBA00"/>
  <rect x="1" y="12" width="10" height="10" fill="#00A4EF"/>
  <rect x="12" y="12" width="10" height="10" fill="#FFB900"/>
</svg>
```

## Paleta do logo

| Token | Hex | Uso |
| --- | --- | --- |
| `--c-red-500` | `#F25022` | Quadrado vermelho Microsoft, gaps críticos. |
| `--c-green-500` | `#7FBA00` | Quadrado verde Microsoft, sucesso. |
| `--c-blue-500` | `#00A4EF` | Quadrado azul Microsoft, links e acento primário. |
| `--c-yellow-500` | `#FFB900` | Quadrado amarelo Microsoft, atenção. |

Veja [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css).

## Barra de marca

```html
<div class="deck-brand">
  <!-- SVG Microsoft de quatro quadrados aqui -->
  <span class="deck-brand__text">Paula Silva | Global Developer Solutions Advisor</span>
</div>
```

## Onde a marca é aplicada

- [../calculadora-pontuacao.html](../calculadora-pontuacao.html), calculadora v2 gerada.
- [../../formularios/assessment-v2.html](../../formularios/assessment-v2.html), formulário offline v2 gerado.
- [../../wizard/implementation-guide-wizard.html](../../wizard/implementation-guide-wizard.html), wizard v2 gerado do guia de implementação.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.html), calculadora v1 arquivada.
- [../../formularios/v1/](../../formularios/v1/), formulários HTML v1 arquivados.
- PDFs v2 renderizados a partir de [../../relatorios/templates/](../../relatorios/templates/) carregam o logo de quatro quadrados na capa.

## Padrões proibidos

- Travessões. Use vírgula, ponto, dois-pontos ou ponto e vírgula.
- Meia-risca em intervalos. Use hífen com espaços, ou `to`.
- Logo pessoal `</>` em material voltado para Microsoft.
- Cores fora da paleta Microsoft sem token explícito.
- Abreviações ou nomes alternativos do papel.
- LinkedIn, GitHub ou site como contato em material Microsoft. Somente email.
