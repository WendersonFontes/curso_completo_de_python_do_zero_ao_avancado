import mod_func as mf

#controlar o fluxo de execução do código, verifica se uma variável especial 
#interna do python chamada __name__ é igual a ese valo __main__
#se for o bloco de código abaixo é executado
#pra que serve isso, o name é uma variável que tem o nome do módulo atual
# quando esse módulo ele é rodado como se fosse o programa principal o valor de name é definido como main
#quando o módulo é importando, o valor do nome é dfeinido com o valor do módulo
#é pra evitar que partes do código seja executada quando importamos o código antes da hora
#somente quando for executado o programa principal, é uma convenção util no python
if __name__ == '__main__':  
    mf.mensagem()
    num =int(input('Digite um número inteiro positivo: '))

    print(f'\nCalcular Fatorial do número: ')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')


    print(f'\nCalcular sequência de fibonacci: ')
    fib = mf.fibo(num)
    print(f'a sequência de fibonacci é {fib}')