# def soma(a, b):
#     print(f'A: {a} + B: {b}')
#     s = a + b
#     print(f'{s}')

# soma(5, 4)

# def contador(*num):
#     print(num)

# contador(1, 5, 6, 5, 4)
# contador(2, 6, 8)
# contador(2, 1)

# def dobra(lst):
#     cont = 0
#     while cont < len(lst):
#         lst[cont] *= 2
#         cont += 1

# valores = [4, 6, 5, 8, 9, 1]
# dobra(valores)
# print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')

soma(2, 6, 5, 7, 2)