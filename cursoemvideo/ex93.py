dados = dict()
lista_gols = list()
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for i in range(1,partidas + 1):
    gols = int(input(f'Quantos gols na partida {i} = '))
    lista_gols.append(gols)

dados['gols'] = lista_gols
dados['total de gols'] = sum(lista_gols)

print('-=' * 30)
print(dados)
print('-=' * 30)

for i, c in dados.items():
    print(f'O {i} do jogador é {c}')

print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for i, c in enumerate(lista_gols):
    print(f'    => Na partida {i+1} fez {c} gols')
print(f'O total de gols foi de {dados["total de gols"]}')