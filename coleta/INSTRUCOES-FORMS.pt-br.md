# Como criar o Microsoft Forms para o AI Maturity Assessment (v2)

🌐 [English](INSTRUCOES-FORMS.md) · Português (Brasil) · [Español](INSTRUCOES-FORMS.es.md)

**`ASSESSMENT`** · 📖 [🏠 Índice](../README.pt-br.md) · [« Guia passo a passo](../GUIA-PASSO-A-PASSO.pt-br.md) · Você está aqui · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md)

> [!TIP]
> O framework v2 tem **5 perguntas de perfil e 61 perguntas pontuadas em 9 dimensões** (127 elementos no Forms, cerca de 25 a 40 minutos por respondente). As instruções v1 (158 perguntas) estão arquivadas em [v1/INSTRUCOES-FORMS.md](v1/INSTRUCOES-FORMS.md).

## Comparação rápida dos 4 caminhos

| Caminho | Tempo de setup | Quando usar |
| --- | --- | --- |
| **A. Microsoft Forms completo** | 60 a 90 minutos | Vários respondentes por papel; você quer resultados por persona e flag de lacuna de percepção. |
| **B. Piloto com uma dimensão** | 15 minutos | Validar redação e duração com 3 a 5 pessoas antes do lançamento completo. |
| **C. Template Excel ou SharePoint** | 5 minutos | Workshops, ou quando Forms não está disponível: uma linha por respondente em [template-export-forms.xlsx](template-export-forms.xlsx). |
| **D. Formulário HTML offline** | Nenhum | Um respondente por vez, sem Microsoft 365: [formularios/assessment-v2.html](../formularios/assessment-v2.pt-br.html) exporta um `respostas.json` por respondente. |

## Caminho A: Microsoft Forms completo

