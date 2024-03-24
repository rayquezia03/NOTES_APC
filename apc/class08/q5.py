# def media_aluno(n1,n2):
notas = {}
medias = {}
nome = 'A'

while nome != '':
    nome = input('Digite o nome do aluno: ')
    if nome == '':
        break
    n1 = int(input('nota 1: '))
    n2 = int(input('nota 2: '))
    notas[nome] = n1,n2
    
    media = (notas[nome][0]+notas[nome][1])/2
    medias[nome] = media
        
print(notas,medias)
        
    