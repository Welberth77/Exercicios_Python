#melhorar exercicio 009
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))