# Cómo crear el Microsoft Forms para el AI Maturity Assessment

🌐 [English](INSTRUCOES-FORMS.md) · [Português (Brasil)](INSTRUCOES-FORMS.pt-br.md) · Español

**`🅰️ ASSESSMENT`** · 📖 [🏠 Índice](../README.es.md) · [« Guía paso a paso](../../GUIA-PASSO-A-PASSO.es.md) · Estás aquí · [» Survey-devs](../../survey-devs/INSTRUCOES-FORMS-DEVS.es.md)

> [!TIP]
> Esta guía muestra **3 caminos** para crear y usar Microsoft Forms con las 158 preguntas. Elige el que mejor se ajuste al tiempo disponible y al perfil técnico del equipo.

---

## ⚖️ Comparación rápida de los 3 caminos

| Camino | Tiempo de configuración | Esfuerzo | Cuándo usarlo |
|---|---|---|---|
| **A. Forms manual completo** | 4-6 horas | Alto (crear 158 preguntas) | Quieres una experiencia Forms 100% nativa, con secciones y branding |
| **B. Forms liviano (1 capability piloto)** | 30 minutos | Bajo | PoC o validación con pocas personas encuestadas antes de escalar |
| **C. Directamente en Excel/SharePoint** ⭐ | 5 minutos | Mínimo | **Recomendado**: usa la plantilla Excel que viene con el kit y evita 4 h de configuración |

---

## 🅰️ Camino A: Forms manual completo (158 preguntas)

### Paso 1 · Crear Forms

1. Ve a <https://forms.office.com> (inicia sesión con tu cuenta Microsoft 365)
2. Haz clic en **+ New Form**
3. Título: `AI Maturity Assessment - <Nombre de tu organización>`
4. Subtítulo (opcional):

   ```text
   Evaluación de madurez de IA en 3 pilares: Productividad, DevOps y Plataforma.
   158 preguntas en una escala L0-L4. Tiempo estimado: 45-90 minutos.
   Tus respuestas son confidenciales y se usan solo para generar el roadmap.
   ```

### Paso 2 · Configurar 3 secciones

Agrega 3 secciones (botón **+ Add new** → icono de sección):

| Sección | Título | Subtítulo sugerido |
|---|---|---|
| 1 | **Pilar P1: Productividad del desarrollador** | 53 preguntas en 9 capabilities |
| 2 | **Pilar P2: Ciclo de vida DevOps** | 59 preguntas en 10 capabilities |
| 3 | **Pilar P3: Plataforma de aplicaciones** | 46 preguntas en 9 capabilities |

### Paso 3 · Agregar las 158 preguntas

Para cada pregunta, agrega **2 elementos** en Forms:

1. **Choice (single answer)** con la pregunta + las 6 opciones de nivel
2. **Long Text** (opcional) para evidencia

Usa [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md) como fuente para copiar y pegar: contiene las 158 preguntas formateadas con IDs (`P1-C1-Q1`, etc.) y el texto completo en español. El mismo banco existe en inglés, [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md), y en portugués (Brasil), [`perguntas-para-forms.md`](perguntas-para-forms.md) (redacción original). El importador encuentra cada pregunta por su ID, así que un formulario creado en cualquiera de los tres idiomas se importa de la misma manera.

#### Opciones fijas para TODAS las preguntas (pégalas de forma idéntica)

```text
L0 - Inicial: Sin práctica establecida
L1 - En desarrollo: Pilotos aislados (<25%)
L2 - Definido: Cobertura 25-50% con directrices
L3 - Gestionado: >75% con métricas de impacto
L4 - Optimizando: Universal (>95%) con automatización continua
NA - No sé / No aplica
```

> ⚠️ **CRÍTICO:** el prefijo `L0`, `L1`, ..., `L4`, `NA` debe aparecer **literalmente al inicio** de cada opción. La skill de importación usa este prefijo para mapear de vuelta al número (0-4 o null). No lo traduzcas ni lo reformatees.

#### Formato del título de cada pregunta

```text
P1-C1-Q1: <texto de la pregunta>
```

