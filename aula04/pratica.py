"""
Aula 04 - Introdução à Bioinformática
Prática didática com sequências sintéticas.

O código foi escrito de forma detalhada para estudantes que ainda não conhecem Python.
Os dados são sintéticos e não devem ser usados para inferência biológica real.
"""

# Path ajuda a localizar arquivos dentro da pasta do projeto.
from pathlib import Path

# pandas trabalha com tabelas e arquivos CSV.
import pandas as pd

# matplotlib cria gráficos.
import matplotlib.pyplot as plt

# Descobre a pasta em que este arquivo pratica.py está salvo.
BASE = Path(__file__).resolve().parent

# Monta o caminho para o arquivo de dados.
ARQUIVO = BASE / "dados" / "sequencias_demo.csv"


def conteudo_gc(sequencia: str) -> float:
    """Calcula o percentual de G + C de uma sequência."""

    # upper() transforma letras minúsculas em maiúsculas.
    # strip() remove espaços extras no início ou no fim.
    sequencia = sequencia.upper().strip()

    # Se a sequência estiver vazia, retornamos zero para evitar divisão por zero.
    if not sequencia:
        return 0.0

    # count() conta quantas vezes cada letra aparece.
    quantidade_g = sequencia.count("G")
    quantidade_c = sequencia.count("C")

    # len() informa o número total de caracteres.
    return 100 * (quantidade_g + quantidade_c) / len(sequencia)


def contar_bases(sequencia: str) -> dict:
    """Conta A, T, C e G e devolve os valores em um dicionário."""

    sequencia = sequencia.upper().strip()

    return {
        "A": sequencia.count("A"),
        "T": sequencia.count("T"),
        "C": sequencia.count("C"),
        "G": sequencia.count("G"),
    }


def main():
    # read_csv() lê o arquivo CSV e cria uma tabela chamada DataFrame.
    df = pd.read_csv(ARQUIVO)

    # Cria uma nova coluna com o tamanho de cada sequência.
    df["tamanho"] = df["sequencia"].str.len()

    # apply() executa a função conteudo_gc em cada sequência da coluna.
    df["gc_percentual"] = df["sequencia"].apply(conteudo_gc)

    # Conta A, T, C e G de cada sequência e transforma os resultados em colunas.
    contagens = df["sequencia"].apply(contar_bases).apply(pd.Series)

    # concat() junta a tabela original com as novas colunas de contagem.
    df = pd.concat([df, contagens], axis=1)

    print("\n=== DADOS ANALISADOS ===")
    print(df[["amostra", "tamanho", "A", "T", "C", "G", "gc_percentual"]].round(2))

    # idxmax() localiza a linha do maior valor de GC.
    maior_gc = df.loc[df["gc_percentual"].idxmax()]

    # idxmin() localiza a linha do menor valor de GC.
    menor_gc = df.loc[df["gc_percentual"].idxmin()]

    print("\n=== RESULTADOS ===")
    print(f"Maior conteúdo GC: {maior_gc['amostra']} ({maior_gc['gc_percentual']:.2f}%)")
    print(f"Menor conteúdo GC: {menor_gc['amostra']} ({menor_gc['gc_percentual']:.2f}%)")

    # Cria um gráfico de barras usando a tabela.
    df.plot(x="amostra", y="gc_percentual", kind="bar", legend=False)

    # Personaliza os textos do gráfico.
    plt.title("Conteúdo GC das sequências didáticas")
    plt.xlabel("Amostra")
    plt.ylabel("GC (%)")
    plt.xticks(rotation=45)

    # Ajusta espaços para evitar cortes nos textos.
    plt.tight_layout()

    # Exibe o gráfico.
    plt.show()


# Esta condição executa main() quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    main()
