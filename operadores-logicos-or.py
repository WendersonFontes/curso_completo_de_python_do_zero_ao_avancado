porta = 'a'
janela = 'a'

alarme = (porta == 'a') or (janela== 'a')
msg = 'Alarm disparado?' + str(alarme)
print(msg)