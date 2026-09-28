# `relatorios/i18n/`

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Reports](../README.md)

String catalogs for localizing the 5 PDFs. Each file is a flat `key → translation` JSON.

## Contents

| File | Language | Lines (approx.) |
|---|---|---|
| [`en.json`](en.json) | English, **default** | base |
| [`pt-br.json`](pt-br.json) | Português (Brasil) | base |
| [`es.json`](es.json) | Español | base |

## How it works

The renderer (`render_reports.py`) loads the catalog matching `payload.locale` (`en`, `pt-br`, or `es`) and injects a `t()` function into the Jinja2 context:

```jinja2
<h1>{{ t('score_justification.title') }}</h1>
```

`payload.locale` is set from `respostas.json::metadata.language` (default: `en`; `"pt-BR"` and `"es"` are also accepted).

## Adding or changing strings

> [!IMPORTANT]
> All 3 languages must have **the same keys**. If you add a key to `en.json`, also add it to `pt-br.json` and `es.json` (even a provisional English value is better than `null`).

```bash
# Validate key parity
python3 -c "import json; a=set(json.load(open('relatorios/i18n/en.json'))); b=set(json.load(open('relatorios/i18n/pt-br.json'))); c=set(json.load(open('relatorios/i18n/es.json'))); print('missing pt-br:', a-b); print('missing es:', a-c)"
```

## Key convention

Hierarchical by context: `<file>.<section>.<element>`. Examples:

- `score_justification.title`
- `roadmap_part_pillar.section.h1_initiatives`
- `common.priority.p0`
