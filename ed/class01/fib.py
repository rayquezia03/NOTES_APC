def fib(n):
    if n == 0 or n ==1:
        return 1
    else:
       return fib(n-1) + fib(n-2)
    
print(fib(4))

# 0 1 1 2 3 5 8 13 21 34