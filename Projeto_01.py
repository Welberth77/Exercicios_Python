# Informações do prédio
class Predio:
    def __init__(self, nome, preço_compra, preço_aluguel):
        self.nome = nome
        self.preço_compra = preço_compra
        self.preço_aluguel = preço_aluguel

# Calcular custo do apartamento - COMPRA
def calcular_custo_compra(loc):
    custo_total = 0
    if loc == 1:
        print('Você escolheu o apartamento na região: Praia')
        preço_predio = Predio("Prédio 1", 200000, 0)
        custos_comodos = {"quarto": 7000, "banheiro": 3000, "sala": 10000, "cozinha": 10000}
    elif loc == 2:
        print('Você escolheu o apartamento na região: Centro')
        preço_predio = Predio("Prédio 2", 100000, 0)
        custos_comodos = {"quarto": 3500, "banheiro": 1500, "sala": 5000, "cozinha": 5000}
    elif loc == 3:
        print('Você escolheu o apartamento na região: Interior')
        preço_predio = Predio("Prédio 3", 70000, 0)
        custos_comodos = {"quarto": 2000, "banheiro": 750, "sala": 3000, "cozinha": 3000}
    elif loc == 4:
        print('Você escolheu o apartamento na região: Praia e centro')
        preço_predio = Predio("Prédio 4", 150000, 0)
        custos_comodos = {"quarto": 5200, "banheiro": 2200, "sala": 7500, "cozinha": 7500}

    custo_total = preço_predio.preço_compra
    for comodo, custo in custos_comodos.items():
        custo_total += custo

    return custo_total

# Calculando preço do apartamento - ALUGUEL
def calcular_custo_aluguel(loc):
    custo_total = 0
    if loc == 1:
         print('Você escolheu o apartamento na região: Praia')
         preço_predio = Predio('Predio 1', 0, 2500 )
         custos_comodos = {"quarto": 300, "banheiro": 200, "sala": 500, "cozinha": 300}
    elif loc == 2:
        print('Você escolheu o apartamento na região: Centro')
        preço_predio = Predio("Prédio 2", 0, 2000)
        custos_comodos = {"quarto": 250, "banheiro": 150, "sala": 400, "cozinha": 250}
    elif loc == 3:
        print('Você escolheu o apartamento na região: Interior')
        preço_predio = Predio("Prédio 3", 0, 1000)
        custos_comodos = {"quarto": 150, "banheiro": 75, "sala": 250, "cozinha": 150}
    elif loc == 4:
        print('Você escolheu o apartamento na região: Praia e Centro')
        preço_predio = Predio("Prédio 4", 0, 1000)
        custos_comodos = {"quarto": 350, "banheiro": 250, "sala": 550, "cozinha": 350}

    custo_total = preço_predio.preço_aluguel
    for comodo, custo in custos_comodos.items():
        custo_total += custo

    return custo_total

# Informações do comprador
class Comprador:
    def __init__(self, cpf, data_nascimento, rg, nome, telefone):
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.nome = nome
        self.telefone = telefone
        self.requisitos = {}

dados_cliente = dict()
lista_clientes = list()

