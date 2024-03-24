
def add_new_contact(name,telefone):
    path = 'database.txt'

    schedule = open(path,'a')
    nome = '\n'+name
    celular = ','+telefone
    
    schedule.write(nome)
    schedule.write(celular)

    schedule.close()
    
    return schedule

a = add_new_contact('bbbb','123456')
texto = a.read()
a.close()

print(a)




    
