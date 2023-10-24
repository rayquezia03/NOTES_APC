# names = ['ana','julia','luana','lia']

# name_digitado = input('Digite um name: ')

# for i in names:
#     if i == name_digitado:
#         print('tá na lista')   
#     else:
#         continue

#========================================
'''
Renda até R$ 1.903,98: isento de imposto de renda; 
Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%; 
Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%; 
Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
'''
  
qtde = int(input('Digite a quantiade de pessoas que serão cadastradas: '))
pessoa = []
lista_de_pessoas = []

for cadastro in range(qtde):
    name = input('Digite o nome do funcionário: ')
    renda_mensal = float(input('Digite o seu salário: '))
    
    pessoa.append(name)
    pessoa.append(renda_mensal)
    
    if renda_mensal >= 4664.68 or renda_mensal >= 3751.06:
        desconto = (22.5/100) * renda_mensal
    elif renda_mensal >= 2826.65 or renda_mensal >= 3751.05:
        desconto = (15/100) * renda_mensal
    elif renda_mensal >= 1903.99 or renda_mensal >= 2826.65:
        desconto = (7.5/100) * renda_mensal
    else:
        desconto = 0
        print('Isento de imposto de renda: ')
        
    pessoa.append(desconto)
    
    lista_de_pessoas.append(pessoa)
    
    pessoa = []
    
for pessoa in lista_de_pessoas:
    print(f'O imposto de renda de {pessoa[0]} é de R$ {round(pessoa[2],2)} mensais!')
    
# print(lista_de_pessoas)