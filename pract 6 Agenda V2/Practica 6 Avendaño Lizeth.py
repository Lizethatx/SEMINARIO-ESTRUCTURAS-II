#Agenda V2
import os.path

class Alumno:
    codigo = 0
    nombre = ""
    carrera = ""

    def __init__(self):
        self.__codigo = 0
        self.__nombre = ""
        self.__carrera = ""

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    def __str__(self):
        return "codigo: " + str(self.__codigo) + " |nombre: " + self.__nombre + " |carrera: " + self.__carrera

    def reiniciar(self):
        return str(self.__codigo) + "|" + self.__nombre + "|" + self.__carrera + "\n"

class Agenda:

    def __init__(self):
        self.__listaAlumnos = []

    @property
    def listaAlumnos(self):
        return self.__listaAlumnos

    @listaAlumnos.setter
    def listaAlumnos(self, listaAlumnos):
        self.__listaAlumnos = listaAlumnos

    def guardar(self):
        archivo = open("agendav2.txt", "w")
        for alumno in self.__listaAlumnos:
            archivo.writelines(alumno.reiniciar())
        archivo.close()

    def cargar(self):
        if os.path.exists("agendav2.txt"):
            archivo = open("agendav2.txt", "r")
            for linea in archivo:
                alumno = Alumno()
                aux = linea.split("|")
                alumno.codigo = int(aux[0])
                alumno.nombre = aux[1]
                if aux[2][-1:] == "\n":
                    alumno.carrera = aux[2][:-1]
                else:
                    alumno.carrera = aux[2]
                self.__listaAlumnos.append(alumno)
            archivo.close()

    def anadirAlumno(self):
        alumno = Alumno()
        alumno.codigo = int(input("Ingrese el código: "))
        alumno.nombre = input("Ingrese el nombre: ")
        alumno.carrera = input("Ingrese la carrera: ")
        self.__listaAlumnos.append(alumno)
        archivo = open("agendav2.txt", "a")
        archivo.writelines(alumno.reiniciar())
        archivo.close()
        print("  Alumno agregado con éxito")

    def buscarAlumnoCodigo(self):
        busqueda = input("Ingrese el código del alumno: ")
        for alumno in self.__listaAlumnos:
            if int(busqueda) == alumno.codigo:
                print("Los datos del alumno son:")
                print(alumno)
                return
        print("El alumno no existe")

    def buscarAlumnoNombre(self):
        busqueda = input("Ingrese el nombre del alumno: ")
        for alumno in self.__listaAlumnos:
            if busqueda == alumno.nombre:
                print("Los datos del alumno son:")
                print(alumno
                      )
                return
        print("El alumno no existe")

    def eliminarAlumno(self):
        auxi = int(input("¿Esta seguro de eliminar un estudiante? (1.si) (2.No): "))
        if auxi == 1:
            codigo = int(input("Ingrese el código del alumno a eliminar:\n"))
            for alumno in self.__listaAlumnos:
                if codigo == alumno.codigo:
                    self.__listaAlumnos.remove(alumno)
                    self.guardar()
                    print("Alumno eliminado")
                    return
            print("El alumno no existe")
        else:
            print("Regresando al menu principal")

    def mostrarAlumnos(self):
        for alumno in self.__listaAlumnos:
            print(alumno)

def menu():
    agenda = Agenda()
    agenda.cargar()
    opc = int(input("\nMenu Principal\n1. Añadir Alumno\n2. Buscar Alumno\n3. Eliminar alumno\n"
                    "4. Mostar Alumnos\n0. Salir\n Elige una opcion: "))
    while opc != 0:

        if opc == 1:
            agenda.anadirAlumno()
        elif opc == 2:
            opc2 = int(input("1 Buscar por codigo\n2. Buscar por nombre\n0 Salir\n"))
            while opc2 != 0:
                if opc2 == 1:
                    agenda.buscarAlumnoCodigo()
                elif opc2 == 2:
                    agenda.buscarAlumnoNombre()
                opc2 = int(input("1 Buscar por codigo\n2. Buscar por nombre\n0 Salir\n"))
        elif opc == 3:
            agenda.eliminarAlumno()
        elif opc == 4:
            agenda.mostrarAlumnos()
        else:
            print("Opcion invalida ")

        opc = int(input("\nMenu Principal\n1. Añadir Alumno\n2. Buscar Alumno\n3. Eliminar alumno\n"
                        "4. Mostar Alumnos\n0. Salir\n Elige una opcion: "))

menu()
