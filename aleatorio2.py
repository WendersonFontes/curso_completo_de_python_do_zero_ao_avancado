import random

print('Gerar cinco números aleatórios entre 1 e 50: \n')

for i in range(5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')