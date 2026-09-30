# Kit AI Maturity Assessment

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

Kit autônomo para conduzir uma autoavaliação de maturidade do SDLC assistido por IA sem depender de uma plataforma web. O framework v2 é o fluxo padrão. O framework v1 continua arquivado e suportado para entradas históricas.

Papel da autora: Global Developer Solutions Advisor.

Versão atual: kit 2.1.0 com framework 2.0.2. Veja [CHANGELOG.md](CHANGELOG.pt-br.md) para o histórico de versões.

## Como obter o kit

- Site: <https://gbb-acelerators.github.io/ai-maturity-client-kit/> (em inglês, português do Brasil e espanhol).
- Baixe um pacote pronto para uso, sem precisar de conta no GitHub: [English](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip), [Português (Brasil)](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-pt.zip), [Español](https://gbb-acelerators.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip). Cada pacote traz o seu idioma com os nomes de arquivo base.
- Ou clone o repositório: `git clone https://github.com/gbb-acelerators/ai-maturity-client-kit.git`.

Requisitos:

- Python 3 (o CI usa 3.12). `make install-deps` instala `jinja2`, `weasyprint`, `openpyxl` e `jsonschema`. O WeasyPrint também precisa das bibliotecas do Pango: `brew install pango` no macOS, ou os pacotes que o CI instala no Linux e no WSL (`libpango-1.0-0`, `libpangoft2-1.0-0`, `libharfbuzz-subset0`, `fonts-dejavu-core`).
- Ou abra o repositório clonado no dev container (`.devcontainer/`), que instala tudo e roda os testes.
- Para os comandos do Copilot Chat: VS Code com GitHub Copilot, em modo Agent.

## O que há de novo no framework v2

- Versão: 2.0.2 (veja o [changelog da especificação](collection/AI-Maturity-Form-Questions_v2.pt-br.md#changelog)).
- Especificação: [collection/AI-Maturity-Form-Questions_v2.pt-br.md](collection/AI-Maturity-Form-Questions_v2.pt-br.md), tradução da fonte em inglês [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md).
- Modelo: [framework.v2.json](framework.v2.json), validado por [framework.v2.schema.json](framework.v2.schema.json) e [scripts/validate_framework_v2.py](scripts/validate_framework_v2.py).
- 5 perguntas de perfil e 61 perguntas pontuadas.
- 9 dimensões: D1 Estratégia, Política e Governança de IA (7), D2 Habilitação, Habilidades e Cultura (6), D3 Planejar, Especificar e Desenhar (6), D4 Código e engenharia de contexto (8), D5 Revisão, qualidade e testes (7), D6 Segurança e cadeia de suprimentos de IA (7), D7 Entregar e Operar (6), D8 Fundamentos de Engenharia (amplificadores de IA) (7), D9 Medição, Valor e AI FinOps (7).
- IDs usam `D#-Q#`. Perguntas de perfil usam `R-Q1` a `R-Q5`.
- Níveis: L0 Não iniciado, L1 Explorando, L2 Adotando, L3 Escalando, L4 Nativo em IA, mais `NA`.
- Formulário principal: [forms/assessment-v2.html](forms/assessment-v2.pt-br.html). Ele roda offline, mostra a nota de escopo de cada pergunta e exporta um respondente por `responses.json`.
- Instruções do Forms: [collection/FORMS-INSTRUCTIONS.pt-br.md](collection/FORMS-INSTRUCTIONS.pt-br.md).
- Páginas de referência por dimensão ficam em [reference/dimensions/](reference/dimensions/) com páginas EN, PT-BR e ES para D1 a D9.

## Quickstart

Caminho mais rápido para o primeiro PDF depois de `make install-deps`, ou dentro do dev container:

```bash
make demo
open output/demo/*.pdf
```

Use `DEMO_LANG=en`, `DEMO_LANG=pt-BR` ou `DEMO_LANG=es` para escolher o idioma da demonstração. A demonstração grava saídas ilustrativas em `output/demo/` e não toca em `responses.json`.

Fluxo real do assessment:

```bash
make install-deps
# Colete pelo Microsoft Forms, ou colete exports offline e una os arquivos:
make merge DIR=exports/
# Ou importe uma exportação do Microsoft Forms:
make import XLSX=forms-responses.xlsx
make pipeline
# Cross-checks opcionais de evidência:
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
# Preencha implementation-guide-inputs.json com o wizard, depois renderize de novo:
make pipeline
```

Comandos diretos continuam disponíveis para automação:

```bash
python3 scripts/import_forms_excel.py forms-responses.xlsx
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 reports/scripts/build_payload_and_render.py
```

## Saídas do v2

| Saída | Uso |
| --- | --- |
| `output/scores.json` | Scores por pergunta, dimensão, persona e geral quando gerados pelo engine. |
| `output/gaps.json` | Gaps de dimensão, prioridades, flags, divergência entre respondentes e insumos de backlog. |
| `output/recommendations.json` | Recomendações de estratégias `S1` a `S7`. |
| `output/scoring-v2-<date>.xlsx` | Planilha auditável com fórmulas e conferência do engine. |
| `output/payload_v2.json` | Payload do relatório para inspeção e customização. |
| `output/v2_assessment_summary.pdf` | Sumário executivo, incluindo cross-checks de evidência quando disponíveis. |
| `output/v2_roadmap_g1.pdf` | G1: D1, D2, D9. |
| `output/v2_roadmap_g2.pdf` | G2: D3, D4, D5. |
| `output/v2_roadmap_g3.pdf` | G3: D6, D7, D8. |
| `output/v2_implementation_guide.pdf` | Parte 4 do v2: governança, RACI, plano por fases, gestão da mudança, riscos, métricas, primeiros 90 dias e referências. |
| `output/round-comparison.pdf` | Relatório de comparação gerado por `make compare BEFORE=old.json AFTER=responses.json`. |
| `output/repo-scan.json` | Scan de repositórios para o cross-check de D4 (`make scan-repos`). |
| `output/telemetry.json` | Resumo das métricas de uso do Copilot para os cross-checks de D4-Q1 e D9-Q1 (`make telemetry`). |
| `output/dora-metrics.json` | Cobertura das métricas DORA para o cross-check de D9-Q2 (`make dora`). |
| `output/developer-survey-maturity-<date>.json`, `output/insights-developer-survey-<date>.md` | Maturidade e insights do Developer Survey. |
| `output/training-plan-<date>.md` | Plano de capacitação do Learning and Growth Survey. |

`make pipeline` renderiza os 5 PDFs v2. O v1 ainda renderiza seu conjunto arquivado de 5 PDFs.

## Resumo de pontuação

Os scripts são a fonte da verdade. Não calcule scores manualmente.

- Score da pergunta: média agrupada dos níveis dos respondentes, excluindo vazio e `NA`.
- Score da dimensão: média dos scores das perguntas.
- Geral: média ponderada das dimensões.
- Pesos de dimensão padrão `1.0`, com valores de `0.5` a `2.0` em `responses.json`.
- Cobertura: OK com 37 ou mais perguntas respondidas, WARNING de 25 a 36, BLOCKED abaixo de 25.
- Prioridade: `peso da dimensão x gap`; P0 em `>= 2.4`, P1 em `>= 1.6`, P2 em `>= 0.9`, senão P3. Comparações de banda e prioridade ignoram ruído de ponto flutuante abaixo de `1e-9`.
- Divergência entre respondentes: uma dimensão é sinalizada quando pelo menos 3 respondentes têm score e o desvio padrão dos scores próprios da dimensão é 1,0 ou mais.

## Cross-checks de evidência

Três insumos opcionais ajudam a desafiar respostas superconfiantes. Eles não mudam os scores.

- `make scan-repos REPOS=~/src` examina clones locais usando apenas arquivos commitados. `make scan-repos ORG=<github-org>` examina branches padrão pela API REST do GitHub e exige `GITHUB_TOKEN` ou `GH_TOKEN`. Saída: `output/repo-scan.json`. O scan posiciona repositórios nos níveis RAMP L1 a L4 como aproximação baseada em padrões. A fração de repositórios em L2+ limita D4-Q4 pelas bandas de cobertura, e a fração em L3+ aparece ao lado de D4-Q5.
- `make telemetry METRICS=<Copilot usage metrics report JSON/NDJSON> [SEATS=200]` grava `output/telemetry.json`. Ele lê exports de métricas de uso do GitHub Copilot e classifica fases de adoção: No Cohort, Phase 1 Code first, Phase 2 Agent first, Phase 3 Multi-agent. O próprio export é evidência para D9-Q1.
- `make dora DORA=<CSV ou JSON> [SERVICES=40]` grava `output/dora-metrics.json`. Ele lê uma linha por serviço e período (`baseline` antes da adoção de IA, `current`) com frequência de deploy, lead time, taxa de falha de mudanças e tempo de restauração. Com `SERVICES`, a parcela de serviços comparados com um baseline limita D9-Q2 pelas faixas de cobertura. Ele checa a cobertura da medição, não o desempenho de entrega.

A seção 2.2 do PDF de sumário mostra os cross-checks e sinaliza respostas acima do que a evidência suporta. O guia de implementação lista essas divergências como riscos. Se os arquivos não existirem, o relatório explica como produzi-los.

## Surveys complementares

O Developer Survey e o Learning and Growth Survey são sinais complementares. Resultados de survey nunca mudam os scores v2.

- Dimensões do Developer Survey são nomeadas como `DS-D2` a `DS-D8` nas saídas. Forms construídos com o texto antigo `D2` ainda são aceitos.
- `framework.v2.json` contém o crosswalk de cada `DS-D#` para as perguntas v2 que ele ajuda a validar.
- O PDF de sumário v2 mostra contexto do Developer Survey quando `output/developer-survey-maturity-*.json` existe.
- A rubrica do survey mantém as bandas v1, então compare por score, não pelo nome do nível.
- Scripts de survey escrevem EN, PT-BR ou ES (`--lang en|pt-br|es`). Os bancos do Developer Survey traduzem as opções de resposta em todos os idiomas; `survey-devs/options.json` as mapeia para as mesmas opções canônicas, então a nota não depende do idioma do formulário.

## Comandos do Copilot Chat

Abra a pasta do kit no VS Code com o GitHub Copilot e use o Copilot Chat no modo Agent. O assistente responde no seu idioma (inglês, português do Brasil ou espanhol) e gera as saídas no idioma do cliente (`metadata.language` em `responses.json`, `--lang` nos scripts dos surveys). Os arquivos de instrução em [.github/](.github/) ficam em inglês por design: quem lê é o modelo, não o cliente.

| Comando | O que faz |
| --- | --- |
| `@ai-maturity-assistant` | Agente concierge: verifica o workspace e executa ou sugere o próximo passo. |
| `/full-pipeline` | Pipeline completo, do `responses.json` até a planilha e os PDFs. |
| `/ai-maturity-reports` | Wrapper do pipeline de relatórios (v2 por padrão, entradas v1 arquivadas suportadas). |
| `/import-responses` | Importa um export do Microsoft Forms ou une exports do formulário offline em `responses.json`. |
| `/calculate-scores` | Calcula os scores com o engine determinístico. |
| `/gap-analysis` | Calcula gaps e prioridades de P0 a P3. |
| `/recommend-strategies` | Mapeia as prioridades para as estratégias S1 a S7. |
| `/fill-workbook` | Preenche a planilha auditável. |
| `/implementation-wizard` | Coleta as 11 entradas do guia de implementação (wizard, manual ou auto-fill). |
| `/generate-report` | Gera os relatórios em PDF. |
| `/import-survey-devs` | Importa o Developer Survey anônimo. |
| `/insights-developer-survey` | Gera o relatório de insights do Developer Survey. |
| `/import-survey-learning` | Importa o Learning and Growth Survey. |
| `/training-plan` | Gera o plano de capacitação a partir do Learning Survey. |

## Arquivo v1

O v1 continua suportado para arquivos sem `metadata.framework_version`, ou com versão `1.x`. Ele usa [framework.json](framework.json), 158 perguntas, 3 pilares e ativos arquivados:

- [collection/v1/](collection/v1/)
- [forms/v1/](forms/v1/)
- [reference/v1/](reference/v1/)

Use `make init-v1` para iniciar uma entrada v1. Os scripts de despacho preservam o comportamento v1.

## Mapa do repositório

| Caminho | Uso |
| --- | --- |
| [collection/](collection/) | Instruções v2, especificação v2, bancos gerados, orientação de merge offline e arquivo v1. |
| [forms/](forms/) | Formulário offline v2 e formulários visuais v1 arquivados. |
| [framework/v2/](framework/v2/) | Traduções PT-BR e ES e as escolhas de design do kit que o `make generate-v2` junta no `framework.v2.json`. |
| [reference/](reference/) | Guia do framework, calculadora v2, páginas por dimensão, branding e exemplos. |
| [reports/](reports/) | Renderer, templates, localização, PDF de comparação e parser de entradas do wizard. |
| [scripts/](scripts/) | Scripts determinísticos de importação, scoring, planilha, comparação, validação, demo, evidências, empacotamento e geração. |
| [survey-devs/](survey-devs/) | Developer Survey anônimo: bancos de perguntas, instruções do Forms, rubrica, scripts e mock. |
| [survey-learning/](survey-learning/) | Learning and Growth Survey identificado: bancos de perguntas, instruções do Forms, scripts e mock. |
| [wizard/](wizard/) | Wizard trilingue gerado do guia de implementação e script de auto-fill. |
| [.github/](.github/) | Agente, prompt e skills do Copilot que chamam os scripts determinísticos. O repositório também guarda aqui os workflows de CI, Pages e release. |
| `docs/` | Site do GitHub Pages (só no repositório): landing page em EN, PT-BR e ES, e os ZIPs públicos gerados no deploy. |
| `output/` | Arquivos gerados. O git os ignora e os pacotes não os incluem. |

## Idiomas

O inglês é o idioma principal. Todo documento tem uma cópia em português do Brasil (`X.pt-br.md`) e uma em espanhol (`X.es.md`), com links na linha de idioma do topo. Os bancos de perguntas, a especificação v2, os assistentes HTML (formulário offline, wizard e calculadora), os relatórios e as saídas dos surveys funcionam em EN, PT-BR e ES. Os pacotes PT e ES entregam todos os documentos no seu idioma com os nomes base dos arquivos. O material arquivado da v1 (docs de referência, instruções de Forms, bancos de perguntas, formulários visuais e calculadora) e o registro do plano de upgrade para a v2 também estão nos três idiomas. Só os arquivos de customização do Copilot em `.github/` ficam em inglês, por design; mesmo assim o assistente responde no idioma de quem usa (veja [Comandos do Copilot Chat](#comandos-do-copilot-chat)). `make validate-docs` falha se faltar uma cópia ou se os títulos dela divergirem do documento em inglês. Todos os nomes de arquivos e pastas estão em inglês; uma cópia de idioma só acrescenta `.pt-br` ou `.es` antes da extensão. Kits anteriores à 2.0.2 usavam nomes em português (por exemplo `coleta/` e `respostas.json`): o [CHANGELOG](CHANGELOG.pt-br.md) lista todas as renomeações, e um `respostas.json` de um kit antigo continua sendo lido.

## Validação

```bash
make validate-docs
make test
make smoke
make smoke-cross
```

O CI roda os testes, as checagens de documentação e de arquivos gerados, os smoke tests v1 e v2 e a demo em todo push e pull request para `main` e `develop`. Todo push em `main` também publica o site com ZIPs novos, e um push que muda arquivos do kit publica uma release `kits-<run>` com os mesmos ZIPs. Rode as checagens localmente antes de fazer push.

## Licença

Este kit é distribuído sob a [licença MIT](LICENSE).
