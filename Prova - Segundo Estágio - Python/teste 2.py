#Faça um programa que lê 4 números reais em uma lista,
#calcula e exibe a quantidade de números negativos
#e a soma de números positivos dessa mesma lista
listanum = []
neg = 0
pos = 0
#preenchimento da lista
for n in range(1, 5):
    numero = (float(input(f'Digite o {n}º número: ')))
    listanum.append(numero)
#varredura (percorrer a lista completamente)
for numero in listanum:
    if numero < 0:
        neg = neg + 1
    if numero > 0:
        pos = pos + numero
print(f'A quantidade de números negativos é: {neg}')
print(f'A soma dos números positivos é: {pos}')