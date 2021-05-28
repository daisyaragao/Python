#Desenvolva um programa que pergunte a distância de uma viagem em quilometros
#Calucule o preço da passagem cobrando 0,50 centavos por km para viagens de até 200km.
#E 0,45 por km para viagens mais longas
distância = float(input('Qual a distância de sua viagem em km? '))
if distância <= 200:
    valor1 = distância * 0.50
    print('Sua viagem custará {:.0f} reais '.format(valor1))
if distância > 200:
    valor2 = distância * 0.45
    print('Sua viagem custará {:.0f} reais'.format(valor2))
print('Obrigado!')