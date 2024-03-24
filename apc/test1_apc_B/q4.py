dias = int(input('Digite a quantidade de dias que pretende ficar hospedado:'))
total_fixo = dias*150

if (dias < 5):
    total_fixo += 10.5*dias
elif (dias == 5):
    total_fixo += 9*dias
elif (dias > 5):
    total_fixo += 7.5*dias
    
print(f'O total a se pagar é de: R$ {total_fixo}')