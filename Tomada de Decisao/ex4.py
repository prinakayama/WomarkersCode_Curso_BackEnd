# Implemente um programa que classifique um aluno com base em sua pontuação
# em um exame. O programa deverá solicitar uma nota de 0 a 10. 
# Se a pontuação for maior ou igual a 7, o aluno é aprovado;
# caso contrário, é reprovado

nota = None
while nota is None: 
    nota = float(input('Informe uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Nota invalida!')
        nota = None

if nota >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print('O aluno foi {}.'.format(resultado))