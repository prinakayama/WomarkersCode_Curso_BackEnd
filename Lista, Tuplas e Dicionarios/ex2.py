# Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene 
# numa lista a média de cada aluno, imprima o número de alunos com média
# maior ou igual a 7.0

media_notas = []

for i in range (5):
    nota1 = float(input('Informe a primeira nota do aluno:'))
    nota2 = float(input('Informe a segunda nota do aluno:'))
    nota3 = float(input('Informe a terceira nota do aluno:'))
    nota4 = float(input('Informe a quarta nota do aluno:'))
   
    
    media = (nota1 + nota2 + nota3 + nota4) / 4 
    media_notas.append(media)
    
num_estudante_acima_media = 0

for media in media_notas:
    if media >= 7:
        num_estudante_acima_media +=1
        
print('Quantidade de estudantes com media 7 ou maior eh :', num_estudante_acima_media)