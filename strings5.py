email = input('Digite seu endereço de e-mail: ')
arroba = email.find('@')  #me diz em qual posição está o elemento solicitado
print(arroba)


usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)