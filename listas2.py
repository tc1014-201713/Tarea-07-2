# encoding: UTF-8
# Autor: Siham El Khoury Caviedes, A01374764.

# Descripción: Tarea 07-2, programas con uso de listas.

# Resolver problema 1:
def crearListaConPares(lista):
    listaPares = []
    for dato in lista:
        if dato%2 == 0:
            listaPares.append(dato)
    return listaPares


# Resolver problema 2:
def crearListaConMayores(lista):
    listaMayores = []
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            numeroMayor = lista[i+1]
            listaMayores.append(numeroMayor)
    return listaMayores


# Resolver problema 3:
def crearListaConIntercambiosPares(lista):
    if len(lista) == 1 or len(lista) == 0:
        listaIntercambiosPares = lista
    else:
        listaIntercambiosPares = []
        if (len(lista) % 2) == 0:
            for i in range(0, len(lista), 2):
                numero1 = lista[i]
                numero2 = lista[i + 1]
                listaIntercambiosPares.append(numero2)
                listaIntercambiosPares.append(numero1)
        if (len(lista) % 2) != 0:
            for i in range(0, len(lista)-1, 2):
                numero1 = lista[i]
                numero2 = lista[i + 1]
                listaIntercambiosPares.append(numero2)
                listaIntercambiosPares.append(numero1)
            listaIntercambiosPares.append(lista[len(lista)-1])

    return listaIntercambiosPares


# Resolver problema 4:
def crearListaConIntercambios(lista):
    if len(lista) == 0 or len(lista) == 1:
        listaModificada = lista
    else:
        listaModificada = []
        menor = min(lista)
        mayor = max(lista)
        for i in range (len(lista)):
            listaModificada.append(lista[i])
            if lista[i] == menor:
                spotMin = i
            elif lista[i] == mayor:
                spotMax = i
        siguienteMayor = spotMax+1
        siguienteMenor = spotMin+1
        listaModificada.insert(spotMax, menor)
        listaModificada.pop(siguienteMayor)
        listaModificada.insert(spotMin, mayor)
        listaModificada.pop(siguienteMenor)
    return listaModificada


# Resolver problema 5:
def crearListaConMayoresAlPromedio(lista):
    if lista == []:
        listaMayoresAlPromedio = []
    else:
        listaMayoresAlPromedio = []
        promedio = sum(lista) / len(lista)
        for dato in lista:
            if dato >= promedio:
                listaMayoresAlPromedio.append(dato)
    return listaMayoresAlPromedio


# Resolver problema 6:
def crearListaConMediaYDesviacion(lista):
    if len(lista) == 0 or len(lista) == 1:
        listaConMediaYDesviacion = [0, 0]
    else:
        listaConMediaYDesviacion = []
        media = sum(lista) / len(lista)
        listaConMediaYDesviacion.append(media)
        desviacion = 0
        numero = 0
        suma = 0
        for i in range (len(lista)):
            numero = (lista[i] - media)**2 + desviacion
            suma = numero + suma
        desviacion = (suma/(len(lista)-1))**0.5
        listaConMediaYDesviacion.append(desviacion)
    return listaConMediaYDesviacion


