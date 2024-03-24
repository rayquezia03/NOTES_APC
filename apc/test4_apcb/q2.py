path = 'q2.txt'

arquivo = open(path)

b = arquivo.read()

formated_text = b.split("''")
# print(formated_text)

letras_count = {'a':0}
count = 0

alfabeto = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

letra_mais_recorrente = 0
count_total_letras = 0

for key in alfabeto:
   for chave in key:
       # letras p fazer a contagem
        for letra in formated_text:
            for a in letra:
                if a == ' ':
                    continue
                else:
                    if a == chave:
                        count_total_letras +=1
                        # print(a ,'==',chave)
                        alfabeto[chave] = (alfabeto[chave])+1


        if alfabeto[chave] > letra_mais_recorrente:
            letra_mais_recorrente = alfabeto[chave]
        
            print(f'A letra {chave} foi a mais recorrente!')
arquivo.close()
percentage =round(letra_mais_recorrente/count_total_letras*100,2)
print(f'A porcentagem de ocorrencia da letra {chave} é de {percentage} %')