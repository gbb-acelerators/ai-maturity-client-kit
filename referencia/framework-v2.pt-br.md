🌐 [English](framework-v2.md) · Português (Brasil) · [Español](framework-v2.es.md)

# Framework AI Maturity v2: guia de referência

Gerado a partir de `framework.v2.json` (framework 2.0.1) por `scripts/generate_v2_reference.py`. A fonte da verdade é [a especificação v2](../coleta/AI-Maturity-Form-Questions_v2.md). Não edite este arquivo à mão.

## Método de pontuação

- Valor da resposta: L0 a L4 = 0 a 4. Respostas NA e em branco são excluídas.
- Score da pergunta: média dos valores dos respondentes.
- Score da dimensão: média dos scores das perguntas. Uma dimensão sem nenhuma pergunta respondida fica sem score.
- Geral: média ponderada das dimensões com score (pesos 1,0 por padrão, permitido de 0,50 a 2,00).
- Cobertura: OK a partir de 37 perguntas com score, WARNING a partir de 25, BLOCKED abaixo disso.
- Gap = alvo (padrão 3,00) menos score. Prioridade = peso × gap: P0 a partir de 2,40, P1 a partir de 1,60, P2 a partir de 0,90, senão P3.
- Alertas: baixa confiança (mais de 30% NA), risco de amplificação (D5, D6 ou D8 uma faixa abaixo do geral), diferença de percepção (executivos vs hands-on, ao menos 3 de cada), ressalva de escopo, L3/L4 não verificado (menos de 50% das respostas com evidência), divergência entre respondentes (desvio padrão das notas de dimensão por respondente de 1,00 ou mais, com ao menos 3 respondentes).
- Checagens cruzadas, quando os arquivos existem: o scan de repositórios (níveis RAMP [47]) limita D4-Q4 pela fração de repositórios com configuração de IA versionada, e as métricas de uso do Copilot [6] limitam D4-Q1 pelas fases de adoção. O relatório sinaliza respostas acima do que a evidência sustenta.

### Faixas de nível

| Nível | Score |
| --- | --- |
| L0 Não iniciado | [0,00; 0,80) |
| L1 Explorando | [0,80; 1,60) |
| L2 Adotando | [1,60; 2,40) |
| L3 Escalando | [2,40; 3,20) |
| L4 Nativo em IA | [3,20; 4,00] |

### Exemplo resolvido: D8 no mock ilustrativo

O mock (`respostas.v2.json.example`, 14 respondentes ilustrativos) gera estes valores, calculados por `scripts/engine_v2.py`.

| Pergunta | Score | Respostas | NA |
| --- | ---: | ---: | ---: |
| D8-Q1 Controle de versão para tudo | 1,07 | 14 | 0 |
| D8-Q2 Frequência de commit e rollback rápido | 1,23 | 13 | 1 |
| D8-Q3 Plataforma interna de qualidade | 1,29 | 14 | 0 |
| D8-Q4 Ecossistema de dados saudável | 0,92 | 13 | 1 |
| D8-Q5 Ambientes reproduzíveis para humanos e agentes | 1,00 | 14 | 0 |
| D8-Q6 Documentação como contexto pronto para IA | 1,36 | 14 | 0 |
| D8-Q7 Testes automatizados como sistema de controle | 0,75 | 12 | 2 |

Score de D8 = média dos 7 scores das perguntas = **1,09** (L1 Explorando). Gap até 3,00 = 1,91; prioridade = 1,00 × 1,91 = 1,91 → **P1 Alto**.

Geral = média dos 9 scores de dimensão = **2,04** (L2 Adotando).

## Dimensões e perguntas

### D1: Estratégia, política e governança de IA

**Por que importa:** DORA identifica uma "postura de IA clara e comunicada" como amplificadora dos benefícios da IA [1], [2]; o Microsoft CAF afirma que "todo agente deve ser observável, governado e seguro" [19].

**Página da dimensão:** [dimensoes/D1.pt-br.md](dimensoes/D1.pt-br.md)

**Estratégias:** S7, S5, S6 · **Grupo do relatório:** G1 (Direção, pessoas e valor)

#### D1-Q1: Estratégia de IA para engenharia de software

Existe uma estratégia documentada de IA para engenharia de software, patrocinada pela liderança, que declare objetivos explícitos e seja comunicada a todas as equipes de engenharia?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Estratégia publicada e revisada pelo menos anualmente; objetivos (por exemplo entrega, qualidade, developer experience) têm responsáveis; a maioria dos engenheiros consegue dizer onde encontrá-la.
- L4: A estratégia é revisada a partir de resultados medidos (D9) e vinculada a OKRs de negócio; o progresso é reportado à liderança em uma cadência fixa.

**Exemplos de evidência:** Documento de estratégia, comunicação da liderança, entradas de OKR.  
**Base:** [1] [2] [18]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q2: Política de uso aceitável

Está claro para os engenheiros como eles podem e não podem usar IA no trabalho, incluindo quais dados podem ser compartilhados com ferramentas de IA?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Política escrita de uso aceitável cobre code, dados de clientes, segredos e IP de terceiros; faz parte do onboarding; exceções têm um responsável.
- L4: A política é aplicada por controles técnicos (por exemplo content exclusion, prevenção contra perda de dados, allowlists) e auditada; violações disparam alertas automatizados.

**Exemplos de evidência:** Link da política, checklist de onboarding, configuração de controles.  
**Base:** [1] [2] [20] [21]  
**Origem na v1:** P1-C1-Q5 (parcial)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q3: Ferramentas e modelos aprovados

Existe um catálogo mantido de ferramentas, recursos e modelos de IA aprovados para desenvolvimento de software, gerenciado por políticas enterprise ou da organização?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Políticas enterprise/da organização habilitam apenas recursos e modelos aprovados; o catálogo lista responsável, tratamento de dados e data de revisão para cada ferramenta.
- L4: Novos modelos e ferramentas passam por uma avaliação definida (qualidade, custo, segurança) antes da habilitação; os descontinuados são removidos conforme cronograma.

**Exemplos de evidência:** Configurações de política do Copilot, catálogo de ferramentas, registros de avaliação de modelos.  
**Base:** [2] [15] [32] [49]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q4: Proteção de dados, IP e residência

Requisitos de residência, retenção, propriedade intelectual e privacidade de dados estão definidos e aplicados às ferramentas e agentes de IA usados no SDLC?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Requisitos são documentados por ferramenta; repositórios ou arquivos sensíveis são excluídos do contexto de IA; retenção de logs e memória segue a política.
- L4: A conformidade é avaliada continuamente (por exemplo com um compliance manager) e mapeada a regulamentações como o EU AI Act quando aplicável.

**Exemplos de evidência:** Registros de processamento de dados, configurações de exclusão, política de retenção.  
**Base:** [19] [20]  
**Origem na v1:** P1-C1-Q5 (parcial)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q5: Níveis de autonomia para trabalho com IA

A organização definiu quais tarefas são lideradas pelo desenvolvedor, conduzidas por desenvolvedor com agente, ou totalmente lideradas por agente, e os controles exigidos para cada nível?

_Nota de escopo: Mede a política que define níveis de autonomia. Como as tarefas são escritas para agentes é D3-Q3; com que frequência o trabalho é delegado é D4-Q3._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Uma matriz publicada mapeia tipos de tarefa (por exemplo upgrades de dependências, geração de testes, trabalho de feature, mudanças em produção) para níveis de autonomia e aprovações exigidas.
- L4: A matriz é aplicada por regras da plataforma (por exemplo branch protection, revisores exigidos por caminho) e atualizada a partir de dados de incidentes e qualidade.

**Exemplos de evidência:** Matriz de autonomia, rulesets de repositório, registros de mudança.  
**Base:** [7] [26] [32] [49] [56]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q6: IA responsável e framework de risco

