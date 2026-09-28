# Assessment de Maturidade IA: Pilar P3, Plataforma de Aplicações

🌐 [English](P3-plataforma-de-aplicações.md) · Português (Brasil) · [Español](P3-plataforma-de-aplicações.es.md)

> Mede a sofisticação da plataforma: arquitetura cloud-native, APIs, IA, dados, agentes, identidade, multi-cloud, performance e FinOps.

## Visão geral

- **Pilar:** `P3`: Plataforma de Aplicações
- **Capacidades (capabilities):** 9
- **Questões totais:** 46
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

## Capacidades do pilar P3

- **P3-C1**: Arquitetura Cloud-Native (5 questões)
- **P3-C2**: Gestão de APIs (5 questões)
- **P3-C3**: Desenvolvimento de Aplicações IA (5 questões)
- **P3-C4**: Plataforma de Dados e Lakehouse (5 questões)
- **P3-C5**: Aplicações Agênticas (6 questões)
- **P3-C6**: Gestão de Identidades e Acessos (5 questões)
- **P3-C7**: Multi-Cloud e Portabilidade (5 questões)
- **P3-C8**: Desempenho e Escalabilidade (5 questões)
- **P3-C9**: FinOps e Otimização de Custos (5 questões)

---

## P3-C1: Arquitetura Cloud-Native

**5 questões neste capability.**

### P3-C1-Q1: Qual é a maturidade da adoção de arquitetura cloud-native?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% workloads containerized`

**Contexto**

- **O que mede (what):** Mede a adoção de padrões cloud-native, incluindo conteinerização, orquestração e decomposição de serviços.
- **Por que importa (why):** Arquiteturas cloud-native permitem escalabilidade 10x mais rápida, disponibilidade de 99.99% e redução de 50% no custo de infraestrutura.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Aplicações monolíticas implantadas em VMs ou bare metal. Sem containerização. | • Sem adoção de containers<br>• Topologia de implantação baseada em VMs<br>• Arquitetura monolítica em uso |
| **L1** | Em Desenvolvimento | Algumas aplicações containerizadas (<30%). Docker usado para desenvolvimento, mas não em produção. | • Taxa medida de containerização <30%<br>• Docker apenas em desenvolvimento<br>• Sem plataforma de orquestração |
| **L2** | Definido | 50-70% das cargas de trabalho containerizadas. Kubernetes ou orquestração de containers em produção. Decomposição básica em microsserviços. | • Taxa medida de containerização de 50-70%<br>• K8s em produção<br>• Alguns microsserviços implantados |
| **L3** | Gerenciado | >85% das cargas de trabalho cloud-native. Service mesh, implantação GitOps, escalabilidade automatizada. Fronteiras de serviço bem definidas. | • Taxa medida cloud-native >85%<br>• Service mesh implantado<br>• Fluxo de trabalho GitOps adotado<br>• Regras de escalabilidade automatizada configuradas |
| **L4** | Otimizando | Cloud-native completo com alocação de recursos otimizada por IA, escalabilidade automática preditiva, infraestrutura self-healing e serverless quando apropriado. | • Otimização de recursos por IA<br>• Escalabilidade automatizada preditiva habilitada<br>• Infraestrutura self-healing habilitada<br>• Adoção de plataforma serverless |

---

### P3-C1-Q2: Em que medida Arquitetura Nativa da Nuvem (container adoption) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads containerized`

**Contexto**

