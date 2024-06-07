n = float(input('Digite seu salário atual: R$'))
#a = n * 0.15
#sa = n + a
a = n + (n * 15 / 100)
print('Seu salário com um aumento de 15% ficará R${:.2f}'.format(a))