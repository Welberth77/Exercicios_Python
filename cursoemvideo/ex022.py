nome = str(input('digite seu nome completo: ')).strip()
# deixar texto maiusculo e minusculo
print('Analizando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# contar quantas letras tem o nome completo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# contar quantas letras tem apenas o primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
