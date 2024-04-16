from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade
        self._data_cadastro = datetime.now()


class Autor(Pessoa):
    def __init__(self, nome, telefone, genero ):
        super(Usuario,self).__init__(
            nome = nome,
            telefone = telefone, 
            nacionalidade = None)
        self.genero = genero

class Usuario(Pessoa):
    def __init__(self, nome, telefone, endereco, nacionalidade, email):
        super(Pessoa).__init__(
            nome = nome, 
            telefone = telefone, 
            nacionalidade = nacionalidade)
        self.endereco = endereco
        self.email = email

class Livro(ABC):
    def __init__(self, titulo, editora, generos, disponibilidade, max_renovacoes=0):
        self._titulo = titulo
        self._editora = editora
        self._generos = generos
        self.disponibilidade = disponibilidade
        self._max_renovacoes = max_renovacoes
        self._autor = []

    @property
    def disponibilidade(self):
        if self.usuario:
            return False
        return True
    
    @property
    def autor(self):
        return self._autor 
    
    def add_autor(self,autor_id, nome,telefone, genero,titulo):
        autor = Autor(nome, telefone, genero,titulo)
        self.autor.append((autor_id, autor))
    
    def add_genero(self, genero):
        if genero not in self._generos:
            self._generos.append(genero)

    def add_exemplar(self, exemplar):
        self._exemplares.append(exemplar)

    def emprestar(self, usuario, data_emprestimo):
        if not self._disponibilidade:
            print("Nenhum exemplar disponível para empréstimo.")
            return

        exemplar = self._exemplares.pop()
        estado_exemplar = "Emprestado"

        data_devolucao = data_emprestimo + timedelta(days=30)
        emprestimo = {
            "usuario": usuario,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao,
            "exemplar": exemplar,
            "estado_exemplar": estado_exemplar
        }

        self._emprestimos.append(emprestimo)

    def devolver(self, exemplar):
        for i, emprestimo in enumerate(self._emprestimos):
            if emprestimo["exemplar"] == exemplar:
                emprestimo["estado_exemplar"] = "Devolvido"
                self._exemplares.append(exemplar)
                self._emprestimos.pop(i)
                break


class Biblioteca:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self._usuarios = []
        self._livros = []


    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def adicionar_livro(self, livro):
        self._livros.append(livro)

    def remover_usuario(self, usuario):
        self._usuarios.remove(usuario)

    def remover_livro(self, livro):
        self._livros.remove(livro)

    def pesquisar_usuario(self, nome):
        for usuario in self._usuarios:
            if usuario.nome == nome:
                return usuario
        return None

    def pesquisar_livro(self, titulo):
        for livro in self._livros:
            if livro.titulo == titulo:
                return livro
        return None
    
    def emprestar_livro(self, livro, usuario,data_emprestimo, data_devolucao, num_renovacao):
        if self.disponivel == True:
            emprestimo = {"livro": livro, "usuario": usuario, "data_emprestimo": data_emprestimo, "data_devolucao": data_devolucao, "num_renovacao": num_renovacao}
            self.data_emprestimo = datetime.now()
            self.data_devolucao = self.data_emprestimo + timedelta(days=7)  
            self.emprestimos.append(emprestimo)
    
        else:
            None

    def renovar(self,emprestimo):
        if self.renovacoes_restantes > 0:
                self.renovacoes_restantes -= 1
                renovar = {"emprestimo": emprestimo, "renovar": self.data_devolucao}
                self.data_devolucao += timedelta(days=7) 
                self.renovacoes.append(renovar)
        return True
            
    def devolver(self,emprestimo):
        self.emprestimos.remove(emprestimo)

import biblioteca_bd
biblioteca = biblioteca_bd.Biblioteca()
obj_bibliotecas = {}

for biblioteca in Biblioteca:
    obj_bibliotecas[biblioteca[0]] = biblioteca(
        nome=biblioteca[1],
        telefone=biblioteca[2],
        nacionalidade=biblioteca[3],
    )

livros = biblioteca_bd.livros 
for livro in livros:
    obj_bibliotecas = obj_bibliotecas[livro[7]]
    
    usuario = None
    if livro [6]:
        usuario = obj_bibliotecas.usuarios[livro[6]]
    
    obj_bibliotecas.registrar_livro(
        livro_id=livro[0],
        titulo=livro[1],
        editora=livro[2],
        generos=livro[3],
        autor=livro[4],
        usuario = usuario
    )
    
    for biblioteca in obj_bibliotecas.values():
        print (
            f" Biblioteca {biblioteca.nome}"
        )
        
        #Exibicao de emprestimo
        for emprestimo in biblioteca.emprestimo:
            print (
                f" Emprestimo do livro {emprestimo.livro.titulo} para o usuário {emprestimo.usuario.nome}"
            )
        #Exibicao para mostrar detalhes dos livros
        for id_livro , livro in biblioteca.livros.items():
            print (
                f" Livro: {livro.titulo}, Editora: {livro.editora}, Genero: {livro.generos},Autor: {livro.autor}"
            )
        #Mostrar disponibilidade
        for emprestimo in biblioteca.emprestimo:
            if emprestimo ['livro'].status == "Disponivel":
                print(f"livro: {livro.titulo}, Editora: {livro.editora}, Genero: {livro.generos},Autor: {livro.autor}")
            else:
                print("Livro indisponivel")
        