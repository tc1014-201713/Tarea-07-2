# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import math

# Función para obtener los valores pares y regresar una nueva lista
def obtenerValoresPares(lista):
    listaNueva = []
    for dato in lista:
        if dato % 2 == 0:
            listaNueva.append(dato)
    return listaNueva

# Función para agregar a una nueva lista los valores que sean mayores a su antecesor
def obtenerNumeroMayorAlAntecesor(lista):
    listaNueva = []
    for x in range(1, len(lista), 1):
        if lista[x] > lista[x-1]:
            listaNueva.append(lista[x])
    return listaNueva

# Función para intercambiar parejas de datos
def intercambiarPareja(lista):
    listaNueva = lista[::1]
    resta = 0
    if len(lista) % 2 == 1:
        resta += 1
    for x in range(0, len(lista)-1-resta, 2):
        intermedio = listaNueva[x]
        listaNueva[x] = listaNueva[x+1]
        listaNueva[x+1] = intermedio
    return listaNueva

# Función que intercambia el valor mayor y el menor
def intercambiarMayorYMenor(lista):
    listaNueva = []
    if len(lista) == 0:
        return listaNueva
    listaNueva = lista[::1]
    numMax = max(listaNueva)
    numMin = min(listaNueva)
    indiceMayor = 0
    indiceMenor = 0
    for x in range(len(listaNueva)):
        if listaNueva[x] == numMax:
            indiceMayor = x
        if listaNueva[x] == numMin:
            indiceMenor = x
    intermedio = listaNueva[indiceMayor]
    listaNueva[indiceMayor] = listaNueva[indiceMenor]
    listaNueva[indiceMenor] = intermedio
    return listaNueva

# Función que crea una nueva lista con los datos mayores a la media
def obtenerDatosMayoresAlPromedio(lista):
    listaNueva = []
    if len(lista) == 0:
        return listaNueva
    promedio = sum(lista) / len(lista)
    for dato in lista:
        if dato >= promedio:
            listaNueva.append(dato)
    return listaNueva

# Función que obtiene la media y desviación estándar de una lista dada
def obtenerPromedioYDesviacion(lista):
    if len(lista) <= 1:
        return (0, 0)
    promedio = sum(lista) / len(lista)
    resultado = 0
    for dato in lista:
        resultado += (dato-promedio)**2
    resultado /= len(lista) - 1
    resultado = math.sqrt(resultado)
    return (promedio, resultado)

#Función principal que prueba con ejemplos varios casos
def main():
    print("Tarea 07-2. Listas. Realiza varios casos para cada una de las funciones")
    print("\nProblema 1.")
    print(obtenerValoresPares([1,2,3,2,4,60,5,8,3,22,44,55]))
    print(obtenerValoresPares([5,7,3]))
    print(obtenerValoresPares([]))

    print("\nProblema 2.")
    print(obtenerNumeroMayorAlAntecesor([1,2,3,2,4,60,5,8,3,22,44,55]))
    print(obtenerNumeroMayorAlAntecesor([5,4,3,2]))
    print(obtenerNumeroMayorAlAntecesor([]))

    print("\nProblema 3.")
    print(intercambiarPareja([1,2,3,2,4,60,5,8,3,22,44,55]))
    print(intercambiarPareja([1,2,3]))
    print(intercambiarPareja([7]))
    print(intercambiarPareja([]))

    print("\nProblema 4.")
    print(intercambiarMayorYMenor([5,9,3,22,19,31,10,7]))
    print(intercambiarMayorYMenor([1,2,3]))
    print(intercambiarMayorYMenor([]))

    print("\nProblema 5.")
    print(obtenerDatosMayoresAlPromedio([70,80,90]))
    print(obtenerDatosMayoresAlPromedio([95,21,73,24,15,69,71,80,49,100,85]))
    print(obtenerDatosMayoresAlPromedio([]))

    print("\nProblema 6.")
    print(obtenerPromedioYDesviacion([1, 2, 3, 4, 5, 6]))
    print(obtenerPromedioYDesviacion([95,21,73,24,15,69,71,80,49,100,85]))
    print(obtenerPromedioYDesviacion([]))




main()