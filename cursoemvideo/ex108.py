# Formatando os valores para reais
import modulos.moedas

print('-=' * 30)
n = float(input('Digite o preço R$'))
print(f'A metade de {modulos.moedas.moeda(n)} é {modulos.moedas.moeda(modulos.moedas.metade(n))}')
print(f'O dobro de {modulos.moedas.moeda(n)} é {modulos.moedas.moeda(modulos.moedas.dobro(n))}')
print(f'Aumentando 10% de {modulos.moedas.moeda(n)} é {modulos.moedas.moeda(modulos.moedas.aumentar(n, 10))}')
print(f'Diminuindo 13% de {modulos.moedas.moeda(n)} é {modulos.moedas.moeda(modulos.moedas.diminuir(n, 13))}')
print('-=' * 30)