# `wizard/scripts/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Wizard](../README.es.md)

Scripts que dan soporte al Implementation Guide Wizard.

## Contenido

| Archivo | Propósito |
| --- | --- |
| [auto_fill_from_plan.py](auto_fill_from_plan.py) | Wizard Modo D. Lee el último `output/training-plan-*.md` y genera `implementation-guide-inputs.json` en la raíz. Soporta `--lang en`, `--lang pt-br` y `--lang es`. Llena 7 de los 11 campos desde la salida de Learning Survey y marca el resto como elementos para completar. |

## Uso

```bash
python3 wizard/scripts/auto_fill_from_plan.py --lang en
```

Ejecútalo después de `/training-plan` o después de `python3 survey-learning/scripts/generate_training_plan.py`. Luego ejecuta `make pipeline` para actualizar los 5 PDFs v2.
