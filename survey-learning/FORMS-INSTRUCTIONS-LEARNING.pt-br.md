# Como criar o Microsoft Forms para o Learning & Growth Survey

🌐 [English](FORMS-INSTRUCTIONS-LEARNING.md) · Português (Brasil) · [Español](FORMS-INSTRUCTIONS-LEARNING.es.md)

**`🅲️ SURVEY-LEARNING`** · _identificado_ · 📖 [🏠 Índice](../README.pt-br.md) · [« Survey-devs](../survey-devs/FORMS-INSTRUCTIONS-DEVS.pt-br.md) · Você está aqui · [» Wizard](../wizard/README.md)

> [!WARNING]
> Diferente dos outros 2 surveys, este é **IDENTIFICADO** (nome + email obrigatórios). É 32 perguntas em 7 seções para construir o **roadmap de capacitação personalizado** da equipe: workshops, cohorts, Champions Network, mentoria. Tempo estimado por dev: **5-8 min**.

**Diferente dos outros 2 surveys:**

- Assessment principal: maturidade organizacional (Likert L0-L4 declarada por liderança)
- Developer Survey: comportamento real ANÔNIMO
- **Este Learning Survey: roadmap de capacitação IDENTIFICADO**: precisa nome+email para convidar pessoas certas para workshops certos

---

## ⚠️ Por que IDENTIFICADO (não anônimo)?

Para gerar valor acionável, este survey **precisa saber quem é quem**:

- Convocar **as pessoas certas** para cada workshop (10 inscritos pré-validados é melhor que "70% mostraram interesse")
- Formar **Champions Network** com nomes (não anônimos)
- Mapear **mentor↔mentee pairs** (precisa nome dos dois lados)
- Atribuir **dono** dos quick wins identificados

**Trade-off honesto:** algumas perguntas (ex.: "qual seu nível em DS-D8 Security?") podem ser respondidas com pouca honestidade se devs sentirem julgamento. Por isso:

- Liderança deve **comunicar claramente**: "respostas usadas para CAPACITAR, não para AVALIAR performance"
- Não usar respostas em performance reviews
- Compartilhar plano consolidado com toda a equipe (transparência)

Se sua organização preferir **anonimato puro**: rode o **Developer Survey** (`survey-devs/`) em paralelo e use a rubrica determinística como "termômetro objetivo".

---

## 📋 Os 7 temas cobertos

| # | Seção | Foco | Q |
|---|---|---|---|
| **L1** | Identificação | Nome, email, cargo, time | 4 |
| **L2** | Auto-percepção de maturidade | Auto-avaliação L0-L4 nas 7 dimensões D2-D8 | 7 |
| **L3** | Onde quer crescer | Top 3 dimensões prioritárias (próximos 6 meses) + por quê | 2 |
| **L4** | Tópicos específicos | Copilot, Foundry, práticas (TDD/SDD), agents, segurança: checkbox | 5 |
| **L5** | Formato e cadência | Workshop hands-on, cohort, self-paced, horários, tempo/semana | 4 |
| **L6** | Champions e mentoria | Quer ser Champion? Mentoria? Quem é referência? | 5 |
| **L7** | Barreiras e Wishlist | O que impede + workshops desejados + palestrantes | 5 |
| | | **TOTAL** | **32** |

---

## 🛠️ Como criar o Forms (passo a passo)

### Passo 1 · Criar formulário

1. Acesse <https://forms.office.com> → **+ New Form**
2. Título: `Learning & Growth IA: O que você quer aprender nos próximos 6 meses?`
3. Subtítulo (cole):

```text
Survey de 5-8 min sobre seu plano de capacitação em IA.

⚠️ IDENTIFICADO: vamos usar seu nome+email para CONVIDAR você para os
workshops/cohorts certos. As respostas individuais NÃO serão compartilhadas
publicamente: apenas insights agregados + listas de inscritos por workshop.

Resultado: plano de capacitação personalizado + cohorts + Champions Network.
```

### Passo 2 · ⚠️ CONFIGURAR como IDENTIFICADO (não anônimo)

