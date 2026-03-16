year = int(input("Ingrese un numero de año: "))
def EsBisiesto(year):
    print(year % 4 == 0 or year % 400 == 0 and year % 100 != 0)

EsBisiesto(year)