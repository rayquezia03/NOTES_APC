tabuleiro = [
   [ 'X','X','O'],
   [ 'X','X','O'],
   [ 'O','O','X']
]

'''
Veirificar linhas
verificar colunas
verificar diagonais
'''
def verificar_ganhador(matriz):
    ganhador = None
    #VERIFICAR LINHAS
    for linha in matriz:
        if linha.count('X') == 3:
            ganhador = 'X'
        elif linha.count('O') == 3:
            ganhador = 'O'
        
    #VERIFICAR COLUNAS
    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna]:
            if matriz[0][coluna] =='X':
                ganhador = 'X'
            elif matriz[0][coluna] =='O':
                ganhador = 'O'
            
    #VERIFICA DIAGONAIS
    '''
    0,0
    1,1
    2,2
    
    0,2
    1,1
    2,0
    '''
    
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == 'X':
            ganhador = 'X'
        elif matriz[0][0] == 'O':
            ganhador = 'O'
    
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
         if matriz[0][2] == 'X':
            ganhador = 'X'
         elif matriz[0][2] == 'O':
            ganhador = 'O'
        
    # return ganhador

    if ganhador == 'X':
        return 'X'
    elif ganhador == 'O':
        return 'O'
    else:
        return 'EMPATE!'  
    
resultado = verificar_ganhador(tabuleiro)
print(resultado)