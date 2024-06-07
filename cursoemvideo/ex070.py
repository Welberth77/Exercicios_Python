print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
soma = mais100 = maisbarato = menor = cont = 0
barato = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço? R$:'))
    cont += 1
    soma += preço
    if preço > 1000:
        mais100 += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R$:{soma:.2f}')
print(f'temos {mais100} produtos custando maiss de R$:1.000,00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')