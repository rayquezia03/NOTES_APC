def fatorial(value):
    if value == 1 or value == 0:
        return 1
    else:
        return value * fatorial(value-1)
    
value = 5

print(fatorial(value))