#Practica 1 POO Operaciones numeros complejos
class Ncomplex:
    #atributos
    Preal = 0
    Pima = 0
    def __init__( self ,real, ima):
        #contructor
        self.Preal = real
        self.Pima = ima

    def imprimir(self):
        if (self.Pima >= 0 ):
            print("El resultado es: " + str(self.Preal) + " + " + str(self.Pima) + " i\n")
        else:
            print("El resultado es: " + str(self.Preal) + str(self.Pima) + " i\n")

    #setter
    def setReal(self, real):
        self.Preal = real

    def setPima(self, ima):
        self.Pima = ima

    # getters
    def getReal(self):
        return self.Preal

    def getPima(self):
        return self.Pima


def opsuma(X,Y):
    A = X.getReal() + Y.getReal()
    B = X.getPima() + Y.getPima()
    Nuevo = Ncomplex(A, B)
    Nuevo.imprimir()

def opresta(X,Y):
    A = X.getReal() - Y.getReal()
    B = X.getPima() - Y.getPima()
    Nuevo = Ncomplex(A, B)
    Nuevo.imprimir()

def opmultiplicacion(X,Y):
    A = X.getReal() * Y.getReal()
    B = X.getPima() * Y.getPima()
    C = A-B
    W = X.getReal() * Y.getPima()
    Z = X.getPima() * Y.getReal()
    D = W + Z
    Nuevo = Ncomplex(C, D)
    Nuevo.imprimir()

X = Ncomplex(5, 3)
Y = Ncomplex(5, -3)
opsuma(X,Y)
opresta(X,Y)
opmultiplicacion(X,Y)
