#codificador Cesar letras minusculas a 1
archivo = open("cancionfavorita.txt", "r")
msj = archivo.read(1)
abc = "abcdefghijklmnñopqrstuvwxyz"
clave = 1
cifrado = ""
archivo.seek(0)
while msj != "":
    msj = archivo.read(1)
    for Letra in msj:
        if Letra in abc:
            suma = abc.find(Letra)
            suma += clave
            if suma <= 27:
                suma -= 27
                cifrado += abc[suma]
        else:
            cifrado += Letra

print(cifrado)
archivo.close()
