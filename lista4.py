n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]
valores = n1 + n2

valores[0] = 9
print(valores[0])

print(valores)

print(valores[0:2]) # imprimir 2 valores a partir da posição zero

print(valores[:4]) # imprimir os 4 primeiros itens

print(valores[3:3]) # imprimir vazio

print(valores[-2:]) # imprimir a partir do penúltimo até o final da minha lista

print(len(valores)) # conta os elementos da lista

print(sorted(valores)) # imprimir versão ordenada da lista

print(sorted(valores, reverse=True)) # imprimir versão ordenada inversa da lista

print(sum(valores)) # imprimir soma dos elementos da lista

print(min(valores)) # imprimir elemento mínimo

print(max(valores)) # imprimir elemento máximo