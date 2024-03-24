'''
Implemente uma função recursiva que, dados dois
números inteiros x e n, calcule o valor de x^n
'''

def expon(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * expon(x,n-1)
    
x = 2
n = 5

print(expon(x,n))
 
#  2² = 2*2