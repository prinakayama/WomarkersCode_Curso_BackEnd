# Reverso do número. Faça uma função que retorne o reverso de um número
# inteiro informado. Por exemplo:127->721.

def reverso_num(num):
    return int(str(num)[::-1])

num = int(input('Digite um número inteiro: '))

reversao = reverso_num(num)

print(f'O número revertido é: {reversao}' )