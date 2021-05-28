#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o valor do seu salário? R$'))
if salario > 1250.00:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print('O seu novo salário é R${}'.format(aumento))


