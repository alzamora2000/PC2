numIngresados = []
numPares = 0
numImpares = 0
#print("Desea ingresar numeros")
#respuesta = input()
while True:
    #print("Desea ingresar otro numero?")
    respuesta = input("desea agregar un numero?\n -> respuesta: ").lower()
    if respuesta == "no":
        print("finalizando programa...")
        break
    
    elif respuesta == "si":
        numIngresadoTeclado = int(input("Ingrese el numero: "))
        #numIngresados.append(numIngresadoTeclado)
        #numIngresados
        if numIngresadoTeclado%2 == 0:
            numIngresados.append(numIngresadoTeclado)
            numIngresados
            numPares = numPares+1
            numImpares = 0
            print(numIngresados)
            print(f"la cantidad de numeros pares es {numPares} y numeros impares es {numImpares}")
        else:
            numPares = 0
            numImpares = numImpares+1
            print(numIngresados)
            print(f"la cantidad de numeros pares es {numPares} y numeros impares es {numImpares}")
print(numIngresados)
