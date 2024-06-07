def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos o voto é: ', end='')
    if idade >= 16 and idade < 18 or idade > 70:
        return 'OPCIONAL'
    elif idade >= 18:
        return 'OBRIGATÓRIO'
    else:
        return 'NEGADO' 
    
print('-=' * 30)
ano = int(input('Qual o seu ano de nascimento? '))
print(f'{voto(ano)}')