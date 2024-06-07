#Contagem regressiva para fogos de artifico
from time import sleep
print('Os fogos de artifício serão lançados em:')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOW!')