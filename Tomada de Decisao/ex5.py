# Desenvolva um programa que solicite ao usuário os comprimentos dos 
# três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.

lado_a = float(input('Digite o comprimento do lado A :'))
lado_b = float(input('Digite o comprimento do lado B :'))
lado_c = float(input('Digite o comprimento do lado C :'))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    if lado_a == lado_b == lado_c:
        print('Triangulo equilatero')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('Triangulo isosceles')
    else:
        print('Triangulo escaleno')

else: 
    print(' Os valores informados nao formam um triangulo valido! ')