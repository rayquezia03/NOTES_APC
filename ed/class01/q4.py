def soma_maxima(conjunto):
    if len(conjunto) < 2:
        return "O conjunto precisa ter pelo menos dois elementos para encontrar a soma máxima."
    
    # Ordena o conjunto em ordem decrescente
    conjunto_ordenado = sorted(conjunto, reverse=True)
    
    # A soma máxima será a soma dos dois primeiros elementos do conjunto ordenado
    soma_max = conjunto_ordenado[0] + conjunto_ordenado[1]
    
    return soma_max

# Exemplo de uso:
conjunto_exemplo = {5, 12, 9, 20, 3}
resultado = soma_maxima(conjunto_exemplo)
print(f"A soma máxima entre dois elementos do conjunto é: {resultado}")