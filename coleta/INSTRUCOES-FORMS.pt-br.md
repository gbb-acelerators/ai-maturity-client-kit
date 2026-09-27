# Como criar o Microsoft Forms do AI Maturity Assessment (v2)

🌐 [English](INSTRUCOES-FORMS.md) · Português (Brasil)

**`🅰️ ASSESSMENT`** · 📖 [🏠 Índice](../README.pt-br.md) · [« Guia passo a passo](../GUIA-PASSO-A-PASSO.pt-br.md) · Você está aqui · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.pt-br.md)

> [!TIP]
> O framework v2 tem **5 perguntas de perfil e 61 perguntas pontuadas em 9 dimensões** (127 elementos no Forms, cerca de 25 a 40 minutos por respondente). As instruções da v1 (158 perguntas) estão arquivadas em [v1/INSTRUCOES-FORMS.pt-br.md](v1/INSTRUCOES-FORMS.pt-br.md).

## Comparação rápida dos caminhos

| Caminho | Tempo de montagem | Quando usar |
| --- | --- | --- |
| **A. Microsoft Forms completo** | 60 a 90 minutos | Vários respondentes por papel; você quer resultados por persona e o alerta de diferença de percepção |
| **B. Piloto com uma dimensão** | 15 minutos | Validar texto e tempo com 3 a 5 pessoas antes do lançamento |
| **C. Template Excel ou SharePoint** | 5 minutos | Workshops, ou quando o Forms não está disponível: uma linha por respondente em [template-export-forms.xlsx](template-export-forms.xlsx) |
| **D. Formulário HTML offline** | Nenhum | Um respondente por vez, sem Microsoft 365: [formularios/assessment-v2.html](../formularios/assessment-v2.html) exporta um `respostas.json` |

## Caminho A: Microsoft Forms completo

