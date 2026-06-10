class Viagem:
    def __init__(self, id_viagem, motorista, veiculo, origem, destino, km_percorridos):
        self.id_viagem = id_viagem
        self.motorista = motorista
        self.veiculo = veiculo
        self.origem = origem
        self.destino = destino
        self.km_percorridos = km_percorridos
        self.status = "Finalizada"

    def exibir_dados(self):
        print("ID Viagem:", self.id_viagem)
        print("Motorista:", self.motorista.nome)
        print("Veículo:", self.veiculo.modelo)
        print("Placa:", self.veiculo.get_placa())
        print("Origem:", self.origem)
        print("Destino:", self.destino)
        print("KM percorridos:", self.km_percorridos)
        print("Status:", self.status)
