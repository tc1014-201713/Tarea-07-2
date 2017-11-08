# Encoding: utf-8
# Autor: Diego A. Prz Gnz
# Tarea 7 Listas 2

def numerosPares(lista):
    listaPares = []

    for x in lista:
        if x % 2 == 0:
            listaPares.append(x)

    return listaPares

def numerosMayores(lista):
    listaMayores = []

    for x in range(0, len(lista) - 1):
        if lista[x + 1] > lista[x]:
            listaMayores.append(lista[x + 1])

    return listaMayores

def numerosParejas(lista):
    listaParejas = []

    if len(lista) % 2 == 0:

        for x in range(0, len(lista) - 1, 2):
            listaParejas.append(lista[x + 1])
            listaParejas.append(lista[x])

    elif len(lista) == 3:

        for x in range(0, len(lista) - 1, 2):
            listaParejas.append(lista[x + 1])
            listaParejas.append(lista[x])
            listaParejas.append(lista[x - 1])

    else:

        listaParejas.append(lista[-1])

    return listaParejas

def numerosIntercambiarMinYMax(lista):
    listaMayor = []

    for x in range(0, len(lista)):

        if max(lista) == lista[x]:
            listaMayor.append(min(lista))

        elif min(lista) == lista[x]:
            listaMayor.append(max(lista))

        else:

            listaMayor.append(lista[x])

    return listaMayor

def regresarListaPromedio(lista):
    listaPromedio = [] #jlj
    prom = int(sum(lista) // len(lista))

    for x in range(0, len(lista)):

        if lista[x] >= prom:
            listaPromedio.append(lista[x])

    cantidad = len(listaPromedio)

    return cantidad

def calcMediaSeis(lista):
    media = sum(lista)/len(lista)

    return media

def calcDesviacionSeis(media, lista):
    listaNumerador = []

    for x in range(0,len(lista)):
        z = (lista[x]-media)**2

        listaNumerador.append(z)

    numeradorSuma = sum(listaNumerador)

    desviacion = (numeradorSuma/(len(lista)-1))**(1/2)

    return desviacion

def main():


    print("Problema 1: Regresa nuevas listas con los valores pares de las anteriores")
    print("")

    listaP1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaP2 = [5, 7, 3]

    print("En la lista: ", listaP1, "los números: ", numerosPares(listaP1), "son pares.")
    print("En la lista: ", listaP2, "los números: ", numerosPares(listaP2), "son pares.")
    print("")

    print("-----------------------------------------------------------------------------------------------------------")
    print("")

    print("Problema 2: Regresa los elementos previos en caso de ser mayor")
    print("")

    listaM1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaM2 = [5, 4, 3, 2]

    print("En la lista: ", listaM1, "los números: ", numerosMayores(listaM1), "son más grandes que el anterior.")
    print("En la lista: ", listaM2, "los números: ", numerosMayores(listaM2), "son más grandes que el anterior.")
    print("")

    print("-----------------------------------------------------------------------------------------------------------")
    print("")

    print("Problema 3: Regresa nuevas listas que invierte la pareja de números de las listas anteriores")
    print("")

    listaPa1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaPa2 = [1, 2, 3]
    listaPa3 = [7]

    print("En la lista: ", listaPa1, "los números: ", numerosParejas(listaPa1), "fueron invertidos.")
    print("En la lista: ", listaPa2, "los números: ", numerosParejas(listaPa2), "fueron invertidos.")
    print("En la lista: ", listaPa3, "los números: ", numerosParejas(listaPa3), "fueron invertidos.")
    print("")

    print("-----------------------------------------------------------------------------------------------------------")
    print("")

    print("Problema 4: Intercambia los valores máximos y mínimos")
    print("")

    listaMax1 = [5, 9, 3, 22, 19, 31, 10, 7]
    listaMax2 = [1, 2, 3]

    print("Tu lista: ", listaMax1, "regresa esta lista: ", numerosIntercambiarMinYMax(listaMax1))
    print("Tu lista: ", listaMax2, "regresa esta lista: ", numerosIntercambiarMinYMax(listaMax2))
    print("")

    print("-----------------------------------------------------------------------------------------------------------")
    print("")

    print("Problema 5: Regresa los valores arriba del promedio y regresa el número de datos que son mayores o iguales al promedio")
    print("")

    listaProm1 = [70, 80, 90]
    listaProm2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]

    print(regresarListaPromedio(listaProm1), "valores de la lista: ", listaProm1, "están arriba del promedio", "que es: ", int(sum(listaProm1) // len(listaProm1)))
    print(regresarListaPromedio(listaProm2), "valores de la lista: ", listaProm2, "están arriba del promedio", "que es: ", int(sum(listaProm2) // len(listaProm2)))
    print("")

    print("-----------------------------------------------------------------------------------------------------------")
    print("")

    print("Problema 6: Regresa una dupla con la media y la desviación estándar")
    print("")

    listaD1 = [1, 2, 3, 4, 5, 6]
    media1 = calcMediaSeis(listaD1)
    desviacion1 = calcDesviacionSeis(media1, listaD1)
    listaD2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    media2 = calcMediaSeis(listaD2)
    desviacion2 = calcDesviacionSeis(media2, listaD2)

    print("Le media de la lista:", listaD1, "es:", media1, "y su desviación es:", desviacion1)
    print("Le media de la lista:", listaD2, "es:", media2, "y su desviación es:", desviacion2)
    print("")

main()