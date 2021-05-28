peso1 = float(input('Digite o peso da 1ª pessoa: '))
menorpeso = peso1
maiorpeso = peso1
for p in range(2, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '))
    if peso > peso1:
        maiorpeso = peso
    if peso < peso1:
        menorpeso = peso
print('O MAIOR peso é {}Kg'.format(maiorpeso))
print('O MENOR peso é {}Kg'.format(menorpeso))