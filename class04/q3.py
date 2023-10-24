# count = 0
# array = []
# ordenation = []

# while count < 3:
#     number = int(input('digite um numero'))
#     count +=1;
#     array.append(number)
#     array.sort(reverse=True)
    
# print(array)

#===============================================
    
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# numero3 = int(input("Digite o terceiro número: "))

# if numero1 > numero2:
#     numero1, numero2 = numero2, numero1

# if numero1 > numero3:
#     numero1, numero3 = numero3, numero1

# if numero2 > numero3:
#     numero2, numero3 = numero3, numero2

# print("Números em ordem crescente:", numero1, numero2, numero3)


#===============================================

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 <= num2 <= num3:
    menor = num1
    meio = num2
    maior = num3
elif num1 <= num3 <= num2:
    menor = num1
    meio = num3
    maior = num2
elif num2 <= num1 <= num3:
    menor = num2
    meio = num1
    maior = num3
elif num2 <= num3 <= num1:
    menor = num2
    meio = num3
    maior = num1
elif num3 <= num1 <= num2:
    menor = num3
    meio = num1
    maior = num2
else:
    menor = num3
    meio = num2
    maior = num1

print("Números ordenados em ordem crescente:", menor, meio, maior)

#===============================================================

primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))
terceiro = int(input("Digite o terceiro valor: "))

if primeiro > segundo:
    (primeiro,segundo) = (segundo,primeiro) #toca os valores

if primeiro > terceiro:
    (primeiro,terceiro) = (terceiro,primeiro)

if segundo > terceiro:
    (segundo,terceiro) = (terceiro,segundo)

print(primeiro,segundo,terceiro)


    