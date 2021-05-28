# Crie um algoritmo que leia um número,mostre o seu dobro,triplo e raiz quadrada

n = int(input('Digite um número: '))
d = 2*n
t = 3*n
r = n**(1/2)
print('O dobro do número é: {}, o triplo do número é: {}, e sua raiz quadrada é: {:.0f}'.format(d, t, r))
