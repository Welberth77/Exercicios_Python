#Ler dois valores e mostrar um menu na tela
from time import sleep
n1 = int(input('Digite o 1 valor: '))
n2 = int(input('Digite o 2 valor: '))
opção = 0
while opção != 5:
    print('='*30)
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR 
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qual a sua opção ? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {} '.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} e {} é igual a {} '.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            print('O maior valor entre {} e {} é {}'.format(n1, n2, n1))
        if n2 > n1:
            print('O maior valor entre {} e {} é {}'.format(n1, n2, n2))
        if n1 == n2:
            print('Os dois números são iguais')
    elif opção == 4:
        n1 = int(input('Qual será o novo 1 número? '))
        n2 = int(input('Qual será o novo 2 número? '))
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim')