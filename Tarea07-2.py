#encoding UTF-8
#AUTOR: Luis Enrique Neri Pérez
#DESCRIPCIÓN: Función Main que demuestra que todas las funciones corren de manera correcta

def devolverPares(lista): #Función que recibe una lista y devuelve una nueva lista con los valores pares de la lista original
    nuevaLista = []
    for dato in lista:
        if dato%2 == 0:
            nuevaLista.append(dato)
    return nuevaLista


def devolverMayores(lista): #Función que recibe una lista y regresa una nueva con los valores que sean mayores que el anterior
    nuevaLista = []
    for k in range (len(lista)-1):
        if lista[k] < lista[k+1]:
            nuevaLista.append(lista[k+1])
    return nuevaLista


def devolverIntercambiados(lista):
    nuevaLista = []
    datoImpar = 0
    datoPar = 1
    if len(lista)%2 == 0:
        for k in range (len(lista)//2):
            nuevaLista.append(lista[datoPar])
            nuevaLista.append(lista[datoImpar])
            datoImpar = datoImpar + 2
            datoPar = datoPar + 2
    else:
        for k in range (len(lista)//2):
            nuevaLista.append(lista[datoPar])
            nuevaLista.append(lista[datoImpar])
            datoImpar = datoImpar + 2
            datoPar = datoPar + 2
        nuevaLista.append(lista[-1])
    return nuevaLista


def devolverIntercambiadosMayor(lista):
    maximo = max(lista)
    minimo = min(lista)
    indiceMax = lista.index(maximo)
    indiceMin = lista.index(minimo)
    lista.remove(maximo)
    lista.remove(minimo)
    lista.insert(indiceMin,maximo)
    lista.insert(indiceMax, minimo)
    return lista


def devolverPromedio(lista):
    promedio = sum(lista)//len(lista)
    nuevaLista = []
    for dato in lista:
        if dato >= promedio:
            nuevaLista.append(str(dato))
    datos = len(nuevaLista)
    if datos == 2:
        cadena = " y "
        cadena = cadena.join(nuevaLista)
    else:
        cadena = ", "
        cadena = cadena.join(nuevaLista)
    return cadena, datos


def devolverDupla(lista):
    if lista == [3] or lista == []:
        return 0,0
    else:
        media = sum(lista)/len(lista)
        sumatoria = 0
        for dato in lista:
            sumatoria = sumatoria + (dato - media)**2
        desviacion = (sumatoria/(len(lista)-1))**0.5
        return media, desviacion


def main(): #Función que demuestra que todas las funciones funcionan correctamente
    print("TAREA 07 PARTE 2")

    print("\nPROBLEMA 1")
    print("---------------------------------")
    prueba1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    prueba2 = [5,7,3]
    res1 = devolverPares(prueba1)
    res2 = devolverPares(prueba2)
    print("La lista",prueba1,"devuelve la lista",res1)
    print("La lista", prueba2, "devuelve la lista", res2)
    
    print("\nPROBLEMA 2")
    print("---------------------------------")
    prueba1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    prueba2 = [5,4,3,2]
    res1 = devolverMayores(prueba1)
    res2 = devolverMayores(prueba2)
    print("La lista", prueba1, "devuelve la lista", res1)
    print("La lista", prueba2, "devuelve la lista", res2)

    print("\nPROBLEMA 3")
    print("---------------------------------")
    prueba1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    prueba2 = [1,2,3]
    prueba3 = [7]
    res1 = devolverIntercambiados(prueba1)
    res2 = devolverIntercambiados(prueba2)
    res3 = devolverIntercambiados(prueba3)
    print("La lista", prueba1, "devuelve la lista", res1)
    print("La lista", prueba2, "devuelve la lista", res2)
    print("La lista", prueba3, "devuelve la lista", res3)

    print("\nPROBLEMA 4")
    print("---------------------------------")
    prueba1 = [5,9,3,22,19,31,10,7]
    dup1 = [5, 9, 3, 22, 19, 31, 10, 7]
    prueba2 = [1,2,3]
    dup2 = [1, 2, 3]
    res1 = devolverIntercambiadosMayor(prueba1)
    res2 = devolverIntercambiadosMayor(prueba2)
    print("La lista", dup1, "devuelve la lista", res1)
    print("La lista", dup2, "devuelve la lista", res2)

    print("\nPROBLEMA 5")
    print("---------------------------------")
    prueba1 = [70, 80, 90]
    prueba2 = [95,21,73,24,15,69,71,80,49,100,85]
    prom1 = sum(prueba1)//len(prueba1)
    cad1, datos1 = devolverPromedio(prueba1)
    prom2 = sum(prueba2) // len(prueba2)
    datos2 = len(prueba2)
    cad2, datos2= devolverPromedio(prueba2)
    print("La lista", prueba1,"devuelve %d datos (%s) que son mayores o iguales al promedio de %d." % (datos1, cad1, prom1))
    print("La lista", prueba2,"devuelve %d datos (%s) que son mayores o iguales al promedio de %d." % (datos2, cad2, prom2))

    print("\nPROBLEMA 6")
    print("---------------------------------")
    prueba1 = [1,2,3,4,5,6]
    prueba2 = [95,21,73,24,15,69,71,80,49,100,85]
    prueba3 = [3]
    prueba4 = []
    m1,dv1 = devolverDupla(prueba1)
    m2,dv2 = devolverDupla(prueba2)
    m3,dv3 = devolverDupla(prueba3)
    m4,dv4 = devolverDupla(prueba4)
    print("La lista", prueba1, "devuelve (%d,%.6f)" %  (m1,dv1))
    print("La lista", prueba2, "devuelve (%d,%.6f)" %  (m2,dv2))
    print("La lista", prueba3, "devuelve (%d,%d)" %  (m3,dv3))
    print("La lista", prueba4, "devuelve (%d,%d)" %  (m4,dv4))

    #devolverDupla()


main()