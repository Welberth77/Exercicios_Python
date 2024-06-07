def area(l, c):
    a = l * c
    print(f'A área do terreno {l}X{c} é {a}m2.')

print(' CONTROLE DE TERRENOS' )
print('-' * 25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)