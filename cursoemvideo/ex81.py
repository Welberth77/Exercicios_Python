lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = input('Quer continuar? [S/N]: ')
    if r in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista de forma decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')