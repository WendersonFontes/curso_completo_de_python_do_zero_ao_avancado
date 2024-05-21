try:
    a = open('frutas.dat', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    a.close()


#outra forma:
with open('frutas.dat', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end= '')