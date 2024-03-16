def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
n=int(input("Escribe un númemro entero para hallar su factorial : "))
print(factorial(n))