#!/usr/bin/env python3
"""Build per-language ZIP packages for the AI Maturity client kit.

Packaging rule:
- Copilot customization files under .github/ stay in English in every package.
- Client-facing documentation in each package must match the selected language.
- Repository docs are English; the Portuguese and Spanish copies of `X.md` /
  `X.html` live next to it as `X.pt-br.*` and `X.es.*`. The PT and ES packages
  ship those copies under the base names, and no package ships the copy
  names (links to them are rewritten to the base names).
- Multi-language assets ship in every package under their own names, so a
  form can be built in any language: the question banks and the v2 spec
  (the English source is parsed by scripts/spec_to_framework_v2.py).
- Shared scripts, templates, JSON schemas, workbooks, and renderers are reused.
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"
ES_TAG = ".es"
LANGUAGE_TAGS = {"pt": PT_BR_TAG, "es": ES_TAG}

# Every language version of these files ships under its own name in every
# package (question banks and the v2 spec). The English spec also keeps its
# name because scripts/spec_to_framework_v2.py parses it.
MULTILINGUAL_STEMS = ("question-bank", "AI-Maturity-Form-Questions_v2")

COMMON_EXCLUDED_PARTS = {
    ".git",
    ".mypy_cache",
    "__pycache__",
    "dist",
    "build",
    "output",
    "saida",  # output folder of kits before 2.0.2
}

COMMON_EXCLUDED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}

GENERATED_OR_CLIENT_INPUTS = {
    "responses.json",
    "implementation-guide-inputs.json",
    "forms-responses.xlsx",
    "survey-devs-responses.xlsx",
    "survey-learning-responses.xlsx",
    "survey-devs/responses-devs.json",
    "survey-learning/responses-learning.json",
    # Names used by kits before 2.0.2.
    "respostas.json",
    "respostas-forms.xlsx",
    "respostas-survey-devs.xlsx",
    "respostas-survey-learning.xlsx",
    "survey-devs/respostas-devs.json",
    "survey-learning/respostas-learning.json",
}

COPILOT_CUSTOMIZATION_ROOTS = [
    ".github/copilot-instructions.md",
    ".github/agents",
    ".github/prompts",
    ".github/skills",
]

SHARED_RUNTIME_ROOTS = [
    "framework.json",
    "framework.v2.json",
    "framework.v2.schema.json",
    "framework",
    "responses.json.example",
    "responses.v2.json.example",
    "Makefile",
    "scripts",
    "reports/templates",
    "reports/scripts",
    "reports/i18n",
    "reports/sample_payload.json",
    "collection/template-export-forms.xlsx",
    "collection/v1/template-export-forms.xlsx",
    "survey-devs/scripts",
    "survey-devs/mock-responses-devs.json",
    "survey-devs/options.json",
    "survey-devs/template-export-forms-devs.xlsx",
    "survey-learning/scripts",
    "survey-learning/mock-responses-learning.json",
    "survey-learning/template-export-forms-learning.xlsx",
    "wizard/scripts",
    "wizard/implementation-guide-inputs.template.json",
    "reference/scoring-and-calculation.xlsx",
    "reference/branding/tokens-paulasilva-ms.css",
    "collection/v2-mock-forms-export.xlsx",
    "CHANGELOG.md",
    "LICENSE",
]

SHARED_CLIENT_ASSETS = [
    # Question banks referenced by every language package. The canonical IDs
    # remain unchanged so Microsoft Forms exports keep parsing correctly.
    "collection/question-bank.pt-br.md",
    "collection/question-bank.md",
    "collection/question-bank.es.md",
    "collection/AI-Maturity-Form-Questions_v2.md",
    "collection/AI-Maturity-Form-Questions_v2.pt-br.md",
    "collection/AI-Maturity-Form-Questions_v2.es.md",
    "collection/v1",
    "reference/framework-v2.md",
    "survey-devs/question-bank-devs.pt-br.md",
    "survey-devs/question-bank-devs.md",
    "survey-devs/question-bank-devs.es.md",
    "survey-learning/question-bank-learning.pt-br.md",
    "survey-learning/question-bank-learning.md",
    "survey-learning/question-bank-learning.es.md",
    # Source docs and references used by translated guides and fallback flows.
    "collection/FORMS-INSTRUCTIONS.md",
    "survey-devs/FORMS-INSTRUCTIONS-DEVS.md",
    "survey-devs/README.md",
    "survey-devs/MATURITY-RUBRIC.md",
    "survey-learning/FORMS-INSTRUCTIONS-LEARNING.md",
    "survey-learning/README.md",
    "wizard/README.md",
    # Visual helpers referenced by the quickstarts.
    "forms",
    "wizard/implementation-guide-wizard.html",
    "reference/scoring-calculator.html",
]

LANGUAGE_NOTES = {
    "pt": """# Notas de idioma do pacote PT-BR

