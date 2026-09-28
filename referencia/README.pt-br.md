# `referencia/`: material de referência

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

O framework v2 é o modelo de referência padrão. O material v1 continua arquivado.

| Caminho | Uso |
| --- | --- |
| [framework-v2.pt-br.md](framework-v2.pt-br.md) | Guia gerado do framework v2 com regras de pontuação, notas de escopo, crosswalk e referências. |
| [dimensoes/](dimensoes/) | Páginas geradas por dimensão para D1 a D9 em EN, PT-BR e ES. |
| [calculadora-pontuacao.pt-br.html](calculadora-pontuacao.pt-br.html) | Calculadora v2 trilíngue gerada, abrindo em português. No repositório, `calculadora-pontuacao.html` segue o idioma do navegador e `calculadora-pontuacao.es.html` abre em espanhol; cada pacote de idioma entrega a sua cópia como `calculadora-pontuacao.html`. Carregue `saida/scores.json`, ajuste pesos e metas, e veja nível, gap, prioridade, horizonte, risco de amplificação e estratégias. |
| [v1/calculadora-pontuacao.html](v1/calculadora-pontuacao.pt-br.html) | Calculadora v1 arquivada. |
| [exemplo-saida/](exemplo-saida/) | Saídas ilustrativas v2, incluindo 5 PDFs, PDF de comparação, planilha, scan de repositórios, telemetria, surveys e entradas do wizard. |
| [v1/](v1/) | Referências e exemplos v1 arquivados. |
| [branding/](branding/) | Orientação de marca e voz. |

A fonte da verdade da pontuação v2 é o engine determinístico e [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md). Não use páginas de pilar v1 arquivadas para novos assessments.

Use `make examples-v2` para regerar os exemplos ilustrativos. Use `make validate-docs` para checar helpers gerados e documentação dos pacotes.
