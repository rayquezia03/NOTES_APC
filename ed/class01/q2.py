valores = [0,1,2,3,-3,-5,-7]
soma = 0

for num in valores:
    soma += num

media = soma /len(valores)

for value in valores:
    if value  < media:
        print(value,' está abaixo da média!',media)