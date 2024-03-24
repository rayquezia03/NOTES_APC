valor_total = float(input('digite o valor da venda:'))

valor_com_desconto = valor_total - ((10/100)*valor_total)
valor_parcelado = round(valor_total/3,2)
comissao_a_vista =  5/100*valor_com_desconto
comissao_a_prazo = 5/100*valor_total

print(f'Valor à vista com desconto: {valor_com_desconto}')
print(f'Valor da parcela em 3x sem juros: {valor_parcelado}')
print(f'Comissão do valor a vista: {comissao_a_vista}')
print(f'Comissão do valor a vista: {comissao_a_prazo}')