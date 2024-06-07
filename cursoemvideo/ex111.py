# Nesse ex foi utilizado o pacote (utilidadescev) contendo o pacote (moeda) e o pacote (dado)
from utilidadescev import moeda

p = float(input('Digite um número: '))
moeda.resumo(p, 80, 20)