# Mostra o nome de quem tem o maior e menor peso na academia
dados = list()
lista = list()
maior = menor = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        elif lista[1] < menor:
            menor = lista[1]

    dados.append(lista[:])
    lista.clear()

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break

print(dados)
print(f'Foram cadastradas {len(dados)} pessoas no total')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')