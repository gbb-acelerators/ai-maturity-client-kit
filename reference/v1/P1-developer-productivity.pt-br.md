# Assessment de Maturidade IA: Pilar P1, Produtividade do Desenvolvedor

🌐 [English](P1-developer-productivity.md) · Português (Brasil) · [Español](P1-developer-productivity.es.md)

> Mede o quanto a engenharia adota IA para acelerar o ciclo de codificação, documentação, revisão, onboarding e colaboração interna.

## Visão geral

- **Pilar:** `P1`: Produtividade do Desenvolvedor
- **Capacidades (capabilities):** 9
- **Questões totais:** 53
- **Escala:** Likert L0 a L4 (Inicial → Otimizando)
- **Idioma da pergunta:** Português (Brasil)
- **Idioma dos KPIs:** inglês em todas as versões (nomes de métrica, como no `framework.json`)
- **Resposta esperada por questão:** 1 nível selecionado + texto de evidência (mín. recomendado 80 caracteres) + anexo opcional

## Como interpretar a escala

| Nível | Rótulo | Significado |
|---|---|---|
| **L0** | Inicial | Sem prática estabelecida; ações ad-hoc, sem ferramenta ou política. |
| **L1** | Em Desenvolvimento | Pilotos isolados, cobertura <25%, sem governança. |
| **L2** | Definido | Adoção em 25-50% das equipes, com diretrizes e treinamento básico. |
| **L3** | Gerenciado | Cobertura >75% com métricas de impacto e bibliotecas/templates compartilhados. |
| **L4** | Otimizando | Cobertura quase universal (>95%), automação, ajuste fino, melhoria contínua mensurada. |

## Tipos de informação coletada por questão

Cada questão captura simultaneamente **três tipos de dado**:

1. **Quantitativo (KPI):** uma métrica numérica explícita (ex.: % desenvolvedores ativos, MTTR, lead time, taxa de cobertura). Use o KPI sugerido para padronizar comparação entre equipes.

2. **Qualitativo (descrição do nível):** o respondente seleciona o nível L0 a L4 cuja descrição melhor representa a realidade observada hoje (não a aspiracional).

3. **Evidência (texto + anexos):** prova documental, como link de pipeline, screenshot de dashboard, política, runbook, contrato de licenças, métrica exportada. Quanto mais específica, maior a qualidade da evidência (escala: nenhuma → mínima → adequada → detalhada → exemplar).

## Critérios de qualidade da evidência

- **Mínima (<80 caracteres):** texto genérico, sem nome de ferramenta, métrica ou link.
- **Adequada (80-250):** menciona ferramenta + cobertura/escopo aproximado.
- **Detalhada (250-500):** inclui métrica numérica + link/anexo + período de medição.
- **Exemplar (>500 ou múltiplos anexos):** múltiplas fontes corroborantes, série temporal, comparativo antes/depois.

## Capacidades do pilar P1

- **P1-C1**: Assistentes de Codificação IA (5 questões)
- **P1-C2**: Plataforma de Experiência do Desenvolvedor (6 questões)
- **P1-C3**: Gestão do Conhecimento (6 questões)
- **P1-C4**: Automação de Revisão de Código (7 questões)
- **P1-C5**: Onboarding e Treinamento de Desenvolvedores (7 questões)
- **P1-C6**: Inner Source e Colaboração (6 questões)
- **P1-C7**: Automação de Documentação (5 questões)
- **P1-C8**: Medição de Produtividade do Desenvolvedor (6 questões)
- **P1-C9**: Automação de Ambientes e Espaços de Trabalho (5 questões)

---

## P1-C1: Assistentes de Codificação IA

**5 questões neste capability.**

### P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% developers using AI completion`

**Contexto**

- **O que mede (what):** Mede a adoção de ferramentas de completação de código e sugestões com IA em toda a equipe de desenvolvimento.
- **Por que importa (why):** Assistentes de codificação com IA podem aumentar a velocidade dos desenvolvedores em 30-55% em tarefas rotineiras de codificação, reduzindo o time-to-market.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ferramentas de IA de codificação implementadas. Todo o código é escrito manualmente sem assistência de IA. | • Sem licenças de ferramentas de IA<br>• Sem políticas para ferramentas de IA<br>• Fluxos de trabalho de codificação apenas manuais |
| **L1** | Em Desenvolvimento | Implementação piloto de assistente de codificação IA para <10% dos desenvolvedores. Uso ad-hoc sem diretrizes. | • Documentação do programa piloto<br>• < 10% de alocação de licenças<br>• Nenhuma política de uso definida |
| **L2** | Definido | Assistente de codificação IA implantado para 25-50% dos desenvolvedores com diretrizes de uso e treinamento básico. | • 25-50% de cobertura de licenças<br>• Diretrizes de uso por escrito<br>• Materiais de treinamento para autocompletar |
| **L3** | Gerenciado | Assistente de codificação IA implantado para >75% dos desenvolvedores com ganhos de produtividade medidos >15% e bibliotecas de prompts. | • >75% de usuários ativos<br>• Métricas de produtividade mostrando ganho >15%<br>• Repositório compartilhado de biblioteca de prompts |
| **L4** | Otimizando | Assistente de codificação IA universal (>95%) com ajuste fino de modelo personalizado e melhoria de velocidade medida >30%. | • >95% de uso diário ativo<br>• Configuração de fine-tuning de modelo personalizado<br>• Melhoria medida de velocidade >30%<br>• Rastreamento automatizado da qualidade das sugestões |

---

### P1-C1-Q2: Quão efetivamente sua equipe aproveita IA para revisão de código e melhoria de qualidade?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs with AI review`

**Contexto**

