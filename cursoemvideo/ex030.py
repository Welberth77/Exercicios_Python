# Dizer se o número é par ou ímpar
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if numero == 0:
    print('O número {} é \033[34mPAR!\033[m '.format(numero))
else:
    print('O número {} é \033[34mÍMPAR!\033[m '.format(numero))