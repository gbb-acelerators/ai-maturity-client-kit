---
description: Atualize o AI Maturity Client Kit do framework v1 (3 pilares, 28 capacidades, 158 perguntas) para o v2 (9 dimensões de AI-SDLC, 61 perguntas) em dados, coleta, importação, pontuação, relatórios, skills, docs e traduções.
agent: agent
---

# Atualize o AI Maturity Client Kit para o framework v2

🌐 [English](upgrade-framework-v2.prompt.md) · Português (Brasil) · [Español](upgrade-framework-v2.prompt.es.md)

> **Status (2026-09-28): executado** na branch `feature/framework-v2`. A especificação é v2.0.1 ([collection/AI-Maturity-Form-Questions_v2.pt-br.md](collection/AI-Maturity-Form-Questions_v2.pt-br.md)); as decisões D-1 a D-8 e o restante das mudanças estão listados em [CHANGELOG.pt-br.md](CHANGELOG.pt-br.md). Mantenha este arquivo como o registro do plano; execute-o novamente apenas para uma nova versão major do framework.

## Papel

Você é um engenheiro sênior e redator técnico atualizando o repositório **AI Maturity Client Kit** para o framework v2. Trabalhe com cuidado, em fases, com validação após cada fase. Pergunte antes de qualquer ação destrutiva ou ambígua.

## Entradas

| Entrada | Localização |
| --- | --- |
| Especificação v2 (fonte da verdade) | `collection/AI-Maturity-Form-Questions_v2.md` (v2.0.1) |
| Repositório do framework | este repositório (branch `develop`) |
| Remoto | `gbb-acelerators/ai-maturity-client-kit` (transferido de `paulasilvatech`) |

Leia toda a especificação v2 antes de mudar qualquer coisa. Trate estas partes como fixas, a menos que você sinalize um problema e eu aprove uma mudança: IDs e texto das perguntas, a escala de resposta e seus prefixos `L0`-`L4`/`NA`, o padrão de rótulo `Evidence (<ID>)`, as âncoras de calibração, as regras de pontuação na seção 8, a rastreabilidade v1→v2 na seção 9 e as referências.

A árvore de trabalho já tem mudanças não commitadas não relacionadas (`.DS_Store` files, `docs/styles.css`, um `scripts/__pycache__/*.pyc` excluído). Não faça stage, commit, revert nem edite essas mudanças.

## O que muda no v2 (resumo)

- 9 dimensões pontuadas (D1-D9) com 61 perguntas substituem 3 pillars / 28 capabilities / 158 questions.
- Nova seção de perfil do respondente sem pontuação: `R-Q1`-`R-Q5` (`R-Q3` é múltipla escolha).
- Escala redefinida: L0 Not started, L1 Exploring (≤25%), L2 Adopting (26-50%), L3 Scaling (51-90%), L4 AI-native (>90%). Mesmos prefixos da v1.
- Âncoras L3/L4 por pergunta, exemplos de evidência, citações de base e linhagem v1.
- Pontuação: score da dimensão = média dos scores das perguntas (NA excluído); geral = média das dimensões (pesos iguais por padrão); faixas de nível com largura 0,8; flag de baixa confiança (>30% NA); flag de risco de amplificação (D5, D6 ou D8 pelo menos uma faixa abaixo do geral); flag de diferença de percepção (executivos vs hands-on engineers por `R-Q1`); cobertura de evidência.
- Rastreabilidade: na v2.0.1, 99 perguntas v1 são consolidadas na v2 e 59 retiradas do assessment principal (partição de todas as 158, sem sobreposições). O rascunho 2.0.0 tinha 97 e 61.
- 58 referências, incluindo 14 pré-prints arXiv de 2026 e a publicação de 2026 na Management Science de Cui et al.

## Mapa do repositório (verificado em 2026-09-25)

