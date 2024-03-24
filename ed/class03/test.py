def busca_bin(dic,chave):
    
    if len(dic) == 0:
        return None
    
    meio = len(dic) // 2
    
    # print(dic[meio][0])
    if chave == dic[meio][0]:
        return dic[meio][1]['tel']
    elif chave < dic[meio][0]:
        return busca_bin(dic[:meio],chave)
    else:
        return busca_bin(dic[meio+1:],chave)
    

contatos = [
    ('ana',{'tel':'123','email':'ana@gmail.com'}),
    ('bruna',{'tel':'123','email':'bruna@gmail.com'}),
    ('carla',{'tel':'123','email':'carla@gmail.com'}),
    ('zelia',{'tel':'123','email':'zeliaa@gmail.com'})]

print(busca_bin(contatos,'zelia'))