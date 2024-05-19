frase = 'Vamos aprender Python hoje'
palavras = frase.split()
print(palavras)

print('A palavra de posição n 1 é: ')
print(palavras[1])


x = int(input('Escolha a posição da palavra que você deseja  de 0 a 3: '))

print(f'A palavra de posição número {x} é:')
print(palavras[x])

print('Abaixo está a sequência de palavras: ')
for palavra in palavras:
    print(palavra)


for letra in frase:
    print(letra)