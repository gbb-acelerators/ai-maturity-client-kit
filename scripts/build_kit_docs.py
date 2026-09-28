#!/usr/bin/env python3
"""Generate kit-en/ and kit-es/ from the canonical docs.

The repository docs are English, with `X.pt-br.md` and `X.es.md` copies
next to them. The EN and ES packages also ship the three quickstart docs
at the package root under names in their own language, so kit-en/ and
kit-es/ are generated here instead of being maintained by hand:

    README.md                     -> kit-en/README.md
    GUIA-PASSO-A-PASSO.md         -> kit-en/STEP-BY-STEP.md
    coleta/INSTRUCOES-FORMS.md    -> kit-en/FORMS-INSTRUCTIONS.md
    README.es.md                  -> kit-es/README.md
    GUIA-PASSO-A-PASSO.es.md      -> kit-es/PASO-A-PASO.md
    coleta/INSTRUCOES-FORMS.es.md -> kit-es/INSTRUCCIONES-FORMS.md

Relative links are rebased so they keep working from kit-en/ and
kit-es/. scripts/check_language_coverage.py checks that every `.pt-br`
and `.es` copy keeps the headings of its English source.

Usage:
    python3 scripts/build_kit_docs.py [--check]
"""
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KITS = {
    "kit-en": {
        "README.md": "kit-en/README.md",
        "GUIA-PASSO-A-PASSO.md": "kit-en/STEP-BY-STEP.md",
        "coleta/INSTRUCOES-FORMS.md": "kit-en/FORMS-INSTRUCTIONS.md",
    },
    "kit-es": {
        "README.es.md": "kit-es/README.md",
        "GUIA-PASSO-A-PASSO.es.md": "kit-es/PASO-A-PASO.md",
        "coleta/INSTRUCOES-FORMS.es.md": "kit-es/INSTRUCCIONES-FORMS.md",
    },
}
SOURCES = {src: dst for kit in KITS.values() for src, dst in kit.items()}
LINK_RE = re.compile(r"(\]\()([^)\s]+)(\))")
SKIP_RE = re.compile(r"^(?:[a-z]+:|#|/|<)")
SWITCHER_RE = re.compile(r"^🌐 .*\n\n?", re.MULTILINE)


def rebase_links(text: str, src: str, dst: str,
                 rename: dict[str, str] | None = None) -> str:
    """Rewrite relative Markdown links from file src to file dst.

    Paths are repository-relative POSIX paths. ``rename`` maps a
    resolved target to the file that replaces it at the destination.
    """
    rename = rename or {}
    src_dir = posixpath.dirname(src)
    dst_dir = posixpath.dirname(dst) or "."

    def fix(match: re.Match) -> str:
        target = match.group(2)
        if SKIP_RE.match(target):
            return match.group(0)
        path, sep, frag = target.partition("#")
        if not path:
            return match.group(0)
        trailing = "/" if path.endswith("/") else ""
        resolved = posixpath.normpath(posixpath.join(src_dir, path))
        resolved = rename.get(resolved, resolved)
        rel = posixpath.relpath(resolved, dst_dir) + trailing
        return f"{match.group(1)}{rel}{sep}{frag}{match.group(3)}"

    return LINK_RE.sub(fix, text)


def outputs() -> dict[Path, str]:
    files = {}
    for kit in KITS.values():
        for src, dst in kit.items():
            text = (ROOT / src).read_text(encoding="utf-8")
            text = SWITCHER_RE.sub("", text, count=1)
            text = rebase_links(text, src, dst, kit)
            note = (f"<!-- Generated from {src} by "
                    f"scripts/build_kit_docs.py. Edit the source, not "
                    f"this file. -->\n")
            files[ROOT / dst] = note + text
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if kit-en/ or kit-es/ is out of date")
    args = ap.parse_args()
    stale = []
    for path, text in outputs().items():
        if args.check:
            if not path.exists() or path.read_text("utf-8") != text:
                stale.append(str(path.relative_to(ROOT)))
            continue
        path.write_text(text, encoding="utf-8")
        print(f"✓ {path.relative_to(ROOT)}")
    if stale:
        print("✗ Out of date (run python3 scripts/build_kit_docs.py): "
              + ", ".join(stale), file=sys.stderr)
        return 1
    if args.check:
        print("✓ kit-en/ and kit-es/ match their sources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
