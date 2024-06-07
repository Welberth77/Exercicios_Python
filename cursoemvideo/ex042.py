#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓRCELES')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo! ')