**Settings (⚙️):**

| Setting | Valor |
|---|---|
| **Anonymous responses** | ☐ **DESMARCADO** (queremos identificação) |
| **Who can respond** | "Only people in my organization" (recomendado) |
| **One response per person** | ☑ MARCADO (1 por dev) |
| **Accept responses** | ☑ MARCADO |
| **Customize thank you message** | "Obrigado! Você receberá convites de workshops baseados nas suas respostas." |

> 🔍 **Diferente do Developer Survey** (`survey-devs/FORMS-INSTRUCTIONS-DEVS.md`): aquele você marca Anonymous ON, este você deixa OFF.

### Passo 3 · Criar 7 seções

```text
Section 1: L1: Identificação                  (4 questões)
Section 2: L2: Auto-percepção (D2-D8)         (7 questões)
Section 3: L3: Onde quer crescer              (2 questões)
Section 4: L4: Tópicos específicos            (5 questões)
Section 5: L5: Formato e cadência             (4 questões)
Section 6: L6: Champions e mentoria           (5 questões)
Section 7: L7: Barreiras e Wishlist           (5 questões)
```

### Passo 4 · Adicionar as 32 perguntas

Use o banco no idioma dos respondentes como fonte de copy/paste: português [`question-bank-learning.pt-br.md`](question-bank-learning.pt-br.md), inglês [`question-bank-learning.md`](question-bank-learning.md) ou espanhol [`question-bank-learning.es.md`](question-bank-learning.es.md).

**Para cada pergunta:**

1. Tipo:
   - `choice` (Single answer) → **Choice**
   - `multi` (Multiple answers) → **Choice** com Multiple answers MARCADO
   - `text-short` (Short Text 1 linha) → **Short answer**
   - `text` (Long Text) → **Long answer**

2. **TÍTULO inicia SEMPRE com o ID + dois pontos**:

   ```text
   L4-Q1: Quais tópicos de GitHub Copilot você quer dominar?
   ```

3. **Required**: marque **L1-Q1 (nome) + L1-Q2 (email)** como required. Demais opcionais (devs podem pular).

### Passo 5 · Customizar L1-Q4 (lista de squads)

A pergunta L1-Q4 ("Time / Squad") tem placeholder `[Lista a customizar pela org]`: substitua pelos nomes reais dos squads da sua organização. Exemplo:

```text
- Squad Pagamentos
- Squad Onboarding
- Squad Plataforma
- SRE Core
- Data Platform
- Outro / não pertenço a um squad fixo
```

### Passo 6 · Compartilhar

1. **+ Send / Collect responses** → **Link**
2. Compartilhar com **TODOS os devs**:
   - Email do líder de engenharia: "Nas próximas 2 semanas, queremos ouvir o que vocês querem aprender em IA, survey de 5-8 min, IDENTIFICADO. Resultado: plano de capacitação personalizado."
   - Slack/Teams canal #engineering
   - All-hands (apresentar o link)

3. **Deadline:** 2 semanas. Lembrete D+7 e D+12.

### Passo 7 · Acompanhar respostas

- Aba **Responses** mostra contagem em tempo real
- Recomendado: **mínimo 5 devs**, ideal **>50% do time**
- Como é identificado, você consegue ver "X de Y devs ainda não responderam" e fazer 1-on-1

### Passo 8 · Exportar

1. **Responses → Open in Excel**
2. Salvar como **`survey-learning-responses.xlsx`**
3. Mover para **raiz do `kit-cliente/`**
4. Verificar: colunas D (Email) e E (Name) devem estar PREENCHIDAS

### Passo 9 · Analisar com o kit

No Copilot Chat (modo Agent):

```text
/import-survey-learning
```

Gera `survey-learning/responses-learning.json` (estruturado).

```text
/training-plan
```

Gera `output/training-plan-<DATE>.md` (em **inglês por padrão**; o script aceita `--lang pt-br` para português (Brasil) e `--lang es` para espanhol) com:

