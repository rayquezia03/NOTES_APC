def intersecao_listas(lista1, lista2):
    # Converte as listas em conjuntos para facilitar a operação de interseção
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Encontra a interseção entre os conjuntos
    intersecao = conjunto1.intersection(conjunto2)
    
    return list(intersecao)

# Exemplo de uso:
lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]
resultado = intersecao_listas(lista_a, lista_b)
print("Interseção entre as listas:", resultado)
