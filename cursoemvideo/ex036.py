#valor da casa
casa = float(input('Qual é o valor da casa R$'))
#Salario
salario = float(input('Qual é o seu salario R$ '))
#quantos anos
anos = int(input('Quantos anos você deseja pagar? '))
prestação = casa / (anos * 12)
#30% do salario
minimo = (30 / 100) * salario
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de {:.2f} '.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')