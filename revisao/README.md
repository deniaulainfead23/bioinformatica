# Aula de hoje — Revisão

Resumo de estudo baseado nos tópicos apresentados nas aulas de Tecnologia em Saúde e Bioinformática. O foco aqui é compreender e interpretar a base, com noções introdutórias de Python.

## 1. Organização de uma base tabular

- Cada linha representa um registro ou amostra.
- Cada coluna representa uma variável.
- Antes de interpretar, confira nomes das colunas, tipos de dados e consistência dos registros.

## 2. CSV e pandas

CSV é um formato de tabela em texto. Na base usada em aula, a leitura é feita com pandas:

```python
import pandas as pd

dados = pd.read_csv('base_python0_bioinformatica.csv')
```

O arquivo precisa estar disponível no ambiente de execução, como no Colab.

## 3. Inspeção inicial

- `head()`: mostra as primeiras linhas.
- `shape`: informa a quantidade de linhas e colunas.
- `columns`: mostra os nomes das colunas.
- `info()`: resume a estrutura e os tipos.
- `isna().sum()`: conta valores ausentes por coluna.

Essas verificações ajudam a conhecer a tabela antes de fazer cálculos ou gráficos.

## 4. Qualidade dos dados

Observe se os dados estão completos, consistentes, válidos, coerentes e sem duplicações indevidas. Um valor ausente não equivale automaticamente a zero. Antes de tratar uma ausência, investigue seu significado e documente a decisão.

## 5. Noções introdutórias de Python

Uma variável guarda um valor. `input()` recebe uma entrada e `print()` exibe uma saída. Os tipos abordados incluem texto (`str`), inteiro (`int`), decimal (`float`) e lógico (`bool`). Uma forma simples de organizar um programa é pensar em entrada → processamento → saída.

## 6. Listas, dicionários e repetição

- **Lista:** reúne valores em sequência.
- **Dicionário:** associa chaves a valores.
- **Laço `for`:** repete uma ação para cada elemento de uma coleção.

Esses recursos aparecem nos exemplos introdutórios para organizar e percorrer informações.

## 7. DataFrame e coluna calculada

DataFrame é uma estrutura tabular do pandas. A base pode ser usada para observar registros e criar uma coluna derivada, como o comprimento de uma sequência. A coluna calculada deve ter um significado compatível com os dados de origem.

## 8. Tipos de gráfico

- **Barras:** comparar categorias.
- **Linhas:** observar variação em uma sequência ou período.
- **Setores:** representar partes de um total.
- **Dispersão:** observar a relação entre duas variáveis.
- **Histograma:** visualizar a distribuição dos valores.

Leia título, eixos, unidades e escala para entender o que o gráfico mostra.

## 9. Interpretação responsável

Um gráfico resume os dados observados, mas não prova sozinho que uma variável causou outra. Considere a qualidade e o contexto da base antes de tirar conclusões.

## 10. GenBank e BLAST: onde ficam e como comparar sequências

- **NCBI:** portal com recursos e bancos de dados biológicos.
- **GenBank:** banco de sequências de nucleotídeos, como DNA e RNA.
- **BLAST:** ferramenta que compara uma sequência de interesse com sequências armazenadas em um banco.
- **BLASTN:** pesquisa semelhanças entre sequências de nucleotídeos.
- **BLASTP:** pesquisa semelhanças entre sequências de proteínas.

Lembre-se: GenBank é um banco de dados; BLAST é uma ferramenta de comparação. Uma semelhança pode apoiar uma hipótese, mas sozinha não comprova a função de uma sequência nem estabelece um diagnóstico. Analise o resultado junto do contexto biológico e das demais evidências.

➡️ [Abrir esta revisão em formato de página](./index.html)  
➡️ [Revisão conceitual da Aula 04](../aula04/REVISAO.md)

## Materiais da aula

- [Base CSV usada nos exemplos](../aula05/base_python0_bioinformatica.csv)
- [Notebook introdutório de Python](../aula05/python_0_colab.ipynb)
- [Atividade da Aula 05](../aula05/atividade.md)
- [Gabarito da Aula 05](../aula05/gabarito.md)

