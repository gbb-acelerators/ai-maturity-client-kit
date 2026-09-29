# Registro de alterações

🌐 [English](CHANGELOG.md) · Português (Brasil) · [Español](CHANGELOG.es.md)

Todas as alterações relevantes no kit de cliente AI Maturity. As datas estão em ISO 8601.

## [2.1.0] - 2026-09-29 (cross-check de métricas DORA, framework 2.0.2)

O framework passa para 2.0.2 (veja Alterado). A escala e a pontuação não
mudam, e respostas coletadas com a 2.0.1 continuam sendo importadas,
mescladas e pontuadas.

### Adicionado

- Cross-check de métricas DORA para D9-Q2: `make dora DORA=<CSV ou JSON>
  [SERVICES=N]` roda `scripts/import_dora_metrics.py` e grava
  `output/dora-metrics.json` (uma linha por serviço e período, `baseline`
  e `current`). Com o número de serviços no escopo, a parcela de
  serviços comparados com um baseline limita D9-Q2 pelas faixas de
  cobertura. O PDF de sumário mostra isso na seção 2.2 e o guia de
  implementação lista a divergência como risco. Ele checa a cobertura da
  medição, não o desempenho de entrega. Os exemplos usam
  `scripts/fixtures/dora-metrics.mock.csv`.

### Alterado

- Framework 2.0.2: a âncora L4 do D1-Q3 pede uma avaliação por tipo de
  tarefa, como a seção 2.1 da spec afirma para Pinna et al. [49].
  `framework.v2.json`, os bancos de perguntas, os formulários, a
  calculadora, o wizard, as páginas de referência e os exemplos foram
  regenerados.

### Corrigido

- Os insights do Developer Survey em PT-BR e ES agora usam vírgula
  decimal.
- O guia de scoring v1 chamava o PE score de "Production Engineering";
  o código e os relatórios se referem à prontidão de Platform
  Engineering, e o guia agora lista as áreas v1 marcadas.
- As instruções do Learning Survey apontavam para nomes de relatórios
  v1; agora descrevem como o plano alimenta o guia de implementação v2.
  Os nomes do arquivo do plano usam `<date>` em todo lugar.
- As perguntas dos surveys em espanhol agora abrem com "¿".
- Vários docs PT-BR apontavam para a cópia em inglês de uma página que
  tem versão PT-BR.
- O log de importação do Forms usava travessão para valores vazios.
- A seção 10 da spec v2 listava ações de tooling pendentes que o kit já
  implementa; agora ela cita o script que atende cada item.
- `.github/copilot-instructions.md` mostrava flags erradas nos scripts
  de evidência (`--repos`, `--metrics`); agora usa `--path` e o arquivo
  de métricas como argumento posicional, como o Makefile.
- Os insights do Developer Survey diziam que o survey usava a mesma
  escala L0-L4 do assessment principal. Agora dizem que ele usa as faixas
  do v1, então a comparação com o v2 é pelo score. A rubrica e as
  instruções do Forms agora apontam para as perguntas v2 do
  `survey_crosswalk`, e não para capabilities do v1.
- Os bancos EN e ES do Developer Survey terminavam com uma seção em
  português, e os bancos EN e ES do Learning Survey tinham um bloco de
  código quebrado.
- Os docs dos surveys e a ajuda do script de relatório não citam mais a
  antiga pasta `kit-cliente/`.
- O quick start e o FAQ do site ainda descreviam o exemplo v1
  (`cp responses.json.example`, Cliente Exemplo S.A.) e a importação v1
  que faz média das linhas. Agora mostram `make demo`, `make init`,
  `make import` e `make merge`, e a importação v2 que mantém cada
  respondente.
- O repositório mudou para `gbb-acelerators/ai-maturity-client-kit`. O
  site, suas tags de SEO e os docs agora usam
  `https://gbb-acelerators.github.io/ai-maturity-client-kit/`; a URL
  antiga do Pages retorna 404.

## [2.0.2] - 2026-09-29 (nomes de arquivos e pastas em inglês)

O framework (perguntas, escala e pontuação) não muda: continua 2.0.1.

### Alterado

- Todos os nomes de arquivos e pastas estão em inglês. As cópias de
  idioma só acrescentam `.pt-br` ou `.es` antes da extensão. Renomeações:

