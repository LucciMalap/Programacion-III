NumeroElegido= int(input("Ingrese un numero para saber si es o no step: "))
def EsStep(numero):
    strNum = str(numero)
    for i in range(len(strNum)-1):
        diferencia = int(strNum[i]) - int(strNum[i+1])
        if diferencia != 1 and diferencia != -1:
            return False
    return True
print(EsStep(NumeroElegido))
