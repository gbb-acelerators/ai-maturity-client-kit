# Puntuación y Cálculo de la Evaluación de Madurez IA

🌐 [English](scoring-and-calculation.md) · [Português (Brasil)](scoring-and-calculation.pt-br.md) · Español

> **Framework v1 (158 preguntas, 3 pilares).** Para el framework v2 (9 dimensiones, 61 preguntas), consulta [framework-v2.es.md](framework-v2.es.md). Los archivos v1 todavía puntúan con estas reglas.
>
> **Documento técnico de referencia**: describe con precisión cómo cada respuesta se convierte en puntaje, cómo se agregan capabilities/pillars/overall, reglas de threshold, manejo multi-respondent, gap analysis y PE score. El kit implementa estas fórmulas en [`scripts/assessment_engine.py`](../scripts/assessment_engine.py) (pruebas golden en `scripts/test_assessment_engine.py`).

**Versión del algoritmo:** 1.0.0 · **Última auditoría del código:** 2026-05-08

---

## Tabla de contenidos

1. [Modelo conceptual de tres capas](#1-modelo-conceptual-de-tres-capas)
2. [Cómo cada respuesta se convierte en número](#2-cómo-cada-respuesta-se-convierte-en-número)
3. [Fórmulas oficiales](#3-fórmulas-oficiales)
4. [Manejo de respuestas faltantes](#4-manejo-de-respuestas-faltantes)
5. [Threshold de cobertura mínima](#5-threshold-de-cobertura-mínima)
6. [Multi-respondent: agregación](#6-multi-respondent-agregación)
7. [Etiquetas de madurez (mapeo de puntaje)](#7-etiquetas-de-madurez-mapeo-de-puntaje)
8. [Gap analysis y priorización](#8-gap-analysis-y-priorización)
9. [PE Score (Production Engineering Readiness)](#9-pe-score-production-engineering-readiness)
10. [Persistencia (tablas y materialización)](#10-persistencia-tablas-y-materialización)
11. [**Ejemplo end-to-end: Pilar P1**](#11-ejemplo-end-to-end-pilar-p1)
12. [**Ejemplo end-to-end: Pilar P2**](#12-ejemplo-end-to-end-pilar-p2)
13. [**Ejemplo end-to-end: Pilar P3**](#13-ejemplo-end-to-end-pilar-p3)
14. [Casos de borde y garantías](#14-casos-de-borde-y-garantías)
15. [Glosario](#15-glosario)

---

## 1. Modelo conceptual de tres capas

```text
┌─────────────────────────────────────────────────────────────┐
│                    OVERALL SCORE (0-4)                      │
│    = promedio ponderado de ALL capabilities (no pillars)    │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                  PILLAR SCORE (P1, P2, P3)                  │
│       = promedio ponderado de las capabilities del pillar   │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                CAPABILITY SCORE (P1-C1 … P3-C9)             │
│      = promedio ponderado de las preguntas de la capability │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│              QUESTION RESPONSE (L0=0 … L4=4)                │
│    = nivel seleccionado por la persona encuestada (multi → promedio) │
└─────────────────────────────────────────────────────────────┘
```

**Característica importante:** el **overall** se calcula directamente sobre las capabilities (SUMPRODUCT); **no** es el promedio de los 3 pillar scores. Esto evita que un pilar con pocas capabilities pese igual que uno con muchas.

---

## 2. Cómo cada respuesta se convierte en número

| Nivel seleccionado | Etiqueta | Valor numérico |
|---|---|---|
| L0 | Inicial | **0** |
| L1 | En desarrollo | **1** |
| L2 | Definido | **2** |
| L3 | Gestionado | **3** |
| L4 | Optimizado | **4** |

La escala es **discreta en la entrada (entero 0-4)**, pero las agregaciones producen **valores continuos de punto flotante (`f64`)**, sin redondeo. Solo la capa de presentación (UI/informe) decide la precisión visual (normalmente 2 decimales).

---

## 3. Fórmulas oficiales

### 3.1 Capability score
>
> Código de referencia: [`scoring.rs:205-225`](../scripts/assessment_engine.py)

$$
\text{capability\_score} = \frac{\sum_{q \in \text{respondidas}} (\text{nivel}_q \times \text{peso}_q)}{\sum_{q \in \text{respondidas}} \text{peso}_q}
$$

- Términos de la fórmula (mantenidos como en la fuente): `respondidas` = preguntas respondidas, `nivel` = nivel, `peso` = peso, `TODAS as capabilities` = todas las capabilities.
- Si ninguna pregunta de la capability fue respondida → `capability_score = None` (no entra en los cálculos superiores).
- Pesos predeterminados: **1.0**. Rango permitido: **[0.5, 2.0]**.

### 3.2 Pillar score
>
> Código de referencia: [`scoring.rs:227-247`](../scripts/assessment_engine.py)

$$
\text{pillar\_score} = \frac{\sum_{c \in \text{pillar}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{pillar}} \text{peso}_c}
$$

Solo participan capabilities con `score = Some(_)` (se omiten las capabilities sin ninguna respuesta).

### 3.3 Overall score
>
> Código de referencia: [`scoring.rs:250-263`](../scripts/assessment_engine.py)

$$
\text{overall\_score} = \frac{\sum_{c \in \text{TODAS as capabilities}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{TODAS as capabilities}} \text{peso}_c}
$$

**Atención:** SUMPRODUCT directamente sobre todas las capabilities; **no** es `mean(P1, P2, P3)`.

---

## 4. Manejo de respuestas faltantes

| Situación | Comportamiento |
|---|---|
| Pregunta sin responder | **Ignorada**. No suma en `wsum` ni en `wtotal`. Sin penalización. |
| Capability sin ninguna respuesta | `score = None`. No entra en el pillar ni en el overall. |
| Pillar sin capabilities respondidas | `pillar_score = 0.0` (caso de borde raro). |
| Overall sin capabilities respondidas | `overall_score = 0.0`. |

> **Regla de oro:** "las respondidas pesan, las faltantes desaparecen". Esto incentiva a la persona encuestada a *no adivinar* cuando no sabe: el sistema solo penaliza vía `threshold_status`, no mediante un puntaje deflactado.

---

## 5. Threshold de cobertura mínima

> Código de referencia: [`scoring.rs:351-359`](../scripts/assessment_engine.py)

| Preguntas aplicables | Status | Comportamiento |
|---|---|---|
| **≥ 40** | `Ok` | Puntuación normal, sin advertencia. |
| **25-39** | `Warning` | Puntuación calculada, pero el informe muestra el banner "Resultado preliminar: confiabilidad limitada". |
| **< 25** | `Blocked` | Puntuación **rechazada**. La API responde 422 `InsufficientData`. |

"Aplicables" = preguntas visibles para la audiencia configurada de la persona encuestada (después del filtro `audience`). Si una persona encuestada es Backend, las preguntas solo de Frontend no cuentan.

---

## 6. Multi-respondent: agregación

> Código de referencia: [`repos/scoring.rs:354-368`](../scripts/assessment_engine.py)

Cuando más de una persona responde la misma evaluación:

1. Para cada `question_id`, el sistema calcula **`AVG(selected_level)`** sobre todas las personas encuestadas que respondieron esa pregunta.
2. Este valor promedio (que puede ser fraccional, por ejemplo, 2.67) entra como `nivel_q` en la fórmula de capability score.
3. **No hay peso por persona encuestada**: todas las personas encuestadas cuentan igual.
4. **No hay estratificación por audiencia**: si Backend y Frontend responden la misma Q, el promedio mezcla ambos.

**Ejemplo:** 3 personas encuestadas para Q1 con niveles 2, 4, 3 → `Q1 = (2+4+3)/3 = 3.0`.

---

## 7. Etiquetas de madurez (mapeo de puntaje)

> Código de referencia: [`scoring.rs:361-373`](../scripts/assessment_engine.py)

Aplicado a cualquier puntaje (capability, pillar u overall):

| Rango de puntaje | Etiqueta | Color (token) |
|---|---|---|
| `score < 0.5` | **L0 Inicial** | `--color-l0` (rojo) |
| `0.5 ≤ score < 1.5` | **L1 En desarrollo** | `--color-l1` (ámbar) |
| `1.5 ≤ score < 2.5` | **L2 Definido** | `--color-l2` (azul) |
| `2.5 ≤ score < 3.5` | **L3 Gestionado** | `--color-l3` (verde) |
| `score ≥ 3.5` | **L4 Optimizado** | `--color-l4` (morado) |

---

## 8. Gap analysis y priorización

> Código de referencia: [`scoring.rs:307-349`](../scripts/assessment_engine.py)

Para cada capability:

```text
target_level   = target_overrides.get(capability_id) or 3.0 (default L3)
gap_size       = target_level − current_score
priority_score = peso_capability × gap_size

If gap_size ≤ 1e-9 (floating-point epsilon) → discard (target already reached)
```

### Clasificación de prioridad

| `priority_score` | Etiqueta | Significado |
|---|---|---|
| ≥ 2.4 | **P0** | Crítico: abordar en los próximos 30 días |
| ≥ 1.6 and < 2.4 | **P1** | Alto: incluir en el próximo trimestre |
| ≥ 0.9 and < 1.6 | **P2** | Medio: backlog del semestre |
| < 0.9 | **P3** | Bajo: monitorear |

**¿Por qué `weight × gap`?** Las capabilities con peso 2.0 y brecha 1.5 (priority_score = 3.0) son más urgentes que peso 1.0 y brecha 2.0 (priority_score = 2.0): el peso refleja el impacto estratégico en el overall.

---

## 9. PE Score (Production Engineering Readiness)

> Código de referencia: [`scoring.rs:266-304`](../scripts/assessment_engine.py)

Subpuntaje calculado **solo con preguntas marcadas `pe = true`** en el seed.

- Filtra → recalcula capability/pillar/overall con el subconjunto.
- Mismo SUMPRODUCT.
- Si ninguna pregunta tiene `pe = true` → devuelve `None`.
- Se muestra lado a lado con el overall general, señalando readiness de producción (resiliencia, observabilidad, runbooks, SLOs, etc.).

---

## 10. Persistencia (tablas y materialización)

> Migration de referencia: [`migrations/20260417000000_initial.sql`](../scripts/assessment_engine.py)

| Tabla | Columnas clave | Cuándo se popula |
|---|---|---|
| `assessment_scores` | `overall_score`, `pe_score`, `total_applicable`, `total_answered`, `scored_at` | `POST /api/scoring/trigger` |
| `pillar_scores` | `pillar_id`, `score` | igual |
| `capability_scores` | `capability_id`, `score` (NULL si no hay respuesta), `weight` | igual |
| `gap_analysis` | `capability_id`, `current_score`, `target_level`, `gap_size`, `priority`, `priority_score` | igual |

`GET /api/scoring/results/{assessment_id}` lee **directamente de las tablas materializadas**; no recalcula. Esto garantiza consistencia entre los informes y roadmaps generados.

---

## 11. Ejemplo end-to-end: Pilar P1

### Escenario

Capability **P1-C1: Asistentes de Codificación IA** (5 preguntas). Evaluación respondida por **2 desarrolladores** (R1 y R2). Todas las preguntas tienen `weight = 1.0` (predeterminado).

### Respuestas reales

| Pregunta | Pregunta (resumida) | R1 | R2 | **Avg** |
|---|---|---|---|---|
| `P1-C1-Q1` | Adopción de herramientas de completado de código con IA | L3 (3) | L4 (4) | **3.5** |
| `P1-C1-Q2` | IA para revisión de código y mejora de calidad | L2 (2) | L3 (3) | **2.5** |
| `P1-C1-Q3` | IA para generación y mantenimiento de pruebas | L1 (1) | L2 (2) | **1.5** |
| `P1-C1-Q4` | Ingeniería de prompts y gestión de plantillas | L2 (2) | L2 (2) | **2.0** |
| `P1-C1-Q5` | Gobernanza y seguridad de las herramientas IA | L3 (3) | L4 (4) | **3.5** |

### Paso 1: Capability score (P1-C1)

```text
wsum   = (3.5×1.0) + (2.5×1.0) + (1.5×1.0) + (2.0×1.0) + (3.5×1.0)
       = 3.5 + 2.5 + 1.5 + 2.0 + 3.5
       = 13.0

wtotal = 1.0 + 1.0 + 1.0 + 1.0 + 1.0 = 5.0

P1-C1.score = 13.0 / 5.0 = 2.60   →   Etiqueta: L3 Gestionado
```

### Paso 2: Pillar score (P1)

Supón que P1-C1 es la única capability respondida del pilar P1, con `weight_capability = 1.0`:

```text
ws = 2.60 × 1.0 = 2.60
wt = 1.0
P1.score = 2.60 / 1.0 = 2.60   →   Etiqueta: L3 Gestionado
```

> En una evaluación real, P1 tiene 9 capabilities. El cálculo sería un SUMPRODUCT sobre todas las que tengan al menos 1 respuesta.

### Paso 3: Gap analysis

`target_level = 3.0` predeterminado:

```text
gap_size       = 3.0 − 2.60 = 0.40
priority_score = 1.0 × 0.40 = 0.40
classification = P3 (Bajo)   ← because 0.40 < 0.9
```

### Paso 4: Threshold

5 preguntas respondidas << 25 → **`threshold_status = Blocked`** si esta fuera la única capability evaluada. En producción, se esperan ≥ 40 preguntas respondidas en toda la evaluación.

---

## 12. Ejemplo end-to-end: Pilar P2

### Escenario

Capability **P2-C1: Inteligencia de Pipeline CI/CD** (6 preguntas). Respondida por **1 SRE** + **1 Platform Engineer**. Mezcla de pesos: Q1 y Q5 con `weight = 1.5` (preguntas con impacto directo en DORA metrics).

### Respuestas

| Pregunta | Pregunta (resumida) | Peso | SRE | PltEng | **Avg** |
|---|---|---:|---:|---:|---:|
| `P2-C1-Q1` | Optimización de pipeline CI/CD con IA | **1.5** | L4 (4) | L3 (3) | **3.5** |
| `P2-C1-Q2` | Self-healing builds y autocorrección | 1.0 | L2 (2) | L2 (2) | **2.0** |
| `P2-C1-Q3` | Análisis predictivo de fallas | 1.0 | L1 (1) | L2 (2) | **1.5** |
| `P2-C1-Q4` | Optimización inteligente de caché | 1.0 | L2 (2) | L3 (3) | **2.5** |
| `P2-C1-Q5` | DORA metrics e insights | **1.5** | L3 (3) | L4 (4) | **3.5** |
| `P2-C1-Q6` | Triaje automatizado de pruebas flaky | 1.0 | L2 (2) | L1 (1) | **1.5** |

### Paso 1: Capability score (P2-C1)

```text
wsum   = (3.5×1.5) + (2.0×1.0) + (1.5×1.0) + (2.5×1.0) + (3.5×1.5) + (1.5×1.0)
       = 5.25 + 2.0 + 1.5 + 2.5 + 5.25 + 1.5
       = 18.00

wtotal = 1.5 + 1.0 + 1.0 + 1.0 + 1.5 + 1.0 = 7.0

P2-C1.score = 18.00 / 7.0 = 2.5714…   →   Etiqueta: L3 Gestionado
```

> **Nota:** sin los pesos extra en Q1 y Q5, el promedio simple sería `(3.5+2.0+1.5+2.5+3.5+1.5)/6 = 2.4167` → caería a L2. El peso 1.5 refleja que estas dos dimensiones importan más para un resultado DevOps maduro.

### Paso 2: Pillar score (P2) con 2 capabilities

Agrega P2-C2 (IaC) con score = 1.80, peso = 1.0:

```text
ws = (2.5714 × 1.0) + (1.80 × 1.0) = 4.3714
wt = 1.0 + 1.0 = 2.0
P2.score = 4.3714 / 2.0 = 2.1857   →   Etiqueta: L2 Definido
```

### Paso 3: Gap analysis (target personalizado)

Para P2-C1, el equipo de SRE definió `target_level = 3.5` (por encima del predeterminado):

```text
gap_size       = 3.5 − 2.5714 = 0.9286
priority_score = 1.0 × 0.9286 = 0.9286
classification = P2 (Medio)   ← because 0.9 ≤ 0.9286 < 1.6
```

---

## 13. Ejemplo end-to-end: Pilar P3

### Escenario

Capability **P3-C5: Aplicaciones Agénticas** (6 preguntas). Respondida por **1 Arquitecto** + **1 ML Engineer** + **1 Security**. Q1, Q3 y Q6 con `weight = 2.0` (pesos máximos, la frontera de innovación).

### Respuestas

| Pregunta | Pregunta (resumida) | Peso | Arq | ML | Sec | **Avg** |
|---|---|---:|---:|---:|---:|---:|
| `P3-C5-Q1` | Implementación de agentes IA autónomos | **2.0** | L2 (2) | L3 (3) | L1 (1) | **2.0** |
| `P3-C5-Q2` | Coordinación multi-agente (orquestación) | 1.0 | L1 (1) | L2 (2) | L1 (1) | **1.33** |
| `P3-C5-Q3` | Frameworks de tool-use y function calling | **2.0** | L3 (3) | L4 (4) | L2 (2) | **3.0** |
| `P3-C5-Q4` | Memoria persistente de agentes | 1.0 | L2 (2) | L2 (2) | L1 (1) | **1.67** |
| `P3-C5-Q5` | Evaluación continua y safety guardrails | 1.0 | L1 (1) | L2 (2) | L3 (3) | **2.0** |
| `P3-C5-Q6` | Gobernanza y auditoría de acciones de agentes | **2.0** | L1 (1) | L1 (1) | L3 (3) | **1.67** |

### Paso 1: Capability score (P3-C5)

```text
wsum   = (2.00×2.0) + (1.33×1.0) + (3.00×2.0) + (1.67×1.0) + (2.00×1.0) + (1.67×2.0)
       = 4.00 + 1.33 + 6.00 + 1.67 + 2.00 + 3.34
       = 18.34

wtotal = 2.0 + 1.0 + 2.0 + 1.0 + 1.0 + 2.0 = 9.0

P3-C5.score = 18.34 / 9.0 = 2.0378…   →   Etiqueta: L2 Definido
```

### Paso 2: Gap analysis (capability estratégica)

El liderazgo definió `target_level = 4.0` (ambición: liderar en el espacio agéntico), y la capability tiene `weight = 1.5`:

```text
gap_size       = 4.0 − 2.0378 = 1.9622
priority_score = 1.5 × 1.9622 = 2.9433
classification = P0 (Crítico)   ← because 2.9433 ≥ 2.4
```

→ Esta capability **entra en el roadmap de los próximos 30 días** con prioridad máxima.

### Paso 3: Contribución al overall

Si la evaluación completa tiene 28 capabilities activas, P3-C5 con `score = 2.0378` y `weight = 1.5` contribuye:

- Numerador del overall: `+ 2.0378 × 1.5 = +3.0567`
- Denominador del overall: `+ 1.5`

→ Subir P3-C5 de 2.04 a 3.5 (target práctico L3) agregaría `(3.5 − 2.04) × 1.5 = 2.19` al numerador y elevaría el overall en ~`2.19 / wtotal_overall` puntos.

---

## 14. Casos de borde y garantías

| Situación | Garantía |
|---|---|
| `wtotal = 0` (ninguna pregunta respondida) | Devuelve `None` (capability) o `0.0` (pillar/overall). Nunca divide por cero. |
| Puntaje por encima de 4.0 | Imposible por construcción: todos los niveles ∈ [0,4] y los promedios ponderados preservan el rango. |
| Puntaje por debajo de 0.0 | Imposible: `selected_level ∈ [0,4]`. |
| `gap_size` negativo (target ya superado) | Filtrado (no aparece en el roadmap). |
| Multi-respondent con 0 respuestas | La capability se vuelve `None`, sin error. |
| Persona encuestada fuera de la audiencia | Sus respuestas a preguntas no aplicables se **ignoran en la puntuación** pero se almacenan para auditoría. |
| Reprocesamiento (recalcular después de una nueva respuesta) | Idempotente: `POST /api/scoring/trigger` reemplaza las 4 tablas materializadas en una transacción. |

---

## 15. Glosario

| Término | Definición |
|---|---|
| **Question** | Elemento concreto de la evaluación. ID estándar `P[1-3]-C[1-19]-Q[1-99]`. |
| **Capability** | Subdominio funcional. Agrupa 5-7 preguntas. |
| **Pillar** | Dimensión estratégica. Agrupa 9-10 capabilities. P1, P2 o P3. |
| **Level (L0-L4)** | Madurez de una respuesta individual. Entero 0-4. |
| **Score** | Resultado continuo `f64 ∈ [0,4]` producido por agregación. |
| **Weight** | Peso de la pregunta (`[0.5, 2.0]`, predeterminado 1.0) o de la capability. |
| **Threshold** | Cobertura mínima de preguntas respondidas: 25 (warning), 40 (ok). |
| **PE flag** | Marca preguntas críticas para Production Engineering. Generan un subpuntaje paralelo. |
| **Gap** | `target − current` por capability. |
| **Priority score** | `weight × gap`, que clasifica la capability en P0/P1/P2/P3. |
| **Audience** | Audiencias objetivo de la pregunta (developer, sre, security…). Filtra visibilidad en el formulario. |
| **`threshold_status`** | `Ok` / `Warning` / `Blocked`, devuelto junto con el resultado. |

---

**Archivos relacionados:**

- 📄 `scoring-and-calculation.xlsx`: workbook auditable con fórmulas SUMPRODUCT visibles (mismos ejemplos que este doc)
- 🌐 `scoring-calculator.html`: calculadora interactiva standalone (selecciona respuestas, ve puntajes en vivo)
- 📚 `P1-…md`, `P2-…md`, `P3-…md`: preguntas reales de la evaluación con KPI/context/evidence por nivel
