nome = input('Digite o seu nome: ')
sexo = input("Digite o seu sexo com 'M' ou 'F':")
altura = float(input('Digite a sua altura em metros: '))

if (sexo == 'M'):
    peso_ideal = (72.7*altura) - 58
    print(f'{nome}, o seu peso ideal é de: {peso_ideal}')
elif (sexo == 'F'):
    peso_ideal = (62.1*altura) - 44.7
    print(f'{nome}, o seu peso ideal é de: {peso_ideal}')
else:
    print('Sexo inválido!')