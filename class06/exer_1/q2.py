#algoritmo que faz a soma de valores contidos dentro de uma lista
# a = 0
# lista = []

# while a < 5:
#     a+=1
#     n = int(input('digite um numero: '))
#     lista.append(n)   

lista = [1,4,10,10,3,2]

soma = 0
for i in lista:
    if (i % 2 == 0):
        soma += i
    
print(soma)

#==========================================

names = ['ana','julia','luana','lia']

name_digitado = input('Digite um name: ')

for i in names:
    if i == name_digitado:
        print('tá na lista')   
    else:
        continue

#===========================================

inteiro_values = [1,2,3,4]
num = int(input('Digite o inteiro a ser achado: '))

for i in inteiro_values:
    if i == num:
        print('Numero encontrado!')
    else:
        continue