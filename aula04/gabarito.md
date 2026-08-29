# Gabarito comentado - Aula 04

Este arquivo é destinado à correção e à explicação da atividade `atividade.md`.

## 1. Quantas sequências existem na base?

**Resposta:** 6 sequências.

**Explicação:** o arquivo possui seis registros, identificados como Amostra_A até Amostra_F.

## 2. Todas possuem o mesmo tamanho?

**Resposta:** sim. Todas possuem 20 nucleotídeos.

**Explicação:** em Python, `len(sequencia)` informa o comprimento da string.

## 3. Qual amostra apresenta o maior percentual de G + C?

**Resposta:** **Amostra_F**, com **80% de GC**.

```text
GC = (8 + 8) / 20 × 100 = 80%
```

## 4. Qual apresenta o menor percentual de G + C?

**Resposta:** **Amostra_E**, com **20% de GC**.

```text
GC = (2 + 2) / 20 × 100 = 20%
```

## 5. Contagem de A, T, C e G

A resposta depende da sequência escolhida. Exemplo com a **Amostra_A**:

```text
A = 5
T = 5
C = 4
G = 6
```

Em Python:

```python
sequencia = "ATGCGTACGTTAGCGGCTAA"
print("A:", sequencia.count("A"))
print("T:", sequencia.count("T"))
print("C:", sequencia.count("C"))
print("G:", sequencia.count("G"))
```

**Explicação:** `.count()` conta quantas vezes um caractere aparece na string.

## 6. Por que DNA pode ser representado como string?

**Resposta esperada:** porque uma sequência pode ser representada computacionalmente por uma cadeia ordenada de caracteres, como A, T, C e G. Isso permite usar operações de texto para contagem, busca, comparação e cálculo de comprimento.

**Atenção:** essa representação é útil, mas o significado biológico depende também de organismo, posição, qualidade, anotação e contexto experimental.

## 7. Por que não interpretar biologicamente sem contexto e qualidade?

**Resposta esperada:** porque um resultado computacional pode estar matematicamente correto e, ainda assim, não sustentar uma conclusão biológica. É necessário conhecer origem, método de coleta, qualidade e possíveis erros.

## Desafio-relâmpago

```python
df["at_percentual"] = df["sequencia"].apply(
    lambda sequencia: 100 * (sequencia.count("A") + sequencia.count("T")) / len(sequencia)
)
```

| Amostra | AT (%) |
|---|---:|
| Amostra_A | 50 |
| Amostra_B | 75 |
| Amostra_C | 25 |
| Amostra_D | 50 |
| Amostra_E | 80 |
| Amostra_F | 20 |

**Maior conteúdo AT:** Amostra_E, com 80%.

## Fechamento

Uma resposta adequada é:

> A Bioinformática utiliza **algoritmos, bancos de dados e estatística** para transformar **dados biológicos** em **informação biologicamente interpretável**.