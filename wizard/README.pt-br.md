# `wizard/`: Wizard do Guia de Implementação (Parte 4 v2)

🌐 [English](README.md) · Português (Brasil)

**`WIZARD`** · _Parte 4 customizada_ · 📖 [🏠 Índice](../README.pt-br.md) · [« Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.pt-br.md) · Você está aqui

Esta pasta contém o wizard trilingue gerado e o template JSON usados para personalizar `saida/v2_implementation_guide.pdf`. O wizard roda offline e migra o armazenamento do navegador usado no v1.

> [!NOTE]
> Saída em todos os modos: `implementation-guide-inputs.json` na raiz do kit. `make pipeline` detecta automaticamente e mescla em `payload_v2.json`.

## Os 11 inputs

| # | Input | O que é |
| --- | --- | --- |
| 1 | `executive_steering_committee` | Sponsor, líder do programa, segurança, finanças, mudança e representantes Champions. |
| 2 | `tpo` | Technology Product Owner ou escritório do programa com autoridade de decisão. |
| 3 | `dimension_owners` | Uma linha por responsável, por exemplo `D4: nome, papel`. |
| 4 | `raci_matrix` | Atividades e atribuições R/A/C/I. |
| 5 | `communication_plan` | Público, canal, frequência e responsável. |
| 6 | `training_plan` | Coortes, formato, cadência e critérios. |
| 7 | `adkar_notes` | Notas de Awareness, Desire, Knowledge, Ability e Reinforcement. |
| 8 | `risk_register` | Tabela com Risk, Impact, Mitigation e Owner. |
| 9 | `quick_wins_w1_4` | Primeiros 30 dias. |
| 10 | `quick_wins_w5_8` | Semanas 5 a 8. |
| 11 | `quick_wins_w9_12` | Semanas 9 a 12. |

## Os 4 modos

### A. Wizard HTML standalone

```bash
open wizard/implementation-guide-wizard.html
```

- Gerado por `scripts/generate_v2_tools_html.py`.
- Seletor de idioma: EN, PT-BR e ES.
- Salva rascunhos em `localStorage`.
- Baixa `implementation-guide-inputs.json` com os 11 campos.
- Campos vazios continuam vazios e aparecem como `to fill with the client`; não existe fallback para exemplo.

### B. Template JSON editável

```bash
cp wizard/implementation-guide-inputs.template.json implementation-guide-inputs.json
code implementation-guide-inputs.json
```

O template gerado tem valores vazios e orientação em `_guide` para EN, PT-BR e ES.

### C. Conversa no Copilot Chat

Use `/wizard-implementacao` quando quiser que o Copilot colete os campos em conversa e salve o JSON depois da confirmação.

### D. Auto-fill a partir do plano do Learning Survey

```bash
python3 wizard/scripts/auto_fill_from_plano.py --lang pt-br
```

O Mode D lê o `saida/plano-capacitacao-*.md` mais recente, preenche 7 dos 11 campos a partir do plano de capacitação do Learning Survey e marca o restante como itens a preencher. Ele usa Champions ativos para o steering committee, calendário para comunicação, coortes para treinamento, notas ADKAR e quick wins.

## Arquivos

| Arquivo | Uso |
| --- | --- |
| [implementation-guide-wizard.html](implementation-guide-wizard.html) | Wizard visual standalone gerado. |
| [implementation-guide-wizard.pt-br.html](implementation-guide-wizard.pt-br.html) | Entrada em português. O seletor de idioma pode alternar idiomas. |
| [implementation-guide-inputs.template.json](implementation-guide-inputs.template.json) | Template JSON vazio gerado com `_guide`. |
| [scripts/auto_fill_from_plano.py](scripts/auto_fill_from_plano.py) | Mode D de auto-fill a partir da saída do Learning Survey. |

## Depois de preencher

```bash
ls implementation-guide-inputs.json
make pipeline
```

A Parte 4 v1 também lê o novo arquivo e ignora campos que não usa.

## Pular e reutilizar

- Pular é permitido. Campos vazios aparecem como `to fill with the client`.
- Você pode preencher apenas alguns dos 11 inputs e rodar `make pipeline` novamente.
- Rodar o wizard novamente sobrescreve apenas os campos salvos de novo.

## Documentação relacionada

- Skill orquestradora: [../.github/skills/wizard-implementacao/SKILL.md](../.github/skills/wizard-implementacao/SKILL.md)
- Como o JSON chega ao PDF: [../relatorios/scripts/wizard_inputs.py](../relatorios/scripts/wizard_inputs.py)
- Template v2 do guia de implementação: [../relatorios/templates/v2_implementation_guide.html.j2](../relatorios/templates/v2_implementation_guide.html.j2)
