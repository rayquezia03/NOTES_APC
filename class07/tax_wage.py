wages = [1501]

def tax_calculation(wage):
    if wage <= 1500:
        return print('you are exempt from income tax!')
    else:
        tax = (27/100)*wage
        return print(f'For the wage: {wage} you need to pay the following tax income: {tax}!')
    
for salary_per_employee in wages:
    tax_calculation(salary_per_employee)