# Assessment de Maturidade IA: Pilar P2, Ciclo de Vida DevOps

🌐 [English](P2-ciclo-de-vida-devops.md) · Português (Brasil) · [Español](P2-ciclo-de-vida-devops.es.md)

> Mede a maturidade de pipelines, infraestrutura como código, observabilidade, DevSecOps, releases, testes, incidentes e segurança da cadeia de suprimentos.

## Visão geral

- **Pilar:** `P2`: Ciclo de Vida DevOps
- **Capacidades (capabilities):** 10
- **Questões totais:** 59
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

## Capacidades do pilar P2

- **P2-C1**: Inteligência de Pipeline CI/CD (6 questões)
- **P2-C2**: Infraestrutura como Código (6 questões)
- **P2-C3**: Observabilidade e Monitoramento (6 questões)
- **P2-C4**: Integração de Segurança (DevSecOps) (6 questões)
- **P2-C5**: Estratégias de Release e Implantação (6 questões)
- **P2-C6**: Automação de Testes (7 questões)
- **P2-C7**: Gestão de Incidentes e SRE (7 questões)
- **P2-C8**: Gestão de Artefatos e Pacotes (5 questões)
- **P2-C9**: Gestão de Mudanças e GitOps (5 questões)
- **P2-C10**: Segurança de Dependências e Cadeia de Suprimentos (5 questões)

---

## P2-C1: Inteligência de Pipeline CI/CD

**6 questões neste capability.**

### P2-C1-Q1: Quão maduro é seu pipeline CI/CD em termos de automação e integração de IA?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `Deployment frequency per week`

**Contexto**

- **O que mede (what):** Mede o nível de automação e inteligência dos pipelines CI/CD.
- **Por que importa (why):** Pipelines CI/CD maduros permitem que equipes implantem 200x mais frequentemente com taxa de falha de mudança 3x menor (pesquisa DORA).

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Builds e implantações manuais. Sem pipeline de CI/CD. Implantações acontecem semanalmente ou com menor frequência. | • Sem pipeline de CI/CD<br>• Processo de build manual<br>• Implantações semanais ou menos frequentes |
| **L1** | Em Desenvolvimento | Pipeline básico de CI com builds automatizados e testes unitários. Processo de implantação manual. Frequência de implantação: semanal. | • Pipeline de CI configurado<br>• Testes unitários automatizados<br>• Implantações manuais semanais |
| **L2** | Definido | Pipeline completo de CI/CD com testes automatizados, implantação em staging e promoção manual para produção. Frequência de implantação: diária. | • Implantação automatizada em staging<br>• Promoção manual para produção<br>• Cadência diária de implantações em produção |
| **L3** | Gerenciado | CI/CD inteligente: suítes de teste com escala automática, seleção inteligente de testes (executa apenas testes afetados), implantações canary. Várias implantações por dia. | • Seleção inteligente de testes<br>• Configuração de implantação canary<br>• Várias implantações diárias<br>• Análise de impacto de testes |
| **L4** | Otimizando | Pipeline otimizado por IA: falhas de build preditivas, remediação automática de testes flaky, análise canary orientada por ML, implantações self-healing. | • Modelo preditivo de falhas<br>• Scripts automatizados de remediação implantados<br>• Análise canary por ML<br>• Documentação de implantações self-healing |

---

### P2-C1-Q2: Em que medida Inteligência de Pipeline CI/CD (pipeline-as-code everywhere) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% pipelines as code`

**Contexto**

- **O que mede (what):** Todos os pipelines vivem junto ao código como YAML/HCL versionado.
- **Por que importa (why):** Pipeline-as-code é auditável, revisável e reproduzível.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem pipeline-as-code everywhere implementado. As equipes operam sem esta capacidade. | • Nenhum pipeline-as-code em todos os lugares implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de pipeline-as-code everywhere com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | pipeline-as-code everywhere adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | pipeline-as-code everywhere padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | pipeline-as-code everywhere é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C1-Q3: Em que medida Inteligência de Pipeline CI/CD (build caching and artifact reuse) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% cache hit ratio`

**Contexto**

- **O que mede (what):** Caches remotos de build e artefatos endereçados por conteúdo reduzem o tempo de build.
- **Por que importa (why):** Caching reduz o tempo de CI em 40-70% e diminui o gasto em nuvem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build caching and artifact reuse implementado. As equipes operam sem esta capacidade. | • Nenhum cache de build e reúso de artefatos implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de build caching and artifact reuse com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | build caching and artifact reuse adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | build caching and artifact reuse padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | build caching and artifact reuse é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C1-Q4: Em que medida Inteligência de Pipeline CI/CD (trunk-based development) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `branches >7 days old`

**Contexto**

- **O que mede (what):** Branches de curta duração são mescladas ao trunk várias vezes por dia.
- **Por que importa (why):** Desenvolvimento trunk-based reduz o inferno de merges e viabiliza entrega contínua.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem trunk-based development implementado. As equipes operam sem esta capacidade. | • Nenhum desenvolvimento trunk-based implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de trunk-based development com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | trunk-based development adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | trunk-based development padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | trunk-based development é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C1-Q5: Em que medida Inteligência de Pipeline CI/CD (deployment frequency) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deploys per day`

