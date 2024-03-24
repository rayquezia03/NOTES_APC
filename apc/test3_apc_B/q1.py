def autenticate(email,senha):
    usuarios = {'ana@gmail.com':['Ana', 'ana123'], 'bob@hotmail.com': ['Bob','123bob'],'claudio@bol.com': ['Claudio','clau!*'] }
    
    if not email in usuarios:
        return print('USUARIO NÃO EXISTE!')
    
    # print(usuarios[email][1])
    if usuarios[email][1] == senha:
        return print('USUÁRIO AUTENTICADO!',usuarios[email][1])
    else:
        return print('CREDENCIAIS DE ACESSO ESTÃO INCORRETAS!')
        

registro = autenticate('ana@gmail.cm','ana12')

