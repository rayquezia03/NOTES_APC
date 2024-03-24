def combinacao(list1, list2):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(list1) and right_index < len(list2):
        if list1[left_index] < list2[right_index]:
            merged.append(list1[left_index])
            left_index += 1
        else:
            merged.append(list2[right_index])
            right_index += 1

    # Adiciona os elementos restantes, se houver, de ambas as sublistas
    merged += list1[left_index:]
    merged += list2[right_index:]

    return merged

list2 = [1,2,3,4,5]
list1 = [6,7,8,9,10]
result = combinacao(list1,list2)
print(result)
