# BIBLIOTECAS

import pandas as pd
import matplotlib.pyplot as plt

# LEITURA DA BASE DE DADOS

print("\nCarregando base de dados dos eletropostos...\n")

df = pd.read_excel("base_ev.csv.xlsx")

print("Base carregada com sucesso!\n")

# LIMPEZA DOS DADOS

# Transformando coluna de consumo em numérica
df["Energy (kWh)"] = pd.to_numeric(
    df["Energy (kWh)"],
    errors="coerce"
)

# Removendo valores vazios
df = df.dropna(subset=["Energy (kWh)"])

print("Dados limpos com sucesso!\n")

# VISUALIZAÇÃO INICIAL

print("Primeiras linhas da base:\n")
print(df.head())

print("\nQuantidade de registros:")
print(df.shape[0])

# CATEGORIZAÇÃO DO CONSUMO

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

# TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIA
# VARIÁVEL QUANTITATIVA DISCRETA

print("\n" + "="*50)
print("TABELA DE FREQUÊNCIA - VARIÁVEL DISCRETA")
print("="*50)

# Frequência absoluta
freq_portas = (
    df["Port Number"]
    .value_counts()
    .sort_index()
)

# Montando tabela completa
tabela_portas = pd.DataFrame({
    "Frequência Absoluta":
    freq_portas,

    "Frequência Relativa (%)":
    round(
        (freq_portas / freq_portas.sum()) * 100,
        2
    )
})

# Frequência acumulada
tabela_portas["Frequência Acumulada"] = (
    tabela_portas[
        "Frequência Absoluta"
    ].cumsum()
)

# Frequência relativa acumulada
tabela_portas[
    "Frequência Relativa Acumulada (%)"
] = round(
    tabela_portas[
        "Frequência Relativa (%)"
    ].cumsum(),
    2
)

print("\nDistribuição de frequência das portas:")
print(tabela_portas)


# INSIGHTS

print("\n# Insight 1:")
print(
    "Algumas portas são utilizadas "
    "com maior frequência do que outras."
)

print("\n# Insight 2:")
print(
    "Existe concentração de utilização "
    "em determinadas portas, o que pode "
    "gerar sobrecarga em pontos específicos."
)

# TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIA
# VARIÁVEL QUANTITATIVA CONTÍNUA

print("\n" + "="*50)
print("TABELA DE FREQUÊNCIA - VARIÁVEL CONTÍNUA")
print("="*50)

# Criando classes
classes = [0, 10, 20, 30, 40, 50, 100]

df["Faixa Consumo"] = pd.cut(
    df["Energy (kWh)"],
    bins=classes
)

# Frequência absoluta
freq_consumo = (
    df["Faixa Consumo"]
    .value_counts()
    .sort_index()
)

# Tabela completa
tabela_consumo = pd.DataFrame({
    "Frequência Absoluta":
    freq_consumo,

    "Frequência Relativa (%)":
    round(
        (freq_consumo / freq_consumo.sum()) * 100,
        2
    )
})

# Frequência acumulada
tabela_consumo[
    "Frequência Acumulada"
] = tabela_consumo[
    "Frequência Absoluta"
].cumsum()

# Frequência relativa acumulada
tabela_consumo[
    "Frequência Relativa Acumulada (%)"
] = round(
    tabela_consumo[
        "Frequência Relativa (%)"
    ].cumsum(),
    2
)

print("\nDistribuição do consumo energético:")
print(tabela_consumo)


# INSIGHTS

print("\n# Insight 1:")
print(
    "Grande parte das sessões apresenta "
    "consumo médio de energia, indicando "
    "um padrão relativamente equilibrado "
    "de utilização."
)

print("\n# Insight 2:")
print(
    "Sessões com alto consumo mostram "
    "a necessidade de monitoramento "
    "inteligente da potência para evitar "
    "sobrecargas na rede elétrica."
)

# GRÁFICO DE BARRAS

plt.figure(figsize=(8, 5))

freq_portas.plot(kind="bar")

plt.title(
    "Utilização das Portas de Carregamento"
)

plt.xlabel("Portas")
plt.ylabel("Quantidade de Utilizações")

plt.show()

# HISTOGRAMA

plt.figure(figsize=(8, 5))

df["Energy (kWh)"].hist(
    bins=10
)

plt.title(
    "Distribuição do Consumo Energético"
)

plt.xlabel("Consumo (kWh)")
plt.ylabel("Frequência")

plt.show()

# BOXPLOT

plt.figure(figsize=(8, 5))

plt.boxplot(
    df["Energy (kWh)"]
)

plt.title(
    "Boxplot do Consumo Energético"
)

plt.ylabel(
    "Consumo (kWh)"
)

plt.show()

# CONCLUSÃO

print("\n" + "="*50)
print("CONCLUSÃO")
print("="*50)

print(
    "\nDurante a análise dos dados, "
    "foi possível perceber que o "
    "consumo energético dos eletropostos "
    "não acontece de forma totalmente "
    "equilibrada."
)

print(
    "\nAlgumas sessões apresentam "
    "consumo muito maior do que outras, "
    "o que mostra como determinados "
    "momentos podem gerar picos de energia."
)

print(
    "\nTambém observamos que algumas "
    "portas de carregamento são "
    "utilizadas com maior frequência, "
    "criando concentração de uso "
    "em pontos específicos."
)

print(
    "\nEsses resultados reforçam a "
    "necessidade de sistemas inteligentes "
    "de monitoramento energético, "
    "capazes de distribuir melhor "
    "a potência e evitar sobrecargas."
)

print(
    "\nAlém disso, os dados mostram "
    "como análises estatísticas podem "
    "contribuir para melhorar a "
    "eficiência energética e apoiar "
    "decisões ligadas à mobilidade "
    "elétrica e sustentabilidade."
)