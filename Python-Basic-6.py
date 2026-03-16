palabrita= str(input("Escribe una frase para contar sus vocales: "))
def AContarVocales(palabra):
    n= 0
    vocales= ["a","e","i","o","u"]
    for i in palabra:
        if i in vocales:
            n += 1
    print(f"{palabra} tiene {n} vocales.")

AContarVocales(palabrita)