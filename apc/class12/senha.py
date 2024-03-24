entrada = ['BCEAEB','ECCBDA']
associacoes = [{'A':{1,7},'B':{3,9},'C':{0,8},'D': {5,6},'E': {2,4}},
               {'A':{9,0},'B':{7,5},'C':{8,4},'D':{6,2},'E':{3,1}}]

for i in range(6):
    letra1 = entrada[0][i]
    letra2 = entrada[1][i]
    numero = associacoes[0][letra1] & associacoes[1][letra2]
    print('\t=> numero: ',numero)
