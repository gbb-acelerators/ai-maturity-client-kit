# `reports/templates/`

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Relatórios](../README.pt-br.md)

Templates Jinja2 para PDFs de relatório. Coordene alterações porque elas afetam todos os clientes que usam o kit.

## Conteúdo

| Arquivo | Renderiza |
| --- | --- |
| [`v2_assessment_summary.html.j2`](v2_assessment_summary.html.j2) | `v2_assessment_summary.pdf`: sumário executivo, scoring, prioridades, cross-checks de evidência e contexto do Developer Survey quando disponível. |
| [`v2_roadmap_group.html.j2`](v2_roadmap_group.html.j2) | PDFs de roadmap por grupo G1, G2 e G3. |
| [`v2_implementation_guide.html.j2`](v2_implementation_guide.html.j2) | `v2_implementation_guide.pdf`: governança, donos por dimensão, RACI, plano por fases, gestão da mudança, riscos, métricas, primeiros 90 dias e referências. |
| [`v2_round_comparison.html.j2`](v2_round_comparison.html.j2) | `round-comparison.pdf` de `scripts/compare_rounds.py --pdf`. |
| [`_v2_components.html.j2`](_v2_components.html.j2) | Macros v2 compartilhadas. |
| [`_print.css`](_print.css) | CSS de impressão com o tratamento visual Microsoft de quatro quadrados. |
| Templates legados | Templates de relatório v1 arquivados usados somente pelo despacho v1. |

## Como customizar

> [!CAUTION]
> Editar arquivos `.html.j2` afeta todos os clientes que usam o kit. Para customização por cliente, edite `implementation-guide-inputs.json` ou rode o wizard novamente, depois renderize.

Se você mudar templates:

1. Rode `make smoke`.
2. Rode `make validate-docs`.
3. Compare com as saídas em [../../reference/sample-output/](../../reference/sample-output/).

## Variáveis principais consumidas

Cada template espera campos de `payload_v2.json`. O guia de implementação lê campos normalizados do wizard em `reports/scripts/wizard_inputs.py`; valores vazios aparecem como `to fill with the client`.

## i18n

Strings localizáveis ficam em [../i18n/](../i18n/) (`en.json`, `es.json`, `pt-br.json`). Templates leem por `{{ t('key') }}`.
