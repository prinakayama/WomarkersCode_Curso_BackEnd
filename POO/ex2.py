'''O banco Banco Delas é um banco moderno e eficiente, com
vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo.
● Cada conta corrente pode ter um ou mais clientes como
titular.
● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque
especial.
Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata" '''

from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

class ContaCorrente(ABC):
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

class ContaCorrenteMulher(ContaCorrente):
    def __init__(self, clientes):
        super().__init__(clientes)

    def sacar(self, valor):
        if self.saldo - valor >= -self.clientes[0].renda_mensal:
            self.saldo -= valor
            self.operacoes.append(f"Saque: R${valor}")
            return True
        else:
            print("Saque não permitido. Valor excede o cheque especial.")
            return False

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: R${valor}")

class ContaCorrenteHomem(ContaCorrente):
    def __init__(self, clientes):
        super().__init__(clientes)

    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            self.operacoes.append(f"Saque: R${valor}")
            return True
        else:
            print("Saque não permitido. Saldo insuficiente.")
            return False

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: R${valor}")

# Exemplo de uso:
cliente_mulher = Cliente("Maria", "123456789", 3000)
cliente_homem = Cliente("João", "987654321", 2500)

conta_mulher = ContaCorrenteMulher([cliente_mulher])
conta_homem = ContaCorrenteHomem([cliente_homem])

conta_mulher.depositar(2000)
conta_mulher.sacar(4000)  # Saque acima do cheque especial
conta_mulher.sacar(1000)  # Saque dentro do cheque especial

conta_homem.depositar(1500)
conta_homem.sacar(2000)  # Saque com saldo insuficiente
conta_homem.sacar(1000)  # Saque com saldo suficiente


                            