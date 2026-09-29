# `survey-devs/scripts/`

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Developer Survey](../README.pt-br.md)

Scripts que calculam maturidade de IA dos desenvolvedores a partir do Developer Survey anônimo.

## Conteúdo

| Arquivo | Uso |
| --- | --- |
| [rubric.py](rubric.py) | Rubrica determinística em `DS-D2` a `DS-D8`. Mapeia respostas (de formulários em EN, PT-BR ou ES, via [../options.json](../options.json)) para scores. As bandas de score correspondem à rubrica v1 do survey. |
| [calculate_maturity.py](calculate_maturity.py) | Lê `survey-devs/responses-devs.json` e gera `output/developer-survey-maturity-<date>.json` com chaves `DS-D#`. |
| [generate_insights.py](generate_insights.py) | Gera `output/insights-developer-survey-<date>.md`. A seção 12 liga sinais do survey a perguntas v2. Inglês por padrão; use `--lang pt-br` ou `--lang es`. As tabelas de opções aparecem no idioma do relatório. |

## Uso

```bash
python3 survey-devs/scripts/calculate_maturity.py
python3 survey-devs/scripts/generate_insights.py
python3 survey-devs/scripts/generate_insights.py --lang pt-br
python3 survey-devs/scripts/generate_insights.py --lang es
```

Saídas de survey são contexto para relatórios v2. Elas nunca mudam scores v2.
