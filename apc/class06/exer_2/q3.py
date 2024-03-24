n = 1
array = []
soma = 0

while (n != 0):
    n = int(input('Digite um valor inteiro ou 0 para parar o recebimento: '))
    soma += n
    if (n != 0):
        array.append(n)
    
media = soma/len(array) 
print(media)

for value in array:
    if value < media:
        print(f'{value} está fora da média')
    else:
        continue