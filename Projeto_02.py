lista_codigo = []
lista_altura = []
lista_peso = []

while True:
  codigo = int(input("Digite seu código: ou [0] para sair: "))
  if codigo == 0:
    break
  altura = float(input("Digite sua altura: "))
  peso = float(input("Digite seu peso: "))

  lista_codigo.append(codigo)
  lista_altura.append(altura)
  lista_peso.append(peso)

#procurar a maior altura
maior_altura = 0
for max in range(len(lista_altura)):
   if maior_altura < lista_altura[max]:
     maior_altura = lista_altura[max]
     codigo_maior_altura = lista_codigo[max]

#Procurar a menor altura
menor_altura = maior_altura
for min in range(len(lista_altura)):
  if menor_altura > lista_altura[min]:
    menor_altura = lista_altura[min]
    codigo_menor_altura = lista_codigo[min]

#Procurar o maior peso
maior_peso = 0
for max in range(len(lista_peso)):
  if maior_peso < lista_peso[max]:
    maior_peso = lista_peso[max]
    codigo_maior_peso = lista_codigo[max]

#procurar o menor peso
menor_peso = maior_peso
for min in range(len(lista_peso)):
  if menor_peso > lista_peso[min]:
    menor_peso = lista_peso[min]
    codigo_menor_peso = lista_codigo[min]

#Calculando a média
media_alturas = sum(lista_altura) / len(lista_altura)
media_pesos = sum(lista_peso) / len(lista_peso)

print(f"o cliente de código {codigo_menor_altura} é o mais alto com {maior_altura}")
print(f"O cliente de código {codigo_menor_altura} é o mais baixo com {menor_altura}")
print(f"O cliente de código {codigo_maior_peso} é o mais gordo pesando {maior_peso}")
print(f"O cliente de código {codigo_menor_peso} é o mais magro pesando {menor_peso}")
print(f"A média de alturas é {media_alturas}")
print(f"A média de pesos é {media_pesos}")
