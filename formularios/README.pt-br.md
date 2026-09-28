# `formularios/`: formulários do assessment

🌐 [English](README.md) · Português (Brasil) · [Español](README.es.md)

O framework v2 é o padrão para novos assessments.

| Ativo | Uso |
| --- | --- |
| [assessment-v2.pt-br.html](assessment-v2.pt-br.html) | Formulário offline v2 gerado em PT-BR, EN e ES, abrindo em português. Ele roda sem internet, mostra a nota de escopo de cada pergunta e exporta um respondente por `respostas.json`. No repositório, `assessment-v2.html` segue o idioma do navegador e `assessment-v2.es.html` abre em espanhol; cada pacote de idioma entrega a sua cópia como `assessment-v2.html`. |
| [v1/](v1/) | Formulários visuais v1 arquivados para assessments históricos. |

Use o fluxo offline quando o Microsoft Forms não estiver disponível ou quando um workshop precisar de coleta local:

```bash
# Colete cada respostas.json exportado em exports/, depois:
make merge DIR=exports/
make pipeline
```

O formulário v2 segue [../coleta/AI-Maturity-Form-Questions_v2.pt-br.md](../coleta/AI-Maturity-Form-Questions_v2.pt-br.md): 5 perguntas de perfil (`R-Q1` a `R-Q5`) e 61 perguntas pontuadas (`D#-Q#`) em 9 dimensões.

Arquivos HTML v1 arquivados ficam em [v1/](v1/). No repositório, cada um tem a versão em inglês (nome base), a cópia em português (`.pt-br.html`) e a cópia em espanhol (`.es.html`); cada pacote de idioma entrega a sua cópia com o nome base:

- [v1/P1-produtividade-do-desenvolvedor.html](v1/P1-produtividade-do-desenvolvedor.pt-br.html)
- [v1/P2-ciclo-de-vida-devops.html](v1/P2-ciclo-de-vida-devops.pt-br.html)
- [v1/P3-plataforma-de-aplicações.html](v1/P3-plataforma-de-aplicações.pt-br.html)
