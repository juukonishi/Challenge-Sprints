; EcoCharge - Controle Inteligente de Potência
; Gerenciamento energético para eletropostos

; R0 = limite máximo da rede (kW)
; R1 = consumo atual
; R2 = endereço do sensor
; R3 = status do carregador
; R4 = potência liberada

START:

MOV R0, #100        ; limite máximo da rede

LDR R1, [R2]        ; leitura do sensor

CMP R1, R0          ; consumo passou do limite?

BGT REDUZ_CARGA     ; se sim, reduz potência

; operação normal
MOV R3, #0          ; carregamento normal
MOV R4, #22         ; libera até 22 kW

B CONTINUA

REDUZ_CARGA:

MOV R3, #1          ; ativa controle de potência
MOV R4, #7          ; reduz carregamento

CONTINUA:

NOP                 ; sistema permanece monitorando