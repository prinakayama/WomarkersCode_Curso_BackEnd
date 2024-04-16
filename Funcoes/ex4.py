# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
# e calcule quanto poderia comprar de cada moeda estrangeira. Considere 
# a tabela de conversão abaixo: Dólar Americano:R$4,91 Peso Argentino:R$0,02
# Dólar Australiano:R$3,18 Dólar Canadense:R$3,64 Franco Suiço:R$0,42
# Euro:R$5,36 Libra esterlina:R$6,21

def converte_dinheiro(quantia, taxa):
   
    return quantia / taxa


dinheiro = float(input('Digite o valor em reais que você tem na carteira: R$'))


dollar_americano = converte_dinheiro(dinheiro, 4.91)
peso_argentino = converte_dinheiro(dinheiro, 0.02)
dolar_australiano = converte_dinheiro(dinheiro, 3.18)
dolar_canadense = converte_dinheiro(dinheiro, 3.64)
franco_suico = converte_dinheiro(dinheiro, 0.42)
euro = converte_dinheiro(dinheiro, 5.36)
libra_esterlina = converte_dinheiro(dinheiro, 6.21)


print('\nCom R${:.2f} você pode comprar:'.format(dinheiro))
print('{:.2f} Dólares Americanos'.format(dollar_americano))
print('{:.2f} Pesos Argentinos'.format(peso_argentino))
print('{:.2f} Dólares Australianos'.format(dolar_australiano))
print('{:.2f} Dólares Canadenses'.format(dolar_canadense))
print('{:.2f} Francos Suíços'.format(franco_suico))
print('{:.2f} Euros'.format(euro))
print('{:.2f} Libras Esterlinas'.format(libra_esterlina))