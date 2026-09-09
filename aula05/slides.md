# Slides — Aula 05
## Python 0: análise de dados aplicada à Bioinformática

### 1. Pergunta da aula

Como transformar uma tabela de dados biológicos em informação organizada?

### 2. Fluxo da análise

```text
CARREGAR → CONHECER → PREPARAR → RESUMIR → VISUALIZAR → INTERPRETAR
```

### 3. Primeiro contato com Python

```python
numero_amostras = 24
print(numero_amostras)
```

### 4. Lista e dicionário

```python
bases_dna = ['A', 'T', 'G', 'C']
amostra = {'id': 'A01', 'grupo': 'Controle',
           'sequencia': 'ATGCGTACGTAA'}
```

### 5. A base CSV

Cada linha representa uma amostra. As colunas registram identificação, grupo, coleta, organismo-modelo, sequência, qualidade, temperatura, resposta, laboratório e observação.

### 6. Ler e conferir

```python
tabela = pd.read_csv('base_python0_bioinformatica.csv')
tabela.head()
tabela.shape
tabela.isna().sum()
```

### 7. Preparar sequências

```python
tabela['sequencia'] = tabela['sequencia'].str.upper()
tabela['tamanho'] = tabela['sequencia'].str.len()
```

### 8. Conteúdo GC

```text
GC% = (G + C) / tamanho × 100
```

### 9. Filtros e agrupamentos

```python
tabela[tabela['resposta_percentual'] >= 40]
tabela.groupby('grupo').mean(numeric_only=True)
```

### 10. Escolher o gráfico

- barras: comparar grupos;
- linhas: observar evolução temporal;
- histograma: observar distribuição;
- dispersão: relacionar duas variáveis numéricas.

### 11. Valores ausentes

Um valor ausente não deve ser preenchido automaticamente. Primeiro é necessário descobrir a causa e definir uma regra documentada.

### 12. Desafio

Mostrar Tratamento_A, localizar a maior sequência, calcular temperatura média por laboratório, criar GC médio por grupo e investigar os valores ausentes.

### 13. Síntese

Executar código não basta. É preciso conferir a base, compreender as variáveis e interpretar os resultados com responsabilidade.