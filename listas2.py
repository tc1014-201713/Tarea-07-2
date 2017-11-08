#encoding: utf-8
#autor: Iván Dumas
#Tarea 2 sobre Listas


def ejercicio1(listX):
    listY=[]
    for p in listX:
        if p % 2 == 0:
            listY.append(p)
    return listY

def ejercicio2(listX):
    listY = []
    for p in range(1, len(listX)):
        if listX[p]>listX[p-1]:
            listY.append(listX[p])
    return listY


def ejercicio3(listX):
    listY = []
    for i in range (1,len(listX),2):
        listY.append(listX[i])
        listY.append(listX[i-1])
    if len(listX)%2 != 0:
        listY.append(listX[len(listX)-1])
    return listY


def ejercicio4(listX):
    listY =[]
    for i in listX:
        listY.append(i)
    if len(listY)>1:
        minY = min(listY)
        maxY = max(listY)
        indexMinY = listY.index(minY)
        indexMaxY = listY.index(maxY)
        listY.remove(minY)
        listY.remove(maxY)
        listY.insert(indexMinY, maxY)
        listY.insert(indexMaxY, minY)

    return listY

def ejercicio5(listX):
    cont = 0
    if len(listX)!=0:
        prom = sum(listX)/len(listX)
        for p in listX:
            if p >= prom:
                cont += 1
    else:
        cont = cont
    return cont


def ejercicio6(listX):
    mean = 0
    deviation = 0
    if len(listX) > 1:
        for i in range(len(listX)):
            mean += listX[i]
        mean /= len(listX)
        for j in range (len(listX)):
            deviation += ((listX[j] - mean)**2)
        deviation /= (len(listX)-1)
        deviation = deviation**0.5
        result = (mean,deviation)
    else:
        result = (0,0)
    return result


def main():
    testList = [[1,2,3,4,5,6],[1,2,3,2,4,60,5,8,3,22,44,55],[5,7,3],[7],[],[5,9,3,22,19,31,10,7],[95,21,73,24,15,69,71,80,49,100,85]] #Lista de listas por probar
    sentenceDict = {"Problema 1. Regresa una lista con los valores pares de la lista original.":ejercicio1,"Problema 2. Regresa una lista con los valores que son mayores a un elemento previo.":ejercicio2,"Problema 3. Regresa una lista con cada pareja de datos intercambiados, si la lista es impar, el último dato no cambia.":ejercicio3,"Problema 4. Regresa una lista con el valor menor y mayor intercambiados.":ejercicio4,"Problema 5. Regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.":ejercicio5,"Ejercicio 6.Regresa una dupla con la media y la desviación estándar.":ejercicio6}

    for sentence in sentenceDict:
        print(sentence)
        for test in testList:
            print("Con la lista",test,", regresa",sentenceDict[sentence](test))
main()