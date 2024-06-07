#Dizer se é ou não um número primo
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 0:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')