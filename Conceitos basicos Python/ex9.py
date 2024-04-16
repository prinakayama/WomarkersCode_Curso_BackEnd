# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício

hr_semana = float(input('Digite o numero de horas de exercicios fisico praticados por semana: '))

min_semana = (hr_semana * 60) * 4

calorias_mes = min_semana  * 5

print( f'O total de calorias queimadas por mes é: {calorias_mes}')