> ⚠️ **IMPORTANTE:** el ID (`P1-C1-Q1`) debe aparecer **literalmente al inicio** del título de la pregunta, seguido de `:`. Ejemplo de [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md):
>
> `P1-C1-Q1: ¿En qué medida tu organización utiliza herramientas de completado de código con IA (por ejemplo, GitHub Copilot)?`

#### Formato del campo de evidencia

```text
Evidencia (P1-C1-Q1)
```

Tipo: **Long Text**, opcional (no lo marques como required). Mantén la etiqueta como se muestra: la skill de importación acepta los prefijos `Evidence (`, `Evidência (` y `Evidencia (` seguidos del ID de la pregunta.

### Paso 4 · Configurar permisos

1. Botón **Settings** (engranaje) en la esquina superior derecha
2. **Who can fill out this form**:
   - **Only people in my organization**: recomendado para uso interno
   - **Anyone with the link**: para uso entre empresas (consultoría)
3. **One response per person**: deshabilitado (queremos múltiples respuestas para agregarlas)
4. **Email notification of each response**: opcional

### Paso 5 · Compartir

1. Botón **Send/Collect responses**
2. Copia el enlace
3. Compártelo con el equipo por Email/Teams/SharePoint

### Paso 6 · Exportar respuestas

Cuando tengas suficientes respuestas (recomendado: ≥3 personas encuestadas para reducir sesgos):

1. Pestaña **Responses**
2. Botón **Open in Excel**
3. Guarda el archivo como **`respostas-forms.xlsx`**
4. Muévelo a la raíz de `kit-cliente/`

### Paso 7 · Importar al kit

En VS Code, abre Copilot Chat (modo **Agent**) y escribe:

```text
/importar-respostas-excel
```

La skill:

- Detecta `respostas-forms.xlsx` automáticamente
- Hace una copia de seguridad del `respostas.json` actual
- Agrega múltiples personas encuestadas mediante el promedio por pregunta
- Sobrescribe `respostas.json`
- Genera `saida/import-log-<DATE>.md`

Luego ejecuta `/pipeline-completo` como de costumbre.

---

## 🅱️ Camino B: Forms liviano (1 capability piloto)

Para **validar el flujo de extremo a extremo** antes de invertir en la configuración completa.

### Paso 1 · Elegir 1 capability

Elige 1 capability con 5-7 preguntas. Sugerencia: **P1-C1 (Asistentes de codificación con IA)**. Es el tema más "caliente" y generará una buena conversación en el equipo.

### Paso 2 · Crear Forms solo con esas 5 preguntas

El mismo proceso del Camino A, pero con solo **5 preguntas** en vez de 158. Tiempo: 15-30 min.

### Paso 3 · Recolectar 3-5 respuestas

Compártelo con tu equipo inmediato (no con toda la empresa). Tiempo: 1-2 días.

### Paso 4 · Importar y ejecutar

Como `respostas.json` tendrá solo 5 preguntas respondidas, el **umbral quedará en BLOCKED** (necesita ≥25). Pero:

- Validarás que el flujo Forms → Excel → respostas.json funciona
- Verás cómo aparece en el informe una capability con datos reales

Para generar un informe útil, completa manualmente el resto mediante `respostas.json` o expande Forms.

---

## 🅲 Camino C: Directamente en Excel/SharePoint ⭐ (RECOMENDADO)

Omite Forms y usa la **plantilla Excel** que viene con el kit.

### Paso 1 · Obtener la plantilla

El kit viene con [`coleta/template-export-forms.xlsx`](template-export-forms.xlsx). Este archivo:

- Tiene el **mismo formato** que exportaría Forms
- Ya tiene las 158 columnas de pregunta + 158 columnas de evidencia
- Viene con **3 personas encuestadas simuladas** como ejemplo (puedes eliminarlas y reemplazarlas)

### Paso 2 · Subir a SharePoint/OneDrive

