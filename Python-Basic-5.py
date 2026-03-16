palabrita= str(input("Escribe una palabra para saber si es o no un palindromo: "))
def EsCapicua(palabra):
    print(palabra[::-1] == palabra)

EsCapicua(palabrita)