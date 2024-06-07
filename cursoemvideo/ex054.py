#ano de nascimento de sete pessoas e dizer quantas são de maior e quantas são de menor
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range( 1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu: '.format(c)))
    if anoatual - ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Ao todo tivemos {} pessoas maiores de idade \nE tamém tivemos {} pessoas menores de idade'.format(maior, menor))