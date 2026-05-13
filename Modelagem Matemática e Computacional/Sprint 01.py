# Challenge Sprint I - Modelagem Matemática e Computacional
# Grupo: Alexandre Rizzi Rm-569621, Julia Junqueira Konishi RM-569506,
# João Victor Scheren Rm-568883, João Vitor Neves Rm-571608, Miguel Putini-571624



import numpy as np
import matplotlib.pyplot as plt


# FUNÇÃO DA POTÊNCIA
# P(t) = 18 + (24t)/(t+2)


def P(t):
    return 18 + (24 * t) / (t + 2)


# DERIVADA DA FUNÇÃO
# P'(t) = 48 / (t+2)^2


def dP(t):
    return 48 / ((t + 2) ** 2)


# DOMÍNIO DO TEMPO


t = np.linspace(0, 20, 1000)


# LIMITES


# Limite quando t -> 0+
limite_t0 = P(0)

# Limite quando t -> infinito
limite_infinito = 42

print("=" * 60)
print("LIMITES")
print("=" * 60)

print(f"Limite de P(t) quando t -> 0+ = {limite_t0:.2f} kW")
print(f"Limite de P(t) quando t -> infinito = {limite_infinito:.2f} kW")

print("\nINTERPRETAÇÃO:")
print("- A potência inicial da recarga é 18 kW.")
print("- Ao longo do tempo, a potência aumenta e tende a 42 kW.")
print("- Isso representa a estabilização do sistema de recarga.")


# VARIAÇÃO MÉDIA ENTRE t=1 E t=3


p1 = P(1)
p3 = P(3)

variacao_media = (p3 - p1) / (3 - 1)

print("\n" + "=" * 60)
print("VARIAÇÃO MÉDIA")
print("=" * 60)

print(f"P(1) = {p1:.2f} kW")
print(f"P(3) = {p3:.2f} kW")
print(f"Variação média = {variacao_media:.2f} kW/min")

print("\nINTERPRETAÇÃO:")
print("- Entre 1 e 3 minutos, a potência aumenta")
print(f"  em média {variacao_media:.2f} kW por minuto.")
print("- Isso auxilia no gerenciamento da infraestrutura elétrica.")


# DERIVADA
print("\n" + "=" * 60)
print("DERIVADA DA FUNÇÃO")
print("=" * 60)

print("P'(t) = 48 / (t+2)^2")

print("\nINTERPRETAÇÃO:")
print("- A derivada representa a taxa instantânea")
print("  de variação da potência ao longo do tempo.")


# COMPARAÇÃO ENTRE P'(1) E P'(6)

dp1 = dP(1)
dp6 = dP(6)

print("\n" + "=" * 60)
print("COMPARAÇÃO DA DERIVADA")
print("=" * 60)

print(f"P'(1) = {dp1:.2f} kW/min")
print(f"P'(6) = {dp6:.2f} kW/min")

print("\nINTERPRETAÇÃO:")
print("- No início da recarga, a potência cresce rapidamente.")
print("- Depois, o crescimento desacelera.")
print("- O sistema tende à estabilização.")


# CRESCIMENTO E DECRESCIMENTO


print("\n" + "=" * 60)
print("ANÁLISE DE CRESCIMENTO")
print("=" * 60)

print("Como P'(t) > 0 para todo t >= 0:")
print("- A função é sempre crescente.")
print("- Não existem intervalos de decrescimento.")


# GRÁFICO DA FUNÇÃO P(t)


plt.figure(figsize=(10, 5))

plt.plot(t, P(t), linewidth=3, label='P(t)')

plt.title("Gráfico da Função P(t)")
plt.xlabel("Tempo (min)")
plt.ylabel("Potência (kW)")
plt.grid(True)

# Pontos
pontos_t = [0, 1, 3, 6, 8]
pontos_p = [P(x) for x in pontos_t]

plt.scatter(pontos_t, pontos_p, s=80)

for i in range(len(pontos_t)):
    plt.text(pontos_t[i],
             pontos_p[i] + 0.5,
                f"({pontos_t[i]}, {pontos_p[i]:.1f})")

plt.legend()

plt.show()


# GRÁFICO DA DERIVADA P'(t)


plt.figure(figsize=(10, 5))

plt.plot(t, dP(t), linewidth=3, label="P'(t)")

plt.title("Gráfico da Derivada P'(t)")
plt.xlabel("Tempo (min)")
plt.ylabel("Taxa de Variação da Potência")
plt.grid(True)

plt.legend()

plt.show()