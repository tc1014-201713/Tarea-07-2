# encoding: UTF-8
# Autor: Arianna Sinai Soriano Vega
# Tarea 2 sobre listas

import math
def Problema1(lista): # Escribe una función que recibe como parámetro una lista de números enteros y regresa UNA NUEVA lista con los valores pares de la lista original.

    nuevalista = []
    for i in lista:
        if i%2==0:
            nuevalista.append(i)
    return nuevalista

def Problema2(lista):
    listanueva=[]
    for i in range(1,len(lista)):
        if lista[i] > lista[i-1]:
            listanueva.append(lista[i])


    return listanueva

def Problema3(lista):

    paresinversos=[]

    if len(lista)==0 or len(lista)==1:
        paresinversos= lista

    elif len(lista)%2==0:
        for i in range(0,len(lista),2):
            valor1=lista[i]
            valor2= lista[i+1]
            paresinversos.append(valor2)
            paresinversos.append(valor1)
    else:
        for i in range(0,len(lista)-1,2):
            valor1=lista[i]
            valor2= lista[i+1]
            paresinversos.append(valor2)
            paresinversos.append(valor1)
        paresinversos.append(lista[len(lista)-1])

    return paresinversos

def Problema4(lista):
    listanew=[]

    if len(lista)!=0:
        mayor = lista.index(max(lista))
        mini = lista.index(min(lista))
        for i in range(len(lista)):

            if mini == i:
                listanew.append(max(lista))
            elif mayor == i:
                listanew.append(min(lista))
            else:
                listanew.append(lista[i])
        return listanew
    else:
        return lista


def Problema5(lista):
    sumatoria = int((sum(lista)))
    if sumatoria!=0 and len(lista)> 0:
        newlist=[]
        promedio=int(sumatoria/(len(lista)))
        for dato in lista:
            if promedio <= dato:
                newlist.append(dato)
        return newlist
        # Si recibe [70, 80, 90], regresa 2. Porque el promedio es 80 y hay dos valores mayores o iguales a 80 (80 y 90)

    else :
        return lista

def Problema6(lista):
    sumatoria = float((sum(lista)))
    newlist = []
    if sumatoria!=0 and len(lista)> 1:

        promedio=float(sumatoria/(len(lista)))
        newlist.append(promedio)
        anterior = 0
        for dato in lista:

            actual= (dato-promedio)**2 +anterior
            anterior=actual

        desviacion = math.sqrt((anterior)/(len(lista)-1))
        newlist.append(desviacion)

        return newlist
    else :
        newlist=[0,0]
        return newlist

def main():
    listas = [[1, 2, 3, 4, 5, 6, 11, 12, 15, 145, 144, 45, 56, 33], [], [111], [222], [1, 3, 5, 7, 9, 1, 43, 77, 101],
              [2, 4, 6, 8, 10, 34, 22, 12, 20, 8]]
    print("Tarea 7-2. ¡Bienvenido al programa que funciona con listas!")
    print("")

    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    for i in range(len(listas)):
        pares=Problema1(listas[i])
        print("Si recibe,",listas[i],",regresa",pares)
    print("")


    print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo.")
    for i in range(len(listas)):
        mayores=Problema2(listas[i])
        print("Si recibe,",listas[i],",regresa",mayores)
    print("")


    print("Problema 3. Regresa una lista con cada pareja de datos intercambiados.")
    for i in range(len(listas)):
        paresin = Problema3(listas[i])
        print("Si recibe,", listas[i], ",regresa", paresin)
    print("")

    print("Problema 4. Regresa una nueva lista con el valor menor y mayor intercambiados. Suponga que los valores son únicos.")
    for i in range(len(listas)):
        maxmin = Problema4(listas[i])
        print("Si recibe,", listas[i], ",regresa", maxmin)
    print("")

    print("Problema 5. Regresa una lista con el número de datos que son mayores o iguales al promedio de todos los valores de la lista.")
    for i in range(len(listas)):
        mayorespromedio = Problema5(listas[i])
        print("Si recibe,", listas[i], ",regresa", len(mayorespromedio),"porque hay",len(mayorespromedio),"valor(es) igual(es) o mayor(es) al promedio.",mayorespromedio)
    print("")

    print("Problema 6. Regresa una dupla con la media y la desviación estándar.")
    for i in range(len(listas)):
        dupla = Problema6(listas[i])
        print("Si recibe,", listas[i], ",regresa", dupla)
    print("")


main ()
