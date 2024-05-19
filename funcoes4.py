def div(k, j):
    if j != 0:
        return k /j
    else:
        return 'Impossível dividir por zero!'

if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}.')