O uso de IA em engenharia de software é governado por um padrão de IA responsável e por um framework de risco reconhecido (por exemplo Microsoft Responsible AI Standard, NIST AI RMF, ISO/IEC 42001)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Um framework nomeado é adotado; riscos relacionados a IA estão no registro de riscos com responsáveis e revisões.
- L4: Controles do framework são auditados interna ou externamente; resultados retroalimentam política e tooling.

**Exemplos de evidência:** Mapeamento do framework, entradas no registro de riscos, relatórios de auditoria.  
**Base:** [20] [21] [41] [42]  
**Origem na v1:** P3-C3-Q5 (parcial)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

#### D1-Q7: Registro e identidade de agentes

Todo agente de IA usado no SDLC (coding agents, review agents, custom agents, pipeline agents) está registrado com um responsável, um propósito, uma identidade distinta e um escopo de acesso definido?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Um único inventário lista todos os agentes com responsável, plataforma e permissões; cada agente executa sob sua própria identidade, não uma conta humana compartilhada.
- L4: Agentes não registrados ("shadow") são detectados automaticamente; o ciclo de vida de identidade (criação, revisão, remoção) é automatizado.

**Exemplos de evidência:** Inventário de agentes, configuração de identidade (por exemplo Microsoft Entra Agent ID), revisões de acesso.  
**Base:** [19] [39]  
**Origem na v1:** P3-C5-Q4 (parcial)  
**Unidade:** organization · **Público:** engineering-leader, architect, security

### D2: Capacitação, habilidades e cultura

**Por que importa:** O Gartner espera que GenAI exija que 80% da força de trabalho de engenharia se requalifique até 2027 [30]; DORA pergunta sobre treinamento, aprendizagem entre pares e suporte à experimentação [2].

**Página da dimensão:** [dimensoes/D2.pt-br.md](dimensoes/D2.pt-br.md)

**Estratégias:** S5 · **Grupo do relatório:** G1 (Direção, pessoas e valor)

#### D2-Q1: Treinamento estruturado de IA

Os engenheiros recebem treinamento estruturado nas ferramentas de IA e workflows de agentes aprovados, além do onboarding padrão do fornecedor?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Currículo baseado em função (desenvolvedor, revisor, plataforma, segurança) com conclusão rastreada; o treinamento é exigido antes que recursos de agentes sejam habilitados; ensina padrões que preservam o aprendizado (pedir explicações, tentar primeiro, depois comparar) e não apenas delegação total.
- L4: O currículo é atualizado a cada trimestre com base em dados de uso e padrões de falha; existem trilhas avançadas (orquestração de agentes, avaliação).

**Exemplos de evidência:** Trilhas de aprendizagem, taxas de conclusão, regras de bloqueio de habilitação.  
**Base:** [2] [30] [48]  
**Origem na v1:** P1-C5-Q4, P1-C3-Q6 (parcial)  
**Unidade:** engineers · **Público:** engineering-leader, developer

#### D2-Q2: Aprendizagem entre pares e champions

Existem formatos regulares de aprendizagem entre pares (demos, brown bags, office hours) e uma rede de champions de IA entre equipes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Champions existem na maioria das equipes; sessões ocorrem pelo menos mensalmente; gravações e exemplos são compartilhados em um único lugar.
- L4: Uma comunidade de prática faz curadoria de ativos reutilizáveis (instruções, arquivos de prompt, agentes) e mede sua reutilização.

**Exemplos de evidência:** Lista de champions, calendário de sessões, repositório compartilhado de exemplos.  
**Base:** [2]  
**Origem na v1:** P1-C6-Q6  
**Unidade:** teams · **Público:** engineering-leader, developer

#### D2-Q3: Suporte à experimentação

A organização dá aos engenheiros tempo, sandboxes e orçamento para experimentar com segurança novas ferramentas de IA e padrões de agentes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Ambientes em sandbox e um caminho leve de solicitação existem; experimentos são registrados e seus resultados compartilhados.
- L4: Experimentos bem-sucedidos entram no catálogo aprovado (D1-Q3) por meio de um caminho definido em semanas.

**Exemplos de evidência:** Assinaturas de sandbox, log de experimentos, registros de promoção.  
**Base:** [2]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** engineering-leader, developer

#### D2-Q4: Habilidades de engenharia de contexto

Os engenheiros são treinados para dar às ferramentas de IA o contexto correto (escopo claro da tarefa, arquivos relevantes, restrições, exemplos) e manter o contexto enxuto?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Orientações e exemplos sobre engenharia de contexto fazem parte do treinamento; equipes revisam suas instruções e prompts quanto à qualidade.
- L4: Práticas de contexto são medidas (por exemplo taxa de sucesso ou uso de tokens por tarefa) e melhoradas ao longo do tempo.

**Exemplos de evidência:** Páginas de orientação, checklists de review, métricas antes/depois.  
**Base:** [25] [30] [32]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** engineers · **Público:** engineering-leader, developer

#### D2-Q5: Papéis e trajetórias de carreira

Descrições de cargo, frameworks de carreira e expectativas de desempenho foram atualizados para engenharia assistida por IA e agentic engineering (por exemplo dirigir agentes, revisar saída de IA, engenharia de IA)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Perfis de função atualizados são publicados; avaliações de desempenho reconhecem uso efetivo de IA e qualidade de review, não volume bruto de saída.
- L4: Existem funções dedicadas (por exemplo engenheiro de IA, responsável pela plataforma de agentes) com um caminho claro de crescimento.

**Exemplos de evidência:** Framework de carreira, descrições de função.  
**Base:** [30]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** engineering-leader, developer

#### D2-Q6: Onboarding assistido por IA

Novos engenheiros usam ferramentas de IA para entender codebases e se tornarem produtivos, com tempo de ramp-up medido?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: O onboarding inclui tours de codebase guiados por IA e instruções de repositório; tempo até o primeiro PR mergeado é rastreado; novos engenheiros são avaliados em leitura de code e debugging, não apenas em saída.
- L4: Métricas de ramp-up e habilidades são comparadas entre coortes e usadas para melhorar material e instruções de onboarding.

**Exemplos de evidência:** Playbook de onboarding, dados de tempo até primeiro PR, resultados de verificação de habilidades.  
**Base:** [27] [48]  
**Origem na v1:** P1-C5-Q2, P1-C5-Q6, P1-C5-Q7  
**Unidade:** engineers · **Público:** engineering-leader, developer

### D3: Planejar, especificar e desenhar

**Por que importa:** em agentic coding, "as pessoas tomam a maior parte das decisões de planejamento (o que fazer) e Claude toma a maior parte das decisões de execução (como fazer)" [24]; a qualidade da definição da tarefa impulsiona a qualidade da saída do agente [8], [27].

**Página da dimensão:** [dimensoes/D3.pt-br.md](dimensoes/D3.pt-br.md)

**Estratégias:** S5, S3 · **Grupo do relatório:** G2 (Planejar, construir e revisar)

#### D3-Q1: IA no refinamento de backlog

IA é usada para redigir e refinar issues ou user stories, incluindo critérios de aceite, com um responsável humano que as aprova?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria das equipes usa IA para redigir ou melhorar itens de trabalho; critérios de aceite são obrigatórios antes do trabalho começar.
- L4: A qualidade dos itens de trabalho (clareza, testabilidade) é medida e vinculada a retrabalho e cycle time.

**Exemplos de evidência:** Templates de issue, exemplos de itens de trabalho, verificações de qualidade.  
**Base:** [16] [17]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** product-owner, architect, developer

#### D3-Q2: Especificação antes da implementação

Para mudanças não triviais, um plano ou especificação escrito é produzido e revisado antes que um agente de IA implemente a mudança?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Planos ou specs são armazenados no repositório ou vinculados à issue, e são revisados por um humano antes da implementação pelo agente.
- L4: Specs são o contrato para verificação automatizada (testes, checks) e são mantidas sincronizadas com o code.

