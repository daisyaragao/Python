#Faça um programa que lê 6 números reais em uma matriz 3x2, calcula e exibe:
#A média dos números positivos
#A soma dos números negativos
#O maior número positivo
#O maior número positivo da 2ª linha

somapos = contpos = mediapos = somaneg = maiorpos = maiorpos2 = 0
matriz = [[0, 0], [0, 0], [0, 0]]
for l in range(0, 3):
    for c in range(0, 2):
        matriz[l][c] = float(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 2):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] > 0:
            somapos = somapos + matriz[l][c]
            contpos = contpos + 1
            maiorpos = max(matriz[0][0], matriz[0][1], matriz[1][0], matriz[1][1], matriz[2][0], matriz[2][1])
            maiorpos2 = max(matriz[1][0], matriz[1][1])
        if matriz[l][c] < 0:
            somaneg = somaneg + matriz[l][c]
    print()
mediapos = somapos / contpos
print(f'A média dos números positivos é: {mediapos}')
print(f'A soma dos números negativos é: {somaneg}')
print(f'O maior número positivo é: {maiorpos}')
print(f'O maior número positivo da 2ª linha é: {maiorpos2}')

