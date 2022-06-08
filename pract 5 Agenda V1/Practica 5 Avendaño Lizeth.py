#Agenda v1
import os
import os.path

def agregar():
    if (not os.path.exists("agendav1.txt")):
        # cuando no existe el archivo
        archivo = open("agendav1.txt", "w")
        archivoRespaldo = open("agendaRespaldo.txt", "w")

        codigo = input("\nIngrese el codigo:")
        nombre = input("Ingrese el nombre:")
        carrera = input("Ingrese la carrera:")

        archivo.write(codigo + "\n")
        archivo.write(nombre + "\n")
        archivo.write(carrera + "\n\n")

        archivoRespaldo.write(codigo + "\n")
        archivoRespaldo.write(nombre + "\n")
        archivoRespaldo.write(carrera + "\n\n")

        archivo.close()
        archivoRespaldo.close()
        print("\nInformacion guardada con éxito")
    else:
        # cuando ya existe el archivo
        archivo = open("agendav1.txt", "w")
        archivoRespaldo = open("agendaRespaldo.txt", "r")

        # Copiar toda la informacion del archivo de respaldo al original
        for linea in archivoRespaldo:
            archivo.write(linea)
        archivoRespaldo.close()

        # le agrego la informacion al original
        codigo = input("\nIngrese el codigo:")
        nombre = input("Ingrese el nombre:")
        carrera = input("Ingrese la carrera:")

        archivo.write(codigo + "\n")
        archivo.write(nombre + "\n")
        archivo.write(carrera + "\n\n")
        archivo.close()

        #Copiar informacion del original al de respaldo y cerrar archivos
        archivo = open("agendav1.txt", "r")
        archivoRespaldo = open("agendaRespaldo.txt", "w")
        for linea in archivo:
            archivoRespaldo.write(linea)

        archivo.close()
        archivoRespaldo.close()
        print("\nInformacion guardada con éxito")

def mostrar():
    if (os.path.exists("agendav1.txt")):
        archivo = open("agendav1.txt", 'r')
        linea = archivo.read(1)
        while linea != "":
            print(linea, end='')
            linea = archivo.read(1)
        archivo.close()
    else:
        print("\nNo existe agenda por favor ingrese datos")

def menu():
    opcion = int(input("Menu de agenda\n1. Agregar información de alumno\n2. Mostrar agenda\n0. Salir\n Elige una opcion: "))

    while opcion != 0:
        if opcion == 1:
            agregar()
        elif opcion == 2:
            mostrar()
        elif opcion == 0:
            pass
        else:
            print("Opción no válida.")
        opcion = int(input("\nMenu de agenda\n1. Añadir alumno\n2. Mostrar agenda\n0. Salir\n Elige una opcion: "))

menu()
