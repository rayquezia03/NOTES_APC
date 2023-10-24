lista = ['65','75','20','61','6d','6f','20','70','72','6f','67','72','61','6d','61','72']

def convert_to_nl(lista):

    utf_letras = {
    '61':'a', '62': 'b', '63': 'c', '64': 'd','65': 'e','66': 'f', '67': 'g','68':'h','69': 'i','6a':'j','6b':'k','6c':'l','6d':'m','6e': 'n', '6f': 'o','70': 'p', '71':'q','72':'r', '73':'s', '74': 't','75':'u', '76':'v','77':'w','78':'x', '79':'y','7a':'z', '20': ' '
    }
    
    saida = []
    for carc in lista:
        utf_letras[carc]
        saida += utf_letras[carc]
    return saida

#saida de strings em lista
traducao = convert_to_nl(lista)
print(traducao)

#saida por letra
for letra in traducao:
    print(letra)