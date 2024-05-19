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

# Exclusão de itens em dicionários
del elemento['período']
print(elemento)

elemento.clear() #limpa o dicionário
print(elemento)

del elemento
print(elemento) #não é possível imprimir nesse caso porque o dicionário foi excluido

