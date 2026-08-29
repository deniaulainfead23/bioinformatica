# Gabarito comentado - Aula 01

Este arquivo é destinado à correção e à explicação da atividade `atividade.md`.

## 1. Quantas sequências existem na base?

**Resposta:** 6 sequências.

**Explicação:** o arquivo possui seis registros, identificados como Amostra_A até Amostra_F.

---

## 2. Todas possuem o mesmo tamanho?

**Resposta:** sim. Todas possuem 20 nucleotídeos.

**Explicação:** em Python, o comprimento de uma sequência pode ser obtido com `len(sequencia)`. Aplicando essa função às seis sequências, o resultado é 20 para todas.

---

## 3. Qual amostra apresenta o maior percentual de G + C?

**Resposta:** **Amostra_F**, com **80% de GC**.

**Explicação:** a sequência possui 8 bases C e 8 bases G. Portanto:

```text
GC = (8 + 8) / 20 × 100 = 80%
```

---

## 4. Qual apresenta o menor percentual de G + C?

**Resposta:** **Amostra_E**, com **20% de GC**.

**Explicação:** a sequência possui 2 bases C e 2 bases G:

```text
GC = (2 + 2) / 20 × 100 = 20%
```

---

## 5. Em uma das sequências, conte quantas vezes aparecem A, T, C e G.

A resposta depende da sequência escolhida. Exemplo com a **Amostra_A**:

```text
A = 5
T = 5
C = 4
G = 6
```

Uma forma de verificar em Python é:

```python
sequencia = "ATGCGTACGTTAGCGGCTAA"

print("A:", sequencia.count("A"))
print("T:", sequencia.count("T"))
print("C:", sequencia.count("C"))
print("G:", sequencia.count("G"))
```

**Explicação:** o método `.count()` conta quantas vezes um determinado caractere aparece em uma string.

---

## 6. Por que uma sequência de DNA pode ser tratada como uma string em uma análise computacional inicial?

**Resposta esperada:** porque ela pode ser representada como uma sequência ordenada de caracteres, normalmente A, T, C e G. Isso permite usar operações computacionais de texto, como contagem, busca, comparação e cálculo de comprimento.

**Explicação importante:** tratar DNA como string é uma representação computacional útil, mas o significado biológico da sequência vai além do texto. Contexto, posição, organismo, qualidade do sequenciamento e anotações também são importantes.

---

## 7. Por que seria inadequado interpretar biologicamente esses dados sem saber de onde vieram, como foram coletados e se passaram por controle de qualidade?

**Resposta esperada:** porque resultados computacionais podem estar corretos do ponto de vista matemático e, ainda assim, não sustentar uma conclusão biológica. É necessário conhecer a origem do dado, o método de coleta, a qualidade, possíveis erros e o contexto experimental.

**Explicação:** em Ciência de Dados e Bioinformática, a qualidade da análise depende da qualidade e da procedência dos dados. Dados incompletos, inconsistentes ou ruidosos podem induzir interpretações erradas.

---

# Desafio-relâmpago

Criar a coluna `at_percentual`:

```python
df["at_percentual"] = df["sequencia"].apply(
    lambda sequencia: 100 * (sequencia.count("A") + sequencia.count("T")) / len(sequencia)
)
```

Resultados esperados:

| Amostra | AT (%) |
|---|---:|
| Amostra_A | 50 |
| Amostra_B | 75 |
| Amostra_C | 25 |
| Amostra_D | 50 |
| Amostra_E | 80 |
| Amostra_F | 20 |

**Maior conteúdo AT:** Amostra_E, com 80%.

---

# Fechamento

Uma resposta adequada é:

> A Bioinformática utiliza **algoritmos, bancos de dados e estatística** para transformar **dados biológicos** em **informação biologicamente interpretável**.

## Observação científica

As sequências da atividade são sintéticas. Os percentuais calculados são corretos para os dados fornecidos, mas não devem ser usados para inferir características de organismos reais.