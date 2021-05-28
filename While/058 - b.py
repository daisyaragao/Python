# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer
from random import randint
numPc = randint(0, 10)
acerta = False
tentativas = 0
print('Olá! Vamos brincar um pouco?\nVocê vai ter que adivinhar em qual número estou pensando.\n'
      'Iremos te mostrar ao final quantas tentativas foram necessárias para você acertar.')
resp = str(input('Para participar responda com [S/N]: ')).strip().upper()
while resp != 'S' and resp != 'N':
    resp = str(input('Resposta inválida, tente novamente respondendo [S/N]: ')).strip().upper()
if resp == 'N':
    print('Obrigado por participar!')
else:
    while not acerta:
        n = int(input('Em que número você acha que eu estou pensando? '))
        tentativas += 1
        if n == numPc:
            acerta = True
        else:
            if n > numPc:
                print('Você está quase lá... tente um VALOR MENOR!')
            elif n < numPc:
                print('Você está quase lá... tente um VALOR MAIOR!')
print('Parabéns você acertou!\nVocê tentou {} vezes e o número que pensei foi {}.'.format(tentativas, numPc))









