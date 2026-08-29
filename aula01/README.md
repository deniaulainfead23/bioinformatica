# Aula 01 - Bioinformática: quando diferentes áreas se encontram

**Duração:** 50 minutos  
**Público:** estudantes de Tecnologia e Saúde / Biomedicina  
**Abordagem:** introdutória, interdisciplinar e progressiva  
**Pré-requisito:** nenhum conhecimento prévio de Python ou Bioinformática

[▶ Abrir a prática no Google Colab](https://colab.research.google.com/github/deniaulainfead23/bioinformatica/blob/main/aula01/aula01_colab.ipynb)

---

# Ideia central da aula

Antes de apresentar ferramentas, bancos de dados ou programação, o estudante precisa compreender **o que é Bioinformática, por que ela existe e quem trabalha nessa área**.

A sequência didática desta aula será:

```text
O QUE É BIOINFORMÁTICA?
          ↓
QUAIS ÁREAS PARTICIPAM?
          ↓
O QUE CADA PROFISSIONAL CONTRIBUI?
          ↓
QUAIS TECNOLOGIAS SÃO UTILIZADAS?
          ↓
POR QUE EXISTEM BANCOS DE DADOS BIOLÓGICOS?
          ↓
COMO A COMPUTAÇÃO ANALISA ESSES DADOS?
```

---

# Objetivos da aula

Ao final da aula, o estudante deverá ser capaz de:

1. explicar o conceito de Bioinformática;
2. reconhecer seu caráter interdisciplinar;
3. identificar diferentes profissionais e conhecimentos envolvidos em projetos de Bioinformática;
4. reconhecer algumas tecnologias utilizadas na área;
5. compreender por que dados biológicos precisam ser armazenados e organizados;
6. relacionar bancos de dados tradicionais aos bancos de dados biológicos;
7. executar uma análise computacional elementar de uma sequência.

---

# Roteiro de 50 minutos

## 0-8 min | O que é Bioinformática?

Comece com uma pergunta simples:

> **O que acontece quando a quantidade de dados produzida pela Biologia se torna tão grande que uma pessoa não consegue mais analisá-la manualmente?**

A resposta leva naturalmente à Bioinformática.

### Definição para apresentar

> **Bioinformática é uma área interdisciplinar que utiliza métodos computacionais, algoritmos, bancos de dados, estatística e conhecimentos biológicos para armazenar, organizar, processar e analisar dados biológicos.**

Uma forma simples de colocar no quadro:

```text
BIOLOGIA
   +
COMPUTAÇÃO
   +
ESTATÍSTICA
   +
CIÊNCIA DE DADOS
   ↓
BIOINFORMÁTICA
```

Mas é importante explicar que a Bioinformática não pertence exclusivamente a nenhuma dessas áreas.

Ela existe justamente **na integração entre diferentes conhecimentos**.

### Exemplos de dados que podem ser analisados

- sequências de DNA;
- RNA;
- proteínas;
- expressão gênica;
- estruturas moleculares;
- dados de microbioma;
- variantes genéticas;
- grandes conjuntos de dados biomédicos.

---

## 8-16 min | Quem trabalha com Bioinformática?

Esse é um ponto importante para mostrar aos estudantes que Bioinformática normalmente é um **trabalho em equipe**.

Um único profissional dificilmente domina profundamente todas as áreas necessárias.

### Biólogo / Biomédico

Pode contribuir com conhecimentos sobre:

- células;
- DNA e RNA;
- genes;
- proteínas;
- organismos;
- funcionamento biológico;
- coleta e interpretação de amostras;
- significado biológico dos resultados.

### Profissional de Computação

Pode contribuir com:

- programação;
- algoritmos;
- estruturas de dados;
- banco de dados;
- processamento de grandes volumes de dados;
- desenvolvimento de software;
- automação;
- computação em nuvem;
- inteligência artificial.

### Estatístico / Cientista de Dados

Pode contribuir com:

- organização dos dados;
- análise estatística;
- visualização;
- identificação de padrões;
- construção e validação de modelos;
- tratamento de incerteza;
- interpretação quantitativa.

### Farmacêutico / Pesquisador da Saúde

Dependendo do projeto, pode contribuir com:

- estudos de medicamentos;
- interação entre moléculas;
- identificação de possíveis alvos terapêuticos;
- interpretação de resultados laboratoriais;
- desenho experimental.

### Engenheiro de Software / Analista de Sistemas

Pode participar do desenvolvimento de:

- plataformas de análise;
- sistemas laboratoriais;
- APIs;
- pipelines automatizadas;
- interfaces para pesquisadores;
- sistemas de armazenamento e processamento.

### Uma pergunta interessante para a turma

> **Quem é o bioinformata: o biólogo que programa ou o programador que conhece Biologia?**

A resposta adequada é:

> **Pode ser qualquer um dos dois — e muitos outros perfis. Bioinformática é essencialmente interdisciplinar.**

---

## 16-21 min | O mínimo de Biologia necessário para começar

Nesta primeira aula, trabalhe somente quatro conceitos.

### DNA

Pode ser representado computacionalmente como uma sequência formada por quatro símbolos principais:

```text
A  T  C  G
```

- A = adenina
- T = timina
- C = citosina
- G = guanina

Do ponto de vista computacional, uma sequência pode inicialmente ser representada como uma **string**:

```python
sequencia = "ATGCGTACGTTAGC"
```

### Gene

Uma região do DNA associada a uma informação funcional. Computacionalmente, pode ser representada por sua sequência e por diversos metadados.

### Genoma

Conjunto do material genético de um organismo.

### Proteoma

Conjunto de proteínas e variantes de proteínas presentes em determinada condição biológica.

### Ponte entre as áreas

```text
BIOLOGIA                    COMPUTAÇÃO
DNA                         sequência/string
Gene                        registro + sequência
Genoma                      grande conjunto de dados
Proteína                    sequência de aminoácidos
Comparar sequências         algoritmo
Organizar informações       banco de dados
Experimento computacional   análise in silico
```

---

## 21-28 min | Tecnologias utilizadas na Bioinformática

Agora, depois de entender a área e seus participantes, apresente as tecnologias.

Não é necessário aprofundar todas. O objetivo é mostrar o ecossistema.

### Linguagens de programação

**Python**

Muito utilizado para:

- manipulação de dados;
- automação;
- análise de sequências;
- inteligência artificial;
- construção de pipelines.

**R**

Muito utilizado em:

- estatística;
- análise de dados biológicos;
- expressão gênica;
- visualização científica.

### Linux

Grande parte das ferramentas de Bioinformática é executada em ambientes Linux, principalmente em servidores e clusters de processamento.

### Computação em nuvem

Projetos de Bioinformática podem gerar grandes volumes de dados. Por isso, processamento e armazenamento em nuvem são cada vez mais relevantes.

### Inteligência Artificial e Machine Learning

Podem ser utilizados para:

- classificação;
- reconhecimento de padrões;
- predição;
- análise de imagens biomédicas;
- estudo de proteínas;
- descoberta de fármacos.

### Ferramentas especializadas

Exemplos que aparecerão durante a disciplina:

- BLAST;
- Clustal;
- ferramentas de sequenciamento;
- ferramentas de análise estrutural;
- plataformas para análise de microbioma.

### Conceito importante: pipeline

Em Bioinformática é comum organizar várias etapas em sequência:

```text
DADO BRUTO
    ↓
CONTROLE DE QUALIDADE
    ↓
PRÉ-PROCESSAMENTO
    ↓
ANÁLISE
    ↓
COMPARAÇÃO
    ↓
VISUALIZAÇÃO
    ↓
INTERPRETAÇÃO
```

Explique aos estudantes que isso se parece muito com um fluxo de processamento de dados na Computação.

---

## 28-36 min | Entrando em Banco de Dados

Agora faça a transição para um conhecimento que os estudantes da Computação provavelmente já reconhecem.

Pergunte:

> **Se milhões de pesquisadores produzem sequências de DNA e proteínas, onde essas informações ficam armazenadas?**

A resposta é: **bancos de dados biológicos**.

### Primeiro: relembrando Banco de Dados

Um banco de dados é uma estrutura utilizada para **armazenar, organizar, relacionar e recuperar informações**.

Em um sistema comum poderíamos ter:

```text
ALUNO
-----------------------
id
nome
email
curso
```

Em Bioinformática poderíamos ter algo conceitualmente semelhante:

```text
GENE
-----------------------
id
gene
organismo
cromossomo
sequencia
funcao
```

Ou ainda:

```text
PROTEINA
-----------------------
id
nome
organismo
sequencia_aminoacidos
funcao
estrutura
```

### O dado biológico não é apenas uma sequência

Uma sequência precisa estar acompanhada de **metadados**.

Por exemplo:

```text
Sequência: ATGCGTAC...
Organismo: Homo sapiens
Gene: exemplo
Cromossomo: 1
Fonte: experimento X
Identificador: ABC123
Referência: artigo científico
```

É isso que transforma uma simples sequência de caracteres em um registro cientificamente utilizável.

---

## 36-41 min | Grandes bancos de dados biológicos

Apresente apenas três nesta primeira aula.

### NCBI / GenBank

**NCBI:** https://www.ncbi.nlm.nih.gov/  
**GenBank:** https://www.ncbi.nlm.nih.gov/genbank/

Use a analogia:

> **O GenBank funciona como uma enorme biblioteca digital de sequências de nucleotídeos e suas informações associadas.**

Uma consulta pode trazer informações como:

- organismo;
- gene;
- sequência;
- localização;
- identificadores;
- referências;
- anotações.

### UniProt

https://www.uniprot.org/

Voltado principalmente para **sequências e anotações de proteínas**.

### Protein Data Bank - PDB

https://www.rcsb.org/

Repositório de estruturas tridimensionais de biomoléculas, especialmente proteínas e ácidos nucleicos.

### Pergunta para consolidar

> **Qual é a diferença entre guardar apenas `ATGCGT...` em um arquivo de texto e possuir essa sequência em um banco de dados científico?**

Resposta esperada:

> O banco associa a sequência a identificadores, organismo, origem, função, referências e outras informações necessárias para interpretação e reutilização científica.

---

## 41-46 min | Banco de dados + algoritmo: onde entra o BLAST?

Agora fica mais fácil explicar o BLAST.

O banco contém milhares ou milhões de sequências conhecidas.

O pesquisador possui uma sequência de interesse.

O algoritmo compara essa sequência com o banco.

```text
SEQUÊNCIA DESCONHECIDA
        ↓
      BLAST
        ↓
BANCO DE SEQUÊNCIAS
        ↓
SEQUÊNCIAS SEMELHANTES
        ↓
POSSÍVEL INTERPRETAÇÃO
```

Explique como um **mecanismo de busca por similaridade de sequências**.

Analogia:

> O Google recebe palavras e procura documentos relacionados. O BLAST recebe uma sequência e procura sequências biologicamente semelhantes em bancos de dados.

O BLAST pode apoiar:

- identificação de sequências semelhantes;
- busca por homologia;
- identificação de organismos;
- anotação;
- localização de sequências.

---

## 46-50 min | Primeira experiência computacional

Abra o [Google Colab da Aula 01](https://colab.research.google.com/github/deniaulainfead23/bioinformatica/blob/main/aula01/aula01_colab.ipynb).

Não tente ensinar Python formalmente nesta aula.

Mostre apenas que o computador consegue receber uma sequência como dado:

```python
sequencia = "ATGCGTACGTTAGC"

print(sequencia)
print(len(sequencia))
```

Explique:

- `sequencia` é o nome da variável;
- `=` armazena o valor;
- as aspas indicam um texto/string;
- `print()` mostra uma informação;
- `len()` calcula o comprimento.

Depois conte uma base:

```python
print(sequencia.count("A"))
```

E finalize:

> **Hoje nós não aprendemos apenas uma linha de Python. Nós vimos que uma informação biológica pode ser representada, armazenada e processada computacionalmente. Esse é um dos fundamentos da Bioinformática.**

---

# Fechamento da aula

Coloque no quadro:

```text
BIOINFORMÁTICA

BIOLOGIA → explica o fenômeno
COMPUTAÇÃO → processa os dados
ESTATÍSTICA → ajuda a analisar os resultados
BANCO DE DADOS → organiza o conhecimento
TECNOLOGIA → permite trabalhar em escala
PESQUISADOR → formula perguntas
```

E finalize com três perguntas rápidas:

1. Por que a Bioinformática precisa de profissionais de diferentes áreas?
2. Qual é a diferença entre uma sequência e um registro de banco de dados biológico?
3. Qual é o papel da Computação dentro da Bioinformática?

---

# O que deixar para as próximas aulas

Nesta primeira aula **não aprofundar**:

- replicação, transcrição e tradução;
- tipos de BLAST;
- FASTQ e Phred;
- filogenia;
- RNA-Seq;
- docking;
- PCA e SVD;
- SQL em profundidade;
- modelagem relacional avançada.

A progressão sugerida é:

```text
AULA 01
O que é Bioinformática
        ↓
AULA 02
Dados biológicos e bancos científicos
        ↓
AULA 03
Comparação de sequências / BLAST
        ↓
AULA 04
Pré-processamento e qualidade
        ↓
AULAS SEGUINTES
Python, análise de dados e aplicações
```

---

# Material complementar

## Vídeo de introdução

**Introdução à Bioinformática - Parte 1**  
Discentes Bioinformática UFPR  
https://www.youtube.com/watch?v=9pkCA01EWy0

Utilize como apoio para a contextualização da área.

---

# Síntese para a professora

> **Bioinformática é uma área interdisciplinar na qual profissionais da Biologia, Saúde, Computação, Estatística e Ciência de Dados utilizam tecnologias computacionais para armazenar, organizar, processar e analisar dados biológicos. Os bancos de dados biológicos permitem preservar e compartilhar esse conhecimento, enquanto algoritmos e ferramentas computacionais permitem compará-lo e transformá-lo em informação útil para a pesquisa.**
