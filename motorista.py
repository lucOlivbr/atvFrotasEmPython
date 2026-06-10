from pessoa import Pessoa

class Motorista(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, idade, cnh, categoria):
        super().__init__(id_pessoa, nome, cpf, idade)
        self.__cnh = cnh
        self.categoria = categoria
        self.viagens = []

    def get_cnh(self):
        return self.__cnh

    def set_cnh(self, cnh):
        self.__cnh = cnh

    def adicionar_viagem(self, viagem):
        self.viagens.append(viagem)

    def total_viagens(self):
        return len(self.viagens)

    def realizar_atividade(self):
        print(self.nome, "está dirigindo um veículo da frota.")

    def exibir_dados(self):
        super().exibir_dados()
        print("CNH:", self.__cnh)
        print("Categoria:", self.categoria)
        print("Total de viagens:", self.total_viagens())