- **O que mede (what):** Workloads rodam como contêineres no Kubernetes ou em plataformas gerenciadas.
- **Por que importa (why):** Contêineres viabilizam densidade, portabilidade e deploys declarativos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem container adoption implementado. As equipes operam sem esta capacidade. | • Nenhuma adoção de containers implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de container adoption com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | container adoption adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | container adoption padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | container adoption é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C1-Q3: Em que medida Arquitetura Nativa da Nuvem (service mesh / zero trust networking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services on mesh`

**Contexto**

- **O que mede (what):** Service mesh lida com mTLS, retentativas e modelagem de tráfego.
- **Por que importa (why):** Mesh move confiabilidade e segurança para fora do código da aplicação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem service mesh / zero trust networking implementado. As equipes operam sem esta capacidade. | • Nenhum service mesh / rede zero trust implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de service mesh / zero trust networking com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | service mesh / zero trust networking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | service mesh / zero trust networking padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | service mesh / zero trust networking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C1-Q4: Em que medida Arquitetura Nativa da Nuvem (event-driven architecture) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% flows async`

**Contexto**

- **O que mede (what):** Eventos e filas desacoplam serviços para resiliência e escala.
- **Por que importa (why):** EDA permite baixo acoplamento e degradação graciosa.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem event-driven architecture implementado. As equipes operam sem esta capacidade. | • Nenhuma arquitetura orientada a eventos implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de event-driven architecture com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | event-driven architecture adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | event-driven architecture padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | event-driven architecture é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C1-Q5: Em que medida Arquitetura Nativa da Nuvem (managed services preference) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% managed vs self-hosted`

**Contexto**

- **O que mede (what):** Prefira bancos de dados, filas e caches gerenciados a operações próprias.
- **Por que importa (why):** Serviços gerenciados deslocam a carga operacional para o provedor de nuvem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem managed services preference implementado. As equipes operam sem esta capacidade. | • Nenhuma preferência por serviços gerenciados implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de managed services preference com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | managed services preference adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | managed services preference padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | managed services preference é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C2: Gestão de APIs

**5 questões neste capability.**

### P3-C2-Q1: Quão madura é sua estratégia de gestão de APIs?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, engineering-leader, Segurança
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% APIs with OpenAPI spec`

**Contexto**

- **O que mede (what):** Mede a maturidade das práticas de design, documentação, versionamento e governança de APIs.
- **Por que importa (why):** APIs bem gerenciadas reduzem o tempo de integração em 70% e permitem crescimento do ecossistema de parceiros.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem padrões de API. APIs desenhadas ad-hoc. Sem documentação além do código-fonte. | • Sem padrões de API<br>• Design de API ad-hoc<br>• Sem documentação de API |
| **L1** | Em Desenvolvimento | Algumas APIs têm documentação básica. Sem estratégia de versionamento. Tratamento de erros inconsistente. | • Documentação básica de API existente<br>• Sem política de versionamento<br>• Formatos de erro inconsistentes |
| **L2** | Definido | Especificações OpenAPI para >50% das APIs. Diretrizes de design de API documentadas. Estratégia de versionamento definida. | • >50% das APIs com OpenAPI<br>• Documento de diretrizes de design<br>• Estratégia de versionamento de API documentada |
| **L3** | Gerenciado | API gateway com gerenciamento centralizado. >80% das APIs documentadas. Rate limiting, autenticação e monitoramento padronizados. Gerenciamento do ciclo de vida de APIs. | • API gateway implantado<br>• Taxa medida de documentação >80%<br>• Autenticação/rate limiting padronizados |
| **L4** | Otimizando | Gerenciamento de APIs com IA: documentação gerada automaticamente a partir do código, detecção de anomalias no tráfego de API, planejamento preditivo de capacidade, verificações automatizadas de compatibilidade retroativa. | • Documentação de API gerada automaticamente<br>• Detecção de anomalias de tráfego<br>• Planejamento preditivo de capacidade<br>• Verificações automáticas de compatibilidade |

---

### P3-C2-Q2: Em que medida Gestão de APIs (API gateway for all external APIs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs behind gateway`

**Contexto**

- **O que mede (what):** Gateway lida com autenticação, rate limiting e observabilidade.
- **Por que importa (why):** Um gateway centraliza preocupações transversais de API.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem api gateway for all external apis implementado. As equipes operam sem esta capacidade. | • Nenhum API gateway para todas as APIs externas implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de api gateway for all external apis com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | API gateway for all external APIs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | API gateway for all external APIs padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | API gateway for all external APIs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C2-Q3: Em que medida Gestão de APIs (OpenAPI contracts) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs with spec`

**Contexto**

- **O que mede (what):** Toda API tem um contrato legível por máquina.
- **Por que importa (why):** Contratos viabilizam codegen, servidores mock e testes de compatibilidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem openapi contracts implementado. As equipes operam sem esta capacidade. | • Nenhum contrato OpenAPI implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de openapi contracts com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | OpenAPI contracts adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | OpenAPI contracts padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | OpenAPI contracts é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C2-Q4: Em que medida Gestão de APIs (versioning & deprecation policy) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deprecated APIs retired on time`

**Contexto**

- **O que mede (what):** Versionamento explícito e cronogramas de descontinuação.
- **Por que importa (why):** Política clara preserva a confiança do cliente e evita quebras.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem versioning & deprecation policy implementado. As equipes operam sem esta capacidade. | • Nenhuma política de versionamento e descontinuação implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de versioning & deprecation policy com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | versioning & deprecation policy adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | versioning & deprecation policy padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | versioning & deprecation policy é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C2-Q5: Em que medida Gestão de APIs (developer portal with self-serve keys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time-to-first-call`

**Contexto**

- **O que mede (what):** Emissão de chaves self-service e documentação interativa.
- **Por que importa (why):** Portais de desenvolvedores aceleram a integração de parceiros.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer portal with self-serve keys implementado. As equipes operam sem esta capacidade. | • Nenhum portal de desenvolvedores com chaves self-service implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de developer portal with self-serve keys com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | developer portal with self-serve keys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | developer portal with self-serve keys padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | developer portal with self-serve keys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C3: Desenvolvimento de Aplicações IA

**5 questões neste capability.**

### P3-C3-Q1: Quão madura é a capacidade da sua organização de construir e implantar aplicações com IA?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `# AI features in production`

**Contexto**

- **O que mede (what):** Mede a capability da organização para desenvolver, implantar e manter features de aplicações com IA.
- **Por que importa (why):** Organizações com desenvolvimento maduro de aplicações de IA entregam features de IA 5x mais rápido e com 3x menos incidentes em produção.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem recursos de IA em aplicações de produção. Sem capability da equipe para desenvolvimento de IA. | • Nenhum recurso de IA implantado<br>• Sem habilidades de engenharia de ML/IA<br>• Sem ferramentas de desenvolvimento de IA |
| **L1** | Em Desenvolvimento | Experimentação com APIs de IA (OpenAI, Azure AI) em 1-2 aplicações. Sem práticas de MLOps. | • 1-2 experimentos de IA<br>• Integração direta por API<br>• Nenhuma ferramenta de MLOps em uso |
| **L2** | Definido | 3-5 recursos com IA em produção. Práticas básicas de engenharia de prompt. Padrão RAG para recuperação de conhecimento. | • 3-5 recursos de IA em produção<br>• Diretrizes de engenharia de prompt<br>• Implementação de RAG implantada |
| **L3** | Gerenciado | Framework padronizado de desenvolvimento de IA. Pipeline de avaliação de modelos. Versionamento de prompts e testes A/B. >10 recursos de IA em produção. | • Documentação de framework de desenvolvimento de IA<br>• Pipeline de avaliação de modelos<br>• Fluxo de versionamento de prompts<br>• >10 recursos de IA |
| **L4** | Otimizando | Aplicações AI-native com agentes autônomos, orquestração multi-modelo, avaliação contínua de modelos e otimização automatizada de prompts. Recursos de IA são centrais para o produto. | • Implantações de agentes autônomos<br>• Orquestração multi-modelo habilitada<br>• Avaliação contínua de modelos<br>• Otimização automatizada de prompts |

---

### P3-C3-Q2: Em que medida Desenvolvimento de Aplicações de IA (LLM application frameworks) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% AI apps on framework`

**Contexto**

- **O que mede (what):** Equipes usam frameworks (LangChain, Semantic Kernel) para aplicações LLM.
- **Por que importa (why):** Frameworks aceleram padrões de RAG, agentes e avaliação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem llm application frameworks implementado. As equipes operam sem esta capacidade. | • Nenhum framework de aplicações LLM implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de llm application frameworks com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | LLM application frameworks adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | LLM application frameworks padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | LLM application frameworks é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C3-Q3: Em que medida Desenvolvimento de Aplicações de IA (evaluation harness for AI) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `evals per release`

**Contexto**

- **O que mede (what):** Evals automatizadas rodam em toda mudança de modelo ou prompt.
- **Por que importa (why):** Evals de IA detectam regressões que testes unitários não conseguem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem evaluation harness for ai implementado. As equipes operam sem esta capacidade. | • Nenhum harness de avaliação para IA implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de evaluation harness for ai com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | evaluation harness for AI adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | evaluation harness for AI padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | evaluation harness for AI é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C3-Q4: Em que medida Desenvolvimento de Aplicações de IA (vector database / RAG platform) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `RAG apps in prod`

**Contexto**

- **O que mede (what):** Uma plataforma compartilhada de vector store/RAG atende múltiplas aplicações.
- **Por que importa (why):** RAG centralizado reduz trabalho duplicado entre equipes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vector database / rag platform implementado. As equipes operam sem esta capacidade. | • Nenhum banco de dados vetorial / plataforma RAG implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de vector database / rag platform com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | vector database / RAG platform adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | vector database / RAG platform padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | vector database / RAG platform é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C3-Q5: Em que medida Desenvolvimento de Aplicações de IA (responsible AI / safety filters) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% AI apps with guardrails`

**Contexto**

- **O que mede (what):** Todas as aplicações de IA integram segurança de conteúdo e logging de auditoria.
- **Por que importa (why):** IA responsável é requisito básico; retrofit é caro.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem responsible ai / safety filters implementado. As equipes operam sem esta capacidade. | • Nenhum filtro de segurança / IA responsável implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de responsible ai / safety filters com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | responsible AI / safety filters adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | responsible AI / safety filters padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | responsible AI / safety filters é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C4: Plataforma de Dados e Lakehouse

**5 questões neste capability.**

### P3-C4-Q1: Em que medida Plataforma de Dados e Lakehouse (lakehouse or data platform in use) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% data in platform`

**Contexto**

- **O que mede (what):** Um lakehouse unifica dados estruturados e não estruturados.
- **Por que importa (why):** Lakehouses combinam desempenho de warehouse com flexibilidade de lake.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem lakehouse or data platform in use implementado. As equipes operam sem esta capacidade. | • Nenhum lakehouse ou plataforma de dados em uso implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de lakehouse or data platform in use com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | lakehouse or data platform in use adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | lakehouse or data platform in use padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | lakehouse or data platform in use é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C4-Q2: Em que medida Plataforma de Dados e Lakehouse (data contracts between producers & consumers) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% pipelines with contracts`

**Contexto**

- **O que mede (what):** Contratos de dados declaram schema e garantias de qualidade.
- **Por que importa (why):** Contratos evitam quebras silenciosas entre equipes.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem data contracts between producers & consumers implementado. As equipes operam sem esta capacidade. | • Nenhum contrato de dados entre produtores e consumidores implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de data contracts between producers & consumers com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | data contracts between producers & consumers adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | data contracts between producers & consumers padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | data contracts between producers & consumers é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C4-Q3: Em que medida Plataforma de Dados e Lakehouse (catalog and lineage tracking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% datasets cataloged`

**Contexto**

- **O que mede (what):** Todo dataset tem propriedade, linhagem e metadados de qualidade.
- **Por que importa (why):** Catálogos aceleram descoberta e investigações.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem catalog and lineage tracking implementado. As equipes operam sem esta capacidade. | • Nenhum catálogo e rastreamento de linhagem implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de catalog and lineage tracking com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | catalog and lineage tracking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | catalog and lineage tracking padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | catalog and lineage tracking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C4-Q4: Em que medida Plataforma de Dados e Lakehouse (self-service analytics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% decisions using data`

**Contexto**

- **O que mede (what):** Usuários de negócio consultam dados por conta própria via ferramentas governadas.
- **Por que importa (why):** Self-service remove o gargalo da equipe de dados.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem self-service analytics implementado. As equipes operam sem esta capacidade. | • Nenhuma análise self-service implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de self-service analytics com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | self-service analytics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | self-service analytics padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | self-service analytics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C4-Q5: Em que medida Plataforma de Dados e Lakehouse (real-time streaming ingestion) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% use-cases real-time`

**Contexto**

- **O que mede (what):** Streaming está disponível para casos de uso sensíveis ao tempo.
- **Por que importa (why):** Dados em tempo real permitem IA mais atualizada e decisões operacionais melhores.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem real-time streaming ingestion implementado. As equipes operam sem esta capacidade. | • Nenhuma ingestão de streaming em tempo real implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de real-time streaming ingestion com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | real-time streaming ingestion adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | real-time streaming ingestion padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | real-time streaming ingestion é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C5: Aplicações Agênticas

**6 questões neste capability.**

### P3-C5-Q1: Em que medida Aplicações Agênticas (agents with tool-use in prod) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `agents in production`

**Contexto**

- **O que mede (what):** Agentes chamam ferramentas e APIs para realizar trabalho em múltiplas etapas.
- **Por que importa (why):** Workflows agênticos automatizam tarefas complexas que humanos costumavam rotear.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem agents with tool-use in prod implementado. As equipes operam sem esta capacidade. | • Nenhum agente com uso de ferramentas em produção implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de agents with tool-use in prod com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | agents with tool-use in prod adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | agents with tool-use in prod padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | agents with tool-use in prod é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C5-Q2: Em que medida Aplicações Agênticas (orchestration framework (Semantic Kernel, etc)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% agents on framework`

**Contexto**

- **O que mede (what):** Agentes são construídos sobre um runtime padrão de orquestração.
- **Por que importa (why):** Runtimes padrão reduzem o custo de engenharia por agente.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem orchestration framework (semantic kernel, etc) implementado. As equipes operam sem esta capacidade. | • Nenhum framework de orquestração (Semantic Kernel, etc) implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de orchestration framework (semantic kernel, etc) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | orchestration framework (Semantic Kernel, etc) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | orchestration framework (Semantic Kernel, etc) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | orchestration framework (Semantic Kernel, etc) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C5-Q3: Em que medida Aplicações Agênticas (evaluation and safety for agents) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `eval scenarios per agent`

**Contexto**

- **O que mede (what):** Agentes são avaliados quanto a segurança, custo e conclusão de tarefas.
- **Por que importa (why):** Avaliação de agentes é diferente da avaliação de LLM.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem evaluation and safety for agents implementado. As equipes operam sem esta capacidade. | • Nenhuma avaliação e segurança para agentes implantadas<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de evaluation and safety for agents com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | evaluation and safety for agents adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | evaluation and safety for agents padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | evaluation and safety for agents é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C5-Q4: Em que medida Aplicações Agênticas (tool/action registry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `tools available to agents`

**Contexto**

- **O que mede (what):** Um registro governado lista as ferramentas que agentes podem chamar.
- **Por que importa (why):** Um registro controla o raio de impacto e permite auditoria.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem tool/action registry implementado. As equipes operam sem esta capacidade. | • Nenhum registro de ferramentas/ações implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de tool/action registry com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | tool/action registry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | tool/action registry padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | tool/action registry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C5-Q5: Em que medida Aplicações Agênticas (human-in-the-loop controls) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% agents with HITL`

**Contexto**

- **O que mede (what):** Ações de alto risco exigem confirmação humana.
- **Por que importa (why):** HITL permite que equipes entreguem agentes com segurança enquanto aprendem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem human-in-the-loop controls implementado. As equipes operam sem esta capacidade. | • Nenhum controle human-in-the-loop implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de human-in-the-loop controls com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | human-in-the-loop controls adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | human-in-the-loop controls padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | human-in-the-loop controls é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C5-Q6: Em que medida Aplicações Agênticas (agent cost and latency telemetry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `p95 agent step latency`

**Contexto**

- **O que mede (what):** Desempenho e custo dos agentes são acompanhados por etapa.
- **Por que importa (why):** Telemetria é necessária para operar agentes com rentabilidade em escala.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem agent cost and latency telemetry implementado. As equipes operam sem esta capacidade. | • Nenhuma telemetria de custo e latência de agentes implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de agent cost and latency telemetry com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | agent cost and latency telemetry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | agent cost and latency telemetry padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | agent cost and latency telemetry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C6: Gestão de Identidades e Acessos

**5 questões neste capability.**

### P3-C6-Q1: Em que medida Gestão de Identidades e Acessos (SSO for all apps) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% apps behind SSO`

**Contexto**

- **O que mede (what):** Todas as aplicações autenticam via SSO central.
- **Por que importa (why):** SSO é a base do ciclo de vida do usuário e da revogação.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sso for all apps implementado. As equipes operam sem esta capacidade. | • Nenhum SSO para todas as aplicações implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de sso for all apps com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | SSO for all apps adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | SSO for all apps padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | SSO for all apps é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C6-Q2: Em que medida Gestão de Identidades e Acessos (workload identity (no long-lived secrets)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads using WI`

**Contexto**

- **O que mede (what):** Workloads usam identidade gerenciada, não chaves estáticas.
- **Por que importa (why):** Identidades gerenciadas eliminam uma classe inteira de vazamento.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem workload identity (no long-lived secrets) implementado. As equipes operam sem esta capacidade. | • Nenhuma identidade de workload (sem segredos de longa duração) implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de workload identity (no long-lived secrets) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | workload identity (no long-lived secrets) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | workload identity (no long-lived secrets) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | workload identity (no long-lived secrets) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C6-Q3: Em que medida Gestão de Identidades e Acessos (least-privilege with JIT elevation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% access through JIT`

**Contexto**

- **O que mede (what):** Admin permanente é substituído por elevação just-in-time.
- **Por que importa (why):** JIT reduz drasticamente o raio de impacto de contas comprometidas.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem least-privilege with jit elevation implementado. As equipes operam sem esta capacidade. | • Nenhum privilégio mínimo com elevação JIT implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de least-privilege with jit elevation com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | least-privilege with JIT elevation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | least-privilege with JIT elevation padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | least-privilege with JIT elevation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C6-Q4: Em que medida Gestão de Identidades e Acessos (conditional access policies) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% sessions policy-evaluated`

**Contexto**

- **O que mede (what):** Acesso é concedido com base em dispositivo, localização e risco.
- **Por que importa (why):** Acesso condicional adapta a segurança ao contexto.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem conditional access policies implementado. As equipes operam sem esta capacidade. | • Nenhuma política de acesso condicional implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de conditional access policies com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | conditional access policies adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | conditional access policies padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | conditional access policies é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C6-Q5: Em que medida Gestão de Identidades e Acessos (access reviews and audit) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `access reviews per year`

**Contexto**

- **O que mede (what):** Acesso é revisado pelo menos trimestralmente e registrado.
- **Por que importa (why):** Reviews previnem drift de acesso causado por aquisições e reorganizações.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem access reviews and audit implementado. As equipes operam sem esta capacidade. | • Nenhuma revisão de acesso e auditoria implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de access reviews and audit com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | access reviews and audit adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | access reviews and audit padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | access reviews and audit é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C7: Multi-Cloud e Portabilidade

**5 questões neste capability.**

### P3-C7-Q1: Em que medida Multi-Cloud e Portabilidade (container-based workloads for portability) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads portable`

**Contexto**

- **O que mede (what):** Workloads rodam em contêineres em qualquer nuvem.
- **Por que importa (why):** Portabilidade é uma proteção contra lock-in e indisponibilidades.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem container-based workloads for portability implementado. As equipes operam sem esta capacidade. | • Nenhuma carga de trabalho baseada em containers para portabilidade implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de container-based workloads for portability com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | container-based workloads for portability adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | container-based workloads for portability padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | container-based workloads for portability é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C7-Q2: Em que medida Multi-Cloud e Portabilidade (abstracted data tier (Postgres, etc)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% data on portable engines`

**Contexto**

- **O que mede (what):** Serviços de dados usam padrões abertos (Postgres, MySQL).
- **Por que importa (why):** Engines abertas mantêm os custos de migração limitados.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem abstracted data tier (postgres, etc) implementado. As equipes operam sem esta capacidade. | • Nenhuma camada de dados abstraída (Postgres, etc) implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de abstracted data tier (postgres, etc) com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | abstracted data tier (Postgres, etc) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | abstracted data tier (Postgres, etc) padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | abstracted data tier (Postgres, etc) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C7-Q3: Em que medida Multi-Cloud e Portabilidade (multi-region deployment capability) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services multi-region`

**Contexto**

- **O que mede (what):** Serviços podem rodar active-active entre regiões.
- **Por que importa (why):** Capability multi-região é necessária para DR e conformidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem multi-region deployment capability implementado. As equipes operam sem esta capacidade. | • Nenhuma capacidade de implantação multi-região implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de multi-region deployment capability com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | multi-region deployment capability adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | multi-region deployment capability padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | multi-region deployment capability é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C7-Q4: Em que medida Multi-Cloud e Portabilidade (cloud-agnostic IaC modules) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% modules cloud-agnostic`

**Contexto**

- **O que mede (what):** Módulos de IaC abstraem especificidades de provedores quando faz sentido.
- **Por que importa (why):** Abstração cuidadosa limita a dor de portabilidade.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cloud-agnostic iac modules implementado. As equipes operam sem esta capacidade. | • Nenhum módulo IaC agnóstico de nuvem implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de cloud-agnostic iac modules com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | cloud-agnostic IaC modules adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | cloud-agnostic IaC modules padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | cloud-agnostic IaC modules é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C7-Q5: Em que medida Multi-Cloud e Portabilidade (disaster recovery drills) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `DR drills per year`

**Contexto**

- **O que mede (what):** Exercícios anuais de DR validam tempo e processo de recuperação.
- **Por que importa (why):** DR não testado não é DR.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem disaster recovery drills implementado. As equipes operam sem esta capacidade. | • Nenhum exercício de recuperação de desastres implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de disaster recovery drills com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | disaster recovery drills adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | disaster recovery drills padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | disaster recovery drills é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C8: Desempenho e Escalabilidade

**5 questões neste capability.**

### P3-C8-Q1: Em que medida Desempenho e Escalabilidade (performance budgets per service) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with perf budget`

**Contexto**

- **O que mede (what):** Serviços declaram orçamentos de latência e throughput.
- **Por que importa (why):** Orçamentos tornam desempenho um requisito de primeira classe.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem performance budgets per service implementado. As equipes operam sem esta capacidade. | • Nenhum orçamento de desempenho por serviço implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de performance budgets per service com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | performance budgets per service adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | performance budgets per service padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | performance budgets per service é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C8-Q2: Em que medida Desempenho e Escalabilidade (load/stress testing in CI) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services load-tested`

**Contexto**

- **O que mede (what):** Testes de carga rodam em todo candidato a release.
- **Por que importa (why):** Detectar regressões no CI é melhor do que detectá-las em prod.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem load/stress testing in ci implementado. As equipes operam sem esta capacidade. | • Nenhum teste de carga/stress em CI implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de load/stress testing in ci com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | load/stress testing in CI adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | load/stress testing in CI padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | load/stress testing in CI é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C8-Q3: Em que medida Desempenho e Escalabilidade (autoscaling based on real demand) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services autoscaled`

**Contexto**

- **O que mede (what):** Serviços escalam automaticamente por CPU, latência ou profundidade de fila.
- **Por que importa (why):** Autoscaling alinha custo à demanda.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem autoscaling based on real demand implementado. As equipes operam sem esta capacidade. | • Nenhuma escalabilidade automática baseada em demanda real implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de autoscaling based on real demand com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | autoscaling based on real demand adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | autoscaling based on real demand padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | autoscaling based on real demand é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C8-Q4: Em que medida Desempenho e Escalabilidade (profiling in production) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services continuously profiled`

**Contexto**

- **O que mede (what):** Profiling always-on (ex., pyroscope, parca) roda em prod.
- **Por que importa (why):** Profiling em prod revela gargalos que usuários reais encontram.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem profiling in production implementado. As equipes operam sem esta capacidade. | • Nenhum profiling em produção implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de profiling in production com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | profiling in production adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | profiling in production padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | profiling in production é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C8-Q5: Em que medida Desempenho e Escalabilidade (capacity planning cadence) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `capacity reviews per year`

**Contexto**

- **O que mede (what):** Capacidade é revisada com projeções de crescimento.
- **Por que importa (why):** Planejamento previne migrações dolorosas em carga de pico.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem capacity planning cadence implementado. As equipes operam sem esta capacidade. | • Nenhuma cadência de planejamento de capacidade implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de capacity planning cadence com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | capacity planning cadence adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | capacity planning cadence padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | capacity planning cadence é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## P3-C9: FinOps e Otimização de Custos

**5 questões neste capability.**

### P3-C9-Q1: Em que medida FinOps e Otimização de Custos (cost allocation & showback) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% cost tagged to team`

**Contexto**

- **O que mede (what):** Todo recurso é etiquetado e atribuído a uma equipe.
- **Por que importa (why):** Showback cria ownership para custos.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cost allocation & showback implementado. As equipes operam sem esta capacidade. | • Nenhuma alocação de custos e showback implantados<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de cost allocation & showback com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | cost allocation & showback adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | cost allocation & showback padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | cost allocation & showback é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C9-Q2: Em que medida FinOps e Otimização de Custos (committed use / savings plans) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% eligible spend committed`

**Contexto**

- **O que mede (what):** Gasto compromissado é usado quando o uso é previsível.
- **Por que importa (why):** Compromissos reduzem o gasto em 20-50% com risco mínimo.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem committed use / savings plans implementado. As equipes operam sem esta capacidade. | • Nenhum plano de uso comprometido / economia implantado<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de committed use / savings plans com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | committed use / savings plans adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | committed use / savings plans padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | committed use / savings plans é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C9-Q3: Em que medida FinOps e Otimização de Custos (idle and unused resource cleanup) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `$/month saved by cleanup`

**Contexto**

- **O que mede (what):** Automação sinaliza e remove recursos ociosos.
- **Por que importa (why):** Limpeza é a atividade FinOps de maior alavancagem.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem idle and unused resource cleanup implementado. As equipes operam sem esta capacidade. | • Nenhuma limpeza de recursos ociosos e não utilizados implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de idle and unused resource cleanup com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | idle and unused resource cleanup adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | idle and unused resource cleanup padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | idle and unused resource cleanup é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C9-Q4: Em que medida FinOps e Otimização de Custos (rightsizing recommendations) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% rightsizing applied`

**Contexto**

- **O que mede (what):** Recomendações automatizadas impulsionam rightsizing contínuo.
- **Por que importa (why):** Rightsizing fecha a lacuna entre o provisionado e o necessário.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem rightsizing recommendations implementado. As equipes operam sem esta capacidade. | • Nenhuma recomendação de rightsizing implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de rightsizing recommendations com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | rightsizing recommendations adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | rightsizing recommendations padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | rightsizing recommendations é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

### P3-C9-Q5: Em que medida FinOps e Otimização de Custos (unit economics per product) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% products with $/user`

**Contexto**

- **O que mede (what):** Produtos acompanham custo por usuário, requisição ou transação.
- **Por que importa (why):** Economia unitária alinha decisões de engenharia e de negócio.

**Formato da resposta**

Escala Likert de 5 níveis (L0 a L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG, até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem unit economics per product implementado. As equipes operam sem esta capacidade. | • Nenhuma economia unitária por produto implantada<br>• Nenhuma política documentada<br>• Nenhum responsável atribuído |
| **L1** | Em Desenvolvimento | Implementação piloto de unit economics per product com <10% de cobertura de equipes e uso ad-hoc. | • Documentação do programa piloto<br>• <10% de cobertura de equipes<br>• Sem política formal |
| **L2** | Definido | unit economics per product adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Taxa de adoção medida de 25-50%<br>• Diretrizes de uso publicadas<br>• Materiais de onboarding existentes |
| **L3** | Gerenciado | unit economics per product padronizado em >75% das equipes com resultados medidos e governança. | • >75% de taxa de adoção medida<br>• KPIs rastreados mensalmente<br>• Revisões de governança em vigor |
| **L4** | Otimizando | unit economics per product é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% de taxa de adoção medida<br>• Loops automatizados de feedback por telemetria<br>• Programa de melhoria contínua |

---

## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P3** é a média das 9 capacidades.
- O resultado é exibido em escala 0-4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0 a L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
