#!/usr/bin/env python3
"""Build per-language ZIP packages for the AI Maturity client kit.

Packaging rule:
- Copilot customization files under .github/ stay in English in every package.
- Client-facing documentation in each package must match the selected language.
- Repository docs are English; the Portuguese copy of `X.md` / `X.html` lives
  next to it as `X.pt-br.md` / `X.pt-br.html`. The PT package ships those
  copies under the base names, and no package ships `*.pt-br.*` names.
- Shared scripts, templates, JSON schemas, workbooks, and renderers are reused.
"""

from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"

COMMON_EXCLUDED_PARTS = {
    ".git",
    ".mypy_cache",
    "__pycache__",
    "dist",
    "build",
    "saida",
}

COMMON_EXCLUDED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}

GENERATED_OR_CLIENT_INPUTS = {
    "respostas.json",
    "implementation-guide-inputs.json",
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
    "respostas.json.example",
    "respostas.v2.json.example",
    "Makefile",
    "scripts",
    "relatorios/templates",
    "relatorios/scripts",
    "relatorios/i18n",
    "relatorios/sample_payload.json",
    "coleta/template-export-forms.xlsx",
    "coleta/v1/template-export-forms.xlsx",
    "survey-devs/scripts",
    "survey-devs/respostas-mock-devs.json",
    "survey-devs/template-export-forms-devs.xlsx",
    "survey-learning/scripts",
    "survey-learning/respostas-mock-learning.json",
    "survey-learning/template-export-forms-learning.xlsx",
    "wizard/scripts",
    "wizard/implementation-guide-inputs.template.json",
    "referencia/pontuacao-e-calculo.xlsx",
]

SHARED_CLIENT_ASSETS = [
    # Question banks referenced by every language package. The canonical IDs
    # remain unchanged so Microsoft Forms exports keep parsing correctly.
    "coleta/perguntas-para-forms.md",
    "coleta/perguntas-para-forms.en.md",
    "coleta/perguntas-para-forms.es.md",
    "coleta/AI-Maturity-Form-Questions_v2.md",
    "coleta/v1",
    "referencia/framework-v2.md",
    "referencia/framework-v2.es.md",
    "survey-devs/perguntas-para-forms-devs.md",
    "survey-devs/perguntas-para-forms-devs.en.md",
    "survey-devs/perguntas-para-forms-devs.es.md",
    "survey-learning/perguntas-para-forms-learning.md",
    "survey-learning/perguntas-para-forms-learning.en.md",
    "survey-learning/perguntas-para-forms-learning.es.md",
    # Source docs and references used by translated guides and fallback flows.
    "coleta/INSTRUCOES-FORMS.md",
    "survey-devs/INSTRUCOES-FORMS-DEVS.md",
    "survey-devs/README.md",
    "survey-devs/RUBRICA-MATURIDADE.md",
    "survey-learning/INSTRUCOES-FORMS-LEARNING.md",
    "survey-learning/README.md",
    "wizard/README.md",
    # Visual helpers referenced by the quickstarts.
    "formularios",
    "wizard/implementation-guide-wizard.html",
    "referencia/calculadora-pontuacao.html",
]

LANGUAGE_DOCS = {
    "pt": [],
    "en": [
        ("kit-en/README.md", "README.md"),
        ("kit-en/STEP-BY-STEP.md", "STEP-BY-STEP.md"),
        ("kit-en/FORMS-INSTRUCTIONS.md", "FORMS-INSTRUCTIONS.md"),
    ],
    "es": [
        ("kit-es/README.md", "README.md"),
        ("kit-es/PASO-A-PASO.md", "PASO-A-PASO.md"),
        ("kit-es/INSTRUCCIONES-FORMS.md", "INSTRUCCIONES-FORMS.md"),
    ],
}

LANGUAGE_NOTES = {
    "pt": """# Notas de idioma do pacote PT-BR

- Documentação de cliente: Português (Brasil). No repositório os documentos
  são em inglês, com cópias `.pt-br`; este pacote entrega as versões em
  português com os nomes base (`README.md`, `GUIA-PASSO-A-PASSO.md` etc.).
- Relatórios são gerados em inglês por padrão. Para PT-BR, defina
  `metadata.language` como `"pt-BR"` em `respostas.json`. Os relatórios dos
  surveys aceitam `--lang pt-br`.
- Arquivos de customização do Copilot em `.github/`: mantidos em inglês por
  design, para economizar contexto e melhorar compatibilidade.
- JSONs, scripts, templates e workbooks são recursos executáveis ou
  estruturados compartilhados por todos os idiomas.
""",
    "en": """# Language Notes for the English Package

- Client-facing documentation: English. Repository docs are English, with
  Portuguese copies kept as `.pt-br` files; those copies ship only in the
  PT-BR package.
- Reports default to English. Set `metadata.language` to `"pt-BR"` or `"es"`
  in `respostas.json` for other languages. Survey reports accept
  `--lang pt-br`.
- Copilot customization files in `.github/`: intentionally kept in English
  across every language package.
- Shared JSON files, scripts, templates, and workbooks are executable or
  structured assets reused by all languages.
- Canonical question IDs and some internal field names remain in Portuguese
  where required by the scoring framework and production platform mapping.
""",
    "es": """# Notas de idioma del paquete Español

- Documentación orientada al cliente: Español (`README.md`,
  `PASO-A-PASO.md`, `INSTRUCCIONES-FORMS.md`). Las guías de apoyo
  compartidas (`coleta/`, `survey-devs/`, `survey-learning/`, `wizard/`)
  y los asistentes HTML están en inglés.
- Los reportes se generan en inglés por defecto. Define `metadata.language`
  como `"es"` en `respostas.json` para español. Los reportes de los surveys
  aceptan `--lang pt-br`.
- Archivos de customización de Copilot en `.github/`: se mantienen en inglés
  intencionalmente en todos los paquetes.
- JSONs, scripts, templates y workbooks compartidos son activos ejecutables
  o estructurados reutilizados por todos los idiomas.
- IDs canónicos de preguntas y algunos nombres internos permanecen en
  portugués cuando el framework de scoring y el mapeo de plataforma lo
  requieren.
""",
}

