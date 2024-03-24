conjunto = [1,2,3,4,-1]
negative = False

for value in conjunto:
    while value < 0:
        negative = True
        break
    
if negative == True:
    print('Valor negativo encontrado!') 
else:
    print('Não há negativos')