- **O que mede (what):** Mede o uso de IA nos processos de revisão de código para detectar bugs, sugerir melhorias e impor padrões.
- **Por que importa (why):** A revisão de código assistida por IA reduz o tempo de revisão em 40% e detecta 20% mais defeitos do que a revisão apenas manual.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem participação de IA em revisão de código. Todas as revisões são revisões manuais entre pares. | • Processo de revisão apenas manual<br>• Sem ferramentas de revisão por IA<br>• Sem quality gates automatizados |
| **L1** | Em Desenvolvimento | Linting básico e ferramentas de análise estática em CI. Sem sugestões de revisão impulsadas por IA. | • Configuração de linting em CI<br>• Configuração de ferramenta de análise estática<br>• Nenhum bot de revisão por IA configurado |
| **L2** | Definido | Bot de revisão com IA configurado em 30-60% dos repositórios, fornecendo sugestões automatizadas de código. | • Bot de revisão por IA em 30-60% dos repositórios<br>• Exemplos de sugestões em PR<br>• Documentação de configuração do bot de revisão |
| **L3** | Gerenciado | Revisão com IA integrada em >80% dos repositórios com regras personalizadas alinhadas aos padrões da equipe. | • >80% de cobertura de repositórios<br>• Configuração de regras personalizadas<br>• Redução medida >25% no ciclo de revisão |
| **L4** | Otimizando | IA realiza primeira revisão em todos os PRs, aprovando automaticamente mudanças de baixo risco e escalando as críticas. | • 100% dos PRs com primeira passada por IA<br>• Política de aprovação automática documentada<br>• Modelo de classificação de risco<br>• Redução >50% no tempo de ciclo |

---

### P1-C1-Q3: Como sua organização mede e rastreia o impacto das ferramentas de codificação IA na produtividade?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 0.8
- **Professional Edition:** Não
- **KPI principal:** `Productivity measurement maturity`

**Contexto**

- **O que mede (what):** Mede a capacidade da organização de quantificar o valor das ferramentas de codificação com IA.
- **Por que importa (why):** Sem medição, as organizações não conseguem justificar o investimento em ferramentas de IA nem otimizar estratégias de adoção.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem medição do impacto das ferramentas de IA. Sem métricas de produtividade base capturadas. | • Sem métricas DORA<br>• Sem dashboards de produtividade<br>• Sem rastreamento de uso de ferramentas de IA |
| **L1** | Em Desenvolvimento | Feedback anedótico de desenvolvedores sobre a utilidade de ferramentas de IA. Sem medição quantitativa. | • Resultados de pesquisa com desenvolvedores<br>• Coleta informal de feedback<br>• Sem dados quantitativos |
| **L2** | Definido | Métricas DORA básicas rastreadas (frequência de implantação, tempo de entrega). Análise de uso de ferramentas de IA disponível. | • Dashboard de métricas DORA<br>• Relatório mensal de análise de uso<br>• Medições de baseline estabelecidas |
| **L3** | Gerenciado | Métricas abrangentes de produtividade do desenvolvedor incluindo medidas específicas de IA: taxa de aceitação, tempo economizado. | • Taxa de aceitação de sugestões >40%<br>• Melhoria >20% no tempo até merge<br>• Análise de tendência de densidade de defeitos |
| **L4** | Otimizando | Plataforma de inteligência de produtividade em tempo real correlacionando o uso de ferramentas de IA com resultados de negócio. | • Dashboard de produtividade em tempo real<br>• Relatórios automatizados de ROI<br>• Análise de correlação com resultados de negócio<br>• Recomendações de otimização por equipe |

---

### P1-C1-Q4: Qual nível de capacidades de testes assistidos por IA sua organização emprega?

**Metadados**

