# Kit AI Maturity Assessment

[English](README.md) | Português (Brasil)

Kit auto-servico para conduzir o AI Maturity Assessment sem depender de uma plataforma web. O framework v2 e o fluxo padrao. O framework v1 continua arquivado e suportado para entradas historicas.

Papel da autora: Global Developer Solutions Advisor.

Veja [CHANGELOG.md](CHANGELOG.md) para o historico de versoes.

## O que muda no framework v2

- Versao: 2.0.1.
- Especificacao: [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- Modelo: [framework.v2.json](framework.v2.json), validado por [framework.v2.schema.json](framework.v2.schema.json) e [scripts/validate_framework_v2.py](scripts/validate_framework_v2.py).
- 5 perguntas de perfil e 61 perguntas pontuadas.
- 9 dimensoes: D1 Estrategia, Politica e Governanca de IA (7), D2 Habilitacao, Habilidades e Cultura (6), D3 Planejar, Especificar e Desenhar (6), D4 Codigo e Engenharia de Contexto (8), D5 Revisao, Qualidade e Testes (7), D6 Seguranca e Cadeia de Suprimentos de IA (7), D7 Entregar e Operar (6), D8 Fundamentos de Engenharia (amplificadores de IA) (7), D9 Medicao, Valor e AI FinOps (7).
- IDs usam `D#-Q#`. Perguntas de perfil usam `R-Q1` a `R-Q5`.
- Niveis: L0 Nao iniciado, L1 Explorando, L2 Adotando, L3 Escalando, L4 Nativo em IA, mais `NA`.
- Formulario principal: [formularios/assessment-v2.html](formularios/assessment-v2.html).
- Instrucoes do Forms: [coleta/INSTRUCOES-FORMS.pt-br.md](coleta/INSTRUCOES-FORMS.pt-br.md).

## Quick start

```bash
make init
# Edite respostas.json, ou importe uma exportacao do Microsoft Forms:
make import XLSX=respostas-forms.xlsx
make scores
make workbook
make pipeline
```

Comandos diretos:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Saidas do v2

| Saida | Uso |
| --- | --- |
| `saida/scores.json` | Scores por pergunta, dimensao, persona e geral quando gerados pelo engine. |
| `saida/gaps.json` | Gaps de dimensao, prioridades, flags e insumos de backlog. |
| `saida/recomendacoes.json` | Recomendacoes de estrategias `S1` a `S7`. |
| `saida/pontuacao-v2-<date>.xlsx` | Planilha auditavel com formulas e conferencia do engine. |
| `saida/payload_v2.json` | Payload do relatorio para inspecao e customizacao. |
| `saida/v2_assessment_summary.pdf` | Sumario executivo. |
| `saida/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `saida/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `saida/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |

## Resumo de pontuacao

Os scripts sao a fonte de verdade. Nao calcule scores manualmente.

- Score da pergunta: media agrupada dos niveis dos respondentes, excluindo vazio e `NA`.
- Score da dimensao: media dos scores das perguntas.
- Geral: media ponderada das dimensoes.
- Pesos de dimensao padrao `1.0`, com valores de `0.5` a `2.0` em `respostas.json`.
- Cobertura: OK com 37 ou mais perguntas respondidas, WARNING de 25 a 36, BLOCKED abaixo de 25.
- Prioridade: `peso da dimensao x gap`; P0 em `>= 2.4`, P1 em `>= 1.6`, P2 em `>= 0.9`, senao P3.

## Surveys complementares

O Developer Survey e o Learning and Growth Survey nao mudaram. Quando as dimensoes do assessment e do Developer Survey aparecerem juntas, use `DS-D#` para as dimensoes do Developer Survey. O v2 cruza os surveys em D2, D5 e D9.

## Arquivo v1

O v1 continua suportado para arquivos sem `metadata.framework_version`, ou com versao `1.x`. Ele usa [framework.json](framework.json), 158 perguntas, 3 pilares e ativos arquivados:

- [coleta/v1/](coleta/v1/)
- [formularios/v1/](formularios/v1/)
- [referencia/v1/](referencia/v1/)

Use `make init-v1` para iniciar uma entrada v1. Os scripts de despacho preservam o comportamento v1.

## Mapa do repositorio

| Caminho | Uso |
| --- | --- |
| [coleta/](coleta/) | Instrucoes v2, especificacao v2, bancos gerados e arquivo v1. |
| [formularios/](formularios/) | Formulario offline v2 e formularios visuais v1 arquivados. |
| [referencia/](referencia/) | Material de referencia e exemplos. |
| [relatorios/](relatorios/) | Renderer, templates e localizacao. |
| [scripts/](scripts/) | Scripts deterministicos de importacao, scoring, planilha, comparacao, validacao e geracao. |
| [.github/skills/](.github/skills/) | Skills custom do Copilot que chamam os scripts deterministicos. |

## Validacao

```bash
make validate-v2
make validate-docs
make test
```
