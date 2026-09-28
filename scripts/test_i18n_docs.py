"""Tests for the trilingual docs: packaging swap and spec copies."""
from __future__ import annotations

import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_language_kits as kits  # noqa: E402
import check_language_coverage as coverage  # noqa: E402
import sync_spec_translations as spec  # noqa: E402

ROOT = kits.ROOT


class FamilyTest(unittest.TestCase):
    def test_translated_copies_map_to_the_english_base(self) -> None:
        self.assertEqual(kits.family_base("README.es.md"), "README.md")
        self.assertEqual(kits.family_base("README.pt-br.md"), "README.md")
        self.assertEqual(
            kits.family_base("formularios/assessment-v2.es.html"),
            "formularios/assessment-v2.html")

    def test_banks_and_spec_keep_their_names(self) -> None:
        self.assertIsNone(
            kits.family_base("coleta/perguntas-para-forms.es.md"))
        self.assertIsNone(kits.family_base(
            "coleta/AI-Maturity-Form-Questions_v2.pt-br.md"))
        self.assertIsNone(kits.family_base(
            "coleta/AI-Maturity-Form-Questions_v2.es.md"))
        self.assertIsNone(kits.family_base("README.md"))

    def test_package_source_picks_the_package_language(self) -> None:
        readme = ROOT / "README.md"
        self.assertEqual(kits.package_source(readme, "es").name,
                         "README.es.md")
        self.assertEqual(kits.package_source(readme, "pt").name,
                         "README.pt-br.md")
        self.assertEqual(kits.package_source(readme, "en").name,
                         "README.md")
        bank = ROOT / "coleta/perguntas-para-forms.md"
        self.assertEqual(kits.package_source(bank, "es"), bank)
        source = ROOT / "coleta/AI-Maturity-Form-Questions_v2.md"
        for lang in ("pt", "es"):
            self.assertEqual(kits.package_source(source, lang), source)

    def test_v1_helpers_ship_in_the_package_language(self) -> None:
        for rel in ("formularios/v1/P1-produtividade-do-desenvolvedor.html",
                    "referencia/v1/calculadora-pontuacao.html",
                    "referencia/v1/P2-ciclo-de-vida-devops.md",
                    "coleta/v1/INSTRUCOES-FORMS.md",
                    "upgrade-framework-v2.prompt.md"):
            source = ROOT / rel
            with self.subTest(rel=rel):
                self.assertEqual(kits.package_source(source, "es").name,
                                 kits.tagged(source.name, ".es"))
                self.assertEqual(kits.package_source(source, "pt").name,
                                 kits.tagged(source.name, ".pt-br"))
                self.assertEqual(kits.package_source(source, "en"), source)
        bank = ROOT / "coleta/v1/perguntas-para-forms.md"
        self.assertEqual(kits.package_source(bank, "es"), bank)

    def test_links_to_copies_point_to_base_names(self) -> None:
        text = ("[a](../survey-devs/README.es.md#x) "
                "[b](perguntas-para-forms.es.md) "
                "[c](AI-Maturity-Form-Questions_v2.es.md) "
                "[d](INSTRUCOES-FORMS.pt-br.md) "
                "[e](https://example.com/README.es.md)")
        out = kits.rewrite_copy_links(text, "coleta/README.md")
        self.assertIn("[a](../survey-devs/README.md#x)", out)
        self.assertIn("[b](perguntas-para-forms.es.md)", out)
        self.assertIn("[c](AI-Maturity-Form-Questions_v2.es.md)", out)
        self.assertIn("[d](INSTRUCOES-FORMS.md)", out)
        self.assertIn("[e](https://example.com/README.es.md)", out)


class SpecCopiesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fw = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
        self.source = (ROOT / spec.SPEC).read_text("utf-8")

    def test_english_sections_round_trip(self) -> None:
        self.assertEqual(
            spec.expected("en", self.fw, self.source, self.source),
            self.source)

    def test_copies_are_up_to_date(self) -> None:
        for lang, rel in spec.COPIES.items():
            current = (ROOT / rel).read_text("utf-8")
            with self.subTest(lang=lang):
                self.assertEqual(
                    spec.expected(lang, self.fw, self.source, current),
                    current)
                self.assertEqual(current.count("\n#### `D"), 61)

    def test_slug_keeps_accents(self) -> None:
        self.assertEqual(spec.slug(" 6. Seção 0: Perfil do respondente"),
                         "6-seção-0-perfil-do-respondente")


class CoverageTest(unittest.TestCase):
    def test_every_doc_has_three_languages(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()) as out:
            problems = coverage.print_translated_docs()
        self.assertEqual(problems, 0, out.getvalue())

    def test_every_html_helper_has_three_languages(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()) as out:
            problems = coverage.print_html_helpers()
        self.assertEqual(problems, 0, out.getvalue())


if __name__ == "__main__":
    unittest.main()
