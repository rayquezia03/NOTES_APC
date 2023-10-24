num_horas_trabalhadas = int(input('digite quantas horas foram trabalhadas: '))
salario_por_hora = float(input('digite qual é o salário por hora trabalhada: '))
salario_total = 0
qtde_horas_extras = num_horas_trabalhadas - 40
salario_extra = qtde_horas_extras * (salario_por_hora + ((50/100)*salario_por_hora))

if (num_horas_trabalhadas > 40):
    print('Fez horas extras!')
    salario_total =  (salario_por_hora * 40) + salario_extra
    print(f'O salário do funcionario foi de {salario_total}')
else:
    print('Não fez horas extras!')
    salario_total =  salario_por_hora * 40
    print(f'O salário do funcionario foi de {salario_total}')