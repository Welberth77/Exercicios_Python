lanche = ("hambúrguer","suco","pizza","pudim")

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("EU comi pra caramba!")

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, item in enumerate(lanche):
    print(f'Eu vou comer {item} na posição {pos}')