| Área | Arquivos | Mudança esperada |
| --- | --- | --- |
| Dados do framework | `framework.json` (v1.0.0: `level_names`, `strategies`, `technologies_per_strategy`, `pillars` → `capabilities` → `questions` com `id`, `weight`, `pe`, `audience`, `kpi`) | Adicionar modelo de dados v2 (veja a Decisão D-1) |
| Dados de resposta | `responses.json`, `responses.json.example` (`metadata`, `target_overrides` indexados por capability, `responses` indexadas por ID de pergunta com `level`, `evidence`, `text_*`) | Exemplo v2 indexado por `D#-Q#`, respostas de perfil, `framework_version` |
| Entradas de implementação | `implementation-guide-inputs.json`, `wizard/implementation-guide-inputs.template.json`, `wizard/implementation-guide-wizard.html`, `wizard/scripts/auto_fill_from_plan.py` | Mapear para dimensões |
| Coleta (PT/EN/ES) | `collection/question-bank{,.pt-br,.es}.md`, `collection/FORMS-INSTRUCTIONS.md`, `collection/README.md`, `collection/template-export-forms.xlsx` | Regenerar a partir dos dados v2; 10 seções, 127 elementos |
| Formulários HTML | `forms/P1-*.html`, `forms/P2-*.html`, `forms/P3-*.html`, `forms/README.md` | Substituir por formulários v2 (perfil + D1-D9) |
| Referência de pontuação | `reference/scoring-and-calculation.md`, `reference/scoring-and-calculation.xlsx`, `reference/scoring-calculator.html` | Regras e flags v2 (engine atual: weighted capabilities, overall = SUMPRODUCT sobre todas as capabilities, pesos 1.0 em [0.5, 2.0], `priority_score = peso_capability × gap_size`) |
| Docs de referência de pilares | `reference/P1-*.md`, `reference/P2-*.md`, `reference/P3-*.md`, `reference/README.md` | Docs de referência por dimensão com base de pesquisa |
| Saídas de exemplo | `reference/sample-output/**` (scores, gaps, recommendations, payload, PDFs, XLSX, pastas EN/ES) | Regenerar a partir de um mock v2; nunca editar à mão |
| Relatórios | `reports/scripts/{build_payload_and_render,render_reports,render_smoke,branding}.py`, `reports/templates/*.j2`, `reports/templates/_print.css`, `reports/i18n/{pt-br,en,es}.json`, `reports/sample_payload.json` | Dimensões, flags, visão por persona, cobertura de evidência, referências |
| Customização do Copilot | `.github/copilot-instructions.md`, `.github/agents/ai-maturity-assistant.agent.md`, `.github/prompts/full-pipeline.prompt.md`, `.github/skills/*/SKILL.md` (12 skills: `import-responses`, `calculate-scores`, `gap-analysis`, `recommend-strategies`, `generate-report`, `ai-maturity-reports`, `fill-workbook`, `implementation-wizard`, `import-survey-devs`, `insights-developer-survey`, `import-survey-learning`, `training-plan`) | Atualizar toda referência a pillar/capability e padrão de ID |
| Surveys complementares | `survey-devs/**` (incl. `MATURITY-RUBRIC.md`, `scripts/rubric.py`), `survey-learning/**` | Apenas criar referências cruzadas; evitar perguntas duplicadas (veja D-6) |
| Docs e site | `README.md`, `STEP-BY-STEP.md`, `docs/{content.json,index.html,en/index.html,es/index.html,app.js,README.md}` | Estrutura, contagens e fluxo v2 |
| Ferramental | `Makefile` (`smoke`, `smoke-cross`, `validate-docs`, `build-kits`, `pipeline`), `scripts/{smoke_test,check_language_coverage,build_language_kits}.py`, `.github/workflows/{pages,release-zips}.yml` | Estender checks para v2 |

## Requisitos adicionais (da auditoria de 2026-09)

Estes itens estavam faltando na primeira versão deste plano e fazem parte da atualização:

- **Sem conteúdo de exemplo em relatórios de cliente (C1).** Qualquer seção de relatório sem dados do cliente é omitida ou marcada como "a preencher", nunca preenchida a partir de payloads de exemplo.
- **Pontuação determinística (C2).** Importação, scores, gaps e estratégias rodam em scripts Python com testes; as skills chamam os scripts em vez de calcular no chat.
- **IDs das perguntas nos títulos do Forms (C3).** Todo título de pergunta do Forms começa com seu ID (`D4-Q3: ...`, `R-Q1: ...`).
- **Sem colisões de ID (C4).** As dimensões do Developer Survey são nomeadas `DS-D2` a `DS-D8`; `D1` a `D9` são reservados para o assessment.
- **Uma regra de faixa por versão (C5).** A v2 usa faixas semiabertas de largura 0,8 sem gaps; o survey complementar mantém as faixas v1 e é comparado por score.
- **Privacidade (C8).** Os Forms incluem aviso de consentimento e retenção; respostas de perfil são dados pessoais; saídas ficam fora do git (`responses.json` e `implementation-guide-inputs.json` não são rastreados).
- **Amostra mínima por persona.** Resultados por persona e de diferença de percepção precisam de pelo menos 3 respondentes por grupo; grupos menores são marcados como amostra baixa.

## Regras inegociáveis

