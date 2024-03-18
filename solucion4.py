respuesta = int(input("Ingrese un resultado válido:\n 0.Salir \n 1.Ingresar datos de un alumno \n -> "))
#nombre = input("Ingrese el nombre del alumno: ")
#edad = int(input("Ingrese la edad del alumno: "))
#profesion = input("Ingrese su profesion del alumno: ")
#idiomas1 = input("Ingrese los idiomas que sabe: ")
#idiomas=[]
#idiomas.append(idiomas1)

while respuesta == 1:
    nomAlumno = input("Ingrese nombres del alumno: ")
    notasAlumno1 = int(input("Ingrese la nota del examen 1: "))
    notasAlumno2 = int(input("Ingrese la nota del examen 2: "))
    notasAlumno3 = int(input("Ingrese la nota del examen 3: "))

    notasTotal=[notasAlumno1,notasAlumno2,notasAlumno3]

    datos2 = {"NOMBRE DEL ALUMNO": nomAlumno,
        "NOTAS DEL ALUMNO": notasTotal}
    print (datos2)

    respuesta2 = int(input("Desea agregar otro alumno más? \n1.si\n0.no\n-> "))

    if respuesta2 ==0:
        print("programa terminado...")
        break
        nomAlumno = input("Ingrese nombres del alumno: ")
        #notas1=[]
        #notas2=[]
        #notas3=[]
        
        notasAlumno1 = int(input("Ingrese la nota del examen 1: "))
        notasAlumno2 = int(input("Ingrese la nota del examen 2: "))
        notasAlumno3 = int(input("Ingrese la nota del examen 3: "))
        notasTotal=[notasAlumno1,notasAlumno2,notasAlumno3]
        
        #notas1.append(notasAlumno1)
        #notas2.append(notasAlumno2)
        #notas3.append(notasAlumno2)
        #notasTotal.extend(notas1,notas2,notas3)

        datos2 = {"NOMBRE DEL ALUMNO": nomAlumno,
        "NOTAS DEL ALUMNO": notasTotal}
        print (datos2)
        respuesta2 = int(input("Desea agregar otro alumno más? \n1.si\n0.no\n"))
    if respuesta2 == 1:
        nomAlumno = input("Ingrese nombres del alumno: ")
        notasAlumno1 = int(input("Ingrese la nota del examen 1: "))
        notasAlumno2 = int(input("Ingrese la nota del examen 2: "))
        notasAlumno3 = int(input("Ingrese la nota del examen 3: "))
        notasTotal=[notasAlumno1,notasAlumno2,notasAlumno3]
        datos2 = {"NOMBRE DEL ALUMNO": nomAlumno,
        "NOTAS DEL ALUMNO": notasTotal}
        print (datos2)
        respuesta2 = int(input("Desea agregar otro alumno más? \n1.si\n0.no\n"))

        #print("¿DESEA AGREGAR OTRO? \n 1.SI\n2.no")
        
        #notasTotal=[notasAlumno1,notasAlumno2,notasAlumno3]
        #datos2 = {"NOMBRE DEL ALUMNO": nomAlumno,
        #"NOTAS DEL ALUMNO": notasTotal}
        #print (datos2)
    else:
        print("numero errado")
if respuesta ==0:
    
    print("No se ingresó ningún dato, saliendo del programa...")
    datosVacio = {"Nombre": "",
        "Examen 1": "",
        "Examen 2": "",
        "Examen 3": ""}
    print(datosVacio)
        
#print("opcion invalida")
    

#datos2 = {"Nombre": nomAlumno,
#          "Examen 1": notasAlumno1,
#          "Examen 2": notasAlumno2,
#          "Examen 3": notasAlumno3}


#print(datos2)