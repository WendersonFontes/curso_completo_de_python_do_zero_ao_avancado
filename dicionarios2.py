elemento = {
    'Z': 3,
    'nome':'Lítio',
    'grupo': 'Metais alcalinos',
    'densidade': 0.534,
}
#não pode utilizar listas como chaves de um dicionário pois são mutáveis.

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')

print(f'O dicionário possui {len(elemento)} elementos.')

#atualizar a entrada do dicionário
elemento ['grupo'] = 'Alcalinos'

print(elemento)

# Adicionar uma entrada
elemento['período'] = 1 #esse 1 no caso depois da igualdade é o valor da chave
print(elemento)


print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')