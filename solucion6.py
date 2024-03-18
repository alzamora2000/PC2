from math import sqrt
def F(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

def Fibonacci(numInicio, numFin):
    n = 0
    cur = F(n)
    while cur <= numFin:
        if numInicio <= cur:
            print(cur)
        n += 1
        cur = F(n)

print("La serie de Fibonacci entre 0 y 50 es:\n")
Fibonacci(1, 50)