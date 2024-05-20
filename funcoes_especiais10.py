from functools import reduce
#soma cumulaiva dos quadrados de valores, usando expressão lambda

numeros = [1,2,3,4]
#((1²+2²)² + 3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numeros) 
print(total)