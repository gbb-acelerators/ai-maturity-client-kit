#!/usr/bin/env python3
"""Report multilingual coverage for the AI Maturity client kit.

Every group is required: a missing file fails the check.

- Repository docs are English (`X.md`) with a Portuguese (`X.pt-br.md`) and
  a Spanish (`X.es.md`) copy. Every English doc in scope must have both
  copies, with the same heading levels and the three-language switcher
  line, including the archived v1 docs. NOT_TRANSLATED lists what stays
  out of scope, and why.
- HTML helpers follow the same rule: `X.html`, `X.pt-br.html`, `X.es.html`.
- Question banks follow the same rule and every package ships all three
  (see scripts/build_language_kits.py).
- The framework v2 group also checks that framework.v2.json carries every
  text in EN, PT-BR and ES (see scripts/validate_framework_v2.py for the
  full check).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"
ES_TAG = ".es"
EXCLUDED_PARTS = {".git", "dist", "output", "saida", "node_modules"}

# English docs that have no PT-BR/ES copies, and why.
NOT_TRANSLATED = {
    ".github/": "model-facing Copilot files stay in English by design (the "
                "assistant answers in the user's language)",
    "docs/downloads/": "package downloads",
    "reference/sample-output/en/": "generated example outputs (English)",
    "reference/sample-output/es/": "generated example outputs (Spanish)",
    "reference/sample-output/v1/": "generated v1 example outputs",
}
# Folders whose HTML helpers need .pt-br.html and .es.html copies.
HTML_HELPER_ROOTS = ("forms", "wizard", "reference")
# Generated example outputs written in Portuguese.
EXAMPLE_SUFFIX = "-EXAMPLE.md"
# File and folder names are English. These Portuguese words (from the
# names used before kit 2.0.2) must not come back.
PORTUGUESE_NAME_WORDS = re.compile(
    r"coleta|formulario|referencia|relatorio|saida|dimensoes|exemplo|"
    r"resposta|pergunta|instruco|guia|passo|rubrica|maturidade|pontuacao|"
    r"calculo|calculadora|produtividade|desenvolvedor|ciclo-de|plataforma|"
    r"aplicac|comparacao|rodada|telemetria|recomendac|preenchid|plano|"
    r"capacitacao|calcular|gerar|importar|preencher|planilha|recomendar|"
    r"estrategia|implementacao|completo|paso|instruccion",
    re.IGNORECASE)
NAME_SCAN_EXCLUDED = {".git", "dist", "output", "saida", "node_modules",
                      "__pycache__", "downloads"}
# Client files of older kits: read or ignored, never shipped.
LEGACY_CLIENT_FILE = re.compile(r"^respostas([.-].*)?\.(json|xlsx)(\..*)?$")

REQUIRED_QUESTION_BANKS = [
    f"{bank}{suffix}.md"
    for bank in ("collection/question-bank", "collection/v1/question-bank",
                 "survey-devs/question-bank-devs",
                 "survey-learning/question-bank-learning")
    for suffix in ("", ".pt-br", ".es")
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
    for base in ("forms/assessment-v2",
                 "wizard/implementation-guide-wizard",
                 "reference/scoring-calculator")
    for suffix in ("", ".pt-br", ".es")
] + [
    f"collection/{name}{suffix}.md"
    for name in ("FORMS-INSTRUCTIONS", "AI-Maturity-Form-Questions_v2")
    for suffix in ("", ".pt-br", ".es")
] + [
    f"reference/framework-v2{suffix}" for suffix in
    (".md", ".pt-br.md", ".es.md")
] + [
    f"reference/dimensions/{name}{suffix}"
    for name in ["README"] + [f"D{n}" for n in range(1, 10)]
    for suffix in (".md", ".pt-br.md", ".es.md")
]

REQUIRED_REFERENCE_OUTPUTS = [
    f"reference/sample-output/{sub}{name}.pdf"
    for sub in ("", "en/", "es/")
    for name in ("v2_assessment_summary", "v2_roadmap_g1",
                 "v2_roadmap_g2", "v2_roadmap_g3",
                 "v2_implementation_guide", "round-comparison")
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
    if rel.endswith(EXAMPLE_SUFFIX):
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
    langs = ("en", "pt-br", "es")
    for rel in in_scope:
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
        print(f"  {'OK' if not issues else 'FAIL'} {rel}")
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


def print_html_helpers() -> int:
    """Each HTML helper has copies that open in PT-BR and ES."""
    bases = []
    for root in HTML_HELPER_ROOTS:
        for path in sorted((ROOT / root).rglob("*.html")):
            name = path.name
            if f"{PT_BR_TAG}." in name or f"{ES_TAG}." in name:
                continue
            bases.append(path.relative_to(ROOT).as_posix())
    print(f"\nHTML helpers: EN + PT-BR + ES ({len(bases)} helpers)")
    missing = 0
    for rel in bases:
        copies = [tagged(rel, tag) for tag in (PT_BR_TAG, ES_TAG)]
        absent = [c for c in copies if not exists(c)]
        print(f"  {'OK' if not absent else 'MISS'} {rel}")
        for c in absent:
            print(f"     - missing {c}")
        missing += len(absent)
    return missing


def repository_paths() -> list[str]:
    """Tracked files and their folders (all files outside git)."""
    import subprocess

    try:
        out = subprocess.run(
            ["git", "-c", "core.quotepath=false", "ls-files"], cwd=ROOT,
            capture_output=True, text=True, check=True).stdout
        files = [line for line in out.split("\n") if line]
    except (OSError, subprocess.CalledProcessError):
        files = [p.relative_to(ROOT).as_posix()
                 for p in ROOT.rglob("*") if p.is_file()]
    paths = set(files)
    for rel in files:
        parts = rel.split("/")[:-1]
        paths.update("/".join(parts[:i]) for i in range(1, len(parts) + 1))
    return sorted(paths)


def portuguese_names() -> list[str]:
    """Repository paths whose file or folder name is not English."""
    found = []
    for rel in repository_paths():
        parts = rel.split("/")
        if set(parts) & NAME_SCAN_EXCLUDED or \
                LEGACY_CLIENT_FILE.match(parts[-1]):
            continue
        if PORTUGUESE_NAME_WORDS.search(parts[-1]):
            found.append(rel)
    return found


def print_english_names() -> int:
    found = portuguese_names()
    print("\nFile and folder names in English")
    for rel in found:
        print(f"  NOT ENGLISH {rel}")
    if not found:
        print("  OK every file and folder name is English")
    return len(found)


def main() -> int:
    print("AI Maturity kit language coverage")
    required_missing = 0
    required_missing += print_group(
        "Question banks (EN, PT-BR, ES) included in all packages",
        REQUIRED_QUESTION_BANKS,
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
    required_missing += print_html_helpers()
    required_missing += print_english_names()

    print("\nSummary")
    print(f"  Required missing: {required_missing}")
    return 1 if required_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
