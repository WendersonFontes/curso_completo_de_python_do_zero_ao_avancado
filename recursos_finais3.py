#Generators

valores = [1, 3, 5, 7, 9, 13, 15]

quadrados = (item**2 for item in valores)
print(quadrados)

for valor in quadrados:
    print(valor)