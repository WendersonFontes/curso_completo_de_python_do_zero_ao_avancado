from functools import reduce
#soma cumulaiva dos quadrados de valores, usando expressão lambda

def somapot(x, y):
    return (x**2 + y**2)

numeros = [1,2,3,4]
#((1²+2²)² + 3²)² + 4²

total = reduce(somapot, numeros) 
print(total)
