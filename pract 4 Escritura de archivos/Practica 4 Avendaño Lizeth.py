#Codificador Decodificador
import os

if os.path.exists:
    archivo = open("cancionfavorita.txt", "r")
    msj = archivo.read(1)
    cancioncodi = open("cancionfavoritacodificada.txt", "w")
    abc = "abcdefghijklmnñopqrstuvwxyz"
    cifrado = ""
    archivo.seek(0)
    while msj != "":
        msj = archivo.read(1)
        for Letra in msj:
            if Letra in abc:
                suma = abc.find(Letra)
                suma += 1
                if suma <= 27:
                    suma -= 27
                    cifrado += abc[suma]
            else:
                cifrado += Letra
    cancioncodi.write(cifrado)
    cancioncodi.close()
    archivo.close()
else:
    print("No existe el archivo")

if os.path.exists:
    archivo = open("cancionfavoritacodificada.txt", "r")
    msj = archivo.read(1)
    canciondecodi = open("cancionfavoritadecodificada.txt", "w")
    abc = "abcdefghijklmnñopqrstuvwxyz"
    descifrado = ""
    archivo.seek(0)
    while msj != "":
        msj = archivo.read(1)
        for Letra in msj:
            if Letra in abc:
                suma = abc.find(Letra)
                suma -= 1
                if suma >= 0:
                    suma -= 27
                    descifrado += abc[suma]
            else:
                descifrado += Letra
    canciondecodi.write(descifrado)
    canciondecodi.close()
    archivo.close()
else:
    print("No existe el archivo")
