a = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    n = int(input("Digite um número de 1 a 20: "))
    if n >= 0 and n <= 20:
        r = int(input("Você quer continuar ? [1] SIM, [2] NÃO "))
        if r == 2:
            break

print(f"Você digitou o número {a[n]}")