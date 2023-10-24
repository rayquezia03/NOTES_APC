num_de_carros = int(input('digite quantos carros foram vendidos pelo vendedor: '))
salario_fixo = float(input('digite o valor do salário fixo do vendendor:'))
comissao_fixa_por_carro = float(input('digite o valor da comissão fixa do vendendor:'))
valor_total_vendas = float(input('digite o valor total das vendas: '))

salario_total = salario_fixo + (num_de_carros*comissao_fixa_por_carro) + (5/100*valor_total_vendas)

print(salario_total)




