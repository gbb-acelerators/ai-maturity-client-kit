# `relatorios/i18n/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Informes](../README.es.md)

Catálogos de cadenas para localizar los 5 PDFs. Cada archivo es un JSON plano `key → translation`.

## Contenido

| Archivo | Idioma | Líneas (aprox.) |
|---|---|---|
| [`en.json`](en.json) | Inglés, **predeterminado** | base |
| [`pt-br.json`](pt-br.json) | Português (Brasil) | base |
| [`es.json`](es.json) | Español | base |

## Cómo funciona

El renderizador (`render_reports.py`) carga el catálogo que coincide con `payload.locale` (`en`, `pt-br` o `es`) e inyecta una función `t()` en el contexto de Jinja2:

```jinja2
<h1>{{ t('score_justification.title') }}</h1>
```

`payload.locale` se configura desde `respostas.json::metadata.language` (predeterminado: `en`; también se aceptan `"pt-BR"` y `"es"`).

## Agregar o cambiar cadenas

> [!IMPORTANT]
> Los 3 idiomas deben tener **las mismas claves**. Si agregas una clave a `en.json`, agrégala también a `pt-br.json` y `es.json` (incluso un valor provisional en inglés es mejor que `null`).

```bash
# Validar paridad de claves
python3 -c "import json; a=set(json.load(open('relatorios/i18n/en.json'))); b=set(json.load(open('relatorios/i18n/pt-br.json'))); c=set(json.load(open('relatorios/i18n/es.json'))); print('missing pt-br:', a-b); print('missing es:', a-c)"
```

## Convención de claves

Jerárquica por contexto: `<file>.<section>.<element>`. Ejemplos:

- `score_justification.title`
- `roadmap_part_pillar.section.h1_initiatives`
- `common.priority.p0`
