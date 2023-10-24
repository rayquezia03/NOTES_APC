#repetição

#para I em intervalo(1,11):
# for i in range (1,11):
#     print(i)   
#=======================================
#somar o valor atual com o inteior

# soma = 0

# for i in range(0,11):
#     soma = soma + i
#     print(i,soma)
#=======================================
# for i in range(0,11):
#     if (i % 2 == 0):
#         print(i)
#=======================================
# for i in range(0,20,2):
#         print(i)
#=======================================

# n = int(input('Digite o incio: '))
# m = int(input('Digite o fim: '))

# count = 0
# soma = 0
# for i in range(n,m):
#         soma = soma + i
#         count = count + 1
        
# print('soma total:',soma)
# print('contagem total:',count)
# media = soma/count
# print(f'A media é igual a: {media}')

#=======================================

# listaNum = [2,3,4,5,6,7]
# soma = 0
# for n in listaNum:
# 	soma = soma + n
# print (soma)

nota = 8.5

notas = [8.5,7,9,7.5,6.9]

#contando os elementos de uma lista
a = len(notas)
print(a)

#pegando o ínidice através da soma de inteiros
#print(notas[1+2])

#atualizando o valor pelo índice
notas[3] = 4


#percorrendo a lista
# for i in range(4):
#         print(notas[i])
        
     
#percorrendo a lista para altereações
# if nota in notas:
#         print(nota)
# else:
#         print('n')

# percorrendo a lista para altereações
if nota in notas:
        print(nota)
else:
        print('n')
        
# for i in range(len(notas))
        
        
#=====================================================
#algoritmo que faz a soma de valores contidos dentro de uma lista
a = 0
lista = []

while a < 5:
    a+=1
    n = int(input('digite um numero: '))
    lista.append(n)

# lista = [1,4,10,10]

soma = 0
for i in lista:
    soma += i
    
print(soma)