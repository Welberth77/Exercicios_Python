#Indice de massa corporal (IMC)
p = float(input('Digite seu peso? (Kg) '))
a = float(input('Digite sua altura? (m) '))
imc = p / (a ** 2)
print('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[1;33;40mABAIXO DO PESO\033[m ideal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no \033[1;32;40mPESO IDEAL!\033[m')
elif imc >= 25 and imc < 30:
    print('Você está em \033[1;33;40mSOBREPESO!\033[m')
elif imc >= 30 and imc < 40:
    print('Você está em \033[1;33;40mOBESIDADE!\033[m')
else:
    print('Você está em \033[1;31;40mOBESIDADE MÓRBIDA!\033[m')