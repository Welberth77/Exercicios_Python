'''programa lê o nome e duas notas de vários alunos e guarda tudo em uma lista composta. 
No final, mostra um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

dados = [[], [], []]

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    dados[0].append(nome)
    if nota1 >= 0 and nota1 <= 10:
        dados[1].append(nota1)
    if nota2 >= 0 and nota2 <= 10:
        dados[2].append(nota2)
    
    resposta = input('Quer continuar? [S/N]: ').upper()[0]
    if resposta in 'Nn':
        break

print('=-' * 40)
print(f'{"N°":<4}{"NOME":<15}{"MÉDIA":>6} ')
print('-' * 25)
for i in range(0, len(dados[0])):
    print(f'{i+1:<4}{dados[0][i]:<15}{(dados[1][i] + dados[2][i]) / 2 :>6}')

while True:    
    verificar_aluno = int(input('Verificar nota de qual aluno? [999 Interoompe]: '))
    if verificar_aluno == 999:
        break
    if verificar_aluno-1 >= len(dados) or verificar_aluno == 0:
        print(f'O aluno de código {verificar_aluno} não está no banco de dados')
    else:
        print(f'As notas de {dados[0][verificar_aluno-1]} são {dados[1][verificar_aluno-1]} e {dados[2][verificar_aluno-1]}')
        if (dados[1][verificar_aluno-1] + dados[2][verificar_aluno-1]) / 2 >= 6:
            print('O aluno está aprovado')
        else:
            print('O aluno está em recuperação!')