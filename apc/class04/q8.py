# se o modulo de a por b == 0, então a é multiplo de b

a = int(input('digite o valor: '))
b = int(input('valor múltiplo: '))

if (a > b and a % b == 0) or (a == b) or (b > a and b % a == 0):
    print('Múltiplos')
else:
    print('Não são múltiplos')
    