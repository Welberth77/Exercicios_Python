# Salario
salario = float(input('Qual é o seu salário do funcionário? R$'))
if salario <= 1250:
   novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava \033[33mR${:.2f}\033[m passa a ganhar \033[32mR${:.2f}\033[m agora.'.format(salario, novo))
