# `wizard/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Wizard](../README.md)

Scripts that support the Implementation Guide Wizard.

## Contents

| File | Purpose |
| --- | --- |
| [auto_fill_from_plano.py](auto_fill_from_plano.py) | Wizard Mode D. Reads the latest `saida/plano-capacitacao-*.md` and generates `implementation-guide-inputs.json` at the root. Supports `--lang en`, `--lang pt-br`, and `--lang es`. Fills 7 of the 11 fields from Learning Survey output and marks the rest as fill-in items. |

## Usage

```bash
python3 wizard/scripts/auto_fill_from_plano.py --lang en
```

Run it after `/plano-capacitacao` or after `python3 survey-learning/scripts/gerar_plano_capacitacao.py`. Then run `make pipeline` to refresh the 5 v2 PDFs.
