# Ver quantas vezes aparece a letra A e onde começa e termina
frase = str(input('Digite sua frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {} '.format(frase.rfind('a')+1))