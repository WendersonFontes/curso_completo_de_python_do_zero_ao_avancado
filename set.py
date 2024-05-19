#diferente dos dicionários, o set só tem os valores
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))
print('Ceres' in planeta_anao) #retorna True se tiver o termo no set
print('Lua' in planeta_anao) 
print('Lua' not in planeta_anao) 

for astro in planeta_anao:
    print(astro.upper(), end='') # o end='' faz com que eles fiquem lado a lado, pra ficar um em cada linha, masta remover o end