ARCHIVE_NAMES = {
    "pt": "ai-maturity-kit-pt.zip",
    "en": "ai-maturity-kit-en.zip",
    "es": "ai-maturity-kit-es.zip",
}

LOCALIZED_TEXT_SUFFIXES = {".md", ".html"}
UNTRANSFORMED_PREFIXES = (".github/", "relatorios/templates/")
# Only link targets: Markdown `](...)` and HTML `href="..."`.
PT_BR_LINK_RE = re.compile(
    r'((?:\]\(|href=")[^)"\s]*?)\.pt-br\.(md|html)'
)
MD_SWITCHER_MARKER = "Português (Brasil)"
HTML_SWITCHER_RE = re.compile(
    r'^\s*<a href="[^"]*" hreflang="[^"]*"[^>]*>[^<]*</a>\s*$'
)


def normalized(path: Path) -> str:
    return path.as_posix()


def is_pt_br_copy(rel: str) -> bool:
    return f"{PT_BR_TAG}." in Path(rel).name


def pt_br_sibling(source: Path) -> Path:
    return source.with_name(f"{source.stem}{PT_BR_TAG}{source.suffix}")


def is_common_excluded(rel: str) -> bool:
    parts = set(Path(rel).parts)
    if parts & COMMON_EXCLUDED_PARTS:
        return True
    if Path(rel).name in COMMON_EXCLUDED_NAMES:
        return True
    # PT copies are shipped under their base names by write_source().
    if is_pt_br_copy(rel):
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
        return rel.startswith("relatorios/templates/")
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
            drop_next_blank = bool(kept) and not kept[-1].strip()
            continue
        if drop_next_blank and not line.strip():
            drop_next_blank = False
            continue
        drop_next_blank = False
        kept.append(line)
    return "".join(kept)


def localize_text(text: str, suffix: str, lang: str) -> str:
    if lang == "pt":
        text = PT_BR_LINK_RE.sub(r"\1.\2", text)
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
    if rel.startswith(UNTRANSFORMED_PREFIXES):
        zf.write(source, arcname)
        return
    if lang == "pt":
        sibling = pt_br_sibling(source)
        if sibling.is_file():
            source = sibling
    suffix = source.suffix.lower()
    if suffix not in LOCALIZED_TEXT_SUFFIXES:
        zf.write(source, arcname)
        return
    text = source.read_text(encoding="utf-8")
    zf.writestr(arcname, localize_text(text, suffix, lang))


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
    if is_pt_br_copy(source_rel):
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
        + [source for docs in LANGUAGE_DOCS.values() for source, _ in docs]
    )
    missing = [path for path in required if not (ROOT / path).exists()]
    if missing:
        joined = "\n  - ".join(missing)
        raise FileNotFoundError(
            f"Missing packaging source files:\n  - {joined}"
        )


def add_reference_examples(zf: zipfile.ZipFile, lang: str) -> None:
    # The current (v2) example sits in referencia/exemplo-saida and the
    # archived v1 example in its v1/ subfolder. JSON outputs are
    # language-neutral; PDFs, workbooks and notes ship per language
    # (PT at the folder root, EN and ES in en/ and es/).
    for base in ("referencia/exemplo-saida", "referencia/exemplo-saida/v1"):
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


def add_pt_documentation(zf: zipfile.ZipFile) -> None:
    excluded_prefixes = (
        ".github/",
        ".git/",
        "docs/",
        "kit-en/",
        "kit-es/",
        "saida/",
        "dist/",
    )
    for file_path in sorted(ROOT.rglob("*.md")):
        rel = normalized(file_path.relative_to(ROOT))
        if rel.startswith(excluded_prefixes) or is_common_excluded(rel):
            continue
        add_file(zf, rel, lang="pt")

    # PT-BR visual guides are intentionally included only in the PT package.
    add_tree(zf, "formularios", lang="pt")
    add_file(zf, "wizard/implementation-guide-wizard.html", lang="pt")
    add_file(zf, "referencia/calculadora-pontuacao.html", lang="pt")


def add_localized_docs(zf: zipfile.ZipFile, lang: str) -> None:
    if lang == "pt":
        add_pt_documentation(zf)
    for source, dest in LANGUAGE_DOCS[lang]:
        add_file(zf, source, dest, lang=lang)
    zf.writestr("PACKAGE-LANGUAGE-NOTES.md", LANGUAGE_NOTES[lang])


def assert_no_pt_br_names(zf: zipfile.ZipFile, archive_path: Path) -> None:
    leaked = [name for name in zf.namelist() if is_pt_br_copy(name)]
    if leaked:
        joined = "\n  - ".join(leaked)
        raise RuntimeError(
            f"{archive_path.name} contains .pt-br names:\n  - {joined}"
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
        add_localized_docs(zf, lang)
        assert_no_pt_br_names(zf, archive_path)

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
