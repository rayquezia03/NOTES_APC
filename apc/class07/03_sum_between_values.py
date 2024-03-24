list_test = [1,2,3,4,10]

def sum_max(list):
    sum_values = list[0]
    sum_max = list[0]

    for elem in list:
        for i in range(0,len(list)-1):
           sum_values = list[i] + list[i+1] 
           
           if sum_values > sum_max:
               sum_max = sum_values
    
    return print(sum_max)


sum_max(list_test)