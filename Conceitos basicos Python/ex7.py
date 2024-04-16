# Solicite ao usuário o peso em kg e a altura em centimetros.
# Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula:
# IMC=peso/(alturaxaltura).

peso = float(input('Digite o seu peso em kilos: '))

altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura * altura)

print( f'Seu Indice de Massa Corporal (IMC) é: {imc:,.2f}') 