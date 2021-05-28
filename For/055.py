#Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o MAIOR e o MENOR peso lidos
maior = 0
menor = 0
for c in range(1, 6):
   peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
   if c == 1:
       maior = peso
       menor = peso
   else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print('{:.0f}Kg é o maior peso'.format(maior))
print('{:.0f}Kg é o menor peso'.format(menor))

