#Impotar data atual do aparelho
from datetime import date
atual = date.today().year
#ler ano
ano = int(input('Qual o ano do seu nascimento? '))
idade = atual - ano
if idade <= 9:
    print('Você é da categoria MIRIM!')
elif idade >= 10 and idade <= 14:
    print('Você é da categoria INFANTIL!')
elif idade >= 15 and idade <= 19:
    print('Você está na categoria JUNIOR!')
elif idade >= 20 and idade <= 25:
    print('Você está na categoria SÊNIOR!')
else:
    print('Você está na categoria MASTER!')