# Función principal:
def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print()
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaPares = crearListaConPares(lista)
    print("Con la lista", lista, "regresa", listaPares)
    lista = [5, 7, 3]
    listaPares = crearListaConPares(lista)
    print("Con la lista", lista, ", regresa", listaPares)
    lista = []
    listaPares = crearListaConPares(lista)
    print("Con la lista", lista, ", regresa", listaPares)
    lista = [2]
    listaPares = crearListaConPares(lista)
    print("Con la lista", lista, ", regresa", listaPares)
    lista = [3]
    listaPares = crearListaConPares(lista)
    print("Con la lista", lista, ", regresa", listaPares)
    print()

    print("Problema 2. Regresa una lista con los valores mayores a un elemento previo.")
    print()
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaMayores = crearListaConMayores(lista)
    print("Con la lista", lista, "regresa", listaMayores)
    lista = [5, 4, 3, 2]
    listaMayores = crearListaConMayores(lista)
    print("Con la lista", lista, "regresa", listaMayores)
    lista = []
    listaMayores = crearListaConMayores(lista)
    print("Con la lista", lista, "regresa", listaMayores)
    lista = [5]
    listaMayores = crearListaConMayores(lista)
    print("Con la lista", lista, "regresa", listaMayores)
    print()

    print("Problema 3. Regresa una lista con cada pareja de datos intercambiados.")
    print()
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaIntercambiosPares = crearListaConIntercambiosPares(lista)
    print("Con la lista", lista, "regresa", listaIntercambiosPares)
    lista = [1, 2, 3, 4, 5]
    listaIntercambiosPares = crearListaConIntercambiosPares(lista)
    print("Con la lista", lista, "regresa", listaIntercambiosPares)
    lista = [1, 2, 3]
    listaIntercambiosPares = crearListaConIntercambiosPares(lista)
    print("Con la lista", lista, "regresa", listaIntercambiosPares)
    lista = [7]
    listaIntercambiosPares = crearListaConIntercambiosPares(lista)
    print("Con la lista", lista, "regresa", listaIntercambiosPares)
    lista = []
    listaIntercambiosPares = crearListaConIntercambiosPares(lista)
    print("Con la lista", lista, "regresa", listaIntercambiosPares)
    print()

    print("Problema 4. Regresa una lista con el valor menor y mayor intercambiados.")
    print()
    lista = [5, 9, 3, 22, 19, 31, 10, 7]
    lista2 = crearListaConIntercambios(lista)
    print("Con la lista", lista, "regresa", lista2)
    lista = [1, 2, 3]
    lista2 = crearListaConIntercambios(lista)
    print("Con la lista", lista, "regresa", lista2)
    lista = [5]
    lista2 = crearListaConIntercambios(lista)
    print("Con la lista", lista, "regresa", lista2)
    lista = []
    lista2 = crearListaConIntercambios(lista)
    print("Con la lista", lista, "regresa", lista2)
    print()

    print("Problema 5. Regresa el numero de datos que son mayores o iguales al promedio y una lista dichos valores.")
    print()
    lista = [70, 80, 90]
    listaMayoresAlPromedio = crearListaConMayoresAlPromedio(lista)
    cantidad = len(listaMayoresAlPromedio)
    print("Con la lista", lista, "regresa", cantidad, "valor(es) en la lista", listaMayoresAlPromedio)
    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    listaMayoresAlPromedio = crearListaConMayoresAlPromedio(lista)
    cantidad = len(listaMayoresAlPromedio)
    print("Con la lista", lista, "regresa", cantidad, "valor(es) en la lista", listaMayoresAlPromedio)
    lista = [5]
    listaMayoresAlPromedio = crearListaConMayoresAlPromedio(lista)
    cantidad = len(listaMayoresAlPromedio)
    print("Con la lista", lista, "regresa", cantidad, "valor(es) en la lista", listaMayoresAlPromedio)
    lista = []
    listaMayoresAlPromedio = crearListaConMayoresAlPromedio(lista)
    cantidad = len(listaMayoresAlPromedio)
    print("Con la lista", lista, "regresa", cantidad, "valor(es) en la lista", listaMayoresAlPromedio)
    print()

    print("Problema 6. Regresa una dupla con la media y la desviación estándar.")
    print()
    lista = [1, 2, 3, 4, 5, 6]
    listaConMediaYDesviacion = crearListaConMediaYDesviacion(lista)
    print("Con la lista", lista, "regresa", listaConMediaYDesviacion)
    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    listaConMediaYDesviacion = crearListaConMediaYDesviacion(lista)
    print("Con la lista", lista, "regresa", listaConMediaYDesviacion)
    lista = [3]
    listaConMediaYDesviacion = crearListaConMediaYDesviacion(lista)
    print("Con la lista", lista, "regresa", listaConMediaYDesviacion)
    lista = []
    listaConMediaYDesviacion = crearListaConMediaYDesviacion(lista)
    print("Con la lista", lista, "regresa", listaConMediaYDesviacion)

main()