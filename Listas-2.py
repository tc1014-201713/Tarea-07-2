#Autor: Leonardo Castillejos Vite
#encode: UTF-8
#Descripción: Tarea 2 de listas

#Regresa los número pares de la lista dada
def regresarPares(lista):
    listapar = []
    for k in lista:
        if k%2 == 0:
            listapar.append(k)
    return listapar

# Regresa una lista con los valores que son mayores a un elemento previo
def listarMayores(lista):
    listamayores = []
    for k in range(len(lista)):
        if k != 0:
            if lista[0 +(k - 1)] < lista[1 + (k - 1)]:
                listamayores.append(lista[1 + (k -1)])
    return listamayores

#Regresa una lista con los volteados en parejas
def voltearValores(lista):
    listaVolteada = []
    if len(lista) != 0:
        if len(lista)%2 == 0:
            for k in range(int(len(lista)/2)):
                listaVolteada.append(lista[1 + (k * 2)])
                listaVolteada.append(lista[0 + (k * 2)])
        else:
            for k in range(int((len(lista))/2)):
                listaVolteada.append(lista[1 + (k * 2)])
                listaVolteada.append(lista[0 + (k * 2)])
            listaVolteada.append(lista[len(lista)-1])
    return listaVolteada

#Regresa una lista con el valor mayor y el menor intercambiados de lugar
def intercambiarMenorMayor(lista):
    listaNueva = []
    if lista != listaNueva:
        indiceMenor = lista.index(min(lista))
        indiceMayor = lista.index(max(lista))

        for k in lista:
            if k == max(lista):
                listaNueva.append(lista[indiceMenor])
            elif k == min(lista):
                listaNueva.append(lista[indiceMayor])
            else:
                listaNueva.append(k)
    return listaNueva

#Regresa el promedio y el número de valores que son mayores o iguales al promedio
def evaluarMayoralPromedio(lista):
    mayores = 0
    if lista != []:
        promedio = sum(lista) / len(lista)
        for k in lista:
            if k >= promedio:
                mayores += 1
    return mayores

#Regresa el promedio y la desviación estándar
def calcularMediayDesviacion(lista):
    if len(lista) < 2:
        return (0,0)
    else:
        diferencia = []
        promedio = sum(lista) / len(lista)
        for k in lista:
            valor = (k - promedio)**2
            diferencia.append(valor)
        desviacion = sum(diferencia)/(len(lista)-1)
        desviacion = desviacion ** 0.5
    return (promedio,desviacion)



#Prueba las otras funciones del programa
def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa", regresarPares([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista [5,7,3], regresa",regresarPares([5,7,3]))
    print('\n' "Problema 2. Regresa una lista con los valores que son mayores a un elemento previo")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa", listarMayores([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista [5,4,3,2], regresa", listarMayores([5,4,3,2]))
    print("Con la lista [], regresa", listarMayores([]))
    print('\n' "Problema 3. Regresa una lista con los volteados en parejas")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa", voltearValores([1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]))
    print("Con la lista [1,2,3], regresa", voltearValores([1,2,3]))
    print("Con la lista [7], regresa", voltearValores([7]))
    print("Con la lista [0], regresa", voltearValores([0]))
    print('\n' "Problema 4. Regresa una lista con el valor mayor y el menor intercambiados de lugar")
    print("Con la lista [5,9,3,22,19,31,10,7], regresa", intercambiarMenorMayor([5,9,3,22,19,31,10,7]))
    print("Con la lista [1,2,3], regresa", intercambiarMenorMayor([1,2,3]))
    print("Con la lista [1], regresa", intercambiarMenorMayor([1]))
    print("Con la lista [], regresa", intercambiarMenorMayor([]))
    print('\n' "Problema 5. Regresa el promedio y el número de valores que son mayores o iguales al promedio")
    print("La lista [70,80,90], tiene", evaluarMayoralPromedio([70,80,90]),"número(s) mayor(es) o igual(es) al promedio")
    print("La lista [], tiene", evaluarMayoralPromedio([]), "número(s) mayor(es) o igual(es) al promedio")
    print("La lista [95, 21, 73,24,15,69,71,80,49,100,85], tiene", evaluarMayoralPromedio([95,21,73,24,15,69,71,80,49,100,85]), "número(s) mayor(es) o igual(es) al promedio")
    print('\n' "Problema 6. Regresa el promedio y la desviación estándar")
    print("Con la lista [1,2,3,4,5,6], regresa", calcularMediayDesviacion([1,2,3,4,5,6]))
    print("Con la lista [95,21,73,24,15,69,71,80,49,100,85], regresa", calcularMediayDesviacion([95,21,73,24,15,69,71,80,49,100,85]))
    print("Con la lista [3], regresa",calcularMediayDesviacion([3]))


main()
