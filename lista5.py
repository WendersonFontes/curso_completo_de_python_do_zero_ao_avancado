n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]
valores = n1 + n2

valores[0] = 9

valores.append(13) # adiciona um elemento na lista

valores.append(14) # adiciona um elemento na lista

valores.pop() # o 14 foi eliminado (último item atual da lista)

valores.pop(3) # elimina o item da posição 3 - contando 0...1...2...3

valores.insert(5, 21) # o 21 foi adicionado na posição 5 e empurrou todos da frente

print(valores)

print(12 in valores) # esse valor existe dentro da lista?  - essa é a pergunta do código, retorna True se verdade

print(17 in valores) # esse valor existe dentro da lista?  - essa é a pergunta do código, retorna True se verdade, pode trabalhar com texto também