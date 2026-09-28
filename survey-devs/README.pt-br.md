# `survey-devs/`: Developer Survey (anônimo, comportamental, individual)

🌐 [English](README.md) · Português (Brasil)

Esta pasta contém um survey separado do assessment principal. Ele mede como desenvolvedores usam GitHub Copilot, agentes, arquivos de instruções, modos do Copilot Chat, práticas de desenvolvimento com IA, governança e segurança no dia a dia. Ele é anônimo.

## Diferença vs. assessment principal e survey-learning

| Aspecto | Assessment principal | Developer Survey | survey-learning |
| --- | --- | --- | --- |
| Público | Liderança, arquitetos e Tech Leads | Desenvolvedores individuais | Desenvolvedores individuais |
| Anônimo? | Não | Sim | Não, identificado por nome e email |
| Foco | Maturidade organizacional, v2 D1 a D9 | Adoção e prática individual real, `DS-D2` a `DS-D8` | O que as pessoas querem aprender |
| Saída | 5 PDFs v2, planilha, JSONs | Relatório de insights e JSON de maturidade calculada | Plano de capacitação e Champions |
| Impacto no score | Fonte dos scores v2 | Apenas contexto | Apenas contexto e auto-fill do wizard |

Resultados de survey nunca mudam scores do assessment v2.

## Dimensões do survey

As dimensões do Developer Survey agora são nomeadas `DS-D2` a `DS-D8` nas chaves JSON, insights, coortes do plano de capacitação e referências cruzadas. Forms construídos com o texto antigo no estilo `D2` ainda são aceitos.

| ID | Foco |
| --- | --- |
| `DS-D2` | Adoção e modos do Copilot. |
| `DS-D3` | Ferramentas do ecossistema Microsoft e GitHub. |
| `DS-D4` | Práticas de desenvolvimento com IA. |
| `DS-D5` | Conceitos e estrutura de agentes. |
| `DS-D6` | Markdown, memória e instruções. |
| `DS-D7` | Usabilidade e melhores práticas. |
| `DS-D8` | Segurança e governança. |

## Crosswalk para o framework v2

`framework.v2.json` mapeia cada `DS-D#` para as perguntas v2 que ele ajuda a validar:

| Dimensão do survey | Perguntas v2 |
| --- | --- |
| `DS-D2` | D4-Q1, D4-Q2, D9-Q1 |
| `DS-D3` | D4-Q3, D4-Q6, D3-Q2, D6-Q1 |
| `DS-D4` | D3-Q2, D5-Q5, D2-Q6 |
| `DS-D5` | D2-Q4, D4-Q5 |
| `DS-D6` | D4-Q4, D4-Q5 |
| `DS-D7` | D2-Q2, D9-Q4 |
| `DS-D8` | D1-Q2, D6-Q1, D6-Q4, D6-Q5, D6-Q7 |

A seção 12 do relatório de insights aponta para perguntas v2, não para capacidades v1. O PDF de sumário v2 mostra contexto do Developer Survey quando `saida/maturidade-developer-survey-*.json` existe.

## Arquivos nesta pasta

| Arquivo | O que é |
| --- | --- |
| [INSTRUCOES-FORMS-DEVS.md](INSTRUCOES-FORMS-DEVS.md) | Guia passo a passo para montar o Microsoft Forms. |
| [perguntas-para-forms-devs.en.md](perguntas-para-forms-devs.en.md) | Banco de perguntas em inglês. |
| [perguntas-para-forms-devs.md](perguntas-para-forms-devs.md) | Banco canônico em PT-BR. |
| [template-export-forms-devs.xlsx](template-export-forms-devs.xlsx) | Template Excel no formato de export do Forms. |
| [respostas-mock-devs.json](respostas-mock-devs.json) | JSON estruturado de exemplo para smoke tests. |
| [RUBRICA-MATURIDADE.md](RUBRICA-MATURIDADE.md) | Rubrica determinística. Ela mantém as bandas v1, então compare por score, não pelo nome do nível. |
| [scripts/](scripts/) | Scripts de importação, scoring e insights. |

## Fluxo de uso

```text
1. Monte o Forms com INSTRUCOES-FORMS-DEVS.md.
2. Colete respostas anonimamente.
3. Exporte para Excel.
4. Rode /importar-survey-devs.
5. Rode /insights-developer-survey.
6. Rode make pipeline novamente se quiser que o PDF de sumário v2 inclua contexto do Developer Survey.
```

Os scripts escrevem EN por padrão, PT-BR com `--lang pt-br` ou espanhol com `--lang es`. Os bancos EN e ES traduzem as opções de resposta; [options.json](options.json) mapeia as opções dos três idiomas (e de formulários antigos em português com travessões nas opções) para a mesma opção canônica antes de pontuar, então o resultado não depende do idioma do formulário.
