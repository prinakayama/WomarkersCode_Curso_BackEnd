# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja invalido e continue pedindo ae que o usuario informe um valor valido


while True:
    num = float(input("Informe um numero entre 0 e 10: "))
    if 0 <= num <= 10:
        break
    else:
        print("Valor invalido! Por favor informe um nuero entre 0 e 10.")