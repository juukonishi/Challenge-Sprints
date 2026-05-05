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

#RFID ou APP
print('\nAproxime o dispositivo...')

rfids_validos = ["1234", "ABCD", "USER01"]

print('\nEscolha como iniciar a sua sessão:')
print('1 - Cartão RFID')
print('2 - App (conexão do celular no aparelho')

modo = input('Opção: ')

presente = False

if modo == "1":
    codigo = input('Aproxime o seu cartão RFID: ')

    if codigo in rfids_validos:
        presente =  True
        print('RFID validado')
    else:
        print('RFID Inválido!')

elif modo == "2":
    conectado = input('Cabo conectado ao veículo? (s/n): ').lower()

    if conectado == 's':
        presente = True
        print('App detectou conexão - sessão iniciada')
    else:
        print('Veículo não conectado!')

else:
    print('Opção Inválida!')


#NO-SHOW
if not presente:
    print('\n' + '=' * 30)
    print('ALERTA: USUÁRIO NÃO COMPARECEU')
    print(f'A reserva de R$ {valor_reserva:.2f} não será estornada.')
    print(f'Crédito atual em conta: R$ {credito:.2f}')
    print('=' * 30)
else:
    print('\n' + '-' * 30)
    print('CHECK-IN REALIZADO: Iniciando recarga')
    print('-' * 30)

    #SIMULAÇÃO COM OS DADOS DO CARREGADOR

    tensao = 380
    corrente = 32
    fator_trifasico = 1.73

    potencia_carregador = (tensao * corrente * fator_trifasico) / 1000

    #LIMITE DO CARRO
    potencia_carro = 22

    #LIMITADOR DE REDE
    potencia_total_rede = 100 #kW total do estabelecimento
    consumo_atual = 80 #kW ja em uso

    potencia_rede_disponivel = potencia_total_rede - consumo_atual

    #LIMITADOR FINAL
    potencia_real = min(
        potencia_carregador,
        potencia_carro,
        potencia_rede_disponivel
    )

    print(f'\nPotência disponível em rede: {potencia_rede_disponivel} kW')
    print(f'Potência do carregador: {round(potencia_carregador, 2)} kW')
    print(f'Limite do carro: {potencia_carro} kW')
    print(f'Potência final utilizada: {round(potencia_real, 2)} kW')

    #SIMULAÇÃO
    if presente:
        print('\nIniciando recarga')

        tempo = tempo_reserva
        energia = 0

        print("\nAPP - MONITORAMENTO")

        for minuto in range(tempo):

            energia += potencia_real / 60
            progresso = ((minuto + 1) / tempo) * 100

            print(f'\nMinuto {minuto+1}')
            print(f'Potência : {round(potencia_real, 2)} kW')
            print(f'Energia: {round(energia, 2)} kW')
            print(f'Progresso: {round(progresso, 1)} %')

        preco = 1.8
        valor = energia * preco

        print("\n========== RELATÓRIO FINAL ==========")
        print(f"Plano: {nome_plano}")
        print(f"Local: {nome_local} - {nome_regiao}")
        print(f"Energia: {round(energia, 2)} kWh")
        print(f"Custo estimado: R$ {round(valor, 2)}")
        print(f"Crédito restante: R$ {round(credito, 2)}")
        print("=====================================")