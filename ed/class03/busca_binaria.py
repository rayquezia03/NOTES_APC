def busca_bin(lista,chave):
    
    if len(lista) == 0:
        return None
    
    meio = len(lista) // 2

    if lista[meio] == chave:
        return lista[meio]
    elif chave < lista[meio]:
        return busca_bin(lista[:meio],chave)
    else:
        return busca_bin(lista[meio+1:],chave)
    
        
numbers = [1,2,3,4,5,6,7,12,9,21,25,40]
value = 25
print(busca_bin(numbers,value))