"""
Aula 01 - Introdução à Bioinformática
Prática didática com sequências sintéticas.

Objetivo:
- tratar DNA como dado computacional;
- calcular tamanho e frequência das bases;
- calcular conteúdo GC;
- comparar amostras simples.

Os dados são sintéticos e não devem ser usados para inferência biológica real.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


BASE = Path(__file__).resolve().parent
ARQUIVO = BASE / "dados" / "sequencias_demo.csv"


def conteudo_gc(sequencia: str) -> float:
    sequencia = sequencia.upper().strip()
    if not sequencia:
        return 0.0
    g = sequencia.count("G")
    c = sequencia.count("C")
    return 100 * (g + c) / len(sequencia)


def contar_bases(sequencia: str) -> dict:
    sequencia = sequencia.upper().strip()
    return {base: sequencia.count(base) for base in "ATCG"}


def main():
    df = pd.read_csv(ARQUIVO)

    df["tamanho"] = df["sequencia"].str.len()
    df["gc_percentual"] = df["sequencia"].apply(conteudo_gc)

    contagens = df["sequencia"].apply(contar_bases).apply(pd.Series)
    df = pd.concat([df, contagens], axis=1)

    print("\n=== DADOS ANALISADOS ===")
    print(df[["amostra", "tamanho", "A", "T", "C", "G", "gc_percentual"]].round(2))

    maior_gc = df.loc[df["gc_percentual"].idxmax()]
    menor_gc = df.loc[df["gc_percentual"].idxmin()]

    print("\n=== RESULTADOS ===")
    print(f"Maior conteúdo GC: {maior_gc['amostra']} ({maior_gc['gc_percentual']:.2f}%)")
    print(f"Menor conteúdo GC: {menor_gc['amostra']} ({menor_gc['gc_percentual']:.2f}%)")

    print("\nPergunta para a turma:")
    print("Como transformar uma sequência de letras em variáveis que um algoritmo possa analisar?")

    df.plot(x="amostra", y="gc_percentual", kind="bar", legend=False)
    plt.title("Conteúdo GC das sequências didáticas")
    plt.xlabel("Amostra")
    plt.ylabel("GC (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
