# EcoCharge - Sistema Inteligente de Gerenciamento Energético para Eletropostos

## Integrantes

Júlia Konishi - 569506
Alexandre Rizzi - 569621
Miguel Putini - 571624
João Vitor Giadans - 571608
João Victor Scheren - 568883

---

# Sobre o Projeto

O **EcoCharge** foi desenvolvido pensando em um problema que pode se tornar cada vez mais comum com o crescimento dos veículos elétricos: o aumento da demanda energética nos eletropostos.

Hoje, muitos carregadores já possuem um limite próprio de potência. Porém, quando vários veículos estão carregando ao mesmo tempo, principalmente em estabelecimentos comerciais, a rede elétrica do local pode sofrer sobrecarga.

Pensando nisso, o EcoCharge surge como uma proposta de gerenciamento inteligente de energia, utilizando conceitos de **arquitetura de computadores** e **programação em baixo nível (Assembly)** para monitorar o consumo energético e redistribuir potência entre carregadores de forma mais eficiente.

O projeto se relaciona principalmente com:

- Controle de carga utilizando menos processamento computacional  
- Monitoramento energético com instruções mais eficientes

---

# Problema

Com o crescimento da mobilidade elétrica, o número de eletropostos também vem aumentando. Apesar disso, muitos locais ainda possuem limitações na infraestrutura elétrica disponível.

Mesmo que um carregador tenha um limite próprio de potência, vários carregadores funcionando ao mesmo tempo podem ultrapassar a capacidade da rede elétrica do estabelecimento.

Isso pode gerar alguns problemas, como:

- aumento do consumo energético  
- sobrecarga da rede elétrica  
- desperdício de energia  
- necessidade de infraestrutura mais robusta  
- maior uso de processamento computacional

Além disso, muitos sistemas utilizam softwares de alto nível e hardwares mais genéricos, que acabam exigindo mais processamento do que realmente seria necessário para tarefas simples de monitoramento e controle.

---

# Justificativa

A ideia do projeto surgiu a partir da necessidade de encontrar uma forma mais eficiente de gerenciar energia em eletropostos.

Durante nossas análises, percebemos que o consumo energético nem sempre acontece de maneira equilibrada. Em determinados momentos, alguns carregadores podem demandar muito mais energia do que outros, criando picos de consumo.

A partir disso, entendemos que seria interessante criar um sistema capaz de acompanhar esse comportamento e agir automaticamente quando o consumo ultrapassasse determinados limites.

Por isso, escolhemos trabalhar com **Assembly**, já que essa linguagem permite um controle mais próximo do hardware, utilizando menos instruções e reduzindo ciclos de processamento da CPU. Isso torna o sistema mais leve e mais adequado para dispositivos embarcados de baixo consumo energético.

---

# Proposta de Solução

O **EcoCharge** propõe um sistema inteligente de monitoramento e controle energético para eletropostos.

O funcionamento acontece de forma simples: o sistema monitora constantemente o consumo total da rede elétrica e compara esse valor com um limite máximo definido.

Quando o consumo permanece dentro do esperado, os carregadores funcionam normalmente.

Mas, caso o sistema identifique risco de sobrecarga, ele reduz automaticamente a potência distribuída aos carregadores ativos, ajudando a manter a estabilidade da rede elétrica.

### Fluxo do Sistema

```text
Monitorar consumo da rede
            ↓
Comparar com o limite máximo permitido
            ↓
Verificar carregadores ativos
            ↓
Redistribuir potência automaticamente
            ↓
Evitar sobrecarga elétrica
```

Com isso, o objetivo do EcoCharge é evitar desperdícios, reduzir riscos de instabilidade energética e melhorar o aproveitamento da infraestrutura já existente.

---

# Arquitetura Utilizada

Para o desenvolvimento da proposta, utilizamos conceitos da arquitetura **RISC (Reduced Instruction Set Computer)**.

Escolhemos essa arquitetura porque ela trabalha com um conjunto menor de instruções, tornando a execução mais rápida e energeticamente mais eficiente.

Esse tipo de arquitetura é muito utilizado em sistemas embarcados e microcontroladores, justamente por consumir menos energia e exigir menos recursos computacionais.

Também utilizamos conceitos importantes estudados na disciplina, como:

- pipeline de instruções  
- ciclos de clock  
- otimização de processamento  
- eficiência computacional

A ideia foi demonstrar como escolhas arquiteturais podem impactar diretamente no desempenho e no consumo energético de um sistema.

---

# Trecho do Código Assembly

```assembly
; EcoCharge - Controle Inteligente de Potência

MOV R0, #100

LDR R1, [R2]

CMP R1, R0

BGT REDUZ_CARGA

MOV R3, #0
MOV R4, #22

B CONTINUA

REDUZ_CARGA:

MOV R3, #1
MOV R4, #7

CONTINUA:

NOP
```

Nesse trecho, o sistema realiza a leitura do consumo energético atual e verifica se o valor ultrapassa o limite definido.

Se o consumo estiver dentro do esperado, o carregamento segue normalmente. Caso contrário, a potência disponibilizada é reduzida automaticamente, evitando sobrecarga na rede elétrica.

A utilização de poucas instruções ajuda a diminuir o processamento necessário, tornando o sistema mais eficiente.

---

# Impactos Esperados

Com a implementação do EcoCharge, espera-se:

- reduzir riscos de sobrecarga elétrica  
- melhorar a distribuição de energia entre carregadores  
- diminuir desperdícios energéticos  
- reduzir processamento computacional desnecessário  
- melhorar a eficiência operacional dos eletropostos  
- aproveitar melhor a infraestrutura elétrica existente

Além disso, o sistema pode ajudar estabelecimentos a evitarem custos elevados com expansão elétrica.

---

# Relação com Sustentabilidade e Energias Renováveis

O EcoCharge também possui uma relação direta com sustentabilidade.

Ao distribuir melhor a energia e evitar desperdícios, o sistema contribui para um uso mais consciente dos recursos energéticos.

Outro ponto importante é que uma infraestrutura mais eficiente também facilita a integração com fontes de energia renovável, como energia solar.

Entre os principais impactos sustentáveis do projeto estão:

- redução de desperdícios energéticos  
- menor sobrecarga na rede elétrica  
- melhor aproveitamento da energia disponível  
- incentivo ao uso de energia renovável  
- menor necessidade de hardware robusto

Dessa forma, o projeto busca mostrar como conceitos de arquitetura de computadores podem contribuir para soluções mais eficientes e sustentáveis dentro da mobilidade elétrica.
