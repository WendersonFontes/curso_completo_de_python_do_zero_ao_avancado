halogenios = ('F', 'cl', 'Br', 'I', 'At')
gases_nomes= ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nomes
t1 = (5, 2, 6, 8, 4, 5, 6, 4, 4, 0, 12, 22, 3, 4, 5)
print(halogenios)
print(halogenios[3])
print(halogenios[-1])
print(halogenios[0:2])
print(halogenios[:3])
print(halogenios[-2:])
print(len(halogenios))
print('Cl' in halogenios) # retorna True se verdade


print(elementos)

print(sum(t1))
print(min(t1))
print(max(t1))
print(t1.count(5)) # quantas vezes aparece o número 5

# .sort(), .append(), .reverse(), .pop() não da pra usar em tupla


