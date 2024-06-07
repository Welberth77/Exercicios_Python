times = ("Botafogo", "Palmeiras", "Grêmio", "Flamengo", 
        "Bragantino", "Fluminense", "Athletico-PR", "Fortaleza", 
        "Atlético-MG", "Cuiabá", "Cruzeiro", "internacional", 
        "São Paulo", "corinthians", "Bahia", "Goiás", 
        "Santos", "Vasco", "América-MG", "Coritiba")

print("=" *50)
print(f"lista de times {times}")
print("=" *50)

print(f"Os 5 primeiros times são {times[:5]}")
print("=" *50)

print(f"Os 4 últimos times são {times[16:]}")
print("=" *50)

print(f"Times em ordem alfabetica: {sorted(times)}")
print("=" *50)

print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
print("=" *50)