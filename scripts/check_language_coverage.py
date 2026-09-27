#!/usr/bin/env python3
"""Report multilingual coverage for the AI Maturity client kit.

Every group is required: a missing file fails the check. The framework v2
group also checks that framework.v2.json carries every text in EN, PT-BR
and ES (see scripts/validate_framework_v2.py for the full check). The
translated-docs group
checks that every `X.pt-br.md` / `X.pt-br.html` has its English base file and
vice versa for the docs that have a Portuguese copy.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"
TRANSLATED_DOC_PATTERNS = ["*.pt-br.md", "*.pt-br.html"]
EXCLUDED_PARTS = {".git", "dist", "saida"}

REQUIRED_LOCALIZED_QUESTION_BANKS = [
    "coleta/perguntas-para-forms.en.md",
    "coleta/perguntas-para-forms.es.md",
    "survey-learning/perguntas-para-forms-learning.en.md",
    "survey-learning/perguntas-para-forms-learning.es.md",
    "survey-devs/perguntas-para-forms-devs.en.md",
    "survey-devs/perguntas-para-forms-devs.es.md",
]

REQUIRED_SHARED_CANONICAL_BANKS = [
    "coleta/perguntas-para-forms.md",
    "survey-devs/perguntas-para-forms-devs.md",
    "survey-learning/perguntas-para-forms-learning.md",
]

REQUIRED_LANGUAGE_PACKAGE_DOCS = [
    "kit-en/README.md",
    "kit-en/STEP-BY-STEP.md",
    "kit-en/FORMS-INSTRUCTIONS.md",
    "kit-es/README.md",
    "kit-es/PASO-A-PASO.md",
    "kit-es/INSTRUCCIONES-FORMS.md",
]

REQUIRED_FRAMEWORK_V2 = [
    "framework.v2.json",
    "framework.v2.schema.json",
    "framework/v2/config.json",
    "framework/v2/i18n.pt-br.json",
    "framework/v2/i18n.es.json",
    "formularios/assessment-v2.html",
    "coleta/INSTRUCOES-FORMS.md",
    "coleta/INSTRUCOES-FORMS.pt-br.md",
]

REQUIRED_REFERENCE_OUTPUTS = [
    f"referencia/exemplo-saida/{sub}{name}.pdf"
    for sub in ("", "en/", "es/")
    for name in ("v2_assessment_summary", "v2_roadmap_g1",
                 "v2_roadmap_g2", "v2_roadmap_g3")
]


def framework_v2_languages() -> int:
    import json

    print("\nframework.v2.json language parity")
    path = ROOT / "framework.v2.json"
    if not path.exists():
        print("  MISS framework.v2.json")
        return 1
    missing: list[str] = []

    def walk(node, where: str) -> None:
        if isinstance(node, dict):
            if "en" in node and set(node) <= {"en", "pt-br", "es"}:
                for lang in ("pt-br", "es"):
                    if not node.get(lang):
                        missing.append(f"{where} [{lang}]")
                return
            for key, value in node.items():
                walk(value, f"{where}.{key}" if where else key)
        elif isinstance(node, list):
            for idx, value in enumerate(node):
                ident = value.get("id") if isinstance(value, dict) else None
                walk(value, f"{where}[{ident or idx}]")

    walk(json.loads(path.read_text(encoding="utf-8")), "")
    for item in missing[:10]:
        print(f"  MISS {item}")
    if len(missing) > 10:
        print(f"  ... {len(missing) - 10} more")
    if not missing:
        print("  OK every text has en, pt-br and es")
    return len(missing)


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def print_group(
    title: str,
    paths: list[str],
    *,
    advisory: bool = False,
) -> int:
    print(f"\n{title}")
    missing = 0
    for rel in paths:
        ok = exists(rel)
        if ok:
            marker = "OK"
        elif advisory:
            marker = "WARN"
        else:
            marker = "MISS"
        print(f"  {marker} {rel}")
        if not ok:
            missing += 1
    return missing


def translated_doc_pairs() -> list[tuple[str, str]]:
    """Return (base, pt_br_copy) pairs for every Portuguese doc copy."""
    pairs: set[tuple[str, str]] = set()
    for pattern in TRANSLATED_DOC_PATTERNS:
        for copy in ROOT.rglob(pattern):
            rel_path = copy.relative_to(ROOT)
            if set(rel_path.parts) & EXCLUDED_PARTS:
                continue
            base_name = copy.name.replace(f"{PT_BR_TAG}.", ".", 1)
            base = rel_path.with_name(base_name)
            pairs.add((base.as_posix(), rel_path.as_posix()))
    return sorted(pairs)


def print_translated_docs() -> int:
    pairs = translated_doc_pairs()
    title = f"Translated docs: EN base + PT-BR copy ({len(pairs)} pairs)"
    print(f"\n{title}")
    missing = 0
    for base, copy in pairs:
        # The glob found the copy, so only the base can be missing.
        if exists(base):
            print(f"  OK {base} <-> {copy}")
        else:
            print(f"  MISS {base} (EN base missing for {copy})")
            missing += 1
    return missing


def main() -> int:
    print("AI Maturity kit language coverage")
    required_missing = 0
    required_missing += print_group(
        "Required package docs",
        REQUIRED_LANGUAGE_PACKAGE_DOCS,
    )
    required_missing += print_group(
        "Canonical question banks included in all packages",
        REQUIRED_SHARED_CANONICAL_BANKS,
    )
    required_missing += print_group(
        "Localized survey question banks",
        REQUIRED_LOCALIZED_QUESTION_BANKS,
    )
    required_missing += print_group(
        "Framework v2 sources and collection assets",
        REQUIRED_FRAMEWORK_V2,
    )
    required_missing += framework_v2_languages()
    required_missing += print_group(
        "Reference PDF examples",
        REQUIRED_REFERENCE_OUTPUTS,
    )
    required_missing += print_translated_docs()

    print("\nSummary")
    print(f"  Required missing: {required_missing}")
    return 1 if required_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
