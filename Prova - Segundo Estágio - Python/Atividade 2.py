#Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:
#A quantidade de produtos com preço inferior a R$ 50,00
#A quantidade de produtos com preço entre R$ 50,00 e 80,00
#A média de preço
#O preço mais barato

listapreco = []
cont1 = cont2 = somapreco = mediapreco = 0
for p in range(1, 6):
    preco = float(input(f'Digite o valor do {p}º produto R$: '))
    listapreco.append(preco)
for preco in listapreco:
    somapreco = somapreco + preco
    if preco < 50:
        cont1 = cont1 + 1
    if preco >= 50 and preco <= 80:
        cont2 = cont2 + 1
mediapreco = somapreco / 5
print(f'Os valores dos produtos digitados foram: {listapreco}')
print(f'A quantidade de produtos com preço inferior a R$ 50,00 é: {cont1}')
print(f'A quantidade de produtos com preço entre R$ 50,00 e 80,00 é: {cont2}')
print(f'A média de preço dos produtos é R$: {mediapreco}')
print(f'O produto com menor preço R$: {min(listapreco)}')





