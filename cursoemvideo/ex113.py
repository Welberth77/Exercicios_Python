def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou o valor!\033[m')    
            return 0
        else:
            return n
            

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou o valor!\033[m')  
            return 0
        else:
            return n


i = leiaInt('Digite um número: ')
r = leiaFloat('Digite um número float: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')