1. **Integridade factual.** Não invente métricas, benchmarks, percentuais nem descobertas de pesquisa. Toda afirmação de dados em docs, skills ou relatórios deve vir das referências v2 (com o mesmo link). Se você precisar de uma nova fonte, verifique-a na web primeiro, adicione-a às referências e me informe.
2. **Compatibilidade retroativa.** Arquivos de resposta v1 e o exemplo v1 existente ainda devem importar, pontuar e renderizar. Detecte a versão a partir de `framework_version` nos metadados de `responses.json` (use v1 como padrão quando ausente). Arquive o conteúdo v1; não o exclua.
3. **Escala e IDs.** Mantenha exatamente os prefixos de opção `L0`-`L4`/`NA` e o padrão de rótulo `Evidence (<ID>)`. IDs são `D#-Q#` (pontuados) e `R-Q#` (perfil).
4. **Fonte única da verdade.** Gere listas de perguntas, formulários, traduções e templates a partir do arquivo de dados v2 com scripts. Não mantenha três cópias de idioma à mão.
5. **Paridade trilíngue.** PT-BR, EN e ES devem ter as mesmas perguntas, âncoras e opções. Mantenha o texto em inglês da especificação como canônico; traduza PT-BR e ES fielmente; `scripts/check_language_coverage.py` deve passar.
6. **Branding.** Siga `reference/branding/` (IDENTITY, VOICE, tokens). Em material voltado à Microsoft, use o logotipo oficial de quatro quadrados da Microsoft e o título "Global Developer Solutions Advisor"; nunca o logotipo pessoal `</>`.
7. **Segurança do Git.** Trabalhe em uma nova branch `feature/framework-v2` criada a partir de `develop`. Faça commit por fase com mensagens claras. Não faça push, force-push, reescrita de histórico nem exclua branches. Pergunte antes de excluir ou mover qualquer arquivo rastreado.
8. **Saídas geradas.** Regenere PDFs, XLSX e exemplos JSON com os scripts do repo; nunca edite artefatos gerados à mão.
9. **Estilo Python.** PEP 8, type hints onde o arquivo já os usa, linhas ≤ 79 caracteres, sem novas dependências sem perguntar.

## Fase 0: descoberta e plano (pare para aprovação)

1. Leia a especificação v2, `framework.json`, `responses.json.example`, `reference/scoring-and-calculation.md`, todo `SKILL.md`, o arquivo do agente, o prompt de pipeline, `Makefile` e os scripts de relatório.
2. Crie um inventário de impacto: grep por `P[0-9]-C[0-9]+-Q[0-9]+`, `P1`/`P2`/`P3`, `pillar`/`pilar`, `capabilit`, `158`, `28 capabilities`, `3 pillars`, nomes de nível (`Inicial`, `Em Desenvolvimento`, `Definido`, `Gerenciado`, `Otimizando`). Liste cada arquivo com a mudança necessária.
3. Apresente o plano e minhas decisões em aberto abaixo, cada uma com sua recomendação e trade-offs. **Aguarde minhas respostas antes da Fase 1.**

Decisões em aberto:

| ID | Decisão | Padrão recomendado |
| --- | --- | --- |
| D-1 | Modelo de dados: estender `framework.json` ou adicionar `framework.v2.json` | Adicionar `framework.v2.json` (versão 2.0.0) e um carregador que escolhe v1/v2 por `framework_version` |
| D-2 | Engine de pontuação | Tratar cada dimensão como a unidade de pontuação (peso 1.0, intervalo permitido [0.5, 2.0]); pesos de pergunta 1.0; geral = média ponderada das dimensões, que equivale aos pesos iguais da especificação por padrão; manter `priority_score = weight × gap` por dimensão |
| D-3 | Mapeamento de `strategies` e `technologies_per_strategy` | Remapear cada uma das 7 estratégias para dimensões; mostre-me a tabela de mapeamento antes de escrevê-la |
| D-4 | Valores de `audience` das perguntas | Derivar das personas de `R-Q1` e do vocabulário de público existente; mostrar o mapeamento |
| D-5 | Campo `pe` | Explicar seu significado atual a partir do código; propor valores v2 ou removê-lo |
| D-6 | Sobreposição com `survey-devs` e `survey-learning` | Criar referência cruzada (por exemplo D2, D5-Q6, D9-Q4) em vez de duplicar perguntas |
| D-7 | Layout de arquivo v1 | Mover artefatos v1 para caminhos `v1/` (por exemplo `collection/v1/`, `forms/v1/`) e manter links funcionando |
| D-8 | Nomes de nível em PT-BR/ES | Propor traduções para Not started / Exploring / Adopting / Scaling / AI-native |

## Fase 1: modelo de dados

- Crie `framework.v2.json` com: `version`, `level_names` (EN/PT-BR/ES), `level_bands`, `coverage_bands`, `dimensions` (id, nomes em 3 idiomas, weight, strategies, questions), `profile_questions` (opções em 3 idiomas, flag `multi` para `R-Q3`), `references` (1-58 com URL), `traceability` (ID v1 → ID v2 ou `retired` com motivo).
- Cada pergunta: `id`, `weight`, `audience`, `kpi`, `text` (en/pt-br/es), `anchors.l3`, `anchors.l4` (mais `l1_l2` para D4-Q1), `evidence_examples`, `basis` (números de referência), `v1_lineage`.
- Adicione um JSON Schema (`framework.v2.schema.json`) e um script validador.
- Aceitação: 61 perguntas pontuadas (D1 7, D2 6, D3 6, D4 8, D5 7, D6 7, D7 6, D8 7, D9 7); 5 perguntas de perfil; IDs únicos; todo número em `basis` existe em `references`; a rastreabilidade cobre todos os 158 IDs v1 exatamente uma vez (99 consolidados, 59 retirados na v2.0.1).

