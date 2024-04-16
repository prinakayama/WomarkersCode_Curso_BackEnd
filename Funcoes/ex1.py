# Faça um programa,com uma função que necessite de três argumentos,e que forneça a soma desses 
# três argumentos

def soma_arg(x,y,z):
    
    return x + y + z

arg1 = float(input('Digite o primeiro argumento '))
arg2 = float(input('Digite o segundo argumento '))
arg3 = float(input('Digite o terceiro argumento '))

resultado = soma_arg(arg1, arg2,arg3)

print('A soma dos tres argumentos sao ',resultado)