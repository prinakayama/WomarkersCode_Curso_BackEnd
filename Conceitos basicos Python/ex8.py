# Faça um Programa qu pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

valor_hora = float(input('Qual eh o valor hora? R$'))
horas_trabalhadas = float(input('Quantas horas voce trabalhou no mes? '))

salario = horas_trabalhadas * horas_trabalhadas

print('O seu salario esse mes eh R${:.2f}'.format(salario))