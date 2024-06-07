def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: (opcional) para mostrar ou não a conta
    :return: retorna o fatorial de n
    """
    print('=-' * 20)
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

help(fatorial)
print(fatorial(5, show=True))
print(fatorial(6, True))