**Contexto**

- **O que mede (what):** Equipes DORA de elite implantam muitas vezes por dia em produção.
- **Por que importa (why):** Alta frequência de deploy se correlaciona com baixa taxa de falha de mudança.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem deployment frequency implementado. As equipes operam sem esta capacidade. | • Nenhuma frequência de implantação implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de deployment frequency com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | deployment frequency adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | deployment frequency padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | deployment frequency é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C1-Q6: Em que medida Inteligência de Pipeline CI/CD (feature flags for progressive delivery) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flags used per release`

**Contexto**

- **O que mede (what):** Feature flags desacoplam implantação de release.
- **Por que importa (why):** Flags permitem dark launches, rollouts canary e rollback rápido.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem feature flags for progressive delivery implementado. As equipes operam sem esta capacidade. | • Nenhuma feature flag para entrega progressiva implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de feature flags for progressive delivery com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | feature flags for progressive delivery adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | feature flags for progressive delivery padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | feature flags for progressive delivery é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C2: Infraestrutura como Código

**6 questões neste capability.**

### P2-C2-Q1: Qual porcentagem de sua infraestrutura é gerenciada por código?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, qa-test
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% infrastructure as code`

**Contexto**

- **O que mede (what):** Mede em que medida o provisionamento e a gestão de infraestrutura são codificados e controlados por versão.
- **Por que importa (why):** IaC reduz erros de provisionamento em 90% e permite que mudanças de infraestrutura sejam revisadas, testadas e auditadas como código de aplicação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Toda a infraestrutura é provisionada manualmente via console de nuvem ou comandos CLI. Sem controle de versão para infraestrutura. | • Apenas provisionamento manual<br>• Sem arquivos IaC nos repositórios<br>• Fluxo de gerenciamento baseado em console |
| **L1** | Em Desenvolvimento | Alguma infraestrutura definida em código (<30%). Mistura de provisionamento manual e automatizado. Scripts sem controle de versão consistente. | • <30% de cobertura de IaC<br>• Processos mistos manuais e automatizados<br>• Controle de versão inconsistente |
| **L2** | Definido | 50-75% da infraestrutura definida em código. Módulos IaC para padrões comuns. Revisão baseada em PR para mudanças de infraestrutura. | • 50-75% de cobertura de IaC<br>• Módulos IaC reutilizáveis<br>• Revisão de infraestrutura baseada em PR |
| **L3** | Gerenciado | >90% da infraestrutura como código. Detecção de drift habilitada. Enforcement de policy-as-code. Provisionamento self-service via templates. | • >90% de cobertura de IaC<br>• Relatórios de detecção de drift<br>• Regras de policy-as-code aplicadas<br>• Templates self-service publicados |
| **L4** | Otimizando | 100% de IaC com recomendações de infraestrutura geradas por IA. Remediação automática de drift. Sugestões de otimização de custos. Escalabilidade preditiva. | • 100% de cobertura de IaC<br>• Recomendações de infraestrutura por IA<br>• Remediação automatizada de drift habilitada<br>• Configuração de escalabilidade preditiva |

---

### P2-C2-Q2: Em que medida Infraestrutura como Código (Terraform/Bicep-based IaC) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% infra as code`

**Contexto**

- **O que mede (what):** Toda infraestrutura de longa duração é declarada como código.
- **Por que importa (why):** IaC elimina servidores snowflake e viabiliza ambientes reproduzíveis.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem terraform/bicep-based iac implementado. As equipes operam sem esta capacidade. | • Nenhuma IaC baseada em Terraform/Bicep implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de terraform/bicep-based iac com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | Terraform/Bicep-based IaC adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | Terraform/Bicep-based IaC padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | Terraform/Bicep-based IaC é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C2-Q3: Em que medida Infraestrutura como Código (module and pattern library) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% resources via modules`

**Contexto**

- **O que mede (what):** Uma biblioteca compartilhada de módulos codifica segurança e rede opinativas.
- **Por que importa (why):** Módulos impõem padrões e reduzem a carga cognitiva por equipe.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem module and pattern library implementado. As equipes operam sem esta capacidade. | • Nenhuma biblioteca de módulos e padrões implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de module and pattern library com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | module and pattern library adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | module and pattern library padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | module and pattern library é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C2-Q4: Em que medida Infraestrutura como Código (GitOps for config drift) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% envs drift-detected`

**Contexto**

