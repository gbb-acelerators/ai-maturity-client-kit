# AI Maturity Assessment kit — convenience targets
#
# All targets are optional shortcuts around the Python entry points so the kit
# remains usable with `python3` directly. There are no compiled artifacts.

PY ?= python3
KIT := $(CURDIR)

.PHONY: help init init-v1 import workbook test scores smoke smoke-cross validate-docs validate-v2 generate-v2 mock-v2 compare build-kits install-deps pipeline clean-saida

help:
	@echo "AI Maturity Assessment kit"
	@echo ""
	@echo "Targets:"
	@echo "  make init          Create respostas.json from the v2 example (keeps an existing file)"
	@echo "  make init-v1       Same, from the archived v1 example (158 questions)"
	@echo "  make import        Import a Microsoft Forms export (XLSX=respostas-forms.xlsx) into respostas.json"
	@echo "  make scores        Compute saida/scores.json, gaps.json and recomendacoes.json (deterministic)"
	@echo "  make workbook      Fill the auditable workbook saida/pontuacao-preenchida-<DATE>.xlsx"
	@echo "  make test          Unit and golden tests (engine, importer, workbook)"
	@echo "  make smoke         End-to-end smoke test (assessment only, no PDFs)"
	@echo "  make smoke-cross   Smoke test including cross-survey enrichment"
	@echo "  make validate-docs Validate JSON content, language coverage and package sources"
	@echo "  make validate-v2   Check framework.v2.json against the spec, schema and translations"
	@echo "  make generate-v2   Regenerate framework.v2.json, question banks, HTML form and template"
	@echo "  make mock-v2       Regenerate the illustrative v2 mock (respostas.v2.json.example)"
	@echo "  make compare       Compare two rounds: BEFORE=old.json AFTER=respostas.json"
	@echo "  make build-kits    Build PT, EN and ES public ZIP packages"
	@echo "  make pipeline      Run full pipeline (scores + payload + PDFs: 4 for v2, 5 for v1)"
	@echo "                    Reports default to English; set metadata.language"
	@echo "                    in respostas.json to pt-BR or es to change it."
	@echo "  make install-deps  Install Python dependencies (jinja2, weasyprint, openpyxl)"
	@echo "  make clean-saida   Remove generated artifacts in saida/"
	@echo ""
	@echo "All commands operate on respostas.json at the workspace root."

init:
	@test -f respostas.json || cp respostas.v2.json.example respostas.json
	@echo "respostas.json ready (an existing file is kept). Run /wizard-implementacao for implementation-guide-inputs.json."

init-v1:
	@test -f respostas.json || cp respostas.json.example respostas.json
	@echo "respostas.json ready (v1). An existing file is kept."

XLSX ?= respostas-forms.xlsx

import:
	@$(PY) scripts/import_forms_excel.py $(XLSX)

scores:
	@$(PY) scripts/assessment_engine.py all

workbook:
	@$(PY) scripts/fill_workbook.py

test:
	@$(PY) -m unittest discover -s scripts -p 'test_*.py'

smoke:
	@$(PY) scripts/smoke_test.py

smoke-cross:
	@$(PY) scripts/smoke_test.py --with-cross-survey

validate-docs:
	@$(PY) -m json.tool docs/content.json >/dev/null
	@$(PY) scripts/check_language_coverage.py
	@$(PY) scripts/validate_framework_v2.py
	@$(PY) scripts/generate_v2_collection.py --check
	@$(PY) scripts/generate_v2_reference.py --check
	@$(PY) scripts/build_language_kits.py --out dist-validate --clean >/dev/null
	@rm -rf dist-validate
	@echo "docs and package sources OK"

validate-v2:
	@$(PY) scripts/validate_framework_v2.py

generate-v2:
	@$(PY) scripts/spec_to_framework_v2.py
	@$(PY) scripts/generate_v2_collection.py
	@$(PY) scripts/generate_v2_reference.py
	@$(PY) scripts/validate_framework_v2.py

mock-v2:
	@$(PY) scripts/make_v2_mock.py

BEFORE ?=
AFTER ?= respostas.json

compare:
	@test -n "$(BEFORE)" || (echo "Usage: make compare BEFORE=old-respostas.json [AFTER=respostas.json]" && exit 1)
	@$(PY) scripts/compare_rounds.py $(BEFORE) $(AFTER)

build-kits:
	@$(PY) scripts/build_language_kits.py --out dist --clean

pipeline:
	@$(PY) scripts/assessment_engine.py all
	@$(PY) relatorios/scripts/build_payload_and_render.py

install-deps:
	@$(PY) -m pip install --user --break-system-packages jinja2 weasyprint openpyxl

clean-saida:
	@find saida -mindepth 1 ! -name '.gitkeep' -delete
	@echo "saida/ cleaned"
