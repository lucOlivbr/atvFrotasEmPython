class Veiculo:
    def __init__(self, id_veiculo, placa, marca, modelo, ano, km):
        self.id_veiculo = id_veiculo
        self.__placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km
        self.status = "Disponível"

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        self.__placa = placa

    def alterar_status(self, status):
        self.status = status

    def realizar_atividade(self):
        print("Veículo em operação.")

    def exibir_dados(self):
        print("ID:", self.id_veiculo)
        print("Placa:", self.__placa)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("KM:", self.km)
        print("Status:", self.status)


class Carro(Veiculo):
    def __init__(self, id_veiculo, placa, marca, modelo, ano, km, quantidade_portas):
        super().__init__(id_veiculo, placa, marca, modelo, ano, km)
        self.quantidade_portas = quantidade_portas

    def realizar_atividade(self):
        print("Carro utilizado para deslocamento administrativo.")

    def exibir_dados(self):
        super().exibir_dados()
        print("Portas:", self.quantidade_portas)


class Caminhao(Veiculo):
    def __init__(self, id_veiculo, placa, marca, modelo, ano, km, capacidade_carga):
        super().__init__(id_veiculo, placa, marca, modelo, ano, km)
        self.capacidade_carga = capacidade_carga

    def realizar_atividade(self):
        print("Caminhão utilizado para transporte de carga.")

    def exibir_dados(self):
        super().exibir_dados()
        print("Capacidade de carga (kg):", self.capacidade_carga)


class Moto(Veiculo):
    def __init__(self, id_veiculo, placa, marca, modelo, ano, km, cilindradas):
        super().__init__(id_veiculo, placa, marca, modelo, ano, km)
        self.cilindradas = cilindradas

    def realizar_atividade(self):
        print("Moto utilizada para entregas rápidas.")

    def exibir_dados(self):
        super().exibir_dados()
        print("Cilindradas:", self.cilindradas)


class Onibus(Veiculo):
    def __init__(self, id_veiculo, placa, marca, modelo, ano, km, capacidade_passageiros):
        super().__init__(id_veiculo, placa, marca, modelo, ano, km)
        self.capacidade_passageiros = capacidade_passageiros

    def realizar_atividade(self):
        print("Ônibus utilizado para transporte de funcionários.")

    def exibir_dados(self):
        super().exibir_dados()
        print("Capacidade de passageiros:", self.capacidade_passageiros)
