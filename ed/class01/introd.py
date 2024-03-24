i = 0 #Atribuições simples são desconsideradas

while i < 100:
    print(i) #1 -> repete-se pela qtde de vezes que i será encrementado, e portanto 100 vezes.
    i +=1 #1
    
# C(n) = 3*n 
'''
Para i < 100, temos:

    C(100) = 3*100
    C(100) = 300

'''
#EXEMPLO 02

nomes = ['ana','julia','carol'] #custo 1 - desconsiderado


type = input("Digite um nome:") #custo 1 - desconsiderado

#custo N - pois no caso do nome ser encontrado antes, o loop seria menor. Dessa forma o custo pode ser variável
for lin in nomes:
    if type == lin:
        print('Autenticado!')