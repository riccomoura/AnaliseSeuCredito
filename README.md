# Terminal para Análise de Crédito

## Ao realizar um pequeno desafio de algoritmo utilizando condicionais compostas, me peguei com dúvida sobre uma vulnerabilidade do meu código que envolvia pontuação e casa decimal. Se fosse digitado 500000 o resultado era X e se fosse digitado 500.000 o resultado era Y, o que obviamente naufragaria toda a lógica matemática do mesmo.

### Sabendo que não há um front-end acoplado ao algoritmo para restringir a forma como o usuário interage com o sistema, imaginei uma condição favorável: Meu algoritmo seria pensado para um sistema orientado por teclado numérico ou eventualmente embarcado em um sistema de entrada ABNT completo necessitando de uma didática que entregasse autonomia e independência ao usuário leigo.

![Alt Text](https://giphy.com/gifs/eOVVPMmXb2P3V6GqAy)

###Pensando na humanização do sistema, sem recursos de inteligência artificial, considerei utilizar função sleep do módulo time para gerar tempos de espera entre orientações de uso, mitigando erros e resultados imprecisos. 

### O terminal foi criado com todo carinho utilizando Python 3 no JetBrains PyCharm, módulos random, math e time. Nada além de condicionais compostas foi utilizado estruturalmente, tendo em vista que o desafio é desenvolver um algoritmo que contemple estruturas de repetição aninhadas.

