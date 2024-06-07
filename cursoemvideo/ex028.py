# Sortear um número de 0 a 5 e deizer se o usuario acertou ou errou
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Digite um numero: ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[32mParabéns você acertou!\033[m ')
else:
    print('\033[31mVocê errou!\033[m eu pensei no número {} e não no número {}! '.format(computador, jogador))
print('---FIM---')