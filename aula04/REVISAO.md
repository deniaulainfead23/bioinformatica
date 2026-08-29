# Revisão - Aula 04

## Bioinformática: conceitos essenciais

### 1. O que é Bioinformática?

É uma área interdisciplinar que utiliza métodos computacionais, algoritmos, bancos de dados e análise quantitativa para organizar e analisar dados biológicos.

### 2. Quais áreas se encontram nela?

- Biologia e Biomedicina: significado biológico dos dados.
- Computação: algoritmos, software, bancos e processamento.
- Estatística e Ciência de Dados: análise, comparação e validação.
- Farmácia e Saúde: aplicação dos resultados em problemas de saúde e fármacos.
- Engenharia de Software: construção de pipelines e sistemas reprodutíveis.

### 3. Tecnologias importantes

Python, R, Linux, SQL, computação em nuvem, ferramentas de análise de sequências e, em alguns projetos, IA/Machine Learning.

### 4. Por que banco de dados é tão importante?

Porque os dados biológicos são produzidos em grande volume e precisam ser armazenados, identificados, consultados e relacionados com metadados.

### 5. Três bancos que precisam ser lembrados

| Recurso | Ideia principal |
|---|---|
| NCBI / GenBank | Sequências de nucleotídeos e anotações |
| UniProt | Sequências e informações de proteínas |
| PDB | Estruturas tridimensionais de biomoléculas |

### 6. BLAST

O BLAST compara uma sequência de interesse com sequências de bancos de referência para encontrar similaridades.

### 7. Pré-processamento

Antes da análise, é necessário verificar qualidade, inconsistências, ruído, redundância e formato dos dados.

### 8. Python na aula

A sequência de DNA foi representada como string, permitindo:

- calcular tamanho com `len()`;
- contar bases com `.count()`;
- calcular conteúdo GC;
- organizar várias sequências em uma tabela com pandas;
- criar gráficos para comparação.

## Para lembrar em uma frase

> **Bioinformática transforma dados biológicos em informação analisável por meio da integração entre Biologia, Computação e métodos quantitativos.**