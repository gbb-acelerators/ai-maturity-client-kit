# Exemplos de saída

🌐 [English](README.md) · Português (Brasil)

Todos os arquivos daqui são gerados por `python3 scripts/build_v2_examples.py` a partir de entradas ilustrativas: o mock `respostas.v2.json.example` (14 respondentes, Contoso Engineering), os mocks dos surveys complementares, repositórios fixture gerados na hora e `scripts/fixtures/copilot-usage-organization-28-day.mock.json`. Nada disso é dado real de cliente. Não edite estes arquivos à mão.

A raiz da pasta tem o exemplo em PT-BR. [en/](en/) e [es/](es/) têm os mesmos PDFs em inglês e espanhol. O exemplo v1 arquivado está em [v1/](v1/).

## Relatórios v2 (PDF)

| Arquivo | Conteúdo |
| --- | --- |
| `v2_assessment_summary.pdf` | Resultado geral, flags, heatmap por persona, checagem cruzada de evidências, contexto do Developer Survey, backlog, estratégias, referências |
| `v2_roadmap_g1.pdf` | G1: D1, D2, D9 |
| `v2_roadmap_g2.pdf` | G2: D3, D4, D5 |
| `v2_roadmap_g3.pdf` | G3: D6, D7, D8 |
| `v2_implementation_guide.pdf` | Governança, plano por fases conforme a prioridade, gestão da mudança, riscos vindos das flags, métricas de sucesso e os primeiros 90 dias |
| `comparacao-rodadas.pdf` | Comparação entre rodadas do exemplo v1 para o mock v2 (linha de base indicativa pela linhagem v1) |

Os guias de implementação em PT-BR e EN usam entradas do wizard preenchidas por `wizard/scripts/auto_fill_from_plano.py` a partir do mock do Learning and Growth Survey. O guia em ES não tem entradas do wizard e por isso mostra as marcações "a completar con el cliente": os scripts dos surveys só geram EN e PT-BR.

## Arquivos de dados

| Arquivo | Conteúdo |
| --- | --- |
| `scores.json`, `gaps.json`, `recomendacoes.json` | Saídas do engine (EN) |
| `payload_v2.json` | Payload dos relatórios (EN) |
| `repo-scan.json` | `scripts/scan_repos_ai_config.py` em 12 repositórios fixture (níveis RAMP [47]) |
| `telemetria.json` | `scripts/import_copilot_metrics.py` sobre o mock de métricas de uso do Copilot |
| `comparacao-rodadas.json` | Resultado de `scripts/compare_rounds.py` usado no PDF de comparação |
| `pontuacao-v2-EXEMPLO.xlsx` | Planilha auditável com fórmulas (PT-BR) |
| `maturidade-developer-survey-EXEMPLO.json`, `insights-developer-survey-EXEMPLO.md` | Saídas do Developer Survey (PT-BR), dimensões `DS-D2` a `DS-D8` |
| `plano-capacitacao-EXEMPLO.md` | Plano de capacitação do Learning and Growth Survey (PT-BR) |
| `implementation-guide-inputs-EXEMPLO.json` | Entradas do wizard preenchidas a partir do plano de capacitação (PT-BR) |

Grupos dos relatórios: G1 = D1, D2, D9; G2 = D3, D4, D5; G3 = D6, D7, D8.

## Arquivo v1

[v1/](v1/) mantém o layout e os exemplos v1 arquivados, do framework de 158 perguntas e 3 pilares.
