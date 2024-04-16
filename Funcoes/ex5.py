# Crie uma função chamada contar_vogais que recebe uma string como 
# parâmetro.Implemente a lógica para contar o número de vogais na string
# e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais


def contar_vogais(texto):
    vogais = "aeiou"
    total_vogais = 0

    for letra in texto:
        if letra.lower() in vogais:
            total_vogais += 1

    return total_vogais


texto = input('Digite uma frase: ')
 
total_vogais = contar_vogais(texto)

print(f'O total de vogais na frase é: {total_vogais}' )