def is_magic_square(matrix):
    # Verifique se a matriz é quadrada
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_rows != num_cols:
        return False

    # Calcule a soma das diagonais principal e secundária
    diag_sum_1 = sum(matrix[i][i] for i in range(num_rows))
    diag_sum_2 = sum(matrix[i][num_rows - i - 1] for i in range(num_rows))

    # Verifique se a soma das diagonais é a mesma
    if diag_sum_1 != diag_sum_2:
        return False

    # Calcule a soma da primeira linha
    expected_sum = diag_sum_1

    # Verifique a soma das linhas e colunas
    for i in range(num_rows):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(num_rows))
        if row_sum != expected_sum or col_sum != expected_sum:
            return False

    return True

# Exemplo de uso
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz não é um quadrado mágico.")
