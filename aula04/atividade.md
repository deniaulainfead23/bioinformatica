# Atividade - Aula 04: transformando sequência em dado

**Tempo sugerido:** 8 a 10 minutos  
**Formato:** duplas ou trios

Use o arquivo [`dados/sequencias_demo.csv`](dados/sequencias_demo.csv) e o notebook [`aula04_colab.ipynb`](aula04_colab.ipynb).

## Missão

Vocês receberam seis sequências biológicas sintéticas. O objetivo é tratá-las como **dados computacionais** e extrair informações simples.

### Questões

1. Quantas sequências existem na base?
2. Todas possuem o mesmo tamanho?
3. Qual amostra apresenta o maior percentual de G + C?
4. Qual apresenta o menor percentual de G + C?
5. Em uma das sequências, conte quantas vezes aparecem A, T, C e G.
6. Explique por que uma sequência de DNA pode ser representada como uma string em uma análise computacional inicial.
7. Por que seria inadequado interpretar biologicamente esses dados sem conhecer sua origem, coleta e controle de qualidade?

## Desafio-relâmpago

Acrescente uma coluna chamada `at_percentual`, contendo a proporção de A + T.

```python
100 * (sequencia.count("A") + sequencia.count("T")) / len(sequencia)
```

## Fechamento

Complete:

> A Bioinformática utiliza __________________ para transformar __________________ em __________________.

## Observação científica

As sequências são sintéticas e foram criadas exclusivamente para ensino. O exercício demonstra operações computacionais sobre sequências, não conclusões biológicas sobre organismos reais.