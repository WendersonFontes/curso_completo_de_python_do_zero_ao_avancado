#map(funcao, iteravel)
#o list converte o map em list, o num é o iteravel

num = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x*2, num)) #multiplicar cada item da lista
print(dobro)