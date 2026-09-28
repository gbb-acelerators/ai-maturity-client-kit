# Kit AI Maturity Assessment

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

Kit autônomo para conduzir uma autoavaliação de maturidade do SDLC assistido por IA sem depender de uma plataforma web. O framework v2 é o fluxo padrão. O framework v1 continua arquivado e suportado para entradas históricas.

Papel da autora: Global Developer Solutions Advisor.

Veja [CHANGELOG.md](CHANGELOG.md) para o histórico de versões.

## O que há de novo no framework v2

- Versão: 2.0.1.
- Especificação: [coleta/AI-Maturity-Form-Questions_v2.pt-br.md](coleta/AI-Maturity-Form-Questions_v2.pt-br.md), tradução da fonte em inglês [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- Modelo: [framework.v2.json](framework.v2.json), validado por [framework.v2.schema.json](framework.v2.schema.json) e [scripts/validate_framework_v2.py](scripts/validate_framework_v2.py).
- 5 perguntas de perfil e 61 perguntas pontuadas.
- 9 dimensões: D1 Estratégia, Política e Governança de IA (7), D2 Habilitação, Habilidades e Cultura (6), D3 Planejar, Especificar e Desenhar (6), D4 Código e engenharia de contexto (8), D5 Revisão, qualidade e testes (7), D6 Segurança e cadeia de suprimentos de IA (7), D7 Entregar e Operar (6), D8 Fundamentos de Engenharia (amplificadores de IA) (7), D9 Medição, Valor e AI FinOps (7).
- IDs usam `D#-Q#`. Perguntas de perfil usam `R-Q1` a `R-Q5`.
- Níveis: L0 Não iniciado, L1 Explorando, L2 Adotando, L3 Escalando, L4 Nativo em IA, mais `NA`.
- Formulário principal: [formularios/assessment-v2.html](formularios/assessment-v2.pt-br.html). Ele roda offline, mostra a nota de escopo de cada pergunta e exporta um respondente por `respostas.json`.
- Instruções do Forms: [coleta/INSTRUCOES-FORMS.pt-br.md](coleta/INSTRUCOES-FORMS.pt-br.md).
- Páginas de referência por dimensão ficam em [referencia/dimensoes/](referencia/dimensoes/) com páginas EN, PT-BR e ES para D1 a D9.

## Quickstart

Caminho mais rápido para o primeiro PDF depois de `make install-deps`, ou dentro do dev container:

```bash
make demo
open saida/demo/*.pdf
```

Use `DEMO_LANG=en`, `DEMO_LANG=pt-BR` ou `DEMO_LANG=es` para escolher o idioma da demonstração. A demonstração grava saídas ilustrativas em `saida/demo/` e não toca em `respostas.json`.

Fluxo real do assessment:

```bash
make install-deps
# Colete pelo Microsoft Forms, ou colete exports offline e una os arquivos:
make merge DIR=exports/
# Ou importe uma exportação do Microsoft Forms:
make import XLSX=respostas-forms.xlsx
make pipeline
# Cross-checks opcionais de evidência:
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
# Preencha implementation-guide-inputs.json com o wizard, depois renderize de novo:
make pipeline
```

Comandos diretos continuam disponíveis para automação:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Saídas do v2

| Saída | Uso |
| --- | --- |
| `saida/scores.json` | Scores por pergunta, dimensão, persona e geral quando gerados pelo engine. |
| `saida/gaps.json` | Gaps de dimensão, prioridades, flags, divergência entre respondentes e insumos de backlog. |
| `saida/recomendacoes.json` | Recomendações de estratégias `S1` a `S7`. |
| `saida/pontuacao-v2-<date>.xlsx` | Planilha auditável com fórmulas e conferência do engine. |
| `saida/payload_v2.json` | Payload do relatório para inspeção e customização. |
| `saida/v2_assessment_summary.pdf` | Sumário executivo, incluindo cross-checks de evidência quando disponíveis. |
| `saida/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `saida/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `saida/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |
| `saida/v2_implementation_guide.pdf` | Parte 4 do v2: governança, RACI, plano por fases, gestão da mudança, riscos, métricas, primeiros 90 dias e referências. |
| `saida/comparacao-rodadas.pdf` | Relatório de comparação gerado por `make compare BEFORE=old.json AFTER=respostas.json`. |

`make pipeline` renderiza os 5 PDFs v2. O v1 ainda renderiza seu conjunto arquivado de 5 PDFs.

## Resumo de pontuação

Os scripts são a fonte da verdade. Não calcule scores manualmente.

- Score da pergunta: média agrupada dos níveis dos respondentes, excluindo vazio e `NA`.
- Score da dimensão: média dos scores das perguntas.
- Geral: média ponderada das dimensões.
- Pesos de dimensão padrão `1.0`, com valores de `0.5` a `2.0` em `respostas.json`.
- Cobertura: OK com 37 ou mais perguntas respondidas, WARNING de 25 a 36, BLOCKED abaixo de 25.
- Prioridade: `peso da dimensão x gap`; P0 em `>= 2.4`, P1 em `>= 1.6`, P2 em `>= 0.9`, senão P3. Comparações de banda e prioridade ignoram ruído de ponto flutuante abaixo de `1e-9`.
- Divergência entre respondentes: uma dimensão é sinalizada quando pelo menos 3 respondentes têm score e o desvio padrão dos scores próprios da dimensão é 1,0 ou mais.

## Cross-checks de evidência

Dois insumos opcionais ajudam a desafiar respostas superconfiantes. Eles não mudam os scores.

- `make scan-repos REPOS=~/src` examina clones locais usando apenas arquivos commitados. `make scan-repos ORG=<github-org>` examina branches padrão pela API REST do GitHub e exige `GITHUB_TOKEN` ou `GH_TOKEN`. Saída: `saida/repo-scan.json`. O scan posiciona repositórios nos níveis RAMP L1 a L4 como aproximação baseada em padrões. A fração de repositórios em L2+ limita D4-Q4 pelas bandas de cobertura, e a fração em L3+ aparece ao lado de D4-Q5.
- `make telemetry METRICS=<Copilot usage metrics report JSON/NDJSON> [SEATS=200]` grava `saida/telemetria.json`. Ele lê exports de métricas de uso do GitHub Copilot e classifica fases de adoção: No Cohort, Phase 1 Code first, Phase 2 Agent first, Phase 3 Multi-agent. O próprio export é evidência para D9-Q1.

A seção 2.2 do PDF de sumário mostra os dois cross-checks e sinaliza respostas acima do que a evidência suporta. O guia de implementação lista essas divergências como riscos. Se os arquivos não existirem, o relatório explica como produzi-los.

## Surveys complementares

O Developer Survey e o Learning and Growth Survey são sinais complementares. Resultados de survey nunca mudam os scores v2.

- Dimensões do Developer Survey são nomeadas como `DS-D2` a `DS-D8` nas saídas. Forms construídos com o texto antigo `D2` ainda são aceitos.
- `framework.v2.json` contém o crosswalk de cada `DS-D#` para as perguntas v2 que ele ajuda a validar.
- O PDF de sumário v2 mostra contexto do Developer Survey quando `saida/maturidade-developer-survey-*.json` existe.
- A rubrica do survey mantém as bandas v1, então compare por score, não pelo nome do nível.
- Scripts de survey escrevem EN, PT-BR ou ES (`--lang en|pt-br|es`). Os bancos do Developer Survey traduzem as opções de resposta em todos os idiomas; `survey-devs/options.json` as mapeia para as mesmas opções canônicas, então a nota não depende do idioma do formulário.

## Arquivo v1

O v1 continua suportado para arquivos sem `metadata.framework_version`, ou com versão `1.x`. Ele usa [framework.json](framework.json), 158 perguntas, 3 pilares e ativos arquivados:

- [coleta/v1/](coleta/v1/)
- [formularios/v1/](formularios/v1/)
- [referencia/v1/](referencia/v1/)

Use `make init-v1` para iniciar uma entrada v1. Os scripts de despacho preservam o comportamento v1.

## Mapa do repositório

| Caminho | Uso |
| --- | --- |
| [coleta/](coleta/) | Instruções v2, especificação v2, bancos gerados, orientação de merge offline e arquivo v1. |
| [formularios/](formularios/) | Formulário offline v2 e formulários visuais v1 arquivados. |
| [referencia/](referencia/) | Guia do framework, calculadora v2, páginas por dimensão, branding e exemplos. |
| [relatorios/](relatorios/) | Renderer, templates, localização, PDF de comparação e parser de entradas do wizard. |
| [scripts/](scripts/) | Scripts determinísticos de importação, scoring, planilha, comparação, validação, demo, evidências, empacotamento e geração. |
| [wizard/](wizard/) | Wizard trilingue gerado do guia de implementação e script de auto-fill. |
| [.github/skills/](.github/skills/) | Skills custom do Copilot que chamam os scripts determinísticos. |

## Idiomas

O inglês é o idioma principal. Todo documento tem uma cópia em português do Brasil (`X.pt-br.md`) e uma em espanhol (`X.es.md`), com links na linha de idioma do topo. Os bancos de perguntas, a especificação v2, os assistentes HTML (formulário offline, wizard e calculadora), os relatórios e as saídas dos surveys funcionam em EN, PT-BR e ES. Os pacotes PT e ES entregam todos os documentos no seu idioma com os nomes base dos arquivos. Ficam fora do conjunto em espanhol apenas os arquivos de customização do Copilot em `.github/` (em inglês por design), o arquivo congelado da v1 (EN e PT-BR) e o registro interno do plano v2 (`upgrade-framework-v2.prompt.md`). `make validate-docs` falha se faltar uma cópia ou se os títulos dela divergirem do documento em inglês.

## Validação

```bash
python3 scripts/build_kit_docs.py
python3 scripts/build_kit_docs.py --check
make validate-docs
make test
```

CI está configurado para testes, validação de documentação, smoke rendering e demo em push e pull requests para `main` e `develop`. GitHub Actions pode estar bloqueado por billing no repositório, então trate a validação local como obrigatória.
