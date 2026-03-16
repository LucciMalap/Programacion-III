lista1= [1,2,3,4]
lista2= [8,12,9,45]
def buscador(lista, valor):
    for i in lista:
        if i == valor:
            print(lista.index(i))
buscador(lista1, 3)
buscador(lista2, 12)