**Exemplos de evidência:** Arquivos de spec, reviews de plano, PRs que referenciam specs.  
**Base:** [23] [24] [27] [58]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** product-owner, architect, developer

#### D3-Q3: Escopo de tarefas para agentes

As tarefas dadas a coding agents são bem delimitadas (pequenas, com critérios de aceite claros e ponteiros para code relevante) antes da atribuição?

_Nota de escopo: Mede como as tarefas são delimitadas para agentes. A política de autonomia é D1-Q5; o volume de delegação é D4-Q3._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Equipes seguem orientação escrita para issues prontas para agentes; tarefas grandes demais são divididas antes da atribuição.
- L4: Sucesso de tarefas de agentes e taxas de retrabalho são rastreados por tipo de tarefa e usados para refinar a orientação.

**Exemplos de evidência:** Diretrizes de tarefas para agentes, exemplos de issues, dados de taxa de sucesso.  
**Base:** [1] [8] [24] [49]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** product-owner, architect, developer

#### D3-Q4: Decisões de arquitetura e design

IA é usada para apoiar trabalho de design (análise de opções, modos de ameaça e falha, architecture decision records), enquanto as decisões permanecem com humanos responsáveis?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: ADRs são versionados; análise assistida por IA é anexada; um humano nomeado aprova cada decisão.
- L4: Agentes verificam novas mudanças contra decisões registradas e sinalizam conflitos automaticamente.

**Exemplos de evidência:** Repositório de ADR, registros de design review.  
**Base:** [8] [24] [26]  
**Origem na v1:** P1-C3-Q5, P1-C6-Q5  
**Unidade:** teams · **Público:** product-owner, architect, developer

#### D3-Q5: Foco centrado no usuário

O trabalho assistido por IA está vinculado a resultados claros para usuários e informado por feedback de usuários?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Itens de trabalho referenciam o problema do usuário e a medida de sucesso; feedback é revisado antes da priorização.
- L4: Métricas de resultado do usuário fazem parte da definition of done para entrega assistida por IA.

**Exemplos de evidência:** Briefs de produto, registros de loop de feedback, dashboards de resultados.  
**Base:** [1] [2] [3]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** product-owner, architect, developer

#### D3-Q6: Modernização assistida por IA

Ferramentas e agentes de IA são usados para entender, fazer upgrade e migrar code legado (por exemplo upgrades de framework ou runtime, migração para cloud), com resultados verificados por testes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Existe um processo repetível de modernização assistida por IA para tipos comuns de upgrade, com gates de teste.
- L4: O backlog de modernização é reduzido continuamente por agentes sob review humano, com taxas de sucesso rastreadas.

**Exemplos de evidência:** Runbooks de upgrade, PRs de migração, resultados de testes.  
**Base:** [16] [17]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** product-owner, architect, developer

### D4: Código e engenharia de contexto

**Por que importa:** GitHub mede a profundidade de adoção como uma progressão de "Code first" para "Agent first" e "Multi-agent" [6]; a Anthropic descreve contexto como "um recurso finito com retornos marginais decrescentes" [25].

**Página da dimensão:** [dimensoes/D4.pt-br.md](dimensoes/D4.pt-br.md)

**Estratégias:** S5, S6, S4 · **Grupo do relatório:** G2 (Planejar, construir e revisar)

#### D4-Q1: Profundidade do uso de IA entre superfícies

Quão profundamente os engenheiros usam IA entre superfícies: completions e edições de agentes no IDE, superfícies de agentes do GitHub (cloud agent, code review, CLI), e vários agentes juntos?

_Nota de escopo: Mede quão profundamente IA é usada. Se esse uso é medido é D9-Q1._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L1-L2: Principalmente completions e edições de agente no IDE ("Code first"); uso só de chat conta como Passive nas coortes do GitHub.
- L3: Muitos engenheiros usam regularmente pelo menos uma superfície de agente do GitHub ("Agent first"), confirmado por métricas de uso.
- L4: Uso multi-agent é normal ("Multi-agent"), com distribuição de coortes rastreada mensalmente.

**Exemplos de evidência:** Dashboard ou API de métricas de uso do Copilot: distribuição de coortes de adoção, usuários ativos diários/semanais.  
**Base:** [6]  
**Origem na v1:** P1-C1-Q1  
**Unidade:** engineers · **Público:** developer, platform-engineer

#### D4-Q2: Modo agente para trabalho multi-file

Os engenheiros usam IDE agent mode (ou equivalente) para mudanças multi-file, e revisam toda mudança antes de fazer commit?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Agent mode é o padrão para refactors e features multi-file na maioria das equipes; mudanças são revisadas no diff antes do commit.
- L4: Equipes compartilham padrões de agent mode que funcionam e rastreiam onde ele falha; permissões de ferramentas são ajustadas por repositório.

**Exemplos de evidência:** Uso por feature/mode, diretrizes da equipe.  
**Base:** [6] [27]  
**Origem na v1:** P1-C1-Q1 (parcial)  
**Unidade:** engineers · **Público:** developer, platform-engineer

#### D4-Q3: Delegação a coding agents

Coding agents (por exemplo Copilot cloud agent) recebem issues e produzem pull requests que são mergeados após review humano?

_Nota de escopo: Mede quanto trabalho é delegado a coding agents. A política de autonomia é D1-Q5; escopo de tarefas é D3-Q3._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria das equipes delega issues adequadas a um coding agent; a parcela de PRs mergeados que são criados por agentes é rastreada.
- L4: Taxa de merge de PRs de agentes, retrabalho e taxa de correções pós-merge são rastreadas por tipo de tarefa; regras de delegação (D1-Q5) são ajustadas a partir desses dados.

**Exemplos de evidência:** Contagens de PRs criados por agentes, taxa de merge, tempo até merge, correções de acompanhamento.  
**Base:** [6] [7] [14] [49] [50]  
**Origem na v1:** P3-C5-Q1 (parcial)  
**Unidade:** teams · **Público:** developer, platform-engineer

#### D4-Q4: Instruções de repositório

Os repositórios contêm custom instructions versionadas e revisadas para ferramentas de IA (por exemplo `.github/copilot-instructions.md`, `AGENTS.md`) descrevendo build, test, convenções e restrições?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria dos repositórios ativos tem instruções estruturadas (build, test, convenções, restrições) com um responsável; mudanças passam por PR review; arquivos são atualizados quando o codebase muda, em vez de serem commitados uma vez.
- L4: Instruções são geradas a partir de uma base compartilhada, verificadas quanto a desatualização, e seu efeito na taxa de merge de agentes e na qualidade de code é medido, já que arquivos de instrução sozinhos não garantem melhores resultados.

**Exemplos de evidência:** Arquivos de instrução, cobertura entre repositórios, histórico de mudanças, métricas antes/depois de PRs de agentes.  
**Base:** [2] [8] [25] [27] [46] [47] [55]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** repositories · **Público:** developer, platform-engineer

#### D4-Q5: Prompts, agentes e skills reutilizáveis

Existe uma biblioteca compartilhada e curada de arquivos de prompt, custom agents e skills reutilizáveis, com responsáveis e versionamento?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Um repositório central contém arquivos de prompt e custom agents aprovados; equipes os reutilizam em vez de copiar.
- L4: Ativos são avaliados antes do release (qualidade, custo), o uso é rastreado, e ativos não usados são retirados.

**Exemplos de evidência:** Repositório da biblioteca, perfis de custom agents, métricas de reutilização.  
**Base:** [11] [25] [47]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** developer, platform-engineer

#### D4-Q6: Governança de MCP servers

MCP servers e outras ferramentas de agentes são governados por uma allowlist ou registry, com ferramentas em escopo e responsáveis nomeados?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Uma allowlist enterprise de MCP ou registry customizado é aplicada; cada server tem um responsável, uma security review e ferramentas limitadas.
- L4: Tool calls são registrados e revisados; novos servers passam por security checks automatizados antes de serem adicionados.