while True:
  # Mostrando opções ao usuário
  # Mostra os 'Requisitos' na cor verde
    print('\033[0;49;34m==' * 8, 'BEM-VINDO A WIRP', '==' * 8, '\033[m', end='')
    # Retorna a cor ao padrão
    print('\033[0;0m ')

    print('Vamos começar o seu cadastro')
    print('Para começarmos escolha a localização desejada para o seu apartamento!')
    print('''ESCOLHA A LOCALIZAÇÃO:
    [1] PRAIA
    [2] CENTRO
    [3] INTERIOR
    [4] PRAIA E CENTRO''')

    # Pedindo a localização ao usuário e validando valores
    while True:
        loc = int(input('Escolha entre (1 e 4): '))
        if loc > 4 or loc < 1:
            print('Erro!, a opção deve estar entre (1 e 4)')
        else:
            break

    # Mostra o 'Cadastro' na cor verde
    print('\033[0;49;92m-=' * 6, 'CADASTRO', '-=' * 6, '\033[m', end='')
    # Retorna a cor ao padrão
    print('\033[0;0m ')

    # Cadastro do cliente
    dados_cliente = {}
    dados_cliente['Nome'] = str(input('Nome: '))
    dados_cliente['CPF'] = str(input('CPF: '))
    dados_cliente['Data de nascimento'] = str(input('Data de nascimento: '))
    dados_cliente['RG'] = str(input('RG: '))
    dados_cliente['Telefone'] = str(input('Telefone: '))

  # Armazenando valores
    comprador1 = Comprador(dados_cliente['CPF'], dados_cliente['Data de nascimento'], dados_cliente['RG'], dados_cliente['Nome'], dados_cliente['Telefone'])

    # Mostra os 'Requisitos' na cor verde
    print('\033[0;49;92m-=' * 6, 'REQUISITOS', '-=' * 6, '\033[m', end='')
    # Retorna a cor ao padrão
    print('\033[0;0m ')

    while True:
        escolha = int(input('Você pretende COMPRAR [1] ou morar de ALUGUEL [2]: '))
        if escolha == 1 or escolha == 2:
            break
        print('Erro!, a opção deve ser 1 ou 2')

    # Pede os requisitos do apartamento ao usuário
    print('O máximo de cômodos por apartamento deve ser 8')
    while True:
        quarto = int(input('Quantos quartos: '))
        sala = int(input('Quantas salas: '))
        banheiro = int(input('Quantos banheiros: '))
        cozinha = int(input('Quantas cozinhas: '))

        # Maximo de 6 cômodos por apartamento
        # A Soma de todos os requisitos tem que ser igual ou menor que 8
        total_requisitos = quarto + sala + banheiro + cozinha
        if total_requisitos > 8:
            print('O máximo de cômodos por apartamento deve ser 8. Por favor, ajuste os requisitos.')
        else:
            break

    # Armazenando valores
    dados_cliente['requisitos'] = {'quarto': quarto, 'sala': sala, 'banheiro': banheiro, 'cozinha': cozinha}

    # Preço de venda e aluguel diferentes
    if escolha == 1:
        custo_total = calcular_custo_compra(loc)
    elif escolha == 2:
        custo_total = calcular_custo_aluguel(loc)
    print(f'O custo total do apartamento é R$ {custo_total:.2f}')

    # Armazenando valores
    dados_cliente['custo_apartamento'] = custo_total
    lista_clientes.append(dados_cliente.copy())

    # Verifica se quer cadastrar mais algum cliente
    # Mostra linha na cor verde
    print('\033[0;49;92m-=' * 30, '\033[m', end='')
    # Retorna a cor ao padrão
    print('\033[0;0m ')

    resp = str(input('Deseja cadastrar mais algum cliente? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
    while resp.upper() != 'S':
        print('Valor inválido!')
        resp = str(input('Deseja cadastrar mais algum cliente? [S/N] '))

print(f'Ao todo temos {len(lista_clientes)} clientes cadastrados.')

print('Códigos dos clientes cadastrados:')
for k, v in enumerate(lista_clientes):
    print(f'{k + 1}: {v["Nome"]}')

# Se o usuário quiser mais detalhes, pode escolher um código específico
while True:
    detalhes_cliente = int(input('Digite o código do cliente para obter mais detalhes ou digite [0] para sair: '))

    if detalhes_cliente == 0:
        break
    elif detalhes_cliente > len(lista_clientes):
        print('Erro! Digite um código válido')
    else:
        detalhes_cliente = int(detalhes_cliente)
        cliente_selecionado = lista_clientes[detalhes_cliente - 1]

        print('-=' * 6, f'Detalhes do Cliente {detalhes_cliente}', '-=-' * 6)
        print(f'Nome: {cliente_selecionado["Nome"]}')
        print(f'CPF: {cliente_selecionado["CPF"]}')
        print(f'Data de nascimento: {cliente_selecionado["Data de nascimento"]}')
        print(f'RG: {cliente_selecionado["RG"]}')
        print(f'Telefone: {cliente_selecionado["Telefone"]}')
        print(f'Custo do apartamento: R$ {cliente_selecionado["custo_apartamento"]:.2f}')
        print()
