#Jogar Par ou ímpar e so terminar o programa quando o usuário perder
from random import randint
v = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')