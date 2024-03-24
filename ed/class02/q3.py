'''
Implemente uma função recursiva que, dada uma lista de inteiros ordenada, busque por um valor
'''

def find_in_list(lista,value):
    
    if len(lista) == 0:
        return None
    
    meio = len(lista) // 2
    
    if lista[meio] == value:
        return print(f'{value} encontrado na posição {meio} da lista!')
    
    elif value < lista[meio]:
        return find_in_list(lista[:meio],value)
    else:
        return find_in_list(lista[meio+1:],value)
    
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
value = 14

print(find_in_list(lista,value))