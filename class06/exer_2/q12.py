palavra = input('digite a palavra: ')
i = 0

for letra_da_vez in palavra:
    if letra_da_vez in ('a','b','c','d','e'):
        i +=1

print(f'A palavra {palavra} é composta por {i} vogais')