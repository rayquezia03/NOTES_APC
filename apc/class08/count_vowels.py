def count_vowels(texto):
    vogais = "aeiouAEIOU"  
    contagem = {}  

    for letra in texto:
        if letra in vogais:
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1
    
    return contagem

texto = input("Type a text: ")
resultado = count_vowels(texto)

print(resultado)
# print("Contagem de vogais: ")
# for vogal, quantidade in resultado.items():
#     print(f"{vogal}: {quantidade}")
