from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analisando valores...')
    maior = 0
    for i, c in enumerate(num): 
        if c > maior:
            maior = c
        sleep(0.5)
        print(f'{c}, ', end='', flush=True)

    print(f'Foram informados {i+1} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2, 6, 4, 3, 8, 1)
maior(4, 2, 3, 1)
    