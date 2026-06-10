class Manutencao:
    def __init__(self, id_manutencao, veiculo, tipo, custo, status):
        self.id_manutencao = id_manutencao
        self.veiculo = veiculo
        self.tipo = tipo
        self.custo = custo
        self.status = status

    def exibir_dados(self):
        print("ID Manutenção:", self.id_manutencao)
        print("Veículo:", self.veiculo.modelo)
        print("Placa:", self.veiculo.get_placa())
        print("Tipo:", self.tipo)
        print("Custo: R$", self.custo)
        print("Status:", self.status)
