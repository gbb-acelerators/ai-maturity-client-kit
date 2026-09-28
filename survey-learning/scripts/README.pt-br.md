# `survey-learning/scripts/`

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Learning Survey](../README.pt-br.md)

Scripts que constroem o plano de capacitação a partir do Learning and Growth Survey identificado.

## Conteúdo

| Arquivo | Uso |
| --- | --- |
| [gerar_plano_capacitacao.py](gerar_plano_capacitacao.py) | Lê `survey-learning/respostas-learning.json` e gera `saida/plano-capacitacao-<date>.md`: tópicos solicitados, coortes por `DS-D#`, Champions, pares de mentoria, calendário de 90 dias, barreiras, wishlist e ações priorizadas. Inglês por padrão; use `--lang pt-br` ou `--lang es`. |

## Uso

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang es
```

Depois de gerar o plano, rode `python3 wizard/scripts/auto_fill_from_plano.py --lang pt-br` ou use `/wizard-implementacao` Mode D para preencher 7 dos 11 campos do guia de implementação.
