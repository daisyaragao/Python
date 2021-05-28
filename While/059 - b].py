n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while True:
    numeros = [n1, n2]
    print('[ 1 ] SOMAR \n[ 2 ] MULTIPLICAR \n[ 3 ] MAIOR VALOR \n[ 4 ] NOVOS NÚMEROS \n[ 5 ] SAIR DO PROGRAMA')
    x = str(input('Escolha: '))
    if x in '1':
        print(f'A soma é {n1 + n2}')
    if x in '2':
        print(f'A multiplicação é {n1 * n2}')
    if x in '3':
        if n1 == n2:
            print(f'{n1} e {n2} são números iguais')
        else:
            print(f'O maior número é {max(numeros)}')
    if x in '4':
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if x not in '12345':
        x = str(input('NÚMERO INVALIDO! Escolha novamente: '))
    if x in '5':
        break
print('PROGRAMA ENCERRADO...')