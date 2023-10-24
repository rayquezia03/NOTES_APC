#Uma matriz é dita simétrica se ela for igual a sua transposta
def create_matrix(linhas,colunas,x):
    matriz = [x]*linhas
    
    for i in range(linhas):
        matriz[i] = [x]*colunas
        
    return matriz

matriz1 = create_matrix(3,3,1)
matriz2 = create_matrix(3,3,1)

linhas = len(matriz1)
colunas = len(matriz1[0])
# print(matriz1)
simetrica = False
for i in range(linhas):
    for j in range(colunas):
        if matriz1[i][j] != matriz2[j][i]:
            simetrica = False
        elif matriz1[i][j] == matriz2[j][i]:
            simetrica = True
    
print(simetrica)
        