| Antes | Agora |
| --- | --- |
| `coleta/` | `collection/` |
| `formularios/` | `forms/` |
| `referencia/`, `referencia/dimensoes/`, `referencia/exemplo-saida/` | `reference/`, `reference/dimensions/`, `reference/sample-output/` |
| `relatorios/` | `reports/` |
| `saida/` | `output/` |
| `respostas.json`, `respostas.json.example`, `respostas.v2.json.example` | `responses.json`, `responses.json.example`, `responses.v2.json.example` |
| `respostas-forms.xlsx`, `respostas-survey-devs.xlsx`, `respostas-survey-learning.xlsx` | `forms-responses.xlsx`, `survey-devs-responses.xlsx`, `survey-learning-responses.xlsx` |
| `GUIA-PASSO-A-PASSO.md` | `STEP-BY-STEP.md` |
| `INSTRUCOES-FORMS.md`, `INSTRUCOES-FORMS-DEVS.md`, `INSTRUCOES-FORMS-LEARNING.md` | `FORMS-INSTRUCTIONS.md`, `FORMS-INSTRUCTIONS-DEVS.md`, `FORMS-INSTRUCTIONS-LEARNING.md` |
| `perguntas-para-forms.md` (PT-BR), `.en.md`, `.es.md` e os bancos `-devs` e `-learning` | `question-bank.md` (EN), `.pt-br.md`, `.es.md` e os bancos `-devs` e `-learning` |
| `RUBRICA-MATURIDADE.md` | `MATURITY-RUBRIC.md` |
| `pontuacao-e-calculo.md` e `.xlsx`, `calculadora-pontuacao.html` | `scoring-and-calculation.md` e `.xlsx`, `scoring-calculator.html` |
| v1 `P1-produtividade-do-desenvolvedor`, `P2-ciclo-de-vida-devops`, `P3-plataforma-de-aplicações` | `P1-developer-productivity`, `P2-devops-lifecycle`, `P3-application-platform` |
| `recomendacoes.json`, `telemetria.json`, `comparacao-rodadas.*` | `recommendations.json`, `telemetry.json`, `round-comparison.*` |
| `pontuacao-v2-<date>.xlsx`, `pontuacao-preenchida-<date>.xlsx` | `scoring-v2-<date>.xlsx`, `scoring-v1-<date>.xlsx` |
| `maturidade-developer-survey-<date>.json`, `plano-capacitacao-<date>.md`, `*-EXEMPLO.*` | `developer-survey-maturity-<date>.json`, `training-plan-<date>.md`, `*-EXAMPLE.*` |
| `merge_offline_respostas.py`, `calcular_maturidade.py`, `gerar_insights.py`, `gerar_plano_capacitacao.py`, `auto_fill_from_plano.py` | `merge_offline_responses.py`, `calculate_maturity.py`, `generate_insights.py`, `generate_training_plan.py`, `auto_fill_from_plan.py` |
| `/calcular-scores`, `/gerar-relatorio`, `/importar-respostas-excel`, `/importar-survey-devs`, `/importar-survey-learning` | `/calculate-scores`, `/generate-report`, `/import-responses`, `/import-survey-devs`, `/import-survey-learning` |
| `/plano-capacitacao`, `/preencher-planilha`, `/recomendar-estrategias`, `/wizard-implementacao`, `/pipeline-completo` | `/training-plan`, `/fill-workbook`, `/recommend-strategies`, `/implementation-wizard`, `/full-pipeline` |
| `make clean-saida`, `--respostas`, `--plano` | `make clean-output`, `--responses`, `--plan` (as flags antigas continuam funcionando) |

- Os bancos de perguntas seguem a convenção dos docs: o arquivo base é
  em inglês, com cópias `.pt-br.md` e `.es.md` e uma linha de idioma.
  Todo pacote continua levando os três bancos.
- `kit-en/`, `kit-es/` e `scripts/build_kit_docs.py` foram removidos:
  todos os pacotes agora têm os mesmos nomes de arquivos e pastas, com o
  seu idioma nos nomes base.
- O código também usa nomes em inglês (por exemplo, o `responses.json`
  lido é `responses_doc`), e o auto-fill do wizard grava
  `metadata.source_plan` em vez de `source_plano`.

### Compatibilidade

- Um `respostas.json` de um kit antigo continua sendo lido quando não
  existe `responses.json` (os scripts mostram um aviso pedindo para
  renomear).
