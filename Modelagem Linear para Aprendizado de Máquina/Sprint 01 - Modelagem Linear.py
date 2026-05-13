# BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt

# LEITURA DA BASE DE DADOS

print("\nCarregando base de dados dos eletropostos...\n")

df = pd.read_excel("base_ev.csv.xlsx")

print("Base carregada com sucesso!\n")

# LIMPEZA DOS DADOS

# Transformando a coluna de consumo em valor numérico
df["Energy (kWh)"] = pd.to_numeric(
    df["Energy (kWh)"],
    errors="coerce"
)

# Removendo linhas com valores vazios
df = df.dropna(subset=["Energy (kWh)"])

# VISUALIZAÇÃO INICIAL

print("Primeiras linhas da base:\n")

print(df.head())

# CRIAÇÃO DE CATEGORIAS

# Separando consumo em níveis para facilitar a análise
def categoria_consumo(kwh):

    if kwh <= 10:
        return "Baixo"

    elif kwh <= 30:
        return "Médio"

    else:
        return "Alto"


df["Categoria Consumo"] = df["Energy (kWh)"].apply(
    categoria_consumo
)

# TABELA DE FREQUÊNCIA
# VARIÁVEL DISCRETA

print("\n===================================")
print("Frequência de utilização das portas")
print("===================================\n")

freq_portas = df["Port Number"].value_counts()

print(freq_portas)

print("\nInsight:")
print("Algumas portas são utilizadas com mais frequência que outras.")

print("\nInsight:")
print("Isso pode gerar concentração de consumo em determinados pontos.")

# TABELA DE FREQUÊNCIA
# VARIÁVEL CONTÍNUA

print("\n===================================")
print("Distribuição do consumo energético")
print("===================================\n")

classes = [0, 10, 20, 30, 40, 50, 100]

df["Faixa Consumo"] = pd.cut(
    df["Energy (kWh)"],
    bins=classes
)

freq_consumo = df["Faixa Consumo"].value_counts().sort_index()

print(freq_consumo)

print("\nInsight:")
print("Grande parte das sessões possui consumo médio de energia.")

print("\nInsight:")
print("Sessões com consumo elevado reforçam a necessidade")
print("de gerenciamento inteligente de potência.")

# GRÁFICO DE BARRAS

plt.figure(figsize=(8,5))

freq_portas.plot(kind="bar")

plt.title("Utilização das Portas de Carregamento")
plt.xlabel("Portas")
plt.ylabel("Quantidade de Utilizações")

plt.show()

# HISTOGRAMA

plt.figure(figsize=(8,5))

df["Energy (kWh)"].hist(bins=10)

plt.title("Distribuição do Consumo Energético")
plt.xlabel("Consumo (kWh)")
plt.ylabel("Frequência")

plt.show()

# BOXPLOT

plt.figure(figsize=(8,5))

plt.boxplot(df["Energy (kWh)"])

plt.title("Boxplot do Consumo Energético")
plt.ylabel("Consumo (kWh)")

plt.show()

# CONCLUSÃO

print("\n===================================")
print("Conclusão")
print("===================================\n")

print("Durante a análise dos dados, foi possível perceber")
print("que o consumo energético dos eletropostos não acontece")
print("de forma totalmente equilibrada.")

print("\nAlgumas sessões apresentam consumo muito maior")
print("do que outras, o que mostra como determinados")
print("momentos podem gerar picos de energia e aumentar")
print("a pressão sobre a rede elétrica.")

print("\nTambém observamos que algumas portas de carregamento")
print("são utilizadas com mais frequência, criando uma")
print("concentração de uso em pontos específicos.")
print("Isso pode causar desperdícios e reduzir a eficiência")
print("da infraestrutura elétrica disponível.")

print("\nEsses resultados ajudaram a justificar a criação")
print("do sistema desenvolvido anteriormente no projeto")
print("de Data Structures, o EcoCharge.")

print("\nA análise mostrou que existe a necessidade de")
print("um sistema capaz de monitorar o consumo energético")
print("dos carregadores em tempo real e controlar")
print("a distribuição de potência de forma inteligente.")

print("\nCom base nisso, o EcoCharge foi pensado para")
print("evitar sobrecargas na rede comercial, principalmente")
print("em locais onde vários veículos elétricos podem")
print("estar carregando ao mesmo tempo.")

print("\nO sistema funciona utilizando limites externos")
print("de potência, permitindo que os carregadores")
print("continuem operando sem ultrapassar a capacidade")
print("energética disponível no estabelecimento.")

print("\nAlém disso, o projeto também contribui para")
print("sustentabilidade, já que reduz desperdícios")
print("de energia, melhora o aproveitamento da")
print("infraestrutura elétrica e possibilita um uso")
print("mais eficiente de fontes renováveis.")

print("\nDessa forma, a análise de dados ajudou não apenas")
print("a entender o comportamento dos eletropostos,")
print("mas também a validar a importância de soluções")
print("inteligentes como o EcoCharge para o futuro")
print("da mobilidade elétrica.")