# `docs/`: mini-sitio (GitHub Pages)

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../README.es.md)

Sitio estático que presenta el kit. El contenido de la landing está centralizado en [`content.json`](content.json) y renderizado por [`app.js`](app.js), con tres rutas públicas:

| Ruta | Idioma | Shell |
| --- | --- | --- |
| `/` | PT-BR | [`index.html`](index.html) |
| `/en/` | English | [`en/index.html`](en/index.html) |
| `/es/` | Español | [`es/index.html`](es/index.html) |

## URL pública

```text
https://paulasilvatech.github.io/ai-maturity-client-kit/
```

## Arquitectura

| Archivo | Propósito |
| --- | --- |
| [`content.json`](content.json) | Fuente única para texto en PT-BR, EN y ES, incluidos hero, pipeline, tarjetas, FAQ, skills y descargas |
| [`app.js`](app.js) | Renderizador estático: carga el JSON, elige el idioma desde la ruta y construye la página |
| [`index.html`](index.html) | Shell PT-BR con autodetección del idioma del navegador |
| [`en/index.html`](en/index.html) | Shell EN |
| [`es/index.html`](es/index.html) | Shell ES |
| [`styles.css`](styles.css) | CSS compartido con tokens paulasilva-ms |

## Idioma automático

La ruta `/` usa el idioma del navegador para redirigir a `/en/` o `/es/` cuando corresponde. PT-BR sigue siendo el valor predeterminado para esta ruta.

El selector PT · EN · ES guarda la elección en `localStorage`, así que las visitas futuras respetan la última selección.

## Edición de contenido

Edita solo [`content.json`](content.json) para cambiar textos y traducciones. Evita editar a mano los tres archivos HTML, son shells mínimos.

Valida el JSON antes de publicar:

```bash
python3 -m json.tool docs/content.json >/dev/null
```

## Vista previa local

El sitio carga `content.json` mediante `fetch`, así que usa un servidor local:

```bash
cd docs
python3 -m http.server 8000
# abre http://localhost:8000
```

No se recomienda abrir `index.html` directamente con `file://`, porque los navegadores bloquean `fetch()` para archivos locales.

## Descargas públicas con un repo privado

Sí, el repositorio puede seguir privado mientras el sitio sea público, siempre que GitHub Pages esté habilitado como público en el plan o la organización.

El detalle importante: los assets de GitHub Releases en un repositorio privado requieren autenticación. Por eso el workflow de Pages construye los ZIPs y los publica dentro del artefacto del sitio:

```text
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-pt.zip
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip
https://paulasilvatech.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip
```

Estos links siguen públicos con el sitio, incluso si el repositorio vuelve a ser privado.

Idiomas de los paquetes: cada ZIP incluye su idioma bajo los nombres de archivo base. El ZIP PT incluye las copias en portugués (`*.pt-br.md`, `*.pt-br.html`), el ZIP ES las copias en español (`*.es.md`, `*.es.html`) y el ZIP EN los docs en inglés; los ZIPs EN y ES agregan los quickstarts `kit-en/` o `kit-es/` en la raíz. Los bancos de preguntas y la especificación v2 se incluyen en los tres idiomas en cada ZIP. Los informes generados usan inglés por defecto en cada paquete (configura `metadata.language` como `"pt-BR"` o `"es"` para cambiarlo).

## Deploy

El workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml):

1. Hace checkout del repositorio.
2. Construye los tres ZIPs en `docs/downloads/`.
3. Sube la carpeta `docs/` como artefacto de GitHub Pages.
4. Publica el sitio.

Cualquier push que toque `docs/**` o el workflow de Pages dispara un nuevo deploy.

## Branding

Tokens MS de 4 colores aplicados mediante variables CSS:

- `--c-blue: #00A4EF`
- `--c-green: #7FBA00`
- `--c-yellow: #FFB900`
- `--c-red: #F25022`

Logo SVG inline, Inter + JetBrains Mono vía Google Fonts y modo oscuro automático mediante `prefers-color-scheme`.
