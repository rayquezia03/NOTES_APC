conjunto = [1,2,3,5]
n = 5
verificacao = False

for num in conjunto:
    while (num > n):
        verificacao = True
        break
        
if verificacao == True:
    print('Há valores maior que ',n)
else:
    print('Não há valores maior que ',n)