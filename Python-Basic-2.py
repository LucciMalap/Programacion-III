
def EsBisiesto():
    year = int(input("Ingrese un numero de año: "))
    print(year % 4 == 0 or year % 400 == 0 and year % 100 != 0)

EsBisiesto()