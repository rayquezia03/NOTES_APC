#subtração do MAIOR valor do conjunto pelo MENOR
# numeros = [1,2,3,4,5]

# maior = numeros[0]
# menor = numeros[0]

# for num in numeros:
#     if num > maior:
#         maior = num
#     else: 
#         maior = maior
    
#     menor = 1
#     if num < menor:
#         menor = num
#     else:
#         menor = menor
numeros = [1,2,3,4,5]

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    while num > maior:
        maior = num
    
    while num < menor:
        menor = num

amplitude = maior - menor

print(maior,'=====',menor)
print(f"A amplitude do conjunto é {amplitude}")