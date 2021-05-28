#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer


from random import randint

c = 0
print('Vamos jogar!\n\nEu vou pensar em um número entre 0 e 10.\nVocê tem que tentar '
      'adivinhar qual é até conseguir acertar.\nSão 10 pontos no total, e a cada nova tentativa você perde um '
      'e eu ganho um.\nSerão 3 rodadas.\nNo final, quem tiver mais pontos, vence!')
p = str(input('\nPronto para começar?\nDiga S ou N. ')).strip().upper()
while p != 'S' and p != 'N':
    p = str(input('\nValor inválido. Por favor, digite novamente [S ou N]. ')).strip().upper()
if p == 'N':
    print('\nAh, que pena, teria sido divertido!')
else:
    for a in range(1, 3):
        r = randint(0, 10)
        t = int(input('\nEm que número inteiro entre 0 e 10 estou pensando? '))
        while t != r:
            t = int(input('Errado, hihi. Tente novamente! '))
            c += 1
        print('\nO número que pensei foi {}.'.format(r))
        if a < 3:
            print('Agora vamos para a próxima rodada.')
    print('\n\nPONTUAÇÃO TOTAL:\n\nSua pontuação foi {} pontos.\n\nMinha pontuação foi {} pontos. \n\n'.format(50 - c, c))
    if (50 - c) > c:
        print('Parabéns, você ganhou! Ótimas jogadas!')
    elif (50 - c) == c:
        print('Dessa vez empatamos.')
    elif (50 -c) < c:
        print('Ganhei hihih... eu sou bom mesmo!!')