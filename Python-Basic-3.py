AltoElegido= int(input("Ingrese un valor de alto para la estructura: "))
AnchoElegido= int(input("Ingrese un valor para el ancho de la estructura: "))
CaracterElegido= str(input("Ingrese un unico caracter para la estructura: "))
def pintame(alto, ancho, caracter):
    for i in range(alto):
            print(ancho * caracter)

pintame(AltoElegido, AnchoElegido, CaracterElegido)