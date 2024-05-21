try: # com o trye except se abrir um arquivo inexistente ele já informa "não foi possível abrir.." e não mostra o erro
    manipulador = open('C:\\Users\\engen\\Documents\\arquivo2.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip() # tira a quebra de linha
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()
    