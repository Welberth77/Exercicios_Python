# Mostra os valores pares e ímpares de uma lista digitada pelo usuário
lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

lista_par = []
lista_impar = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {lista_par}')
print(f'Os valores ímpares digitados foram {lista_impar}')