## Fase 2: coleta

- Escreva um gerador que produza `collection/question-bank{,.pt-br,.es}.md` a partir de `framework.v2.json`, seguindo o layout da especificação (Seção 0 perfil, depois D1-D9, âncoras no subtítulo da pergunta, campo de evidência por pergunta).
- Atualize as instruções do Forms em PT/EN/ES: 10 seções, 127 elementos, as seis opções na ordem, orientação ao respondente (≥3 respondentes por persona).
- Atualize `collection/template-export-forms.xlsx` para o formato de exportação v2 (colunas de perfil, colunas de resposta `D#-Q#`, colunas `Evidence (D#-Q#)`).
- Substitua `forms/*.html` por formulários v2; mantenha v1 no caminho de arquivo da D-7.
- Crie um `responses.json.example` v2 e um mock multipersona realista para testes. Rotule todos os dados mock como ilustrativos.

## Fase 3: importação e pontuação

- `import-responses`: detectar v1 vs v2 por IDs de coluna; analisar `D#-Q#` e `R-Q#`; dar suporte a multisseleção em `R-Q3`; mapear prefixos de opção para 0-4/null; agregar por respondente e por persona; gravar `framework_version` em `responses.json`.
- `calculate-scores` mais `reference/scoring-and-calculation.{md,xlsx}` e `scoring-calculator.html`: implementar a seção 8 da especificação (scores de dimensão, geral, faixas, flags de baixa confiança, risco de amplificação e diferença de percepção, cobertura de evidência, scores por persona). Manter o caminho v1 funcionando.
- `gap-analysis` e `recommend-strategies`: trabalhar por dimensão; recomendações começam pelas perguntas com menor score e citam suas âncoras L3; recomendações devem citar referências da especificação, não benchmarks inventados.

## Fase 4: relatórios

- Atualize `build_payload_and_render.py`, templates e arquivos de i18n para dimensões, flags, heatmap de personas (dimensões × personas), cobertura de evidência e um apêndice de referências.
- Substitua o template de roadmap por pilar por um template por dimensão (ou agrupado); proponha o agrupamento antes de construí-lo.
- Regenere `reports/sample_payload.json` e todo `reference/sample-output/**` (PT/EN/ES) a partir do mock v2. Mantenha o exemplo v1 no caminho de arquivo.

## Fase 5: customização do Copilot e docs

- Atualize `.github/copilot-instructions.md`, o agente, `full-pipeline.prompt.md` e todas as 12 skills. Siga o padrão existente: agente enxuto com o workflow, conhecimento de domínio nas skills.
- Atualize `implementation-wizard` e as entradas do wizard; vincule `training-plan` a D2; faça `insights-developer-survey` criar referência cruzada para D2/D5/D9 em vez de duplicar.
- Substitua `reference/P1..P3-*.md` por docs de referência por dimensão que incluam o texto "por que importa", âncoras e base de pesquisa da especificação.
- Atualize `README.md`, `STEP-BY-STEP.md` e o site de docs (`docs/content.json` e os três `index.html`) com contagens e fluxo v2. Adicione uma entrada de changelog (pergunte onde se não houver CHANGELOG).

## Fase 6: validação (tudo deve passar)

1. `make smoke`, `make smoke-cross`, `make validate-docs`, `make build-kits`.
2. `python3 scripts/check_language_coverage.py` com zero gaps entre PT-BR/EN/ES.
3. O validador de schema e o check de rastreabilidade (158 = 99 + 59, sem sobreposição, sem gaps).
4. Fim a fim, `make pipeline` duas vezes: com o mock v2 e com o exemplo v1. Ambos devem produzir scores e relatórios.
5. Abra os PDFs regenerados e verifique quebras de página, fontes, logotipo, flags e heatmap de personas.
6. Grep por texto v1 obsoleto (`158`, `28 capabilities`, `3 pillars`, `P1-C`, nomes de nível antigos) fora do arquivo v1 e do changelog; liste tudo que restar e por quê.
7. Markdown lint e check de links internos em todos os docs alterados.

## Relatório final

Responda com:

- As decisões tomadas (D-1 a D-8) e o que você implementou para cada uma.
- Uma tabela de arquivos alterados, adicionados e arquivados agrupados por fase.
- A saída de cada comando de validação.
- Itens em aberto, riscos e qualquer coisa que você não alterou, com o motivo.
