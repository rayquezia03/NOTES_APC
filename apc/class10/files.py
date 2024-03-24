# arquivo = open(/home/rayane/exercicios/class10/dados.pxt,)

path = 'dados.pxt'

arquivo = open(path,'r')

# arquivo.write('passaword: aaaaaa, user: rayane')
# arquivo.close()

# print(arquivo)

texto = arquivo.read()
arquivo.close()

att = texto.split("\n")

usuarios = []

for linha in att:
    
    print(linha)
    nw = linha.split(', ')
    print(nw)
    
    usuario = {'nome':nw[0], 'email':nw[1], 'password': nw[2]}

    usuarios.append(usuario)    
 
for user_info in usuarios:
    print(user_info['email'])
    print(user_info['nome'])
    print(user_info['password'])
 
