alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

frase = 'rayane'
letra_cifrada = ''
i = 0

for letra in frase:
    print('====================')
    print(letra)
    while (i < len(alfabeto)-1) and letra != alfabeto[i]:
        i +=1
        print('--------------------------')
        print(alfabeto[i])
        if letra == alfabeto[i]:
            print('BINGO')
            letra_cifrada += alfabeto[i+3]
            
    # aqui, ao finalizar a palavra zero a variável como estratégia para romper o loop
    i = 0
                        
print('cifra: ',letra_cifrada)