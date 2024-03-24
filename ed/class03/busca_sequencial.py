# def find_contato(dic,name):
#     if name not in dic:
#         return None
    
#     keys = []
#     for key in contatos:
#         keys.append(key)
    
#     indice = len(keys) // 2
    
#     if dic[keys[indice]] == name:
#         print('ACHOU!')

# contatos = {'ana': {'cel':123,'email':'aninha@gmail.com'},'lia': {'cel':123,'email':'aninha@gmail.com'},'clara': {'cel':123,'email':'aninha@gmail.com'},'maria': {'cel':123,'email':'aninha@gmail.com'},'miria': {'cel':123,'email':'aninha@gmail.com'},'maria': {'cel':123,'email':'aninha@gmail.com'}}

# index = len(contatos)//2


# pessoas = ['ana','clara','zelia','cecilia']

# keys = []
# for key in pessoas:
#     keys.append(key)

# print(keys)


def buscaBin(lista, chave):
    if len(lista) == 0:
        return None

    meio = len(lista)//2

    if lista[meio] == chave:
        return lista[meio]

    elif chave < lista[meio]:
        return buscaBin(lista[:meio], chave)

    else:
        return buscaBin(lista[meio+1:], chave)

lista = [1,2,5,6,8,10,12,13,20,25,28,31,40]
print(buscaBin(lista,31))   