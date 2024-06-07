import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.erro.URLError:
    print('O site pudim não está acessivel no momento!')
else:
    print('Site acessado com sucesso!')