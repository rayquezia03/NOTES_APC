# Abra o arquivo para leitura
with open("arquivo.txt", 'r') as arquivo:
    # Inicialize um dicionário vazio
    dicionario = {}
    
    # Itere pelas linhas do arquivo
    for linha in arquivo:
        # Divida cada linha em identidade e nome
        partes = linha.split()
        
        # Verifique se a linha tem pelo menos duas partes (identidade e nome)
        if len(partes) >= 2:
            identidade = partes[0]
            nome = ' '.join(partes[1:])  # Para lidar com nomes com espaços
            
            # Adicione a entrada ao dicionário
            dicionario[nome] = identidade

# print(dicionario)
#rg de Alberto
#A busca é feita passando como chave o nome do dono do cpf
print(dicionario['Alberto'])