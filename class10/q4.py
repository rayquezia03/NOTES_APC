path = 'temperaturas.txt'

arquivo = open(path,'r')

texto = arquivo.read()
arquivo.close()

att = texto.split("\n")

usuarios = {}
for linha in att:
    
    nw = linha.split(', ')

    usuarios[nw[0]] = nw[1]

months = []
month_keys = usuarios.keys()
for mt in month_keys:
    months.append(mt)

media_anual = 0
for mes in months:  
    media_anual += int(usuarios[mes])
media_anual = media_anual/12
print(media_anual)
    
meses_acima_da_media = []
for mes in months: 
    if int(usuarios[mes]) > media_anual:
        meses_acima_da_media.append(mes)
        print(f'No mês de {mes}, a media de temp foi acima da media anual, e portanto foi de {usuarios[mes]}')

count = 1
for mes in meses_acima_da_media:
    print(f'{count} - {mes}')
    count +=1