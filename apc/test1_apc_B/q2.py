idade = int(input('Digite a idade do seu funcionário:'))
anos_de_trabalho = int(input('Digite quantos anos o funcionário tem de trabalho:'))

if idade < anos_de_trabalho:
    print('IDADE INVÁLIDA')
elif (idade >= 65):
     print('Funcionário pode se aposentar!')
elif (anos_de_trabalho >= 30):
    print('Funcionário pode se aposentar!')
elif (idade >= 60 and anos_de_trabalho >= 25):
    print('Funcionário pode se aposentar!')
else:
    print('Não pode se aposentar!')