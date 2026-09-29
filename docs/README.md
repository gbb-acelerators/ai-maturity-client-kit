# `docs/`: Mini-site (GitHub Pages)

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

📖 **Navigation:** [🏠 Index](../README.md)

Static site that presents the kit. Landing content is centralized in [`content.json`](content.json) and rendered by [`app.js`](app.js), with three public routes:

| Route | Language | Shell |
| --- | --- | --- |
| `/` | PT-BR | [`index.html`](index.html) |
| `/en/` | English | [`en/index.html`](en/index.html) |
| `/es/` | Español | [`es/index.html`](es/index.html) |

## Public URL

```text
https://paulasilvatech.github.io/ai-maturity-client-kit/
```

## Architecture

| File | Purpose |
| --- | --- |
| [`content.json`](content.json) | Single source for PT-BR, EN, and ES text, including hero, pipeline, cards, FAQ, skills, and downloads |
| [`app.js`](app.js) | Static renderer: loads the JSON, picks the language from the route, and builds the page |
| [`index.html`](index.html) | PT-BR shell with browser language auto-detection |
| [`en/index.html`](en/index.html) | EN shell |
| [`es/index.html`](es/index.html) | ES shell |
| [`styles.css`](styles.css) | Shared CSS with paulasilva-ms tokens |

## Automatic language

The `/` route uses the browser language to redirect to `/en/` or `/es/` when appropriate. PT-BR remains the default for this route.

The PT · EN · ES selector stores the choice in `localStorage`, so future visits respect the last selection.

## Editing content

Edit only [`content.json`](content.json) to change text and translations. Avoid hand-editing the three HTML files; they are minimal shells.

Validate the JSON before publishing:

```bash
python3 -m json.tool docs/content.json >/dev/null
```

## Local preview

The site loads `content.json` through `fetch`, so use a local server:

```bash
cd docs
python3 -m http.server 8000
# open http://localhost:8000
```

Opening `index.html` directly via `file://` is not recommended, because browsers block `fetch()` for local files.

## Public downloads with a private repo

Yes, the repository can stay private while the site is public, as long as GitHub Pages is enabled as public in the plan or organization.

The important detail: GitHub Releases assets in a private repository require authentication. That is why the Pages workflow builds the ZIPs and publishes them inside the site artifact itself:

```text
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-pt.zip
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip
```

These links stay public with the site, even if the repository goes back to private.

Package languages: each ZIP ships its language under the base file names. The PT ZIP ships the Portuguese copies (`*.pt-br.md`, `*.pt-br.html`), the ES ZIP the Spanish copies (`*.es.md`, `*.es.html`) and the EN ZIP the English docs, so every ZIP has the same file and folder names. The question banks and the v2 spec ship in the three languages in every ZIP. Generated reports default to English in every package (set `metadata.language` to `"pt-BR"` or `"es"` to change it).

## Deploy

The workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml):

1. Checks out the repository.
2. Builds the three ZIPs in `docs/downloads/`.
3. Uploads the `docs/` folder as the GitHub Pages artifact.
4. Publishes the site.

Any push that touches `docs/**` or the Pages workflow triggers a new deploy.

## Branding

MS 4-color tokens applied through CSS variables:

- `--c-blue: #00A4EF`
- `--c-green: #7FBA00`
- `--c-yellow: #FFB900`
- `--c-red: #F25022`

Inline SVG logo, Inter + JetBrains Mono via Google Fonts, and automatic dark mode via `prefers-color-scheme`.
