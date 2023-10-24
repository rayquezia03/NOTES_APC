values = [100,20,3,4,5]

def Bigger(values):
    bigger_value = values[0]
    for value in values:
        if value > bigger_value:
            bigger_value = value
            
    return bigger_value
   
a = Bigger(values)
    
print(a)
