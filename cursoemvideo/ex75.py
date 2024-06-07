numeros = (int(input("Digite o primeiro número: ")),
           int(input("Digite o segundo número: ")),
           int(input("Digite o terceiro número: ")),
           int(input("Digite o quarto número: ")))

print(f"Você digitou os valores {numeros}")
print(f"o número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O primeiro número 3 foi digitado na posição {numeros.index(3) + 1}")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")