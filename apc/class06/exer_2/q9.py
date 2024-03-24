# conjunto_lista = [100,250,700,13,15]

# n = int(input("Digite o valor de n: "))

# if not conjunto_lista:
#     print("Erro: O conjunto não pode estar vazio.")
# else:
#     valor_mais_proximo = conjunto_lista[0]
#     menor_distancia = n - conjunto_lista[0]

#     for num in conjunto_lista:
#         distancia = n - num
#         if distancia == 0:
#             valor_mais_proximo = num
#             break
#         elif distancia < 0:
#             print(-distancia)
#             print('==========')
#             print(menor_distancia)
#             if -distancia < abs(menor_distancia):
#                 valor_mais_proximo = num
#                 menor_distancia = -distancia
#         elif distancia > 0:
#             if distancia < menor_distancia:
#                 valor_mais_proximo = num
#                 menor_distancia = distancia

#     print(f"O valor mais próximo de {n} no conjunto é: {valor_mais_proximo}")

conjunto_lista = [100,250,700,13,15]

n = int(input("Digite o valor de n: "))

valor_mais_proximo = conjunto_lista[0]
menor_distancia = n - conjunto_lista[0]

for num in conjunto_lista:
    distancia = n - num
    if distancia == 0:
        valor_mais_proximo = num
        break
    elif distancia < 0:
        print('==========')
        # print(menor_distancia, -menor_distancia)
        # print(abs(menor_distancia))
        # print(-distancia < abs(menor_distancia))
        if -distancia < abs(menor_distancia):
            valor_mais_proximo = num
            menor_distancia = -distancia
    elif distancia > 0:
        print('aaaaaaaaaaa')
        if distancia < menor_distancia:
            valor_mais_proximo = num
            menor_distancia = distancia

print(f"O valor mais próximo de {n} no conjunto é: {valor_mais_proximo}")