var_global = "Curso Completo de Python"

def escreve_texto():
    global var_global #agora consegue acessar a variável externa e alterar ela, se não só altera dentro da função
    var_global = "Bancos de dados com SQL"
    var_local = "Fábio dos reis"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
