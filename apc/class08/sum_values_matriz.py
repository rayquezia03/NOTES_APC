# linhas = 3
# colunas = 3

# matriz = [0]*linhas

# for i in range(linhas):
#     matriz[i] = [0]*colunas
    
# print(matriz)

matriz1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matriz2 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matriz3 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
matriz_soma = []
cont_lin = 0
cont_col = 0

for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        matriz3[i][j] =  matriz1[i][j] * matriz2[i][j]
        j+=1
    i+=1
    
        
print(matriz3)