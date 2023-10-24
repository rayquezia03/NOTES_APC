def vencedor(numeros):
    for pos,valor in enumerate(numeros,1):
        if pos == int(valor):
            return valor
        
arquivo  = open('quermesse.txt','r')
conteudo = arquivo.read()
numeros = conteudo.split(' ')
print(vencedor(numeros))
arquivo.close()
