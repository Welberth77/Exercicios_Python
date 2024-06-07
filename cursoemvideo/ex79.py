lista = []

while True:
    n = int(input('Digite o valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
    resposta = input('Quer continuar ? [s/n]: ')
    if resposta in 'Nn':
        break

lista.sort()
print(f'Você digitou os valores {lista}')