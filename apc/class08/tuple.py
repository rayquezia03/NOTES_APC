usuarios = []

for i in range(0,2):    

    nome = input('DIgite o nome do usuário:')
    idade = int(input('Digite a idade do usuário: '))
    cpf = int(input('Digite o cpf do usuário: '))
    tupla_created = nome,idade,cpf
    print("---------------")
    print(tupla_created)
    
    usuarios.append((tupla_created),)
    
   
print('===========')
print(usuarios)