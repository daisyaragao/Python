#Faça programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
num = int(input('Digite um número e descubra se ele é um número primo: '))
for c in range(1, num+1):
    if num % c == 0:
        cont = cont+1
print('O {} escolhido foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('O número escolhido é PRIMO')
else:
    print('O número escolhido NÃO é primo')



