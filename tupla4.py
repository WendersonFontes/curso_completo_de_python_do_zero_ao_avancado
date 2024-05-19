#criar uma lista a partir de uma tupla
halogenios = ('F', 'cl', 'Br', 'I', 'At')
gases_nomes= ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nomes

grupo17= list(halogenios) #por estar criando uma lista, conseguimos fazer alterações

grupo17[0] = 'H'
print(grupo17) 