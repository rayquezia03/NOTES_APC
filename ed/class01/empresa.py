valor_bolsa = {'Rommanel': 222,'Dafiti': 333,'Zatini': 888,'Sadia':444}
for value in valor_bolsa:
    print(value)

maior = valor_bolsa['Rommanel']
print(maior)
# print(len(valor_bolsa))

for key in valor_bolsa:
    if valor_bolsa[key] > maior:
        maior = valor_bolsa[key]
        empresa_maior = key
        
print(maior,empresa_maior)

#possui custo N