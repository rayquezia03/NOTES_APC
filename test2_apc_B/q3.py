pesos = [56,78,89,76]
alturas = [1.80,1.55,1.9,1.8]

imc = 0
i = 0

while i < (len(pesos)):
    
    imc = round(pesos[i]/alturas[i]**2,2)
    
    print(f'O IMC é de {imc}')
    i +=1
    
    if imc > 30:
        print('Obesidade')
    elif imc > 25 and imc < 30:
        print('Acima do peso')
    elif imc > 18.5 and imc < 25:
        print('Peso normal')
    else:
        print('Abaixo do peso')