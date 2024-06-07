# Ano bissexto
from datetime import date    # para pegar a data do computador
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year   # Para pegar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[32mBISSEXTO!\033[m '.format(ano))
else:
    print('O ano {} NÃO é \033[31mBISSEXTO!\033[m '.format(ano))