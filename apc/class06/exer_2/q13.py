conjunto = [1,2,3,4,5,90]
i = 0

m = int(input('digite uma sequencia e 0 para parar'))
n = int(input('digite uma sequencia e 0 para parar'))
# var = False

while (i < len(conjunto) -1) and not(m != conjunto[i] and n!= conjunto[i+1]):
    i +=1

if i == len(conjunto)-1:
    print('não')
else:
    print('sim')