- **Público-alvo:** Desenvolvedor, qa-test, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% test coverage from AI generation`

**Contexto**

- **O que mede (what):** Mede o uso de IA para gerar, manter e otimizar suítes de testes.
- **Por que importa (why):** Testes gerados por IA podem aumentar a cobertura de 40% para 80% em semanas, detectando regressões que testes manuais deixam passar.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Todos os testes escritos manualmente. Cobertura de testes inferior a 40% na maioria dos projetos. | • Apenas escrita manual de testes<br>• <40% de cobertura média<br>• Sem ferramentas de geração de testes por IA |
| **L1** | Em Desenvolvimento | Uso ocasional de IA para gerar esqueletos de testes unitários. A cobertura permanece abaixo de 50%. | • Geração ad-hoc de testes por IA<br>• Taxa de cobertura medida <50%<br>• Sem abordagem sistemática |
| **L2** | Definido | Geração de testes com IA integrada no fluxo de desenvolvimento para 30-50% do novo código. Cobertura >60%. | • Geração de testes por IA em 30-50% do código novo<br>• Gates de 60% de cobertura em CI<br>• Diretrizes de geração de testes |
| **L3** | Gerenciado | IA gera >70% de testes unitários com revisão humana. Cobertura >75%. IA identifica casos extremos. | • >70% de testes gerados por IA<br>• >75% de cobertura entre projetos<br>• Exemplos de sugestões de casos de borda |
| **L4** | Otimizando | Otimização de testes impulsionada por IA: gera suites de regressão automaticamente, identifica testes instáveis, otimiza cobertura. | • Taxa de cobertura medida >85%<br>• Taxa de testes flaky <5%<br>• Geração automatizada de suíte de regressão<br>• Integração de testes de mutação |

---

### P1-C1-Q5: Como sua organização governa o código gerado por IA em termos de segurança e conformidade?

**Metadados**

- **Público-alvo:** Desenvolvedor, Segurança, product-owner, qa-test
- **Peso:** 1.1
- **Professional Edition:** Não
- **KPI principal:** `AI code governance maturity`

**Contexto**

- **O que mede (what):** Mede políticas e controles sobre qualidade, segurança e conformidade de propriedade intelectual do código gerado por IA.
- **Por que importa (why):** Sem governança, o código gerado por IA pode introduzir vulnerabilidades, violações de licença e riscos de conformidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem governança sobre código gerado por IA. Nenhuma política existe. Desenvolvedores usam ferramentas de IA sem restrições. | • Sem política para código de IA<br>• Sem varredura de segurança de código de IA<br>• Sem verificações de conformidade de licenças |
| **L1** | Em Desenvolvimento | Política básica existe proibindo uso de IA em módulos sensíveis à segurança. Sem automação. | • Política de uso de IA por escrito<br>• Lista de módulos sensíveis à segurança<br>• Sem enforcement automatizado |
| **L2** | Definido | Código gerado por IA passa por análise de segurança padrão (SAST/DAST). Verificação de conformidade de licenças em CI. | • Pipeline SAST/DAST inclui código de IA<br>• Varredura de conformidade de licenças<br>• Enforcement de políticas em CI |
| **L3** | Gerenciado | Portões de qualidade de código dedicados para IA: varredura de vulnerabilidades, auditoria de licenças, revisão de qualidade de código. | • Quality gates específicos de IA<br>• Rastreamento de proveniência de código<br>• Taxa de sinalização de segurança <2%<br>• Relatórios trimestrais de auditoria |
| **L4** | Otimizando | Governança de código IA em tempo real: cada sugestão varrida antes de exibir, licenças bloqueadas e métricas de qualidade rastreadas. | • Varredura de conteúdo antes da exibição habilitada<br>• Rejeição automática de licenças bloqueadas<br>• Política de zero código de IA sem revisão<br>• Certificação de conformidade alcançada |

---

## P1-C2: Plataforma de Experiência do Desenvolvedor

**6 questões neste capability.**

### P1-C2-Q1: Quão maduro é seu portal ou plataforma interna para desenvolvedores?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `Developer portal adoption %`

**Contexto**

- **O que mede (what):** Mede a maturidade de um portal centralizado para desenvolvedores para catálogo de serviços, documentação e self-service.
- **Por que importa (why):** Um portal de desenvolvedores maduro reduz o tempo de onboarding em 60% e elimina a troca de contexto entre ferramentas.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem portal de desenvolvedores. Documentação espalhada por wikis, Slack e email. | • Sem portal centralizado<br>• Documentação em várias ferramentas<br>• Sem catálogo de serviços |
| **L1** | Em Desenvolvimento | Wiki básico ou espaço no Confluence com alguma documentação. Sem catálogo de serviços ou capabilities self-service. | • Wiki central existente<br>• Alguma documentação de APIs<br>• Sem catálogo de serviços |
| **L2** | Definido | Portal de desenvolvedores implantado (Backstage ou similar) com catálogo de serviços cobrindo >50% dos serviços. Templates básicos de documentação. | • >50% dos serviços catalogados<br>• Documentação de implantação do portal<br>• Templates de documentação publicados |
| **L3** | Gerenciado | Portal de desenvolvedores cobre >80% dos serviços com scaffolding self-service, documentação de API automatizada e status de CI/CD integrado. Tempo de onboarding reduzido >40%. | • >80% de cobertura de serviços<br>• Ferramentas de scaffolding self-service<br>• Redução >40% no tempo de onboarding |
| **L4** | Otimizando | Portal de desenvolvedores com IA: busca em linguagem natural em toda a documentação, diagramas de arquitetura gerados automaticamente, detecção preditiva de problemas. Satisfação dos desenvolvedores >95%. | • Busca com IA habilitada<br>• Diagramas de arquitetura gerados automaticamente<br>• Pontuação de satisfação >95%<br>• Detecção preditiva de problemas |

---

### P1-C2-Q2: Quão efetivamente suas equipes usam ambientes de desenvolvimento padronizados?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 0.9
- **Professional Edition:** Sim
- **KPI principal:** `Environment setup time (minutes)`

**Contexto**

- **O que mede (what):** Mede a padronização dos ambientes de desenvolvimento entre as equipes.
- **Por que importa (why):** Ambientes padronizados eliminam problemas de 'funciona na minha máquina' e reduzem o tempo de configuração de dias para minutos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Cada desenvolvedor mantém a própria configuração de ambiente. Sem padronização. A configuração leva >4 horas para novos membros da equipe. | • Sem padronização de ambientes<br>• Tempo de configuração >4 horas<br>• Instalação manual de dependências |
| **L1** | Em Desenvolvimento | README com instruções de configuração. Algumas equipes usam Docker para desenvolvimento local. Tempo de configuração de 1-4 horas. | • Guia de configuração no README<br>• Algum uso de Docker<br>• Tempo de configuração de 1-4 horas |
| **L2** | Definido | Docker Compose ou devcontainer para >50% dos projetos. Tempo de configuração <30 minutos. Configurações compartilhadas. | • >50% dos projetos com containers<br>• Tempo de configuração <30 min<br>• Configurações de desenvolvimento compartilhadas |
| **L3** | Gerenciado | Devcontainers padronizados para >80% dos projetos. Ambientes de desenvolvimento baseados em nuvem disponíveis (Codespaces). Tempo de configuração <10 minutos. | • >80% de cobertura com devcontainer<br>• Ambiente de desenvolvimento em nuvem disponível<br>• Tempo de configuração <10 min |
| **L4** | Otimizando | Ambientes de desenvolvimento efêmeros com um clique, com dependências configuradas por IA. Zero configuração manual. Paridade do ambiente com produção garantida. | • Criação de ambiente com um clique<br>• Zero etapas manuais de configuração<br>• Verificação de paridade com produção documentada<br>• Configuração de dependências por IA |

---

### P1-C2-Q3: Em que medida Plataforma de Experiência do Desenvolvedor (self-service IDP) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Self-service catalog coverage`

