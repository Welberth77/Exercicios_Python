matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor para [{i}], [{c}] '))

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end='')
        if matriz [i][c] % 2 == 0:
            soma_par = soma_par + matriz[i][c]
    print()

print(f'A soma dos valores pares é {soma_par}')

for i in range(0, 3):
    soma_coluna = soma_coluna + matriz[i][2]

print(f'A soma dos valores da terceira coluna é {soma_coluna}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior número da segunda linha é {maior}')