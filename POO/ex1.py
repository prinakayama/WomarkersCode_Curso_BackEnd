'''1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.'''

class Carro:
    def __init__(self, ligado=False, cor='', modelo='', velocidade=0):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelera(self, quantidade):
        if self.ligado:
            self.velocidade += quantidade
        else:
            print('O carro está desligado.')

    def desacelera(self, quantidade):
        if self.ligado:
            self.velocidade -= quantidade
            if self.velocidade < 0:
                self.velocidade = 0
        else:
            print('O carro está desligado.')


carro = Carro(cor='vermelho', modelo='Fusca')

carro.ligar()
carro.acelera(50)
print(f'O carro está a {carro.velocidade} km/h.')
carro.acelera(50)
print(f'O carro está a {carro.velocidade} km/h.')


carro.desacelera(50)
print(f'O carro está a {carro.velocidade} km/h.')
carro.desacelera(50)
print(f'O carro está parado.')
carro.desligar()
carro.desacelera(10)