- Top 10 tópicos demandados (com lista de inscritos pré-validados)
- Cohorts sugeridos por dimensão D2-D8
- Champions Network identificados (3 tiers)
- Mentor ↔ mentee pairs
- Calendário de workshops (próximos 90 dias)
- Barreiras priorizadas
- 5 ações priorizadas (impacto × facilidade)
- Conexão com /insights-developer-survey + /calculate-scores

### Passo 10 · ⭐ Auto-fill do wizard (Mode D)

Depois de gerar o plano, ao rodar `/implementation-wizard`, o Copilot Agent **detecta automaticamente** o `output/training-plan-*.md` e oferece **Mode D: Auto-fill** que preenche **7 dos 11 campos** do wizard automaticamente:

| Input do wizard (Parte 4 do PDF) | Vem de |
|---|---|
| `executive_steering_committee` | Champions Network "ativos" |
| `communication_plan` | Calendário de workshops |
| `training_plan` | Cohorts por dimensão |
| `adkar_notes` | Workshops top 5 (Knowledge stage) |
| `quick_wins_w1_4` / `quick_wins_w5_8` / `quick_wins_w9_12` | Calendário 90 dias |

Você preenche manualmente: **escritório do programa (TPO)**, **RACI**, **responsáveis por dimensão** e o **registro de riscos do cliente** (o Learning Survey não cobre esses campos). Campos vazios aparecem como "a preencher com o cliente" no guia de implementação.

**Economia estimada:** 30-45 min de wizard manual. E os dados vêm do seu time.

### Passo 11 · Re-renderizar PDFs com plano + wizard auto-fill

```text
/generate-report
```

A skill detecta:

- ✅ `implementation-guide-inputs.json` (do wizard Mode D auto-fill) → popula Parte 4 com seus Champions e workshops
- ✅ `output/training-plan-*.md` (deste survey) → enriquece roadmap_part4.pdf
- ✅ `output/insights-developer-survey-*.md` (se você rodou) → cross-references no apêndice
- ✅ `output/developer-survey-maturity-*.json` (se você rodou) → score_justification.pdf inclui "maturity vs declared"

**Output:** 5 PDFs production-quality com dados REAIS do learning survey embarcados.

---

## 🅱️ Caminho alternativo: Excel/SharePoint direto

Para times pequenos (3-5 devs):

```bash
cp survey-learning/template-export-forms-learning.xlsx survey-learning-responses.xlsx
# Limpar linhas de mocks (linhas 2-6)
# Subir SharePoint com edit
# Cada dev preenche uma linha (incluindo nome+email)
# Baixar e mover para raiz
/import-survey-learning + /training-plan
```

---

## 💡 Boas práticas

### Compromisso de uso ético dos dados

Comunique antes de lançar:

> "Suas respostas serão usadas para: (1) construir nosso roadmap de capacitação, (2) convidar você para workshops específicos que pediu, (3) formar Champions Network. **NÃO** serão usadas para performance review, comparação entre devs, ou compartilhadas com clientes externos."

### Privacidade e proteção de dados (LGPD / GDPR)

Este survey trata dados pessoais (nome, e-mail, cargo, squad, autoavaliação). Combine os pontos abaixo com o time de privacidade ou jurídico antes do lançamento; esta checklist não é aconselhamento jurídico.

- **Finalidade e base legal:** documente por que os dados são coletados (plano de capacitação, convites, Champions Network) e a base legal escolhida pelo seu time.
- **Aviso de privacidade:** inclua no formulário o aviso de `question-bank-learning.pt-br.md` (passo 3), com controlador, acesso, retenção e contato preenchidos.
- **Minimização:** colete só as perguntas de identificação do L1; não acrescente campos como matrícula ou gestor.
- **Armazenamento e acesso:** mantenha `survey-learning-responses.xlsx`, `survey-learning/responses-learning.json` e `output/training-plan-*.md` em armazenamento gerenciado com acesso restrito. Esses caminhos estão no `.gitignore`; nunca faça commit deles.
- **Apêndice só para liderança:** o apêndice de respondentes do plano tem nomes e e-mails. Compartilhe só com quem envia os convites.
- **Retenção e exclusão:** exclua as respostas do Forms, o `.xlsx`, o JSON e o apêndice do plano ao fim do prazo de retenção.
- **Pedidos individuais:** defina um responsável por pedidos de acesso, correção e exclusão.

