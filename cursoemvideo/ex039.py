#Alistamento
from datetime import date
print('''Qual o seu sexo ?
[ 1 ] MASCULINO
[ 2 ] FEMININO ''')
sexo = int(input('Digite sua opção: '))
if sexo == 1:
    ano = int(input('Digite seu ano de nascimeno: '))
    atual = date.today().year
    idade = atual - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        anos = atual + saldo
        print('Seu alistamento foi em {}'.format(anos))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos'.format(saldo))
        anos = atual - saldo
        print('Seu alistamento foi em {}'.format(anos))
else:
    print('Você não precisa se alistar, obrigado')