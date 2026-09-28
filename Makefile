# AI Maturity Assessment kit — convenience targets
#
# All targets are optional shortcuts around the Python entry points so the kit
# remains usable with `python3` directly. There are no compiled artifacts.

PY ?= python3
KIT := $(CURDIR)

.PHONY: help demo init init-v1 import merge workbook test scores smoke smoke-cross validate-docs validate-v2 generate-v2 mock-v2 examples-v2 compare scan-repos telemetry build-kits install-deps pipeline clean-saida

help:
	@echo "AI Maturity Assessment kit"
	@echo ""
	@echo "Targets:"
	@echo "  make demo          First look: the 5 v2 PDFs from the illustrative mock in saida/demo/"
	@echo "                    (DEMO_LANG=en|pt-BR|es; your respostas.json is not touched)"
	@echo "  make init          Create respostas.json from the v2 example (keeps an existing file)"
	@echo "  make init-v1       Same, from the archived v1 example (158 questions)"
	@echo "  make import        Import a Microsoft Forms export (XLSX=respostas-forms.xlsx) into respostas.json"
	@echo "  make merge         Merge offline-form exports (DIR=exports/) into respostas.json"
	@echo "  make scores        Compute saida/scores.json, gaps.json and recomendacoes.json (deterministic)"
	@echo "  make workbook      Fill the auditable workbook saida/pontuacao-preenchida-<DATE>.xlsx"
	@echo "  make test          Unit and golden tests (engine, importer, workbook)"
	@echo "  make smoke         End-to-end smoke test (assessment only, no PDFs)"
	@echo "  make smoke-cross   Smoke test including cross-survey enrichment"
	@echo "  make validate-docs Validate JSON content, language coverage and package sources"
	@echo "  make validate-v2   Check framework.v2.json against the spec, schema and translations"
	@echo "  make generate-v2   Regenerate framework.v2.json, question banks, HTML form and template"
	@echo "  make mock-v2       Regenerate the illustrative v2 mock (respostas.v2.json.example)"
	@echo "  make examples-v2   Regenerate referencia/exemplo-saida (v2 PDFs, workbook, surveys, cross-checks)"
	@echo "  make compare       Compare two rounds (JSON, MD and PDF): BEFORE=old.json AFTER=respostas.json"
	@echo "  make scan-repos    D4 cross-check: REPOS=~/src (local clones) or ORG=<github-org> (GITHUB_TOKEN)"
	@echo "  make telemetry     D4/D9 cross-check: METRICS=copilot-usage.json [SEATS=200]"
	@echo "  make build-kits    Build PT, EN and ES public ZIP packages"
	@echo "  make pipeline      Run full pipeline (scores + payload + PDFs: 5 for v2, 5 for v1)"
	@echo "                    Reports default to English; set metadata.language"
	@echo "                    in respostas.json to pt-BR or es to change it."
	@echo "  make install-deps  Install Python dependencies (jinja2, weasyprint, openpyxl)"
	@echo "  make clean-saida   Remove generated artifacts in saida/"
	@echo ""
	@echo "All commands operate on respostas.json at the workspace root."

DEMO_LANG ?= en

demo:
	@$(PY) scripts/run_demo.py --lang $(DEMO_LANG)

init:
	@test -f respostas.json || cp respostas.v2.json.example respostas.json
	@echo "respostas.json ready (an existing file is kept). Run /wizard-implementacao for implementation-guide-inputs.json."

init-v1:
	@test -f respostas.json || cp respostas.json.example respostas.json
	@echo "respostas.json ready (v1). An existing file is kept."

XLSX ?= respostas-forms.xlsx

import:
	@$(PY) scripts/import_forms_excel.py $(XLSX)

DIR ?= exports

merge:
	@$(PY) scripts/merge_offline_respostas.py $(DIR)

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
	@$(PY) scripts/generate_v2_tools_html.py --check
	@$(PY) scripts/build_kit_docs.py --check
	@$(PY) scripts/build_language_kits.py --out dist-validate --clean >/dev/null
	@rm -rf dist-validate
	@echo "docs and package sources OK"

validate-v2:
	@$(PY) scripts/validate_framework_v2.py

generate-v2:
	@$(PY) scripts/spec_to_framework_v2.py
	@$(PY) scripts/generate_v2_collection.py
	@$(PY) scripts/generate_v2_reference.py
	@$(PY) scripts/generate_v2_tools_html.py
	@$(PY) scripts/validate_framework_v2.py

mock-v2:
	@$(PY) scripts/make_v2_mock.py

examples-v2:
	@$(PY) scripts/build_v2_examples.py

BEFORE ?=
AFTER ?= respostas.json

compare:
	@test -n "$(BEFORE)" || (echo "Usage: make compare BEFORE=old-respostas.json [AFTER=respostas.json]" && exit 1)
	@$(PY) scripts/compare_rounds.py $(BEFORE) $(AFTER) --pdf

REPOS ?=
ORG ?=

scan-repos:
	@test -n "$(REPOS)$(ORG)" || (echo "Usage: make scan-repos REPOS=~/src  or  make scan-repos ORG=<github-org>" && exit 1)
	@$(PY) scripts/scan_repos_ai_config.py $(if $(REPOS),--path $(REPOS)) $(if $(ORG),--github-org $(ORG))

METRICS ?=
SEATS ?=

telemetry:
	@test -n "$(METRICS)" || (echo "Usage: make telemetry METRICS=copilot-usage.json [SEATS=200]" && exit 1)
	@$(PY) scripts/import_copilot_metrics.py $(METRICS) $(if $(SEATS),--seats $(SEATS))

build-kits:
	@$(PY) scripts/build_language_kits.py --out dist --clean

pipeline:
	@$(PY) scripts/assessment_engine.py all
	@$(PY) relatorios/scripts/build_payload_and_render.py

install-deps:
	@$(PY) -m pip install --user --break-system-packages jinja2 weasyprint openpyxl jsonschema

clean-saida:
	@find saida -mindepth 1 ! -name '.gitkeep' -delete
	@echo "saida/ cleaned"