**Exemplos de evidência:** Política de allowlist ou registry, configuração de MCP, registros de review.  
**Base:** [9] [10] [38]  
**Origem na v1:** P3-C5-Q4  
**Unidade:** organization · **Público:** developer, platform-engineer · **Prontidão de platform engineering:** sim

#### D4-Q7: Acesso de IA ao conhecimento interno

Ferramentas e agentes de IA conseguem usar com segurança fontes internas (code, documentação, wikis, itens de trabalho) como contexto, por meio de conectores aprovados?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Conectores aprovados dão às ferramentas de IA acesso ciente de permissões às principais fontes internas; respostas citam material interno.
- L4: Fontes de conhecimento são curadas para uso por IA (atualização, ownership) e a qualidade de retrieval é avaliada.

**Exemplos de evidência:** Configuração de conectores, avaliações de retrieval.  
**Base:** [1] [2] [19]  
**Origem na v1:** P1-C3-Q2, P1-C3-Q3  
**Unidade:** teams · **Público:** developer, platform-engineer · **Prontidão de platform engineering:** sim

#### D4-Q8: Seleção e roteamento de modelos

A escolha do modelo é combinada à complexidade da tarefa (modelos menores para trabalho rotineiro, frontier models para trabalho complexo), por orientação ou roteamento automático?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Orientação escrita mapeia tipos de tarefa a modelos; modelos padrão são definidos por política.
- L4: Roteamento automático está em vigor e é ajustado a partir de dados de custo e qualidade.

**Exemplos de evidência:** Orientação de modelos, configurações de política, configuração de roteamento.  
**Base:** [26] [32]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** developer, platform-engineer

### D5: Revisão, qualidade e testes

**Por que importa:** DORA vincula o volume de mudanças impulsionadas por IA à instabilidade, a menos que existam sistemas de controle fortes [3]; GitHub exige revisão humana antes que PRs de agentes sejam mergeados [7]; 46% dos desenvolvedores desconfiam da precisão da saída de IA [37].

**Página da dimensão:** [dimensoes/D5.pt-br.md](dimensoes/D5.pt-br.md)

**Estratégias:** S5, S7 · **Grupo do relatório:** G2 (Planejar, construir e revisar)

#### D5-Q1: AI-assisted code review

AI code review (por exemplo Copilot code review) é aplicado a pull requests, com um revisor humano ainda responsável pela aprovação?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: AI review executa automaticamente na maioria dos PRs; equipes rastreiam sugestões úteis versus descartadas.
- L4: Regras de review são ajustadas por repositório a partir dos resultados de sugestões; tempo de review e defeitos escapados são rastreados; PRs em que apenas IA revisou code criado por IA são visíveis e governados.

**Exemplos de evidência:** Rulesets de repositório, métricas de adoção de code review, resultados de sugestões.  
**Base:** [6] [12] [14] [54] [55]  
**Origem na v1:** P1-C1-Q2, P1-C4-Q1  
**Unidade:** repositories · **Público:** developer, qa-test

#### D5-Q2: Human-in-the-loop para mudanças de agentes

Pull requests criados por agentes exigem aprovação humana independente (não o solicitante), com workflow runs aprovadas antes de executarem?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Proteções padrão são mantidas: PRs de agentes precisam de um aprovador humano independente (aprovações do Copilot, se habilitadas, não contam); "Approve and run workflows" não é desabilitado sem uma decisão de risco documentada.
- L4: Requisitos de aprovação escalam com o risco (D1-Q5) e são auditados; exceções expiram automaticamente.

**Exemplos de evidência:** Rulesets, branch protection, configurações de agentes.  
**Base:** [7] [12] [14] [38] [53] [55] [56]  
**Origem na v1:** P3-C5-Q5, P2-C9-Q3  
**Unidade:** repositories · **Público:** developer, qa-test

#### D5-Q3: Mesmos quality gates para code de IA e humano

Mudanças geradas por IA e criadas por agentes passam pelos mesmos checks exigidos (build, tests, linting, security scans, coverage) que mudanças humanas?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Checks exigidos são aplicados por rulesets nos protected branches da maioria dos repositórios, sem bypass para identidades de agentes.
- L4: Gates são policy as code, aplicados em todos os repositórios (>90%) e revisados após incidentes.

**Exemplos de evidência:** Rulesets, checks exigidos, listas de bypass.  
**Base:** [3] [7] [31] [50] [55]  
**Origem na v1:** P1-C4-Q2, P1-C4-Q4  
**Unidade:** repositories · **Público:** developer, qa-test

#### D5-Q4: Lotes pequenos

As mudanças são mantidas pequenas (limites de tamanho de PR, uma preocupação por PR), incluindo mudanças produzidas por agentes?

_Nota de escopo: Mede o tamanho das mudanças assistidas por IA. Com que frequência o code é commitado e quão rápido é revertido é D8-Q2._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Orientação de tamanho de PR é aplicada ou monitorada; PRs de agentes grandes demais são divididos antes do review.
- L4: Tamanho de lote é rastreado em relação a change failure rate e tempo de review, e usado para ajustar limites.

**Exemplos de evidência:** Distribuição de tamanho de PR, configuração de bot ou ruleset.  
**Base:** [1] [2] [5] [53] [57]  
**Origem na v1:** P1-C4-Q6  
**Unidade:** teams · **Público:** developer, qa-test

#### D5-Q5: Testes assistidos por IA

IA é usada para gerar e manter testes, com qualidade dos testes verificada (por exemplo coverage do code alterado, mutation testing) em vez de apenas contagem de testes?

_Nota de escopo: Mede IA usada para escrever e melhorar testes. Se testes automatizados atuam como gate é D8-Q7._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria das equipes usa IA para escrever testes; coverage de linhas alteradas é um check exigido.
- L4: Efetividade dos testes (mutation score, defeitos escapados) é rastreada; flaky tests são detectados e colocados em quarentena automaticamente.

**Exemplos de evidência:** Relatórios de coverage, resultados de mutation testing, dashboard de flaky tests.  
**Base:** [3] [8] [17]  
**Origem na v1:** P1-C1-Q4, P2-C6-Q1, P2-C6-Q5, P2-C6-Q6, P2-C6-Q7  
**Unidade:** teams · **Público:** developer, qa-test

#### D5-Q6: Cultura de verificação e confiança calibrada

Os engenheiros verificam sistematicamente a saída de IA (executam, testam, leem) e a confiança na saída de IA é medida ao longo do tempo?

_Nota de escopo: Mede comportamento de review e calibração de confiança. Como developer experience é pesquisada é D9-Q4._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Diretrizes de review explicam o que verificar na saída de IA; confiança na saída de IA faz parte da pesquisa com desenvolvedores.
- L4: Confiança e precisão são comparadas com dados reais de defeitos, e a orientação é atualizada onde divergem.

**Exemplos de evidência:** Diretrizes de review, resultados de pesquisa, análise de defeitos.  
**Base:** [3] [23] [35] [37] [48] [52]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** teams · **Público:** developer, qa-test

#### D5-Q7: Saúde do code gerado por IA

A saúde de longo prazo do code gerado por IA é monitorada (duplicação, churn, complexidade, manutenibilidade)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Métricas de code health são coletadas para a maioria dos repositórios e revisadas em retrospectivas de equipe; code gerado por IA tem um responsável humano nomeado.
- L4: Tendências de saúde (por exemplo complexidade cognitiva, avisos de static analysis) são comparadas entre code com alta presença de IA e outros codes, com ações corretivas rastreadas.

**Exemplos de evidência:** Dashboards de static analysis, relatórios de churn, arquivos de ownership.  
**Base:** [2] [5] [47] [51]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** repositories · **Público:** developer, qa-test

### D6: Segurança e cadeia de suprimentos de IA

