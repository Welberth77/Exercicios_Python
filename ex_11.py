from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(f'{i}, ', end='', flush=True)
        print('Fim!')
    elif inicio > fim:
        if passo < 0:
            passo = passo * -1
        for i in range(inicio, fim - 1, -passo):
            sleep(0.5)
            print(f'{i}, ', end='', flush=True)
        print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
