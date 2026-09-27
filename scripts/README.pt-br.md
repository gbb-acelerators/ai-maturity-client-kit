# `scripts/`: utilitarios deterministicos do kit

Estes scripts sao a fonte de verdade para importacao, scoring, planilha, comparacao e validacao. Nao calcule saidas do assessment manualmente.

## Comandos principais

| Comando | Uso |
| --- | --- |
| `python3 scripts/import_forms_excel.py respostas-forms.xlsx` | Importa exportacoes do Microsoft Forms. Detecta v2 por cabecalhos `R-Q#` e `D#-Q#` e preserva a importacao v1. |
| `python3 scripts/assessment_engine.py all` | Despacha v2 ou v1 e escreve `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`. |
| `python3 scripts/fill_workbook.py` | Despacha para a planilha v2 ou para o fluxo v1 arquivado. |
| `python3 scripts/compare_rounds.py BEFORE AFTER` | Compara v2 com v2, v1 com v1 ou v1 com v2 indicativo via `v1_lineage`. |
| `python3 scripts/generate_v2_collection.py` | Gera bancos v2, formulario offline e template de importacao. |
| `python3 scripts/make_v2_mock.py` | Gera respostas mock v2 e exportacao Forms ilustrativa. |
| `python3 scripts/validate_framework_v2.py` | Valida `framework.v2.json` contra spec, schema e traducoes. |

## Targets Make

Use `make init`, `make init-v1`, `make import XLSX=...`, `make scores`, `make workbook`, `make pipeline`, `make validate-v2`, `make generate-v2`, `make mock-v2`, `make compare BEFORE=... [AFTER=...]` e `make test`.
