n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))



try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f'Não é possível dividir por zero!')
else:
    print(f'Resultado: {r}')
