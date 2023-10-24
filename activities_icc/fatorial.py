#função que calcula fatorial de forma interativa
def fatorial_interativo(number):
    
    fatorial = 1
    n = number

    for i in range(1,1+n):
        fatorial = fatorial * i
        
    return fatorial
 
#função que calcula o fatorial de forma recursiva   
def fatorial_recursivo(number):
 
    n = number
    
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n-1)

#função de inicialização que chama as duas funções anteriores: Interativa e Recursiva
def initializer(name,numero):
    
    numero = int(input('Digite o número que você deseja calcular o fatorial: '))

    result_interativo = fatorial_interativo(numero)
    result_recursivo = fatorial_recursivo(numero)
    
    return print(f'Seja bem-vindo {name}! voce escolheu o numero {numero}.\n Obtendo o resultado interativo: {result_interativo}; \n Obtendo o resultado recursivo: {result_recursivo}')
    

initializer('ray',6)
'''
CHAMADAS DE TESTE:

initializer('ray',6)
initializer('juliana',3)
initializer('louise',8)
'''