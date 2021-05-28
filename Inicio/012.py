#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('Gostaríamos de saber de você, os valores de três retas para formar um triângulo, para isso, preciso '
      'que digite três valores: ')
v1 = int(input('Qual o primeiro valor? '))
v2 = int(input('Qual o segundo valor? '))
v3 = int(input('Qual o terceiro valor? '))
if (v1<(v2+v3) and v1>(v2-v3)) and (v2<(v1+v3) and v2>(v1-v3)) and (v3<(v1+v2) and v3>(v1-v2)):
    print('Os valores digitados {}, {} e {} podem formar um triângulo.'.format(v1,v2,v3))
else:
    print('Os valores digitados {},{} e {} NÃO podem formar um triângulo.'.format(v1,v2,v3))
