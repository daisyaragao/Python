#Cada espectador de um cinema respondeu a um questionário no qual constava
#sua opinião em relação ao filme: ótimo-3, bom-2, regular-1.
#Faça um programa que receba a opinião de 5 espectadores em uma lista, calcule e mostre:
#- a quantidade de pessoas que responderam ótimo
#- a quantidade de pessoas que responderam bom
#- a quantidade de pessoas que responderma regular
listafilme = []
otimo = 0
bom = 0
regular = 0
for p in range(1, 6):
    pessoas = str(input('Qual a sua opinião sobre o filme? Responda com [ótimo, bom ou regular]:'))
    listafilme.append(pessoas)
    if pessoas == 'ótimo':
        otimo = otimo + 1
    if pessoas == 'bom':
        bom = bom + 1
    if pessoas == 'regular':
        regular = regular + 1
    else:
        while pessoas != 'ótimo' and pessoas != 'bom' and pessoas != 'regular':
            pessoas = str(input('Comanda inválido! Responda com [ótimo, bom ou regular]:'))
print(f'A quantidade de pessoas que considerou o filme ótimo: {otimo}')
print(f'A quantidade de pessoas que considerou o filme bom: {bom}')
print(f'A quantidade de pessoas que considerou o filme regular: {regular}')






