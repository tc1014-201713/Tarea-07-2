#encoding: UTF-8
#Autor: Natalia Meraz Tostado
#Tarea 7-2 listas

def regresarPares():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 57]
    lista2 = []
    for dato in range(0, len(lista)):
        if lista[dato] % 2 == 0:
            lista2.append(lista[dato])
    return lista2


def mayorAnterior():
    lista=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista2=[]
    for dato in range(0, len(lista)):
        if lista[dato] > lista[dato - 1]:
            lista2.append(lista[dato])
    return lista2


def intercambiarParejas():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2=[]
    if len(lista) % 2 != 0:
        for dato in range(0, len(lista), 2):
            lista2.append(lista[dato+1])
            lista2.append(lista[dato])
        return lista2
    else:
        for dato in range(0, len(lista)-1, 2):
            lista2.append(lista[dato + 1])
            lista2.append(lista[dato])
        return lista2


def intercambiarMayorMenor():
    lista = [5,9,3,22,19,31,10,7]
    lista2=lista[:]
    mayor = 0
    menor = 0
    for dato in range(0,len(lista)):
        if lista2[dato]== max(lista):
            mayor = dato
        elif lista2[dato]==min(lista):
            menor = dato
        numero =  lista2[mayor]
        lista2[mayor]=lista2[menor]
        lista2[menor]=numero
        return lista2


def datosPromedio():
    lista = [70,80,90]
    valor = 0
    for dato in range(0,len(lista)):
        if lista[dato] >= int((sum(lista)/len(lista))):
            valor +=1
    return valor


def calcularDupla():
    lista = [1,2,3,4,5,6]
    lista2 = []
    mean = 0
    desviacion =  0
    if len(lista)>2:
        for dato in range(0,len(lista)):
            mean += lista[dato]
        mean = mean / len(lista)
        lista2.append(mean)
        desviacion += (lista[dato] - mean) ** 2
        desviacion = (desviacion / (len(lista)-1)) **(1/2)
        lista2.append(desviacion)
        return lista2
    else:
        return [0,0]


def main():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    regresarPares()
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista %s regresa %s" % (lista, regresarPares()))
    print("")
    mayorAnterior()
    print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo")
    print("Con la lista %s regresa %s" % (lista, mayorAnterior()))
    print("")
    intercambiarParejas()
    print("Problema 3. Regresa una lista con los valores con cada pareja de datos intercambiados pero si el ulotmo ")
    print("Con la lista %s regresa %s" % (lista, mayorAnterior()))
    print("")
    intercambiarMayorMenor()
    lista = [5, 9, 3, 22, 19, 31, 10, 7]
    print("Problema 4. Regresa una lista con el valor menor y mayor intercambiados")
    print("Con la lista %s regresa %s" % (lista, intercambiarMayorMenor()))
    print("")
    datosPromedio()
    lista = [70, 80, 90]
    print("Problema 5. Regresa el número de datos que son mayores o iguales al promedio de los valores de la lista")
    print("Con la lista %s regresa %s" % (lista, datosPromedio()))
    print("")
    calcularDupla()
    lista=[1,2,3,4,5,6]
    print("Problema 6. Regresa una dupla con la media y la desviación estándar.")
    print("Con la lista %s regresa %s" % (lista, calcularDupla()))
    print("")


main()