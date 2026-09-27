# Guía Paso a Paso · Edición Español

> Walkthrough completo para ejecutar el kit AI Maturity Assessment desde cero hasta los 5 PDFs finales.

🏠 [Volver al README](README.md) · 🌐 [Sitio](https://paulasilvatech.github.io/ai-maturity-client-kit/es/) · 🇧🇷 [PT-BR](../GUIA-PASSO-A-PASSO.md) · 🇺🇸 [EN](../kit-en/STEP-BY-STEP.md)

---

## Prerequisitos

| Requisito | Versión | Verificar con |
|---|---|---|
| Python | 3.10+ | `python3 --version` |
| VS Code | última | `code --version` |
| GitHub Copilot Chat | Pro / Business / Enterprise | Ícono en el sidebar |
| Paquetes pip | `jinja2`, `weasyprint`, `openpyxl` | `pip list \| grep -E "jinja2\|weasy\|openpyxl"` |

En **macOS**, WeasyPrint además necesita `brew install pango`. En **Linux/WSL**: `sudo apt install libpango-1.0-0 libpangoft2-1.0-0`.

> [!TIP]
> Ejecuta `make smoke` después de extraer el ZIP. Valida cada prerequisito en 5 segundos.

## Paso 1 — Obtener el kit

Descarga el ZIP desde el sitio, extraelo y abre la carpeta extraida en VS Code.

```bash
make install-deps   # instala jinja2 + weasyprint + openpyxl
make smoke          # valida el entorno
```

Output esperado: `✅ Smoke test passed (X checks).`

## Paso 2 — Elige tu fuente de datos

Tienes **3 opciones** para llenar las 158 preguntas del framework:

### Opción A — Datos de ejemplo (más rápido, ~3 min)

```bash
cp respostas.json.example respostas.json
```

Usa el ficticio **Cliente Exemplo S.A.** con 46 respuestas pre-llenadas. Ideal para validar el pipeline completo antes de ejecutarlo en producción.

### Opción B — Llenado manual

Edita `respostas.json` y define `level` (0 a 4) y `evidence` para cada pregunta. Salta las preguntas que no puedas responder; el algoritmo solo usa las respondidas.

### Opción C — Microsoft Forms (multi-respondente)

1. Publica los 3 forms HTML en `formularios/` como 3 encuestas de Microsoft Forms (ver `INSTRUCCIONES-FORMS.md`).
2. Recolecta respuestas del liderazgo (3-5 respondentes recomendados).
3. Exporta el Excel consolidado a la raíz del workspace como `respostas-forms.xlsx`.
4. Ejecuta `/importar-respostas-excel` en Copilot Chat para auto-agregar a `respostas.json`.

## Paso 3 — Ejecuta el pipeline

Abre VS Code → Copilot Chat → cambia a **modo Agent** (dropdown junto al ícono).

### Camino más fácil: agente concierge

```
@ai-maturity-assistant
```

El agente lee el estado del workspace y pregunta una cosa a la vez, invocando cada skill en el orden correcto. Recomendado para primera vez.

### Camino power user: orquestador completo

```
/pipeline-completo
```

Ejecuta los 6 pasos end-to-end (auto-detecta Excel e inputs del wizard).

### Camino manual: una skill a la vez

```
/calcular-scores
/gap-analysis
/recomendar-estrategias
/wizard-implementacao
/gerar-relatorio
```

Útil cuando quieres inspeccionar cada JSON intermedio antes de continuar.

## Paso 4 — Inspecciona los outputs

Todo va a `saida/`:

| Archivo | Propósito |
|---|---|
| `scores-<FECHA>.json` | Scores por capability / pilar / global |
| `gaps-<FECHA>.json` | Gaps priorizados P0 / P1 / P2 / P3 |
| `recomendacoes-<FECHA>.json` | Estrategias S1-S7 mapeadas a gaps + tecnologías |
| `pontuacao-preenchida-<FECHA>.xlsx` | Excel auditable con fórmulas en vivo |
| **5 PDFs** | Score Justification + 3 Pillar Roadmaps + Implementation Guide |

Los PDFs son **~2 MB en total**, listos para presentar al board.

## Paso 5 — Personaliza el Implementation Guide (PDF Parte 4)

El PDF del Implementation Guide tiene 9 inputs específicos del cliente (miembros del Steering Committee, TPO, RACI, plan de comunicaciones, plan de capacitación, notas ADKAR, 3 olas de quick-wins). Llénalos de 3 formas:

- **Wizard HTML**: abre `wizard/implementation-guide-wizard.html` en cualquier navegador, llena, descarga el JSON.
- **Template JSON**: copia `wizard/implementation-guide-inputs.template.json` y edita.
- **Chat**: ejecuta `/wizard-implementacao` y responde en conversación.

El Learning & Growth Survey auto-llena 6 de los 9 inputs si ejecutaste la encuesta C primero.

## Troubleshooting

> [!WARNING]
> **`/calcular-scores` no aparece cuando escribo `/`**
>
> No estás en modo Agent. Haz clic en el dropdown junto al ícono de Copilot y elige **Agent**. Luego recarga la ventana (`Cmd+Shift+P` → "Developer: Reload Window").

> [!WARNING]
> **Error de WeasyPrint en macOS: "no library called pango"**
>
> `brew install pango glib gobject-introspection libffi`

> [!WARNING]
> **Los scores se ven bajos / muchos "sin respuesta"**
>
> Umbral de cobertura: 40+ respondidas = OK, 25-39 = WARNING (preliminar), <25 = BLOQUEADO. Revisa `saida/scores-<FECHA>.json::metadata::coverage`.

## ¿Atascado en algún paso?

Contacta a Paula Silva en [LinkedIn](https://linkedin.com/in/paulanunes).

## Continuar leyendo

| ⬅ Anterior          | Siguiente ➡                                          |
| :------------------ | ----------------------------------------------------: |
| [🏠 README](README.md) | [📝 Instrucciones Forms](INSTRUCCIONES-FORMS.md) |

---

**Paula Silva** — Global Developer Solutions Advisor | [LinkedIn](https://linkedin.com/in/paulanunes)
