# Ex 107
# No ex109 foi adicionado o formato para saber se o usuario quer o número formatado ou não
def metade(num = 0, formato=False):
    res = num / 2
    return res if formato == False else moeda(res)

def dobro(num = 0, formato=False):
    res = num * 2
    return res if formato == False else moeda(res)

def aumentar(num = 0, porc = 0, formato=False):
    res = num + (num * porc/100)
    return res if formato == False else moeda(res)

def diminuir(num = 0, porc = 0, formato=False):
    res = num - (num * porc/100)
    return res if formato == False else moeda(res)

# Ex 108
def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

# Ex110
def resumo(num=0, aum=10, dim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aum}% de aumento: \t{aumentar(num, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(num, dim, True)}')
    print('-' * 30)