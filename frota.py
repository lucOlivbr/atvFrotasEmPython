class Frota:
    def __init__(self, nome):
        self.nome = nome
        self.lista_veiculos = []
        self.lista_motoristas = []
        self.lista_viagens = []
        self.lista_manutencoes = []

    def adicionar_veiculo(self, veiculo):
        self.lista_veiculos.append(veiculo)

    def adicionar_motorista(self, motorista):
        self.lista_motoristas.append(motorista)

    def adicionar_viagem(self, viagem):
        # nao permite viagem com veiculo em manutencao
        if viagem.veiculo.status == "Em manutenção":
            print("Erro: o veiculo", viagem.veiculo.modelo, "esta em manutencao e nao pode viajar.")
            return
        self.lista_viagens.append(viagem)
        viagem.motorista.adicionar_viagem(viagem)
        viagem.veiculo.km += viagem.km_percorridos

    def adicionar_manutencao(self, manutencao):
        self.lista_manutencoes.append(manutencao)
        manutencao.veiculo.alterar_status("Em manutenção")

    def listar_veiculos(self):
        print("\nVEICULOS DA FROTA")
        for veiculo in self.lista_veiculos:
            veiculo.exibir_dados()
            print("--------------------")

    def listar_motoristas(self):
        print("\nMOTORISTAS")
        for motorista in self.lista_motoristas:
            motorista.exibir_dados()
            print("--------------------")

    def relatorio_viagens(self):
        print("\nRELATORIO DE VIAGENS")
        for viagem in self.lista_viagens:
            viagem.exibir_dados()
            print("--------------------")

    def relatorio_manutencoes(self):
        print("\nRELATORIO DE MANUTENCOES")
        for manutencao in self.lista_manutencoes:
            manutencao.exibir_dados()
            print("--------------------")

    def viagens_por_motorista(self):
        print("\nVIAGENS POR MOTORISTA")
        for motorista in self.lista_motoristas:
            print(motorista.nome, "-", motorista.total_viagens(), "viagem(ns)")

    def custo_total_manutencao(self):
        total = 0
        for m in self.lista_manutencoes:
            total += m.custo
        print("\nCUSTO TOTAL DE MANUTENCOES")
        print("Total: R$", total)

    def listar_veiculos_disponiveis(self):
        print("\nVEICULOS DISPONIVEIS")
        for veiculo in self.lista_veiculos:
            if veiculo.status == "Disponível":
                print(veiculo.modelo, "- Placa:", veiculo.get_placa(), "- KM:", veiculo.km)

    def relatorio_km_por_veiculo(self):
        print("\nKM RODADOS POR VEICULO")
        for veiculo in self.lista_veiculos:
            print(veiculo.modelo, "("+veiculo.get_placa()+"): ", veiculo.km, "km")

    def veiculos_alta_quilometragem(self):
        print("\nVEICULOS COM MAIS DE 100.000 KM")
        for veiculo in self.lista_veiculos:
            if veiculo.km > 100000:
                print(veiculo.modelo, "- Placa:", veiculo.get_placa(), "- KM:", veiculo.km)
