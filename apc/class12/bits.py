def calcularNotas(valor):
    cinquenta = valor // 50
    valor = valor % 50
    dez = valor // 10
    valor = valor % 10
    cinco  = valor // 5
    valor = valor % 5
    um = valor 
    return str(cinquenta) + ' ' + str(dez)+ ' ' + str(cinco) + ' ' +str(um) + '\n\n'

arquivo = open('bits.txt','r')
arq_escrita = open('saida_bits.txt','w')

linhas_escrita = ''
i = 1

for linha in arquivo.readlines():
    valor = int(linha.replace('\n',''))
    if valor == 0:
        pass
    else:
        notas = calcularNotas(valor)
        linhas_escrita += 'Teste '+ str(i) + '\n'
        linhas_escrita += notas
        i += 1

arq_escrita.write(linhas_escrita)
arquivo.close()
arq_escrita.close()