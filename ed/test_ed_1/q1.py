def schedule(agenda,name,tel):
    exists = None
    
    #atualiza caso haja o usuario na agenda
    if name in agenda:
         agenda[name] = tel
         exists = True
    else:
        agenda[name] = tel
        exists = False
        
    return agenda,agenda[name],exists
    
contatos = {
    'ana': 1233333,
    'bruna': 344555655,
    'carla': 56878797
}

contact_name = 'mirian'
new_tel = 222
#chamada da função para add o contato novo
updated_schedule,tel,exists = schedule(contatos,contact_name,new_tel)
contatos = updated_schedule

print(f'Agenda de contatos atualizada: {updated_schedule}')
print('@@@@@@@@')

'''
if exists == True:
    print(f'O contato {contact_name} existe na sua agenda, e portanto foi atualizado o numero de contato.')
else:
    print(f'O novo contato {contact_name} foi adicionado na sua agenda.')
'''