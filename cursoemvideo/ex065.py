#Ler varios números, calcular a média e qual foi o maior e o menor número lido, o programa deve perguntar ao usuario se ele quer ou não contnuar
resposta = 'S'
soma = quantidade = média = maior = menor = 0
while resposta in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quantidade += 1
    if quantidade == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resposta = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
média = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, média))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))
