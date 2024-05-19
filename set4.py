astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'cometa de Halley'}

#adicionar elementos a um conjunto

astros1.add('Urano')
astros1.add('Sol')
print(astros1)


#remover elementos a um conjunto

astros1.remove('Io')
print(astros1)

astros1.discard('Saturno') #remover elementos a um conjunto, diferente do remove, nesse se o elemento não estiver no conjunto ele não mostra erro na saída do terminal
print(astros1)


astros1.pop() #remover elementos arbitrário, você não sabe qual ele removeu, pode aproveitar isso em jogos por exemplo
print(astros1)


astros1.clear() #limpa tudo