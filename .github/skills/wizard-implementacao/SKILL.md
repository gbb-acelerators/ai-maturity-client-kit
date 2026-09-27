---
name: wizard-implementacao
description: Collects implementation guide inputs for report personalization. Use for "wizard implementacao", "implementation guide", "personalizar relatorio".
---

# Skill: Implementation wizard

Use the existing wizard assets to collect client-specific implementation inputs. Do not alter scoring.

## Relationship to v2

For v2, wizard inputs personalize narrative and implementation guidance after deterministic outputs are generated. They do not change dimension scores, gaps, priority bands, flags, or strategy mappings.

## Procedure

1. Run the wizard flow documented in [wizard/README.md](../../../wizard/README.md).
2. Save `implementation-guide-inputs.json` at the workspace root.
3. Re-render reports:

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

## v1 archive

For v1 inputs, the report dispatcher keeps the archived implementation guide behavior.
