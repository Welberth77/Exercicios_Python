# Foi adicionado mais um parametro, o formato, para saber se o usuario quer o número formatado ou não
# Essa edição foi feita no módulo moedas
import modulos.moedas

print('-=' * 30)
n = float(input('Digite o preço R$'))
print(f'A metade de {modulos.moedas.moeda(n)} é {modulos.moedas.metade(n, True)}')
print(f'O dobro de {modulos.moedas.moeda(n)} é {modulos.moedas.dobro(n, True)}')
print(f'Aumentando 10% de {modulos.moedas.moeda(n)} é {modulos.moedas.aumentar(n, 10, True)}')
print(f'Diminuindo 13% de {modulos.moedas.moeda(n)} é {modulos.moedas.diminuir(n, 13, True)}')
print('-=' * 30)