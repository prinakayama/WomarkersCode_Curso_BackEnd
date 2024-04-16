# Escreva um programa que calcule o tempo de uma viagem.
# Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração: avião = 600km/h carro = 100km/h ônibus = 80km/h

aviao = 600
carro = 100
onibus = 80

distancia = float(input('Informe a distancia da viagem em Km:'))
tipo_transporte = input('Digite qual o meio de transporte (aviao, carro ou onibus) ')

if tipo_transporte.lower() == "aviao":
    duracao_viagem = distancia / aviao
elif tipo_transporte.lower() == "carro":
    duracao_viagem = distancia / carro
elif tipo_transporte.lower() == "onibus":
    duracao_viagem = distancia / onibus
else:
    print('Informe um meio de transporte valido! ')
    exit()

print("A duracao da viagem eh {:.2f} horas.".format(duracao_viagem))