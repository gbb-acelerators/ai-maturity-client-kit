# Banco de perguntas para Microsoft Forms: AI-Assisted SDLC Maturity Assessment v2

> Gerado a partir de `framework.v2.json` (versão 2.0.1) por `scripts/generate_v2_collection.py`. Não edite à mão. Fonte do texto: [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md). O banco v1 (158 perguntas) está arquivado em [v1/](v1/).

## Como montar o formulário

1. Acesse <https://forms.office.com> e crie um formulário em branco. Título sugerido: `AI-Assisted SDLC Maturity Assessment v2 - <Organização>`.
2. Cole o aviso de privacidade de [INSTRUCOES-FORMS.pt-br.md](INSTRUCOES-FORMS.pt-br.md) na descrição do formulário.
3. Adicione **10 seções**: Seção 0 (perfil) e uma por dimensão, D1 a D9.
4. Seção 0: adicione as 5 perguntas de perfil como **Choice**. `R-Q3` permite várias respostas. Elas não pontuam.
5. Para cada pergunta pontuada, adicione 2 elementos: um **Choice** (resposta única) cujo título começa com o ID e dois-pontos (por exemplo `D4-Q3: ...`), com as 6 opções abaixo na ordem; e um **Long Text** opcional com o título `Evidence (<ID>)`.
6. Cole as linhas **L3 se parece com** e **L4 se parece com** no subtítulo da pergunta.
7. Compartilhe o link. Busque ao menos 3 respondentes por papel (`R-Q1`).
8. `Responses` > `Open in Excel`, baixe o arquivo e rode `make import XLSX=<arquivo>`.

Total de elementos: 5 de perfil + 61 pontuados + 61 campos opcionais de evidência = 127 elementos.

## As 6 opções de toda pergunta pontuada

- **L0 - Não iniciado: Nenhuma prática ainda, ou IA não permitida para esta atividade**
- **L1 - Explorando: Uso individual ou ad hoc, sem orientação acordada (mais de 0% e até 25% das equipes)**
- **L2 - Adotando: Prática no nível da equipe com orientação escrita (26-50% das equipes)**
- **L3 - Escalando: Padrão organizacional, governado e medido (51-90% das equipes)**
- **L4 - Nativo em IA: Universal (>90%), continuamente avaliado e melhorado, vinculado a resultados**
- **NA - Não sei / Não se aplica**

> Mantenha o prefixo `L0` a `L4` e `NA` no início de cada opção e o ID no início de cada título: o importador depende dos dois. Mantenha também o rótulo `Evidence (<ID>)` em inglês.

## Como responder

- Leia cada pergunta como "em que medida isto é verdade?".
- Responda no nível mais alto em que **todas** as partes da pergunta são verdadeiras.
- Se cobertura, governança e medição apontarem níveis diferentes, escolha o menor.
- Escolha `L0` quando a prática poderia existir mas ainda não existe; escolha `NA` só quando você não sabe ou a atividade não existe no seu escopo.

---

## Seção 0: Perfil do respondente (não pontua)

### R-Q1: Função principal

**R-Q1: Qual opção descreve melhor sua função principal?**

_Choice, resposta única_

- Software engineer / developer
- Engineering manager / tech lead
- Arquiteto
- Platform / DevOps / SRE engineer
- Security / AppSec
- QA / test engineer
- Product / program manager
- Executive (CTO, VP, Director)
- Outro

### R-Q2: Escopo das suas respostas

**R-Q2: Em qual escopo suas respostas se baseiam?**

_Choice, resposta única_

- Uma única equipe
- Várias equipes em uma unidade de negócio
- Uma unidade de negócio
- Toda a organização

### R-Q3: Principais ferramentas de AI coding

**R-Q3: Quais ferramentas de IA você usa pelo menos semanalmente para trabalho de software? (múltiplas respostas)**

_Choice, várias respostas_

- GitHub Copilot no IDE (completions, chat, agent mode)
- GitHub Copilot cloud agent / code review / CLI
- Claude Code ou Claude em outros clientes
- Ferramentas internas baseadas em Microsoft Foundry / Azure OpenAI
- Outras ferramentas comerciais de AI coding
- Modelos internos ou self-hosted
- Nenhuma

### R-Q4: Experiência profissional

**R-Q4: Quantos anos de experiência profissional em software você tem?**

_Choice, resposta única_

- Menos de 2
- 2-5
- 6-10
- Mais de 10

### R-Q5: Tempo hands-on

**R-Q5: Em uma semana típica, quanto do seu tempo é hands-on construindo (code, configuração, testes)?**

_Choice, resposta única_

- Menos de 20%
- 20-50%
- 51-80%
- Mais de 80%

---

## Seção D1: Estratégia, política e governança de IA

_7 perguntas. Por que importa: DORA identifica uma "postura de IA clara e comunicada" como amplificadora dos benefícios da IA [1]; o Microsoft CAF exige que "todo agente deve ser observável, governado e seguro" [19]._

### D1-Q1: Estratégia de IA para engenharia de software

