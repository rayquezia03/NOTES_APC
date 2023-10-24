arquivo = open('eleicoes.txt')
votos = []
for linha in arquivo.readlines():
    votos.append(int(linha.replace('\n','')))
print(votos)

contagem = {}
for voto in votos:
    if voto not in contagem:
        contagem[voto] = 1
    else:
        contagem[voto] += 1

maior = 0
vencedor = 0
for voto in contagem:
    if contagem[voto] > maior:
        maior = contagem[voto]
        vencedor = voto

print(contagem)
print(vencedor)

arquivo.close()