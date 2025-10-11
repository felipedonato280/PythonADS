import random

def fatorial (n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)
    
resp = fatorial(random.randint(1, 10000))
print(resp)