- **O que mede (what):** Controladores GitOps reconciliam o estado de cluster e nuvem com o Git.
- **Por que importa (why):** GitOps elimina drift e torna o Git a fonte única da verdade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem gitops for config drift implementado. As equipes operam sem esta capacidade. | • Nenhum GitOps para drift de configuração implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de gitops for config drift com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | GitOps for config drift adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | GitOps for config drift padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | GitOps for config drift é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C2-Q5: Em que medida Infraestrutura como Código (policy-as-code (OPA/Conftest)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `policies enforced in PR`

**Contexto**

- **O que mede (what):** Políticas são avaliadas em mudanças de IaC antes do merge.
- **Por que importa (why):** Policy-as-code desloca a governança para a esquerda e escala a revisão de segurança.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem policy-as-code (opa/conftest) implementado. As equipes operam sem esta capacidade. | • Nenhum policy-as-code (OPA/Conftest) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de policy-as-code (opa/conftest) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | policy-as-code (OPA/Conftest) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | policy-as-code (OPA/Conftest) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | policy-as-code (OPA/Conftest) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C2-Q6: Em que medida Infraestrutura como Código (ephemeral environment per PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `PR envs spun up`

**Contexto**

- **O que mede (what):** Todo PR recebe um ambiente efêmero para testes de integração.
- **Por que importa (why):** Ambientes efêmeros encontram bugs mais cedo e aceleram a review.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ephemeral environment per pr implementado. As equipes operam sem esta capacidade. | • Nenhum ambiente efêmero por PR implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de ephemeral environment per pr com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | ephemeral environment per PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | ephemeral environment per PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | ephemeral environment per PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C3: Observabilidade e Monitoramento

**6 questões neste capability.**

### P2-C3-Q1: Quão abrangente é sua stack de observabilidade (logs, métricas, traces)?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `MTTR in minutes`

**Contexto**

- **O que mede (what):** Mede a maturidade da stack de observabilidade, incluindo logging, métricas e tracing distribuído.
- **Por que importa (why):** Observabilidade abrangente reduz MTTR de horas para minutos e permite detecção proativa de problemas.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Logging mínimo. Sem monitoramento centralizado. Problemas descobertos por usuários que os reportam. | • Sem logging centralizado<br>• Sem dashboards de monitoramento<br>• Apenas problemas reportados por usuários |
| **L1** | Em Desenvolvimento | Logging centralizado (ELK/CloudWatch). Monitoramento básico de disponibilidade. MTTR >60 minutos. | • Plataforma de logs centralizada<br>• Verificações básicas de disponibilidade<br>• MTTR >60 minutos |
| **L2** | Definido | Logging estruturado, métricas de aplicação (Prometheus/Datadog), alertas básicos. MTTR 30-60 minutos. | • Logging estruturado em JSON<br>• Dashboard de métricas da aplicação<br>• MTTR 30-60 minutos |
| **L3** | Gerenciado | Observabilidade completa: rastreamento distribuído, logs-métricas-traces correlacionados, alertas baseados em SLO. MTTR <15 minutos. | • Rastreamento distribuído habilitado<br>• Stack de observabilidade correlacionada implantada<br>• Alertas baseados em SLO configurados<br>• MTTR <15 minutos |
| **L4** | Otimizando | Observabilidade com IA: detecção de anomalias, alertas preditivos, correlação automática de incidentes, remediação sugerida. MTTR <5 minutos. | • Detecção de anomalias por IA<br>• Alertas preditivos habilitados<br>• Correlação automatizada de incidentes habilitada<br>• MTTR <5 minutos |

---

### P2-C3-Q2: Em que medida Observabilidade e Monitoramento (structured logging w/ correlation IDs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services emitting structured logs`

**Contexto**

- **O que mede (what):** Todos os logs seguem um schema e carregam IDs de trace/correlação.
- **Por que importa (why):** Logs estruturados são pesquisáveis, agregáveis e legíveis por máquina.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem structured logging w/ correlation ids implementado. As equipes operam sem esta capacidade. | • Nenhum logging estruturado com IDs de correlação implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de structured logging w/ correlation ids com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | structured logging w/ correlation IDs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | structured logging w/ correlation IDs padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | structured logging w/ correlation IDs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C3-Q3: Em que medida Observabilidade e Monitoramento (distributed tracing (OpenTelemetry)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services instrumented`

**Contexto**

- **O que mede (what):** SDKs OTEL emitem traces através das fronteiras de serviços.
- **Por que importa (why):** Tracing distribuído revela contribuidores de latência entre microserviços.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem distributed tracing (opentelemetry) implementado. As equipes operam sem esta capacidade. | • Nenhum rastreamento distribuído (OpenTelemetry) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de distributed tracing (opentelemetry) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | distributed tracing (OpenTelemetry) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | distributed tracing (OpenTelemetry) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | distributed tracing (OpenTelemetry) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C3-Q4: Em que medida Observabilidade e Monitoramento (SLOs and error budgets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with SLOs`

**Contexto**

- **O que mede (what):** Objetivos de nível de serviço com error budgets orientam decisões de confiabilidade.
- **Por que importa (why):** SLOs alinham prioridades de engenharia com a experiência do usuário.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem slos and error budgets implementado. As equipes operam sem esta capacidade. | • Nenhum SLO e orçamento de erro implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de slos and error budgets com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SLOs and error budgets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SLOs and error budgets padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SLOs and error budgets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C3-Q5: Em que medida Observabilidade e Monitoramento (synthetic monitoring) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `journeys monitored`

**Contexto**

- **O que mede (what):** Probes sintéticas exercitam jornadas críticas de usuário continuamente.
- **Por que importa (why):** Sintéticos detectam regressões antes dos usuários.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem synthetic monitoring implementado. As equipes operam sem esta capacidade. | • Nenhum monitoramento sintético implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de synthetic monitoring com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | synthetic monitoring adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | synthetic monitoring padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | synthetic monitoring é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C3-Q6: Em que medida Observabilidade e Monitoramento (anomaly detection with ML) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `alerts auto-triaged`

**Contexto**

- **O que mede (what):** Modelos de ML detectam anomalias e suprimem ruído.
- **Por que importa (why):** Detecção baseada em ML reduz fadiga de alertas e acelera a resposta.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem anomaly detection with ml implementado. As equipes operam sem esta capacidade. | • Nenhuma detecção de anomalias com ML implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de anomaly detection with ml com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | anomaly detection with ML adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | anomaly detection with ML padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | anomaly detection with ML é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C4: Integração de Segurança (DevSecOps)

**6 questões neste capability.**

### P2-C4-Q1: Quão integrada está a segurança no seu pipeline de desenvolvimento e implantação?

**Metadados**

- **Público-alvo:** Segurança, devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% vulnerabilities caught pre-prod`

**Contexto**

- **O que mede (what):** Mede a integração de práticas de segurança no ciclo de vida de desenvolvimento (segurança shift-left).
- **Por que importa (why):** Corrigir vulnerabilidades em produção custa 30x mais do que detectá-las no desenvolvimento. DevSecOps reduz incidentes de segurança em 50%.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Segurança revisada apenas antes do release. Sem varredura automatizada. Vulnerabilidades encontradas em produção. | • Sem varredura de segurança automatizada<br>• Revisões apenas antes do release<br>• Incidentes de vulnerabilidade em produção |
| **L1** | Em Desenvolvimento | Varredura básica de dependências em CI (Dependabot/Snyk). Revisão manual de segurança para recursos críticos. | • Varredura de dependências configurada<br>• Revisões manuais de segurança<br>• Sem varredura SAST ou DAST |
| **L2** | Definido | SAST e varredura de dependências no pipeline de CI. Requisitos de segurança na definição de pronto. >50% das vulnerabilidades capturadas antes da produção. | • SAST no pipeline de CI<br>• Segurança na DoD<br>• Taxa de captura pré-produção >50% |
| **L3** | Gerenciado | DevSecOps completo: SAST, DAST, SCA, varredura de containers, detecção de segredos. Gates de segurança bloqueiam a implantação. Taxa de captura pré-produção >80%. | • SAST, DAST, SCA e varredura de containers<br>• Detecção de segredos habilitada<br>• Taxa de captura pré-produção >80% |
| **L4** | Otimizando | Segurança com IA: modelagem de ameaças automatizada, detecção preditiva de vulnerabilidades, patches automáticos de CVEs conhecidas, proteção em runtime. Taxa de captura pré-produção >95%. | • Modelagem de ameaças automatizada<br>• Detecção preditiva de vulnerabilidades<br>• Pipeline automatizado de patches habilitado<br>• Taxa de captura pré-produção >95% |

---

### P2-C4-Q2: Em que medida Integração de Segurança (DevSecOps) (SAST in every pipeline) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with SAST`

**Contexto**

- **O que mede (what):** Análise estática varre todo PR em busca de vulnerabilidades.
- **Por que importa (why):** SAST encontra bugs de forma barata no momento da autoria.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sast in every pipeline implementado. As equipes operam sem esta capacidade. | • Nenhum SAST em todos os pipelines implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de sast in every pipeline com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SAST in every pipeline adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SAST in every pipeline padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SAST in every pipeline é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C4-Q3: Em que medida Integração de Segurança (DevSecOps) (SCA and dependency review) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with SCA`

**Contexto**

- **O que mede (what):** Análise de composição de software sinaliza dependências vulneráveis.
- **Por que importa (why):** Dependências com vulnerabilidades conhecidas são um dos principais vetores de ataque.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sca and dependency review implementado. As equipes operam sem esta capacidade. | • Nenhuma SCA e revisão de dependências implantadas<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de sca and dependency review com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SCA and dependency review adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SCA and dependency review padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SCA and dependency review é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C4-Q4: Em que medida Integração de Segurança (DevSecOps) (secret scanning and push protection) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `secrets blocked per month`

**Contexto**

- **O que mede (what):** Segredos são detectados antes do commit e bloqueados no push.
- **Por que importa (why):** Segredos vazados são a fonte #1 de violações em ambientes de nuvem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem secret scanning and push protection implementado. As equipes operam sem esta capacidade. | • Nenhuma varredura de segredos e push protection implantadas<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de secret scanning and push protection com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | secret scanning and push protection adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | secret scanning and push protection padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | secret scanning and push protection é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C4-Q5: Em que medida Integração de Segurança (DevSecOps) (DAST and API security testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs DAST-tested`

**Contexto**

- **O que mede (what):** Testes dinâmicos exercitam a aplicação em execução para vulnerabilidades de runtime.
- **Por que importa (why):** DAST detecta problemas que SAST não consegue (autenticação, lógica, configuração).

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dast and api security testing implementado. As equipes operam sem esta capacidade. | • Nenhum DAST e teste de segurança de API implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de dast and api security testing com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | DAST and API security testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | DAST and API security testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | DAST and API security testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C4-Q6: Em que medida Integração de Segurança (DevSecOps) (security champions program) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `champions per 20 devs`

**Contexto**

- **O que mede (what):** Toda equipe tem um champion de segurança treinado e com recursos.
- **Por que importa (why):** Champions escalam expertise de segurança para todas as equipes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem security champions program implementado. As equipes operam sem esta capacidade. | • Nenhum programa de security champions implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de security champions program com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | security champions program adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | security champions program padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | security champions program é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C5: Estratégias de Release e Implantação

**6 questões neste capability.**

### P2-C5-Q1: Em que medida Estratégias de Release e Implantação (blue/green or canary deploys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with canary`

**Contexto**

- **O que mede (what):** Deploys canary ou blue/green reduzem o raio de impacto.
- **Por que importa (why):** Rollout progressivo detecta problemas antes da exposição total.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem blue/green or canary deploys implementado. As equipes operam sem esta capacidade. | • Nenhum deploy blue/green ou canary implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de blue/green or canary deploys com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | blue/green or canary deploys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | blue/green or canary deploys padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | blue/green or canary deploys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C5-Q2: Em que medida Estratégias de Release e Implantação (automated rollback) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median rollback time`

**Contexto**

- **O que mede (what):** Violação de SLO ou pico de erros dispara rollback automático.
- **Por que importa (why):** Rollback automatizado limita o impacto ao usuário quando deploys dão errado.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated rollback implementado. As equipes operam sem esta capacidade. | • Nenhum rollback automatizado implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de automated rollback com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | automated rollback adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | automated rollback padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | automated rollback é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C5-Q3: Em que medida Estratégias de Release e Implantação (feature flag platform) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flags in active use`

**Contexto**

- **O que mede (what):** Uma plataforma de flags dá suporte a exposição progressiva e experimentos.
- **Por que importa (why):** Flags desacoplam deploy de release.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem feature flag platform implementado. As equipes operam sem esta capacidade. | • Nenhuma plataforma de feature flags implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de feature flag platform com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | feature flag platform adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | feature flag platform padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | feature flag platform é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C5-Q4: Em que medida Estratégias de Release e Implantação (release coordination via ChatOps) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% releases using ChatOps`

**Contexto**

- **O que mede (what):** Releases são coordenadas por um chat bot com aprovações.
- **Por que importa (why):** ChatOps cria uma trilha de auditoria e reduz erros de handoff.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem release coordination via chatops implementado. As equipes operam sem esta capacidade. | • Nenhuma coordenação de release via ChatOps implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de release coordination via chatops com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | release coordination via ChatOps adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | release coordination via ChatOps padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | release coordination via ChatOps é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C5-Q5: Em que medida Estratégias de Release e Implantação (progressive delivery across regions) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `regions rolled out per release`

**Contexto**

- **O que mede (what):** Releases se propagam entre regiões com verificações de saúde automatizadas.
- **Por que importa (why):** Rollout multi-região contém falhas regionais.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem progressive delivery across regions implementado. As equipes operam sem esta capacidade. | • Nenhuma entrega progressiva entre regiões implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de progressive delivery across regions com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | progressive delivery across regions adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | progressive delivery across regions padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | progressive delivery across regions é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C5-Q6: Em que medida Estratégias de Release e Implantação (release metrics dashboard) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% releases meeting SLO`

**Contexto**

- **O que mede (what):** Sucesso de implantação e impacto em SLO são acompanhados por release.
- **Por que importa (why):** Retros de release orientadas por dados impulsionam melhoria contínua.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem release metrics dashboard implementado. As equipes operam sem esta capacidade. | • Nenhum dashboard de métricas de release implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de release metrics dashboard com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | release metrics dashboard adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | release metrics dashboard padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | release metrics dashboard é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C6: Automação de Testes

**7 questões neste capability.**

### P2-C6-Q1: Em que medida Automação de Testes (unit test coverage targets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos >80% coverage`

**Contexto**

- **O que mede (what):** Todo repositório tem uma meta mensurável de cobertura.
- **Por que importa (why):** Cobertura é uma proxy útil quando combinada com testes de mutação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem unit test coverage targets implementado. As equipes operam sem esta capacidade. | • Nenhuma meta de cobertura de testes unitários implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de unit test coverage targets com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | unit test coverage targets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | unit test coverage targets padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | unit test coverage targets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q2: Em que medida Automação de Testes (integration test suites) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `integration tests in CI`

**Contexto**

- **O que mede (what):** Testes de integração exercitam fronteiras reais de serviços.
- **Por que importa (why):** Testes de integração detectam bugs de conexão que testes unitários não conseguem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem integration test suites implementado. As equipes operam sem esta capacidade. | • Nenhuma suíte de testes de integração implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de integration test suites com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | integration test suites adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | integration test suites padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | integration test suites é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q3: Em que medida Automação de Testes (end-to-end / journey tests) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical journeys automated`

**Contexto**

- **O que mede (what):** Jornadas críticas de usuário rodam automaticamente em todo deploy.
- **Por que importa (why):** Testes E2E protegem fluxos críticos para receita.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem end-to-end / journey tests implementado. As equipes operam sem esta capacidade. | • Nenhum teste end-to-end / de jornada implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de end-to-end / journey tests com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | end-to-end / journey tests adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | end-to-end / journey tests padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | end-to-end / journey tests é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q4: Em que medida Automação de Testes (contract testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% service pairs with contract tests`

**Contexto**

- **O que mede (what):** Testes de contrato orientados pelo consumidor detectam quebras de API.
- **Por que importa (why):** Testes de contrato protegem a compatibilidade de microserviços.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem contract testing implementado. As equipes operam sem esta capacidade. | • Nenhum teste de contrato implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de contract testing com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | contract testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | contract testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | contract testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q5: Em que medida Automação de Testes (AI-assisted test generation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% tests AI-generated`

**Contexto**

- **O que mede (what):** IA propõe testes para código novo e alterado.
- **Por que importa (why):** Testes gerados por IA elevam o patamar mínimo de cobertura.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai-assisted test generation implementado. As equipes operam sem esta capacidade. | • Nenhuma geração de testes assistida por IA implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de ai-assisted test generation com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | AI-assisted test generation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | AI-assisted test generation padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | AI-assisted test generation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q6: Em que medida Automação de Testes (flaky-test detection & quarantine) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flaky test rate`

**Contexto**

- **O que mede (what):** Testes flaky são colocados automaticamente em quarentena e triados.
- **Por que importa (why):** Testes flaky corroem a confiança; a detecção a restaura.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem flaky-test detection & quarantine implementado. As equipes operam sem esta capacidade. | • Nenhuma detecção e quarentena de testes flaky implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de flaky-test detection & quarantine com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | flaky-test detection & quarantine adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | flaky-test detection & quarantine padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | flaky-test detection & quarantine é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C6-Q7: Em que medida Automação de Testes (mutation testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `mutation score of critical modules`

**Contexto**

- **O que mede (what):** Testes de mutação validam a qualidade da suíte de testes.
- **Por que importa (why):** Pontuações de mutação revelam se os testes realmente detectam bugs.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem mutation testing implementado. As equipes operam sem esta capacidade. | • Nenhum teste de mutação implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de mutation testing com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | mutation testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | mutation testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | mutation testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C7: Gestão de Incidentes e SRE

**7 questões neste capability.**

### P2-C7-Q1: Em que medida Gestão de Incidentes e SRE (on-call rotation with tooling) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with on-call`

**Contexto**

- **O que mede (what):** Todo serviço de produção tem uma rotação de on-call nomeada.
- **Por que importa (why):** Propriedade clara é a base da confiabilidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem on-call rotation with tooling implementado. As equipes operam sem esta capacidade. | • Nenhuma rotação on-call com ferramentas implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de on-call rotation with tooling com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | on-call rotation with tooling adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | on-call rotation with tooling padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | on-call rotation with tooling é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q2: Em que medida Gestão de Incidentes e SRE (blameless postmortems) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% incidents with postmortem`

**Contexto**

- **O que mede (what):** Postmortems focam em sistemas, não em pessoas.
- **Por que importa (why):** Cultura sem culpabilização desbloqueia aprendizado honesto.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem blameless postmortems implementado. As equipes operam sem esta capacidade. | • Nenhum postmortem sem culpa implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de blameless postmortems com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | blameless postmortems adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | blameless postmortems padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | blameless postmortems é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q3: Em que medida Gestão de Incidentes e SRE (error budget policy) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Segurança, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services using error budgets`

**Contexto**

- **O que mede (what):** Error budgets governam trabalho de features versus trabalho de confiabilidade.
- **Por que importa (why):** Error budgets tornam a confiabilidade uma decisão de negócio compartilhada.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem error budget policy implementado. As equipes operam sem esta capacidade. | • Nenhuma política de orçamento de erro implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de error budget policy com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | error budget policy adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | error budget policy padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | error budget policy é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q4: Em que medida Gestão de Incidentes e SRE (chaos engineering) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `gamedays per quarter`

**Contexto**

- **O que mede (what):** Injeção controlada de falhas exercita a resiliência.
- **Por que importa (why):** Chaos engineering constrói confiança na recuperação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem chaos engineering implementado. As equipes operam sem esta capacidade. | • Nenhuma engenharia do caos implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de chaos engineering com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | chaos engineering adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | chaos engineering padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | chaos engineering é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q5: Em que medida Gestão de Incidentes e SRE (incident commander role) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% major incidents with IC`

**Contexto**

- **O que mede (what):** Um incident commander coordena a resposta.
- **Por que importa (why):** Um único coordenador reduz a confusão durante incidentes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem incident commander role implementado. As equipes operam sem esta capacidade. | • Nenhum papel de comandante de incidente implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de incident commander role com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | incident commander role adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | incident commander role padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | incident commander role é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q6: Em que medida Gestão de Incidentes e SRE (SRE-dev partnership model) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams with SRE partner`

**Contexto**

- **O que mede (what):** Equipes de SRE e desenvolvimento colaboram em roadmaps de confiabilidade.
- **Por que importa (why):** Parceria incorporada supera gatekeeping.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sre-dev partnership model implementado. As equipes operam sem esta capacidade. | • Nenhum modelo de parceria SRE-dev implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de sre-dev partnership model com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SRE-dev partnership model adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SRE-dev partnership model padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SRE-dev partnership model é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C7-Q7: Em que medida Gestão de Incidentes e SRE (runbook automation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% incidents with runbook run`

**Contexto**

- **O que mede (what):** Etapas de runbook são codificadas e executadas automaticamente.
- **Por que importa (why):** Automação de runbook reduz MTTR e erro humano.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem runbook automation implementado. As equipes operam sem esta capacidade. | • Nenhuma automação de runbooks implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de runbook automation com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | runbook automation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | runbook automation padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | runbook automation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C8: Gestão de Artefatos e Pacotes

**5 questões neste capability.**

### P2-C8-Q1: Em que medida Gestão de Artefatos e Pacotes (internal package registry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% packages via registry`

**Contexto**

- **O que mede (what):** Registro interno hospeda todos os pacotes; nada depende apenas de fontes públicas.
- **Por que importa (why):** Um registro permite controles de auditoria e disponibilidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem internal package registry implementado. As equipes operam sem esta capacidade. | • Nenhum registro interno de pacotes implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de internal package registry com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | internal package registry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | internal package registry padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | internal package registry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C8-Q2: Em que medida Gestão de Artefatos e Pacotes (SBOM for every build) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% builds with SBOM`

**Contexto**

- **O que mede (what):** Cada build gera uma lista de materiais de software.
- **Por que importa (why):** SBOMs agora são um requisito regulatório e de segurança.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sbom for every build implementado. As equipes operam sem esta capacidade. | • Nenhum SBOM para todo build implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de sbom for every build com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SBOM for every build adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SBOM for every build padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SBOM for every build é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C8-Q3: Em que medida Gestão de Artefatos e Pacotes (artifact signing (SLSA)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% artifacts signed`

**Contexto**

- **O que mede (what):** Artefatos são assinados e verificados no deploy.
- **Por que importa (why):** Assinatura previne adulteração da cadeia de suprimentos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem artifact signing (slsa) implementado. As equipes operam sem esta capacidade. | • Nenhuma assinatura de artefatos (SLSA) implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de artifact signing (slsa) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | artifact signing (SLSA) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | artifact signing (SLSA) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | artifact signing (SLSA) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C8-Q4: Em que medida Gestão de Artefatos e Pacotes (vulnerability scanning of artifacts) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% artifacts scanned`

**Contexto**

- **O que mede (what):** Todo artefato é varrido antes da implantação.
- **Por que importa (why):** Varredura pre-deploy bloqueia artefatos sabidamente ruins.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vulnerability scanning of artifacts implementado. As equipes operam sem esta capacidade. | • Nenhuma varredura de vulnerabilidades de artefatos implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de vulnerability scanning of artifacts com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | vulnerability scanning of artifacts adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | vulnerability scanning of artifacts padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | vulnerability scanning of artifacts é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C8-Q5: Em que medida Gestão de Artefatos e Pacotes (retention & promotion policies) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `artifacts promoted via policy`

**Contexto**

- **O que mede (what):** Artefatos avançam por dev→stage→prod com gates de política.
- **Por que importa (why):** Políticas de promoção vinculam deploys à proveniência.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem retention & promotion policies implementado. As equipes operam sem esta capacidade. | • Nenhuma política de retenção e promoção implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de retention & promotion policies com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | retention & promotion policies adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | retention & promotion policies padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | retention & promotion policies é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C9: Gestão de Mudanças e GitOps

**5 questões neste capability.**

### P2-C9-Q1: Em que medida Gestão de Mudanças e GitOps (GitOps controllers in prod) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% clusters on GitOps`

**Contexto**

- **O que mede (what):** O estado do cluster é reconciliado a partir do Git por um controlador.
- **Por que importa (why):** GitOps torna a mudança rastreável, auditável e reversível.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem gitops controllers in prod implementado. As equipes operam sem esta capacidade. | • Nenhum controlador GitOps em produção implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de gitops controllers in prod com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | GitOps controllers in prod adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | GitOps controllers in prod padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | GitOps controllers in prod é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C9-Q2: Em que medida Gestão de Mudanças e GitOps (automated change tickets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% changes ticketed automatically`

**Contexto**

- **O que mede (what):** Registros de mudança são criados automaticamente a partir de PRs.
- **Por que importa (why):** Automação mantém registros precisos sem desacelerar a entrega.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated change tickets implementado. As equipes operam sem esta capacidade. | • Nenhum ticket de mudança automatizado implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de automated change tickets com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | automated change tickets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | automated change tickets padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | automated change tickets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C9-Q3: Em que medida Gestão de Mudanças e GitOps (approvals in PR (not tickets)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% approvals in PR`

**Contexto**

- **O que mede (what):** Aprovações de mudança acontecem na revisão de código, não em tickets separados.
- **Por que importa (why):** Approval-as-code reduz o tempo de ciclo mantendo a trilha de auditoria.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem approvals in pr (not tickets) implementado. As equipes operam sem esta capacidade. | • Nenhuma aprovação em PR (não tickets) implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de approvals in pr (not tickets) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | approvals in PR (not tickets) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | approvals in PR (not tickets) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | approvals in PR (not tickets) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C9-Q4: Em que medida Gestão de Mudanças e GitOps (environment promotion via PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% envs promoted via PR`

**Contexto**

- **O que mede (what):** Mover de stage para prod é um PR, não um clique.
- **Por que importa (why):** Promoção baseada em PR herda review e rollback.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem environment promotion via pr implementado. As equipes operam sem esta capacidade. | • Nenhuma promoção de ambiente via PR implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de environment promotion via pr com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | environment promotion via PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | environment promotion via PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | environment promotion via PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C9-Q5: Em que medida Gestão de Mudanças e GitOps (compliance evidence auto-collected) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `controls automated`

**Contexto**

- **O que mede (what):** Evidências para SOC2/ISO são coletadas automaticamente do CI.
- **Por que importa (why):** Autoevidência transforma auditorias em efeito colateral do trabalho normal.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem compliance evidence auto-collected implementado. As equipes operam sem esta capacidade. | • Nenhuma evidência de conformidade coletada automaticamente implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de compliance evidence auto-collected com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | compliance evidence auto-collected adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | compliance evidence auto-collected padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | compliance evidence auto-collected é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P2-C10: Segurança de Dependências e Cadeia de Suprimentos

**5 questões neste capability.**

### P2-C10-Q1: Em que medida Segurança de Dependências e Cadeia de Suprimentos (dependabot or renovate on every repo) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos auto-updated`

**Contexto**

- **O que mede (what):** Dependabot ou Renovate abre PRs para dependências desatualizadas.
- **Por que importa (why):** Atualizações automatizadas mantêm curta a janela de CVE.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dependabot or renovate on every repo implementado. As equipes operam sem esta capacidade. | • Nenhum dependabot ou renovate em todo repositório implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de dependabot or renovate on every repo com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | dependabot or renovate on every repo adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | dependabot or renovate on every repo padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | dependabot or renovate on every repo é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C10-Q2: Em que medida Segurança de Dependências e Cadeia de Suprimentos (allow-list registries only) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% deps from allow-listed source`

**Contexto**

- **O que mede (what):** Registros proxy filtram pacotes de fontes confiáveis.
- **Por que importa (why):** Proxying bloqueia typosquatting e pacotes maliciosos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem allow-list registries only implementado. As equipes operam sem esta capacidade. | • Nenhum uso exclusivo de registries em allow-list implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de allow-list registries only com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | allow-list registries only adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | allow-list registries only padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | allow-list registries only é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C10-Q3: Em que medida Segurança de Dependências e Cadeia de Suprimentos (build provenance (SLSA level)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `SLSA level reached`

**Contexto**

- **O que mede (what):** Builds carregam metadados de proveniência verificáveis.
- **Por que importa (why):** Proveniência é a base da confiança na cadeia de suprimentos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build provenance (slsa level) implementado. As equipes operam sem esta capacidade. | • Nenhuma proveniência de build (nível SLSA) implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de build provenance (slsa level) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | build provenance (SLSA level) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | build provenance (SLSA level) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | build provenance (SLSA level) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C10-Q4: Em que medida Segurança de Dependências e Cadeia de Suprimentos (critical dep response playbook) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median time to patch critical`

**Contexto**

- **O que mede (what):** Um playbook trata eventos da classe Log4Shell.
- **Por que importa (why):** Preparação supera improvisação em um zero-day.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem critical dep response playbook implementado. As equipes operam sem esta capacidade. | • Nenhum playbook de resposta a dependências críticas implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de critical dep response playbook com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | critical dep response playbook adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | critical dep response playbook padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | critical dep response playbook é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P2-C10-Q5: Em que medida Segurança de Dependências e Cadeia de Suprimentos (vendor/OSS risk reviews) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical vendors reviewed/year`

**Contexto**

- **O que mede (what):** Fornecedores de alto risco e dependências OSS são revisados anualmente.
- **Por que importa (why):** A review revela risco antes que ele vire incidente.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vendor/oss risk reviews implementado. As equipes operam sem esta capacidade. | • Nenhuma revisão de risco de fornecedor/OSS implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de vendor/oss risk reviews com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | vendor/OSS risk reviews adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | vendor/OSS risk reviews padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | vendor/OSS risk reviews é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P2** é a média das 10 capacidades.
- O resultado é exibido em escala 0-4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0 a L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
