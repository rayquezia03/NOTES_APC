qtde = int(input('Digite a quantiade de pessoas que serão cadastradas: '))
pessoa = []
lista_de_pessoas = []

for cadastro in range(qtde):
    
    name = input('Digite o seu nome: ')
    peso = int(input('Digite o seu peso'))
    altura = int(input('Digite a sua altura'))
    
    pessoa.append(name)
    pessoa.append(peso)
    pessoa.append(altura)
    
    lista_de_pessoas.append(pessoa)
    
    pessoa = []
    
for array_pessoa in lista_de_pessoas:
    
    imc = array_pessoa[1]*array_pessoa[2]
    
    print('==========================================')
    print(f'O IMC de {array_pessoa[0]} é {imc}')