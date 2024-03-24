def calculate_punctuation(punctuation,max,min):
    nota = ((punctuation-min)/(max-min))*10
    
    return nota

nota = calculate_punctuation(9,7,2)
print(f'A nota do aluno é {nota}!')