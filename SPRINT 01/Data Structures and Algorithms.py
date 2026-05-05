#SISTEMA DE RECARGA INTELIGENTE
#Possui: Plano + Credito; Reserva de vaga; No-show; Check-in por localização; Controle de energia (Limitador de kW); Relatório final

import random

print('=== SISTEMA DE RECARGA INTELIGENTE ===')

#PLANO

print('\nPlanos disponíveis:')
print('1 - Básico (7 kW - R$ 50)')
print('2 - Intermediário (11 kW - R$ 100)')
print('3 - Premium (22 kW - R$ 200)')

plano = int(input('Escolha seu plano (1/2/3): '))

while plano not in [1, 2, 3]:
    print('Opção inválida!')
    plano = int(input('Escolha seu plano (1/2/3): '))

if plano == 1:
    credito = 50
    potencia_max = 7
    nome_plano = 'Básico'
elif plano == 2:
    credito = 100
    potencia_max = 11
    nome_plano = 'Intermediário'
else:
    credito = 200
    potencia_max = 22
    nome_plano = 'Premium'

print(f'\nCrédito disponível: R$ {credito}')
print(f'Potência máxima: {potencia_max} kW')
print(f'Plano: {nome_plano}')

#REGIÃO

print('\nRegiões:')
print('1 - Sul')
print('2 - Leste')
print('3 - Oeste')
print('4 - Norte')

regiao = int(input('Escolha a região (1-4): '))

while regiao not in [1, 2, 3, 4]:
    regiao = int(input('Inválido. Escolha (1-4): '))

regioes = {1: 'Sul', 2: 'Leste', 3: 'Oeste', 4: 'Norte'}
nome_regiao = regioes[regiao]

#LOCAL

print(f'\nLocais disponíveis em {nome_regiao}:')
print('1 - Mercado A')
print('2 - Mercado B')
print('3 - Mercado C')

local = int(input('Escolha o local (1-3): '))

while local not in [1, 2, 3]:
    local = int(input('Inválido (1-3): '))

locais = {1: 'Mercado A', 2: 'Mercado B', 3: 'Mercado C'}
nome_local = locais[local]

print(f'\nLocal escolhido: {nome_local} - {nome_regiao}')

#MATRIZ DE VAGAS

vagas = [
    ["L", "R", "L"],
    ["O", "L", "R"]
]

def mostrar_vagas():
    print("\nMapa de vagas:")
    for i in range(2):
        for j in range(3):
            print(f"{chr(65+i)}{j+1}:{vagas[i][j]}", end="  ")
        print()

print("\nLegenda: L = Livre | R = Reservada | O = Ocupada")
mostrar_vagas()

#ESCOLHA DE VAGA

while True:
    linha = input('\nEscolha a fileira (A/B): ').upper()

    while linha not in ["A", "B"]:
        linha = input('Inválido. A ou B: ').upper()

    i = ord(linha) - 65

    coluna = int(input('Escolha a vaga (1-3): ')) - 1

    if coluna < 0 or coluna > 2:
        print('Vaga inexistente!')
        continue

    if vagas[i][coluna] != "L":
        print('Vaga não disponível!')
        continue

    print('Vaga selecionada com sucesso!')
    break

#RESERVA

reserva = input('\nDeseja confirmar reserva? (s/n): ').lower()

while reserva not in ["s", "n"]:
    reserva = input('Digite apenas s ou n: ').lower()

tempo_reserva = 0
valor_reserva = 0

if reserva == "s":
    tempo_reserva = int(input('Tempo de reserva (min): '))
    valor_reserva = tempo_reserva * 0.5

    print(f'Valor da reserva: R$ {valor_reserva:.2f}')

    if credito >= valor_reserva:
        credito -= valor_reserva
        vagas[i][coluna] = "R"
        print(f'Reserva confirmada! Crédito atual: R$ {credito:.2f}')
    else:
        print('Crédito insuficiente!')
        tempo_reserva = 0

# CHECK-IN (GPS SIMULADO)

print('\nVerificando localização...')

local_posto = 10
local_usuario = random.randint(0, 20)

distancia = abs(local_usuario - local_posto)

print(f'Local do posto: {local_posto}')
print(f'Local usuário: {local_usuario}')
print(f'Distância: {distancia}')

presente = distancia <= 2

if presente:
    print('Check-in confirmado!')
else:
    print('Usuário não compareceu!')

#NO-SHOW

if reserva == "s" and not presente:
    multa = valor_reserva / 2
    credito -= multa

    print('\nNO-SHOW (RESERVA NÃO UTILIZADA)')
    print(f'Multa: R$ {multa:.2f}')
    print(f'Crédito atual: R$ {credito:.2f}')

elif reserva == "s" and presente:
    print('\nReserva utilizada com sucesso')

#RECARGA

elif presente:

    print('\nINICIANDO RECARGA')

    tempo = int(input('Tempo de recarga (min): '))

    energia = 0
    potencia_carro = 10

    for _ in range(tempo):
        potencia_real = min(potencia_carro, potencia_max)
        energia += potencia_real / 60

    preco_kwh = 1.8
    valor = energia * preco_kwh
    credito -= valor

    print("\n========== RELATÓRIO FINAL ==========")
    print(f"Plano: {nome_plano}")
    print(f"Região: {nome_regiao}")
    print(f"Local: {nome_local}")
    print(f"Energia consumida: {round(energia, 2)} kWh")
    print(f"Valor recarga: R$ {round(valor, 2)}")
    print(f"Crédito restante: R$ {round(credito, 2)}")
    print("=====================================")

    if credito < 0:
        print("⚠️ Saldo negativo")
    else:
        print("✅ Sessão concluída")
