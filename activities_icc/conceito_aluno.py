def initializer(name):
    print(f'Seja bem-vindo {name}!')
     
def calculate_medias(name,ab1,ab2):
    
    #call da func de boas vindas!
    initializer(name)
    
    conceito = None
    realized_reav = False
    
    notas = [ab1,ab2]
    media_inicial = (notas[0]+notas[1])/2
       
    
    #chamada para realização da REPOSIÇÃO da menor nota entre as AB1 e AB2
    if realized_reav != True:
        for nota in notas:
            if nota < 7:    
                reav_nota = float(input('Digite a nota da reavalição para substituição da menor nota!'))
                realized_reav = True
                notas = reavaliacao(notas,reav_nota)
                media_inicial = (notas[0]+notas[1])/2 
                break                
            
    if media_inicial >= 7:
        #APROVADO!
        conceito = 'AP'
        
    elif media_inicial < 5:
        #REPROVADO!
        conceito = 'RP'
        
    elif media_inicial >= 5 and media_inicial < 7:
        #DIREITO DE REALIZAR A FINAL!
        result_final = final_avaliation(media_inicial)
        
        if result_final == True:
            conceito = 'AF'
        else:
            conceito = 'RF'
        
    return print(conceito)
    
def reavaliacao(notas,reavaliacao_nota):
    
    menor_nota = notas[0]
    for nota in notas:  
        #verificação da menor nota
        if nota < menor_nota:
            menor_nota = nota
            
    #fluxo de substituição da menor nota:
    index_subs_nota = notas.index(menor_nota)
    
    #antes de subst. verifico se a nota da reavaliação foi maior que a menor nota
    if reavaliacao_nota >= menor_nota:
        notas[index_subs_nota] = reavaliacao_nota
        
    return notas

def final_avaliation(media):
    nota_avaliacao_final = float(input('Digite a nota da avaliação FINAL: '))
        
    media_ponderada = (media*6 + nota_avaliacao_final*4)/10
    
    if media_ponderada >= 5.5:
        return True
    else:
        return False
   
'''
TESTES:
 
calculate_medias('Ray',9,10)   
calculate_medias('Bob',5,4)
calculate_medias('Ana',7,7)
'''