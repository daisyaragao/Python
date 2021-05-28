#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade atual do seu carro? '))
if v>80:
    print('Você foi multado e excedeu o limite de velocidade de 80km/h')
    multa = (v-80)*7
    print('O valor da sua multa é: ', multa)
print('Obrigado! Lembre-se, dirija com cuidado')
