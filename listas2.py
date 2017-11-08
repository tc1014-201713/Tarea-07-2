#encoding: UTF-8
#Neftalí Rodríguez Martínez.
#Archivo de solución a tarea 2 listas.

def regresarPares (lista): #Solución al problema 1.
    lista_nueva = lista[:]

    for dato in lista:
        if dato % 2 > 0:
            lista_nueva.remove(dato)

    return lista_nueva


def obtenerPromedio(lista): #primera parte problema 5
    if sum(lista) == 0 or len(lista) == 0 or len(lista) == 1:
        promedio = 0
    else:
        promedio = sum(lista) // len(lista)
    return promedio


def obtenerMayoresoIgual(lista, promedio): #segunda parte problema 5.
    contador = 0

    for dato in lista:
        if dato >= promedio:
            contador = contador + 1

    return contador


def obtenerMediaDesviacion(lista): # problema 6
    acumulador = 0

    if len(lista) == 0 or len(lista) == 1:
        media = 0
    else:
        media = sum(lista) / len(lista)

    for dato in lista:
        acumulador = acumulador + ((dato - media) ** 2)

    if len(lista) == 0 or len(lista) == 1:
        desviacion = 0
    else:
        desviacion = (acumulador / (len(lista) - 1)) ** 0.5

    resultado = (media, desviacion)

    return resultado


def intercambiarParejas(lista): #problema 3.
    lista_nueva = []
    final_lista = len(lista)

    if len(lista) % 2 != 0:
        final_lista = len(lista)-1
        lista_nueva.insert(-1,lista[-1])

    for k in range(0, final_lista, 2):
        lista_nueva.append(lista[k+1])
        lista_nueva.append(lista[k])

    return lista_nueva


def valoresMayores(lista): #Problema 2.
    lista_nueva = []
    for k in range (1, len(lista)):
        if lista[k] > lista[k-1]:
            lista_nueva.append(lista[k])

    return lista_nueva


def invertirMayorMenor(lista):
    lista_nueva = lista[:]
    if len(lista) == 0 or len(lista) == 1:
        return lista_nueva
    else:
        lista_nueva[lista.index(max(lista))] = min(lista)
        lista_nueva[lista.index(min(lista))] = max(lista)

    return lista_nueva


def main (): #Programa principal.
    print("Este programa da solución a la Tarea 2 de listas")
    print("\r")

    print("Estos son los resultados al problema 1.")
    #Datos problema 1.
    lista1_1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1_2 = [5,7,3]
    print("Con la lista", lista1_1, "regresa", regresarPares(lista1_1))
    print("Con la lista", lista1_2, "regresa", regresarPares(lista1_2))
    print("\r")

    print("Estos son los resultados al problema 2.")
    #Datos problema 2.
    lista2_1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2_2 = [5,4,3,2]
    print("Con la lista", lista2_1, "regresa", valoresMayores(lista2_1))
    print("Con la lista", lista2_2, "regresa", valoresMayores(lista2_2))
    print("\r")


    print("Estos son los resultados al problema 3.")
    lista3_1 = 	[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista3_2 = 	[1, 2, 3]
    lista3_3 = [7]

    print("Con la lista", lista3_1, "regresa", intercambiarParejas(lista3_1))
    print("Con la lista", lista3_2, "regresa", intercambiarParejas(lista3_2))
    print("Con la lista", lista3_3, "regresa", intercambiarParejas(lista3_3))
    print("\r")

    print("Estos son los resultados al problema 4.")
    lista4_1 = [5,9,3,22,19,31,10,7]
    lista4_2 = [1,2,3]
    lista4_3 = []
    lista4_4 = [1]
    
    print("Con la lista", lista4_1, "regresa", invertirMayorMenor(lista4_1))
    print("Con la lista", lista4_2, "regresa", invertirMayorMenor(lista4_2))
    print("Con la lista", lista4_3, "regresa", invertirMayorMenor(lista4_3))
    print("Con la lista", lista4_4, "regresa", invertirMayorMenor(lista4_4))
    print("\r")



    print("Estos son los resultados al problema 5.")
    #Datos problema 5.
    lista5_1 = 	[70, 80, 90]
    lista5_2 = [95,21,73,24,15,69,71,80,49,100,85]
    lista5_3 = []

    print("Con la lista", lista5_1, "el promedio es", obtenerPromedio(lista5_1), "hay", obtenerMayoresoIgual(lista5_1, obtenerPromedio(lista5_1)), "números mayores o igual al promedio.")
    print("Con la lista", lista5_2, "el promedio es", obtenerPromedio(lista5_2), "hay", obtenerMayoresoIgual(lista5_2, obtenerPromedio(lista5_2)), "números mayores o igual al promedio.")
    print("\r")

    print("Estos son los resultados al problema 6.")
    #Datos problema 6.
    lista6_1 = [1,2,3,4,5,6]
    lista6_2 = 	[95,21,73,24,15,69,71,80,49,100,85]
    lista6_3 = []
    lista6_4 = [3]

    media1 = obtenerMediaDesviacion(lista6_1)[0]
    desviacion1 = obtenerMediaDesviacion(lista6_1)[1]
    media2 = obtenerMediaDesviacion(lista6_2)[0]
    desviacion2 = obtenerMediaDesviacion(lista6_2)[1]

    print("La media y desviación estándar de %s es (%g, %.6f)" % (lista6_1, media1, desviacion1))
    print("La media y desviación estándar de %s es (%g, %.4f)" % (lista6_2, media2, desviacion2))
    print("La media y desviación estándar de", lista6_3, "es", obtenerMediaDesviacion(lista6_3))
    print("La media y desviación estándar de", lista6_4, "es", obtenerMediaDesviacion(lista6_4))
    print("\r")


main()