path = 'notas.txt'

arquivo = open(path,'r')

texto = arquivo.read()
arquivo.close()

notas = texto.split("\n")

print(f'A quantiade de notas fornecidas foi de: {len(notas)}')
#verificações
print('Notas na ordem em que foram informadas:')
sum = 0
for nota in notas:
    sum += int(nota)
    print(nota)
    
print(f'A soma das notas é: {sum}')
print(f'A médias das notas é: {sum/len(notas)}')
print(f'A soma das notas é: {sum}')
media = sum/len(notas)

count = 0
for nota in notas:
    if int(nota) > media:
        count+=1

print(f'Dentre as notas fornecidas, {count} são acima da média!')

