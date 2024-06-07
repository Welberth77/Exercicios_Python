#melhorar o jogo do exercicio 028
from random import randint
computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi ? ')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez! ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez! ')
print('Acertou! Com {} tentativas. Parabéns! '.format(tentativa))