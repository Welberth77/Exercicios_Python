listagem = ("Lápis", 1.75,
            "Borracha", 2.0,
            "Caderno", 15.90,
            "estojo", 25,
            "Trasferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "livro", 34.90)

print("-" * 40)
print(f'{"Listagem de preços":^40}')
print("-" * 40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<30}", end="")
    else: 
        print(f"R${listagem[i]:>7.2f}")
print("-" * 40)