litros = float(input("Quantos litros você deseja abastecer? "))
combustivel = int(input("Qual o tipo de combustível? [1] Álcool, [2] Gasolina: "))

preco_alcool = 1.90
preco_gasolina = 2.50

if combustivel == 1:
    if litros <= 20:
        desconto = 0.03
        preco_total = litros * (preco_alcool - (preco_alcool * desconto))
        print("Valor total é R$:",preco_total)
    elif litros > 20:
        desconto = 0.05
        preco_total = litros * (preco_alcool - (preco_alcool * desconto))
        print("Valor total é R$:",preco_total)
elif combustivel == 2:
    if litros <= 20:
        desconto = 0.04
        preco_total = litros * (preco_gasolina - (preco_gasolina * desconto))
        print("Valor total é R$:",preco_total)
    elif litros > 20:
        desconto = 0.06
        preco_total = litros * (preco_gasolina - (preco_gasolina * desconto))
        print("Valor total é R$:",preco_total)
else:
    print("Opção inválida!")