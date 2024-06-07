#Refazer o desafio 051, mostrando os 10 primeiros termos da progressão usando while
print('Gerador de PA ')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} => '.format(termo), end= '')
    termo += razão
    cont += 1
print('FIM')
