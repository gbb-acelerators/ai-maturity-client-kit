# `referencia/branding/`: identidade visual

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

Esta pasta contém os ativos de marca aplicados aos helpers HTML e PDFs voltados para Microsoft neste kit.

## Arquivos

| Arquivo | Uso |
| --- | --- |
| [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css) | Tokens de design com paleta Microsoft, neutros, tipografia e classes utilitárias. |
| [IDENTITY.md](IDENTITY.md) | Strings canônicas, SVG oficial Microsoft de quatro quadrados, barra de marca e padrões proibidos. |
| [VOICE.md](VOICE.md) | Pilares de voz, vocabulário proibido, regras de pontuação e tom por público. |

## Onde a marca é aplicada

O logo oficial Microsoft de quatro quadrados e `Paula Silva | Global Developer Solutions Advisor` aparecem em:

- [../calculadora-pontuacao.html](../calculadora-pontuacao.html), calculadora v2 gerada.
- [../../formularios/assessment-v2.html](../../formularios/assessment-v2.html), formulário v2 gerado.
- [../../wizard/implementation-guide-wizard.html](../../wizard/implementation-guide-wizard.html), wizard gerado do guia de implementação.
- [../v1/calculadora-pontuacao.html](../v1/calculadora-pontuacao.pt-br.html), calculadora v1 arquivada.
- [../../formularios/v1/](../../formularios/v1/), formulários v1 arquivados.
- PDFs v2 renderizados a partir de [../../relatorios/templates/](../../relatorios/templates/), na capa.

O logo pessoal `</>` não é usado em material voltado para Microsoft.

## Atribuição

```text
Paula Silva | Global Developer Solutions Advisor
paulasilva@microsoft.com
```

Somente email. Não adicione LinkedIn, GitHub ou site.

## Criar um novo HTML alinhado

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

Carregue [tokens-paulasilva-ms.css](tokens-paulasilva-ms.css), use Inter e JetBrains Mono, e siga [VOICE.md](VOICE.md).
