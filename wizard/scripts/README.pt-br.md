# `wizard/scripts/`

🌐 [English](README.md) · Português (Brasil)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Wizard](../README.pt-br.md)

Scripts que dão suporte ao Wizard do Guia de Implementação.

## Conteúdo

| Arquivo | Uso |
| --- | --- |
| [auto_fill_from_plano.py](auto_fill_from_plano.py) | Mode D do wizard. Lê o `saida/plano-capacitacao-*.md` mais recente e gera `implementation-guide-inputs.json` na raiz. Suporta `--lang en`, `--lang pt-br` e `--lang es`. Preenche 7 dos 11 campos a partir da saída do Learning Survey e marca o restante como itens a preencher. |

## Uso

```bash
python3 wizard/scripts/auto_fill_from_plano.py --lang pt-br
```

Rode depois de `/plano-capacitacao` ou depois de `python3 survey-learning/scripts/gerar_plano_capacitacao.py`. Depois rode `make pipeline` para atualizar os 5 PDFs v2.
