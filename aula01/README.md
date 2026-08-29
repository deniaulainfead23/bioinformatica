# Aula 01 - Bioinformática: quando a Biologia vira dado

**Duração:** 50 minutos  
**Público:** estudantes de Tecnologia e Saúde / Biomedicina  
**Abordagem:** introdutória, visual e prática  
**Pré-requisito:** nenhum conhecimento avançado de Biologia Molecular

[▶ Abrir a prática no Google Colab](https://colab.research.google.com/github/deniaulainfead23/bioinformatica/blob/main/aula01/aula01_colab.ipynb)

---

## Objetivos da aula

Ao final da aula, o estudante deverá ser capaz de:

1. explicar, em linguagem simples, o que é Bioinformática;
2. reconhecer a integração entre Biologia, Computação e Estatística;
3. compreender que sequências de DNA e proteínas podem ser tratadas como dados;
4. identificar a função geral de bancos como GenBank/NCBI, UniProt e PDB;
5. reconhecer a importância da qualidade e do pré-processamento dos dados;
6. executar uma análise elementar de sequências com Python.

---

# Roteiro de 50 minutos

## 0-5 min | A pergunta que abre a aula

Comece perguntando:

> **Se eu entregar ao computador uma sequência com milhões de letras A, T, C e G, como ele consegue transformar isso em informação útil para a saúde?**

Explique que essa é uma das perguntas centrais da Bioinformática.

### Frase-chave para o quadro

**Bioinformática = Biologia + Computação + Estatística aplicada a dados biológicos.**

A Bioinformática desenvolve métodos, algoritmos e softwares para obter, armazenar, organizar e analisar dados biológicos.

---

## 5-12 min | O mínimo de Biologia que precisamos saber

Para esta primeira aula, basta trabalhar com quatro ideias:

### DNA

Pode ser representado computacionalmente como uma sequência formada principalmente por quatro símbolos:

```text
A  T  C  G
```

- A = adenina
- T = timina
- C = citosina
- G = guanina

Para o computador, uma sequência pode ser manipulada inicialmente como uma **string**.

```python
sequencia = "ATGCGTACGTTAGC"
```

### Gene

Uma região do DNA que contém informação biológica. Nesta aula não precisamos aprofundar os mecanismos moleculares: o ponto principal é perceber que o gene pode ser representado e analisado computacionalmente por meio de sua sequência e de suas anotações.

### Genoma

Conjunto do material genético de um organismo.

### Proteoma

Conjunto de proteínas e variantes proteicas presentes em determinada condição biológica.

### Ponte com Computação

```text
BIOLOGIA                 COMPUTAÇÃO
DNA                      sequência/string
Gene                     registro + sequência
Genoma                    grande conjunto de dados
Proteína                  sequência de aminoácidos
Banco biológico           banco de dados
Comparar sequências       algoritmo de alinhamento
Experimento virtual       análise in silico
```

---

## 12-18 min | Por que surgiu a Bioinformática?

O avanço do sequenciamento produziu volumes cada vez maiores de dados biológicos. O Projeto Genoma Humano, iniciado em 1990 e concluído em 2003, é um marco importante para mostrar aos estudantes por que armazenar e analisar dados passou a exigir ferramentas computacionais.

Explique assim:

> Produzir o dado não basta. Precisamos armazenar, organizar, comparar, analisar e interpretar esse dado.

Essa necessidade aproxima diretamente a Bioinformática de Banco de Dados, Algoritmos, Ciência de Dados e Estatística.

---

## 18-25 min | Os grandes bancos de dados biológicos

Apresente apenas três nesta primeira aula.

### 1. NCBI / GenBank

**NCBI:** https://www.ncbi.nlm.nih.gov/  
**GenBank:** https://www.ncbi.nlm.nih.gov/genbank/

Use a analogia:

> **GenBank é como uma enorme biblioteca de sequências de DNA.**

Mostre que uma busca pode trazer informações como:

- organismo;
- nome do gene;
- localização;
- sequência de nucleotídeos;
- identificadores;
- referências e anotações.

### 2. UniProt

https://www.uniprot.org/

Banco voltado principalmente para **sequências e anotações de proteínas**.

Analogia:

> Se o GenBank ajuda a procurar DNA, o UniProt é uma grande referência para proteínas.

### 3. Protein Data Bank - PDB

https://www.rcsb.org/

Repositório de estruturas tridimensionais de moléculas biológicas, especialmente proteínas e ácidos nucleicos.

Pergunte:

> Por que a forma tridimensional de uma proteína poderia ser importante na pesquisa de medicamentos?

Não é necessário aprofundar docking nesta primeira aula; apenas introduza a ideia de que estrutura está relacionada a função e interação molecular.

---

## 25-30 min | E onde entra o BLAST?

**BLAST:** https://blast.ncbi.nlm.nih.gov/Blast.cgi

Explique como um “mecanismo de busca por similaridade de sequências”.

Se recebemos uma sequência desconhecida, podemos compará-la com sequências armazenadas em bancos de dados.

O BLAST pode auxiliar em tarefas como:

- encontrar sequências semelhantes;
- identificar possíveis homologias;
- auxiliar na identificação de organismos;
- mapear sequências;
- apoiar anotação de genes e proteínas.

### Analogia para a turma

> O Google procura textos semelhantes às palavras digitadas. O BLAST procura sequências biológicas semelhantes à sequência fornecida.

Nesta aula apenas apresente o conceito. Uma aula posterior pode ser dedicada ao BLAST.

---

## 30-35 min | Antes de analisar: qualidade dos dados

Faça a ponte com Ciência de Dados.

Um algoritmo sofisticado não compensa dados ruins. Bases reais podem apresentar:

- dados ausentes;
- inconsistências;
- ruído;
- redundância;
- formatos diferentes.

Apresente o fluxo:

```text
COLETA
  ↓
PRÉ-PROCESSAMENTO
  ↓
ANÁLISE
  ↓
INTERPRETAÇÃO
```

Cinco processos clássicos de pré-processamento que serão retomados em aulas posteriores:

1. limpeza;
2. integração;
3. redução;
4. transformação;
5. discretização.

Na Bioinformática isso aparece, por exemplo, quando leituras de sequenciamento precisam passar por controle de qualidade antes das análises.

---

## 35-45 min | Prática rápida em Python

Opção mais simples: [abrir diretamente no Google Colab](https://colab.research.google.com/github/deniaulainfead23/bioinformatica/blob/main/aula01/aula01_colab.ipynb).

Também é possível executar `pratica.py` localmente.

### Passo 1 - Uma sequência é um dado

```python
sequencia = "ATGCGTACGTTAGC"

print("Sequência:", sequencia)
print("Tamanho:", len(sequencia))
```

### Passo 2 - Contar bases

```python
for base in "ATCG":
    print(base, sequencia.count(base))
```

### Passo 3 - Conteúdo GC

```python
gc = (sequencia.count("G") + sequencia.count("C")) / len(sequencia) * 100
print(f"GC: {gc:.2f}%")
```

Explique apenas que o **conteúdo GC** mede a proporção de G e C na sequência. Neste momento, o objetivo é mostrar como uma característica biológica pode ser transformada em uma variável quantitativa.

### Passo 4 - Várias sequências

Use o arquivo [`dados/sequencias_demo.csv`](dados/sequencias_demo.csv).

```python
import pandas as pd

df = pd.read_csv("dados/sequencias_demo.csv")

df["tamanho"] = df["sequencia"].str.len()
df["gc_percentual"] = df["sequencia"].apply(
    lambda s: 100 * (s.count("G") + s.count("C")) / len(s)
)

print(df)
```

Pergunte aos alunos:

> **Qual sequência possui maior conteúdo GC?**

Nesse ponto eles já fizeram uma pequena análise bioinformática.

---

## 45-50 min | Fechamento

Peça que os estudantes completem oralmente o fluxo:

```text
DADO BIOLÓGICO
      ↓
ARMAZENAMENTO
      ↓
PRÉ-PROCESSAMENTO
      ↓
ALGORITMO
      ↓
ANÁLISE
      ↓
INFORMAÇÃO BIOLÓGICA
```

### Três perguntas de saída

1. O que diferencia um dado biológico bruto de informação biologicamente útil?
2. Qual é a função de um banco de dados como o GenBank?
3. Por que a qualidade dos dados deve ser verificada antes da análise?

---

# O que NÃO aprofundar nesta primeira aula

Para caber em 50 minutos, deixe para aulas posteriores:

- mecanismos detalhados de replicação, transcrição e tradução;
- alinhamento global/local em profundidade;
- tipos de BLAST;
- FASTQ e scores Phred em detalhes;
- filogenia;
- RNA-Seq;
- docking molecular;
- PCA e SVD.

A primeira aula deve fazer o estudante entender **o problema computacional** antes de estudar as ferramentas especializadas.

---

# Material complementar

## Vídeo de introdução

**Introdução à Bioinformática - Parte 1**  
Discentes Bioinformática UFPR  
https://www.youtube.com/watch?v=9pkCA01EWy0

Use o vídeo como apoio para a definição e contextualização inicial da área, e não como substituto da prática.

---

# Para a professora: explicação em uma frase

> **Bioinformática é a área que usa computação, estatística e métodos quantitativos para armazenar, organizar e analisar dados biológicos, transformando sequências e medições em informação útil para pesquisa e saúde.**
