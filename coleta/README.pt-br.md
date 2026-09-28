# `coleta/`: ativos de coleta

🌐 [English](README.md) · Português (Brasil)

O framework v2 é o fluxo de coleta padrão.

| Ativo | Uso |
| --- | --- |
| [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md) | Especificação v2.0.1 aprovada. |
| [INSTRUCOES-FORMS.md](INSTRUCOES-FORMS.md) | Configuração em inglês de Microsoft Forms, Excel e merge offline para v2. |
| [INSTRUCOES-FORMS.pt-br.md](INSTRUCOES-FORMS.pt-br.md) | Configuração em PT-BR de Microsoft Forms, Excel e merge offline para v2. |
| [perguntas-para-forms.md](perguntas-para-forms.md) | Banco de perguntas v2 gerado em PT-BR. |
| [perguntas-para-forms.en.md](perguntas-para-forms.en.md) | Banco de perguntas v2 gerado em inglês. |
| [perguntas-para-forms.es.md](perguntas-para-forms.es.md) | Banco de perguntas v2 gerado em espanhol. |
| [template-export-forms.xlsx](template-export-forms.xlsx) | Template de importação v2 no formato Microsoft Forms. |
| [v1/](v1/) | Bancos, instruções e template v1 arquivados. |

O formulário offline exporta um respondente por `respostas.json`. Colete os exports em uma pasta e rode `make merge DIR=exports/` antes de `make pipeline`.

Regere os ativos de coleta v2 com:

```bash
make generate-v2
```

Valide sem alterar arquivos com:

```bash
make validate-v2
```
