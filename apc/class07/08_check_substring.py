# def substring(palavra_a,palavra_b):
#     resultado = 'não'
#     if palavra_b in palavra_a:
#         resultado = 'sim'
#         return resultado
#     return resultado

# palavra_a = (input('Digite uma palavra-A: '))
# palavra_b = (input('Digite uma palavra-B: '))

# print(substring(palavra_a,palavra_b))

def substring(palavra_a,palavra_b):
    i = 0
    j = 0
    subs = False
    while j < len(palavra_a) and i < len(palavra_b):
        if palavra_a[i] == palavra_b[j]:
            j +=1
        else:
            if j > 0:
                j = 0
            else:
                i +=1
    if j == len(palavra_b):
        subs = True
    elif i == len(palavra_a):
        subs = True
        return subs
    return subs
substring('abora','bora')