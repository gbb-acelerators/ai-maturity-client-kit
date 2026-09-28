#!/usr/bin/env python3
"""Keep the PT-BR and ES copies of the v2 spec in step with the source.

The English spec (coleta/AI-Maturity-Form-Questions_v2.md) is the source
of truth. Its translations are coleta/AI-Maturity-Form-Questions_v2.pt-br.md
and coleta/AI-Maturity-Form-Questions_v2.es.md:

- the prose (sections 1 to 5, 8 to 11 and the changelog) is translated by
  hand in those files;
- sections 6 and 7 (profile questions and the scored question bank) are
  generated here from framework.v2.json, which carries every text in EN,
  PT-BR and ES;
- the reference list is copied from the English spec.

The same renderer also rebuilds sections 6 and 7 in English, and --check
fails if that differs from the English spec, so the generated sections
keep the exact layout of the source.

Usage:
    python3 scripts/sync_spec_translations.py          # update the copies
    python3 scripts/sync_spec_translations.py --check  # fail if stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = "coleta/AI-Maturity-Form-Questions_v2.md"
COPIES = {
    "pt-br": "coleta/AI-Maturity-Form-Questions_v2.pt-br.md",
    "es": "coleta/AI-Maturity-Form-Questions_v2.es.md",
}

LABELS = {
    "en": {
        "h6": "## 6. Section 0: Respondent profile",
        "intro6": ("Unscored. Used to segment results. Options are specific "
                   "to each question (not the L0 to L4 scale)."),
        "profile": "### Question `{id}`: {title}",
        "multi": "_Type: Choice (multiple answers)._",
        "h7": "## 7. Scored question bank",
        "intro7": (
            "Every scored question uses the six options from "
            "[section 4](#{scale}) and is followed by an optional "
            "`Evidence (<ID>)` Long Text field. Bracketed numbers refer to "
            "[References](#{refs}). **v1 lineage** lists the v1 question "
            "IDs that this question replaces or consolidates; `New` means "
            "no v1 equivalent."),
        "count": "_{n} questions. Why it matters: {why}_",
        "scope": "Scope note",
        "l1_l2": "L1 to L2 look like",
        "l3": "L3 looks like",
        "l4": "L4 looks like",
        "evidence": "Evidence examples",
        "basis": "Basis",
        "lineage": "v1 lineage",
        "new": "New",
        "partial": "(partial)",
    },
    "pt-br": {
        "h6": "## 6. Seção 0: Perfil do respondente",
        "intro6": ("Não pontua. Serve para segmentar os resultados. As "
                   "opções são específicas de cada pergunta (não a escala "
                   "L0 a L4)."),
        "profile": "### Pergunta `{id}`: {title}",
        "multi": "_Tipo: Choice (múltiplas respostas)._",
        "h7": "## 7. Banco de perguntas pontuadas",
        "intro7": (
            "Toda pergunta pontuada usa as seis opções da "
            "[seção 4](#{scale}) e é seguida por um campo opcional de Long "
            "Text `Evidence (<ID>)`. Os números entre colchetes remetem às "
            "[Referências](#{refs}). **Linhagem v1** lista os IDs das "
            "perguntas v1 que esta pergunta substitui ou consolida; `Nova` "
            "significa sem equivalente na v1."),
        "count": "_{n} perguntas. Por que importa: {why}_",
        "scope": "Nota de escopo",
        "l1_l2": "L1 a L2 se parecem com",
        "l3": "L3 se parece com",
        "l4": "L4 se parece com",
        "evidence": "Exemplos de evidência",
        "basis": "Base",
        "lineage": "Linhagem v1",
        "new": "Nova",
        "partial": "(parcial)",
    },
    "es": {
        "h6": "## 6. Sección 0: Perfil de la persona que responde",
        "intro6": ("No puntúa. Sirve para segmentar los resultados. Las "
                   "opciones son propias de cada pregunta (no la escala "
                   "L0 a L4)."),
        "profile": "### Pregunta `{id}`: {title}",
        "multi": "_Tipo: Choice (múltiples respuestas)._",
        "h7": "## 7. Banco de preguntas puntuadas",
        "intro7": (
            "Toda pregunta puntuada usa las seis opciones de la "
            "[sección 4](#{scale}) y va seguida de un campo opcional Long "
            "Text `Evidence (<ID>)`. Los números entre corchetes remiten a "
            "las [Referencias](#{refs}). **Linaje v1** lista los IDs de las "
            "preguntas v1 que esta pregunta reemplaza o consolida; `Nueva` "
            "significa sin equivalente en v1."),
        "count": "_{n} preguntas. Por qué importa: {why}_",
        "scope": "Nota de alcance",
        "l1_l2": "L1 a L2 se ven así",
        "l3": "L3 se ve así",
        "l4": "L4 se ve así",
        "evidence": "Ejemplos de evidencia",
        "basis": "Base",
        "lineage": "Linaje v1",
        "new": "Nueva",
        "partial": "(parcial)",
    },
}

# Notes inside the English basis lists (framework.v2.json keeps them in
# English only). Reference IDs such as LLM06:2025 need no translation.
BASIS_NOTES = {
    "pt-br": {
        "general SDLC scope; no cited source covers AI in CI/CD pipelines "
        "specifically":
            "escopo geral do SDLC; nenhuma fonte citada trata "
            "especificamente de IA em pipelines de CI/CD",
        "push protection and dependency review on every repository are a "
        "kit design choice":
            "push protection e dependency review em todos os repositórios "
            "são uma escolha de design do kit",
        "counterpoint: [56]": "contraponto: [56]",
        "code quality outcome": "resultado de qualidade de código",
        "AI-accessible internal data": "dados internos acessíveis à IA",
    },
    "es": {
        "general SDLC scope; no cited source covers AI in CI/CD pipelines "
        "specifically":
            "alcance general del SDLC; ninguna fuente citada trata "
            "específicamente la IA en pipelines de CI/CD",
        "push protection and dependency review on every repository are a "
        "kit design choice":
            "push protection y dependency review en todos los repositorios "
            "son una decisión de diseño del kit",
        "counterpoint: [56]": "contrapunto: [56]",
        "code quality outcome": "resultado de calidad de código",
        "AI-accessible internal data": "datos internos accesibles para la IA",
    },
}
NOTE_RE = re.compile(r"\(([^()]+)\)")


def slug(heading: str) -> str:
    """GitHub anchor of a heading text (accents are kept)."""
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")


def heading_slug(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return slug(line.lstrip("#"))
    raise ValueError(f"heading starting with {prefix!r} not found")


def basis_text(raw: str, lang: str) -> str:
    notes = BASIS_NOTES.get(lang, {})

    def swap(match: re.Match) -> str:
        inner = match.group(1)
        if inner not in notes and re.search(r"[a-z]{3}", inner) \
                and lang != "en":
            raise KeyError(f"no {lang} translation for basis note {inner!r}")
        return f"({notes.get(inner, inner)})"

    return NOTE_RE.sub(swap, raw)


def lineage(items: list[dict], t: dict) -> str:
    if not items:
        return t["new"]
    return ", ".join(
        item["id"] + (f" {t['partial']}" if item["partial"] else "")
        for item in items)


def render(fw: dict, lang: str, scale: str, refs: str) -> str:
    t = LABELS[lang]
    out = [t["h6"], "", t["intro6"], ""]
    for p in fw["profile_questions"]:
        out += [t["profile"].format(id=p["id"], title=p["title"][lang]), "",
                f"> **{p['text'][lang]}**", ""]
        if p.get("multi"):
            out += [t["multi"], ""]
        out += [f"- {option}" for option in p["options"][lang]] + [""]
    out += ["---", "", t["h7"], "",
            t["intro7"].format(scale=scale, refs=refs), ""]
    for d in fw["dimensions"]:
        out += [f"### {d['id']}: {d['name'][lang]}", "",
                t["count"].format(n=len(d["questions"]),
                                  why=d["why_it_matters"][lang]), ""]
        for q in d["questions"]:
            out += [f"#### `{q['id']}`: {q['title'][lang]}", "",
                    f"> **{q['text'][lang]}**", ""]
            if q.get("scope_note"):
                out.append(f"- **{t['scope']}:** {q['scope_note'][lang]}")
            anchors = q["anchors"]
            if "l1_l2" in anchors:
                out.append(f"- **{t['l1_l2']}:** {anchors['l1_l2'][lang]}")
            out += [f"- **{t['l3']}:** {anchors['l3'][lang]}",
                    f"- **{t['l4']}:** {anchors['l4'][lang]}",
                    f"- **{t['evidence']}:** "
                    f"{q['evidence_examples'][lang]}",
                    f"- **{t['basis']}:** "
                    f"{basis_text(q['basis_text'], lang)}",
                    f"- **{t['lineage']}:** {lineage(q['v1_lineage'], t)}",
                    ""]
    out += ["---", "", ""]
    return "\n".join(out)


def split(text: str) -> tuple[str, str, str, str, str]:
    """(head, sections 6-7, middle, references heading, reference list)."""
    start = text.index("\n## 6. ") + 1
    end = text.index("\n## 8. ", start) + 1
    ref_at = text.rindex("\n## ") + 1
    ref_end = text.index("\n", ref_at) + 1
    return (text[:start], text[start:end], text[end:ref_at],
            text[ref_at:ref_end], text[ref_end:])


def expected(lang: str, fw: dict, source: str, current: str) -> str:
    head, _, middle, ref_heading, _ = split(current)
    ref_list = split(source)[4]
    block = render(fw, lang, heading_slug(current, "## 4. "),
                   slug(ref_heading.lstrip("#")))
    return head + block + middle + ref_heading + ref_list


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if a translated spec is out of date")
    args = ap.parse_args()
    fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
    source = (ROOT / SPEC).read_text("utf-8")
    problems = []
    if expected("en", fw, source, source) != source:
        problems.append(f"{SPEC}: sections 6-7 do not match framework.v2"
                        ".json (run make generate-v2)")
    for lang, rel in COPIES.items():
        path = ROOT / rel
        if not path.exists():
            problems.append(f"{rel}: missing")
            continue
        current = path.read_text("utf-8")
        text = expected(lang, fw, source, current)
        if text == current:
            continue
        if args.check:
            problems.append(f"{rel}: out of date (run python3 "
                            "scripts/sync_spec_translations.py)")
            continue
        path.write_text(text, encoding="utf-8")
        print(f"✓ {rel}")
    if problems:
        print("✗ " + "\n✗ ".join(problems), file=sys.stderr)
        return 1
    if args.check:
        print("✓ translated specs match the English spec and "
              "framework.v2.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
