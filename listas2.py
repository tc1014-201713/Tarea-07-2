# encoding:UTF-8
# Autor: Carlos Pano Hernández
# Tarea 7-2

def regresarNumerosPares(lista):
    listaPares = [] #Crea nueva lista

    for n in lista:
        if n % 2 == 0:#Verifica que valores son divisibles entre dos.
            listaPares.append(n)#Agrega los valores a la nueva lista.

    return listaPares #Imprime lista

def regresarListaMayores(lista):
    listaMayores = []#Crea nueva lista

    for n in range(0, len(lista) - 1):#Determina el tamaño de la lista y le quita uno para que esté dentro del rango.
        if lista[n + 1] > lista[n]:#Verifica si el numero después del primero(sucesor) es mayor a su antecesor.
            listaMayores.append(lista[n + 1])#Agrega el numeor mayor

    return listaMayores#Regresa nueva lista

def regresarListaPareja(lista):
    listaPareja = []#Crea nueva lista

    if len(lista) % 2 == 0:#Para lista que tienen números pares

        for n in range(0, len(lista) - 1, 2):#Determina el ritmo de cambio de do en dos
            listaPareja.append(lista[n + 1])#Pone el segundo datos antes que el primero
            listaPareja.append(lista[n])#Pone el primer dato

    elif len(lista) == 3:#Para LISTAS QUE TIENEN 3 DÍGITOS SOLAMENTE. NO PROBAR CON MÁS

        for n in range(0, len(lista) - 1, 2):#Determina el ritmo de cambio
            listaPareja.append(lista[n + 1])#Pone el segundo valor en el primero
            listaPareja.append(lista[n])#Pone el primer valor en el segundo lugar.
            listaPareja.append(lista[n - 1])#Imprime el último valor al último

    else:
        listaPareja.append(lista[-1])#Imprime el único valor en la lista nueva.

    return listaPareja

def regresarListaIntercambioMayor(lista):
    listaMayor = []#Crea nueva lista

    for n in range(0, len(lista)):#Determina el tamño de la lista para no pasarse del "range"

        if max(lista) == lista[n]:#Encuentra el número mayor.
            listaMayor.append(min(lista))#Lo pone en el lugar del mínimo

        elif min(lista) == lista[n]:#Encuentra el número menor.
            listaMayor.append(max(lista))#Lo pone en el lugar del mayor

        else:
            listaMayor.append(lista[n])#Agrega los demás valores

    return listaMayor

def regresarListaPromedio(lista):
    promedio = int(sum(lista) // len(lista))#Saca el promedio de la lista

    listaPromedio = []#Crea nueva lista

    for n in range(0, len(lista)):#Determina el tamaño de la lista

        if lista[n] >= promedio:#Determina los números que son mayores al promedio
            listaPromedio.append(lista[n])#Los apila en una lista.

    cantidad = len(listaPromedio)#Calcula el tamaño de la lista

    return cantidad#Regresa la cantidad de números en la lista

def calcularMedia(lista):
    media=sum(lista)/len(lista)#Calcula el promedio con la lista mandada desde main

    return media#Regresa el promedio

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
    desviacion1 = calcularDesviacion(media1, lista1md)#Egrega el promedio y lo manda a la función

    lista2md = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    media2 = calcularMedia(lista2md)
    desviacion2 = calcularDesviacion(media2, lista2md)

    print("Le media de tu lista:", lista1md, "es:", media1, "y su desviación es:", desviacion1)
    print("Le media de tu lista:", lista2md, "es:", media2, "y su desviación es:", desviacion2)
    print("")

main()
