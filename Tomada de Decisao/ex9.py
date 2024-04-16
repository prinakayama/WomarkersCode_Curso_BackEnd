# O programa deve calcular e apresentar a quantidade de números pares 
# e ímpares inseridos. O processo de leitura deve ser encerrado quando 
# o usuário informar o valor zero. Certifique-se de incluir validações 
# para garantir que apenas números positivos sejam considerados
# na contagem e cálculos

num_pares = 0
num_impares = 0

while True:
    num = int(input('Digite um numero (ou zero para sair): '))

    if num == 0:
        break
    
    if num > 0:
       
        if num % 2 == 0:
            num_pares += 1
       
        else:
            num_impares += 1
    else:
        print('Apenas numeros positivos são aceitos.')


print('A quantidade de numeros pares inseridos é: {}'.format(num_pares))
print('A quantidade de numeros impares inseridos é: {}'.format(num_impares))