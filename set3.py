astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'cometa de Halley'}
print(astros1 == astros2) #verifica se é igual e retorna True  ou False
print(astros1 != astros2) #verifica se é diferente e retorna True  ou False

print(astros1 | astros2) #união de conjuntos
print(astros1.union(astros2)) #união de conjuntos também

print(astros1 & astros2) #intersecção de conjuntos
print(astros1.intersection(astros2)) #intersecção de conjuntos também

print(astros1 ^ astros2) # diferença simétrica de a pra b e b pra a entre os conjuntos
print(astros1.symmetric_difference(astros2)) # diferença simétrica de a pra b e b pra a entre os conjuntos

