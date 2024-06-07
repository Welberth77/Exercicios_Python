n = float(input('Qual é p preço do produto? R$'))
d = n * 0.05
# também é possivel calcular a porcentagem com (preço * 5 / 100)
vf = n - d
print('O valor com 5% de desconto ficará {:.2f}'.format(vf))