**Por que importa:** OWASP lista prompt injection (LLM01:2025), supply chain (LLM03:2025) e agência excessiva (LLM06:2025) entre os principais riscos [38], e agent goal hijack (ASI01) em primeiro lugar para aplicações agentic [39]; NIST SP 800-218A adiciona ao SSDF práticas para o desenvolvimento de modelos de IA [40].

**Página da dimensão:** [dimensoes/D6.pt-br.md](dimensoes/D6.pt-br.md)

**Estratégias:** S7, S6 · **Grupo do relatório:** G3 (Proteger, entregar e fundações)

#### D6-Q1: Scanning de base em todo repositório

Code scanning (SAST), secret scanning com push protection e dependency review são aplicados a todos os repositórios, incluindo branches de agentes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Habilitado por padrão para todos os repositórios novos e a maioria dos existentes; push protection se aplica a todo commit, humano ou de agente; alertas têm responsáveis e metas de nível de serviço.
- L4: A cobertura é quase completa e verificada automaticamente; mean time to remediate é rastreado.

**Exemplos de evidência:** Dashboard de cobertura de segurança, tempo de remediação.  
**Base:** [7] [13] [40] [52]  
**Origem na v1:** P1-C4-Q3, P2-C4-Q1, P2-C4-Q2, P2-C4-Q3, P2-C4-Q4, P2-C10-Q1  
**Unidade:** repositories · **Público:** security, platform-engineer

#### D6-Q2: Remediação assistida por IA

Remediação assistida por IA (por exemplo autofix para code scanning) é usada para corrigir vulnerabilidades, com correções revisadas e testadas antes do merge?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Sugestões de autofix são habilitadas para a maioria dos repositórios; taxas de aceitação e reabertura são rastreadas.
- L4: Campanhas de segurança usam remediação com IA em escala, e o tempo de remediação é reportado à liderança.

**Exemplos de evidência:** Configurações de autofix, métricas de remediação.  
**Base:** [13] [57]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** repositories · **Público:** security, platform-engineer

#### D6-Q3: Defesas contra prompt injection para agentes

Agentes são protegidos contra prompt injection e goal hijack (conteúdo não confiável tratado como dados, instruções ocultas filtradas, saída de rede restrita)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Agent firewalls e restrições de egress permanecem ativados; a orientação informa às equipes quais fontes de conteúdo não são confiáveis.
- L4: Agentes passam regularmente por red team contra cenários OWASP LLM01:2025 e ASI01; achados são rastreados até o fechamento.

**Exemplos de evidência:** Configuração de firewall, relatórios de red team.  
**Base:** [7] [38] [39]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** security, platform-engineer

#### D6-Q4: Least privilege para agentes

Agentes executam com least privilege (tokens com escopo, sem segredos de produção, branches restritos, ambientes em sandbox)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Permissões de agentes são documentadas e revisadas; agentes não conseguem acessar credenciais de produção nem fazer push para protected branches.
- L4: Permissões são just-in-time e limitadas no tempo; o acesso é revisado automaticamente.

**Exemplos de evidência:** Configuração de ambiente de agentes, escopos de token, revisões de acesso.  
**Base:** [7] [19] [38] [39]  
**Origem na v1:** P3-C6-Q2, P3-C6-Q3 (parcial)  
**Unidade:** organization · **Público:** security, platform-engineer

#### D6-Q5: AI supply chain

Modelos, MCP servers, extensões de IDE e ferramentas de agentes são avaliados antes do uso, com proveniência e SBOMs para o que você constrói e entrega?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Um processo de review cobre componentes de IA; SBOMs e proveniência de build são produzidos para a maioria dos builds.
- L4: Proveniência é verificada no deploy (por exemplo metas de nível SLSA); componentes não avaliados são bloqueados automaticamente.

**Exemplos de evidência:** Registros de review de componentes, amostras de SBOM e atestação.  
**Base:** [38] [40] [43] [52]  
**Origem na v1:** P2-C8-Q2, P2-C8-Q3, P2-C10-Q2, P2-C10-Q3, P2-C10-Q5  
**Unidade:** repositories · **Público:** security, platform-engineer

#### D6-Q6: Threat modeling para features e agentes de IA

Features de IA e workflows agentic são threat-modeled com riscos específicos de IA (OWASP LLM and Agentic Top 10, NIST SP 800-218A)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Threat models são exigidos para novas features de IA e workflows de agentes, e revisados por segurança.
- L4: Threat models são atualizados após incidentes e exercícios de red team; controles são verificados por testes automatizados.

**Exemplos de evidência:** Documentos de threat model, registros de security review.  
**Base:** [38] [39] [40]  
**Origem na v1:** P2-C4-Q6 (parcial), P3-C3-Q5, P3-C5-Q3  
**Unidade:** services · **Público:** security, platform-engineer

#### D6-Q7: Trilha de auditoria para ações de agentes

Sessões e ações de agentes (prompts, tool calls, commits, aprovações) são registradas, atribuíveis a uma identidade e retidas de acordo com a política?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Atividade de agentes é registrada centralmente e vinculada ao usuário solicitante e à identidade do agente.
- L4: Logs alimentam detecção de anomalias; auditorias conseguem reconstruir qualquer mudança de agente de ponta a ponta.

**Exemplos de evidência:** Configuração de audit log, exemplo de investigação.  
**Base:** [7] [19]  
**Origem na v1:** P3-C6-Q5 (parcial)  
**Unidade:** organization · **Público:** security, platform-engineer

### D7: Entregar e operar

**Por que importa:** mais mudanças geradas por IA precisam de redes de segurança fortes na entrega [3], [5]; a Microsoft recomenda observação contínua da atividade de agentes [19] e está estendendo agentes para operações de cloud [22].

**Página da dimensão:** [dimensoes/D7.pt-br.md](dimensoes/D7.pt-br.md)

**Estratégias:** S2, S6 · **Grupo do relatório:** G3 (Proteger, entregar e fundações)

#### D7-Q1: IA em pipelines CI/CD

IA é usada para criar, manter e solucionar problemas em pipelines CI/CD (por exemplo explicar runs com falha, propor correções), sobre pipeline-as-code?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Pipelines são code na maioria dos repositórios; análise de falhas assistida por IA está disponível para todas as equipes.
- L4: Agentes propõem correções e otimizações de pipeline automaticamente, sob review, com tempo de build e taxa de falhas rastreados.

**Exemplos de evidência:** Repositórios de pipeline, uso de análise de falhas, métricas de build.  
**Base:** [16] [17]  
**Origem na v1:** P2-C1-Q1, P2-C1-Q2, P2-C1-Q3  
**Unidade:** repositories · **Público:** devops, platform-engineer · **Prontidão de platform engineering:** sim

#### D7-Q2: Entrega progressiva e rollback

As equipes conseguem lançar mudanças assistidas por IA com segurança por meio de entrega progressiva (feature flags, canary ou blue/green) e rollback automatizado?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria dos serviços usa feature flags ou rollout em estágios; rollback é automatizado para serviços críticos.
- L4: Decisões de rollout são conduzidas automaticamente por sinais de saúde; change failure rate e tempo de recuperação são rastreados por serviço.

**Exemplos de evidência:** Plataforma de feature flags, configuração de rollout, registros de rollback.  
**Base:** [3] [5]  
**Origem na v1:** P2-C1-Q6, P2-C5-Q1, P2-C5-Q2, P2-C5-Q3, P2-C5-Q5  
**Unidade:** services · **Público:** devops, platform-engineer

#### D7-Q3: Resposta a incidentes assistida por IA

IA é usada em resposta a incidentes (correlação de alertas, sumarização, hipóteses de causa raiz, rascunhos de revisão pós-incidente) com humanos no comando?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Engenheiros de on-call na maioria das equipes usam IA para triage e resumos; revisões pós-incidente registram se a IA ajudou.
- L4: Agentes de operações executam diagnósticos aprovados automaticamente; tempo de restauração é comparado antes e depois da adoção.

