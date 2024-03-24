path = 'ips.txt'

arquivo = open(path,'r')

texto = arquivo.read()
arquivo.close()

list_ips = texto.split("\n")

#verificações
endereco = []
for ip in list_ips:
    endereco.append(ip.split('.'))

# print(endereco)
for adress in endereco:
    # print(adress)
    if adress.count('X') == 3:
        print('Endereço válido!')
    else:
        print('Este endereço não é válido pela quantidade de bits possíveis para representar')
    for value in adress:
        if int(value) > 256:
            print(f'O endereço {adress} não é valido, pois {value} é um valor maior do que o convencional!')
        else:
            print(f'O endereço {adress} não é valido, pois {value} é um valor maior do que o convencional!')


#   
# for elem in endereco:
#     while elem != ' ':
#         caracs.append(elem)
#         print(caracs)
# print(endereco[0])


        # if int(a) > 256:
        #     print(f'Este ip {a} é inválido!')
        # else:
        #     print(f'Este ip {a} é válido!')
