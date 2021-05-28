#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo, qual o nome do homem mais velho, quantas mulheres tem menos de 20 anos
mediaidade = 0
somaidade = 0
maioridade = 0
nomemaisvelho = 0
mulher20 = 0
for p in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(p)))
    idade = int(input('Qual a idade da {}ª pessoa? '.format(p)))
    sexo = str(input('Qual o sexo da {}ª pessoa? [M/F]: '.format(p)))
    somaidade = idade + 1
    if p == 1 and sexo in 'mM':
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'mM' and idade > maioridade:
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'fF' and idade < 20:
        mulher20 = mulher20 + 1
mediaidade = somaidade / 4
print('A média das idade é {}'.format(mediaidade))
print('O nome do homem mais velho é {} e sua idade é {}'.format(nomemaisvelho,maioridade))
print('A quantidade de mulheres com menos de 20 anos é de {} mulheres'.format(mulher20))


