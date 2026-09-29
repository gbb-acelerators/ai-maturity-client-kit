# Rúbrica de Madurez IA: Developer Survey

🌐 [English](MATURITY-RUBRIC.md) · [Português (Brasil)](MATURITY-RUBRIC.pt-br.md) · Español

> **Modelo determinístico** que mapea respuestas de la encuesta a niveles L0-L4 en **7 dimensiones**, con las bandas L0-L4 de la evaluación v1 (ver el principio 5). Puntuación por equipo (sin puntajes individuales en el informe, lo que preserva el anonimato).

**Versión de la rúbrica:** 1.0 · **Fecha:** 2026-05-08
**Implementación:** [`scripts/rubric.py`](scripts/rubric.py) · **Runner:** [`scripts/calculate_maturity.py`](scripts/calculate_maturity.py)

> **Sobre las señales de respuesta abajo:** las respuestas entre comillas son las cadenas de opciones canónicas en español de [`question-bank-devs.es.md`](question-bank-devs.es.md), que [`options.json`](options.json) mapea a las mismas opciones canónicas usadas por la rúbrica. El banco canónico PT-BR es [`question-bank-devs.pt-br.md`](question-bank-devs.pt-br.md).

---

## 🎯 Principios

1. **Determinístico**: la misma respuesta siempre produce el mismo nivel. Sin LLM, sin aleatoriedad.
2. **Auditable**: cada regla está documentada en este archivo, y el código la replica 1:1.
3. **Conservador**: ante la duda, el nivel baja (evita inflar la madurez declarada).
4. **Anónimo**: se calcula para cada persona encuestada individualmente, pero **solo agregados** aparecen en el informe (media, distribución).
5. **Bandas v1**: usa las bandas L0-L4 de la evaluación v1 (Inicial a Optimizing). Framework v2 usa otras bandas (0.8 de ancho) y nombres de nivel, así que compara resultados de la encuesta y v2 por puntaje y mediante las preguntas v2 listadas abajo, no por nombre de nivel.

## 🧭 Escala (bandas de la evaluación v1)

| Rango | Etiqueta | Descripción |
|---|---|---|
| `< 0.5` | **L0 Initial** | Sin práctica, sin conocimiento, sin herramientas |
| `[0.5, 1.5)` | **L1 Developing** | Adopción ocasional, conocimiento básico |
| `[1.5, 2.5)` | **L2 Defined** | Uso regular, conoce conceptos clave |
| `[2.5, 3.5)` | **L3 Managed** | Adopción amplia, conoce conceptos avanzados, mide impacto |
| `≥ 3.5` | **L4 Optimizing** | Dominio completo, crea primitivos, optimización continua |

> **IDs:** las dimensiones de la encuesta son `DS-D2` a `DS-D8`. El prefijo `DS-` las mantiene separadas de las dimensiones `D1` a `D9` de la evaluación v2, que significan cosas diferentes. `survey_crosswalk` en [framework.v2.json](../framework.v2.json) lista las preguntas v2 que cada dimensión de la encuesta ayuda a validar; los resultados de la encuesta nunca cambian los puntajes v2.

## 📊 Las 7 dimensiones

| ID | Dimensión | Viene de | Qué mide |
|---|---|---|---|
| **DS-D2** | **Copilot Adoption** | S2 (9 q) | Frecuencia + amplitud de modos + features + ganancia medida |
| **DS-D3** | **MS/GH Tooling Breadth** | S3 (7 q) | Cuántas herramientas avanzadas (Foundry, Spaces, Coding Agent, MCP, Spec Kit) se usan |
| **DS-D4** | **AI Dev Practices** | S4 (9 q) | TDD con IA, SDD, pair programming, debugging, onboarding |
| **DS-D5** | **Agent Concepts Mastery** | S5 (11 q) | Conocimiento de 9 conceptos clave + creación de primitivos + tests |
| **DS-D6** | **Instructions Maturity** | S6 (6 q) | Uso de instruction files, mantenimiento, prompt library compartida |
| **DS-D7** | **Best Practices** | S7 (9 q) | Champion, métricas DORA/DX, comunidad, compartir |
| **DS-D8** | **Security & Governance** | S8 (13 q) | Política, GHAS, scanners, SBOM, JIT, red-lines, audit, entrenamiento |

> **Excluidas del puntaje:** S1 (perfil, solo categoriza) y S9 (texto libre, se convierte en citas).

## ⚖️ Reglas detalladas por dimensión

### DS-D2: Copilot Adoption

