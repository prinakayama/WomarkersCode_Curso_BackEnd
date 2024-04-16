# Escreva um script que pergunta ao usuário se ele deseja converter uma
# temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada
# opção, crie uma função.Plus:Crie uma terceira, que é um menu para o 
# usuário escolher a opção desejada,onde esse menu chama a função de conversão 
# correta.

def menu():
    print('Selecione uma opção:')
    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')
    print('3. Sair')


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = 0 
while opcao != 3: 
    menu()
    opcao = float(input('Informe o número da opção desejada: '))

    if opcao == 1:
        temperatura = float(input('Digite a temperatura em graus Celsius: '))
        conversao = celsius_para_fahrenheit(temperatura)
        print(f'{temperatura} graus Celsius é igual a {conversao} graus Fahrenheit.')
    elif opcao == 2:
        temperatura = float(input('Digite a temperatura em graus Fahrenheit: '))
        conversao = fahrenheit_para_celsius(temperatura)
        print(f'{temperatura} graus Fahrenheit é igual a {conversao:.2f} graus Celsius.')
    elif opcao == 3:
        print("Saindo...")
    else:
        print('Opção inválida. Tente novamente.')