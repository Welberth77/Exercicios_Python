jogador = dict()
time = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for i in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partidas {i+1} = ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end=' ')
    print()
print('-' * 40)

while True:
    busca =  int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca-1 >= len(time) or busca-1 == -1:
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'-- Levantamento do jogador {time[busca-1]["nome"]}: ')
        for i, g in enumerate(time[busca-1]['gols']):
            print(f' Na partida {i+1} fez {g} gols. ')
    print('-' * 40)
print('<< ENCERRADO >>')