- O `.gitignore` e o gerador de pacotes continuam excluindo os nomes
  antigos dos arquivos do cliente e a antiga pasta `saida/`, então dados
  antigos de clientes nunca entram em commits nem em pacotes.

## [2.0.1] - 2026-09-28 (framework v2)

### Adicionado

- Guia de implementação v2 (`v2_implementation_guide.pdf`, o quinto PDF de v2):
  governança, responsáveis por dimensão, um plano em fases por prioridade com
  as perguntas de menor score, âncoras L3 de "pronto quando", evidência a
  coletar e KPIs, gestão da mudança, riscos derivados dos flags de pontuação
  mais o registro de riscos do cliente, métricas de sucesso e os primeiros 90
  dias. Campos vazios do wizard mostram "to fill with the client".
- Wizard do guia de implementação e calculadora de pontuação regenerados a
  partir de `framework.v2.json` por `scripts/generate_v2_tools_html.py`,
  trilíngues (EN, PT-BR, ES) e offline. O wizard tem 11 campos (novos:
  `dimension_owners`, `risk_register`); a calculadora é uma visão what-if da
  seção 8 (pesos, alvos, prioridades, estratégias, risco de amplificação) com
  um teste de paridade contra o motor. O template
  `wizard/implementation-guide-inputs.template.json` mantém orientação em
  `_guide` e valores vazios. `auto_fill_from_plan.py` oferece suporte a ES e
  converte o calendário e as coortes em tabelas.
- Checagens cruzadas de evidência: `scripts/scan_repos_ai_config.py`
  (`make scan-repos`) posiciona repositórios nos níveis RAMP [47] e limita
  D4-Q4 pela fração com configuração de IA versionada;
  `scripts/import_copilot_metrics.py` (`make telemetry`) lê relatórios de
  métricas de uso do Copilot [6] e limita D4-Q1 pelas fases de adoção. O PDF de
  resumo mostra ambos e sinaliza respostas acima da evidência.
- Flag de divergência entre respondentes (desvio padrão dos scores de dimensão
  por respondente de 1.0 ou mais, com ao menos 3 respondentes).
- PDF de comparação de rodadas (`make compare` renderiza
  `round-comparison.pdf`).
- `make demo` renderiza os cinco PDFs de v2 a partir do mock em `output/demo/`;
  `make merge` combina exportações de formulários offline em `responses.json`;
  `make examples-v2` regenera os exemplos de referência.
- Páginas de referência por dimensão em `reference/dimensions/` (EN, PT-BR,
  ES) e notas de escopo no guia de referência e no formulário offline.
- `survey_crosswalk` em `framework.v2.json` vincula cada dimensão do Developer
  Survey às perguntas de v2 que ela ajuda a validar; o PDF de resumo mostra o
  contexto do survey quando existe um resultado de survey.
- Workflow de CI (`.github/workflows/ci.yml`) para testes, arquivos gerados,
  pacotes, smoke tests e a demo.
- Developer Survey em três idiomas: os bancos EN e ES traduzem as opções de
  resposta, e `survey-devs/options.json` mapeia cada idioma (e opções antigas
  em português com hífens) para a mesma opção canônica, então os scores não
  dependem do idioma do formulário. Os insights mostram opções no idioma do
  relatório.
- Saída em espanhol para os scripts de survey (`--lang es`) e cabeçalhos de
  plano em espanhol no autopreenchimento do wizard; o exemplo ES agora mostra o
  fluxo completo.

- Framework v2: 9 dimensões, 61 perguntas e 5 perguntas de perfil (`R-Q1` a
  `R-Q5`), gerado a partir de
  [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md)
  para `framework.v2.json` por `scripts/spec_to_framework_v2.py`, com as
  decisões de design do kit em `framework/v2/config.json` e traduções em
  `framework/v2/i18n.{pt-br,es}.json`. JSON Schema em
  `framework.v2.schema.json`; `scripts/validate_framework_v2.py` verifica
  contagens, IDs, citações, a partição de rastreabilidade de v1, paridade de
  idioma e desatualização.
- Motor v2 (`scripts/engine_v2.py`), selecionado por
  `metadata.framework_version` em `responses.json`: respostas por respondente,
  médias agrupadas de perguntas, pesos de dimensão (0.5 a 2.0), status de
  cobertura, baixa confiança, risco de amplificação, gap de percepção e flags
  de escopo, cobertura de evidência com perguntas L3/L4 não verificadas, um top
  5 backlog com âncoras L3 e recomendações de estratégia que citam as
  referências da especificação.
