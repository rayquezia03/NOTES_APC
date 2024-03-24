def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente aplica o merge_sort nas sublistas
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina as sublistas ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Combina as sublistas ordenadas
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes, se houver, de ambas as sublistas
    merged += left[left_index:]
    merged += right[right_index:]

    return merged

# Exemplo de uso:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Lista ordenada:", sorted_arr)
