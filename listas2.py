#Encoding: UTF-8
#Autor: Alberto López Reyes
#Descripción: Imprime los resultados de las siguientes funciones de acuerdo a las listas que estas tengan de entrada.

def discriminarImpares(lstListaCompleta):
    lstListaPares = []
    for intNIndex in range(0, len(lstListaCompleta)):
        if lstListaCompleta[intNIndex] % 2 == 0:
            lstListaPares.append(lstListaCompleta[intNIndex])
    return lstListaPares

def integrarMayoresAPrevio(lstListaCompleta):
    lstListaMayoresAPrevio = []
    for intNIndex in range(1, len(lstListaCompleta)):
        if lstListaCompleta[intNIndex] > lstListaCompleta[intNIndex-1]:
            lstListaMayoresAPrevio.append(lstListaCompleta[intNIndex])
    return lstListaMayoresAPrevio

def intercambiarPosicionPorPares(lstListaCompleta):
    lstListaIntercambiadaPorPares = []
    for intNPar in range(0, len(lstListaCompleta)//2):
        lstListaIntercambiadaPorPares.append(lstListaCompleta[intNPar*2+1])
        lstListaIntercambiadaPorPares.append(lstListaCompleta[intNPar*2])
    if len(lstListaCompleta) % 2 != 0:
        lstListaIntercambiadaPorPares.append(lstListaCompleta[len(lstListaCompleta)-1])
    return lstListaIntercambiadaPorPares

def intercambiarMayoryMenor(lstListaCompleta):
    while len(lstListaCompleta) > 1:
        lstListaMayorMenorIntercambiada = lstListaCompleta
        intMayor = max(lstListaCompleta)
        intIndexMayor = lstListaCompleta.index(intMayor)
        intMenor = min(lstListaCompleta)
        intIndexMenor = lstListaCompleta.index(intMenor)
        lstListaMayorMenorIntercambiada.remove(intMayor)
        lstListaMayorMenorIntercambiada.remove(intMenor)
        lstListaMayorMenorIntercambiada.insert(intIndexMenor, intMayor)
        lstListaMayorMenorIntercambiada.insert(intIndexMayor, intMenor)
        return lstListaMayorMenorIntercambiada
    return lstListaCompleta

def esMayorIgualAlPromedio(lstListaCompleta):
    intMayoresIguales = 0
    if len(lstListaCompleta) != 0:
        intPromedioLista = sum(lstListaCompleta)/len(lstListaCompleta)
        for intNIndex in range(0, len(lstListaCompleta)):
            if lstListaCompleta[intNIndex] - intPromedioLista >= 0:
                intMayoresIguales = intMayoresIguales + 1
    else:
        intMayoresIguales = 0
    return intMayoresIguales

def calcularMediaDesviacion(lstListaCompleta):
    while len(lstListaCompleta) <= 1:
        return (0, 0)
    fltMedia = sum(lstListaCompleta)/len(lstListaCompleta)
    fltSigmaDesviacion = 0
    for intNIndex in range (0, len(lstListaCompleta)):
        fltSigmaDesviacion = fltSigmaDesviacion + (lstListaCompleta[intNIndex] - fltMedia)**2
    fltDesviacion = (fltSigmaDesviacion/(len(lstListaCompleta)-1))**.5
    return (fltMedia, fltDesviacion)

def main():
    print("Problema 1. Se regresa una lista con los valores pares de la losta original.")
    lstLista = [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [5, 7, 3], []]
    for intNIndex in range (0, len(lstLista)):
        print("Con la lista "+str(lstLista[intNIndex])+", regresa "+str(discriminarImpares(lstLista[intNIndex])))

    print("Problema 2. Se regresa una lista con los valores mayores a uno previo.")
    lstLista = [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [5, 4, 3, 2], []]
    for intNIndex in range(0, len(lstLista)):
        print("Con la lista " + str(lstLista[intNIndex]) + ", regresa " + str(integrarMayoresAPrevio(lstLista[intNIndex])))

    print("Problema 3. Se regresa una lista con los valores intercambiados por pareja.")
    lstLista = [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [1, 2, 3], [7]]
    for intNIndex in range(0, len(lstLista)):
        print("Con la lista " + str(lstLista[intNIndex]) + ", regresa " + str(intercambiarPosicionPorPares(lstLista[intNIndex])))

    print("Problema 4. Se regresa una nueva lista con el valor menor y mayor intercambiados.")
    lstLista = [[5, 9, 3, 22, 19, 31, 10, 7], [1, 2, 3], []]
    for intNIndex in range(0, len(lstLista)):
        print("Con la lista " + str(lstLista[intNIndex]) + ", regresa " + str(intercambiarMayoryMenor(lstLista[intNIndex])))

    print("Problema 5. Se regresa el número de valores mayores o iguales al promedio de la lista.")
    lstLista = [[70, 80, 90], [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85], []]
    for intNIndex in range(0, len(lstLista)):
        print("Con la lista " + str(lstLista[intNIndex]) + ", regresa " + str(esMayorIgualAlPromedio(lstLista[intNIndex])))

    print("Problema 6. Se regresa una dupla con la media y la desviación estándar de la lista.")
    lstLista = [[1, 2, 3, 4, 5, 6], [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85], []]
    for intNIndex in range(0, len(lstLista)):
        print("Con la lista " + str(lstLista[intNIndex]) + ", regresa " + str(calcularMediaDesviacion(lstLista[intNIndex])))

main()