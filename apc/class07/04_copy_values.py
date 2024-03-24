list_test = [1,2,3,4,9,12,44]
list_test2 = [1,2,3,4,15,20]

def copy_list_whithout_repetition(list1,list2):
    list_final = []
    for value in list1:
        for elem in list2:
            if elem != value and elem not in list_final:
                list_final.append(elem)              
                
    return print(list_final)

copy_list_whithout_repetition(list_test,list_test2)