- Documentação de cliente: Português (Brasil), inclusive os guias de todas
  as pastas. No repositório os documentos são em inglês, com cópias
  `.pt-br` e `.es`; este pacote entrega as versões em português com os
  nomes base (`README.md`, `STEP-BY-STEP.md` etc.).
- A especificação v2 e os bancos de perguntas vêm nos três idiomas, para
  montar o formulário no idioma do cliente:
  `collection/AI-Maturity-Form-Questions_v2.pt-br.md` (português),
  `collection/AI-Maturity-Form-Questions_v2.md` (inglês, a fonte lida por
  `scripts/spec_to_framework_v2.py`) e `.es.md`;
  `collection/question-bank.pt-br.md` (português),
  `collection/question-bank.md` (inglês) e `.es.md`.
- Relatórios são gerados em inglês por padrão. Para PT-BR, defina
  `metadata.language` como `"pt-BR"` em `responses.json`. Os relatórios dos
  surveys aceitam `--lang pt-br` (ou `en`, `es`).
- Os assistentes HTML (formulário offline, wizard e calculadora) têm
  seletor de idioma e abrem em português neste pacote. O material
  arquivado da v1 (docs, bancos, formulários visuais e calculadora) também
  vem em português.
- Ficam em inglês por design os arquivos de customização do Copilot em
  `.github/`: são lidos pelo modelo, e o assistente responde no idioma de
  quem usa.
- JSONs, scripts, templates e workbooks são recursos executáveis ou
  estruturados compartilhados por todos os idiomas.
""",
    "en": """# Language Notes for the English Package

- Client-facing documentation: English, including every folder guide.
  The Portuguese and Spanish copies (`.pt-br` and `.es` files) ship in the
  PT-BR and ES packages under the base names.
- `README.md` and `STEP-BY-STEP.md` at the root are the English quickstart
  and step-by-step guide; the Forms instructions are in
  `collection/FORMS-INSTRUCTIONS.md`.
- The v2 spec and the question banks ship in the three languages, to build
  the form in the client's language:
  `collection/AI-Maturity-Form-Questions_v2.md` (English source, parsed by
  `scripts/spec_to_framework_v2.py`), `.pt-br.md` and `.es.md`;
  `collection/question-bank.md` (English), `.pt-br.md` (Portuguese) and
  `.es.md` (Spanish).
- Reports default to English. Set `metadata.language` to `"pt-BR"` or `"es"`
  in `responses.json` for other languages. Survey reports accept
  `--lang en`, `--lang pt-br` or `--lang es`.
- The HTML helpers (offline form, wizard, calculator) have a language
  selector and follow the browser language. The archived v1 material
  (docs, banks, visual forms and calculator) ships in English too.
- Copilot customization files in `.github/`: intentionally kept in English
  across every language package, because the model reads them; the
  assistant answers in the user's language.
- Shared JSON files, scripts, templates, and workbooks are executable or
  structured assets reused by all languages.
""",
    "es": """# Notas de idioma del paquete Español

- Documentación orientada al cliente en español, incluidas las guías de
  todas las carpetas. En el repositorio los documentos están en inglés, con
  copias `.pt-br` y `.es`; este paquete entrega las versiones en español con
  los nombres base (`README.md`, `STEP-BY-STEP.md`, etc.).
- `README.md` y `STEP-BY-STEP.md` en la raíz son la guía rápida y el paso a
  paso en español; las instrucciones de Forms están en
  `collection/FORMS-INSTRUCTIONS.md`.
- La especificación v2 y los bancos de preguntas van en los tres idiomas,
  para armar el formulario en el idioma del cliente:
  `collection/AI-Maturity-Form-Questions_v2.es.md` (español),
  `collection/AI-Maturity-Form-Questions_v2.md` (inglés, la fuente que lee
  `scripts/spec_to_framework_v2.py`) y `.pt-br.md`;
  `collection/question-bank.es.md` (español),
  `collection/question-bank.md` (inglés) y `.pt-br.md` (portugués).