1. Abra o banco de perguntas no seu idioma: [perguntas-para-forms.en.md](perguntas-para-forms.en.md) (EN), [perguntas-para-forms.md](perguntas-para-forms.md) (PT-BR) ou [perguntas-para-forms.es.md](perguntas-para-forms.es.md) (ES). Os três são gerados a partir de [framework.v2.json](../framework.v2.json) e têm as mesmas perguntas, opções, âncoras e notas de escopo.
2. Acesse <https://forms.office.com>, crie um formulário em branco e nomeie como `AI-Assisted SDLC Maturity Assessment v2 - <Organização>`.
3. Cole o [aviso de privacidade](#aviso-de-privacidade-cole-na-descrição-do-formulário) na descrição do formulário e preencha os colchetes.
4. Adicione **10 seções**: Seção 0 (perfil) e D1 a D9.
5. Seção 0: adicione `R-Q1` a `R-Q5` como **Escolha**. Ative **Múltiplas respostas** somente para `R-Q3`.
6. Para cada pergunta pontuada, adicione:
   - uma **Escolha** (resposta única) cujo título começa com o ID e dois-pontos, por exemplo `D4-Q3: Are well-scoped tasks delegated ...`;
   - as 6 opções, na ordem, mantendo o prefixo `L0` a `L4` e `NA` no início;
   - as linhas **L3 se parece com** e **L4 se parece com**, e a **Nota de escopo** quando a pergunta tiver uma, no subtítulo;
   - um **Texto Longo** opcional com o título exato `Evidence (D4-Q3)`.
7. Opcional: em `...` > `Ramificação`, permita que pessoas que respondem Executive ou Product / program manager em `R-Q1` pulem D4 a D7. Perguntas puladas contam como não respondidas, não como `NA`.
8. `Configurações`: restrinja à sua organização, ou use `Qualquer pessoa pode responder` se compartilhar por link.
9. Compartilhe o link. Busque **pelo menos 3 respondentes por papel**: resumos por persona marcam grupos menores como amostra baixa, e as flags de lacuna de percepção e divergência entre respondentes precisam de respondentes suficientes para serem úteis.
10. Quando houver respostas: `Respostas` > `Abrir no Excel`, baixe o arquivo e rode:

    ```bash
    make import XLSX=respostas-forms.xlsx
    make pipeline
    ```

> [!IMPORTANT]
> O importador encontra cada coluna pelo ID no início do título (`D1-Q1:`, `R-Q1:`) e cada coluna de evidência por `Evidence (<ID>)`. Ele detecta v2 por esses IDs. Não traduza o rótulo `Evidence (<ID>)` nem os prefixos das opções.

## Caminho B: Piloto com uma dimensão

Crie o formulário com a Seção 0 e uma dimensão. D4 é um bom começo, pois tem 8 perguntas. Colete 3 a 5 respostas, depois rode:

```bash
python3 scripts/import_forms_excel.py <file> --allow-partial
```

O engine reporta cobertura `BLOCKED` porque menos de 25 perguntas foram respondidas. Use o piloto apenas para verificar redação e duração.

## Caminho C: Template Excel ou SharePoint

1. Copie [template-export-forms.xlsx](template-export-forms.xlsx) para SharePoint ou OneDrive. A linha de cabeçalho tem o formato exato do export do Forms: colunas de perfil, colunas de resposta `D#-Q#` e colunas `Evidence (D#-Q#)`.
2. Cada respondente preenche uma linha. Respostas devem começar com `L0` a `L4` ou `NA`. `R-Q3` aceita várias opções separadas por `;`.
3. Baixe o arquivo e rode `make import XLSX=<file>`.

Um exemplo preenchido e sintético é [v2-mock-forms-export.xlsx](v2-mock-forms-export.xlsx) (14 respondentes ilustrativos; não é um cliente real).

## Caminho D: Formulário HTML offline mais merge

Use este caminho quando respondentes não puderem acessar o Microsoft Forms ou quando você precisar de um fluxo rápido de workshop.

1. Envie [../formularios/assessment-v2.html](../formularios/assessment-v2.pt-br.html) para cada respondente, ou abra a partir do repositório.
2. O formulário roda offline, suporta EN, PT-BR e ES, mostra a nota de escopo de cada pergunta e exporta um respondente por `respostas.json`.
3. Colete os arquivos exportados em uma pasta, por exemplo `exports/`.
4. Una os arquivos:

   ```bash
   make merge DIR=exports/
   ```

O script de merge atribui IDs únicos `R01`, `R02` e assim por diante. Ele recusa arquivos v1 e recusa organizações mistas exceto quando você passa `--org` ou `--allow-mixed-org` para `scripts/merge_offline_respostas.py`. Ele faz backup de um `respostas.json` existente antes de gravar o arquivo unificado.

Depois rode:

```bash
make pipeline
```

## Aviso de privacidade (cole na descrição do formulário)

```text
Este assessment pergunta sobre práticas de engenharia, não sobre desempenho individual.
Coletamos seu papel, o escopo das respostas, as ferramentas de IA que você usa, seus anos de experiência e seu tempo hands-on, para que resultados possam ser exibidos por papel.
Controlador: [organização]. Finalidade: diagnóstico de maturidade em IA e roadmap.
Acesso: [nomes ou time]. Retenção: [período], depois exclusão.
Resultados são reportados de forma agregada; grupos com menos de 3 pessoas são marcados como amostra baixa.
Dúvidas ou pedidos de exclusão: [contato].
```

Combine estes pontos com seu time de privacidade ou jurídico antes do lançamento (LGPD / GDPR); esta lista não é aconselhamento jurídico:

- **Minimização:** o formulário não precisa de nome nem email. Se o Forms coletar automaticamente, desative ou restrinja o acesso ao export.
- **Armazenamento:** mantenha `.xlsx`, `respostas.json` e `saida/` em armazenamento gerenciado com acesso restrito. `respostas.json` e `saida/` estão no `.gitignore`; nunca faça commit deles.
- **Retenção e exclusão:** exclua as respostas do Forms e os arquivos exportados quando o período de retenção terminar.

## Como respostas viram scores

O engine ([scripts/assessment_engine.py](../scripts/assessment_engine.py)) segue a seção 8 de [AI-Maturity-Form-Questions_v2.pt-br.md](AI-Maturity-Form-Questions_v2.pt-br.md): média agrupada por pergunta, média por dimensão, média ponderada das dimensões, bandas de nível semiabertas, e as flags de baixa confiança, risco de amplificação, lacuna de percepção, divergência entre respondentes, escopo, L3/L4 sem verificação e cobertura de evidência.

Cross-checks opcionais de evidência vêm de `make scan-repos` e `make telemetry`. Eles aparecem no PDF de sumário e são listados como riscos no guia de implementação quando desafiam uma resposta.

## Solução de problemas

| Sintoma | Correção |
| --- | --- |
| `No column header starts with a question ID` | Os títulos das perguntas não começam com `D1-Q1:`. Renomeie no Forms e exporte de novo. |
| `Only N of 61 v2 questions were found` | Alguns títulos perderam o ID. Use `--allow-partial` somente para piloto. |
| `unrecognized value at R-Q1` | O texto da opção foi editado. Use o texto exato do banco de perguntas (qualquer um dos 3 idiomas é aceito). |
| Heatmap de persona diz amostra baixa | Menos de 3 respondentes naquele papel. Convide mais pessoas ou leia a coluna com cuidado. |
| `make merge` recusa um arquivo | Verifique se é um export v1 ou se a organização difere dos outros exports. |