| Respuesta clave | Señales |
|---|---|
| `S2-Q1: No tengo licencia` OR `Tengo licencia pero no la uso` | **Hard L0** |
| `S2-Q2: Nunca` | **Hard L0** |
| `S2-Q2: Rara vez` | L1 |
| `S2-Q2: Diariamente (varias horas)` OR `Diariamente (esporádico)` + `S2-Q5: 2+ features` + `S2-Q3: 1+ modo` | **L2** |
| Lo anterior + `S2-Q3: usa Agent o Coding Agent` + `S2-Q5: 4+ features` + ganancia positiva | **L3** |
| Lo anterior + `S2-Q3: Copilot Coding Agent (autónomo en GitHub.com, asigna issues, abre PRs solo)` + `S2-Q5: Copilot Spaces (contexto compartido: repos + docs + custom instructions)` + `S2-Q7: ganancia >40%` + `S2-Q5: 5+ features` | **L4** |

### DS-D3: MS/GH Tooling Breadth

Puntaje punto a punto: `n_tools (S3-Q1) + advanced_signals (S3-Q3, Q4, Q6, Q2)`

- `n_tools` = cuántas herramientas están marcadas en S3-Q1 (excluyendo "Ninguna de las anteriores")
- `advanced_signals` = +1 por cada:
  - Coding Agent: "Lo uso activamente en producción"
  - Spaces: "Uso y creo Spaces para mi equipo"
  - MCP: "Uso servidores MCP en mi workflow" o "Configuré algún MCP server custom"
  - Foundry usado para "Multi-agent orchestration vía MCP" o "Foundry Agent Service para agentes autónomos"

**Mapping:**

- `score ≥ 8` → **L4** (5+ herramientas + 3+ señales avanzadas)
- `score 5-7` → **L3**
- `score 3-4` → **L2**
- `score 1-2` → **L1**
- `score 0` → **L0**

### DS-D4: AI Dev Practices

Suma ponderada (máx. ~10 puntos), mapeada a 0-4:

| Pregunta | Señal | Puntos |
|---|---|---|
| `S4-Q1` TDD con IA | "Siempre que sea posible" | +2 |
|  | "Frecuentemente" | +1.5 |
|  | "No sé qué es TDD" | -1 |
| `S4-Q2` SDD | "Lo uso activamente (con Spec Kit o similar)" | +2 |
|  | "Ya lo probé en algunos proyectos" | +1 |
|  | "Nunca escuché hablar de eso" | -0.5 |
| `S4-Q3` Momentos en que se consulta IA (multi) | n_momentos × 0.4 (cap 2.0) | hasta +2 |
| `S4-Q4` Mentalidad de pair programmer | "Sí, lo trato como par" | +1.5 |
|  | "A veces (depende de la tarea)" | +0.5 |
| `S4-Q5` Refactoring | "Todas las semanas" | +1 |
| `S4-Q7` Debugging primero con IA | "Le pregunto a Copilot Chat / Claude / otra IA" | +0.5 |
| `S4-Q8` Onboarding con IA | "Siempre, es lo primero que hago" | +1 |

**Mapping:** `score / 10 × 4` → redondeado.

### DS-D5: Agent Concepts Mastery

3 componentes:

**(a) Cobertura de 9 conceptos** (60% del peso): por cada uno, +1.0 si "lo uso / lo explico", de lo contrario 0:

- S5-Q1 AI agent
- S5-Q2 Modos Copilot
- S5-Q3 Custom agents
- S5-Q4 Skills
- S5-Q5 Prompt files
- S5-Q6 A2A
- S5-Q7 Handoffs
- S5-Q8 Subagentes
- S5-Q9 Personas Agentic DevOps

**(b) Primitivos creados (S5-Q11 multi)** (25% del peso): n_primitivos × 0.25 (cap 1.0)

**(c) Tests de agents (S5-Q10)** (15% del peso):

- "Siempre, tengo test suite para mis agents" → +1.0
- "Frecuentemente, manual pero sistemático" → +0.5
- "No creo agents/prompts/skills" → 0 (neutral)

**Fórmula:** `(coverage × 0.6 × 4) + min(n_primitivos × 0.25, 1.0) + (test_bonus × 0.36)`. Limitado a 4.0.

**Cobertura mínima:** si `<5` preguntas están respondidas → devuelve `None` (no puntuado).

### DS-D6: Instructions Maturity

