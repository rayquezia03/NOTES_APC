matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

def mult_mtz(matriz,integer):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matriz_mult = [0]*linhas
    for i in range(linhas):
        matriz_mult[i] = [0]*colunas
        

    i = 0
    j = 0

    #vai percorrer as linhas 
    for i in range(linhas):
        #vai percorrer as colunas
        for j in range(colunas):
            matriz_mult[i][j] = matriz[i][j] * integer                
            j+=1
        i+=1
    return print(matriz_mult)


mult_mtz(matrix,2)