**Exemplos de evidência:** Configuração de ferramentas de incidentes, timelines de incidentes, dados de tempo de restauração.  
**Base:** [16] [17] [22]  
**Origem na v1:** P2-C3-Q6, P2-C7-Q2, P2-C7-Q5  
**Unidade:** services · **Público:** devops, platform-engineer

#### D7-Q4: Observabilidade de agentes

Agentes de IA no SDLC são observáveis (traces de runs e tool calls, latência, falhas, custo), por exemplo por meio de OpenTelemetry?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Runs de agentes emitem telemetria para a stack central de observabilidade; dashboards mostram falhas e custo por agente.
- L4: Alertas disparam em drift de agentes, picos de erro ou anomalias de custo; achados alimentam governança (D1).

**Exemplos de evidência:** Dashboards de telemetria, regras de alerta.  
**Base:** [19] [32] [45]  
**Origem na v1:** P2-C3-Q3, P3-C5-Q6  
**Unidade:** organization · **Público:** devops, platform-engineer

#### D7-Q5: Infrastructure as code com guardrails

IA é usada para escrever e revisar infrastructure as code, com guardrails de policy-as-code que bloqueiam mudanças não conformes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maior parte da infraestrutura é code; IaC gerado por IA passa pelos mesmos policy checks e plan reviews.
- L4: Drift é detectado e corrigido por meio de GitOps; violações de política por IaC gerado por IA são rastreadas e estão em queda.

**Exemplos de evidência:** Repositórios de IaC, regras de policy-as-code, relatórios de drift.  
**Base:** [3] [19]  
**Origem na v1:** P2-C2-Q1, P2-C2-Q2, P2-C2-Q4, P2-C2-Q5, P2-C9-Q1  
**Unidade:** services · **Público:** devops, platform-engineer · **Prontidão de platform engineering:** sim

#### D7-Q6: Automação operacional orientada por agentes

Tarefas operacionais (runbooks, remediação, atualizações de dependências e patches) são automatizadas por agentes sob regras de aprovação definidas?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Runbooks comuns e atualizações de dependências são automatizados; aprovações seguem a matriz de autonomia (D1-Q5).
- L4: A maioria das operações rotineiras executa automaticamente com aprovações auditadas; o esforço humano se desloca para exceções.

**Exemplos de evidência:** Catálogo de automação, logs de aprovação.  
**Base:** [19] [22]  
**Origem na v1:** P2-C7-Q7, P2-C10-Q4  
**Unidade:** services · **Público:** devops, platform-engineer · **Prontidão de platform engineering:** sim

### D8: Fundamentos de engenharia (amplificadores de IA)

**Por que importa:** DORA constata que essas capacidades amplificam os benefícios da adoção de IA, e que uma plataforma interna de alta qualidade se correlaciona com a capacidade de desbloquear valor de IA [1], [3].

**Página da dimensão:** [dimensoes/D8.pt-br.md](dimensoes/D8.pt-br.md)

**Estratégias:** S1, S2, S3 · **Grupo do relatório:** G3 (Proteger, entregar e fundações)

#### D8-Q1: Controle de versão para tudo

Application code, configuração, automação de build, configuração de sistema e prompts/instruções de IA estão todos armazenados em controle de versão?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Todos os cinco tipos de ativos são versionados para a maioria dos serviços.
- L4: Nada chega à produção sem uma fonte versionada; checks confirmam isso automaticamente.

**Exemplos de evidência:** Inventário de repositórios, fontes de configuração.  
**Base:** [1] [2]  
**Origem na v1:** P1-C7-Q1 (parcial)  
**Unidade:** teams · **Público:** platform-engineer, devops, developer

#### D8-Q2: Frequência de commit e rollback rápido

Os engenheiros fazem commit de mudanças pequenas com frequência e contam com undo/revert rápido ao experimentar com saída de IA?

_Nota de escopo: Mede frequência de commit e velocidade de rollback. O tamanho das mudanças assistidas por IA é D5-Q4._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria dos engenheiros faz commit pelo menos diariamente; reverter uma mudança é rotina e rápido.
- L4: Trunk-based development com branches de curta duração é a norma; tempo de revert é medido.

**Exemplos de evidência:** Dados de frequência de commit, idade de branch.  
**Base:** [2]  
**Origem na v1:** P2-C1-Q4  
**Unidade:** teams · **Público:** platform-engineer, devops, developer

#### D8-Q3: Plataforma interna de qualidade

Existe uma internal developer platform fácil de usar, que abstrai infraestrutura e torna o caminho seguro e conforme o padrão para humanos e agentes?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Uma equipe dedicada de plataforma oferece golden paths de self-service usados pela maioria das equipes; a equipe age com base em feedback.
- L4: Agentes usam as mesmas APIs e guardrails da plataforma que humanos; satisfação com a plataforma é medida e melhora.

**Exemplos de evidência:** Catálogo da plataforma, golden paths, pesquisa de satisfação.  
**Base:** [1] [2] [3] [31]  
**Origem na v1:** P1-C2-Q1, P1-C2-Q3, P1-C2-Q4, P1-C2-Q5, P1-C2-Q6  
**Unidade:** organization · **Público:** platform-engineer, devops, developer · **Prontidão de platform engineering:** sim

#### D8-Q4: Ecossistema de dados saudável

Engenheiros e ferramentas de IA conseguem encontrar e usar dados internos confiáveis (não em silos, de boa qualidade, respondíveis rapidamente)?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Dados-chave são catalogados com responsáveis e indicadores de qualidade; a maioria das perguntas pode ser respondida em até uma hora.
- L4: Qualidade de dados é monitorada automaticamente; linhagem e contratos existem para dados críticos.

**Exemplos de evidência:** Catálogo de dados, dashboards de qualidade.  
**Base:** [1] [2]  
**Origem na v1:** P3-C4-Q1, P3-C4-Q2, P3-C4-Q3  
**Unidade:** organization · **Público:** platform-engineer, devops, developer

#### D8-Q5: Ambientes reproduzíveis para humanos e agentes

Ambientes de desenvolvimento são reproduzíveis (devcontainers, cloud workspaces, toolchains fixadas) para que humanos e agentes façam build e test da mesma forma?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria dos repositórios define um ambiente reproduzível; agentes usam a mesma definição.
- L4: Ambientes iniciam em minutos para qualquer repositório; drift em relação à definição é detectado.

**Exemplos de evidência:** Arquivos devcontainer, tempos de start-up de ambiente.  
**Base:** [8]  
**Origem na v1:** P1-C2-Q2, P1-C5-Q1, P1-C9-Q1, P1-C9-Q2, P1-C9-Q3  
**Unidade:** repositories · **Público:** platform-engineer, devops, developer · **Prontidão de platform engineering:** sim

#### D8-Q6: Documentação como contexto pronto para IA

A documentação é mantida como code, atual e com ownership, para que sirva como contexto confiável para ferramentas de IA?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Docs ficam junto ao code com responsáveis; docs desatualizadas são sinalizadas em reviews.
- L4: Atualização é verificada automaticamente; mudanças de docs geradas por IA são revisadas como code.

**Exemplos de evidência:** Repositórios de docs, checks de atualização.  
**Base:** [2] [25]  
**Origem na v1:** P1-C3-Q1, P1-C3-Q4, P1-C7-Q1, P1-C7-Q2, P1-C7-Q3, P1-C7-Q4  
**Unidade:** repositories · **Público:** platform-engineer, devops, developer

#### D8-Q7: Testes automatizados como sistema de controle

Testes automatizados são profundos e rápidos o suficiente para capturar regressões de altos volumes de mudanças geradas por IA (unit, integration, end-to-end, contract)?

_Nota de escopo: Mede testes automatizados como sistema de controle. IA usada para escrever testes é D5-Q5._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: A maioria dos serviços tem testes automatizados em camadas que executam em todo PR dentro de time budgets acordados.
- L4: Suites de teste são ajustadas a partir de dados de defeitos escapados; tempo de feedback é rastreado e melhora.

