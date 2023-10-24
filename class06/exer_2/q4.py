conjunto = []
i = 0
n = 5
count = 0

while (i < 3):
    i = i + 1
    inteiro = int(input('Digite um inteiro: '))
    conjunto.append(inteiro)
    
for num in conjunto:
    if num > n:
        count +=1
        
print(count,'numeros são maiores do que',n)