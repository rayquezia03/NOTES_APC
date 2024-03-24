matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def check_int_in_mtz(matriz,num):
    linhas = len(matriz)
    colunas = len(matriz[0])

    existe = False

    i = 0
    j = 0

    #vai percorrer as linhas 
    for i in range(linhas):
        #vai percorrer as colunas
        for j in range(colunas):
            '''
            Com a junção dos dois laços, é possível percorrer TODAS as posições de index possíveis na mtriz!
            
            '''
            #Aqui I percorre a linha e J cada elemento por linha
            if matriz[i][j] == num:
                existe = True
       
        
    return existe

a = check_int_in_mtz(matriz,1)
print(a)