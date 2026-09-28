# `formularios/`: formularios de evaluación

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Framework v2 es el valor predeterminado para evaluaciones nuevas.

| Recurso | Propósito |
| --- | --- |
| [assessment-v2.es.html](assessment-v2.es.html) | Formulario offline v2 generado en PT-BR, EN y ES, que se abre en español. Funciona sin internet, muestra la nota de alcance de cada pregunta y exporta una persona encuestada por `respostas.json`. En el repositorio, `assessment-v2.html` sigue el idioma del navegador y `assessment-v2.pt-br.html` se abre en portugués; cada paquete de idioma entrega su copia como `assessment-v2.html`. |
| [v1/](v1/) | Formularios visuales v1 archivados para evaluaciones históricas. |

Usa el flujo offline cuando Microsoft Forms no esté disponible o cuando un workshop necesite recolección local:

```bash
# Recolecta cada respostas.json exportado bajo exports/, luego:
make merge DIR=exports/
make pipeline
```

El formulario v2 sigue [../coleta/AI-Maturity-Form-Questions_v2.es.md](../coleta/AI-Maturity-Form-Questions_v2.es.md): 5 preguntas de perfil (`R-Q1` a `R-Q5`) y 61 preguntas puntuadas (`D#-Q#`) en 9 dimensiones.

Los archivos HTML v1 archivados están en [v1/](v1/). En el repositorio, cada uno tiene la versión en inglés (nombre base), la copia en portugués (`.pt-br.html`) y la copia en español (`.es.html`); cada paquete de idioma entrega su copia con el nombre base:

- [v1/P1-produtividade-do-desenvolvedor.html](v1/P1-produtividade-do-desenvolvedor.es.html)
- [v1/P2-ciclo-de-vida-devops.html](v1/P2-ciclo-de-vida-devops.es.html)
- [v1/P3-plataforma-de-aplicações.html](v1/P3-plataforma-de-aplicações.es.html)
