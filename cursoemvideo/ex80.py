lista = []

for i in range(0, 5):
    n = int(input(f'Digite o {i+1}° número: '))
    lista.append(n)

lista.sort()
print(f'Os valores digitados em ordem foram {lista}')