import pandas as pd
import matplotlib.pyplot as plt


# LEITURA DA BASE DE DADOS

df = pd.read_excel("base_ev.xlsx")


# LIMPEZA DOS DADOS

df["Energy (kWh)"] = pd.to_numeric(
    df["Energy (kWh)"],
    errors="coerce"
)

df["Port Number"] = pd.to_numeric(
    df["Port Number"],
    errors="coerce"
)

df = df.dropna(
    subset=["Energy (kWh)", "Port Number"]
)


# VISUALIZAÇÃO INICIAL DA BASE

print("Primeiras linhas da base:\n")
print(df.head())

print("\nQuantidade de registros:")
print(df.shape[0])


# CRIAÇÃO DA VARIÁVEL DE CATEGORIA DE CONSUMO

def categoria_consumo(kwh):

    if kwh <= 10:
        return "Baixo"

    elif kwh <= 30:
        return "Médio"

    else:
        return "Alto"


df["Categoria Consumo"] = df[
    "Energy (kWh)"
].apply(categoria_consumo)


# ITEM 01A - GRÁFICO DE SETORES

consumo_categoria = df[
    "Categoria Consumo"
].value_counts()

plt.figure(figsize=(8, 6))

plt.pie(
    consumo_categoria,
    labels=consumo_categoria.index,
    autopct="%1.1f%%",
    colors=[
        "lightgreen",
        "gold",
        "salmon"
    ]
)

plt.title(
    "Distribuição do Consumo Energético"
)

plt.legend(
    title="Categorias"
)

plt.show()


# ITEM 01B - GRÁFICO DE BARRAS

freq_portas = (
    df["Port Number"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

plt.bar(
    freq_portas.index.astype(str),
    freq_portas.values,
    color="skyblue",
    label="Quantidade de Utilizações"
)

plt.title(
    "Frequência de Utilização das Portas"
)

plt.xlabel(
    "Número da Porta"
)

plt.ylabel(
    "Quantidade de Utilizações"
)

plt.legend()

plt.show()


# ITEM 01C - HISTOGRAMA

plt.figure(figsize=(8, 5))

plt.hist(
    df["Energy (kWh)"],
    bins=10,
    color="lightcoral"
)

plt.title(
    "Distribuição do Consumo Energético"
)

plt.xlabel(
    "Consumo (kWh)"
)

plt.ylabel(
    "Frequência"
)

plt.show()


# ITEM 01D - BOXPLOT

plt.figure(figsize=(8, 5))

plt.boxplot(
    df["Energy (kWh)"],
    patch_artist=True,
    boxprops=dict(
        facecolor="lightblue"
    )
)

plt.title(
    "Boxplot do Consumo Energético"
)

plt.xlabel(
    "Sessões de Carregamento"
)

plt.ylabel(
    "Consumo (kWh)"
)

plt.show()


# ITEM 02 - ANÁLISE UNIVARIADA 1

# ITEM 02A - MEDIDAS DE TENDÊNCIA CENTRAL

print("\nANÁLISE UNIVARIADA 1")
print("ENERGY (kWh)")

energia = df["Energy (kWh)"]

print("\nMEDIDAS DE TENDÊNCIA CENTRAL")

print(
    "Média:",
    round(
        energia.mean(),
        2
    )
)

print(
    "Mediana:",
    round(
        energia.median(),
        2
    )
)

print(
    "Moda:",
    energia.mode()[0]
)


# ITEM 02B - MEDIDAS DE DISPERSÃO

print("\nMEDIDAS DE DISPERSÃO")

print(
    "Amplitude:",
    round(
        energia.max()
        - energia.min(),
        2
    )
)

print(
    "Variância:",
    round(
        energia.var(),
        2
    )
)

print(
    "Desvio Padrão:",
    round(
        energia.std(),
        2
    )
)


# ITEM 02C - MEDIDAS SEPARATRIZES

print("\nMEDIDAS SEPARATRIZES")

print(
    "1º Quartil (25%):",
    round(
        energia.quantile(0.25),
        2
    )
)

print(
    "2º Quartil (50%):",
    round(
        energia.quantile(0.50),
        2
    )
)

print(
    "3º Quartil (75%):",
    round(
        energia.quantile(0.75),
        2
    )
)

print(
    "Percentil 90:",
    round(
        energia.quantile(0.90),
        2
    )
)


# ITEM 02 - ANÁLISE UNIVARIADA 2

# ITEM 02A - MEDIDAS DE TENDÊNCIA CENTRAL

print("\nANÁLISE UNIVARIADA 2")
print("PORT NUMBER")

porta = df["Port Number"]

print("\nMEDIDAS DE TENDÊNCIA CENTRAL")

print(
    "Média:",
    round(
        porta.mean(),
        2
    )
)

print(
    "Mediana:",
    round(
        porta.median(),
        2
    )
)

print(
    "Moda:",
    porta.mode()[0]
)


# ITEM 02B - MEDIDAS DE DISPERSÃO

print("\nMEDIDAS DE DISPERSÃO")

print(
    "Amplitude:",
    round(
        porta.max()
        - porta.min(),
        2
    )
)

print(
    "Variância:",
    round(
        porta.var(),
        2
    )
)

print(
    "Desvio Padrão:",
    round(
        porta.std(),
        2
    )
)


# ITEM 02C - MEDIDAS SEPARATRIZES

print("\nMEDIDAS SEPARATRIZES")

print(
    "1º Quartil (25%):",
    round(
        porta.quantile(0.25),
        2
    )
)

print(
    "2º Quartil (50%):",
    round(
        porta.quantile(0.50),
        2
    )
)

print(
    "3º Quartil (75%):",
    round(
        porta.quantile(0.75),
        2
    )
)

print(
    "Percentil 90:",
    round(
        porta.quantile(0.90),
        2
    )
)