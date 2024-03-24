valor = float(input('digite o valor das vendas:'))
comissao = 0

if valor > 50000:
    comissao = (12/100)*valor
elif valor < 50000 and valor >= 30000:
    comissao = (9.5/100)*valor
else:
    comissao = (7/100)*valor
    
print('o valor da sua comissão é de:',int(comissao))