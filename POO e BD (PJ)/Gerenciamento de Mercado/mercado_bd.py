import sqlite3

biblioteca = sqlite3.connect('biblioteca.bd')
cursor = biblioteca.cursor()

#criacao da tbl
cursor.execute('''
    CREATE TABLE fornecedores (
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        endereco VARCHAR(255) NOT NULL));
''')

cursor.execute('''
    CREATE TABLE produtos (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        categorias VARCHAR(100) NOT NULL,
        quantidade_disponivel INTEGER NOT NULL,
        FOREIGN KEY(id_fornecedor) REFERENCES fornecedor(id));
''')

cursor.execute('''
    CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL));
''')

cursor.execute('''
    CREATE TABLE transacoes (
        id INT PRIMARY KEY,
        data DATE NOT NULL,
        FOREIGN KEY(id_cliente) REFERENCES clientes(id),
        FOREIGN KEY(id_produto) REFERENCES produtos(id));
''')

# # Inserção de Dados nas tabelas:
cursor.execute('''
    INSERT INTO fornecedores (id, nome, telefone, endereco) VALUES
        (1,"Marcella Amazonas", "81999999999", "Avenida Boa Viagem, 545, ap 120, Boa viagem, Recife, Pernambuco" ),
        (2,"Priscila Nakayama", "11999999999", "Avenida São Paulo, 234, ap 1200, Mogi das Cruzes, São Paulo"),
        (3,"Pedro Silva", "84999999999", "Rua Professor Luiz, 767, Jaboatão, Recife, Pernambuco" ),
        (4,"Livia Maria", "91999999999", "Rua D, 567, Minas Gerais"),
        (5,"Ana Oliveira", "21999999999", "Rua das Graças, 301, Recife, Pernambuco"),
        (6,"Pedro Costa", "22999999999", "Travessa F, 123, Salvador, Bahia"),
        (7,"Laura Fernandes", "33999999999", "Rua das Flores, 5678, Florianópolis, Santa Catarina"),
        (8,"Victor Correia", "54999999999", "Rua Guiliano Professor, 9087, ap 2300, João Pessoa,Paraiba"),
        (9,"Eliane Santos", "89999999999", "Avenida dos Ventos, 456, Vista Bela, Piauí" ),
        (10,"Giovana Lacerda", "75999999999", "Rua das Borboletas, 123, Jardim Primavera, Alagoas" )
''')

cursor.execute('''
    INSERT INTO produtos(id, nome, categoria, quantidade_disponivel, id_fornecedor) VALUES
        (100,'vestuario', 541, 1),
        (101,'calcados', 784, 2),
        (102,'vestuario', 22, 3),
        (103,'vestuario', 265, 4),
        (104,'vestuario', 385, 5),
        (105,'vestuario', 693, 6),
        (106,'vestuario', 147, 7),
        (107,'vestuario', 120, 8),
        (108,'vestuario', 460, 9),
        (109,'vestuario', 852, 10),
''')

cursor.execute('''
    INSERT INTO clientes (id, nome, telefone) VALUES
        (200, "Marcella Amazonas", "81999999999"),
        (201, "Priscila Nakayama", "11999999999" ),
        (202, "Pedro Silva", "84999999999"),
        (203, "Livia Maria", "91999999999"),
        (204, "Ana Oliveira", "21999999999"),
        (205, "Pedro Costa", "22999999999"),
        (206, "Laura Fernandes", "33999999999"),
        (207, "Victor Correia", "54999999999" ),
        (208, "Eliane Santos", "89999999999"),
        (209, "Giovana Lacerda", "75999999999")
''')

cursor.execute('''
    INSERT INTO transacoes (id, data, id_cliente, id_produto) VALUES
        (1000, '2024-04-16', 200,100 ),
        (1001, '2024-04-16', 201,101 ),
        (1002, '2024-04-16', 202,102 ),
        (1003, '2024-04-16', 203,103 ),
        (1004, '2024-04-16', 204,104 ),
        (1005, '2024-04-16', 205,105 ),
        (1006, '2024-04-16', 206,106 ),
        (1007, '2024-04-16', 207,107 ),
        (1008, '2024-04-16', 208,108 ),
        (1009, '2024-04-16', 209,109 ),
''')

# Listar todos os produtos em estoque 
cursor.execute(''' SELECT * FROM produtos WHERE quantidade_disponivel > 0; ''')

#Encontrar as vendas realizadas por um cliente especifico 
cursor.execute(''' SELECT * FROM transacoes WHERE id_cliente = 208; ''')

# Calcular o total de Vendas por categoria de produto 
cursor.execute(''' SELECT p.categoria, SUM(s.preco_total) as TotalVendas FROM transacoes s 
               JOIN produtos p ON s.id_produto = 106 GROUP BY p.categoria; ''')

# Identificar os produtos mais vendidos 
cursor.execute(''' SELECT p.nome, SUM(s.quantidade) as TotalQtdVendida
               FROM transacoes s
               JOIN produtos p ON s.id_produto = 105
               GROUP BY p.nome 
               ORDER BY TotalQtdVendida DESC; ''')
