teste = list()
teste.append('Wel')
teste.append(18)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)