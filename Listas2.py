# encoding: UTF-8
# Autor: Edgar Alexis González Amador    A01746540
# Porgrama correspondiente a la tarea numero 7-2, del tema listas.

import math

def generarListaDeNumerosPares(lista):
    listaFinal = []
    for numeroActual in range (len(lista)):
        if lista[numeroActual]%2 == 0:
            listaFinal.append(lista[numeroActual])
    return listaFinal

def generarListaDeNumerosConMenorPrevio(lista):
    listaFinal = []
    if len(lista) != 0:
        numeroAnterior = lista[0]
        for numeroActual in range (len(lista)):
            if lista[numeroActual] > numeroAnterior:
                listaFinal.append(lista[numeroActual])
            numeroAnterior = lista[numeroActual]
    return listaFinal

def generarListaConParesIntercambiados(lista):
    listaFinal = []
    for parActual in range (0, len(lista)-1, 2):
        listaFinal.append(lista[parActual+1])
        listaFinal.append(lista[parActual])
    if len(lista)%2 != 0:
        listaFinal.append(lista[len(lista)-1])
    return listaFinal

def generarListaConElMayorYMenosIntercambiados(lista):
    listaFinal = []
    if len(lista) != 0:
        maximo = max(lista)
        minimo = min(lista)
        for numeroActual in range (len(lista)):
            if lista[numeroActual] != maximo and lista[numeroActual] != minimo:
                listaFinal.append(lista[numeroActual])
            elif lista[numeroActual] == maximo:
                listaFinal.append(minimo)
            elif lista[numeroActual] == minimo:
                listaFinal.append(maximo)
    return listaFinal

def regresarCantidadMayorAlPromedio(lista):
    numerosMayoresAlPromedio = 0
    if len(lista) != 0:
        promedio = sum(lista)/len(lista)
        for numeroActual in range (len(lista)):
            if lista[numeroActual] >= promedio:
                numerosMayoresAlPromedio += 1
    return numerosMayoresAlPromedio

def regresarMediaYDesviacion(lista):
    media = 0
    desviacion = 0
    sumatoriaDesviacion = 0
    if len(lista) != 0 and len(lista) != 1:
        media = sum(lista)/len(lista)
        for numeroActual in range (len(lista)):
            sumatoriaDesviacion += ((lista[numeroActual])-media)**2
        desviacion = math.sqrt(sumatoriaDesviacion / (len(lista)-1))
    resultado = (media, desviacion)
    return resultado

def main():
    #Declaracion de listas

    print("Prueba de las listas")
    # Prueba 1
    print("\nPrueba 1")
    lista11=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista12=[5,7,3]
    lista13=[6]
    lista14=[]
    print("Con la lista ", lista11, ", regresa ", generarListaDeNumerosPares(lista11))
    print("Con la lista ", lista12, ", regresa ", generarListaDeNumerosPares(lista12))
    print("Con la lista ", lista13, ", regresa ", generarListaDeNumerosPares(lista13))
    print("Con la lista ", lista14, ", regresa ", generarListaDeNumerosPares(lista14))
    # Prueba 2
    print("\nPrueba 2")
    lista21=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista22=[5,4,3,2]
    lista23=[7]
    lista24=[]
    print("Con la lista ", lista21, ", regresa ", generarListaDeNumerosConMenorPrevio(lista21))
    print("Con la lista ", lista22, ", regresa ", generarListaDeNumerosConMenorPrevio(lista22))
    print("Con la lista ", lista23, ", regresa ", generarListaDeNumerosConMenorPrevio(lista23))
    print("Con la lista ", lista24, ", regresa ", generarListaDeNumerosConMenorPrevio(lista24))
    # Prueba 3
    print("\nPrueba 3")
    lista31=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista32=[1,2,3]
    lista33=[7]
    lista34=[]
    print("Con la lista ", lista31, ", regresa ", generarListaConParesIntercambiados(lista31))
    print("Con la lista ", lista32, ", regresa ", generarListaConParesIntercambiados(lista32))
    print("Con la lista ", lista33, ", regresa ", generarListaConParesIntercambiados(lista33))
    print("Con la lista ", lista34, ", regresa ", generarListaConParesIntercambiados(lista34))
    # Prueba 4
    print("\nPrueba 4")
    lista41=[5,9,3,22,19,31,10,7]
    lista42=[1,2,3]
    lista43=[1]
    lista44=[]
    print("Con la lista ", lista41, ", regresa ", generarListaConElMayorYMenosIntercambiados(lista41))
    print("Con la lista ", lista42, ", regresa ", generarListaConElMayorYMenosIntercambiados(lista42))
    print("Con la lista ", lista43, ", regresa ", generarListaConElMayorYMenosIntercambiados(lista43))
    print("Con la lista ", lista44, ", regresa ", generarListaConElMayorYMenosIntercambiados(lista44))
    # Prueba 5
    print("\nPrueba 5")
    lista51=[70, 80, 90]
    lista52=[95,21,73,24,15,69,71,80,49,100,85]
    lista53=[1]
    lista54=[]
    print("Con la lista ", lista51, ", regresa ", regresarCantidadMayorAlPromedio(lista51))
    print("Con la lista ", lista52, ", regresa ", regresarCantidadMayorAlPromedio(lista52))
    print("Con la lista ", lista53, ", regresa ", regresarCantidadMayorAlPromedio(lista53))
    print("Con la lista ", lista54, ", regresa ", regresarCantidadMayorAlPromedio(lista54))
    # Prueba 6
    print("\nPrueba 6")
    lista61=[1,2,3,4,5,6]
    lista62=[95,21,73,24,15,69,71,80,49,100,85]
    lista63=[3]
    lista64=[]
    print("Con la lista ", lista61, ", regresa ", regresarMediaYDesviacion(lista61))
    print("Con la lista ", lista62, ", regresa ", regresarMediaYDesviacion(lista62))
    print("Con la lista ", lista63, ", regresa ", regresarMediaYDesviacion(lista63))
    print("Con la lista ", lista64, ", regresa ", regresarMediaYDesviacion(lista64))

main()