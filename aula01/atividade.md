# Atividade - Aula 01: transformando sequência em dado

**Tempo sugerido:** 8 a 10 minutos  
**Formato:** duplas ou trios

Use o arquivo [`dados/sequencias_demo.csv`](dados/sequencias_demo.csv) e o script [`pratica.py`](pratica.py).

## Missão

Vocês receberam seis sequências biológicas sintéticas. O objetivo é tratá-las como **dados computacionais** e extrair informações simples.

### Questões

1. Quantas sequências existem na base?
2. Todas possuem o mesmo tamanho?
3. Qual amostra apresenta o maior percentual de G + C?
4. Qual apresenta o menor percentual de G + C?
5. Em uma das sequências, conte quantas vezes aparecem A, T, C e G.
6. Explique por que uma sequência de DNA pode ser tratada como uma string em uma análise computacional inicial.
7. Por que seria inadequado interpretar biologicamente esses dados sem saber de onde vieram, como foram coletados e se passaram por controle de qualidade?

## Desafio-relâmpago

Modifique o código para acrescentar uma coluna chamada `at_percentual`, contendo a proporção de A + T.

Dica:

```python
100 * (sequencia.count("A") + sequencia.count("T")) / len(sequencia)
```

## Fechamento

Complete a frase:

> A Bioinformática não é apenas “programar DNA”. Ela utiliza ______________________ para transformar ______________________ em ______________________.

Uma possível síntese é:

> **algoritmos, bancos de dados e estatística** para transformar **dados biológicos** em **informação biologicamente interpretável**.

## Observação científica

As sequências deste exercício são sintéticas e foram criadas exclusivamente para ensino. O resultado desta atividade demonstra operações computacionais sobre sequências, e não conclusões biológicas sobre organismos reais.
