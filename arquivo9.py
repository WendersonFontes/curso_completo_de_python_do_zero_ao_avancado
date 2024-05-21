texto = '\nPython é u sado em Ciência de Dados extensivamente'

try: 
    manipulador = open('arquivo.txt', 'a', encoding='utf-8') #muda para o 'a' para o append
    manipulador.write(texto)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()