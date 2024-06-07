# Ajuda interativa
# help()

# Ajuda interativa para a sua função
def contador(inicio, fim, passo):
    # Manual da sua função
    """
    -> Faz uma contagem e mostra na tela
    :param inicio: inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    """
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i}, ', end='')
        print('Fim!')
    elif inicio > fim:
        if passo < 0:
            passo = passo * -1
        for i in range(inicio, fim - 1, -passo):
            print(f'{i}, ', end='')
        print('Fim!')

help(contador)

# Parâmetros opcionais
# É adicionado o (=0) nos parâmetros para não dar erro caso o usuário digite menos parâmetros
def somar(a=0 ,b=0 ,c=0 ):
    """
    -> FAz a soma de 3 números e mostra
    :param a: recebe o 1 valor
    :param b: recebe o 2 valor
    :param c: recebe o 3 valor
    """
    s = a + b + c
    print(f'A soma dos valores é {s}')

somar(1,1)