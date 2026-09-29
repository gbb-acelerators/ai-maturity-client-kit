# `collection/`: recursos de recolección

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

Framework v2 es el flujo de recolección predeterminado.

| Recurso | Propósito |
| --- | --- |
| [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md) | Especificación fuente v2.0.2 aprobada (en inglés). |
| [AI-Maturity-Form-Questions_v2.pt-br.md](AI-Maturity-Form-Questions_v2.pt-br.md) | Traducción PT-BR de la especificación. Las secciones 6 y 7 y las referencias son generadas por `scripts/sync_spec_translations.py`. |
| [AI-Maturity-Form-Questions_v2.es.md](AI-Maturity-Form-Questions_v2.es.md) | Traducción al español de la especificación, mantenida sincronizada de la misma manera. |
| [FORMS-INSTRUCTIONS.es.md](FORMS-INSTRUCTIONS.es.md) | Configuración de Microsoft Forms, Excel y combinación offline para v2. En el repositorio también están `FORMS-INSTRUCTIONS.md` (inglés) e `FORMS-INSTRUCTIONS.pt-br.md` (portugués); cada paquete de idioma entrega su copia como `FORMS-INSTRUCTIONS.md`. |
| [question-bank.pt-br.md](question-bank.pt-br.md) | Banco de preguntas v2 generado en PT-BR. |
| [question-bank.md](question-bank.md) | Banco de preguntas v2 generado en inglés. |
| [question-bank.es.md](question-bank.es.md) | Banco de preguntas v2 generado en español. |
| [template-export-forms.xlsx](template-export-forms.xlsx) | Plantilla de importación de Microsoft Forms v2. |
| [v1/](v1/) | Bancos, instrucciones y plantilla v1 archivados. |

El formulario offline exporta una persona encuestada por `responses.json`. Recolecta las exportaciones en una carpeta y ejecuta `make merge DIR=exports/` antes de `make pipeline`.

Regenera los recursos de recolección v2 con:

```bash
make generate-v2
```

Valida sin cambiar archivos con:

```bash
make validate-v2
```
