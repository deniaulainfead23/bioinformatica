"""Python 0 — introdução à análise de dados em Bioinformática.

Base inteiramente sintética e destinada apenas ao ensino.
Execute este arquivo na mesma pasta de base_python0_bioinformatica.csv.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# 1. Variáveis, leitura e impressão
titulo = "Python 0 — Análise de dados"
numero_esperado_amostras = 24
print(titulo)
print("Número esperado de amostras:", numero_esperado_amostras)

# 2. Lista e dicionário
bases_dna = ["A", "T", "G", "C"]
exemplo_amostra = {
    "id": "A01",
    "grupo": "Controle",
    "sequencia": "ATGCGTACGTAA",
}
print("Bases do DNA:", bases_dna)
print("Exemplo de amostra:", exemplo_amostra)

# 3. Leitura do arquivo CSV
caminho_csv = Path(__file__).with_name("base_python0_bioinformatica.csv")
tabela = pd.read_csv(caminho_csv)

print("\nPrimeiras linhas:")
print(tabela.head())
print("\nDimensão da base (linhas, colunas):", tabela.shape)
print("\nValores ausentes por coluna:")
print(tabela.isna().sum())

# 4. Criação de novas colunas
tabela["sequencia"] = tabela["sequencia"].str.upper()
tabela["tamanho"] = tabela["sequencia"].str.len()
tabela["quantidade_gc"] = (
    tabela["sequencia"].str.count("G") + tabela["sequencia"].str.count("C")
)
tabela["gc_percentual"] = 100 * tabela["quantidade_gc"] / tabela["tamanho"]

colunas_exibidas = [
    "id_amostra",
    "grupo",
    "sequencia",
    "tamanho",
    "gc_percentual",
]
print("\nTabela enriquecida:")
print(tabela[colunas_exibidas].head(10))

# 5. Resumo por grupo
resumo = (
    tabela.groupby("grupo", as_index=False)
    .agg(
        numero_amostras=("id_amostra", "count"),
        tamanho_medio=("tamanho", "mean"),
        gc_medio=("gc_percentual", "mean"),
        resposta_media=("resposta_percentual", "mean"),
    )
    .round(2)
)
print("\nResumo por grupo:")
print(resumo)

# 6. Filtro simples
resposta_alta = tabela[tabela["resposta_percentual"] >= 40]
print("\nAmostras com resposta igual ou superior a 40%:")
print(resposta_alta[["id_amostra", "grupo", "resposta_percentual"]])

# 7. Gráfico de barras
resumo.plot(
    x="grupo",
    y="resposta_media",
    kind="bar",
    color=["#2563EB", "#10B981", "#F97316"],
    legend=False,
)
plt.title("Resposta média por grupo")
plt.xlabel("Grupo")
plt.ylabel("Resposta média (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 8. Gráfico de linhas
serie_temporal = tabela.pivot_table(
    index="dia_coleta",
    columns="grupo",
    values="resposta_percentual",
    aggfunc="mean",
)
serie_temporal.plot(marker="o")
plt.title("Resposta ao longo dos dias")
plt.xlabel("Dia de coleta")
plt.ylabel("Resposta média (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 9. Gráfico de dispersão
tabela.plot(
    x="tamanho",
    y="gc_percentual",
    kind="scatter",
    color="#0F766E",
)
plt.title("Tamanho da sequência e conteúdo GC")
plt.xlabel("Tamanho da sequência (bases)")
plt.ylabel("Conteúdo GC (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nAnálise concluída.")
print("Lembrete: os dados são sintéticos e não sustentam inferências biológicas reais.")
