#Encoding: UTF-8
#Autor: Roberto Téllez Perezyera
"""
Este programa prueba cada una de las funciones que lo conforman dentro de una función main. El usuario no teclea ni
ingresa dato alguno. Las funciones reciben listas y regresan las listas modificadas, o valores como promedios y número
de datos que cumplan con alguna condición dada.
"""

import math


def conservarPares(lista):
    #Regresa una nueva lista con los valores de la original
    sinNones = []
    for dato in lista:
        if dato % 2 == 0:
            sinNones.append(dato)

    return sinNones


def conservarMayorAPrevio(lista):
    #Regresa una nueva lista con los valores que son mayores a un elemento previo
    mayores = []
    for k in range(len(lista)-1):
        if lista[k+1] > lista[k]:
            mayores.append(lista[k+1])

    return mayores


def intercambiarParejas(lista):
    #Regresa una nueva lista con las parejas de datos intercambiadas. Si el número de datos es impar, el último valor
    #NO cambia.
    swappedPairs = []
    if len(lista) % 2 == 0:
        for k in range(0,len(lista),2):
            swappedPairs.append(lista[k+1])
            swappedPairs.append(lista[k])
        return swappedPairs
    else:
        for k in range(0,len(lista)-1,2):
            swappedPairs.append(lista[k+1])
            swappedPairs.append(lista[k])
        swappedPairs.append(lista[len(lista)-1])    #ahora sí regresa el último valor de la lista en el 2º ejemplo
        return swappedPairs


def intercambiarMayorMenor(lista):
    #Regresa una nueva lista con los valores mayor y menor de la lista intercambiados
    listMax = max(lista)
    listMin = min(lista)    #Howto swappearlos??
    swapped = lista[:]
    maxIndex = swapped.index(max(swapped))
    minIndex = swapped.index(min(swapped))
    swapped[minIndex], swapped[maxIndex] = swapped[maxIndex], swapped[minIndex]

    return swapped


def countGreaterEqualToAvg(lista):
    #Regresa el NÚMERO DE DATOS que son mayores o iguales al promedio de todos los valores de la lista.
    contador = 0
    mean = (sum(lista)/len(lista))
    for dato in lista:
        if dato >= mean:
            contador += 1

    return contador
    #Y si también quiero regresar la media (pero NO en una tupla) para mostrarlo como en la especificación de la tarea?


def calculateMeanAndStdDev(lista):
    #Recibe una lista y regresa en una tupla la media y la desviación estándar
    if len(lista) <= 1:
        return (0, 0)
    else:
        mean = (sum(lista) / len(lista))

        #StdDev:
        sumatoria = 0
        for k in lista:
            sumatoria += (k - mean)**2
        stdDev = math.sqrt( sumatoria / (len(lista)-1) )

        return(mean, stdDev)


def main():
    #Función principal, donde se imprime lo que el usuario podrá ver al correr el programa
    #Listas para probar las funciones
    listaA = [1,2,3,2,4,60,5,8,3,22,44,55]
    listaB = [5,7,3]
    listaC = []
    listaD = [5,4,3,2]
    listaE = [1,2,3]
    listaF = [7]
    listaG = [1,2,3,4,5,6]
    listaH = [3]
    listaI = [5,9,3,22,19,31,10,7]
    listaJ = [95,21,73,24,15,69,71,80,49,100,85]
    listaK = [70,80,90]


    #Se prueban las funciones con todos los casos necesarios para demostrar que funcionan adecuadamente

    #Problema1
    print("Problema 1. Regresa una lista nueva, con los valores pares de la lista original.")
    print("Con la lista ", listaA, ", regresa ", conservarPares(listaA))
    print("Con la lista ", listaB, ", regresa ", conservarPares(listaB))
    print("Con la lista ", listaC, ", regresa ", conservarPares(listaC))

    #Problema2
    print("\nProblema 2. Regresa una lista nueva, con los valores que son mayores a un elemento previo.")
    print("Si recibe ", listaA, ", regresa ", conservarMayorAPrevio(listaA))
    print("Si recibe ", listaD, ", regresa ", conservarMayorAPrevio(listaD))

    #Problema3
    print("\nProblema 3. Regresa una lista nueva, cuyas parejas de datos están intercambiadas. Si el número de datos es impar, el último elemento no cambia.")
    print("Si recibe ", listaA, ", regresa ", intercambiarParejas(listaA))
    print("Si recibe ", listaE, ", regresa ", intercambiarParejas(listaE))
    print("Si recibe ", listaF, ", regresa ", intercambiarParejas(listaF))

    #Problema4
    print("\nProblema 4. Regresa una lista nueva con el valor menor y el mayor (de la lista) intercambiados.")
    print("Si recibe ", listaI, ", regresa ", intercambiarMayorMenor(listaI))
    print("Si recibe ", listaE, ", regresa ", intercambiarMayorMenor(listaE))

    #Problema5
    print("\nProblema 5. Regresa el número de datos que son mayores o iguales al promedio de los valores en la lista.")
    print("Si recibe ", listaK, ", regresa ", countGreaterEqualToAvg(listaK))
    print("Si recibe ", listaJ, ", regresa ", countGreaterEqualToAvg(listaJ))

    #Problema6
    print("\nProblema 6. Regresa una tupla con la media y la desviación estándar de los datos en la lista, usando las fórmulas para obtener éstas.")
    print("Si recibe ", listaG, ", regresa ", calculateMeanAndStdDev(listaG))
    print("Si recibe ", listaJ, " o ", listaH, ", regresa ", calculateMeanAndStdDev(listaJ))
    print("Si recibe ", listaC, " o ", listaH, ", regresa ", calculateMeanAndStdDev(listaC), " en ambos casos.")


main()