1. Limpia las 3 filas de personas encuestadas simuladas (filas 2, 3, 4) y mantén solo el encabezado
2. Renómbralo: `respostas-forms.xlsx` (u otro nombre)
3. **SharePoint:** súbelo a la biblioteca del proyecto y genera un enlace "Anyone with the link can edit"
4. **OneDrive:** súbelo y compártelo con permisos de edición
5. **Teams:** adjúntalo al canal y fíjalo

### Paso 3 · Cada persona encuestada completa una fila

Comparte estas instrucciones:

```text
¡Hola, equipo!

Por favor completen UNA fila por persona en este archivo:
<enlace de SharePoint>

Para cada una de las 158 columnas de pregunta:
- Selecciona un nivel L0-L4 (o déjalo en blanco si "no sabes")
- El texto debe comenzar con el código (ej.: "L3")
- Usa la columna Evidencia justo a la derecha para describir herramienta/cobertura/métrica

Tiempo estimado: 45-90 min. Puedes pausar y volver.

¿Preguntas? Consulta los documentos en referencia/P*.md (en kit-cliente).
```

### Paso 4 · Descargar el Excel

Cuando todos lo hayan completado:

1. SharePoint → file → **Download a Copy**
2. Renómbralo a **`respostas-forms.xlsx`**
3. Muévelo a la raíz de `kit-cliente/`

### Paso 5 · Importar y ejecutar

```text
/importar-respostas-excel
/pipeline-completo
```

---

## 🆚 Forms vs. Excel directo: ¿cuál elegir?

| Criterio | Microsoft Forms | Excel/SharePoint |
|---|---|---|
| **Tiempo de configuración** | 4-6 h (crear 158 preguntas) | 5 min (plantilla lista) |
| **UX para la persona encuestada** | Mobile-friendly, 1 pregunta a la vez | Hoja de cálculo (intimidante para personas no técnicas) |
| **Validación de datos** | Fija (Choice = solo 6 opciones) | Frágil (las personas pueden escribir cualquier cosa) |
| **Múltiples personas encuestadas** | Nativo | Manual (1 fila por persona) |
| **Edición posterior** | Difícil (cada envío es final) | Fácil (cualquiera puede cambiarlo en cualquier momento) |
| **Audit trail** | Nativo (timestamp por envío) | SharePoint version history |
| **Costo de licencia** | Microsoft 365 estándar | Microsoft 365 estándar |
| **Integración con el kit** | Idéntica (`/importar-respostas-excel`) | Idéntica |

**Recomendación práctica:**

- **PoC / equipo pequeño (3-5 personas):** Excel directo (Camino C)
- **Roll-out organizacional (10+ personas encuestadas):** Forms (Camino A)
- **Cliente exigente / branding profesional:** Forms (Camino A)

---

## 🔄 Otros formatos compatibles con la skill

La skill `/importar-respostas-excel` acepta cualquier Excel/CSV cuyo encabezado de pregunta empiece con `P[1-3]-C\d+-Q\d+:`. Esto incluye:

- ✅ Exportación de **Microsoft Forms** (formato oficial)
- ✅ Exportación de **Google Forms** (Sheets → Download as .xlsx)
- ✅ **Excel/SharePoint** personalizado (la plantilla del kit o la tuya)
- ✅ **CSV** (si lo renombras a .xlsx o lo conviertes)
- ⚠️ **Typeform**: funciona si ajustas los encabezados para incluir los IDs

---

## 💡 Consejos prácticos

### Consejo 1 · Empieza con 1 pilar

No intentes recolectar respuestas de los 3 pilares al mismo tiempo. Empieza por P1 (Productividad), que es el más tangible para devs. Luego P2 (DevOps) con SREs. Luego P3 (Plataforma) con arquitectos.

### Consejo 2 · Prellenado mediante entrevistas

En vez de enviar el enlace y esperar, realiza una **entrevista de 1 hora por persona encuestada** y complétalo en conjunto. Capturas mejor los matices y generas evidencia más rica.

### Consejo 3 · Capacita antes del lanzamiento

Realiza un **kick-off de 30 min** explicando:

- Qué es la evaluación
- Cómo se definen L0-L4
- Por qué importa la evidencia
- Cuánto tiempo tomará
- Cuándo recibirán el informe