| Pregunta | Señal | Puntos |
|---|---|---|
| `S6-Q1` Files (multi) | "Ninguno" o vacío | **Hard L0** |
|  | 4+ tipos | +2 |
|  | 2-3 tipos | +1.5 |
|  | 1 tipo | +1 |
| `S6-Q2` Maintainer | "Todo el equipo contribuye" | +2 |
|  | "1-2 personas dedicadas" | +1.5 |
|  | "Nadie los mantiene, están desactualizados" / "No tenemos" | -1 |
| `S6-Q3` Update freq | "Todas las semanas" | +1 |
|  | "Mensualmente" | +0.7 |
|  | "Nunca los actualizo" | -0.5 |
| `S6-Q4` Content (multi) | n_tipos × 0.3 (cap 2.0) | hasta +2 |
| `S6-Q5` Library shared | "Sí, Copilot Space compartido" / "Sí, repo dedicado" | +1 |
|  | "No compartimos prompts" | -0.5 |

**Mapping:** `score / 9 × 4`.

### DS-D7: Best Practices

| Pregunta | Señal | Puntos |
|---|---|---|
| `S7-Q1` Learning sources (multi) | n_fuentes × 0.3 (cap 1.5) | hasta +1.5 |
| `S7-Q2` Champion | "Sí, soy yo" / "Sí, otra persona" | +1.5 |
|  | "No, cada quien se las arregla" | -0.5 |
| `S7-Q3` Internal channel | ">5 mensajes/semana" | +1 |
|  | "Sí, poco activo" | +0.5 |
| `S7-Q4` Metrics (multi) | DORA/DX/SPACE/Copilot count × 0.5 (cap 2.0) | hasta +2 |
|  | "No medimos formalmente" | -1 |
| `S7-Q5` Iterations | "Acierta en el 1er intento" / "2-3 iteraciones" | +1 |
|  | "7+ iteraciones (frecuente)" | -0.5 |
| `S7-Q9` Comparte prompts | "Frecuentemente, en un canal compartido" | +1 |
|  | "Nunca" | -0.5 |

**Mapping:** `score / 8 × 4`.

### DS-D8: Security & Governance (CRÍTICO, conservador)

Mayor número de reglas + penalizaciones por red flags:

| Pregunta | Señal | Puntos |
|---|---|---|
| `S8-Q1` Policy + `S8-Q4` (Sec tools) | "No tenemos política" + "Ninguna" | **Hard L0** |
| `S8-Q1` | "Sí, política formal y clara" | +2 |
|  | "Sí, pero poco clara" | +1 |
|  | "Política informal (sin documento)" | +0.5 |
| `S8-Q2` Knows sensitive data | "Sé claramente qué se puede y qué NO se puede" | +1 |
| `S8-Q3` Forbidden (multi) | n_tipos × 0.2 (cap 1.0) | hasta +1 |
|  | "Ninguna restricción (no tenemos política)" | -1 |
| `S8-Q4` Sec tools (multi) | n_tools × 0.3 (cap 2.0) | hasta +2 |
| `S8-Q5` Code scan on PR | "Sí, gate obligatorio en el PR" | +1 |
| `S8-Q6` SBOM | "Sí, automatizado" | +0.5 |
| `S8-Q7` Formal AI review | "Sí, review obligatorio por otro humano + scanner" | +1 |
| `S8-Q8` Agent red-lines | "Siempre, alcance + red-lines documentados" | +1 |
| `S8-Q9` JIT permissions | "Sí, JIT obligatorio para agents" | +1 |
| `S8-Q10` DLP | "Sí, bloquea activamente" | +0.5 |
| `S8-Q11` Audit | "Sí, logs activos y revisados" | +0.5 |
| `S8-Q12` Training | "Sí, entrenamiento obligatorio anual" | +0.5 |

**Mapping:** `score / 12 × 4`.

## 🧮 Puntaje general de la persona encuestada

```text
overall = mean(DS-D2..DS-D8)  # only dimensions with score != None
```

## 🧮 Agregación del equipo

```text
team_score(D) = mean(D across all respondents)  # ignores None
team_overall  = mean(overall of all respondents)
distribution(D) = % of respondents in each L0-L4
```

## 📤 Salida

`output/developer-survey-maturity-<DATE>.json`:

