class Pessoa:
    def __init__(self, id_pessoa, nome, cpf, idade):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def exibir_dados(self):
        print("ID:", self.id_pessoa)
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Idade:", self.idade)
