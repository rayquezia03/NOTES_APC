# numeros_negativos = []
# n = 1
# print('Digite 0 para parar o recebimento de valores dentro da lista.')

# while (n != 0):
#     n = int(input('Digite um número real: '))
#     if (n < 0):
#         numeros_negativos.append(n)
    
# print(f'Foram digitados {len(numeros_negativos)} numeros negativos!')

numeros_negativos = [1,2,3,4,-1,-2,-4]
count = 0

for num in numeros_negativos:
    if num < 0:
        count += 1
        
print(f'Há {count} números negativos!')