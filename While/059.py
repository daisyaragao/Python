#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, 
# [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Digite o seu primeiro valor: '))
n2 = int(input('Digite o seu segundo valor: '))
op = 0
while op != 5:
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
    op = int(input('Qual a sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma dos números {} + {} é: {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O resultado da multiplicação de {} e {} é {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            print('O número maior é: {}'.format(n1))
        elif n1 == n2:
            print('Os números são iguais.')
        elif n2 > n1:
            print('O número maior é: {}'.format(n2))
    elif op == 4:
        n1 = int(input('Digite o seu primeiro valor: '))
        n2 = int(input('Digite o seu segundo valor: '))
    elif op == 5:
        print('Programa finalizado')
    else:
        print('Operação inválida, tente novamente!')












