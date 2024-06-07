from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))