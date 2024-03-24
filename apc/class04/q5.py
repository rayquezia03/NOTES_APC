l1 = float(input('digite o lado 1'))
l2 = float(input('digite o lado 2'))
l3 = float(input('digite o lado 3'))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('TRIANGULO')
    
    if l1 == l2 and l2 == l3:
        print('EQUILATERO')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('ISOCELES')
    elif l1 != l2 and l2 != l3:
        print('ESCALENO')
else:
    print('Não é triângulo')