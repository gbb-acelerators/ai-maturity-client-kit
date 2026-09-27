# Passo a passo: AI Maturity Assessment

[English](GUIA-PASSO-A-PASSO.md) | Português (Brasil)

Este guia executa o assessment v2 da coleta aos relatorios. O v1 continua disponivel para entradas arquivadas.

## 1. Escolha o fluxo

Use v2 para novos assessments. Use v1 apenas para comparacao historica ou arquivos `respostas.json` existentes sem `metadata.framework_version`.

- Especificacao v2: [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- Formulario v2: [formularios/assessment-v2.html](formularios/assessment-v2.html).
- Instrucoes Forms v2: [coleta/INSTRUCOES-FORMS.pt-br.md](coleta/INSTRUCOES-FORMS.pt-br.md).
- Arquivo v1: [coleta/v1/](coleta/v1/), [formularios/v1/](formularios/v1/), [referencia/v1/](referencia/v1/).

## 2. Prepare as entradas

```bash
make init
```

Esse comando copia `respostas.v2.json.example` para `respostas.json` se o arquivo ainda nao existir.

Voce tambem pode importar uma exportacao do Microsoft Forms:

```bash
make import XLSX=respostas-forms.xlsx
```

O importador detecta v2 por cabecalhos como `R-Q1:` e `D4-Q3:`. Ele detecta v1 pelos IDs arquivados.

## 3. Entenda a estrutura v2

- 5 perguntas de perfil: `R-Q1` a `R-Q5`.
- 61 perguntas pontuadas: `D#-Q#`.
- 9 dimensoes: D1 Estrategia, Politica e Governanca de IA; D2 Habilitacao, Habilidades e Cultura; D3 Planejar, Especificar e Desenhar; D4 Codigo e Engenharia de Contexto; D5 Revisao, Qualidade e Testes; D6 Seguranca e Cadeia de Suprimentos de IA; D7 Entregar e Operar; D8 Fundamentos de Engenharia; D9 Medicao, Valor e AI FinOps.
- Niveis: L0 Nao iniciado, L1 Explorando, L2 Adotando, L3 Escalando, L4 Nativo em IA, mais `NA`.

## 4. Rode o scoring deterministico

```bash
make scores
```

ou:

```bash
python3 scripts/assessment_engine.py all
```

Nao calcule scores manualmente. O engine escreve:

- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`

Cobertura: OK com 37 ou mais perguntas respondidas, WARNING de 25 a 36, BLOCKED abaixo de 25.

## 5. Crie a planilha

```bash
make workbook
```

No v2, o dispatcher escreve `saida/pontuacao-v2-<date>.xlsx`. A planilha inclui formulas e coluna de conferencia do engine. No v1, o dispatcher preserva o fluxo arquivado.

## 6. Gere os relatorios

```bash
make pipeline
```

ou, se os scores ja existem:

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

Arquivos v2:

- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`, D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`, D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`, D6, D7, D8.
- `saida/payload_v2.json`.

Entradas v1 continuam produzindo o conjunto arquivado de 5 PDFs.

## 7. Compare rodadas

```bash
make compare BEFORE=old-respostas.json AFTER=respostas.json
```

O script suporta v2 para v2, v1 para v1 e comparacao indicativa v1 para v2 via `v1_lineage`.

## 8. Use os surveys complementares

O Developer Survey e o Learning and Growth Survey nao mudaram. Eles contextualizam v2 D2, D5 e D9. Se mencionar dimensoes do Developer Survey perto das dimensoes do assessment, use `DS-D#`.

## 9. Valide as fontes do repositorio

```bash
make validate-v2
make validate-docs
make test
```

Veja [CHANGELOG.md](CHANGELOG.md) para o historico de versoes.
