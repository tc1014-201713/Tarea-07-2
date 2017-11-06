# encoding:UTF-8
# Autor: Carlos Pano Hernández
# Tarea 7-2

def regresarNumerosPares(lista):
    listaPares = []

    for n in lista:
        if n % 2 == 0:
            listaPares.append(n)

    return listaPares

def regresarListaMayores(lista):
    listaMayores = []

    for n in range(0, len(lista) - 1):
        if lista[n + 1] > lista[n]:
            listaMayores.append(lista[n + 1])

    return listaMayores

def regresarListaPareja(lista):
    listaPareja = []

    if len(lista) % 2 == 0:

        for n in range(0, len(lista) - 1, 2):
            listaPareja.append(lista[n + 1])
            listaPareja.append(lista[n])

    elif len(lista) == 3:

        for n in range(0, len(lista) - 1, 2):
            listaPareja.append(lista[n + 1])
            listaPareja.append(lista[n])
            listaPareja.append(lista[n - 1])

    else:
        listaPareja.append(lista[-1])

    return listaPareja

def regresarListaIntercambioMayor(lista):
    listaMayor = []

    for n in range(0, len(lista)):

        if max(lista) == lista[n]:
            listaMayor.append(min(lista))

        elif min(lista) == lista[n]:
            listaMayor.append(max(lista))

        else:
            listaMayor.append(lista[n])

    return listaMayor

def regresarListaPromedio(lista):
    promedio = int(sum(lista) // len(lista))

    listaPromedio = []

    for n in range(0, len(lista)):

        if lista[n] >= promedio:
            listaPromedio.append(lista[n])

    cantidad = len(listaPromedio)

    return cantidad

def calcularMedia(lista):
    media=sum(lista)/len(lista)

    return media

def calcularDesviacion(media, lista):
    listaNumerador=[]

    for n in range(0,len(lista)):
        a=(lista[n]-media)**2

        listaNumerador.append(a)

    sumaNumerador=sum(listaNumerador)

    desviacion=(sumaNumerador/(len(lista)-1))**(1/2)

    return desviacion

def main():
    # Problema 1: Números pares
    print("Problema 1: Regresar lista con valores pares-----------------------------------")
    print("")
    lista1Pares = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2Pares = [5, 7, 3]
    print("En tu lista:", lista1Pares, "los números:", regresarNumerosPares(lista1Pares), "son pares.")
    print("En tu lista:", lista2Pares, "los números:", regresarNumerosPares(lista2Pares), "son pares.")
    print("")

    # Problema 2: Valores mayores a un elemento previo
    print("Problema 2: Regresar elemento previo si es mayor-------------------------------")
    print("")
    lista1Mayores = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2Mayores = [5, 4, 3, 2]
    print("En tu lista:", lista1Mayores, "los números:", regresarListaMayores(lista1Mayores),
          "son más grandes que el antecesor.")
    print("En tu lista:", lista2Mayores, "los números:", regresarListaMayores(lista2Mayores),
          "son más grandes que el antecesor.")
    print("")

    # Problema 3: Parejas Intercambiadas
    print("Problema 3: Intercambiar pareja de números-------------------------------------")
    print("")
    lista1Pareja = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2Pareja = [1, 2, 3]
    lista3Pareja = [7]
    print("En tu lista:", lista1Pareja, "los números:", regresarListaPareja(lista1Pareja), "fueron invertidos.")
    print("En tu lista:", lista2Pareja, "los números:", regresarListaPareja(lista2Pareja), "fueron invertidos.")
    print("En tu lista:", lista3Pareja, "los números:", regresarListaPareja(lista3Pareja), "fueron invertidos.")
    print("")

    # Problema 4: Intercambiar valores máximos y mínimos
    print("Problema 4: Intercambiar valores máximos y mínimos-----------------------------")
    print("")
    lista1Max = [5, 9, 3, 22, 19, 31, 10, 7]
    lista2Max = [1, 2, 3]
    print("Tu lista:", lista1Max, "regresa esta lista:", regresarListaIntercambioMayor(lista1Max))
    print("Tu lista:", lista2Max, "regresa esta lista:", regresarListaIntercambioMayor(lista2Max))
    print("")

    # Problema 5: Intercambiar valores máximos y mínimos
    print("Problema 5: Regresar los valores arriba del promedio: Intercambiar valores máximos y mínimos-----")
    print("")
    lista1Promedio = [70, 80, 90]
    lista2Promedio = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    print(regresarListaPromedio(lista1Promedio), "valores de la lista:", lista1Promedio, "están arriba del promedio",
          "que es:", int(sum(lista1Promedio) // len(lista1Promedio)))
    print(regresarListaPromedio(lista2Promedio), "valores de la lista:", lista2Promedio, "están arriba del promedio",
          "que es:", int(sum(lista2Promedio) // len(lista2Promedio)))
    print("")

    # Problema 6: Media y derivada
    print("Problema 6: Regresar la media y desviación estándar de las listas:-------------------------------")
    print("")

    lista1md = [1, 2, 3, 4, 5, 6]
    media1 = calcularMedia(lista1md)
    desviacion1 = calcularDesviacion(media1, lista1md)

    lista2md = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    media2 = calcularMedia(lista2md)
    desviacion2 = calcularDesviacion(media2, lista2md)

    print("Le media de tu lista:", lista1md, "es:", media1, "y su desviación es:", desviacion1)
    print("Le media de tu lista:", lista2md, "es:", media2, "y su desviación es:", desviacion2)
    print("")

main()
