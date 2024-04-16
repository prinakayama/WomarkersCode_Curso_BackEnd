# Faça um Programa que pergunte em que turno você estuda. Peça para 
# digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "BomDia!", "BoaTarde!" ou "BoaNoite!" 
# ou "Valor Inválido!", conforme o caso

print('Digite M-matutino, V-vespertino ou N- noturno :')
turno = input()

if turno == "M":
    print('Bom dia !! ')
    
elif turno == "V":
    print('Boa tarde !! ')

elif turno == "N":
    print('Boa noite !! ')

else :
    print('Valor invalido! ')