- Los informes se generan en inglés por defecto. Define `metadata.language`
  como `"es"` en `responses.json` para español. Los informes de las
  encuestas complementarias aceptan `--lang en`, `--lang pt-br` o
  `--lang es`.
- Los asistentes HTML (formulario offline, wizard y calculadora) tienen
  selector de idioma y abren en español en este paquete. El material
  archivado de v1 (docs, bancos, formularios visuales y calculadora)
  también va en español.
- Quedan en inglés por diseño los archivos de customización de Copilot en
  `.github/`: los lee el modelo, y el asistente responde en el idioma de
  quien lo usa.
- JSONs, scripts, plantillas y workbooks compartidos son activos ejecutables
  o estructurados reutilizados por todos los idiomas.
""",
}

ARCHIVE_NAMES = {
    "pt": "ai-maturity-kit-pt.zip",
    "en": "ai-maturity-kit-en.zip",
    "es": "ai-maturity-kit-es.zip",
}

LOCALIZED_TEXT_SUFFIXES = {".md", ".html"}
UNTRANSFORMED_PREFIXES = (".github/", "reports/templates/")
# Only link targets: Markdown `](...)` and HTML `href="..."`.
COPY_LINK_RE = re.compile(r'(\]\(|href=")([^)"\s]+)')
MD_SWITCHER_MARKER = "Português (Brasil)"
HTML_SWITCHER_RE = re.compile(
    r'^\s*<a href="[^"]*" hreflang="[^"]*"[^>]*>[^<]*</a>\s*$'
)


def normalized(path: Path) -> str:
    return path.as_posix()


def tagged(rel: str, tag: str) -> str:
    """`a/X.md` + `.es` -> `a/X.es.md`."""
    stem, ext = posixpath.splitext(rel)
    return f"{stem}{tag}{ext}"


def is_multilingual(rel: str) -> bool:
    return posixpath.basename(rel).startswith(MULTILINGUAL_STEMS)


def family_base(rel: str) -> str | None:
    """English base of a translated copy (`X.pt-br.*` or `X.es.*`).

    A Spanish file counts as a copy only when the Portuguese copy exists
    too. Multilingual assets are never copies.
    """
    if is_multilingual(rel):
        return None
    name = posixpath.basename(rel)
    for tag in (PT_BR_TAG, ES_TAG):
        marker = f"{tag}."
        if marker not in name:
            continue
        base = posixpath.join(posixpath.dirname(rel),
                              name.replace(marker, ".", 1))
        if tag == PT_BR_TAG:
            return base
        pt_copy = ROOT / tagged(base, PT_BR_TAG)
        if (ROOT / base).is_file() and pt_copy.is_file():
            return base
    return None


def is_translated_copy(rel: str) -> bool:
    return family_base(rel) is not None


def package_source(source: Path, lang: str) -> Path:
    """The file whose content ships under `source`'s name in `lang`."""
    tag = LANGUAGE_TAGS.get(lang)
    rel = normalized(source.relative_to(ROOT))
    if not tag or is_multilingual(rel):
        return source
    copy = ROOT / tagged(rel, tag)
    if copy.is_file() and family_base(tagged(rel, tag)) == rel:
        return copy
    return source


def is_common_excluded(rel: str) -> bool:
    parts = set(Path(rel).parts)
    if parts & COMMON_EXCLUDED_PARTS:
        return True
    if Path(rel).name in COMMON_EXCLUDED_NAMES:
        return True
    # Translated copies ship under their base names (write_source()).
    if is_translated_copy(rel):
        return True
    if rel.startswith(".github/workflows/"):
        return True
    if rel.startswith("docs/downloads/"):
        return True
    if rel in GENERATED_OR_CLIENT_INPUTS:
        return True
    return False


def should_include_runtime_file(rel: str) -> bool:
    if is_common_excluded(rel):
        return False
    path = Path(rel)
    if path.suffix.lower() == ".md":
        return rel.startswith(".github/")
    if path.suffix.lower() in {".html", ".htm"}:
        return rel.startswith("reports/templates/")
    return True


def is_switcher_line(line: str, suffix: str) -> bool:
    if suffix == ".md":
        stripped = line.strip()
        return stripped.startswith("🌐 ") and MD_SWITCHER_MARKER in stripped
    return bool(HTML_SWITCHER_RE.match(line))


