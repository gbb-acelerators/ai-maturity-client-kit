#!/usr/bin/env python3
"""Report multilingual coverage for the AI Maturity client kit.

Every group is required: a missing file fails the check.

- Repository docs are English (`X.md`) with a Portuguese (`X.pt-br.md`) and
  a Spanish (`X.es.md`) copy. Every English doc in scope must have both
  copies, with the same heading levels and the three-language switcher
  line. NOT_TRANSLATED and V1_ARCHIVE list what stays out of scope, and
  why.
- The framework v2 group also checks that framework.v2.json carries every
  text in EN, PT-BR and ES (see scripts/validate_framework_v2.py for the
  full check).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"
ES_TAG = ".es"
EXCLUDED_PARTS = {".git", "dist", "saida", "node_modules"}

# English docs that have no PT-BR/ES copies, and why.
NOT_TRANSLATED = {
    ".github/": "Copilot customization files stay in English by design",
    "kit-en/": "generated from the English quickstart docs",
    "kit-es/": "generated from the Spanish (.es.md) quickstart docs",
    "docs/downloads/": "package downloads",
    "referencia/exemplo-saida/en/": "generated example outputs (English)",
    "referencia/exemplo-saida/es/": "generated example outputs (Spanish)",
    "referencia/exemplo-saida/v1/": "generated v1 example outputs",
    "upgrade-framework-v2.prompt.md": "internal record of the v2 plan",
}
# Frozen v1 archive: English + Portuguese, as published. The v1 question
# bank also has EN and ES versions (coleta/v1/perguntas-para-forms.*).
V1_ARCHIVE = ("referencia/v1/", "coleta/v1/", "formularios/v1/")
# Question banks (Portuguese base with .en and .es versions, checked in
# the question bank groups) and generated example outputs.
LANGUAGE_BASED_NAMES = ("perguntas-para-forms", "-EXEMPLO.md")

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
    "wizard/implementation-guide-inputs.template.json",
] + [
    f"{base}{suffix}.html"
    for base in ("formularios/assessment-v2",
                 "wizard/implementation-guide-wizard",
                 "referencia/calculadora-pontuacao")
    for suffix in ("", ".pt-br", ".es")
] + [
    f"coleta/{name}{suffix}.md"
    for name in ("INSTRUCOES-FORMS", "AI-Maturity-Form-Questions_v2")
    for suffix in ("", ".pt-br", ".es")
] + [
    f"referencia/framework-v2{suffix}" for suffix in
    (".md", ".pt-br.md", ".es.md")
] + [
    f"referencia/dimensoes/{name}{suffix}"
    for name in ["README"] + [f"D{n}" for n in range(1, 10)]
    for suffix in (".md", ".pt-br.md", ".es.md")
]

REQUIRED_REFERENCE_OUTPUTS = [
    f"referencia/exemplo-saida/{sub}{name}.pdf"
    for sub in ("", "en/", "es/")
    for name in ("v2_assessment_summary", "v2_roadmap_g1",
                 "v2_roadmap_g2", "v2_roadmap_g3",
                 "v2_implementation_guide", "comparacao-rodadas")
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


def heading_levels(rel: str) -> list[int]:
    import re

    levels, fence = [], False
    for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            fence = not fence
            continue
        if not fence and re.match(r"^#{1,6} ", line):
            levels.append(len(line.split(" ")[0]))
    return levels


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


def tagged(rel: str, tag: str) -> str:
    stem, ext = rel.rsplit(".", 1)
    return f"{stem}{tag}.{ext}"


def not_translated(rel: str) -> str | None:
    """Reason why an English doc has no copies, or None if in scope."""
    for prefix, reason in NOT_TRANSLATED.items():
        if rel.startswith(prefix):
            return reason
    if LANGUAGE_BASED_NAMES[0] in rel:
        return ("question banks: Portuguese base with .en and .es "
                "versions")
    if rel.endswith(LANGUAGE_BASED_NAMES[1]):
        return "generated example outputs (Portuguese)"
    return None


def english_docs() -> list[str]:
    """English Markdown docs: every .md that is not a language copy."""
    docs = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if set(rel.parts) & EXCLUDED_PARTS:
            continue
        name = rel.name
        if any(f"{tag}." in name for tag in (PT_BR_TAG, ES_TAG, ".en")):
            continue
        docs.append(rel.as_posix())
    return sorted(docs)


def switcher(rel: str, lang: str, langs: tuple[str, ...]) -> str:
    base = rel.rsplit("/", 1)[-1]
    labels = {"en": "English", "pt-br": "Português (Brasil)",
              "es": "Español"}
    files = {"en": base, "pt-br": tagged(base, PT_BR_TAG),
             "es": tagged(base, ES_TAG)}
    return "🌐 " + " · ".join(
        labels[code] if code == lang else f"[{labels[code]}]({files[code]})"
        for code in langs)


def switcher_ok(rel: str, expected: str) -> bool:
    lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    return [ln for ln in lines if ln.startswith("🌐 ")] == [expected]


def print_translated_docs() -> int:
    """Each English doc in scope has PT-BR and ES copies in step."""
    docs = english_docs()
    in_scope = [rel for rel in docs if not not_translated(rel)]
    print(f"\nTranslated docs: EN + PT-BR + ES ({len(in_scope)} docs)")
    problems = 0
    for rel in in_scope:
        v1 = rel.startswith(V1_ARCHIVE)
        langs = ("en", "pt-br") if v1 else ("en", "pt-br", "es")
        files = {"en": rel, "pt-br": tagged(rel, PT_BR_TAG),
                 "es": tagged(rel, ES_TAG)}
        issues = [f"missing {files[code]}" for code in langs
                  if not exists(files[code])]
        if not issues:
            levels = heading_levels(rel)
            issues += [f"headings differ in {files[code]}"
                       for code in langs[1:]
                       if heading_levels(files[code]) != levels]
            issues += [f"switcher line in {files[code]}"
                       for code in langs
                       if not switcher_ok(files[code],
                                          switcher(rel, code, langs))]
        note = " (v1 archive: EN + PT-BR)" if v1 else ""
        print(f"  {'OK' if not issues else 'FAIL'} {rel}{note}")
        for issue in issues:
            print(f"     - {issue}")
        problems += bool(issues)
    groups: dict[str, list[str]] = {}
    for rel in docs:
        reason = not_translated(rel)
        if reason:
            groups.setdefault(reason, []).append(rel)
    print("  Not translated, by design:")
    for reason, paths in groups.items():
        shown = paths[0] if len(paths) == 1 else \
            f"{paths[0]} and {len(paths) - 1} more"
        print(f"     - {reason}: {shown}")
    return problems


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
