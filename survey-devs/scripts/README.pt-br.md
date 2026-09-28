# `survey-devs/scripts/`

🌐 [English](README.md) · Português (Brasil)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Developer Survey](../README.pt-br.md)

Scripts que calculam maturidade de IA dos desenvolvedores a partir do Developer Survey anônimo.

## Conteúdo

| Arquivo | Uso |
| --- | --- |
| [rubric.py](rubric.py) | Rubrica determinística em `DS-D2` a `DS-D8`. Mapeia respostas (de formulários em EN, PT-BR ou ES, via [../options.json](../options.json)) para scores. As bandas de score correspondem à rubrica v1 do survey. |
| [calcular_maturidade.py](calcular_maturidade.py) | Lê `survey-devs/respostas-devs.json` e gera `saida/maturidade-developer-survey-<date>.json` com chaves `DS-D#`. |
| [gerar_insights.py](gerar_insights.py) | Gera `saida/insights-developer-survey-<date>.md`. A seção 12 liga sinais do survey a perguntas v2. Inglês por padrão; use `--lang pt-br` ou `--lang es`. As tabelas de opções aparecem no idioma do relatório. |

## Uso

```bash
python3 survey-devs/scripts/calcular_maturidade.py
python3 survey-devs/scripts/gerar_insights.py
python3 survey-devs/scripts/gerar_insights.py --lang pt-br
python3 survey-devs/scripts/gerar_insights.py --lang es
```

Saídas de survey são contexto para relatórios v2. Elas nunca mudam scores v2.
