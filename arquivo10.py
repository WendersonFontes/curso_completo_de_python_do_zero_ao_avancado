frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

try: 
    manipulador = open('frutas.txt', 'w', encoding='utf-8') 
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Ler o arquivo criado

try:
    manipulador = open('frutas.txt', 'r', encoding='utf-8') 
    print(manipulador.read())
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()