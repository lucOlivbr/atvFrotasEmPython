# Sistema de Controle de Frota - Python

Atividade de POO - 1º Período  
Feito no Google Colab

## Arquivos do projeto

- pessoa.py — classe base Pessoa
- motorista.py — classe Motorista, herda de Pessoa
- veiculo.py — classes Veiculo, Carro, Caminhao, Moto e Onibus
- viagem.py — classe Viagem
- manutencao.py — classe Manutencao
- frota.py — classe Frota que gerencia tudo
- main.py — arquivo principal com o menu

## Como rodar no Google Colab

Fazer upload do arquivo `frota_corporativa.ipynb` no Google Colab e executar as células em ordem. A última célula inicia o sistema com `%run main.py`.

## Questões conceituais

**1. Qual é a diferença entre classe e objeto no sistema de frota?**

A classe é o molde, ela define como algo vai ser. Por exemplo, a classe Veiculo define que todo veículo tem placa, marca, modelo, km... Mas ela sozinha não representa nenhum veículo real. O objeto é quando a gente cria uma instância dessa classe, tipo `v1 = Carro(...)`. Aí sim temos um veículo de verdade na memória.

**2. Por que Motorista herda de Pessoa?**

Porque motorista é uma pessoa. Ele tem nome, CPF, idade igual a qualquer pessoa. Com a herança a gente não precisa repetir esses atributos na classe Motorista, só aproveita o que a classe Pessoa já tem e adiciona o que é específico do motorista, que é a CNH e a categoria.

**3. Por que Carro, Caminhao e Moto herdam de Veiculo?**

Porque todos são veículos. Todos têm placa, marca, modelo, km e status. A herança evita repetição de código. Cada subclasse só adiciona o que é diferente: o Carro tem quantidade de portas, o Caminhao tem capacidade de carga, a Moto tem cilindradas e o Onibus tem capacidade de passageiros.

**4. Onde aparece o encapsulamento no código?**

Na classe Veiculo o atributo `__placa` é privado, não dá para acessar direto de fora da classe. Para ler ou alterar a placa é preciso usar os métodos `get_placa()` e `set_placa()`. A mesma coisa acontece com `__cnh` na classe Motorista, com `get_cnh()` e `set_cnh()`.

**5. Por que a placa do veículo foi definida como privada?**

Porque a placa é um dado importante e não faz sentido qualquer parte do código conseguir alterá-la diretamente. Ao deixar privada e usar o método `set_placa()`, temos mais controle sobre isso. No futuro daria para colocar uma validação dentro do método antes de aceitar a mudança.

**6. Onde aparece o polimorfismo?**

No método `realizar_atividade()`. Todas as classes de veículo têm esse método, mas cada uma responde de um jeito diferente. Quando a gente faz um for em todos os veículos e chama `realizar_atividade()`, o Carro fala que é para deslocamento, o Caminhao fala que é para carga, a Moto para entregas e o Onibus para transporte de funcionários. Mesmo método, comportamentos diferentes dependendo do objeto.

**7. Qual é a responsabilidade da classe Frota?**

A Frota é quem gerencia tudo. Ela guarda as listas de veículos, motoristas, viagens e manutenções. Ela também tem os métodos para adicionar e listar cada coisa. Quando uma viagem é adicionada, ela já atualiza o km do veículo e registra a viagem no motorista automaticamente.

**8. Qual é a responsabilidade da classe Viagem?**

A Viagem guarda os dados de um deslocamento: qual motorista foi, qual veículo usou, de onde saiu, para onde foi, quantos km rodou e o status. Ela também tem o método `exibir_dados()` para mostrar essas informações.

**9. Qual é a responsabilidade da classe Manutencao?**

A Manutencao registra quando um veículo precisa de algum serviço. Ela guarda qual veículo é, o tipo do serviço, o custo e se está aberta ou fechada. Quando uma manutenção é adicionada na frota, o veículo automaticamente fica com status "Em manutenção".

**10. Como esse sistema poderia ser usado em uma empresa real?**

Em uma empresa real daria para conectar esse sistema a um banco de dados para salvar as informações entre execuções. Também daria para fazer uma interface web ou um aplicativo para os funcionários usarem pelo celular. Poderia ter alertas quando um veículo atingir muitos km e precisar de revisão, ou relatórios de gasto com manutenção por mês. A estrutura de classes que fizemos já facilita expandir o sistema com essas funcionalidades.

## Desafios implementados

1. Menu com `input()` para cadastrar motoristas e veículos — `main.py`
2. Total de viagens por motorista — `frota.py`, método `viagens_por_motorista()`
3. Custo total de manutenção — `frota.py`, método `custo_total_manutencao()`
4. Listar veículos disponíveis — `frota.py`, método `listar_veiculos_disponiveis()`
5. Impedir viagem com veículo em manutenção — `frota.py`, método `adicionar_viagem()`
6. Classe Onibus — `veiculo.py`
7. KM rodados por veículo — `frota.py`, método `relatorio_km_por_veiculo()`
8. Veículos com mais de 100.000 km — `frota.py`, método `veiculos_alta_quilometragem()`

## Onde usamos herança, encapsulamento e polimorfismo

**Herança:** Motorista herda de Pessoa. Carro, Caminhao, Moto e Onibus herdam de Veiculo.

**Encapsulamento:** atributo `__placa` em Veiculo e `__cnh` em Motorista, ambos com getters e setters.

**Polimorfismo:** método `realizar_atividade()` é sobrescrito em cada subclasse de Veiculo e também em Motorista, cada um com comportamento diferente.
