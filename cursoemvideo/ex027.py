# Mostrar qual é o primeiro e último nome de uma pessoa
n = str(input('Qual é o seu nome ? ')).strip()
nome = n.split()
print('Prazer em te conhecer! ')
print('primeiro nome é {} '.format(nome[0]))
print('Seu último nome é {} '.format(nome[len(nome)-1]))