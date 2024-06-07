lista = []
maior = 0
menor = 0

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]

print(f'Os valores digitados foram {lista}')
print(f'O maior valor da lista foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor da lista foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()