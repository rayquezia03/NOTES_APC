list_test = [2,3,5,2]

def average(list):
    sum_total = 0
    for value in list:
        sum_total += value
        
    average = sum_total/len(list)
    
    return average

media_of_list = average(list_test)
print(f'The average of elements of list is: {media_of_list}')

'''
CALCULO DA VARIÂNCIA:

1 - Primeiramente, devemos calcular a média aritmética do conjunto;
2 - Em seguida, subtraímos de cada valor do conjunto a média calculada e elevamos o resultado ao quadrado;
3 - Por fim, somamos todos os valores e dividimos pelo número de dados.
'''

def variance(list):
    sum_total = 0
    for value in list:
        sum_total += value
        
    average = sum_total/len(list)
    
    var = 0
    sum_variance = 0
    set_variance = 0
    for value in list:
        var = (value - average)**2
        sum_variance += var
        
    set_variance = sum_variance/len(list)
        
    return set_variance


print(f'The variance of set numbers is: {variance(list_test)}')