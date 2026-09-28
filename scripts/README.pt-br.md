# `scripts/`: utilitários determinísticos do kit

🌐 [English](README.md) · Português (Brasil)

Estes scripts são a fonte da verdade para importação, scoring, geração de planilha, comparação, cross-checks de evidência, helpers gerados, exemplos, empacotamento e validação. Não calcule saídas do assessment manualmente.

## Comandos principais

| Comando | Uso |
| --- | --- |
| `python3 scripts/import_forms_excel.py respostas-forms.xlsx` | Importa exports do Microsoft Forms. Detecta v2 por cabeçalhos `R-Q#` e `D#-Q#` e preserva a importação v1. |
| `python3 scripts/merge_offline_respostas.py exports/` | Une exports do formulário offline, um respondente por arquivo, em `respostas.json`. Recusa arquivos v1 e organizações mistas exceto quando explicitamente permitido. |
| `python3 scripts/assessment_engine.py all` | Despacha v2 ou v1 e grava `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`. |
| `python3 scripts/fill_workbook.py` | Despacha para o gerador de planilha v2 ou fluxo arquivado de planilha v1. |
| `python3 scripts/compare_rounds.py BEFORE AFTER --pdf` | Compara v2 com v2, v1 com v1 ou v1 com v2 indicativo via `v1_lineage`, e grava `saida/comparacao-rodadas.pdf`. |
| `python3 scripts/run_demo.py` | Renderiza os 5 PDFs v2, planilha e JSONs a partir de dados mock ilustrativos em `saida/demo/` sem tocar em `respostas.json`. |
| `python3 scripts/scan_repos_ai_config.py` | Grava `saida/repo-scan.json` a partir de clones locais ou de uma organização GitHub. Usado como cross-check de evidência para D4-Q4 e D4-Q5. |
| `python3 scripts/import_copilot_metrics.py` | Grava `saida/telemetria.json` a partir de exports de métricas de uso do GitHub Copilot. Usado como cross-check de evidência para D4-Q1 e D9-Q1. |
| `python3 scripts/generate_v2_collection.py` | Gera bancos de perguntas v2, formulário offline e template de importação. |
| `python3 scripts/generate_v2_tools_html.py` | Gera a calculadora v2 e o wizard do guia de implementação. `make validate-docs` roda com `--check`. |
| `python3 scripts/generate_v2_reference.py` | Gera [../referencia/framework-v2.pt-br.md](../referencia/framework-v2.pt-br.md) e [../referencia/dimensoes/](../referencia/dimensoes/). |
| `python3 scripts/build_kit_docs.py` | Gera [../kit-en/](../kit-en/) a partir dos docs fonte em inglês e checa docs de pacote. |
| `python3 scripts/build_v2_examples.py` | Regenera exemplos em [../referencia/exemplo-saida/](../referencia/exemplo-saida/), incluindo 5 PDFs por idioma, PDF de comparação, planilha, scan de repositórios, telemetria, surveys e amostra de entradas do wizard. |
| `python3 scripts/test_surveys.py` | Testa parsing e convenções de saída do Developer Survey e Learning Survey. |
| `python3 scripts/validate_framework_v2.py` | Valida `framework.v2.json` contra especificação, schema e traduções. |

Fixtures para exemplos e testes ficam em [fixtures/](fixtures/).

## Targets Make

Use `make install-deps`, `make demo [DEMO_LANG=en|pt-BR|es]`, `make init`, `make init-v1`, `make import XLSX=...`, `make merge DIR=...`, `make scores`, `make workbook`, `make pipeline`, `make compare BEFORE=... AFTER=...`, `make scan-repos REPOS=...`, `make scan-repos ORG=...`, `make telemetry METRICS=...`, `make examples-v2`, `make validate-v2`, `make validate-docs`, `make generate-v2`, `make mock-v2` e `make test`.
