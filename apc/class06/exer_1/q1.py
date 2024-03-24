lista = [ ]
num = 1

while (num != 0):
        num = int(input('Digite um número'))
        lista.append(num)
        
print(lista)

soma = 0
count = 0
for i in lista:
    soma += i
    
media = soma/len(lista)
print(media)