```jsonc
{
  "metadata": {
    "computed_at": "2026-05-08T12:00:00Z",
    "n_respondents": 12,
    "rubric_version": "1.0 (deterministic)",
    "anonymous": true,
    "scope": "team aggregate (no individual scores in output)"
  },
  "team_overall": {
    "score": 2.22,
    "label": "L2: Definido",
    "respondents_with_overall": 12
  },
  "dimensions": {
    "DS-D2": {
      "name": "Copilot Adoption",
      "team_score": 0.80,
      "label": "L1: Em Desenvolvimento",
      "respondents_with_score": 12,
      "distribution_count": {"L0": 5, "L1": 5, "L2": 2, "L3": 0, "L4": 0},
      "distribution_pct": {"L0": 41.7, "L1": 41.7, "L2": 16.7, "L3": 0, "L4": 0}
    },
    "DS-D3": {...}, "DS-D4": {...}, "DS-D5": {...},
    "DS-D6": {...}, "DS-D7": {...}, "DS-D8": {...}
  },
  "ranking": {
    "top": [["DS-D7", "Best Practices", 2.91], ...],
    "bottom": [["DS-D2", "Copilot Adoption", 0.80], ...]
  }
}
```

La muestra anterior muestra las etiquetas PT-BR. La salida legible para humanos (el informe de insights) ahora se genera en **inglés por defecto**, con PT-BR y ES disponibles vía `--lang pt-br` y `--lang es` en los scripts.

## 🔄 Cómo ejecutar

### Vía skill en Copilot Chat

```text
/insights-developer-survey   # invokes the script automatically
```

### Vía CLI

```bash
python3 survey-devs/scripts/calculate_maturity.py
# Output:
#   - output/developer-survey-maturity-DATE.json
#   - summary on stdout (overall + table per dimension + ranking)
```

## 🔗 Referencia cruzada con la evaluación principal

La madurez individual (de la encuesta) **ayuda a validar** las respuestas de la evaluación organizacional v2. Las listas de preguntas vienen de `survey_crosswalk` en [framework.v2.json](../framework.v2.json); los resultados de la encuesta nunca cambian los puntajes v2.

| Dimensión de la encuesta | Preguntas de la evaluación v2 | Qué validar |
|---|---|---|
| **DS-D2** Copilot Adoption | `D4-Q1`, `D4-Q2`, `D9-Q1` | Puntaje declarado vs. adopción real declarada por desarrolladores |
| **DS-D3** MS/GH Tooling | `D4-Q3`, `D4-Q6`, `D3-Q2`, `D6-Q1` | Sofisticación técnica en IA |
| **DS-D4** AI Dev Practices | `D3-Q2`, `D5-Q5`, `D2-Q6` | Prácticas estructuradas |
| **DS-D5** Agent Concepts | `D2-Q4`, `D4-Q5` | Conocimiento avanzado |
| **DS-D6** Instructions | `D4-Q4`, `D4-Q5` | Mantenimiento de contexto de IA |
| **DS-D7** Best Practices | `D2-Q2`, `D9-Q4` | Cultura de adopción |
| **DS-D8** Security & Governance | `D1-Q2`, `D6-Q1`, `D6-Q4`, `D6-Q5`, `D6-Q7` | Gobernanza real |

> 💡 **Patrón clásico:** el liderazgo califica D4-Q1 como L3, pero la encuesta DS-D2 muestra L1 (60% de los desarrolladores rara vez lo usan) → **disonancia** entre estrategia y práctica. La skill `/insights-developer-survey` destaca esto en la sección 12 del informe.

## 📊 Calibración y revisión de la rúbrica

Esta es la **versión 1.0**. Revísala trimestralmente con base en:

- Casos donde el puntaje parece subestimado o sobreestimado (calibrar pesos)
- Cambios del ecosistema (p. ej., Copilot lanza un modo nuevo → agrégalo a S2-Q3 + actualiza DS-D2)
- Feedback de personas encuestadas ("esta pregunta era ambigua")

**Cómo proponer un cambio:**

1. Edita `scripts/rubric.py` con la regla actualizada
2. Documenta la razón en este archivo
3. Incrementa `RUBRIC_VERSION` y vuelve a ejecutar con datos anteriores para comparar

## 🔐 Política de anonimato en la puntuación

La rúbrica calcula un puntaje PARA CADA persona encuestada individualmente, pero la salida JSON y el informe:

- ✅ Muestran **puntajes agregados del equipo** (media, % distribución)
- ✅ Muestran **distribución por nivel** (% de desarrolladores en cada L0-L4)
- ❌ NO muestran un puntaje por respondent_id
- ❌ NO muestran rol/perfil junto con un puntaje (agregación por rol solo si ≥3 desarrolladores comparten el mismo rol)

Esto preserva el pacto de anonimato de la encuesta mientras sigue produciendo insights útiles para el equipo.