### Consejo 4 · Ejecuta ciclos cortos

No esperes el 100% de las respuestas para ejecutar `/pipeline-completo`. Ejecútalo con 25 (WARNING), luego 50 (OK), luego 100. Con cada ciclo, el informe mejora y capturas más conversaciones.

### Consejo 5 · Versionado

Cada vez que importas, la skill crea `respostas.json.backup-<timestamp>`. Conserva esas copias de seguridad: son tu **historial de evolución** entre rondas de evaluación.

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solución |
|---|---|---|
| La skill no detecta `respostas-forms.xlsx` | El archivo no está en la raíz | Muévelo a `kit-cliente/respostas-forms.xlsx` (no dentro de coleta/) |
| "No recognized header" | Los encabezados de Excel no empiezan con `P1-C1-Q1:` etc. | Edita manualmente los encabezados para incluir los IDs al inicio |
| Una persona encuestada aparece dos veces | Forms permite múltiples envíos de la misma persona | Edita el Excel manualmente para eliminar la fila duplicada antes de importar |
| Los niveles se volvieron texto | Forms exportó la opción SIN el prefijo `L0/L1/...` | Reconstruye Forms incluyendo los prefijos al inicio de cada opción Choice |
| Excel tiene 158 columnas pero solo se reconocen 90 preguntas | Encabezados truncados por Forms (límite de 4000 caracteres) | Acorta el texto de las preguntas en Forms (mantén solo el ID + una frase resumida) |

---

## 📚 Referencias

- **Lista completa de las 158 preguntas formateadas para Forms:** [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md) (español) · [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md) (inglés) · [`perguntas-para-forms.md`](perguntas-para-forms.md) (portugués (Brasil), redacción original)
- **Plantilla Excel lista (3 personas encuestadas simuladas):** [`template-export-forms.xlsx`](template-export-forms.xlsx)
- **Skill de importación:** [`../.github/skills/importar-respostas-excel/SKILL.md`](../../.github/skills/importar-respostas-excel/SKILL.md)
- **Algoritmo de agregación de múltiples personas encuestadas:** [`../referencia/pontuacao-e-calculo.md`](../../referencia/pontuacao-e-calculo.es.md) sección 6

---

**Versión:** 1.0 · **Fecha:** 2026-05-08

---

## ¿Te bloqueaste en alguno de estos pasos?

<details>
<summary><strong>FAQ: dudas comunes sobre la recolección mediante Forms</strong></summary>

| Síntoma | Causa probable | Cómo resolverlo |
|---|---|---|
| **Open in Excel** está deshabilitado en Forms | Tu cuenta no tiene licencia M365 / Forms está en una cuenta personal | Pide a un admin que mueva Forms a la cuenta organizacional |
| Tengo múltiples personas encuestadas: ¿cómo las agrego? | Comportamiento predeterminado de la skill | `/importar-respostas-excel` calcula una **media automática** por pregunta |
| Los encabezados de las columnas no empiezan con `P1-C1-Q1:` | No seguiste el patrón al crear Forms | Edita los títulos de las preguntas en Forms para incluir el ID al inicio |
| Compartir Forms con personas fuera de la organización | La configuración de Forms restringe el acceso | Settings → **Anyone with the link can respond** |
| Excel llega con columnas extra (ID, Start time, ...) | Comportamiento predeterminado de Forms | La skill ignora automáticamente las columnas A-E |
| `respostas-forms.xlsx` no se detecta | El archivo está dentro de `coleta/` en vez de la raíz | Muévelo a la **raíz** del kit |

</details>

---

## Continuar leyendo

| ← ANTERIOR | SIGUIENTE → |
|:---|---:|
| **[Guía paso a paso](../../GUIA-PASSO-A-PASSO.es.md)** | **[Developer Survey (anónimo)](../../survey-devs/INSTRUCOES-FORMS-DEVS.es.md)** |
| De cero al PDF ejecutivo en 60-90 min. | 75 preguntas anónimas sobre Copilot, agentes, gobernanza, MCP / A2A. |

↑ [Volver al Índice del kit](../README.es.md)