**Exemplos de evidência:** Inventário de suites de teste, durações de pipeline, dados de defeitos escapados.  
**Base:** [3]  
**Origem na v1:** P2-C6-Q2, P2-C6-Q3, P2-C6-Q4, P1-C8-Q3  
**Unidade:** services · **Público:** platform-engineer, devops, developer

### D9: Medição, valor e AI FinOps

**Por que importa:** estudos controlados variam de 55.8% mais rápido [33] e 26.08% mais tarefas concluídas [34] a 19% mais lento com uma forte lacuna de percepção [35], portanto as organizações precisam de sua própria medição objetiva; o Gartner prevê que os custos de AI coding ultrapassarão o salário médio de um desenvolvedor até 2028 [32].

**Página da dimensão:** [dimensoes/D9.pt-br.md](dimensoes/D9.pt-br.md)

**Estratégias:** S5, S2 · **Grupo do relatório:** G1 (Direção, pessoas e valor)

#### D9-Q1: Métricas de profundidade de adoção

A adoção de IA é rastreada com telemetria além da contagem de seats (usuários ativos, engajamento por feature, coortes de adoção)?

_Nota de escopo: Mede se a adoção é rastreada. Quão profundamente IA é usada é D4-Q1._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Métricas de uso (por exemplo a API ou dashboard de métricas de uso do Copilot) são revisadas mensalmente pela liderança de engenharia.
- L4: Movimento de coortes é uma meta gerenciada; ações de capacitação são avaliadas por seu efeito nas coortes.

**Exemplos de evidência:** Dashboards de uso, relatórios de tendência de coortes.  
**Base:** [6]  
**Origem na v1:** P1-C1-Q3  
**Unidade:** organization · **Público:** engineering-leader, product-owner

#### D9-Q2: Métricas de resultado de entrega

Métricas de entrega de software (lead time, deployment frequency, change failure rate, time to restore) são rastreadas e comparadas antes e depois da adoção de IA?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Métricas DORA são coletadas automaticamente para a maioria dos serviços e revisadas com dados de adoção de IA.
- L4: Métricas de entrega fazem parte das decisões de investimento em IA; regressões disparam ação corretiva.

**Exemplos de evidência:** Dashboards DORA, comparação baseline versus atual.  
**Base:** [2] [3] [5]  
**Origem na v1:** P1-C8-Q1, P2-C1-Q5, P2-C5-Q6, P2-C3-Q1  
**Unidade:** services · **Público:** engineering-leader, product-owner

#### D9-Q3: Métricas de fluxo de pull request

Throughput de PR, tempo até merge e a parcela e taxa de merge de PRs criados por IA ou agentes são rastreados?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Métricas de ciclo de vida de PR são reportadas por organização; PRs criados por agentes são identificados separadamente, incluindo sua taxa de correções pós-merge.
- L4: Métricas de fluxo são vinculadas a métricas de qualidade (D5) para que fluxo mais rápido não seja comprado com instabilidade.

**Exemplos de evidência:** Métricas de ciclo de vida de PR, relatórios de PRs de agentes, análise de correções de acompanhamento.  
**Base:** [6] [34] [50]  
**Origem na v1:** P1-C4-Q5, P1-C8-Q5  
**Unidade:** organization · **Público:** engineering-leader, product-owner

#### D9-Q4: Developer experience e fricção

Developer experience é medida regularmente (produtividade percebida, fricção, confiança em IA, satisfação), usando um framework reconhecido como SPACE ou as perguntas de resultado do DORA?

_Nota de escopo: Mede a pesquisa de developer experience. Comportamento de review e calibração de confiança é D5-Q6._

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Uma pesquisa ocorre pelo menos duas vezes por ano com boa participação; resultados são compartilhados e geram ações.
- L4: Resultados de pesquisa são combinados com telemetria (D9-Q1 a Q3) para encontrar e remover fricção.

**Exemplos de evidência:** Instrumento de pesquisa, taxa de participação, log de ações.  
**Base:** [2] [44]  
**Origem na v1:** P1-C8-Q2, P1-C8-Q4  
**Unidade:** organization · **Público:** engineering-leader, product-owner

#### D9-Q5: Medição controlada de impacto

O impacto de IA é estimado com comparações controladas ou baseadas em coortes (por exemplo piloto versus controle, coortes de adoção, antes/depois com um baseline) em vez de apenas estimativas autorreportadas?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Pelo menos uma comparação controlada ou de coorte foi executada e documentada, com suas limitações.
- L4: Comparações são executadas continuamente para ferramentas e práticas principais; decisões as citam.

**Exemplos de evidência:** Desenho do estudo, resultados, registros de decisão.  
**Base:** [6] [34] [35]  
**Origem na v1:** Nenhuma (nova na v2)  
**Unidade:** organization · **Público:** engineering-leader, product-owner

#### D9-Q6: Governança de custos de IA (AI FinOps)

Custos de IA (seats, premium requests, tokens, runs de agentes) são orçados, monitorados por equipe e caso de uso, com thresholds e revisões regulares?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Orçamentos e thresholds de alerta existem por organização ou equipe; workflows de alto consumo são revisados em retrospectivas.
- L4: Custo por resultado (por exemplo por PR mergeado) é rastreado; práticas de roteamento e contexto são ajustadas para reduzir desperdício.

**Exemplos de evidência:** Dashboards de custo, alertas de orçamento, notas de retrospectiva.  
**Base:** [19] [32] [38] [45]  
**Origem na v1:** P3-C9-Q1 (parcial)  
**Unidade:** organization · **Público:** engineering-leader, product-owner

#### D9-Q7: Vínculo com valor de negócio

Resultados de engenharia com IA são conectados a valor de negócio (business case, premissas de ROI, OKRs) e revisados com stakeholders de finanças ou negócio?

- L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade
- L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)
- L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)
- L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)
- L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados
- L3: Existe um business case com premissas explícitas e ele é revisado pelo menos anualmente.
- L4: Valor é reportado em uma cadência fixa com insumos medidos de D9-Q1 a Q6; investimento é ajustado a partir dos resultados.

**Exemplos de evidência:** Business case, relatórios de valor.  
**Base:** [18] [28] [32]  
**Origem na v1:** P1-C8-Q6, P3-C9-Q5  
**Unidade:** organization · **Público:** engineering-leader, product-owner

## Referências

