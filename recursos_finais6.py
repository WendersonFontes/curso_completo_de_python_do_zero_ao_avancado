temperaturas = [-1, 10, 5, -2, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativam, com {t} Celcius.')