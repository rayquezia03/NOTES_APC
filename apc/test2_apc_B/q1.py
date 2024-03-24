pesos = [90,100,93,94,95,92,88]

for peso_produto in pesos:
    if peso_produto > 92 or peso_produto < 88:
        print('Este produto deve ser descartado')
    else:
        print('O produto está dentro do padrão para comercialização!')