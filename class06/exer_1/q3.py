# regra levando em consideração para qualquer valor de lista2 contido dentro de lista1

lista1 = [1,3,4,5]
lista2 = [4,5,6,7,8]
sub = False
# gera uma matriz de valores -> para cada elemento dentro da lista1, ele percorre todos os elementos da lista2
for a in lista1:
    # print(a)
    for b in lista2:
        # print(b)
        if a == b:
            sub = True

if sub == True:
    print(f'{a},{b} é subconjunto de lista1: {lista1}' ) 