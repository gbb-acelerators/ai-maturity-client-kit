# `wizard/`: Implementation Guide Wizard (v2 Parte 4)

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

**`WIZARD`** · _Parte 4 personalizada_ · 📖 [🏠 Índice](../README.es.md) · [« Learning Survey](../survey-learning/FORMS-INSTRUCTIONS-LEARNING.es.md) · Estás aquí

Esta carpeta contiene el wizard trilingüe generado y la plantilla JSON usada para personalizar `output/v2_implementation_guide.pdf`. El wizard funciona offline y migra almacenamiento de navegador v1 antiguo.

> [!NOTE]
> Salida en todos los modos: `implementation-guide-inputs.json` en la raíz del kit. `make pipeline` lo detecta automáticamente y lo combina en `payload_v2.json`.

## Las 11 entradas

| # | Entrada | Qué es |
| --- | --- | --- |
| 1 | `executive_steering_committee` | Sponsor, líder de programa, seguridad, finanzas, cambio y representantes champion. |
| 2 | `tpo` | Technology Product Owner u oficina de programa con autoridad de decisión. |
| 3 | `dimension_owners` | Una línea por responsable, por ejemplo `D4: name, role`. |
| 4 | `raci_matrix` | Actividades y asignaciones R/A/C/I. |
| 5 | `communication_plan` | Audiencia, canal, frecuencia y responsable. |
| 6 | `training_plan` | Cohorts, formato, cadencia y criterios. |
| 7 | `adkar_notes` | Notas de Awareness, Desire, Knowledge, Ability y Reinforcement. |
| 8 | `risk_register` | Tabla con Risk, Impact, Mitigation y Owner. |
| 9 | `quick_wins_w1_4` | Primeros 30 días. |
| 10 | `quick_wins_w5_8` | Semanas 5 a 8. |
| 11 | `quick_wins_w9_12` | Semanas 9 a 12. |

## Los 4 modos

### A. Wizard HTML standalone

```bash
open wizard/implementation-guide-wizard.html
```

- Generado por `scripts/generate_v2_tools_html.py`.
- Selector de idioma: EN, PT-BR y ES.
- Guarda borradores en `localStorage`.
- Descarga `implementation-guide-inputs.json` con los 11 campos.
- Los campos vacíos permanecen vacíos y se renderizan como `to fill with the client`.

### B. Plantilla JSON editable

```bash
cp wizard/implementation-guide-inputs.template.json implementation-guide-inputs.json
code implementation-guide-inputs.json
```

La plantilla generada tiene valores vacíos y guía en `_guide` para EN, PT-BR y ES.

### C. Conversación en Copilot Chat

Usa `/implementation-wizard` cuando quieras que Copilot reúna los campos en conversación y guarde el JSON después de la confirmación.

### D. Auto-fill desde el plan de Learning Survey

```bash
python3 wizard/scripts/auto_fill_from_plan.py --lang en
```

El Modo D lee el último `output/training-plan-*.md`, llena 7 de los 11 campos desde el plan de capacitación de Learning Survey y marca el resto como elementos para completar. Usa Champions activos para el comité directivo, el calendario para comunicación, cohorts para capacitación, notas ADKAR y quick wins.

## Archivos

| Archivo | Propósito |
| --- | --- |
| [implementation-guide-wizard.es.html](implementation-guide-wizard.es.html) | Wizard visual standalone generado, que se abre en español, con selector de idioma. En el repositorio, `implementation-guide-wizard.html` sigue el idioma del navegador y `implementation-guide-wizard.pt-br.html` se abre en portugués; cada paquete de idioma entrega su copia como `implementation-guide-wizard.html`. |
| [implementation-guide-inputs.template.json](implementation-guide-inputs.template.json) | Plantilla JSON vacía generada con `_guide`. |
| [scripts/auto_fill_from_plan.py](scripts/auto_fill_from_plan.py) | Auto-fill de Modo D desde salida de Learning Survey. |

## Después de llenar

```bash
ls implementation-guide-inputs.json
make pipeline
```

La Parte 4 v1 también lee el archivo nuevo e ignora los campos que no usa.

## Omitir y reutilizar

- Omitir está permitido. Los campos vacíos se renderizan como `to fill with the client`.
- Puedes llenar solo algunas de las 11 entradas y volver a ejecutar `make pipeline`.
- Volver a ejecutar el wizard sobrescribe solo los campos que vuelvas a guardar.

## Documentación relacionada

- Skill de orquestación: [../.github/skills/implementation-wizard/SKILL.md](../.github/skills/implementation-wizard/SKILL.md)
- Cómo llega el JSON al PDF: [../reports/scripts/wizard_inputs.py](../reports/scripts/wizard_inputs.py)
- Plantilla de guía de implementación v2: [../reports/templates/v2_implementation_guide.html.j2](../reports/templates/v2_implementation_guide.html.j2)
