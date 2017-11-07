#encoding: UTF-8
# Sebastian Morales Martin
#Tarea 07: Listas

lista1= [1, 2, 4, 5, 60, 40, 8, 9, 5, 99, 654, 653, 6]
lista2 = [1, 25, 5, 6, 5, 45, 45, 45, 35, 99, 78]
lista3 = [1,2,3,5,7,6]
lista4 = [7]
lista5 = [22,44,867,65]
lista6 = []
listaMaster = [lista1, lista2, lista3, lista4, lista5, lista6]


def encontrarPares(lista):      #la función genera una lista nueva en base a la lista proporcionada con sus pares
    nuevaListaPares = []
    for numero in lista:
        if numero % 2 == 0:
            nuevaListaPares.append(numero)
    return nuevaListaPares



def encontrarMayores(lista):   #genera una lista con valores mayores al anterior en la lista
    listaMay = []
    numeroAnterior = 0
    for numero in lista:
        if numero > numeroAnterior:
            listaMay.append(numero)
        numeroAnterior = numero

    return listaMay

def cambioDePares(lista):   # cambia los pares en una función de lugar
    listaCambios = []
    cuenta = 0
    if len(lista) > 1:
        for numero in lista:
            lugar = lista.index(numero)
            if lugar == len(lista):
                listaCambios.append(numero)
            elif lugar % 2 ==1:
                listaCambios.insert(cuenta-1, numero)
            else:
                listaCambios.insert(cuenta, numero)
            cuenta += 1
    return listaCambios


def cambioMinMax(lista):   #intercambia los numeros mínimo y máximo de lugar en la lista
    listaNueva = lista[:]

    if len(lista) > 1:

        valorMin = min(lista)

        valorMax = max(lista)

        posMin = lista.index(valorMin)

        posMax = lista.index(valorMax)

        listaNueva.remove(valorMin)

        listaNueva.insert(posMax, valorMin)

        listaNueva.remove(valorMax)

        listaNueva.insert(posMin, valorMax)



        return (listaNueva)

def encontrarPromedio(lista): #crea una lista con los números máyores al promedio de la lista
    conteoTotal = len(lista)
    if conteoTotal > 0:
        promedio = sum(lista)/conteoTotal
        listaMayores = []
        contador = 0
        for numero in lista:
            if numero >= promedio:
                listaMayores.append(numero)
                contador += 1
        return (contador, promedio, lista)
    else:
        return(0, 0, lista)

def calcularDesviacion(lista):  #calcula la desviación estándar de la lista (pruebas)

    totalLista = len(lista)

    media = 0

    if totalLista > 1:

        media = sum(lista) / totalLista

        suma = 0

        for numero in lista:
            suma += (numero-media)**2
        dentro = suma / (totalLista - 1)
        desviacion = dentro ** .5

    else:
        desviacion = 0

    return(desviacion)









def main():
    print("Ejercicio 1.0: Encontrar los pares dentro de una lista:")
    for numero in listaMaster:
        print("\n Al recibir: ", numero, ", la función regresa: ", encontrarPares(numero), ) # \n es usado para separar los párrafos y asi hacer más "amigable" la lectura del programa

    print("\n-------------------------------------------------------------------------------------------")   #usados para separar los ejercicios y así hacerlos más entendibles

    print("\nEjercicio 2.0: Enlistar los números mayores de la lista en comparacion a los anteriores")
    for numero in listaMaster:
        print("\n Al recibir: ", numero, ", la función regresa: ", encontrarMayores(numero))

    print("\n-------------------------------------------------------------------------------------------")

    print("\nEjercicio 3.0: Intercambia los pares de una lista de lugar")
    for numero in listaMaster:
        print("\n Al recibir: ", numero, ", la función regresa: ", cambioDePares(numero))

    print("\n-------------------------------------------------------------------------------------------")

    print("\nEjercicio 4.0: Intercambiar el número mayor con el menor de la lista")
    for numero in listaMaster:
        print("\n Al recibir: ", numero, ", la función regresa: ", cambioMinMax(numero))

    print("\n-------------------------------------------------------------------------------------------")

    print("\nEjercicio 5.0: Encontrar los valores que son mayores al promedio")
    for numero in listaMaster:
        cont, prome, listFinal = encontrarPromedio(numero)
        print("\nAl recibir", numero, ", la función regresa %d. El promedio es %.2f y hay %d valores iguales o mayores que %.2f"
              % (cont, prome, cont, prome), listFinal)

    print("\n-------------------------------------------------------------------------------------------")

    print("\nEjercicio 6.0: Desviación estándar (arroja hasta 14 decimales)")
    for numero in listaMaster:
        print("\nAl recibir: ", numero, "la función regresa: ", calcularDesviacion(numero))




main()
