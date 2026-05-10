; ==========================================
; EcoCharge - Controle Inteligente de Potência
; Simulação de gerenciamento energético
; em eletropostos utilizando Assembly
; ==========================================

; R0 = limite máximo da rede elétrica
; R1 = consumo atual da rede
; R2 = endereço do sensor
; R3 = status do controle de carga

START:

MOV R0, #100        ; define limite da rede (100 kW)

LDR R1, [R2]        ; lê consumo atual do sensor

CMP R1, R0          ; compara consumo com limite

BGT REDUZ_CARGA     ; se consumo > limite, reduz carga

B CONTINUA          ; continua operação normal

REDUZ_CARGA:
MOV R3, #1          ; ativa modo de redução de potência

CONTINUA:
NOP                 ; mantém sistema em execução