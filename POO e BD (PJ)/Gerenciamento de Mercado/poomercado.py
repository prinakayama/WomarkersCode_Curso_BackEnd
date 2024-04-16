import datetime

class Fornecedor:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Produto:
    def __init__(self, nome, categorias, quantidade_disponivel, fornecedores):
        self.nome = nome
        self.categorias = categorias
        self.quantidade_disponivel = quantidade_disponivel
        self.fornecedores = fornecedores

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Transacao:
    def __init__(self, data, cliente, produtos):
        self.data = data
        self.cliente = cliente
        self.produtos = produtos

class Mercado:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.transacoes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def pesquisar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def realizar_transacao(self, data, cliente, produtos):
        self.transacoes.append(Transacao(data, cliente, produtos))
        for produto in produtos:
            produto.quantidade_disponivel -= produto.quantidade_comprada


mercado = Mercado()


cliente1 = Cliente("João", "1234567890")
cliente2 = Cliente("Maria", "9876543210")
mercado.adicionar_cliente(cliente1)
mercado.adicionar_cliente(cliente2)

# Add products
fornecedor1 = Fornecedor("Fornecedor 1", "1111111111", "Endereço 1")
fornecedor2 = Fornecedor("Fornecedor 2", "2222222222", "Endereço 2")
produto1 = Produto("Produto 1", ["Categoria 1"], 10, [fornecedor1])
produto2 = Produto("Produto 2", ["Categoria 2"], 5, [fornecedor2])
produto1.adicionar_fornecedor(fornecedor2)
mercado.adicionar_produto(produto1)
mercado.adicionar_produto(produto2)

# Make a transaction
data = datetime.datetime.now()
cliente = cliente1
produtos = [{"produto": mercado.pesquisar_produto("Produto 1"), "quantidade_comprada": 2},
            {"produto": mercado.pesquisar_produto("Produto 2"), "quantidade_comprada": 1}]
mercado.realizar_transacao(data, cliente, produtos)

# Print transactions
for transaction in mercado.transacoes:
    print("Data:", transaction.data)
    print("Cliente:", transaction.cliente.nome)
    print("Produtos:")
    for produto in transaction.produtos:
        print("- Nome:", produto["produto"].nome)
        print(" Quantidade comprada:", produto["quantidade_comprada"])
    print()