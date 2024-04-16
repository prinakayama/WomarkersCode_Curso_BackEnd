# Desenvolver um programa que solicite a idade do usuário e identifique
# se ele é uma criança, um adolescente, adulto ou idoso

idade = int(input('Informe sua idade: '))

if idade < 13: 
    print('Voce eh uma crianca! ')
elif idade < 18:
    print('Voce eh um adolescente! ')
elif idade < 60:
    print('Voce eh adulto! ')
else:
    print('Voce eh idoso')