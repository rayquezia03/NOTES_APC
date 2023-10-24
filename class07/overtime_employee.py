employeers_hours = [100]

def overtime_calculate(wage_per_hour,hours):
    salary = 0
    
    if hours <= 40:
        salary = hours*wage_per_hour
        print('You didnt make overtime')
    else:
        salary = 40*wage_per_hour + (hours-40)*(1.5*wage_per_hour)
        extra_salary = (hours-40)*(1.5*wage_per_hour)
        print(f'Your extra salary is: {extra_salary}')
        print(f'You did overtime! You won {salary} R$ of extra salary!')

for hour in employeers_hours: 
    value_hour = 40
    overtime_calculate(value_hour,hour)
