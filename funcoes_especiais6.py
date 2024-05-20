#Função filter()
# Sintaxe:
# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_par = list(filter(numeros_pares, numeros)) #converter para lista com list
print(num_par)

