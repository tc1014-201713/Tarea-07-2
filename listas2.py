#encoding: UTF-8
#Autor: Daniel Sahuer
#Programa que resuelve 6 ejercicios usando listas


#Listas usadas
lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
lista2 = [5, 7, 3]
lista3 = [5, 4, 3, 2]
lista4 = [1, 2, 3]
lista5 = [7]
lista6 = [5, 9, 3, 22, 19, 31, 10, 7]
lista7 = [70, 80, 90]
lista8 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
lista9 = [1, 2, 3, 4, 5, 6]



def valoresPares(lista):    #Ejercicio 1: se regresan unicamente los valores pares de una lista
    par = []

    for i in lista:
        if i%2 == 0:
            par.append(i)

    return par


def valoresMayores(lista):  #Ejercicio 2: se regresan unicamente los valores que son mayores a un elemento previo de la lista
    mayor = []

    for i in range (0,len(lista)-1):
        if lista[i+1]>lista[i]:
            mayor.append(lista[i+1])
    return mayor


def parejaIntercamiados(lista): #Ejercicio 3: se intercambian los valores de cada pareja de la lista

    intercambio = []
    intercambio1 = []
    intercambio2 = []


    if len(lista)%2 == 0:

        for i in range(0, len(lista),2):
            intercambio1.append(lista[i])

        for i in range(1,len(lista),2):
            intercambio2.append(lista[i])

        for i in range(0,len(intercambio1) and len(intercambio2)):
            intercambio.append(intercambio2[i])
            intercambio.append(intercambio1[i])

    else:
        for i in range(0, len(lista),2):
            intercambio1.append(lista[i])

        for i in range(1,len(lista),2):
            intercambio2.append(lista[i])

        for i in range(0,len(intercambio1) and len(intercambio2)):
            intercambio.append(intercambio2[i])
            intercambio.append(intercambio1[i])

        intercambio.append(lista[-1])

    return intercambio


def mayorYMenorIntercambiados(lista): #Ejercicio 4: se intercambia el valor menor con el mayor de una lista

    intercambio = []

    for i  in range(0,len(lista)):
        if max(lista) == lista[i]:
            intercambio.append(min(lista))

        elif min(lista) == lista[i]:
            intercambio.append(max(lista))

        else:
            intercambio.append(lista[i])

    return intercambio


def mayoresPromedio(lista): #Ejercicio 5: se calcula el número de valores de una lista que son mayores al promedio de los valores
    promedio = sum(lista)/len(lista)
    total = 0

    for i in range (0, len(lista)):
        if lista[i] >= promedio:
            total += 1

    return total


def mediayDesviacion(lista):    #Ejercicio 6: se calcula el promedio y la desviación estándar de los valores de una lista

    promedio = sum(lista) / len(lista)
    suma = 0

    if len(lista) != 0 and len(lista) != 1:

        for i in lista:
            suma = suma + (i-promedio)**2
        desviacion = (suma/(len(lista)-1))**(1/2)

        total =  (promedio,desviacion)

    else:
        total =  (0,0)

    return total


def main():

    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista %s ,regresa %s" % (lista1,valoresPares(lista1)))
    print("Con la lista %s ,regresa %s" % (lista2,valoresPares(lista2)))

    print("\nProblema 2. Regresa una lista con los valores que son mayores a un elemento previo.")
    print("Con la lista %s ,regresa %s" % (lista1,valoresMayores(lista1)))
    print("Con la lista %s ,regresa %s" % (lista3,valoresMayores(lista3)))

    print("\nProblema 3. Regresa una lista con cada pareja de datos intercambiados. Si el número de datos es impar, el último elemento no cambia.")
    print("Con la lista %s ,regresa %s" % (lista1,parejaIntercamiados(lista1)))
    print("Con la lista %s ,regresa %s" % (lista4,parejaIntercamiados(lista4)))
    print("Con la lista %s ,regresa %s" % (lista5,parejaIntercamiados(lista5)))

    print("\nProblema 4. Regresa una lista con el valor menor y mayor intercambiados.")
    print("Con la lista %s ,regresa %s" % (lista6,mayorYMenorIntercambiados(lista6)))
    print("Con la lista %s ,regresa %s" % (lista4,mayorYMenorIntercambiados(lista4)))

    print("\nProblema 5. Regresa una lista con el número de datos que son mayores o iguales al promedio de todos los valores de la lista.")
    print("Con la lista %s ,regresa %s" % (lista7,mayoresPromedio(lista7)))
    print("Con la lista %s ,regresa %s" % (lista8,mayoresPromedio(lista8)))

    print("\nProblema 6. Regresa una dupla con la media y la desviación estándar.")
    print("Con la lista %s ,regresa %s" % (lista9,mediayDesviacion(lista9)))
    print("Con la lista %s ,regresa %s" % (lista8,mediayDesviacion(lista8)))
    print("Con la lista %s ,regresa %s" % (lista5,mediayDesviacion(lista5)))


main()