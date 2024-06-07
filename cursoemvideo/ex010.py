n = float(input('Quanto de dinheiro você têm: R$'))
d = n / 5.285
e = n / 6.371
print('com R${:.2f} reais você pode comprar US${:.2f} dolares e {:.2f} euros'.format(n, d, e))