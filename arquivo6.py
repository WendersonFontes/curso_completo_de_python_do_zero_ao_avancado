texto = input('Qual termo deseja procurar no arquivo?')

try: # com o try e except se abrir um arquivo inexistente ele já informa "não foi possível abrir.." e não mostra o erro
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip() # tira a quebra de linha
        if texto in linha:
              print(f'A string foi encontrada!')
              print(linha)
        else:
            print(f'String não encontrada')
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()