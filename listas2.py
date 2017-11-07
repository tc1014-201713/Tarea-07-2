#encoding: UTF-8
#Autor: Joaquin Rios Corvera A01375441

import math

#Regresa los números pares que se encuentran en alguna lista
def regresarPares(lista):
    listaPar = []
    for elemento in lista:
        if elemento % 2 == 0:
            listaPar.append(elemento)
    return listaPar

#Regresa los números de una lista que son mayores al número previo a ellos
def regresarMayores(lista):
    listaMayores = []
    for x in range (0, len(lista)-1):
        if lista[x] < lista[x+1]:
            listaMayores.append(lista[x+1])
    return listaMayores

#Intercambia la posición de cada par de valores de una lista
def intercambiarValores(lista):
    listaIntercambiada = lista[::1]
    a = 1
    if len(listaIntercambiada)%2 == 1:
        a = 2
    for x in range (0, len(listaIntercambiada)-a, 2):
        y = listaIntercambiada[x]
        listaIntercambiada[x] = listaIntercambiada[x+1]
        listaIntercambiada[x+1] = y
    return listaIntercambiada

#Encuentra el número mayor y menor de una lista e intercambia sus posiciones
def cambiarMenorMayor(lista):
    listaN = lista[::1]
    if len(lista) != 0:
        maximo = max(listaN)
        minimo = min(listaN)
        maximoPos = listaN.index(maximo)
        minimoPos = listaN.index(minimo)
        listaN[maximoPos] = minimo
        listaN[minimoPos] = maximo
    else:
        listaN = []
    return listaN

#Encuentra el promedio de una lista de números y regresa la cantidad de números que son mayores o igual a ese promedio
def encontrarMayorAPromedio(lista):
    listaMayorAPromedio = []
    if len(lista) != 0:
        promedio = sum(lista)/len(lista)
    else:
        return 0
    for elemento in lista:
        if elemento >= promedio:
            listaMayorAPromedio.append(elemento)
    return len(listaMayorAPromedio)


#Encuentra la desviación estándar y el promedio de una lista de números
def encontrarDesviacionEstandar(lista):
    if len(lista)== 0 or len(lista)==1:
        return "(0,0}"
    else:
        promedio = sum(lista)/len(lista)
        sumatoria = 0
        for x in lista:
            sumatoria += (x-promedio)**2
        desviacion = math.sqrt((sumatoria)/(len(lista)-1))
        resultado = "(" + str(promedio) + ", " + str(desviacion) + ")"
        return resultado


def main():
    listas = [[70,80,90], [5,9,3,22,19,31,10,7], [], [5], [1,2,3,2,4,60,5,8,3,22,44,55], [5,4,3,2],[5,7,3]]
    funciones = {"Problema 1. Regresa una lista con los valores pares de la lista original.": regresarPares, "Problema 2. Regresa una lista con los valores mayores a un elemento previo.":regresarMayores, "Problema 3. Regresa una lista con cada pareja de datos intercambiados.":intercambiarValores, "Problema 4. Regresa una lista con su valor mayor y menor intercambiados.":cambiarMenorMayor, "Problema 5. Regresa la cantidad de datos mayores o iguales al promedio de los números.": encontrarMayorAPromedio, "Problema 6. Regresa una dupla con la media y la desviación estándar de los datos.":encontrarDesviacionEstandar}

    #Toma cada función y la evalua con cada lista
    for enunciado, funcion in funciones.items():
        print(enunciado)
        for lista in listas:
            print("Con la lista " + str(lista) + ", regresa " + str(funcion(lista)))
        print("")

main()