1. Abra o banco de perguntas no seu idioma: [perguntas-para-forms.md](perguntas-para-forms.md) (PT-BR), [perguntas-para-forms.en.md](perguntas-para-forms.en.md) (EN) ou [perguntas-para-forms.es.md](perguntas-para-forms.es.md) (ES). Os três são gerados a partir de [framework.v2.json](../framework.v2.json) e têm as mesmas perguntas, opções e âncoras.
2. Acesse <https://forms.office.com>, crie um formulário em branco e dê o nome `AI-Assisted SDLC Maturity Assessment v2 - <Organização>`.
3. Cole o [aviso de privacidade](#aviso-de-privacidade-cole-na-descrição-do-formulário) na descrição do formulário e preencha os colchetes.
4. Adicione **10 seções**: Seção 0 (perfil) e D1 a D9.
5. Seção 0: adicione `R-Q1` a `R-Q5` como **Choice**. Ative **Multiple answers** só em `R-Q3`.
6. Para cada pergunta pontuada, adicione:
   - um **Choice** (resposta única) cujo título começa com o ID e dois-pontos, por exemplo `D4-Q3: Tarefas bem delimitadas são delegadas ...`;
   - as 6 opções, na ordem, mantendo o prefixo `L0` a `L4` e `NA` no início;
   - as linhas **L3 se parece com** e **L4 se parece com** no subtítulo;
   - um **Long Text** opcional com o título exato `Evidence (D4-Q3)`.
7. Opcional: em `...` > `Branching`, deixe quem responde "Executivo" ou "Gerente de produto / programa" em `R-Q1` pular D4 a D7. Perguntas puladas contam como não respondidas, não como `NA`.
8. `Settings`: restrinja à sua organização, ou `Anyone can respond` se for compartilhar por link.
9. Compartilhe o link. Busque **ao menos 3 respondentes por papel**: o heatmap por persona marca grupos menores como amostra pequena, e o alerta de diferença de percepção precisa de 3 executivos e 3 engenheiros hands-on.
10. Com as respostas prontas: `Responses` > `Open in Excel`, baixe o arquivo e rode:

    ```bash
    make import XLSX=respostas-forms.xlsx
    make pipeline
    ```

> [!IMPORTANT]
> O importador encontra cada coluna pelo ID no início do título (`D1-Q1:`, `R-Q1:`) e cada coluna de evidência por `Evidence (<ID>)`. Ele detecta a v2 por esses IDs. Não traduza o rótulo `Evidence (<ID>)` nem os prefixos das opções.

## Caminho B: Piloto com uma dimensão

Crie o formulário com a Seção 0 e uma dimensão (D4 é um bom começo, tem 8 perguntas). Colete 3 a 5 respostas e rode `python3 scripts/import_forms_excel.py <arquivo> --allow-partial`. O motor informa cobertura `BLOCKED` porque menos de 25 perguntas foram respondidas: use o piloto só para validar texto e tempo.

## Caminho C: Template Excel ou SharePoint

1. Copie [template-export-forms.xlsx](template-export-forms.xlsx) para o SharePoint ou OneDrive. O cabeçalho tem o formato exato do export do Forms: colunas de perfil, colunas de resposta `D#-Q#` e colunas `Evidence (D#-Q#)`.
2. Cada respondente preenche uma linha. As respostas devem começar com `L0` a `L4` ou `NA`. `R-Q3` aceita várias opções separadas por `;`.
3. Baixe o arquivo e rode `make import XLSX=<arquivo>`.

Um exemplo preenchido e sintético está em [v2-mock-forms-export.xlsx](v2-mock-forms-export.xlsx) (14 respondentes ilustrativos; não é um cliente real).

## Aviso de privacidade (cole na descrição do formulário)

```text
Este assessment pergunta sobre práticas de engenharia, não sobre desempenho individual.
Coletamos seu papel, o escopo das suas respostas, as ferramentas de IA que você usa, seus anos de experiência e seu tempo hands-on, para mostrar resultados por papel.
Controlador: [organização]. Finalidade: diagnóstico de maturidade em IA e roadmap.
Acesso: [nomes ou time]. Retenção: [prazo], depois os dados são apagados.
Os resultados são agregados; grupos com menos de 3 pessoas são marcados como amostra pequena.
Dúvidas ou pedidos de exclusão: [contato].
```

Combine estes pontos com seu time de privacidade ou jurídico antes do lançamento (LGPD / GDPR); esta checklist não é aconselhamento jurídico:

- **Minimização:** o formulário não precisa de nome nem e-mail. Se o Forms coletar automaticamente, desative ou restrinja o acesso ao export.
- **Armazenamento:** mantenha o `.xlsx`, o `respostas.json` e a pasta `saida/` em armazenamento gerenciado com acesso restrito. `respostas.json` e `saida/` estão no `.gitignore`; nunca faça commit deles.
- **Retenção e exclusão:** apague as respostas do Forms e os arquivos exportados ao fim do prazo de retenção.

## Como as respostas viram scores

O motor ([scripts/assessment_engine.py](../scripts/assessment_engine.py)) segue a seção 8 de [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md): média agrupada por pergunta, média por dimensão, média ponderada das dimensões, faixas de nível semiabertas (L0 abaixo de 0,8, L1 abaixo de 1,6, L2 abaixo de 2,4, L3 abaixo de 3,2, L4 até 4,0), além dos alertas de baixa confiança, risco de amplificação, diferença de percepção e escopo, e a cobertura de evidências.

## Solução de problemas

| Sintoma | Correção |
| --- | --- |
| `No column header starts with a question ID` | Os títulos não começam com `D1-Q1:`. Renomeie no Forms e exporte de novo. |
| `Only N of 61 v2 questions were found` | Alguns títulos perderam o ID. Use `--allow-partial` só em piloto. |
| `unrecognized value at R-Q1` | O texto da opção foi editado. Use o texto exato do banco de perguntas (qualquer um dos 3 idiomas é aceito). |
| O heatmap por persona diz "amostra pequena" | Menos de 3 respondentes naquele papel. Convide mais pessoas ou leia essa coluna com cuidado. |
