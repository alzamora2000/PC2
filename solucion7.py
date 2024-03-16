def numeroPrimo(n1):
    i=1
    divisores=0
    primo=True
    while(i<=n1):
        if(n1%i==0):
            i=i+1
            divisores=divisores+1
        else:
            i=i+1
    if(divisores==2):
        primo==True
        return(primo)
    else:
        return(primo==False)
    
respuesta = int(input("Ingrese un numero para determinar si es primo o no:\n-> "))
print(numeroPrimo(respuesta))