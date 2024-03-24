matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix2 = [
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2[j][i]=matrix[i][j]

print(matrix2)

#SEGUNDA MANEIRA DE FAZER
linhas = len(matrix)
colunas =  len(matrix[0])

colum_to_line = []

aux = 0
while aux < len(matrix[0]):
    for i in range(3):
        colum_to_line.append(matrix[i][aux])
    aux +=1

print(colum_to_line)