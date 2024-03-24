def determinar_vencedor(matriz):
    # Verificar linhas
    for linha in matriz:
        if linha.count('X') == 3:
            print(linha.count('X'))
            return 'X'
        elif linha.count('O') == 3:
            print(linha.count('O'))
            return 'O'

    # Verificar colunas
    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna]:
            if matriz[0][coluna] == 'X':
                return 'X'
            elif matriz[0][coluna] == 'O':
                return 'O'

    # Verificar diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[1][1] == 'X':
            return 'X'
        elif matriz[1][1] == 'O':
            return 'O'

    # Se não houver vencedor
    return None

# Exemplo de uso:
tabuleiro = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', 'X', 'O']
]

vencedor = determinar_vencedor(tabuleiro)
if vencedor:
    print(f'O jogador {vencedor} venceu!')
else:
    print('O jogo terminou em empate ou ainda não foi concluído.')
 
'''
COMBINAÇÕES POSSÍVEIS DE VITORIA

1 - PEGAR LINHAS VERTICAIS E HORIZONTAIS


2 - PEGAR DIAGONAIS: 
    DIAGONAL: QUANDO J == I 

0,0
1,1
2,2

OU 

0,2
1,1
2,0

'''

def create_matriz(linhas,colunas,x):
    matriz = [x]*linhas
    
    for i in range(linhas):
        matriz[i] = [x]*colunas
        
    return matriz

a = create_matriz(3,3,0)

for linha in a:
    print(linha)