# Controle de Temperatura para Estufa
## Descrição do Projeto

Este projeto implementa um sistema de controle de temperatura para uma estufa utilizando lógica fuzzy. O sistema regula a potência do resfriador (de 0 a 100%) com base na temperatura atual fornecida por um sensor (-10 a 10°C). Ele é capaz de operar em diferentes modos definidos por setpoints específicos: Armazenamento de Vacinas a 2°C, Temperatura de Mantimento Fora de Operação a 6°C e Armazenamento de Amostras Biológicas a 8°C.

## Funcionamento do Sistema

O sistema utiliza a técnica de controle fuzzy para determinar a potência do resfriador com base no erro de temperatura e na variação desse erro em relação ao setpoint estabelecido. Para isso, o código realiza as seguintes etapas:

1. **Definição das Variáveis Fuzzy:**
   - `errotemp`: Representa o erro de temperatura.
   - `varerrotemp`: Representa a variação do erro de temperatura.
   - `resfriador`: Representa a potência do resfriador.

2. **Funções de Pertinência:**
   - Cada variável fuzzy é dividida em conjuntos fuzzy (Muito Baixo, Baixo, Médio, Alto e Muito Alto) com funções de pertinência que definem os limites e associações de valores.

3. **Regras Fuzzy:**
   - Com base nos conjuntos fuzzy das variáveis de entrada (`errotemp` e `varerrotemp`), são definidas regras fuzzy que relacionam o erro e sua variação com a potência do resfriador.

4. **Simulação do Sistema:**
   - Um loop principal simula o comportamento do sistema.
   - Calcula o erro atual e sua variação em relação ao setpoint.
   - Utiliza o controlador fuzzy para determinar a potência do resfriador.
   - Ajusta a temperatura atual com base na potência calculada e na função de transferência estimada.

5. **Comunicação MQTT:**
   - Os valores de temperatura atual e erro são publicados em tópicos MQTT para monitoramento externo.

## Pré-Requisitos e Tecnologias Utilizadas

- **Python**
- Bibliotecas: `numpy`, `skfuzzy`, `paho.mqtt.client`, `time`

## Execução do Código

Para executar o código:

1. Certifique-se de ter todas as bibliotecas instaladas.
2. Substitua os valores dos setpoints e outras variáveis conforme necessário.
3. Execute o código em um ambiente Python adequado.

## Estrutura do Código

O código está estruturado em diversas seções:

- Importação de bibliotecas necessárias.
- Definição das variáveis fuzzy, suas funções de pertinência e regras fuzzy.
- Simulação do sistema com o loop principal.
- Publicação dos valores de temperatura atual e erro via MQTT.

## Alunos

- Pedro Pereira Guimarães
- Nathan Santos Ataliba
