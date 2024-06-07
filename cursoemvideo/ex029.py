# se o carro ultrapassar 80km/h ele é multado por 7 reais a cada km
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mVocê foi multado!\033[m Você execeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('A sua multa vai ser de {:.2f}'.format(multa))
print('Tenha um bom dia! dirija com segurança. ')