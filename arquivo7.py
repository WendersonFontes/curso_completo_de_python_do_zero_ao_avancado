#escrever em arquivos de texto

try: # com o try e except se abrir um arquivo inexistente ele já informa "não foi possível abrir.." e não mostra o erro
    manipulador = open('arquivo.txt', 'w', encoding='utf-8')
    manipulador.write('Bóson Treinamentos\n')
    manipulador.write('Como criar um arquivo de texto com Python')
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()