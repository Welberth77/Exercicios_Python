import modulos.moedas

print('-=' * 30)
n = float(input('Digite o preço R$'))
print(f'A metade de R${n} é R${modulos.moedas.metade(n)}')
print(f'O dobro de R${n} é R${modulos.moedas.dobro(n)}')
print(f'Aumentando 10% de {n} é R${modulos.moedas.aumentar(n, 10)}')
print(f'Diminuindo 13% de {n} é R${modulos.moedas.diminuir(n, 13)}')
print('-=' * 30)