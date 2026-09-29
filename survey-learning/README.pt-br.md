# `survey-learning/`: Learning and Growth Survey (identificado, capacitação)

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

Este survey identificado gera o plano de capacitação usado pela liderança e pelo wizard do guia de implementação. Ele complementa o assessment principal e o Developer Survey anônimo.

## Diferença vs. os outros surveys

| Aspecto | Assessment principal | Developer Survey | Learning Survey |
| --- | --- | --- | --- |
| Público | Liderança | Desenvolvedores anônimos | Desenvolvedores identificados |
| Foco | Maturidade organizacional, D1 a D9 | Comportamento e prática, `DS-D2` a `DS-D8` | Demanda de aprendizagem e Champions |
| Saída | 5 PDFs v2 | Insights e JSON de maturidade | `output/training-plan-<date>.md` |
| Impacto no score | Fonte dos scores v2 | Apenas contexto | Apenas contexto e auto-fill do wizard |

## IDs do Learning Survey

Os rótulos do banco de perguntas do Learning Survey usam `L#-Q#`. Quando uma pergunta se refere a dimensões do Developer Survey, ela usa `DS-D#`, por exemplo `L2-Q1: DS-D2 Copilot Adoption ...`. Isso evita colisão com dimensões D1 a D9 do assessment v2.

## Arquivos nesta pasta

| Arquivo | O que é |
| --- | --- |
| [FORMS-INSTRUCTIONS-LEARNING.md](FORMS-INSTRUCTIONS-LEARNING.pt-br.md) | Como montar o Microsoft Forms identificado. |
| [question-bank-learning.md](question-bank-learning.md) | Banco de perguntas em inglês. |
| [question-bank-learning.pt-br.md](question-bank-learning.pt-br.md) | Banco de perguntas em português (Brasil). |
| [question-bank-learning.es.md](question-bank-learning.es.md) | Banco de perguntas em espanhol. Os scripts escrevem EN, PT-BR ou ES (`--lang es`). |
| [template-export-forms-learning.xlsx](template-export-forms-learning.xlsx) | Template Excel. |
| [mock-responses-learning.json](mock-responses-learning.json) | JSON estruturado de exemplo. |
| [scripts/](scripts/) | Gerador do plano de capacitação. |

## Fluxo de uso

```text
1. Monte o Forms com FORMS-INSTRUCTIONS-LEARNING.md.
2. Compartilhe com os desenvolvedores.
3. Exporte respostas para Excel.
4. Rode /import-survey-learning.
5. Rode /training-plan.
6. Rode /implementation-wizard Mode D, ou rode wizard/scripts/auto_fill_from_plan.py.
7. Rode make pipeline para atualizar v2_implementation_guide.pdf.
```

## O que o plano de capacitação contém

`output/training-plan-<date>.md` é escrito em inglês por padrão, ou em PT-BR ou ES com `--lang pt-br` ou `--lang es`. Ele inclui tópicos solicitados, coortes sugeridas por `DS-D#`, Champions, pares de mentoria, calendário de 90 dias, barreiras, wishlist e ações priorizadas.

## Conexão com o wizard

O Mode D preenche 7 dos 11 campos do guia de implementação a partir do plano do Learning Survey: steering committee a partir de Champions ativos, plano de comunicação a partir do calendário, plano de treinamento a partir das coortes, notas ADKAR e quick wins. Os campos restantes são marcados como itens a preencher.
