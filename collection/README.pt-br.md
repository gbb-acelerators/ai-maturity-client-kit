# `collection/`: ativos de coleta

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

O framework v2 é o fluxo de coleta padrão.

| Ativo | Uso |
| --- | --- |
| [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md) | Especificação v2.0.2 aprovada (fonte em inglês). |
| [AI-Maturity-Form-Questions_v2.pt-br.md](AI-Maturity-Form-Questions_v2.pt-br.md) | Tradução da especificação em PT-BR. As seções 6 e 7 e as referências são geradas por `scripts/sync_spec_translations.py`. |
| [AI-Maturity-Form-Questions_v2.es.md](AI-Maturity-Form-Questions_v2.es.md) | Tradução da especificação em espanhol, mantida em dia do mesmo jeito. |
| [FORMS-INSTRUCTIONS.pt-br.md](FORMS-INSTRUCTIONS.pt-br.md) | Configuração de Microsoft Forms, Excel e merge offline para v2. No repositório há também `FORMS-INSTRUCTIONS.md` (inglês) e `FORMS-INSTRUCTIONS.es.md` (espanhol); cada pacote de idioma entrega a sua cópia como `FORMS-INSTRUCTIONS.md`. |
| [question-bank.pt-br.md](question-bank.pt-br.md) | Banco de perguntas v2 gerado em PT-BR. |
| [question-bank.md](question-bank.md) | Banco de perguntas v2 gerado em inglês. |
| [question-bank.es.md](question-bank.es.md) | Banco de perguntas v2 gerado em espanhol. |
| [template-export-forms.xlsx](template-export-forms.xlsx) | Template de importação v2 no formato Microsoft Forms. |
| [v1/](v1/) | Bancos, instruções e template v1 arquivados. |

O formulário offline exporta um respondente por `responses.json`. Colete os exports em uma pasta e rode `make merge DIR=exports/` antes de `make pipeline`.

Regere os ativos de coleta v2 com:

```bash
make generate-v2
```

Valide sem alterar arquivos com:

```bash
make validate-v2
```
