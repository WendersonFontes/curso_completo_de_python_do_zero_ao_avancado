#append em arquivos de texto

try: 
    manipulador = open('arquivo.txt', 'a', encoding='utf-8') #muda para o 'a' para o append
    manipulador.write('\nPython é muito empregado em IA')
    manipulador.write('\nInteligência Artificial veio para ficar!')
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()