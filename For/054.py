#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas já atingiram a maior idade e quantas são menores de idade
cont1 = 0
cont2 = 0
atual = int(input('Qual o ano atual? '))
for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}º pessoa? '.format(c)))
    if (atual - nasc) >= 18:
        cont1 = cont1+1
    else:
        cont2 = cont2+1
print('{} pessoas já atingiram a maior idade'.format(cont1))
print('{} pessoas ainda são menores de idade'.format(cont2))





