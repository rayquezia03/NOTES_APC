print('Welcolme to your schedule contacts!')

#função que recebe o nome do novo contato e uma lista contendo os numeros de celulare
def IncluirNovoNome(nome,telefones):
    schedule = {}
    lista_celulares = []

    if not telefones:
        return print('Digite um numero de celular para add o novo contato!')
    elif len(telefones) == 1:
        schedule[nome] = telefones
    else:
        for numero in telefones:
            lista_celulares.append(numero)
        schedule[nome] = lista_celulares
    
    return print(schedule)

def IncluirNovoTelefone(nome,telefones_novos):
    schedule = {
    'mariana': [456]}
    lista_celulares = []

    for key in schedule:
        if key == nome:
           schedule[nome].append(telefones_novos)
        else:
            print('Usuário não existe na agenda. Deseja criar um novo? S/N')
            resp = input('S/N')
            
            if resp == 'N':
                return print('Operação cancelada!')
            elif resp == 'S':
                IncluirNovoNome(nome,[telefones_novos])
                
        return print(schedule)
    

def ExcluirTelefone(nome,telefone_excluir):
    schedule = {
    'mariana': [456],'ana': [123,234]}
    lista_celulares = []

    for key in schedule:
        if key == nome:
           if len(schedule[nome]) == 1:
               print(f'O contato {nome} só possui um telefone vinculado, portanto será exlcuído do sistema!')
               del schedule[nome]
               print('Contato removido com sucesso!')
               break
           else:
               for celular in schedule[nome]:
                  if celular == telefone_excluir:
                    schedule[nome].remove(celular)
            
            
    return print(schedule)
               
def ExcluirNome(nome):
    schedule = {
    'mariana': [456],'ana': [123,234]}
    lista_celulares = []

    for key in schedule:
        if key == nome:
            del schedule[nome]
            break
                          
    return print(schedule)

def ConsultarTelefone(nome):
    schedule = {
    'mariana': [456],'ana': [123,234]}
    lista_celulares = []

    for key in schedule:
        if key == nome:
            celulares = schedule[nome]
            print(f'Os numeros de celulares vinculados ao contato {nome} é/são:')
            for numeros in celulares:
                print(numeros)


ConsultarTelefone('mariana')