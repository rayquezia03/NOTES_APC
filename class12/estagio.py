def encontrarMaiorNota(notas):
    maior_nota = -1
    for nota in notas:
        if nota[1] > maior_nota:
            maior_nota = nota[1]
    return maior_nota

def encontrarAlunos(notas):
    alunos = []
    maior_nota = encontrarMaiorNota(notas)
    for nota in notas:
        if nota[1] == maior_nota:
            alunos.append(nota[0])
    return alunos

notas = [
    (1,87),
    (2,90),
    (3,75),
    (4,12),
    (5,40),
    (6,95),
    (7,92),
    (8,95),
    (9,50),
    (10,45)]

print(encontrarAlunos(notas))