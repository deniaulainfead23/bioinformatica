# Identidade do repositório

## BioCode | Bioinformática

**Conceito:** o encontro entre **código e vida**.

**Slogan:** `Onde o código encontra a vida.`

A personalidade do repositório combina duas linguagens visuais:

- **Computação:** terminal, código, dados, algoritmos, Python, bancos de dados e estruturas lógicas.
- **Biologia:** DNA, células, proteínas, diversidade, saúde e sistemas vivos.

A proposta é apresentar Bioinformática sem transformar o material em um curso de Biologia Molecular. O estudante deve enxergar primeiro o **dado**, depois o **algoritmo** e, por fim, a **interpretação biológica**.

---

## Assinatura conceitual

```text
      BIOLOGIA                         COMPUTAÇÃO
          🧬                                 </>
           \                                 /
            \                               /
             └────── BIOINFORMÁTICA ──────┘
                       dados
                         ↓
                    algoritmos
                         ↓
                    conhecimento
```

---

## Paleta sugerida

| Cor | Hex | Uso |
|---|---|---|
| Azul profundo | `#071A2B` | fundo, terminal, computação |
| Ciano tecnológico | `#00B8D9` | links, código, destaques tecnológicos |
| Verde biológico | `#34D399` | DNA, vida, resultados positivos |
| Verde-lima | `#A3E635` | pequenos destaques e indicadores |
| Branco gelo | `#F5FAFC` | textos e áreas claras |

A combinação **azul + ciano + verde** deve aparecer de forma consistente. O azul representa computação; o verde, vida; o ciano funciona como ponte visual entre os dois domínios.

---

## Elementos visuais

Símbolos preferenciais:

`🧬 DNA`  `</> código`  `⌘ algoritmo`  `▦ dados`  `◉ análise`  `⌁ sequência`

Evitar excesso de elementos médicos genéricos. A identidade deve remeter prioritariamente a **dados biológicos e computação científica**.

---

## Personalidade textual

O material deve ser:

- científico e tecnicamente correto;
- didático;
- progressivo;
- visual;
- orientado à prática;
- acessível a estudantes sem conhecimento prévio de Python;
- cuidadoso ao distinguir dado sintético, dado real e interpretação científica.

### Frase-guia

> **Dado biológico → representação computacional → processamento → análise → interpretação.**

---

## Padrão das aulas

Cada aula deve, sempre que possível, possuir:

```text
aulaXX/
├── README.md               # roteiro da aula
├── aulaXX_colab.ipynb      # prática guiada
├── atividade.md            # exercício dos estudantes
├── gabarito.md             # respostas + explicações
└── dados/                  # arquivos usados na prática
```

### Regra para exercícios

Toda atividade deve possuir um arquivo separado de **gabarito**, contendo:

1. resposta correta;
2. explicação do raciocínio;
3. quando pertinente, interpretação científica;
4. alerta quando o resultado não permitir conclusão biológica.

### Regra para Google Colab

Os notebooks são escritos para quem **ainda não sabe Python**. Portanto:

- cada importação deve ser explicada;
- variáveis devem ter nomes legíveis;
- cada comando novo deve receber comentário;
- funções como `print()`, `len()`, `.count()`, `DataFrame`, `.apply()` e gráficos devem ser explicadas antes do uso;
- evitar código compacto quando uma versão mais longa favorecer a compreensão;
- utilizar células Markdown para explicar o que será executado e o que o estudante deve observar.

---

## Mensagem da identidade

A Bioinformática não substitui a Biologia pela Computação. Ela cria uma ponte entre as duas áreas: **a vida produz dados; a Computação ajuda a organizá-los, compará-los e analisá-los; a interpretação devolve significado ao dado.**
