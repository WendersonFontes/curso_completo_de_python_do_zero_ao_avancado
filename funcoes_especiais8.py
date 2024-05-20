# função reduce()
# sintaxe:
# reduce(função, sequência, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,2,2,4,8,6]

total = reduce(mult, numeros) # 1 * 2 * 2 * 4 * 8 * 6 é isso o que representa
print(total)