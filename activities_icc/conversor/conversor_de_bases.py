def converter_para_base10(numero, base_origem):
    
    #se o valor for decimal, converto para decimal_value e retorno o proprio numero
    if base_origem == 10:
        return float(numero) if '.' in numero else int(numero)
    
    #digitos que abrangem até a base 36
    caractere = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decimal_value = 0
    
    #iterar sobre cada caractere da base de origem
    for i, digito in enumerate(reversed(numero)):
        
        #o índice na lista de caracteres multiplicado pelo valor da base original à potencia i
        decimal_value += caractere.index(digito.upper()) * (base_origem ** i)
        
        '''
        100110
        
        0*2⁰+1*2¹+1*2²+0*2³+0*2⁴+1*2⁵ = 2+4+32 = 38
        '''
    
    return decimal_value

def converter_da_base10(numero, base_destino):
    if base_destino == 10:
        return str(numero)
    
    caractere = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    numero = int(numero)
    
    while numero > 0:
        resto = numero % base_destino
        #string incremental que busca na lista caractere o valor associado ào indice 'resto'
        result = caractere[resto] + result
        numero //= base_destino
        
        '''
        Exemplo:
        38/2 = 0
        19/2 = 1
        9/2 = 1
        4/2 = 0
        2/2 = 0
        1/2 = 1
        '''
    
    return result

def converter_base(numero, base_origem, base_destino):
    if '.' in numero:
        parte_inteira, parte_decimal = numero.split('.')
        parte_inteira_base10 = converter_para_base10(parte_inteira, base_origem)
        parte_decimal_base10 = converter_para_base10(parte_decimal, base_origem) / (base_origem ** len(parte_decimal))
        resultado_base10 = parte_inteira_base10 + parte_decimal_base10
    else:
        resultado_base10 = converter_para_base10(numero, base_origem)
    
    resultado_base_destino = converter_da_base10(resultado_base10, base_destino)
    
    return resultado_base_destino

print('=================================================')
print('Seja bem vindo (a) ao conversor de bases numéricas!')

base_origem = int(input("Digite a base de origem (2 a 36): "))
numero = input(f"Digite o número na base {base_origem}: ")
base_destino = int(input("Digite a base de destino (2 a 36): "))

resultado = converter_base(numero, base_origem, base_destino)

print(f"O número '{numero}' na base {base_origem} é equivalente a '{resultado}' na base {base_destino}.")
