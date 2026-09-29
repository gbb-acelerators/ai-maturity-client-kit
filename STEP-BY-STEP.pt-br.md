# Passo a passo: AI Maturity Assessment

🌐 [English](STEP-BY-STEP.md) · Português (Brasil) · [Español](STEP-BY-STEP.es.md)

Este guia executa o assessment v2 da coleta aos relatórios. O v1 continua disponível para entradas arquivadas.

## Quickstart

Caminho mais rápido para o primeiro PDF:

```bash
make install-deps
make demo
open output/demo/*.pdf
```

Fluxo real com cliente:

```bash
# Colete respostas pelo Microsoft Forms, ou com exports do HTML offline.
make merge DIR=exports/
# Se usar Microsoft Forms em vez dos exports offline:
make import XLSX=forms-responses.xlsx
make pipeline
# Cross-checks opcionais de evidência.
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
# Preencha implementation-guide-inputs.json com o wizard, depois renderize de novo.
make pipeline
```

## 1. Escolha o fluxo

Use v2 para novos assessments. Use v1 somente para comparação histórica ou arquivos `responses.json` sem `metadata.framework_version`.

- Especificação v2: [collection/AI-Maturity-Form-Questions_v2.pt-br.md](collection/AI-Maturity-Form-Questions_v2.pt-br.md), tradução da fonte em inglês [collection/AI-Maturity-Form-Questions_v2.md](collection/AI-Maturity-Form-Questions_v2.md).
- Formulário v2: [forms/assessment-v2.html](forms/assessment-v2.pt-br.html).
- Instruções Forms v2: [collection/FORMS-INSTRUCTIONS.pt-br.md](collection/FORMS-INSTRUCTIONS.pt-br.md).
- Páginas de dimensão v2: [reference/dimensions/](reference/dimensions/).
- Arquivo v1: [collection/v1/](collection/v1/), [forms/v1/](forms/v1/), [reference/v1/](reference/v1/).

## 2. Prepare entradas

```bash
make init
```

Isso copia `responses.v2.json.example` para `responses.json` se o arquivo ainda não existir.

Você pode importar uma exportação do Microsoft Forms:

```bash
make import XLSX=forms-responses.xlsx
```

Você também pode usar o formulário offline. Cada respondente abre [forms/assessment-v2.html](forms/assessment-v2.pt-br.html), exporta um `responses.json` e envia ao facilitador. Coloque os exports em uma pasta e rode:

```bash
make merge DIR=exports/
```

O merge atribui IDs únicos de respondente, recusa arquivos v1, recusa organizações mistas exceto com `--org` ou `--allow-mixed-org`, e faz backup de um `responses.json` existente antes de gravar o arquivo unificado.

## 3. Entenda a estrutura v2

- 5 perguntas de perfil: `R-Q1` a `R-Q5`.
- 61 perguntas pontuadas: `D#-Q#`.
- 9 dimensões: D1 Estratégia, Política e Governança de IA; D2 Habilitação, Habilidades e Cultura; D3 Planejar, Especificar e Desenhar; D4 Código e engenharia de contexto; D5 Revisão, qualidade e testes; D6 Segurança e cadeia de suprimentos de IA; D7 Entregar e Operar; D8 Fundamentos de Engenharia; D9 Medição, Valor e AI FinOps.
- Níveis: L0 Não iniciado, L1 Explorando, L2 Adotando, L3 Escalando, L4 Nativo em IA, mais `NA`.
- Páginas de referência de D1 a D9 incluem notas de escopo, âncoras, exemplos de evidência, base, contexto do Developer Survey e referências citadas.

## 4. Execute scoring determinístico

```bash
make scores
```

ou:

```bash
python3 scripts/assessment_engine.py all
```

Não calcule scores manualmente. O engine escreve:

- `output/scores.json`
- `output/gaps.json`
- `output/recommendations.json`

Cobertura é OK com 37 ou mais perguntas respondidas, WARNING de 25 a 36 e BLOCKED abaixo de 25. Divergência entre respondentes é sinalizada quando uma dimensão tem pelo menos 3 scores de respondentes e desvio padrão de 1,0 ou mais.

## 5. Crie a planilha

```bash
make workbook
```

Para v2, o dispatcher grava `output/scoring-v2-<date>.xlsx`. Ela inclui fórmulas e uma coluna de conferência do engine. As fórmulas arredondam comparações para 9 casas decimais para que limites de prioridade ignorem ruído de ponto flutuante.

## 6. Gere os relatórios

```bash
make pipeline
```

ou, depois que os scores já existirem:

```bash
python3 reports/scripts/build_payload_and_render.py
```

Arquivos v2:

- `output/v2_assessment_summary.pdf`
- `output/v2_roadmap_g1.pdf`, D1, D2, D9.
- `output/v2_roadmap_g2.pdf`, D3, D4, D5.
- `output/v2_roadmap_g3.pdf`, D6, D7, D8.
- `output/v2_implementation_guide.pdf`.
- `output/payload_v2.json`.

Entradas v1 ainda produzem o conjunto arquivado de 5 PDFs.

## 7. Adicione cross-checks de evidência

Rode qualquer um deles antes do `make pipeline` final:

```bash
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
make dora DORA=dora-metrics.csv SERVICES=40
```

A saída do scan de repositórios é `output/repo-scan.json`. A saída das métricas do Copilot é `output/telemetry.json`. A saída das métricas DORA é `output/dora-metrics.json`: uma linha por serviço e período (`baseline`, `current`), e `SERVICES` é o número de serviços no escopo. O relatório de sumário mostra uma seção Evidence cross-checks e sinaliza respostas acima do que a evidência suporta. O guia de implementação lista essas flags como riscos. Sem os arquivos, o PDF explica como produzi-los.

## 8. Preencha o wizard do guia de implementação

Abra o wizard trilingue gerado:

```bash
open wizard/implementation-guide-wizard.html
```

Ele salva 11 campos em `implementation-guide-inputs.json`: `executive_steering_committee`, `tpo`, `dimension_owners`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`, `risk_register`, `quick_wins_w1_4`, `quick_wins_w5_8` e `quick_wins_w9_12`. Campos vazios aparecem como `to fill with the client`, não como conteúdo de exemplo.

O Mode D pode preencher 7 campos a partir do plano do Learning Survey:

```bash
python3 wizard/scripts/auto_fill_from_plan.py --lang pt-br
```

Depois do wizard, rode `make pipeline` de novo.

## 9. Compare rodadas

```bash
make compare BEFORE=old-responses.json AFTER=responses.json
```

O script de comparação suporta deltas comparáveis v2 para v2, baseline indicativo v1 para v2 via `v1_lineage`, e v1 para v1. Ele grava `output/round-comparison.pdf` quando a renderização de PDF está disponível.

## 10. Use surveys complementares

Developer Survey e Learning and Growth Survey fornecem contexto. Eles não mudam scores v2.

- Dimensões do Developer Survey são `DS-D2` a `DS-D8` nas saídas.
- O PDF de sumário v2 mostra contexto do Developer Survey quando `output/developer-survey-maturity-*.json` existe.
- A saída do Learning Survey pode alimentar o Mode D do wizard de implementação.
- Scripts de survey escrevem EN, PT-BR ou ES (`--lang en|pt-br|es`) e pontuam da mesma forma formulários montados em qualquer um dos três idiomas.

## 11. Valide as fontes do repositório

```bash
make validate-v2
make validate-docs
make test
```

Veja [CHANGELOG.md](CHANGELOG.pt-br.md) para o histórico de versões.
