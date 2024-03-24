def remover_repetidos(lista):
    lista_sem_repeticao = list(set(lista))
    return lista_sem_repeticao

# Exemplo de uso:
lista_original = [1, 2, 2, 3, 4, 4, 5]
lista_sem_repeticao = remover_repetidos(lista_original)
print("Lista original:", lista_original)
print("Lista sem elementos repetidos:", lista_sem_repeticao)
