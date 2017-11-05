#encoding:UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que posee diferentes funciones que manean listas de python de manera distinta

#Funcion que crea una lista con solamente los pares de la lista que recibe
def diferenciarpares(listaoriginal):
    listapares = []
    for x in listaoriginal:
        if x % 2 == 0:
            listapares.append(x)
    return listapares

#Funcion que regresa una lista con los valores que son mayores al previo en una lista nueva
def determinarmayoralprevio(listaoriginal):
    listamayores = []
    for x in range (0,len(listaoriginal)-1):
        if listaoriginal[x]<listaoriginal[x+1]:
            listamayores.append(listaoriginal[x+1])
    return listamayores

#Funcion que intercambia los nuemros de dos en dos y regresa una lista nueva
def intercambiarparejas(listaoriginal):
    listaintercambiados = []
    if len(listaoriginal) % 2 == 0:
        for x in range(0, len(listaoriginal),2):
            listaintercambiados.append(listaoriginal[x+1])
            listaintercambiados.append(listaoriginal[x])
        return listaintercambiados
    else:
        for x in range(0, len(listaoriginal)-1,2):
            listaintercambiados.append(listaoriginal[x+1])
            listaintercambiados.append(listaoriginal[x])
        listaintercambiados.append(listaoriginal[len(listaoriginal)-1])
        return listaintercambiados

#Funcion que intercambia el mayor y al menor entre ellos de lugar y regresa una nueva lista
def intercambiarmayormenor(listaoriginal):
    nuevalista = listaoriginal[:]
    lugarmayor = nuevalista.index(max(nuevalista))
    lugarmenor = nuevalista.index(min(nuevalista))
    maximo = max(nuevalista)
    minimo = min(nuevalista)
    nuevalista.remove(minimo)
    nuevalista.remove(maximo)
    nuevalista.insert(lugarmayor, minimo)
    nuevalista.insert(lugarmenor, maximo)
    return nuevalista

#Funcion que calcula el promedio de los valores dentro de una lista y regresa cuantos valores estan por encima de ese número
def compararconpromedio(listaoriginal):
    promedio = sum(listaoriginal)/len(listaoriginal)
    contador = 0
    for x in listaoriginal:
        if x >= promedio:
            contador += 1
    return contador

#Funcion que calcula el promedio y la deviacion de los valores dentro de una lista y los regresa en una dupla
def calcularpromedioydesviacion(listaoriginal):
    if len(listaoriginal) != 0 and len(listaoriginal) != 1:
        promedio = sum(listaoriginal)/len(listaoriginal)
        sumadeladesviacion = 0
        for x in listaoriginal:
            sumadeladesviacion = sumadeladesviacion + (x-promedio)**2
        desviacion = (sumadeladesviacion/(len(listaoriginal)-1))**(1/2)
        return (promedio,desviacion)
    else:
        return (0,0)

#Funcion que llama a las demas funciones y establece las listas con que trabajaran
def main():
    print("Problema 1.")
    listaoriginal = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 25]
    print("Con la lista: ", listaoriginal, ",regresa: ", diferenciarpares(listaoriginal))
    listaoriginal = [3,5,7,9,15]
    print("Con la lista: ", listaoriginal, ",regresa: ", diferenciarpares(listaoriginal))

    print("\nProblema 2.")
    listaoriginal = [1, 2, 45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 65]
    print("Con la lista: ", listaoriginal, ",regresa: ", determinarmayoralprevio(listaoriginal))
    listaoriginal = [5,4,3,2]
    print("Con la lista: ", listaoriginal, ",regresa: ", determinarmayoralprevio(listaoriginal))

    print("\nProblema 3.")
    listaoriginal = [1, 2,45, 3, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 65]
    print("Con la lista: ", listaoriginal, ",regresa: ", intercambiarparejas(listaoriginal))
    listaoriginal = [5, 4, 3, 2, 3, 45, 2, 4, 7, 21, 23]
    print("Con la lista: ", listaoriginal, ",regresa: ", intercambiarparejas(listaoriginal))
    listaoriginal = [5]
    print("Con la lista: ", listaoriginal, ",regresa: ", intercambiarparejas(listaoriginal))

    print("\nProblema 4.")
    listaoriginal = [1, 2, 45, 6, 34, 7, 135, 234, 23, 86, 34, 56, 12, 3, 8, 57, 65]
    print("Con la lista: ", listaoriginal, ",regresa: ", intercambiarmayormenor(listaoriginal))
    listaoriginal = [1,2,3]
    print("Con la lista: ", listaoriginal, ",regresa: ", intercambiarmayormenor(listaoriginal))

    print("\nProblema 5.")
    listaoriginal = [80,100,90]
    print("Con la lista: ", listaoriginal, ",regresa: ", compararconpromedio(listaoriginal))
    listaoriginal = [70,65,89,34,23,75,68,98,100,56,78,93,45]
    print("Con la lista: ", listaoriginal, ",regresa: ", compararconpromedio(listaoriginal))

    print("\nProblema 6.")
    listaoriginal = [1, 2, 3, 4, 5, 6]
    print("Con la lista: ", listaoriginal, ",regresa: ", calcularpromedioydesviacion(listaoriginal))
    listaoriginal = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    print("Con la lista: ", listaoriginal, ",regresa: ", calcularpromedioydesviacion(listaoriginal))
    listaoriginal = []
    print("Con la lista: ", listaoriginal, ",regresa: ", calcularpromedioydesviacion(listaoriginal))
    listaoriginal = [3]
    print("Con la lista: ", listaoriginal, ",regresa: ", calcularpromedioydesviacion(listaoriginal))



main()