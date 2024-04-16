# Criar um programa em Python que solicite três números ao usuário,
# utilize estruturas condicionais para determinar o maior entre eles e 
# apresente o resultado.

num1 = float(input('Digite o primeiro numero:'))
num2 = float(input('Digite o segundo numero:'))
num3 = float(input('Digite o terceiro numero:'))

if num1>= num2 and num1 >= num3:
    maior_num = num1
elif num2 >= num1 and num2 >= num3:
    maior_num = num2
else: 
    maior_num = num3
    
print(f'O maior numero eh {maior_num}:')