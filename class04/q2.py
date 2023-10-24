idade = int(input('digite a sua idade: '))

if idade <= 14:
    print('CRIANÇA')
elif idade <= 17:
    print('ADOLESCENTE')
elif idade <= 59:
    print('ADULTO')
else:
    print('IDOSO')  