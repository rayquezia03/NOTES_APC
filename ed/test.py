#insertion sort
def insertion_sort(list):
    num_comp = 0
    for i in range(1,len(list)):
        chave = list[i]
        j = i-1
        while j >= 0 and list[j] > chave:
            num_comp +=1
            list[j+1] = list[j]
            j -=1
        list[j+1] = chave
    return list,num_comp


nomes = ['dayane','ana','carla','bruna','maria']
num_comp_insertion = insertion_sort(nomes)[1]
print('Num de comparações para insertion sort:',insertion_sort(nomes)[0])

#selection sort
def selection_sort(list):
    n = len(list)
    num_comp = 0
    for i in range(0,n-1):
        meio = i
        for j in range(i+1,n):
            num_comp +=1
            if list[meio] > list[j]:
                meio = j
        list[i],list[meio] = list[meio],list[i]
    return list,num_comp

nomes = ['dayane','ana','carla','bruna','maria']
num_comp_selection = selection_sort(nomes)[1]
print('Num de comparações para selection sort:',selection_sort(nomes)[0])

print('@@@@@@@@@@@@@@@@@@@@@@@@')
print(num_comp_insertion,num_comp_selection)
if num_comp_insertion < num_comp_selection:
    print('O numero de comparações foi menor com o algoritmo insertion sort, e portanto pode ser considerado o algoritmo mais eficiente!')
else:
    print('O algoritmo mais eficiente,PARA ESSE CASO EM ESPECÍFICO, foi o selection sort!')