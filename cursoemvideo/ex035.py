# analizador de triangulos
print('-=-' * 20)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=-' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m triângulo! ')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo! ')
