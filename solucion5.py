n = int(input("ingresar numero: "))
c= 0
r=0
while c <=9:
    aux = n
    fd= 0
    while aux > 0:
        r = aux %10
        if r==c:
            fd =fd+1
        aux = (aux-r)/10
    if fd>0:
        print(f"la frecuencia de {c} es {fd}")
    c=c+1