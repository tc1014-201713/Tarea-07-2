#encoding UTF-8
#Autor: Javier León Alcántara
#Tarea 07 Listas

from math import *

def valoresPares(lista):
    newLista = []  #crea nueva lista

    for i in lista:
        if i % 2 == 0:
            newLista.append(i)     #si el valor al dividirlo entre dos da como resultado cero, lo agregará a la lista

    print(newLista)


def mayor(lista):
    newLista = []  #crea nueva lista
    lista2 = lista[1:]     #crea nueva lista con los datos a partir del indice 1 de "newlista"

    for i in lista2:
        if i > lista[0]:
            newLista.append(i)  #si el valor en la segunda lista es mayor al valor en el indice cero de "newlista" lo agregará
            lista = lista[1:]   #descarta el primer indice de la lista

        else:
            lista = lista[1:]

    print(newLista)


def cambio(lista):
    newLista = []   #crea nueva lista

    if len(lista) % 2 == 0:
        for i in range(len(lista) // 2):
            x = lista[0]
            y = lista[1]
            newLista.append(y)
            newLista.append(x)        #agrega a otra lista los valores invertidos

            lista = lista[2:]        #descarta los valores ya ocupados
    else:
        for i in range(len(lista) // 2):
            x = lista[0]
            y = lista[1]
            newLista.append(y)
            newLista.append(x)

            lista = lista[2:]
        newLista.append(lista[-1])      #realiza lo mismo que el for de arriba sólo que aqui se agrega el último valor si es impar

    print(newLista)


def cambioMaxMin(lista):
    valormax = lista[0]
    valormin = lista[0]

    for i in lista:
        if i > valormax:
            valormax = i
        elif i < valormin:
            valormin = i      #compara los datos y los va sustituyendo

    indicemax = lista.index(valormax)
    indicemin = lista.index(valormin)     #busca los valores maximo y minimo para encontrar su indice

    lista[indicemax] = valormin
    lista[indicemin] = valormax      #sustituye en los indices los valores opuestos

    print(lista)



def mayorAPromedio(lista):

    promedio = (sum(lista)) // len(lista)      #calcula promedio
    numeros = 0
    listanumeros = []    #crea nueva lista

    for i in lista:
        if i >= promedio:
            listanumeros.append(i)
            numeros += 1             #calcula los numeros mayores al promedio

    print("El promedio es",promedio,"y hay",numeros,"valores mayores o iguales a",promedio,listanumeros)


def desviacion(lista):
    varianza = []     #crea nueva lista
    cuadrado = []     #crea nueva lista

    if len(lista) >= 2:

        media = sum(lista)/len(lista)    #calcula la media

        for i in lista:
            varianza.append(i-media)     #se resta la media a los valores

        for i in varianza:
            cuadrado.append(i**2)    #se elevan al cuadrado

        suma = sum(cuadrado)     #suma de los cuadrado
        varianza = suma / (len(lista)-1)    #calcula la varianza


        desviacion = sqrt(varianza)     #calcula la desviación

        print((media,"%.4f" % desviacion))

    else:
        print((0,0))

def main():

    print("Problema 1.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    valoresPares(lista)
    print("")
    lista =[1,5,7,3,4]
    print("Con la lista: ", lista, ",regresa:")
    valoresPares(lista)
    print("-----------------------------------------------------")

    print("Problema 2.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    mayor(lista)
    print("")
    lista = [1, 5, 7, 3, 4]
    print("Con la lista: ", lista, ",regresa:")
    mayor(lista)
    print("-----------------------------------------------------")

    print("Problema 3.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    cambio(lista)
    print("")
    lista = [1, 5, 7, 3, 4]
    print("Con la lista: ", lista, ",regresa:")
    cambio(lista)
    print("-----------------------------------------------------")

    print("Problema 4.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    cambioMaxMin(lista)
    print("")
    lista = [1, 5, 7, 3, 4]
    print("Con la lista: ", lista, ",regresa:")
    cambioMaxMin(lista)
    print("-----------------------------------------------------")

    print("Problema 5.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    mayorAPromedio(lista)
    print("")
    lista = [1, 5, 7, 3, 4]
    print("Con la lista: ", lista, ",regresa:")
    mayorAPromedio(lista)
    print("-----------------------------------------------------")

    print("Problema 6.")
    lista = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", lista, ",regresa:")
    desviacion(lista)
    print("")
    lista = [4]
    print("Con la lista: ", lista, ",regresa:")
    desviacion(lista)


main()