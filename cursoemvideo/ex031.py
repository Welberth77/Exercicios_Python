# Viagem menor de 200km é cobrado 0.50 por km e viagens maiores de 200km é cobrado 0.45 por km
n = float(input('Digite a distância da sua viagem? '))
if n <= 200:
    print('A sua viagem vai custar \033[32mR${:.2f}\033[m'.format(0.50 * n))
else:
    print('A sua viagem vai custar \033[32mR${:.2f}\033[m '.format(0.45 * n))