def strip_language_switchers(text: str, suffix: str) -> str:
    # The other-language file is not shipped, so switcher links would break.
    kept: list[str] = []
    drop_next_blank = False
    for line in text.splitlines(keepends=True):
        if is_switcher_line(line, suffix):
            # Drop one of the blank lines around it (or the blank line
            # after a switcher on the first line).
            drop_next_blank = not kept or not kept[-1].strip()
            continue
        if drop_next_blank and not line.strip():
            drop_next_blank = False
            continue
        drop_next_blank = False
        kept.append(line)
    return "".join(kept)


def rewrite_copy_links(text: str, arcname: str) -> str:
    """Point links to translated copies at the base names.

    No package ships copy names: each one has its own language under the
    base name.
    """
    folder = posixpath.dirname(arcname)

    def fix(match: re.Match) -> str:
        target = match.group(2)
        if re.match(r"^(?:[a-z]+:|#|/|<)", target):
            return match.group(0)
        path, sep, frag = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(folder, path))
        base = family_base(resolved)
        if base is None:
            return match.group(0)
        new_path = posixpath.join(posixpath.dirname(path),
                                  posixpath.basename(base))
        return f"{match.group(1)}{new_path}{sep}{frag}"

    return COPY_LINK_RE.sub(fix, text)


def localize_text(text: str, suffix: str, lang: str, arcname: str) -> str:
    text = rewrite_copy_links(text, arcname)
    return strip_language_switchers(text, suffix)


def write_source(
    zf: zipfile.ZipFile,
    source: Path,
    arcname: str,
    lang: str,
) -> None:
    if arcname in zf.NameToInfo:
        return
    rel = normalized(source.relative_to(ROOT))
    if rel.startswith(UNTRANSFORMED_PREFIXES) and source.suffix != ".md":
        zf.write(source, arcname)
        return
    source = package_source(source, lang)
    suffix = source.suffix.lower()
    if suffix not in LOCALIZED_TEXT_SUFFIXES:
        zf.write(source, arcname)
        return
    text = source.read_text(encoding="utf-8")
    zf.writestr(arcname, localize_text(text, suffix, lang, arcname))


def add_file(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
    *,
    lang: str,
) -> None:
    source = ROOT / source_rel
    if not source.exists() or not source.is_file():
        return
    if is_translated_copy(source_rel):
        return
    write_source(zf, source, dest_rel or source_rel, lang)


def iter_source_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    return sorted(path for path in source.rglob("*") if path.is_file())


def should_add_tree_file(rel: str, runtime_filter: bool) -> bool:
    if runtime_filter and not should_include_runtime_file(rel):
        return False
    return not is_common_excluded(rel)


def destination_for(
    file_path: Path,
    source: Path,
    dest_rel: str | None,
) -> str:
    if not dest_rel:
        return normalized(file_path.relative_to(ROOT))
    if source.is_file():
        return dest_rel
    return normalized(Path(dest_rel) / file_path.relative_to(source))


def add_tree(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
    *,
    lang: str,
    runtime_filter: bool = False,
) -> None:
    source = ROOT / source_rel
    if not source.exists():
        return

    for file_path in iter_source_files(source):
        rel = normalized(file_path.relative_to(ROOT))
        if not should_add_tree_file(rel, runtime_filter):
            continue
        dest = destination_for(file_path, source, dest_rel)
        write_source(zf, file_path, dest, lang)


def add_copilot_customizations(zf: zipfile.ZipFile, lang: str) -> None:
    for root in COPILOT_CUSTOMIZATION_ROOTS:
        add_tree(zf, root, lang=lang)


def add_shared_runtime(zf: zipfile.ZipFile, lang: str) -> None:
    for root in SHARED_RUNTIME_ROOTS:
        add_tree(zf, root, lang=lang, runtime_filter=True)


def add_shared_client_assets(zf: zipfile.ZipFile, lang: str) -> None:
    for root in SHARED_CLIENT_ASSETS:
        add_tree(zf, root, lang=lang)


def validate_packaging_sources() -> None:
    required = (
        COPILOT_CUSTOMIZATION_ROOTS
        + SHARED_RUNTIME_ROOTS
        + SHARED_CLIENT_ASSETS
    )
    missing = [path for path in required if not (ROOT / path).exists()]
    if missing:
        joined = "\n  - ".join(missing)
        raise FileNotFoundError(
            f"Missing packaging source files:\n  - {joined}"
        )


