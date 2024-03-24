'''
Implemente uma função recursiva que, dados dois
números inteiros x e n, calcule o valor de x.n
'''

def multp(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x + multp(x,n-1)
    
x = 2
n = 5

print(multp(x,n))
 
#  2*5 = 2+2+2+2+2