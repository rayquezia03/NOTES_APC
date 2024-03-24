def buscabin(lista,chave):
    if len(lista) == 0:
        return None
    
    meio = len(lista) // 2
    
    if lista[meio] == chave:
        return lista[meio]
    elif chave < lista[meio]:
        return buscabin(lista[:meio],chave)
    else:
        return buscabin(lista[meio+1:],chave)
    
students = [
    ('ana',{'tel':123,'matricula': 123456,'data_nasc': '15/11/2003'}),
    ('bruna',{'tel':345,'matricula': 123456,'data_nasc': '15/11/2003'}),
    ('carla',{'tel':678,'matricula': 123456,'data_nasc': '15/11/2003'}),
    ('dayane',{'tel':1567,'matricula': 123456,'data_nasc': '15/11/2003'}),
    ('elianne',{'tel':1567,'matricula': 123456,'data_nasc': '15/11/2003'}),
    ('fátima',{'tel':1567,'matricula': 123456,'data_nasc': '15/11/2003'}),
]

#aluno que será buscado:
value = students[5]

#resultado da busca:
info_aluno = buscabin(students,value)
print(f'Dados do aluno encontrado: {info_aluno}')