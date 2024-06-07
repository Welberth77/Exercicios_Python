#Ler notas
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {} e {} a média do aluno foi {}'.format(n1, n2, m))
if m < 5:
    print('Você está \033[0;30;41mREPROVADO!!\033[m estude mais!')
elif m >= 5 and m < 6.9:
    print('Você está de \033[0;30;43mRECUPERAÇÃO!!\033[m')
elif m >= 7:
    print('Parabéns você está \033[0;30;42mAPROVADO!!!\033[m')
