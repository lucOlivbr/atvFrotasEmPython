from motorista import Motorista
from veiculo import Carro, Caminhao, Moto, Onibus
from viagem import Viagem
from manutencao import Manutencao
from frota import Frota

frota = Frota("Frota Corporativa Python")

# criando os motoristas
m1 = Motorista(1, "Carlos Silva", "111.111.111-11", 42, "CNH123", "D")
m2 = Motorista(2, "Ana Souza", "222.222.222-22", 35, "CNH456", "B")

# criando os veiculos
v1 = Carro(1, "ABC-1234", "Toyota", "Corolla", 2020, 50000, 4)
v2 = Caminhao(2, "DEF-5678", "Mercedes", "Accelo", 2019, 120000, 8000)
v3 = Moto(3, "GHI-9012", "Honda", "CG 160", 2022, 15000, 160)
v4 = Onibus(4, "JKL-3456", "Marcopolo", "Paradiso", 2021, 80000, 42)

frota.adicionar_motorista(m1)
frota.adicionar_motorista(m2)

frota.adicionar_veiculo(v1)
frota.adicionar_veiculo(v2)
frota.adicionar_veiculo(v3)
frota.adicionar_veiculo(v4)

viagem1 = Viagem(1, m1, v2, "Contagem", "Belo Horizonte", 35)
viagem2 = Viagem(2, m2, v1, "Belo Horizonte", "Betim", 45)
frota.adicionar_viagem(viagem1)
frota.adicionar_viagem(viagem2)

manutencao1 = Manutencao(1, v3, "Troca de óleo", 180.00, "Aberta")
frota.adicionar_manutencao(manutencao1)

# contadores de id para novos cadastros
prox_id_motorista = 3
prox_id_veiculo = 5
prox_id_viagem = 3
prox_id_manutencao = 2


def cadastrar_motorista():
    global prox_id_motorista
    print("\n--- Cadastrar Motorista ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    cnh = input("Numero da CNH: ")
    categoria = input("Categoria da CNH (A/B/C/D/E): ")
    m = Motorista(prox_id_motorista, nome, cpf, idade, cnh, categoria)
    frota.adicionar_motorista(m)
    prox_id_motorista += 1
    print("Motorista cadastrado com sucesso!")


def cadastrar_veiculo():
    global prox_id_veiculo
    print("\n--- Cadastrar Veiculo ---")
    print("Tipo: 1-Carro  2-Caminhao  3-Moto  4-Onibus")
    tipo = input("Escolha: ")
    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    km = float(input("KM atual: "))

    if tipo == "1":
        portas = int(input("Quantidade de portas: "))
        v = Carro(prox_id_veiculo, placa, marca, modelo, ano, km, portas)
    elif tipo == "2":
        cap = float(input("Capacidade de carga (kg): "))
        v = Caminhao(prox_id_veiculo, placa, marca, modelo, ano, km, cap)
    elif tipo == "3":
        cil = int(input("Cilindradas: "))
        v = Moto(prox_id_veiculo, placa, marca, modelo, ano, km, cil)
    elif tipo == "4":
        cap = int(input("Capacidade de passageiros: "))
        v = Onibus(prox_id_veiculo, placa, marca, modelo, ano, km, cap)
    else:
        print("Tipo invalido.")
        return

    frota.adicionar_veiculo(v)
    prox_id_veiculo += 1
    print("Veiculo cadastrado com sucesso!")


def registrar_viagem():
    global prox_id_viagem
    print("\n--- Registrar Viagem ---")

    print("Motoristas:")
    for m in frota.lista_motoristas:
        print(" ", m.id_pessoa, "-", m.nome)
    id_m = int(input("ID do motorista: "))

    motorista = None
    for m in frota.lista_motoristas:
        if m.id_pessoa == id_m:
            motorista = m
    if motorista is None:
        print("Motorista nao encontrado.")
        return

    print("Veiculos:")
    for v in frota.lista_veiculos:
        print(" ", v.id_veiculo, "-", v.modelo, v.get_placa(), "- Status:", v.status)
    id_v = int(input("ID do veiculo: "))

    veiculo = None
    for v in frota.lista_veiculos:
        if v.id_veiculo == id_v:
            veiculo = v
    if veiculo is None:
        print("Veiculo nao encontrado.")
        return

    origem = input("Origem: ")
    destino = input("Destino: ")
    km = float(input("KM percorridos: "))

    viagem = Viagem(prox_id_viagem, motorista, veiculo, origem, destino, km)
    frota.adicionar_viagem(viagem)
    prox_id_viagem += 1


def registrar_manutencao():
    global prox_id_manutencao
    print("\n--- Registrar Manutencao ---")

    print("Veiculos:")
    for v in frota.lista_veiculos:
        print(" ", v.id_veiculo, "-", v.modelo, v.get_placa())
    id_v = int(input("ID do veiculo: "))

    veiculo = None
    for v in frota.lista_veiculos:
        if v.id_veiculo == id_v:
            veiculo = v
    if veiculo is None:
        print("Veiculo nao encontrado.")
        return

    tipo = input("Tipo de manutencao: ")
    custo = float(input("Custo (R$): "))
    status = input("Status (Aberta/Fechada): ")

    man = Manutencao(prox_id_manutencao, veiculo, tipo, custo, status)
    frota.adicionar_manutencao(man)
    prox_id_manutencao += 1
    print("Manutencao registrada!")


def menu():
    while True:
        print("\n=== SISTEMA DE CONTROLE DE FROTA ===")
        print("1. Cadastrar motorista")
        print("2. Cadastrar veiculo")
        print("3. Registrar viagem")
        print("4. Registrar manutencao")
        print("5. Listar motoristas")
        print("6. Listar veiculos")
        print("7. Listar veiculos disponiveis")
        print("8. Relatorio de viagens")
        print("9. Relatorio de manutencoes")
        print("10. Viagens por motorista")
        print("11. Custo total de manutencoes")
        print("12. KM rodados por veiculo")
        print("13. Veiculos com mais de 100.000 km")
        print("14. Polimorfismo")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_motorista()
        elif opcao == "2":
            cadastrar_veiculo()
        elif opcao == "3":
            registrar_viagem()
        elif opcao == "4":
            registrar_manutencao()
        elif opcao == "5":
            frota.listar_motoristas()
        elif opcao == "6":
            frota.listar_veiculos()
        elif opcao == "7":
            frota.listar_veiculos_disponiveis()
        elif opcao == "8":
            frota.relatorio_viagens()
        elif opcao == "9":
            frota.relatorio_manutencoes()
        elif opcao == "10":
            frota.viagens_por_motorista()
        elif opcao == "11":
            frota.custo_total_manutencao()
        elif opcao == "12":
            frota.relatorio_km_por_veiculo()
        elif opcao == "13":
            frota.veiculos_alta_quilometragem()
        elif opcao == "14":
            print("\nPOLIMORFISMO")
            for veiculo in frota.lista_veiculos:
                veiculo.realizar_atividade()
            for motorista in frota.lista_motoristas:
                motorista.realizar_atividade()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu()