def add_reference_examples(zf: zipfile.ZipFile, lang: str) -> None:
    # The current (v2) example sits in reference/sample-output and the
    # archived v1 example in its v1/ subfolder. JSON outputs are
    # language-neutral; PDFs, workbooks and notes ship per language
    # (PT at the folder root, EN and ES in en/ and es/).
    for base in ("reference/sample-output", "reference/sample-output/v1"):
        example_dir = ROOT / base
        if not example_dir.is_dir():
            continue
        for file_path in sorted(example_dir.glob("*.json")):
            add_file(zf, normalized(file_path.relative_to(ROOT)), lang=lang)
        if lang == "pt":
            for pattern in ("*.pdf", "*.xlsx", "*.md"):
                for file_path in sorted(example_dir.glob(pattern)):
                    rel = normalized(file_path.relative_to(ROOT))
                    if PT_BR_TAG in file_path.name:
                        continue
                    add_file(zf, rel, lang=lang)
        elif (example_dir / lang).is_dir():
            add_tree(zf, f"{base}/{lang}", lang=lang)


def add_documentation(zf: zipfile.ZipFile, lang: str) -> None:
    # 1. Every repository doc: the PT and ES packages get the .pt-br / .es
    #    copies under the base names, the EN package gets the English docs.
    excluded_prefixes = (".github/", ".git/", "docs/", "output/", "dist/")
    for file_path in sorted(ROOT.rglob("*.md")):
        rel = normalized(file_path.relative_to(ROOT))
        if rel.startswith(excluded_prefixes) or is_common_excluded(rel):
            continue
        add_file(zf, rel, lang=lang)
    # 2. HTML helpers: one trilingual file each; the PT and ES packages
    #    get the copy that opens in their language.
    add_tree(zf, "forms", lang=lang)
    add_tree(zf, "reference/v1", lang=lang)
    add_file(zf, "wizard/implementation-guide-wizard.html", lang=lang)
    add_file(zf, "reference/scoring-calculator.html", lang=lang)
    zf.writestr("PACKAGE-LANGUAGE-NOTES.md", LANGUAGE_NOTES[lang])


LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def broken_links(zf: zipfile.ZipFile) -> list[str]:
    """Relative Markdown links that point outside the package."""
    names = set(zf.namelist())
    folders = {"."}
    for name in names:
        parts = name.split("/")[:-1]
        folders.update("/".join(parts[:i]) for i in range(1, len(parts) + 1))
    bad = []
    for name in sorted(n for n in names if n.endswith(".md")):
        text = zf.read(name).decode("utf-8", "ignore")
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#")[0]
            if not target or re.match(r"^(?:[a-z]+:|/|<)", target):
                continue
            resolved = os.path.normpath(
                os.path.join(os.path.dirname(name), target)).rstrip("/")
            if resolved not in names and resolved not in folders:
                bad.append(f"{name}: {match.group(1)}")
    return bad


def assert_no_copy_names(zf: zipfile.ZipFile, archive_path: Path) -> None:
    leaked = [name for name in zf.namelist() if is_translated_copy(name)]
    if leaked:
        joined = "\n  - ".join(leaked)
        raise RuntimeError(
            f"{archive_path.name} contains translated copy names:\n"
            f"  - {joined}"
        )


def build_archive(lang: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / ARCHIVE_NAMES[lang]
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as zf:
        add_copilot_customizations(zf, lang)
        add_shared_runtime(zf, lang)
        add_shared_client_assets(zf, lang)
        add_reference_examples(zf, lang)
        add_documentation(zf, lang)
        assert_no_copy_names(zf, archive_path)
        bad = broken_links(zf)
        if bad:
            joined = "\n  - ".join(bad)
            raise RuntimeError(
                f"{archive_path.name} has broken relative links:\n"
                f"  - {joined}")

    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build PT, EN, and ES language kit ZIPs."
    )
    parser.add_argument(
        "--out",
        default="dist",
        help="Output directory for generated ZIP files.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete the output directory before building.",
    )
    args = parser.parse_args()

    output_dir = (ROOT / args.out).resolve()
    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)

    validate_packaging_sources()
    archives = [build_archive(lang, output_dir) for lang in ("pt", "en", "es")]
    for archive in archives:
        size_mb = archive.stat().st_size / (1024 * 1024)
        try:
            display_path = archive.relative_to(ROOT)
        except ValueError:
            display_path = archive
        print(f"{display_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
