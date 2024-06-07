mais = homem = mulher20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()[0]
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if idade > 18:
        mais += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mulher20 += 1
    if resp == 'N':
        break
print(f'{mais} pessoas tem mais de 18 anos')
print(f'Temos {homem} pessoas do sexo masculino')
print(f'Temos {mulher20} mulheres com menos de 20 anos')