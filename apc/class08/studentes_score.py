qtde_alunos = int(input('Digite quantos alunos são: '))
count = qtde_alunos
dicionario = {}

while count != 0:
   
    aluno = input('Digite o nome')
    
    n1 = int(input('Digite n1: '))
    n2 = int(input('Digite n2: '))
    
    dicionario[aluno] = [n1,n2]
    count -= 1
    
def medias(nome,dicionario):
    medias = {}
    for aluno in dicionario:  
        print(aluno)  
        media = (dicionario[aluno][0] + dicionario[aluno][1])/2
        medias[aluno] = (dicionario[aluno][0] + dicionario[aluno][1])/2
    return medias

print(medias('ana',dicionario))
    
# print(dicionario)