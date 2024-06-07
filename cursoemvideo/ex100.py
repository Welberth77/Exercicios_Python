from random import randint

numeros = []
def sorteio(numeros):
    for i in range(0, 5):
        numeros.append(randint(1, 10))
        i += 1
    print(f'Sorteando 5 valores da lista {numeros}')

def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma = soma + i
    print(f'A soma dos valores pares é {soma}')

sorteio(numeros)
somaPar(numeros)