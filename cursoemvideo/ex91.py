from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

ranking = list()

print('Valores Sorteados')
for i, c in jogo.items():
    sleep(1)
    print(f'{i} sorteou {c}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' RANKING DOS JOGADORES ')

for i, c in enumerate(ranking):
    print(f'{i+1}° lugar: {c[0]} com {c[1]}')
    sleep(1)