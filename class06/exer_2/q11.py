palavra = input('digite a palavra: ')
letra = input('digite uma letra: ')
i = 0

for letra_da_vez in palavra:
    if letra_da_vez == letra:
        i +=1
        
print(f'A letra {letra} se repete {i} vezes')