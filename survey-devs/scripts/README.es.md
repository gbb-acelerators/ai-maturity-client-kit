# `survey-devs/scripts/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Developer Survey](../README.es.md)

Scripts que calculan la madurez de IA de desarrolladores a partir del Developer Survey anónimo.

## Contenido

| Archivo | Propósito |
| --- | --- |
| [rubric.py](rubric.py) | Rúbrica determinística en `DS-D2` a `DS-D8`. Mapea respuestas (desde Forms en EN, PT-BR o ES, mediante [../options.json](../options.json)) a puntajes. Las bandas de puntaje coinciden con la rúbrica de encuesta v1. |
| [calcular_maturidade.py](calcular_maturidade.py) | Lee `survey-devs/respostas-devs.json` y genera `saida/maturidade-developer-survey-<date>.json` con claves `DS-D#`. |
| [gerar_insights.py](gerar_insights.py) | Genera `saida/insights-developer-survey-<date>.md`. La sección 12 conecta señales de encuesta con preguntas v2. Inglés por defecto; pasa `--lang pt-br` o `--lang es`. Las tablas de opciones se muestran en el idioma del informe. |

## Uso

```bash
python3 survey-devs/scripts/calcular_maturidade.py
python3 survey-devs/scripts/gerar_insights.py
python3 survey-devs/scripts/gerar_insights.py --lang pt-br
python3 survey-devs/scripts/gerar_insights.py --lang es
```

Las salidas de encuestas son contexto para informes v2. Nunca cambian los puntajes v2.
