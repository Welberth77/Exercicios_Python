palavras = ("aprender", "programar", "linguagem", "python", "welberth")

for i in palavras:
    print(f"\nNa palavra {i} temos ", end="")
    for letras in i:
        if letras.lower() in "aeiou":
            print(letras, end=", ")