1. DORA. _DORA AI Capabilities Model_. Google Cloud, 2025. <https://dora.dev/ai/capabilities-model/report/>
2. DORA. _DORA AI Capabilities Model: Survey Questions_. Google Cloud, 2025. <https://dora.dev/ai/capabilities-model/questions/>
3. Google Cloud. _Announcing the 2025 DORA Report: State of AI-Assisted Software Development_. 2025. <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>
4. DORA. _State of AI-assisted Software Development 2025_. <https://dora.dev/research/2025/dora-report/>
5. Google Cloud. _Announcing the 2024 DORA report_. 2024-10-22. <https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report>
6. GitHub Docs. _GitHub Copilot usage metrics_. <https://docs.github.com/en/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics>
7. GitHub Docs. _Risks and mitigations for GitHub Copilot cloud agent_. <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations>
8. GitHub Docs. _Best practices for using GitHub Copilot to work on tasks_. <https://docs.github.com/enterprise-cloud@latest/copilot/tutorials/cloud-agent/get-the-best-results>
9. GitHub Docs. _Configuring an MCP server allowlist for your enterprise_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist>
10. GitHub Docs. _Restrict MCP server access to a custom registry_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/restrict-based-on-registry>
11. GitHub Docs. _Custom agents configuration_. <https://docs.github.com/en/copilot/reference/custom-agents-configuration>
12. GitHub Docs. _About GitHub Copilot code review_. <https://docs.github.com/copilot/concepts/agents/code-review>
13. GitHub Docs. _About autofix for code scanning_. <https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning>
14. GitHub Docs. _Application card: GitHub Copilot Agents_. <https://docs.github.com/en/copilot/responsible-use/agents>
15. GitHub Docs. _Managing policies and features for GitHub Copilot in your organization_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies>
16. Microsoft Azure Blog. _Agentic DevOps: Evolving software development with GitHub Copilot and Microsoft Azure_. 2025. <https://azure.microsoft.com/en-us/blog/agentic-devops-evolving-software-development-with-github-copilot-and-microsoft-azure/>
17. Microsoft for Developers. _Agentic DevOps in action: Reimagining every phase of the developer lifecycle_. 2025. <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle/>
18. Microsoft Learn. _AI strategy: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy>
19. Microsoft Learn. _Govern and secure AI agents: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization>
20. Microsoft Learn. _Responsible AI policies: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/responsible-ai-policies>
21. Microsoft. _Responsible AI Principles and Approach_. <https://www.microsoft.com/en-us/ai/principles-and-approach>
22. Microsoft Azure Blog. _Announcing Azure Copilot agents and AI infrastructure innovations_. 2025. <https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/>
23. Anthropic. _Anthropic Economic Index: AI's impact on software development_. 2025-04-28. <https://www.anthropic.com/research/impact-software-development>
24. Anthropic. _How Claude Code is used in practice_. 2026-06-16. <https://www.anthropic.com/research/claude-code-expertise>
25. Anthropic. _Effective context engineering for AI agents_. 2025-09-29. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
26. Anthropic. _Building effective agents_. 2024-12-19. <https://www.anthropic.com/engineering/building-effective-agents>
27. Anthropic. _Best practices for Claude Code_. Claude Code Docs. <https://code.claude.com/docs/en/best-practices>
28. Gartner. _Gartner Says 75% of Enterprise Software Engineers Will Use AI Code Assistants by 2028_. 2024-04-11. <https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028>
29. Gartner. _Gartner Identifies the Top Strategic Trends in Software Engineering for 2025 and Beyond_. 2025-07-01. <https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond>
30. Gartner. _Gartner Says Generative AI will Require 80% of Engineering Workforce to Upskill Through 2027_. 2024-10-03. <https://www.gartner.com/en/newsroom/press-releases/2024-10-03-gartner-says-generative-ai-will-require-80-percent-of-engineering-workforce-to-upskill-through-2027>
31. Gartner. _Gartner Says the Market for Enterprise AI Coding Agents Is Entering a New Phase of Expansion and Competitive Realignment_. 2026-05-20. <https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-says-the-market-for-enterprise-ai-coding-agents-is-entering-a-new-phase-of-expansion-and-competitive-realignment>
32. Gartner. _Gartner Predicts AI Coding Costs Will Surpass Average Developer's Salary by 2028 as Token Consumption Surges_. 2026-06-24. <https://www.gartner.com/en/newsroom/press-releases/2026-06-24-gartner-predicts-ai-coding-costs-will-surpass-average-developer-salary-by-2028-as-token-consumption-surges>
33. Peng, S., Kalliamvakou, E., Cihon, P., Demirer, M. _The Impact of AI on Developer Productivity: Evidence from GitHub Copilot_. arXiv:2302.06590, 2023. <https://arxiv.org/abs/2302.06590>
34. Cui, Z. K., Demirer, M., Jaffe, S., Musolff, L., Peng, S., Salz, T. _The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers_. Management Science, published online 2026-02-27. <https://doi.org/10.1287/mnsc.2025.00535> (pre-print: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566>)
35. METR. _Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity_. 2025-07-10. <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/> (paper: <https://arxiv.org/abs/2507.09089>)
36. METR. _We are Changing our Developer Productivity Experiment Design_. 2026-02-24. <https://metr.org/blog/2026-02-24-uplift-update/>
37. Stack Overflow. _2025 Developer Survey: AI_. <https://survey.stackoverflow.co/2025/ai>
38. OWASP GenAI Security Project. _OWASP Top 10 for LLM Applications 2025_. <https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/>
39. OWASP GenAI Security Project. _OWASP Top 10 for Agentic Applications for 2026_. 2025-12-09. <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
40. NIST. _SP 800-218A: Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile_. 2024-07. <https://csrc.nist.gov/pubs/sp/800/218/a/final>
41. NIST. _AI Risk Management Framework_. <https://www.nist.gov/itl/ai-risk-management-framework>
42. ISO. _ISO/IEC 42001:2023: AI management systems_. <https://www.iso.org/standard/42001>
43. OpenSSF. _SLSA: Supply-chain Levels for Software Artifacts_. <https://slsa.dev/>
44. Forsgren, N., Storey, M.-A., Maddila, C., Zimmermann, T., Houck, B., Butler, J. _The SPACE of Developer Productivity_. ACM Queue 19(1), 2021-03-06. <https://queue.acm.org/detail.cfm?id=3454124> (DOI: <https://doi.org/10.1145/3454122.3454124>)
45. Liu, B., Qiu, H., Goiri, Í., Fonseca, R., Bianchini, R., Choukse, E. _Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale_. arXiv:2608.00101, 2026-07-30. <https://arxiv.org/abs/2608.00101>
46. Arabat, A., Sayagh, M. _Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests_. arXiv:2606.13449, 2026-06-11. <https://arxiv.org/abs/2606.13449>
47. Denisov-Blanch, Y., Agarwal, S., Azaletskiy, P., He, H., Schaeffer, R., Miranda, B., Vasilescu, B., Koyejo, S. _A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption_. arXiv:2608.25241, 2026-08-26. <https://arxiv.org/abs/2608.25241>
48. Shen, J. H., Tamkin, A. _How AI Impacts Skill Formation_. arXiv:2601.20245, 2026-01-28. <https://arxiv.org/abs/2601.20245> (Anthropic summary: <https://www.anthropic.com/research/AI-assistance-coding-skills>)
49. Pinna, G., Gong, J., Williams, D., Sarro, F. _Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance_. arXiv:2602.08915, 2026-02-09. <https://arxiv.org/abs/2602.08915>
50. Takerngsaksiri, W., Duong, N., Barnett, S. _Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests_. arXiv:2609.26847, 2026-09-22. <https://arxiv.org/abs/2609.26847>
51. Sawada, S., Shirai, T., Kashiwa, Y., Yamaguchi, K., Iwata, H., Iida, H. _To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study_. arXiv:2605.06464, 2026-05-07. <https://arxiv.org/abs/2605.06464>
52. Sakib, A. H. M. N., Banik, D., Jadliwala, M. _Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents_. arXiv:2607.12428, 2026-07-14. <https://arxiv.org/abs/2607.12428>
53. Nachuma, C., Zibran, M. _When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests_. arXiv:2602.19441, 2026-02-23. <https://arxiv.org/abs/2602.19441>
54. Selvanayagam, N., Ghaleb, T. A. _AI-to-AI Code Reviews of GitHub Pull Requests_. arXiv:2608.21311, 2026-08-21. <https://arxiv.org/abs/2608.21311>
55. Stolze, M., Strässle, M. _When Review Alone No Longer Scales: Layered Supervision in AI-Assisted Software Engineering_. arXiv:2608.26316, 2026-08-26. <https://arxiv.org/abs/2608.26316>
56. Monperrus, M. _The End of Code Review: Coding Agents Supersede Human Inspection_. arXiv:2606.13175, 2026-06-11. <https://arxiv.org/abs/2606.13175>
57. Siddiq, M. L., Zhao, X., Lopes, V. C., Casey, B., Santos, J. C. S. _Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub_. arXiv:2601.00477, 2026-01-01. <https://arxiv.org/abs/2601.00477>
58. Farrag, S. E. _The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development_. arXiv:2605.01160, 2026-05-01. <https://arxiv.org/abs/2605.01160>
