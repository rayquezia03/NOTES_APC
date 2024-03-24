path = 'q1.txt'

arquivo = open(path)

list_value_v2 = arquivo.read()

formated_values = list_value_v2.split('\n')

for list_value in formated_values:
    list_value_v2 = list_value.split(', ')
    print(list_value_v2)
    maior = list_value_v2[0]
    for number in list_value_v2:
        if number > maior:
            maior = number
            
    print(f'O maior valor da sequencia: {list_value_v2} é: {maior}')
arquivo.close()
