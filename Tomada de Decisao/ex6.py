# Crie um programa que solicite ao usuário um login e uma senha. 
# O programa deve permitir o acesso apenas se o usuário for "admin" 
# e a senha for"admin123",caso contrário imprima uma mensagem de erro.

login = str(input('Informe o seu usuario: '))
senha = str(input('Digite sua senha: '))

if login == "admin" and senha == "admin123":
    print('Acesso permitido! ')
else:
    print('Usuario ou senha incorretos! ')