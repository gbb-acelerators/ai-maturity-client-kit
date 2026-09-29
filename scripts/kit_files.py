"""Default input file of the kit, with the name used by older kits."""
from __future__ import annotations

import sys
from pathlib import Path

RESPONSES = "responses.json"
# Kits before 2.0.2 used Portuguese file names.
LEGACY_RESPONSES = "respostas.json"


def responses_file(kit: Path) -> Path:
    """kit/responses.json, or kit/respostas.json from an older kit."""
    path = Path(kit) / RESPONSES
    legacy = Path(kit) / LEGACY_RESPONSES
    if not path.exists() and legacy.exists():
        print(f"ℹ Reading {legacy.name}, the file name used by older kits. "
              f"Rename it to {RESPONSES}.", file=sys.stderr)
        return legacy
    return path