- Ativos de coleta v2 de `scripts/generate_v2_collection.py`: bancos de
  perguntas em PT-BR, EN e ES, o formulário offline
  `forms/assessment-v2.html` e o template de exportação do Forms.
- Relatórios v2 (`reports/scripts/build_report_v2.py`): resumo de avaliação
  com heatmap de personas e flags, mais um roadmap por grupo de dimensões (G1 a
  G3). `make pipeline` escolhe v1 ou v2 automaticamente.
- Workbook auditável v2 (`scripts/fill_workbook_v2.py`): cada score é uma
  fórmula sobre as respostas brutas, ao lado do valor do motor.
- Comparação de rodadas (`scripts/compare_rounds.py`, `make compare`): v2 a
  v2, v1 a v1 e uma baseline indicativa de v1 a v2 por meio da linhagem de v1.
- Mock ilustrativo v2 (`responses.v2.json.example`,
  `collection/v2-mock-forms-export.xlsx`), `CHANGELOG.md` e um dev container.

- Versões completas em português do Brasil e em espanhol de todos os
  documentos, com o inglês como idioma principal: cada `X.md` tem
  `X.pt-br.md` e `X.es.md` com os mesmos títulos e uma linha de seletor com
  os três idiomas. Novas cópias em espanhol de todos os guias de pasta,
  `CHANGELOG.pt-br.md`, `CHANGELOG.es.md` e cópias PT-BR e ES da
  especificação v2 (`collection/AI-Maturity-Form-Questions_v2.pt-br.md`,
  `.es.md`).
- `scripts/sync_spec_translations.py` gera as seções 6 e 7 e a lista de
  referências das cópias da especificação a partir de `framework.v2.json` e
  checa que as seções em inglês fazem o caminho de ida e volta;
  `make generate-v2` e `make validate-docs` o executam.
- Cópias do formulário offline, do wizard e da calculadora que abrem em
  português e em espanhol (`*.pt-br.html`, `*.es.html`). O formulário
  offline agora segue o idioma do navegador, como o wizard e a calculadora.
- `scripts/test_i18n_docs.py` cobre a troca de idioma dos pacotes, as cópias
  da especificação e a cobertura dos documentos.
- O material arquivado da v1 nos três idiomas: referências dos pilares
  em espanhol (`reference/v1/P1` a `P3` `.es.md`) e instruções de Forms
  (`collection/v1/FORMS-INSTRUCTIONS.es.md`); cópias em inglês e espanhol dos
  formulários visuais da v1 (`forms/v1/*.html`, `*.es.html`, com o
  original em português em `*.pt-br.html`) e uma calculadora v1 em
  espanhol. Os docs e formulários v1 em PT-BR agora também traduzem o
  contexto e as evidências sugeridas, que estavam em inglês; os nomes de
  KPI continuam em inglês em todas as versões, como no `framework.json`.
- Cópias PT-BR e ES de `upgrade-framework-v2.prompt.md`.
- Seção "Comandos do Copilot Chat" no README, nos três idiomas.

### Alterado

- As dimensões do Developer Survey são `DS-D2` a `DS-D8` nas saídas e no banco
  do Learning Survey, então elas não colidem mais com as dimensões v2; Forms
  criados com o texto antigo ainda são processados. A rubrica do survey afirma
  que mantém as faixas de v1.
- `kit-en/` é gerado a partir da documentação em inglês
  (`scripts/build_kit_docs.py`); os pacotes incluem cada documento no seu
  idioma e o build falha com links relativos quebrados.
- Comparações de faixa e prioridade ignoram ruído de ponto flutuante abaixo de
  1e-9 no motor, na calculadora e nas fórmulas do workbook.
- PT-BR e ES: opções de perfil traduzidas, nomes de dimensão mais claros (D4,
  D5, D6) e decimais com vírgula nos PDFs.
- Todo auxiliar HTML usa o logotipo de quatro quadrados da Microsoft.
- Bancos de survey, templates de exportação e documentação de survey não usam
  mais travessões ou meia-riscas; o Markdown de survey gerado passa no Markdown
  lint e mostra emails como links.