**D1-Q1: Existe uma estratégia documentada de IA para engenharia de software, patrocinada pela liderança, que declare objetivos explícitos e seja comunicada a todas as equipes de engenharia?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Estratégia publicada e revisada pelo menos anualmente; objetivos (por exemplo entrega, qualidade, developer experience) têm responsáveis; a maioria dos engenheiros consegue dizer onde encontrá-la.
- **L4 se parece com:** A estratégia é revisada a partir de resultados medidos (D9) e vinculada a OKRs de negócio; o progresso é reportado à liderança em uma cadência fixa.
- **Exemplos de evidência:** Documento de estratégia, comunicação da liderança, entradas de OKR.
- **Campo de evidência:** `Evidence (D1-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q2: Política de uso aceitável

**D1-Q2: Está claro para os engenheiros como eles podem e não podem usar IA no trabalho, incluindo quais dados podem ser compartilhados com ferramentas de IA?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Política escrita de uso aceitável cobre code, dados de clientes, segredos e IP de terceiros; faz parte do onboarding; exceções têm um responsável.
- **L4 se parece com:** A política é aplicada por controles técnicos (por exemplo content exclusion, prevenção contra perda de dados, allowlists) e auditada; violações disparam alertas automatizados.
- **Exemplos de evidência:** Link da política, checklist de onboarding, configuração de controles.
- **Campo de evidência:** `Evidence (D1-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q3: Ferramentas e modelos aprovados

**D1-Q3: Existe um catálogo mantido de ferramentas, recursos e modelos de IA aprovados para desenvolvimento de software, gerenciado por políticas enterprise ou da organização?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Políticas enterprise/da organização habilitam apenas recursos e modelos aprovados; o catálogo lista responsável, tratamento de dados e data de revisão para cada ferramenta.
- **L4 se parece com:** Novos modelos e ferramentas passam por uma avaliação definida (qualidade, custo, segurança) antes da habilitação; os descontinuados são removidos conforme cronograma.
- **Exemplos de evidência:** Configurações de política do Copilot, catálogo de ferramentas, registros de avaliação de modelos.
- **Campo de evidência:** `Evidence (D1-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q4: Proteção de dados, IP e residência

**D1-Q4: Requisitos de residência, retenção, propriedade intelectual e privacidade de dados estão definidos e aplicados às ferramentas e agentes de IA usados no SDLC?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Requisitos são documentados por ferramenta; repositórios ou arquivos sensíveis são excluídos do contexto de IA; retenção de logs e memória segue a política.
- **L4 se parece com:** A conformidade é avaliada continuamente (por exemplo com um compliance manager) e mapeada a regulamentações como o EU AI Act quando aplicável.
- **Exemplos de evidência:** Registros de processamento de dados, configurações de exclusão, política de retenção.
- **Campo de evidência:** `Evidence (D1-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q5: Níveis de autonomia para trabalho com IA

**D1-Q5: A organização definiu quais tarefas são lideradas pelo desenvolvedor, conduzidas por desenvolvedor com agente, ou totalmente lideradas por agente, e os controles exigidos para cada nível?**

- **Nota de escopo:** Mede a política que define níveis de autonomia. Como as tarefas são escritas para agentes é D3-Q3; com que frequência o trabalho é delegado é D4-Q3.
- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Uma matriz publicada mapeia tipos de tarefa (por exemplo upgrades de dependências, geração de testes, trabalho de feature, mudanças em produção) para níveis de autonomia e aprovações exigidas.
- **L4 se parece com:** A matriz é aplicada por regras da plataforma (por exemplo branch protection, revisores exigidos por caminho) e atualizada a partir de dados de incidentes e qualidade.
- **Exemplos de evidência:** Matriz de autonomia, rulesets de repositório, registros de mudança.
- **Campo de evidência:** `Evidence (D1-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q6: IA responsável e framework de risco

**D1-Q6: O uso de IA em engenharia de software é governado por um padrão de IA responsável e por um framework de risco reconhecido (por exemplo Microsoft Responsible AI Standard, NIST AI RMF, ISO/IEC 42001)?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Um framework nomeado é adotado; riscos relacionados a IA estão no registro de riscos com responsáveis e revisões.
- **L4 se parece com:** Controles do framework são auditados interna ou externamente; resultados retroalimentam política e tooling.
- **Exemplos de evidência:** Mapeamento do framework, entradas no registro de riscos, relatórios de auditoria.
- **Campo de evidência:** `Evidence (D1-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D1-Q7: Registro e identidade de agentes

**D1-Q7: Todo agente de IA usado no SDLC (coding agents, review agents, custom agents, pipeline agents) está registrado com um responsável, um propósito, uma identidade distinta e um escopo de acesso definido?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Um único inventário lista todos os agentes com responsável, plataforma e permissões; cada agente executa sob sua própria identidade, não uma conta humana compartilhada.
- **L4 se parece com:** Agentes não registrados ("shadow") são detectados automaticamente; o ciclo de vida de identidade (criação, revisão, remoção) é automatizado.
- **Exemplos de evidência:** Inventário de agentes, configuração de identidade (por exemplo Microsoft Entra Agent ID), revisões de acesso.
- **Campo de evidência:** `Evidence (D1-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D2: Capacitação, habilidades e cultura

_6 perguntas. Por que importa: O Gartner espera que GenAI exija que 80% da força de trabalho de engenharia se requalifique até 2027 [30]; DORA pergunta sobre treinamento, aprendizagem entre pares e suporte à experimentação [2]._

### D2-Q1: Treinamento estruturado de IA

**D2-Q1: Os engenheiros recebem treinamento estruturado nas ferramentas de IA e workflows de agentes aprovados, além do onboarding padrão do fornecedor?**

- **Unidade de cobertura:** engenheiros
- **L3 se parece com:** Currículo baseado em função (desenvolvedor, revisor, plataforma, segurança) com conclusão rastreada; o treinamento é exigido antes que recursos de agentes sejam habilitados; ensina padrões que preservam o aprendizado (pedir explicações, tentar primeiro, depois comparar) e não apenas delegação total.
- **L4 se parece com:** O currículo é atualizado a cada trimestre com base em dados de uso e padrões de falha; existem trilhas avançadas (orquestração de agentes, avaliação).
- **Exemplos de evidência:** Trilhas de aprendizagem, taxas de conclusão, regras de bloqueio de habilitação.
- **Campo de evidência:** `Evidence (D2-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D2-Q2: Aprendizagem entre pares e champions

**D2-Q2: Existem formatos regulares de aprendizagem entre pares (demos, brown bags, office hours) e uma rede de champions de IA entre equipes?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Champions existem na maioria das equipes; sessões ocorrem pelo menos mensalmente; gravações e exemplos são compartilhados em um único lugar.
- **L4 se parece com:** Uma comunidade de prática faz curadoria de ativos reutilizáveis (instruções, arquivos de prompt, agentes) e mede sua reutilização.
- **Exemplos de evidência:** Lista de champions, calendário de sessões, repositório compartilhado de exemplos.
- **Campo de evidência:** `Evidence (D2-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D2-Q3: Suporte à experimentação

**D2-Q3: A organização dá aos engenheiros tempo, sandboxes e orçamento para experimentar com segurança novas ferramentas de IA e padrões de agentes?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Ambientes em sandbox e um caminho leve de solicitação existem; experimentos são registrados e seus resultados compartilhados.
- **L4 se parece com:** Experimentos bem-sucedidos entram no catálogo aprovado (D1-Q3) por meio de um caminho definido em semanas.
- **Exemplos de evidência:** Assinaturas de sandbox, log de experimentos, registros de promoção.
- **Campo de evidência:** `Evidence (D2-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D2-Q4: Habilidades de engenharia de contexto

**D2-Q4: Os engenheiros são treinados para dar às ferramentas de IA o contexto correto (escopo claro da tarefa, arquivos relevantes, restrições, exemplos) e manter o contexto enxuto?**

- **Unidade de cobertura:** engenheiros
- **L3 se parece com:** Orientações e exemplos sobre engenharia de contexto fazem parte do treinamento; equipes revisam suas instruções e prompts quanto à qualidade.
- **L4 se parece com:** Práticas de contexto são medidas (por exemplo taxa de sucesso ou uso de tokens por tarefa) e melhoradas ao longo do tempo.
- **Exemplos de evidência:** Páginas de orientação, checklists de review, métricas antes/depois.
- **Campo de evidência:** `Evidence (D2-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D2-Q5: Papéis e trajetórias de carreira

**D2-Q5: Descrições de cargo, frameworks de carreira e expectativas de desempenho foram atualizados para engenharia assistida por IA e agentic engineering (por exemplo dirigir agentes, revisar saída de IA, engenharia de IA)?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Perfis de função atualizados são publicados; avaliações de desempenho reconhecem uso efetivo de IA e qualidade de review, não volume bruto de saída.
- **L4 se parece com:** Existem funções dedicadas (por exemplo engenheiro de IA, responsável pela plataforma de agentes) com um caminho claro de crescimento.
- **Exemplos de evidência:** Framework de carreira, descrições de função.
- **Campo de evidência:** `Evidence (D2-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D2-Q6: Onboarding assistido por IA

**D2-Q6: Novos engenheiros usam ferramentas de IA para entender codebases e se tornarem produtivos, com tempo de ramp-up medido?**

- **Unidade de cobertura:** engenheiros
- **L3 se parece com:** O onboarding inclui tours de codebase guiados por IA e instruções de repositório; tempo até o primeiro PR mergeado é rastreado; novos engenheiros são avaliados em leitura de code e debugging, não apenas em saída.
- **L4 se parece com:** Métricas de ramp-up e habilidades são comparadas entre coortes e usadas para melhorar material e instruções de onboarding.
- **Exemplos de evidência:** Playbook de onboarding, dados de tempo até primeiro PR, resultados de verificação de habilidades.
- **Campo de evidência:** `Evidence (D2-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D3: Planejar, especificar e desenhar

_6 perguntas. Por que importa: em agentic coding, "as pessoas tomam a maior parte das decisões de planejamento (o que fazer) e Claude toma a maior parte das decisões de execução (como fazer)" [24]; a qualidade da definição da tarefa impulsiona a qualidade da saída do agente [8], [27]._

### D3-Q1: IA no refinamento de backlog

**D3-Q1: IA é usada para redigir e refinar issues ou user stories, incluindo critérios de aceite, com um responsável humano que as aprova?**

- **Unidade de cobertura:** times
- **L3 se parece com:** A maioria das equipes usa IA para redigir ou melhorar itens de trabalho; critérios de aceite são obrigatórios antes do trabalho começar.
- **L4 se parece com:** A qualidade dos itens de trabalho (clareza, testabilidade) é medida e vinculada a retrabalho e cycle time.
- **Exemplos de evidência:** Templates de issue, exemplos de itens de trabalho, verificações de qualidade.
- **Campo de evidência:** `Evidence (D3-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D3-Q2: Especificação antes da implementação

**D3-Q2: Para mudanças não triviais, um plano ou especificação escrito é produzido e revisado antes que um agente de IA implemente a mudança?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Planos ou specs são armazenados no repositório ou vinculados à issue, e são revisados por um humano antes da implementação pelo agente.
- **L4 se parece com:** Specs são o contrato para verificação automatizada (testes, checks) e são mantidas sincronizadas com o code.
- **Exemplos de evidência:** Arquivos de spec, reviews de plano, PRs que referenciam specs.
- **Campo de evidência:** `Evidence (D3-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D3-Q3: Escopo de tarefas para agentes

**D3-Q3: As tarefas dadas a coding agents são bem delimitadas (pequenas, com critérios de aceite claros e ponteiros para code relevante) antes da atribuição?**

- **Nota de escopo:** Mede como as tarefas são delimitadas para agentes. A política de autonomia é D1-Q5; o volume de delegação é D4-Q3.
- **Unidade de cobertura:** times
- **L3 se parece com:** Equipes seguem orientação escrita para issues prontas para agentes; tarefas grandes demais são divididas antes da atribuição.
- **L4 se parece com:** Sucesso de tarefas de agentes e taxas de retrabalho são rastreados por tipo de tarefa e usados para refinar a orientação.
- **Exemplos de evidência:** Diretrizes de tarefas para agentes, exemplos de issues, dados de taxa de sucesso.
- **Campo de evidência:** `Evidence (D3-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D3-Q4: Decisões de arquitetura e design

**D3-Q4: IA é usada para apoiar trabalho de design (análise de opções, modos de ameaça e falha, architecture decision records), enquanto as decisões permanecem com humanos responsáveis?**

- **Unidade de cobertura:** times
- **L3 se parece com:** ADRs são versionados; análise assistida por IA é anexada; um humano nomeado aprova cada decisão.
- **L4 se parece com:** Agentes verificam novas mudanças contra decisões registradas e sinalizam conflitos automaticamente.
- **Exemplos de evidência:** Repositório de ADR, registros de design review.
- **Campo de evidência:** `Evidence (D3-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D3-Q5: Foco centrado no usuário

**D3-Q5: O trabalho assistido por IA está vinculado a resultados claros para usuários e informado por feedback de usuários?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Itens de trabalho referenciam o problema do usuário e a medida de sucesso; feedback é revisado antes da priorização.
- **L4 se parece com:** Métricas de resultado do usuário fazem parte da definition of done para entrega assistida por IA.
- **Exemplos de evidência:** Briefs de produto, registros de loop de feedback, dashboards de resultados.
- **Campo de evidência:** `Evidence (D3-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D3-Q6: Modernização assistida por IA

**D3-Q6: Ferramentas e agentes de IA são usados para entender, fazer upgrade e migrar code legado (por exemplo upgrades de framework ou runtime, migração para cloud), com resultados verificados por testes?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Existe um processo repetível de modernização assistida por IA para tipos comuns de upgrade, com gates de teste.
- **L4 se parece com:** O backlog de modernização é reduzido continuamente por agentes sob review humano, com taxas de sucesso rastreadas.
- **Exemplos de evidência:** Runbooks de upgrade, PRs de migração, resultados de testes.
- **Campo de evidência:** `Evidence (D3-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D4: Code e engenharia de contexto

_8 perguntas. Por que importa: GitHub mede a profundidade de adoção como uma progressão de "Code first" para "Agent first" e "Multi-agent" [6]; a Anthropic descreve contexto como "um recurso finito com retornos marginais decrescentes" [25]._

### D4-Q1: Profundidade do uso de IA entre superfícies

**D4-Q1: Quão profundamente os engenheiros usam IA entre superfícies: completions e edições de agentes no IDE, superfícies de agentes do GitHub (cloud agent, code review, CLI), e vários agentes juntos?**

- **Nota de escopo:** Mede quão profundamente IA é usada. Se esse uso é medido é D9-Q1.
- **Unidade de cobertura:** engenheiros
- **L1 a L2 se parecem com:** Principalmente completions e chat ("Code first").
- **L3 se parece com:** Muitos engenheiros usam regularmente pelo menos uma superfície de agente do GitHub ("Agent first"), confirmado por métricas de uso.
- **L4 se parece com:** Uso multi-agent é normal ("Multi-agent"), com distribuição de coortes rastreada mensalmente.
- **Exemplos de evidência:** Dashboard ou API de métricas de uso do Copilot: distribuição de coortes de adoção, usuários ativos diários/semanais.
- **Campo de evidência:** `Evidence (D4-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q2: Modo agente para trabalho multi-file

**D4-Q2: Os engenheiros usam IDE agent mode (ou equivalente) para mudanças multi-file, e revisam toda mudança antes de fazer commit?**

- **Unidade de cobertura:** engenheiros
- **L3 se parece com:** Agent mode é o padrão para refactors e features multi-file na maioria das equipes; mudanças são revisadas no diff antes do commit.
- **L4 se parece com:** Equipes compartilham padrões de agent mode que funcionam e rastreiam onde ele falha; permissões de ferramentas são ajustadas por repositório.
- **Exemplos de evidência:** Uso por feature/mode, diretrizes da equipe.
- **Campo de evidência:** `Evidence (D4-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q3: Delegação a coding agents

**D4-Q3: Coding agents (por exemplo Copilot cloud agent) recebem issues e produzem pull requests que são mergeados após review humano?**

- **Nota de escopo:** Mede quanto trabalho é delegado a coding agents. A política de autonomia é D1-Q5; escopo de tarefas é D3-Q3.
- **Unidade de cobertura:** times
- **L3 se parece com:** A maioria das equipes delega issues adequadas a um coding agent; a parcela de PRs mergeados que são criados por agentes é rastreada.
- **L4 se parece com:** Taxa de merge de PRs de agentes, retrabalho e taxa de correções pós-merge são rastreadas por tipo de tarefa; regras de delegação (D1-Q5) são ajustadas a partir desses dados.
- **Exemplos de evidência:** Contagens de PRs criados por agentes, taxa de merge, tempo até merge, correções de acompanhamento.
- **Campo de evidência:** `Evidence (D4-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q4: Instruções de repositório

**D4-Q4: Os repositórios contêm custom instructions versionadas e revisadas para ferramentas de IA (por exemplo `.github/copilot-instructions.md`, `AGENTS.md`) descrevendo build, test, convenções e restrições?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** A maioria dos repositórios ativos tem instruções estruturadas (build, test, convenções, restrições) com um responsável; mudanças passam por PR review; arquivos são atualizados quando o codebase muda, em vez de serem commitados uma vez.
- **L4 se parece com:** Instruções são geradas a partir de uma base compartilhada, verificadas quanto a desatualização, e seu efeito na taxa de merge de agentes e na qualidade de code é medido, já que arquivos de instrução sozinhos não garantem melhores resultados.
- **Exemplos de evidência:** Arquivos de instrução, cobertura entre repositórios, histórico de mudanças, métricas antes/depois de PRs de agentes.
- **Campo de evidência:** `Evidence (D4-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q5: Prompts, agentes e skills reutilizáveis

**D4-Q5: Existe uma biblioteca compartilhada e curada de arquivos de prompt, custom agents e skills reutilizáveis, com responsáveis e versionamento?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Um repositório central contém arquivos de prompt e custom agents aprovados; equipes os reutilizam em vez de copiar.
- **L4 se parece com:** Ativos são avaliados antes do release (qualidade, custo), o uso é rastreado, e ativos não usados são retirados.
- **Exemplos de evidência:** Repositório da biblioteca, perfis de custom agents, métricas de reutilização.
- **Campo de evidência:** `Evidence (D4-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q6: Governança de MCP servers

**D4-Q6: MCP servers e outras ferramentas de agentes são governados por uma allowlist ou registry, com ferramentas em escopo e responsáveis nomeados?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Uma allowlist enterprise de MCP ou registry customizado é aplicada; cada server tem um responsável, uma security review e ferramentas limitadas.
- **L4 se parece com:** Tool calls são registrados e revisados; novos servers passam por security checks automatizados antes de serem adicionados.
- **Exemplos de evidência:** Política de allowlist ou registry, configuração de MCP, registros de review.
- **Campo de evidência:** `Evidence (D4-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q7: Acesso de IA ao conhecimento interno

**D4-Q7: Ferramentas e agentes de IA conseguem usar com segurança fontes internas (code, documentação, wikis, itens de trabalho) como contexto, por meio de conectores aprovados?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Conectores aprovados dão às ferramentas de IA acesso ciente de permissões às principais fontes internas; respostas citam material interno.
- **L4 se parece com:** Fontes de conhecimento são curadas para uso por IA (atualização, ownership) e a qualidade de retrieval é avaliada.
- **Exemplos de evidência:** Configuração de conectores, avaliações de retrieval.
- **Campo de evidência:** `Evidence (D4-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_

### D4-Q8: Seleção e roteamento de modelos

**D4-Q8: A escolha do modelo é combinada à complexidade da tarefa (modelos menores para trabalho rotineiro, frontier models para trabalho complexo), por orientação ou roteamento automático?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Orientação escrita mapeia tipos de tarefa a modelos; modelos padrão são definidos por política.
- **L4 se parece com:** Roteamento automático está em vigor e é ajustado a partir de dados de custo e qualidade.
- **Exemplos de evidência:** Orientação de modelos, configurações de política, configuração de roteamento.
- **Campo de evidência:** `Evidence (D4-Q8)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D5: Review, qualidade e testes

_7 perguntas. Por que importa: DORA vincula o volume de mudanças impulsionadas por IA à instabilidade, a menos que existam sistemas de controle fortes [3]; GitHub exige revisão humana antes que PRs de agentes sejam mergeados [7]; 46% dos desenvolvedores desconfiam da precisão da saída de IA [37]._

### D5-Q1: AI-assisted code review

**D5-Q1: AI code review (por exemplo Copilot code review) é aplicado a pull requests, com um revisor humano ainda responsável pela aprovação?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** AI review executa automaticamente na maioria dos PRs; equipes rastreiam sugestões úteis versus descartadas.
- **L4 se parece com:** Regras de review são ajustadas por repositório a partir dos resultados de sugestões; tempo de review e defeitos escapados são rastreados; PRs em que apenas IA revisou code criado por IA são visíveis e governados.
- **Exemplos de evidência:** Rulesets de repositório, métricas de adoção de code review, resultados de sugestões.
- **Campo de evidência:** `Evidence (D5-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q2: Human-in-the-loop para mudanças de agentes

**D5-Q2: Pull requests criados por agentes exigem aprovação humana independente (não o solicitante), com workflow runs aprovadas antes de executarem?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Proteções padrão são mantidas: PRs de agentes precisam de um aprovador independente; "Approve and run workflows" não é desabilitado sem uma decisão de risco documentada.
- **L4 se parece com:** Requisitos de aprovação escalam com o risco (D1-Q5) e são auditados; exceções expiram automaticamente.
- **Exemplos de evidência:** Rulesets, branch protection, configurações de agentes.
- **Campo de evidência:** `Evidence (D5-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q3: Mesmos quality gates para code de IA e humano

**D5-Q3: Mudanças geradas por IA e criadas por agentes passam pelos mesmos checks exigidos (build, tests, linting, security scans, coverage) que mudanças humanas?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Checks exigidos são aplicados por rulesets nos protected branches da maioria dos repositórios, sem bypass para identidades de agentes.
- **L4 se parece com:** Gates são policy as code, aplicados em todos os repositórios (>90%) e revisados após incidentes.
- **Exemplos de evidência:** Rulesets, checks exigidos, listas de bypass.
- **Campo de evidência:** `Evidence (D5-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q4: Lotes pequenos

**D5-Q4: As mudanças são mantidas pequenas (limites de tamanho de PR, uma preocupação por PR), incluindo mudanças produzidas por agentes?**

- **Nota de escopo:** Mede o tamanho das mudanças assistidas por IA. Com que frequência o code é commitado e quão rápido é revertido é D8-Q2.
- **Unidade de cobertura:** times
- **L3 se parece com:** Orientação de tamanho de PR é aplicada ou monitorada; PRs de agentes grandes demais são divididos antes do review.
- **L4 se parece com:** Tamanho de lote é rastreado em relação a change failure rate e tempo de review, e usado para ajustar limites.
- **Exemplos de evidência:** Distribuição de tamanho de PR, configuração de bot ou ruleset.
- **Campo de evidência:** `Evidence (D5-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q5: Testes assistidos por IA

**D5-Q5: IA é usada para gerar e manter testes, com qualidade dos testes verificada (por exemplo coverage do code alterado, mutation testing) em vez de apenas contagem de testes?**

- **Nota de escopo:** Mede IA usada para escrever e melhorar testes. Se testes automatizados atuam como gate é D8-Q7.
- **Unidade de cobertura:** times
- **L3 se parece com:** A maioria das equipes usa IA para escrever testes; coverage de linhas alteradas é um check exigido.
- **L4 se parece com:** Efetividade dos testes (mutation score, defeitos escapados) é rastreada; flaky tests são detectados e colocados em quarentena automaticamente.
- **Exemplos de evidência:** Relatórios de coverage, resultados de mutation testing, dashboard de flaky tests.
- **Campo de evidência:** `Evidence (D5-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q6: Cultura de verificação e confiança calibrada

**D5-Q6: Os engenheiros verificam sistematicamente a saída de IA (executam, testam, leem) e a confiança na saída de IA é medida ao longo do tempo?**

- **Nota de escopo:** Mede comportamento de review e calibração de confiança. Como developer experience é pesquisada é D9-Q4.
- **Unidade de cobertura:** times
- **L3 se parece com:** Diretrizes de review explicam o que verificar na saída de IA; confiança na saída de IA faz parte da pesquisa com desenvolvedores.
- **L4 se parece com:** Confiança e precisão são comparadas com dados reais de defeitos, e a orientação é atualizada onde divergem.
- **Exemplos de evidência:** Diretrizes de review, resultados de pesquisa, análise de defeitos.
- **Campo de evidência:** `Evidence (D5-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D5-Q7: Saúde do code gerado por IA

**D5-Q7: A saúde de longo prazo do code gerado por IA é monitorada (duplicação, churn, complexidade, manutenibilidade)?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Métricas de code health são coletadas para a maioria dos repositórios e revisadas em retrospectivas de equipe; code gerado por IA tem um responsável humano nomeado.
- **L4 se parece com:** Tendências de saúde (por exemplo complexidade cognitiva, avisos de static analysis) são comparadas entre code com alta presença de IA e outros codes, com ações corretivas rastreadas.
- **Exemplos de evidência:** Dashboards de static analysis, relatórios de churn, arquivos de ownership.
- **Campo de evidência:** `Evidence (D5-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D6: Segurança e AI Supply Chain

_7 perguntas. Por que importa: OWASP lista prompt injection (LLM01), supply chain (LLM03) e agência excessiva (LLM06) entre os principais riscos [38], e agent goal hijack (ASI01) em primeiro lugar para aplicações agentic [39]; NIST SP 800-218A adiciona práticas específicas de IA ao SSDF [40]._

### D6-Q1: Scanning de base em todo repositório

**D6-Q1: Code scanning (SAST), secret scanning com push protection e dependency review são aplicados a todos os repositórios, incluindo branches de agentes?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Habilitado por padrão para todos os repositórios novos e a maioria dos existentes; push protection se aplica a todo commit, humano ou de agente; alertas têm responsáveis e metas de nível de serviço.
- **L4 se parece com:** A cobertura é quase completa e verificada automaticamente; mean time to remediate é rastreado.
- **Exemplos de evidência:** Dashboard de cobertura de segurança, tempo de remediação.
- **Campo de evidência:** `Evidence (D6-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q2: Remediação assistida por IA

**D6-Q2: Remediação assistida por IA (por exemplo autofix para code scanning) é usada para corrigir vulnerabilidades, com correções revisadas e testadas antes do merge?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Sugestões de autofix são habilitadas para a maioria dos repositórios; taxas de aceitação e reabertura são rastreadas.
- **L4 se parece com:** Campanhas de segurança usam remediação com IA em escala, e o tempo de remediação é reportado à liderança.
- **Exemplos de evidência:** Configurações de autofix, métricas de remediação.
- **Campo de evidência:** `Evidence (D6-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q3: Defesas contra prompt injection para agentes

**D6-Q3: Agentes são protegidos contra prompt injection e goal hijack (conteúdo não confiável tratado como dados, instruções ocultas filtradas, saída de rede restrita)?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Agent firewalls e restrições de egress permanecem ativados; a orientação informa às equipes quais fontes de conteúdo não são confiáveis.
- **L4 se parece com:** Agentes passam regularmente por red team contra cenários OWASP LLM01 e ASI01; achados são rastreados até o fechamento.
- **Exemplos de evidência:** Configuração de firewall, relatórios de red team.
- **Campo de evidência:** `Evidence (D6-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q4: Least privilege para agentes

**D6-Q4: Agentes executam com least privilege (tokens com escopo, sem segredos de produção, branches restritos, ambientes em sandbox)?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Permissões de agentes são documentadas e revisadas; agentes não conseguem acessar credenciais de produção nem fazer push para protected branches.
- **L4 se parece com:** Permissões são just-in-time e limitadas no tempo; o acesso é revisado automaticamente.
- **Exemplos de evidência:** Configuração de ambiente de agentes, escopos de token, revisões de acesso.
- **Campo de evidência:** `Evidence (D6-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q5: AI supply chain

**D6-Q5: Modelos, MCP servers, extensões de IDE e ferramentas de agentes são avaliados antes do uso, com proveniência e SBOMs para o que você constrói e entrega?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Um processo de review cobre componentes de IA; SBOMs e proveniência de build são produzidos para a maioria dos builds.
- **L4 se parece com:** Proveniência é verificada no deploy (por exemplo metas de nível SLSA); componentes não avaliados são bloqueados automaticamente.
- **Exemplos de evidência:** Registros de review de componentes, amostras de SBOM e atestação.
- **Campo de evidência:** `Evidence (D6-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q6: Threat modeling para features e agentes de IA

**D6-Q6: Features de IA e workflows agentic são threat-modeled com riscos específicos de IA (OWASP LLM and Agentic Top 10, NIST SP 800-218A)?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** Threat models são exigidos para novas features de IA e workflows de agentes, e revisados por segurança.
- **L4 se parece com:** Threat models são atualizados após incidentes e exercícios de red team; controles são verificados por testes automatizados.
- **Exemplos de evidência:** Documentos de threat model, registros de security review.
- **Campo de evidência:** `Evidence (D6-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D6-Q7: Trilha de auditoria para ações de agentes

**D6-Q7: Sessões e ações de agentes (prompts, tool calls, commits, aprovações) são registradas, atribuíveis a uma identidade e retidas de acordo com a política?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Atividade de agentes é registrada centralmente e vinculada ao usuário solicitante e à identidade do agente.
- **L4 se parece com:** Logs alimentam detecção de anomalias; auditorias conseguem reconstruir qualquer mudança de agente de ponta a ponta.
- **Exemplos de evidência:** Configuração de audit log, exemplo de investigação.
- **Campo de evidência:** `Evidence (D6-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D7: Entregar e operar

_6 perguntas. Por que importa: mais mudanças geradas por IA precisam de redes de segurança fortes na entrega [3], [5]; a Microsoft recomenda observação contínua da atividade de agentes [19] e está estendendo agentes para operações de cloud [22]._

### D7-Q1: IA em pipelines CI/CD

**D7-Q1: IA é usada para criar, manter e solucionar problemas em pipelines CI/CD (por exemplo explicar runs com falha, propor correções), sobre pipeline-as-code?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Pipelines são code na maioria dos repositórios; análise de falhas assistida por IA está disponível para todas as equipes.
- **L4 se parece com:** Agentes propõem correções e otimizações de pipeline automaticamente, sob review, com tempo de build e taxa de falhas rastreados.
- **Exemplos de evidência:** Repositórios de pipeline, uso de análise de falhas, métricas de build.
- **Campo de evidência:** `Evidence (D7-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D7-Q2: Entrega progressiva e rollback

**D7-Q2: As equipes conseguem lançar mudanças assistidas por IA com segurança por meio de entrega progressiva (feature flags, canary ou blue/green) e rollback automatizado?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** A maioria dos serviços usa feature flags ou rollout em estágios; rollback é automatizado para serviços críticos.
- **L4 se parece com:** Decisões de rollout são conduzidas automaticamente por sinais de saúde; change failure rate e tempo de recuperação são rastreados por serviço.
- **Exemplos de evidência:** Plataforma de feature flags, configuração de rollout, registros de rollback.
- **Campo de evidência:** `Evidence (D7-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D7-Q3: Resposta a incidentes assistida por IA

**D7-Q3: IA é usada em resposta a incidentes (correlação de alertas, sumarização, hipóteses de causa raiz, rascunhos de revisão pós-incidente) com humanos no comando?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** Engenheiros de on-call na maioria das equipes usam IA para triage e resumos; revisões pós-incidente registram se a IA ajudou.
- **L4 se parece com:** Agentes de operações executam diagnósticos aprovados automaticamente; tempo de restauração é comparado antes e depois da adoção.
- **Exemplos de evidência:** Configuração de ferramentas de incidentes, timelines de incidentes, dados de tempo de restauração.
- **Campo de evidência:** `Evidence (D7-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D7-Q4: Observabilidade de agentes

**D7-Q4: Agentes de IA no SDLC são observáveis (traces de runs e tool calls, latência, falhas, custo), por exemplo por meio de OpenTelemetry?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Runs de agentes emitem telemetria para a stack central de observabilidade; dashboards mostram falhas e custo por agente.
- **L4 se parece com:** Alertas disparam em drift de agentes, picos de erro ou anomalias de custo; achados alimentam governança (D1).
- **Exemplos de evidência:** Dashboards de telemetria, regras de alerta.
- **Campo de evidência:** `Evidence (D7-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D7-Q5: Infrastructure as code com guardrails

**D7-Q5: IA é usada para escrever e revisar infrastructure as code, com guardrails de policy-as-code que bloqueiam mudanças não conformes?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** A maior parte da infraestrutura é code; IaC gerado por IA passa pelos mesmos policy checks e plan reviews.
- **L4 se parece com:** Drift é detectado e corrigido por meio de GitOps; violações de política por IaC gerado por IA são rastreadas e estão em queda.
- **Exemplos de evidência:** Repositórios de IaC, regras de policy-as-code, relatórios de drift.
- **Campo de evidência:** `Evidence (D7-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D7-Q6: Automação operacional orientada por agentes

**D7-Q6: Tarefas operacionais (runbooks, remediação, atualizações de dependências e patches) são automatizadas por agentes sob regras de aprovação definidas?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** Runbooks comuns e atualizações de dependências são automatizados; aprovações seguem a matriz de autonomia (D1-Q5).
- **L4 se parece com:** A maioria das operações rotineiras executa automaticamente com aprovações auditadas; o esforço humano se desloca para exceções.
- **Exemplos de evidência:** Catálogo de automação, logs de aprovação.
- **Campo de evidência:** `Evidence (D7-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D8: Fundamentos de engenharia (amplificadores de IA)

_7 perguntas. Por que importa: DORA constata que essas capacidades amplificam os benefícios da adoção de IA, e que uma plataforma interna de alta qualidade se correlaciona com a capacidade de desbloquear valor de IA [1], [3]._

### D8-Q1: Controle de versão para tudo

**D8-Q1: Application code, configuração, automação de build, configuração de sistema e prompts/instruções de IA estão todos armazenados em controle de versão?**

- **Unidade de cobertura:** times
- **L3 se parece com:** Todos os cinco tipos de ativos são versionados para a maioria dos serviços.
- **L4 se parece com:** Nada chega à produção sem uma fonte versionada; checks confirmam isso automaticamente.
- **Exemplos de evidência:** Inventário de repositórios, fontes de configuração.
- **Campo de evidência:** `Evidence (D8-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q2: Frequência de commit e rollback rápido

**D8-Q2: Os engenheiros fazem commit de mudanças pequenas com frequência e contam com undo/revert rápido ao experimentar com saída de IA?**

- **Nota de escopo:** Mede frequência de commit e velocidade de rollback. O tamanho das mudanças assistidas por IA é D5-Q4.
- **Unidade de cobertura:** times
- **L3 se parece com:** A maioria dos engenheiros faz commit pelo menos diariamente; reverter uma mudança é rotina e rápido.
- **L4 se parece com:** Trunk-based development com branches de curta duração é a norma; tempo de revert é medido.
- **Exemplos de evidência:** Dados de frequência de commit, idade de branch.
- **Campo de evidência:** `Evidence (D8-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q3: Plataforma interna de qualidade

**D8-Q3: Existe uma internal developer platform fácil de usar, que abstrai infraestrutura e torna o caminho seguro e conforme o padrão para humanos e agentes?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Uma equipe dedicada de plataforma oferece golden paths de self-service usados pela maioria das equipes; a equipe age com base em feedback.
- **L4 se parece com:** Agentes usam as mesmas APIs e guardrails da plataforma que humanos; satisfação com a plataforma é medida e melhora.
- **Exemplos de evidência:** Catálogo da plataforma, golden paths, pesquisa de satisfação.
- **Campo de evidência:** `Evidence (D8-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q4: Ecossistema de dados saudável

**D8-Q4: Engenheiros e ferramentas de IA conseguem encontrar e usar dados internos confiáveis (não em silos, de boa qualidade, respondíveis rapidamente)?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Dados-chave são catalogados com responsáveis e indicadores de qualidade; a maioria das perguntas pode ser respondida em até uma hora.
- **L4 se parece com:** Qualidade de dados é monitorada automaticamente; linhagem e contratos existem para dados críticos.
- **Exemplos de evidência:** Catálogo de dados, dashboards de qualidade.
- **Campo de evidência:** `Evidence (D8-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q5: Ambientes reproduzíveis para humanos e agentes

**D8-Q5: Ambientes de desenvolvimento são reproduzíveis (devcontainers, cloud workspaces, toolchains fixadas) para que humanos e agentes façam build e test da mesma forma?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** A maioria dos repositórios define um ambiente reproduzível; agentes usam a mesma definição.
- **L4 se parece com:** Ambientes iniciam em minutos para qualquer repositório; drift em relação à definição é detectado.
- **Exemplos de evidência:** Arquivos devcontainer, tempos de start-up de ambiente.
- **Campo de evidência:** `Evidence (D8-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q6: Documentação como contexto pronto para IA

**D8-Q6: A documentação é mantida como code, atual e com ownership, para que sirva como contexto confiável para ferramentas de IA?**

- **Unidade de cobertura:** repositórios
- **L3 se parece com:** Docs ficam junto ao code com responsáveis; docs desatualizadas são sinalizadas em reviews.
- **L4 se parece com:** Atualização é verificada automaticamente; mudanças de docs geradas por IA são revisadas como code.
- **Exemplos de evidência:** Repositórios de docs, checks de atualização.
- **Campo de evidência:** `Evidence (D8-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D8-Q7: Testes automatizados como sistema de controle

**D8-Q7: Testes automatizados são profundos e rápidos o suficiente para capturar regressões de altos volumes de mudanças geradas por IA (unit, integration, end-to-end, contract)?**

- **Nota de escopo:** Mede testes automatizados como sistema de controle. IA usada para escrever testes é D5-Q5.
- **Unidade de cobertura:** serviços
- **L3 se parece com:** A maioria dos serviços tem testes automatizados em camadas que executam em todo PR dentro de time budgets acordados.
- **L4 se parece com:** Suites de teste são ajustadas a partir de dados de defeitos escapados; tempo de feedback é rastreado e melhora.
- **Exemplos de evidência:** Inventário de suites de teste, durações de pipeline, dados de defeitos escapados.
- **Campo de evidência:** `Evidence (D8-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_

---

## Seção D9: Medição, valor e AI FinOps

_7 perguntas. Por que importa: estudos controlados variam de 55.8% mais rápido [33] e 26.08% mais tarefas concluídas [34] a 19% mais lento com uma forte lacuna de percepção [35], portanto as organizações precisam de sua própria medição objetiva; o Gartner prevê que os custos de AI coding ultrapassarão o salário médio de um desenvolvedor até 2028 [32]._

### D9-Q1: Métricas de profundidade de adoção

**D9-Q1: A adoção de IA é rastreada com telemetria além da contagem de seats (usuários ativos, engajamento por feature, coortes de adoção)?**

- **Nota de escopo:** Mede se a adoção é rastreada. Quão profundamente IA é usada é D4-Q1.
- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Métricas de uso (por exemplo a API ou dashboard de métricas de uso do Copilot) são revisadas mensalmente pela liderança de engenharia.
- **L4 se parece com:** Movimento de coortes é uma meta gerenciada; ações de capacitação são avaliadas por seu efeito nas coortes.
- **Exemplos de evidência:** Dashboards de uso, relatórios de tendência de coortes.
- **Campo de evidência:** `Evidence (D9-Q1)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q2: Métricas de resultado de entrega

**D9-Q2: Métricas de entrega de software (lead time, deployment frequency, change failure rate, time to restore) são rastreadas e comparadas antes e depois da adoção de IA?**

- **Unidade de cobertura:** serviços
- **L3 se parece com:** Métricas DORA são coletadas automaticamente para a maioria dos serviços e revisadas com dados de adoção de IA.
- **L4 se parece com:** Métricas de entrega fazem parte das decisões de investimento em IA; regressões disparam ação corretiva.
- **Exemplos de evidência:** Dashboards DORA, comparação baseline versus atual.
- **Campo de evidência:** `Evidence (D9-Q2)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q3: Métricas de fluxo de pull request

**D9-Q3: Throughput de PR, tempo até merge e a parcela e taxa de merge de PRs criados por IA ou agentes são rastreados?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Métricas de ciclo de vida de PR são reportadas por organização; PRs criados por agentes são identificados separadamente, incluindo sua taxa de correções pós-merge.
- **L4 se parece com:** Métricas de fluxo são vinculadas a métricas de qualidade (D5) para que fluxo mais rápido não seja comprado com instabilidade.
- **Exemplos de evidência:** Métricas de ciclo de vida de PR, relatórios de PRs de agentes, análise de correções de acompanhamento.
- **Campo de evidência:** `Evidence (D9-Q3)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q4: Developer experience e fricção

**D9-Q4: Developer experience é medida regularmente (produtividade percebida, fricção, confiança em IA, satisfação), usando um framework reconhecido como SPACE ou as perguntas de resultado do DORA?**

- **Nota de escopo:** Mede a pesquisa de developer experience. Comportamento de review e calibração de confiança é D5-Q6.
- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Uma pesquisa ocorre pelo menos duas vezes por ano com boa participação; resultados são compartilhados e geram ações.
- **L4 se parece com:** Resultados de pesquisa são combinados com telemetria (D9-Q1 a Q3) para encontrar e remover fricção.
- **Exemplos de evidência:** Instrumento de pesquisa, taxa de participação, log de ações.
- **Campo de evidência:** `Evidence (D9-Q4)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q5: Medição controlada de impacto

**D9-Q5: O impacto de IA é estimado com comparações controladas ou baseadas em coortes (por exemplo piloto versus controle, coortes de adoção, antes/depois com um baseline) em vez de apenas estimativas autorreportadas?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Pelo menos uma comparação controlada ou de coorte foi executada e documentada, com suas limitações.
- **L4 se parece com:** Comparações são executadas continuamente para ferramentas e práticas principais; decisões as citam.
- **Exemplos de evidência:** Desenho do estudo, resultados, registros de decisão.
- **Campo de evidência:** `Evidence (D9-Q5)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q6: Governança de custos de IA (AI FinOps)

**D9-Q6: Custos de IA (seats, premium requests, tokens, runs de agentes) são orçados, monitorados por equipe e caso de uso, com thresholds e revisões regulares?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Orçamentos e thresholds de alerta existem por organização ou equipe; workflows de alto consumo são revisados em retrospectivas.
- **L4 se parece com:** Custo por resultado (por exemplo por PR mergeado) é rastreado; práticas de roteamento e contexto são ajustadas para reduzir desperdício.
- **Exemplos de evidência:** Dashboards de custo, alertas de orçamento, notas de retrospectiva.
- **Campo de evidência:** `Evidence (D9-Q6)` · _Ferramenta, % de cobertura, métrica, período, link_

### D9-Q7: Vínculo com valor de negócio

**D9-Q7: Resultados de engenharia com IA são conectados a valor de negócio (business case, premissas de ROI, OKRs) e revisados com stakeholders de finanças ou negócio?**

- **Unidade de cobertura:** prática da organização inteira (use as colunas de governança e medição)
- **L3 se parece com:** Existe um business case com premissas explícitas e ele é revisado pelo menos anualmente.
- **L4 se parece com:** Valor é reportado em uma cadência fixa com insumos medidos de D9-Q1 a Q6; investimento é ajustado a partir dos resultados.
- **Exemplos de evidência:** Business case, relatórios de valor.
- **Campo de evidência:** `Evidence (D9-Q7)` · _Ferramenta, % de cobertura, métrica, período, link_
