## Repositório para o trabalho de Controle Clássico 🕹️

O objetico do trabalho é aplicar conceitos vistos em um projeto de uma planta de temperatura.

### Questões 🧪
- ```1- Levante  a  função  de  transferência  da  planta  destinada  ao  seu  grupo.```
- ```2- Escolha o método de identificação da planta e com isso encontre os valores de k, Ɵ e τ.```
- ```3- Plote a resposta original em relação a estimada na mesma figura e verifique se a aproximação foi satisfatória.```
- ```4- Levante os valores de erro da planta em malhar aberta e fechada, fazendo comentários sobre os resultados.```
- ```5- Realize a simulação e fale sobre o que aprendeu sobre a história e teoria do método novo em comparação com o clássico.```
- ```6- Realize o ajuste fino  se necessário, comentando o que  foi  feito e qual o reflexo desse ajuste na resposta do sistema.```
- ```7-  Ao  comparar os métodos, você  identificou alguma  desvantagem  no método tradicional? Caso sim, o novo método resolveu o problema? Explique!```
- ```8- Crie  uma  interface  que  permita  com  que  o  usuário  entre  com  os  dados  os parâmetros do PID e do Setpoint.```

### Métodos Designados 🔎
- ```Método clássico IMC```: O método IMC (Internal Model Control) foi proposto por Rivera et al (1986). Neste método o controlador possui um modelo interno do processo no qual utiliza a função de transferência da planta para determinar o ajuste dos parâmetros PID.

  Para um processo de baixa ordem sem tempo morto (atraso de resposta) o trabalho propõe as regras de ajuste dos parâmetros do controlador PID, dado como uma função de um parâmetro ajustável 𝜆, o qual determina a velocidade da resposta. Quanto menor o valor de 𝜆 mais rápida a resposta  e  melhor o  desempenho.  No entanto, a resposta  será mais  sensível às perturbações  do processo (RIVERA et al, 1986). 
- ```Método novo Integral de Erro```: O Método da Integral do Erro (IAE), também conhecido como Método da Integral do Erro Absoluto, é uma técnica de controle utilizada em sistemas de controle automático, como controle PID (Proporcional-Integral-Derivativo). Esse método é uma extensão do controle proporcional e integral, onde a principal finalidade é reduzir o erro em regime permanente a zero.

  Em sistemas de controle, o erro é a diferença entre o valor de referência desejado e o valor real da variável controlada. O controle proporcional (P) age em função do erro atual, o controle integral (I) age acumulando os erros passados ao longo do tempo e o controle derivativo (D) age com base na taxa de variação do erro. Enquanto o controle proporcional e integral podem reduzir o erro em regime permanente, o controle derivativo ajuda a melhorar a resposta transitória, ou seja, a estabilidade do sistema.

### Autores 💻
```
Pedro Pereira Guimarães - GEC - 1666
Nathan Santos Ataliba - GEC- 1663
```


