# def find_in_list(lista, value, inicio=0, fim=None):
#     if fim is None:
#         fim = len(lista) - 1

#     if inicio > fim:
#         return f'{value} não existe dentro da lista!'

#     meio = (inicio + fim) // 2

#     if lista[meio] == value:
#         return f'{value} encontrado na posição {meio} da lista!'
#     elif lista[meio] < value:
#         return find_in_list(lista, value, meio + 1, fim)
#     else:
#         return find_in_list(lista, value, inicio, meio - 1)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# value = 4

# print(find_in_list(lista, value))

def buscaBin(lista, chave):
    if len(lista) == 0:
        return None

    # verificar o elemento exatamente ao meio
    meio = len(lista) // 2

    # se for igual, retorne
    if lista[meio] == chave:
        return print(f'{value} encontrado na posição {meio} da lista!')

    # se for menor, chame a função para a porção inicial
    elif chave < lista[meio]:
        return buscaBin(lista[:meio], chave)

    # se for maior, chame a função para a porção final
    else:
        return buscaBin(lista[meio + 1:], chave)
    
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
value = 4

print(buscaBin(lista,value))