### Cadência de relançamento

- **A cada 6 meses** ou após eventos grandes (rollout Copilot, mudança de stack, etc.)
- **Compare evoluções**: dev que estava L1 em DS-D5 e agora se auto-avalia L3? Champion natural

### Transparência do plano

- Apresentar o `training-plan-DATA.md` em all-hands
- Pessoas que pediram workshop X recebem convite: fechar o loop
- Champions identificados são reconhecidos publicamente (com consentimento)

---

## 🆘 Troubleshooting

| Problema | Solução |
|---|---|
| Skill não detecta arquivo | Mover para raiz do `kit-cliente/` |
| Email/Name vazios em algumas linhas | Forms config OFF Anonymous + L1-Q1/Q2 required |
| Headers não reconhecidos | Garantir que cada pergunta começa com `L[1-7]-Q\d+:` |
| Dev recusou identificar | Aceitar resposta parcial; redirecionar para `survey-devs` (anônimo) |
| Baixa adesão (< 50% do time) | Líder de engenharia deve ENDORSE explicitamente |

---

## 📚 Referências

- **As 32 perguntas formatadas:** [`question-bank-learning.pt-br.md`](question-bank-learning.pt-br.md) (português), [`question-bank-learning.md`](question-bank-learning.md) (inglês), [`question-bank-learning.es.md`](question-bank-learning.es.md) (espanhol)
- **Template Excel pronto:** [`template-export-forms-learning.xlsx`](template-export-forms-learning.xlsx)
- **JSON estruturado de exemplo:** [`mock-responses-learning.json`](mock-responses-learning.json)
- **Skill de import:** [`../.github/skills/import-survey-learning/SKILL.md`](../.github/skills/import-survey-learning/SKILL.md)
- **Skill de plano:** [`../.github/skills/training-plan/SKILL.md`](../.github/skills/training-plan/SKILL.md)
- **Cross-reference com Developer Survey** (anônimo): [`../survey-devs/`](../survey-devs/README.pt-br.md)

---

**Versão:** 1.0 · **Data:** 2026-05-08

---

## Travou em algum desses passos?

<details>
<summary><strong>FAQ: dúvidas comuns no Learning & Growth Survey (identificado)</strong></summary>

| Sintoma | Causa provável | Como resolver |
|---|---|---|
| Excel chega sem nome/email | **Anonymous responses** está marcado (este survey precisa ser identificado) | Settings do Forms → ❌ DESmarcar **Anonymous responses** |
| Como uso o plano para convidar pessoas? | O plano traz nome+email por workshop | Copie lista de inscritos do markdown → cole em Outlook/Teams meeting invite |
| Champions Network está vazio no plano gerado | Ninguém respondeu "sim" em L6-Q1 | Sem Champions auto-declarados: use ranking por dimensão como proxy |
| Cohorts estão vazios em algumas dimensões | Menos de 3 respondentes por dimensão | Peça reforço na campanha ou aceite cohorts menores |
| Posso re-rodar o plano se mais respostas chegarem? | Sim, é idempotente | Re-exporte Excel → `/import-survey-learning` → `/training-plan` |

</details>

---

## Continuar a leitura

| ← ANTERIOR | PRÓXIMO → |
|:---|---:|
| **[Developer Survey (anônimo)](../survey-devs/FORMS-INSTRUCTIONS-DEVS.pt-br.md)** | **[Wizard: Parte 4](../wizard/README.md)** |
| 75 perguntas anônimas: Copilot, agentes, governança. | Personalizar Steering Committee, RACI, ADKAR, Quick Wins do PDF executivo. |

↑ [Voltar ao Índice do kit](../README.pt-br.md)
