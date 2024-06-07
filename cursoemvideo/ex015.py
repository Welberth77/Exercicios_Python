d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodados? '))
total = (d * 60) + (km * 0.15)
print('Você tera que pagar o valor de R${:.2f}'.format(total))