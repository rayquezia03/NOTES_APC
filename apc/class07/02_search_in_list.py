list_test = [1,2,3,4,5]

def search_value(list,value):
    hold = False
    for elem in list:
        if elem == value:
            hold = True
        
    
    if hold == True: 
        return print('Is in list!')
    else:
        print('Isnt in list!')
            
search_value(list_test,33)