**Contexto**

- **O que mede (what):** A plataforma interna de desenvolvedores (IDP) oferece paved paths com provisionamento self-service.
- **Por que importa (why):** IDPs reduzem a carga cognitiva e aceleram o onboarding em 50-70%.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem self-service idp implementado. As equipes operam sem esta capacidade. | • Nenhum IDP self-service implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de self-service idp com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | self-service IDP adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | self-service IDP padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | self-service IDP é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C2-Q4: Em que medida Plataforma de Experiência do Desenvolvedor (golden paths and templates) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services from templates`

**Contexto**

- **O que mede (what):** Templates de golden path codificam padrões opinativos para novos serviços.
- **Por que importa (why):** Templates padrão reduzem o tempo até o primeiro commit e impõem baselines de segurança.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem golden paths and templates implementado. As equipes operam sem esta capacidade. | • Nenhum golden path e template implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de golden paths and templates com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | golden paths and templates adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | golden paths and templates padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | golden paths and templates é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C2-Q5: Em que medida Plataforma de Experiência do Desenvolvedor (developer portal) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Portal MAU (monthly active users)`

**Contexto**

- **O que mede (what):** Um portal de desenvolvedores centraliza documentação, APIs e catálogo de serviços.
- **Por que importa (why):** Uma visão única reduz a troca de contexto e melhora a descoberta.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer portal implementado. As equipes operam sem esta capacidade. | • Nenhum portal de desenvolvedores implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de developer portal com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | developer portal adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | developer portal padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | developer portal é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C2-Q6: Em que medida Plataforma de Experiência do Desenvolvedor (paved road policy enforcement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Segurança, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `services on paved road`

**Contexto**

- **O que mede (what):** Políticas de plataforma são codificadas para que as equipes precisem optar explicitamente por não segui-las.
- **Por que importa (why):** Policy-as-code transforma a governança em habilitadora, não em bloqueio.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem paved road policy enforcement implementado. As equipes operam sem esta capacidade. | • Nenhum enforcement de política de paved road implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de paved road policy enforcement com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | paved road policy enforcement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | paved road policy enforcement padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | paved road policy enforcement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C3: Gestão do Conhecimento

**6 questões neste capability.**

### P1-C3-Q1: Quão efetivamente sua organização captura e compartilha conhecimento de desenvolvimento?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Knowledge retrieval success rate %`

**Contexto**

- **O que mede (what):** Mede quão bem o conhecimento de desenvolvimento é capturado, organizado e acessível.
- **Por que importa (why):** A má gestão do conhecimento causa desperdício de 20% do tempo dos desenvolvedores procurando informações ou reinventando soluções.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | O conhecimento vive na cabeça de desenvolvedores individuais. Sem cultura de documentação. Alto risco de bus factor. | • Sem política de documentação<br>• Conhecimento em indivíduos<br>• Alto risco de bus factor |
| **L1** | Em Desenvolvimento | Existe documentação básica para sistemas críticos. Compartilhamento de conhecimento por reuniões ad-hoc e threads no Slack. | • Alguma documentação de sistemas críticos<br>• Compartilhamento de conhecimento ad-hoc<br>• Canal de perguntas e respostas baseado em Slack |
| **L2** | Definido | Documentação estruturada em wiki central. Tech talks regulares ou sessões de compartilhamento de conhecimento. Registros de decisão para mudanças importantes. | • Wiki central com estrutura<br>• Tech talks regulares<br>• Prática de ADR estabelecida |
| **L3** | Gerenciado | Base de conhecimento pesquisável cobrindo >70% dos sistemas. Geração de documentação assistida por IA. Runbooks automatizados para problemas comuns. | • >70% de documentação de sistemas<br>• Geração de documentação assistida por IA<br>• Runbooks automatizados publicados |
| **L4** | Otimizando | Grafo de conhecimento com IA conectando código, documentação, incidentes e decisões. Consultas em linguagem natural retornam respostas contextuais. Atualização do conhecimento monitorada automaticamente. | • Implementação de grafo de conhecimento<br>• Interface de consulta em linguagem natural<br>• Monitoramento automatizado de atualização habilitado<br>• Sistema de respostas contextuais |

---

### P1-C3-Q2: Em que medida Gestão do Conhecimento (semantic code search) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos indexed`

**Contexto**

- **O que mede (what):** Busca semântica em toda a organização em repositórios, documentação e chats.
- **Por que importa (why):** A busca semântica reduz trabalho duplicado ao tornar soluções anteriores descobríveis.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem semantic code search implementado. As equipes operam sem esta capacidade. | • Nenhuma busca semântica de código implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de semantic code search com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | semantic code search adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | semantic code search padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | semantic code search é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C3-Q3: Em que medida Gestão do Conhecimento (RAG-based docs assistant) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `queries per developer/month`

**Contexto**

- **O que mede (what):** Um assistente apoiado por LLM responde perguntas de desenvolvimento a partir da base de conhecimento interna.
- **Por que importa (why):** Assistentes RAG reduzem a carga de interrupções sobre engenheiros seniores.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem rag-based docs assistant implementado. As equipes operam sem esta capacidade. | • Nenhum assistente de documentação baseado em RAG implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de rag-based docs assistant com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | RAG-based docs assistant adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | RAG-based docs assistant padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | RAG-based docs assistant é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C3-Q4: Em que medida Gestão do Conhecimento (runbook and playbook coverage) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% critical services with runbook`

**Contexto**

- **O que mede (what):** Runbooks automatizados capturam conhecimento operacional.
- **Por que importa (why):** Runbooks documentados encurtam o MTTR e viabilizam rotação de on-call.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem runbook and playbook coverage implementado. As equipes operam sem esta capacidade. | • Nenhuma cobertura de runbooks e playbooks implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de runbook and playbook coverage com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | runbook and playbook coverage adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | runbook and playbook coverage padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | runbook and playbook coverage é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C3-Q5: Em que medida Gestão do Conhecimento (ADR (architecture decision records)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with ADRs`

**Contexto**

- **O que mede (what):** Decisões de arquitetura são capturadas como ADRs no repositório.
- **Por que importa (why):** ADRs preservam a memória institucional além das pessoas.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem adr (architecture decision records) implementado. As equipes operam sem esta capacidade. | • Nenhum ADR (registros de decisões de arquitetura) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de adr (architecture decision records) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | ADR (architecture decision records) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | ADR (architecture decision records) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | ADR (architecture decision records) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C3-Q6: Em que medida Gestão do Conhecimento (learning content & curated paths) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `completions per quarter`

**Contexto**

- **O que mede (what):** Trilhas de aprendizagem curadas vinculadas ao papel e à carreira.
- **Por que importa (why):** Aprendizagem estruturada reduz o tempo de ramp-up e melhora a retenção.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem learning content & curated paths implementado. As equipes operam sem esta capacidade. | • Nenhum conteúdo de aprendizado e trilhas curadas implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de learning content & curated paths com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | learning content & curated paths adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | learning content & curated paths padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | learning content & curated paths é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C4: Automação de Revisão de Código

**7 questões neste capability.**

### P1-C4-Q1: Em que medida Automação de Revisão de Código (AI reviewer bot on every PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs AI-reviewed`

**Contexto**

- **O que mede (what):** Um bot publica comentários de revisão gerados por IA em todo PR.
- **Por que importa (why):** Revisores de IA detectam problemas antes que humanos olhem o código.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai reviewer bot on every pr implementado. As equipes operam sem esta capacidade. | • Nenhum bot revisor de IA em todo PR implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de ai reviewer bot on every pr com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | AI reviewer bot on every PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | AI reviewer bot on every PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | AI reviewer bot on every PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q2: Em que medida Automação de Revisão de Código (static linting and style auto-fix) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `lint violations per kLOC`

**Contexto**

- **O que mede (what):** Linters e formatadores rodam automaticamente em todo commit.
- **Por que importa (why):** Estilo automatizado remove discussões improdutivas das reviews.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem static linting and style auto-fix implementado. As equipes operam sem esta capacidade. | • Nenhum linting estático e correção automática de estilo implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de static linting and style auto-fix com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | static linting and style auto-fix adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | static linting and style auto-fix padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | static linting and style auto-fix é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q3: Em que medida Automação de Revisão de Código (automated security review) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical findings per PR`

**Contexto**

- **O que mede (what):** SAST comenta inline no diff do PR.
- **Por que importa (why):** Achados inline são corrigidos 10x mais rápido do que itens de backlog.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated security review implementado. As equipes operam sem esta capacidade. | • Nenhuma revisão de segurança automatizada implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de automated security review com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | automated security review adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | automated security review padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | automated security review é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q4: Em que medida Automação de Revisão de Código (required-reviewer rules) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs meeting review rule`

**Contexto**

- **O que mede (what):** CODEOWNERS impõe revisão por especialista de domínio por caminho.
- **Por que importa (why):** Revisor certo + código certo = melhores detecções.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem required-reviewer rules implementado. As equipes operam sem esta capacidade. | • Nenhuma regra de revisor obrigatório implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de required-reviewer rules com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | required-reviewer rules adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | required-reviewer rules padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | required-reviewer rules é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q5: Em que medida Automação de Revisão de Código (review SLA tracking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median PR cycle time`

**Contexto**

- **O que mede (what):** O tempo de ciclo de PR é medido e gerenciado por metas.
- **Por que importa (why):** Ciclos rápidos de revisão mantêm desenvolvedores em flow.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem review sla tracking implementado. As equipes operam sem esta capacidade. | • Nenhum rastreamento de SLA de revisão implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de review sla tracking com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | review SLA tracking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | review SLA tracking padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | review SLA tracking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q6: Em que medida Automação de Revisão de Código (change size enforcement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median PR size (LoC)`

**Contexto**

- **O que mede (what):** Hooks de pre-commit incentivam PRs pequenos.
- **Por que importa (why):** PRs pequenos recebem reviews melhores e fazem merge mais rápido.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem change size enforcement implementado. As equipes operam sem esta capacidade. | • Nenhum enforcement de tamanho de mudança implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de change size enforcement com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | change size enforcement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | change size enforcement padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | change size enforcement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C4-Q7: Em que medida Automação de Revisão de Código (reviewer load balancing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `review load balance index`

**Contexto**

- **O que mede (what):** A atribuição de revisores equilibra a carga pela equipe.
- **Por que importa (why):** Carga de revisão equilibrada previne burnout dos principais revisores.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem reviewer load balancing implementado. As equipes operam sem esta capacidade. | • Nenhum balanceamento de carga de revisores implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de reviewer load balancing com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | reviewer load balancing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | reviewer load balancing padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | reviewer load balancing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C5: Onboarding e Treinamento de Desenvolvedores

**7 questões neste capability.**

### P1-C5-Q1: Em que medida Onboarding e Treinamento de Desenvolvedores (codespaces/dev containers for instant env) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time-to-first-commit (hours)`

**Contexto**

- **O que mede (what):** Ambientes de desenvolvimento na nuvem ficam prontos em minutos.
- **Por que importa (why):** Configuração rápida de ambiente desbloqueia novos contratados no primeiro dia.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem codespaces/dev containers for instant env implementado. As equipes operam sem esta capacidade. | • Nenhum codespaces/dev containers para ambiente instantâneo implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de codespaces/dev containers for instant env com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | codespaces/dev containers for instant env adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | codespaces/dev containers for instant env padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | codespaces/dev containers for instant env é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q2: Em que medida Onboarding e Treinamento de Desenvolvedores (structured onboarding playbook) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% new hires completing onboarding`

**Contexto**

- **O que mede (what):** Um plano de onboarding documentado de 30/60/90 dias por função.
- **Por que importa (why):** Onboarding estruturado reduz o tempo de ramp-up em 30-50%.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem structured onboarding playbook implementado. As equipes operam sem esta capacidade. | • Nenhum playbook estruturado de onboarding implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de structured onboarding playbook com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | structured onboarding playbook adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | structured onboarding playbook padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | structured onboarding playbook é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q3: Em que medida Onboarding e Treinamento de Desenvolvedores (mentor pairing program) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `mentor:mentee ratio`

**Contexto**

- **O que mede (what):** Todo novo contratado recebe um mentor sênior por 90 dias.
- **Por que importa (why):** Mentoria encurta o ramp-up e aumenta a retenção.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem mentor pairing program implementado. As equipes operam sem esta capacidade. | • Nenhum programa de mentoria em pares implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de mentor pairing program com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | mentor pairing program adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | mentor pairing program padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | mentor pairing program é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q4: Em que medida Onboarding e Treinamento de Desenvolvedores (hands-on curriculum & kata) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `katas completed per hire`

**Contexto**

- **O que mede (what):** Katas de codificação específicos por função produzem habilidade demonstrável.
- **Por que importa (why):** Prática deliberada desenvolve habilidade mais rápido do que leitura.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem hands-on curriculum & kata implementado. As equipes operam sem esta capacidade. | • Nenhum currículo prático e kata implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de hands-on curriculum & kata com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | hands-on curriculum & kata adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | hands-on curriculum & kata padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | hands-on curriculum & kata é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q5: Em que medida Onboarding e Treinamento de Desenvolvedores (shadow on-call rotation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `new hires who shadowed on-call`

**Contexto**

- **O que mede (what):** Novos contratados acompanham on-call para aprender o contexto operacional.
- **Por que importa (why):** Contexto operacional é a forma mais rápida de entender o sistema.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem shadow on-call rotation implementado. As equipes operam sem esta capacidade. | • Nenhuma rotação shadow de on-call implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de shadow on-call rotation com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | shadow on-call rotation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | shadow on-call rotation padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | shadow on-call rotation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q6: Em que medida Onboarding e Treinamento de Desenvolvedores (onboarding feedback loop) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `NPS from new hires`

**Contexto**

- **O que mede (what):** Novos contratados avaliam o onboarding; os resultados orientam melhorias.
- **Por que importa (why):** Loops de feedback transformam o onboarding em um produto em melhoria contínua.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem onboarding feedback loop implementado. As equipes operam sem esta capacidade. | • Nenhum loop de feedback de onboarding implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de onboarding feedback loop com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | onboarding feedback loop adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | onboarding feedback loop padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | onboarding feedback loop é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C5-Q7: Em que medida Onboarding e Treinamento de Desenvolvedores (ramp-time measurement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median ramp-time to first deploy`

**Contexto**

- **O que mede (what):** O tempo até a primeira implantação é medido e melhorado para novos contratados.
- **Por que importa (why):** Medir o ramp-up transforma melhorias de onboarding em ROI.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ramp-time measurement implementado. As equipes operam sem esta capacidade. | • Nenhuma medição de tempo de ramp-up implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de ramp-time measurement com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | ramp-time measurement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | ramp-time measurement padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | ramp-time measurement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C6: Inner Source e Colaboração

**6 questões neste capability.**

### P1-C6-Q1: Em que medida Inner Source e Colaboração (internal repos with open contribution) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos open to all devs`

**Contexto**

- **O que mede (what):** Repositórios dentro da organização aceitam PRs de outras equipes.
- **Por que importa (why):** Inner source quebra silos e aumenta o reúso.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem internal repos with open contribution implementado. As equipes operam sem esta capacidade. | • Nenhum repositório interno com contribuição aberta implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de internal repos with open contribution com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | internal repos with open contribution adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | internal repos with open contribution padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | internal repos with open contribution é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C6-Q2: Em que medida Inner Source e Colaboração (CONTRIBUTING.md standards) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with CONTRIBUTING`

**Contexto**

- **O que mede (what):** Todo repositório documenta como contribuir e revisar.
- **Por que importa (why):** Normas claras de contribuição reduzem o atrito no trabalho entre equipes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem contributing.md standards implementado. As equipes operam sem esta capacidade. | • Nenhum padrão CONTRIBUTING.md implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de contributing.md standards com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | CONTRIBUTING.md standards adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | CONTRIBUTING.md standards padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | CONTRIBUTING.md standards é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C6-Q3: Em que medida Inner Source e Colaboração (inner-source discovery portal) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `cross-team PRs per month`

**Contexto**

- **O que mede (what):** Um portal indexa projetos inner source em busca de contribuições.
- **Por que importa (why):** Descoberta impulsiona participação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem inner-source discovery portal implementado. As equipes operam sem esta capacidade. | • Nenhum portal de descoberta de inner source implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de inner-source discovery portal com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | inner-source discovery portal adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | inner-source discovery portal padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | inner-source discovery portal é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C6-Q4: Em que medida Inner Source e Colaboração (good-first-issue labeling) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `GFI issues closed per month`

**Contexto**

- **O que mede (what):** Issues iniciais ajudam novatos a contribuir com confiança.
- **Por que importa (why):** Rotulagem reduz a barreira para contribuidores de primeira viagem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem good-first-issue labeling implementado. As equipes operam sem esta capacidade. | • Nenhuma marcação de good-first-issue implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de good-first-issue labeling com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | good-first-issue labeling adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | good-first-issue labeling padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | good-first-issue labeling é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C6-Q5: Em que medida Inner Source e Colaboração (cross-team design reviews) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `reviews per quarter`

**Contexto**

- **O que mede (what):** Documentos de design são revisados por múltiplas equipes.
- **Por que importa (why):** Revisão entre equipes detecta suposições e compartilha padrões.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cross-team design reviews implementado. As equipes operam sem esta capacidade. | • Nenhuma revisão de design entre equipes implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de cross-team design reviews com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | cross-team design reviews adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | cross-team design reviews padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | cross-team design reviews é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C6-Q6: Em que medida Inner Source e Colaboração (community of practice) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `CoP active members`

**Contexto**

- **O que mede (what):** Guildas e CoPs constroem expertise horizontal.
- **Por que importa (why):** CoPs aceleram o aprendizado e reduzem riscos de lacunas de contratação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem community of practice implementado. As equipes operam sem esta capacidade. | • Nenhuma comunidade de prática implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de community of practice com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | community of practice adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | community of practice padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | community of practice é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C7: Automação de Documentação

**5 questões neste capability.**

### P1-C7-Q1: Em que medida Automação de Documentação (docs-as-code in Git) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with docs in repo`

**Contexto**

- **O que mede (what):** A documentação vive com o código e é revisada em PRs.
- **Por que importa (why):** Docs-as-code evita que a documentação se deteriore longe do código-fonte.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem docs-as-code in git implementado. As equipes operam sem esta capacidade. | • Nenhum docs-as-code em Git implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de docs-as-code in git com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | docs-as-code in Git adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | docs-as-code in Git padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | docs-as-code in Git é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C7-Q2: Em que medida Automação de Documentação (auto-generated API reference) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs with generated docs`

**Contexto**

- **O que mede (what):** A referência de API é gerada a partir de OpenAPI ou do código-fonte.
- **Por que importa (why):** Documentação gerada está sempre atualizada.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem auto-generated api reference implementado. As equipes operam sem esta capacidade. | • Nenhuma referência de API gerada automaticamente implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de auto-generated api reference com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | auto-generated API reference adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | auto-generated API reference padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | auto-generated API reference é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C7-Q3: Em que medida Automação de Documentação (AI-assisted doc drafting) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs with AI doc suggestions`

**Contexto**

- **O que mede (what):** IA sugere atualizações de README e documentação a partir de diffs de código.
- **Por que importa (why):** Rascunhos de IA elevam o patamar mínimo de qualidade da documentação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai-assisted doc drafting implementado. As equipes operam sem esta capacidade. | • Nenhum rascunho de documentação assistido por IA implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de ai-assisted doc drafting com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | AI-assisted doc drafting adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | AI-assisted doc drafting padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | AI-assisted doc drafting é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C7-Q4: Em que medida Automação de Documentação (doc quality linting) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `broken-link count`

**Contexto**

- **O que mede (what):** Verificações de links e linters de estilo rodam no CI.
- **Por que importa (why):** Verificações automatizadas mantêm a documentação confiável.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem doc quality linting implementado. As equipes operam sem esta capacidade. | • Nenhum linting de qualidade de documentação implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de doc quality linting com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | doc quality linting adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | doc quality linting padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | doc quality linting é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C7-Q5: Em que medida Automação de Documentação (docs analytics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `top unanswered queries`

**Contexto**

- **O que mede (what):** Analytics de busca revelam o que usuários não conseguem encontrar.
- **Por que importa (why):** Analytics transformam a documentação em um produto orientado por dados.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem docs analytics implementado. As equipes operam sem esta capacidade. | • Nenhuma análise de documentação implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de docs analytics com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | docs analytics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | docs analytics padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | docs analytics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C8: Medição de Produtividade do Desenvolvedor

**6 questões neste capability.**

### P1-C8-Q1: Em que medida Medição de Produtividade do Desenvolvedor (DORA four key metrics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deploys/day, lead time, CFR, MTTR`

**Contexto**

- **O que mede (what):** Frequência de implantação, lead time, taxa de falha de mudança e MTTR são acompanhados.
- **Por que importa (why):** Métricas DORA se correlacionam com resultados de negócio.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dora four key metrics implementado. As equipes operam sem esta capacidade. | • Nenhuma das quatro métricas-chave DORA implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de dora four key metrics com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | DORA four key metrics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | DORA four key metrics padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | DORA four key metrics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C8-Q2: Em que medida Medição de Produtividade do Desenvolvedor (developer experience surveys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `DX survey NPS`

**Contexto**

- **O que mede (what):** Pesquisas trimestrais medem a satisfação dos desenvolvedores.
- **Por que importa (why):** Pesquisas de DX revelam atritos que as métricas não capturam.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer experience surveys implementado. As equipes operam sem esta capacidade. | • Nenhuma pesquisa de experiência de desenvolvedores implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de developer experience surveys com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | developer experience surveys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | developer experience surveys padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | developer experience surveys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C8-Q3: Em que medida Medição de Produtividade do Desenvolvedor (build/test feedback loop time) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `p95 CI duration`

**Contexto**

- **O que mede (what):** CI fornece sinal em até 10 minutos para PRs típicos.
- **Por que importa (why):** Feedback rápido mantém desenvolvedores em flow.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build/test feedback loop time implementado. As equipes operam sem esta capacidade. | • Nenhum tempo de loop de feedback de build/test implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de build/test feedback loop time com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | build/test feedback loop time adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | build/test feedback loop time padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | build/test feedback loop time é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C8-Q4: Em que medida Medição de Produtividade do Desenvolvedor (SPACE framework adoption) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `SPACE dimensions tracked`

**Contexto**

- **O que mede (what):** Equipes acompanham Satisfação, Performance, Atividade, Comunicação e Eficiência.
- **Por que importa (why):** SPACE equilibra sinais quantitativos e qualitativos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem space framework adoption implementado. As equipes operam sem esta capacidade. | • Nenhuma adoção do framework SPACE implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de space framework adoption com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SPACE framework adoption adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SPACE framework adoption padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SPACE framework adoption é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C8-Q5: Em que medida Medição de Produtividade do Desenvolvedor (flow vs friction dashboards) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams viewing dashboard monthly`

**Contexto**

- **O que mede (what):** Líderes e equipes veem dados de produtividade lado a lado.
- **Por que importa (why):** Dados compartilhados alinham melhorias entre equipes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem flow vs friction dashboards implementado. As equipes operam sem esta capacidade. | • Nenhum dashboard de fluxo versus atrito implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de flow vs friction dashboards com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | flow vs friction dashboards adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | flow vs friction dashboards padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | flow vs friction dashboards é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C8-Q6: Em que medida Medição de Produtividade do Desenvolvedor (quarterly productivity OKRs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams hitting DX OKRs`

**Contexto**

- **O que mede (what):** Melhorias de DX são acompanhadas como OKRs.
- **Por que importa (why):** OKRs tornam produtividade um investimento de primeira classe.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem quarterly productivity okrs implementado. As equipes operam sem esta capacidade. | • Nenhum OKR trimestral de produtividade implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de quarterly productivity okrs com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | quarterly productivity OKRs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | quarterly productivity OKRs padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | quarterly productivity OKRs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P1-C9: Automação de Ambientes e Espaços de Trabalho

**5 questões neste capability.**

### P1-C9-Q1: Em que medida Automação de Ambientes e Espaços de Trabalho (reproducible local envs (devcontainers)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with devcontainer`

**Contexto**

- **O que mede (what):** Todo repositório entrega um devcontainer ou Nix shell.
- **Por que importa (why):** Ambientes reproduzíveis eliminam falhas de 'funciona na minha máquina'.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem reproducible local envs (devcontainers) implementado. As equipes operam sem esta capacidade. | • Nenhum ambiente local reproduzível (devcontainers) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de reproducible local envs (devcontainers) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | reproducible local envs (devcontainers) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | reproducible local envs (devcontainers) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | reproducible local envs (devcontainers) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C9-Q2: Em que medida Automação de Ambientes e Espaços de Trabalho (cloud workspaces (Codespaces/Gitpod)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% devs using cloud workspace`

**Contexto**

- **O que mede (what):** Workspaces na nuvem são o ambiente de desenvolvimento padrão.
- **Por que importa (why):** Workspaces na nuvem tornam a configuração de ambiente instantânea e consistente.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cloud workspaces (codespaces/gitpod) implementado. As equipes operam sem esta capacidade. | • Nenhum workspace em nuvem (Codespaces/Gitpod) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de cloud workspaces (codespaces/gitpod) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | cloud workspaces (Codespaces/Gitpod) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | cloud workspaces (Codespaces/Gitpod) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | cloud workspaces (Codespaces/Gitpod) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C9-Q3: Em que medida Automação de Ambientes e Espaços de Trabalho (tool and SDK version pinning) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `tools pinned per repo`

**Contexto**

- **O que mede (what):** Versões de linguagens e ferramentas são fixadas e lockfiles são commitados.
- **Por que importa (why):** Versões fixadas mantêm builds reproduzíveis entre máquinas.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem tool and sdk version pinning implementado. As equipes operam sem esta capacidade. | • Nenhum pinning de versões de ferramentas e SDKs implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de tool and sdk version pinning com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | tool and SDK version pinning adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | tool and SDK version pinning padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | tool and SDK version pinning é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C9-Q4: Em que medida Automação de Ambientes e Espaços de Trabalho (on-demand test data) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time to get fresh test data`

**Contexto**

- **O que mede (what):** Desenvolvedores podem redefinir ou provisionar dados de teste realistas sob demanda.
- **Por que importa (why):** Dados frescos desbloqueiam testes e depuração.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem on-demand test data implementado. As equipes operam sem esta capacidade. | • Nenhum dado de teste sob demanda implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de on-demand test data com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | on-demand test data adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | on-demand test data padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | on-demand test data é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P1-C9-Q5: Em que medida Automação de Ambientes e Espaços de Trabalho (workspace telemetry & health) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workspaces healthy`

**Contexto**

- **O que mede (what):** Telemetria de workspace revela falhas de configuração e travamentos de ferramentas.
- **Por que importa (why):** Telemetria permite que equipes de plataforma corrijam atritos proativamente.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem workspace telemetry & health implementado. As equipes operam sem esta capacidade. | • Nenhuma telemetria e saúde de workspace implantadas<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de workspace telemetry & health com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | workspace telemetry & health adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | workspace telemetry & health padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | workspace telemetry & health é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P1** é a média das 9 capacidades.
- O resultado é exibido em escala 0-4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0 a L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