- Especificação v2.0.1: títulos de formulário começam com o ID da pergunta;
  regras de pontuação foram tornadas precisas (faixas semiabertas, dimensões
  vazias, pesos, cobertura, grupos de gap de percepção, amostra mínima, ressalva
  de escopo, regra de evidência); correções de citação e rastreabilidade (99
  consolidadas + 59 perguntas de v1 aposentadas); sem travessões ou
  meia-riscas.
- `make init` agora começa pelo exemplo v2; `make init-v1` mantém o fluxo v1.
- Papel de autor em cada saída: "Global Developer Solutions Advisor".
- `scripts/import_forms_excel.py` detecta exportações v2 e mantém cada
  respondente, respostas de perfil em qualquer um dos três idiomas e respostas
  NA explícitas.

- O pacote ES entrega todos os documentos em espanhol com os nomes base dos
  arquivos, como o pacote PT faz em português. `kit-es/` é gerado a partir
  das cópias `.es.md`, e nenhum pacote entrega as pastas `kit-en/` ou
  `kit-es/`. A especificação v2 e os bancos de perguntas vão nos três
  idiomas em todos os pacotes.
- `scripts/check_language_coverage.py` exige as cópias PT-BR e ES de todo
  documento no escopo, com os mesmos títulos e linhas de seletor, e lista o
  que fica em inglês por design: `.github/`, o arquivo congelado da v1 (EN e
  PT-BR), o plano interno da v2 e as saídas geradas.
- Os textos gerados em espanhol (banco de perguntas, guia de referência)
  usam o registro "tú", e o banco em espanhol aponta para as instruções de
  Forms em espanhol. A referência de pontuação em PT-BR não usa mais
  travessões (em dash ou en dash).
- O agente, as instruções e o prompt de pipeline do Copilot respondem no
  idioma de quem usa e geram as saídas no idioma do cliente
  (`metadata.language`, `--lang`); as descrições das skills também listam
  frases de acionamento em espanhol. Os arquivos de `.github/` continuam
  em inglês porque quem os lê é o modelo.
- Os bancos de perguntas v1 em EN e ES trazem as perguntas e os nomes de
  pilares e capabilities no próprio idioma (o importador mapeia as colunas
  pelo ID), com opções sem travessões.
- `check_language_coverage.py` exige os três idiomas também para os docs
  da v1 e verifica que todo assistente HTML tem as cópias `.pt-br.html` e
  `.es.html`.

### Corrigido

- As listas de referência v2 eram numeradas sequencialmente em vez de pelo
  número de referência, então citações e números de lista não correspondiam.
- Os pacotes EN e ES enviavam seus guias raiz com links `../` quebrados.
- Os insights do Developer Survey apontavam para capacidades de v1; agora
  apontam para perguntas de v2.
- `calculate_maturity.py --lang pt-br` falhava em uma dimensão sem dados
  (chave de texto ausente).
- Seis arquivos `SKILL.md` tinham front matter YAML inválido.
- `reference/scoring-and-calculation.xlsx` armazenava texto explicativo como
  fórmulas quebradas.
- A calculadora v1 e o banco de perguntas v1 em inglês mostravam as
  perguntas em português; algumas perguntas v1 em inglês listavam o
  público "Arquiteto".
- Os READMEs do exemplo v1 em `reference/sample-output/v1/en/` e `es/`
  estavam no idioma errado ou apontavam para caminhos antigos.
- A calculadora v1 nunca atualizava os scores dos pilares e o geral depois
  da primeira resposta (os cards dos pilares perdiam as classes de
  marcação), e os formulários visuais v1 apontavam para um CSS de branding
  inexistente.
- Os docs, o banco de perguntas, as instruções de Forms, os formulários
  visuais e a calculadora da v1 em português não usam mais travessões (em
  dash ou en dash) como separadores.

### Arquivado

- Bancos de perguntas, instruções e template de v1 em `collection/v1/`, os
  formulários HTML de v1 em `forms/v1/`, as referências de pilares de v1
  e a calculadora de v1 em `reference/v1/`. Arquivos v1 ainda são pontuados e
  renderizados sem alterações.

## [1.x] - 2026-05 to 2026-09

- Motor determinístico, importador de Forms e workbook com testes golden; PDFs
  de cliente sem fatos de exemplo; aviso de privacidade para o Learning Survey;
  inglês como idioma padrão com cópias PT-BR; limpeza de branches (somente
  `main` e `develop`).
