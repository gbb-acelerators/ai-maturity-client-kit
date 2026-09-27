# `relatorios/`: renderizacao de relatorios

O dispatcher de relatorios usa v2 por padrao e v1 para entradas arquivadas.

## Executar

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

O script le `respostas.json::metadata.framework_version` e escolhe o fluxo automaticamente.

## Saidas v2

- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`, D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`, D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`, D6, D7, D8.

## Arquivo v1

Entradas v1 continuam renderizando o conjunto arquivado de 5 PDFs. Nao aponte novos docs de assessment para PDFs de pilares v1, exceto quando a entrada for v1.

## Localizacao

O idioma dos PDFs vem de `respostas.json::metadata.language`: `en`, `pt-BR` ou `es`.
