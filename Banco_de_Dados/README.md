# 1.Crie uma tabela chamada "alunos" com os seguintes campos:id(inteiro), nome(texto), idade(inteiro) e curso(texto).
## CREATE TABLE alunos (id INTEGER primary key, nome TEXT not null, idade INTEGER, curso TEXT);

# 2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
## INSERT INTO alunos VALUES(01, 'Priscila', 39,'Ciencia de Dados');

# 3.Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
## SELECT * FROM alunos;

# b) Selecionar o nome e a idade dos alunos com mais de 20anos.
## SELECT nome FROM alunos WHERE idade > 20;

# c)Selecionar os alunos do curso de "Engenharia" em ordem alfabética. 
## SELECT nome FROM alunos WHERE curso ='Engenharia' ORDER BY Nome ASC; 

# d)Contar o número total de alunos na tabela 
## SELECT COUNT(*) AS total_alunos FROM alunos;

# 4.Atualização e Remoção
# a)Atualize a idade de um aluno específico na tabela.
## UPDATE alunos SET idade =  26 WHERE id = 01;

# b)Remova um aluno pelo seu ID.
## DELETE FROM alunos WHERE id = 02;

# 5. Criar uma Tabela e Inserir Dados   
# Crie uma tabela chamada "clientes" com os campos: id(chave primária), nome(texto), idade(inteiro) e saldo(float).
## CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, saldo FLOAT);

# Insira alguns registros de clientes na tabela.
## INSERT INTO clientes VALUES(101, 'Sara', 37, 4567.78);

# 6. Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:
# a)Selecione o nome e a idade dos clientes com idade superior a 30anos. 
## SELECT nome FROM clientes WHERE idade > 30;

# b)Calcule o saldo médio dos clientes. 
## SELECT AVG(saldo) AS saldo_medio FROM clientes;

# c)Encontre o cliente com o saldo máximo.
## SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1;

# d)Conte quantos clientes têm saldo acima de 1000.
## SELECT COUNT(*) FROM clientes WHERE saldo > 1000;

# 7. Atualização e Remoção com Condições
# a)Atualize o saldo de um cliente específico.
## UPDATE clientes SET saldo=98758.42 WHERE id=105;

# b)Remova um cliente pelo seu ID.
## DELETE FROM clientes WHERE id=104;

# 8.Junção de Tabelas 
# Crie uma segunda tabela chamada "compras"com os campos:id(chave primária),cliente_id(chave estrangeira referenciando o id da tabela "clientes"), produto(texto) e valor(real).
## CREATE TABLE compras(id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES cliente(id));

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
## INSERT INTO compras VALUES(1000,101,'placa-mae', 1521.12);

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
## SELECT c.nome AS nome_cliente, co.produto, co.valor FROM clientes c JOIN compras co ON c.id = co.cliente_id;

## c.= clientes; co.= compras 