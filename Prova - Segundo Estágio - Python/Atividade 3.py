#Faça um programa que receba o preço de um produto, calcule e mostre,
# de acordo com as tabelas a seguir, o novo preço e a classificação.
#Novo preço:
#Até R$ 50,00 - 5%
#Entre R$ 50,00 e R$ 100,00 - 10%
#Acima de R$ 100,00 - 15%
#Classificação:
#Até R$ 80,00 - Barato
#Entre R$ 80,00 e R$ 120,00 - Normal
#Entre R$ 120,00 e R$ 200,00 - Caro
#Maior que R$ 200,00 - Muito caro

produto = float(input("Digite o preço do seu produto R$:"))
if produto <= 50:
    valor = produto + (produto * 0.05)
    print(f'O novo valor do seu produto é R${valor}')
elif produto > 50 and produto <= 100:
    valor = produto + (produto * 0.10)
    print(f'O novo valor do seu produto é R${valor}')
else:
    valor = produto + (produto * 0.15)
    print(f'O novo valor do seu produto é R${valor}')
if valor <= 80:
    print('O seu produto é classificado como um item BARATO')
elif valor > 80 and valor < 120:
    print('O seu produto é classificado como um item NORMAL')
elif valor > 120 and valor < 200:
    print('O seu produto é classificado como um item CARO')
else:
    print('O seu produto é classificado como um item MUITO CARO')




