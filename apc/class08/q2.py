#lista de tuplas 

list = []
tuple_cod = []

for i in range(0,3):
    # tupla = 'verde:',(200,20,100)
    cor = input('Digite a cor: ')
    for i in range(0,3):
        codigo = int(input('Digite o código: '))
        tuple_cod.append(codigo)
        
    list.append((cor,tuple(tuple_cod)))
    

print(list[0])


