var1 = 12
var2 = 31

#operador condicional ternário

menor = var1 if var1 < var2 else var2 #na prática é melhor usar da outra forma que o código fica legível
print(f'Menor valor: {menor}')
print(f'Menor valor: {(var2, var1)[var1 < var2]}')