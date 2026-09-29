# `reports/`: renderização de relatórios

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

O dispatcher de relatórios suporta v2 por padrão e v1 para entradas arquivadas.

## Executar

```bash
python3 reports/scripts/build_payload_and_render.py
```

O script lê `responses.json::metadata.framework_version` e despacha automaticamente. `make pipeline` executa scoring, geração da planilha, construção do payload e renderização.

## Saídas v2

- `output/payload_v2.json`
- `output/v2_assessment_summary.pdf`
- `output/v2_roadmap_g1.pdf`, D1, D2, D9.
- `output/v2_roadmap_g2.pdf`, D3, D4, D5.
- `output/v2_roadmap_g3.pdf`, D6, D7, D8.
- `output/v2_implementation_guide.pdf`.

O sumário inclui a seção 2.2 Evidence cross-checks quando `output/repo-scan.json` ou `output/telemetry.json` existe, e contexto do Developer Survey quando `output/developer-survey-maturity-*.json` existe. O guia de implementação usa `implementation-guide-inputs.json`; campos vazios do wizard aparecem como `to fill with the client`.

## Relatórios de comparação

`make compare BEFORE=old.json AFTER=responses.json` chama `scripts/compare_rounds.py --pdf` e grava `output/round-comparison.pdf`. Ele suporta v2 para v2, baseline indicativo v1 para v2 via linhagem v1, e v1 para v1.

## Arquivo v1

Entradas v1 ainda renderizam o conjunto arquivado de 5 PDFs. Não aponte novos docs de assessment para PDFs de pilar v1 exceto quando a entrada for v1.

## Localização

O idioma do PDF vem de `responses.json::metadata.language`: `en`, `pt-BR` ou `es`. PDFs PT-BR e ES usam vírgula decimal.
