#ler sexo de uma pessoa mas so aceite M ou F como resposta
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#enquanto sexo não estiver entre M e F:
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))