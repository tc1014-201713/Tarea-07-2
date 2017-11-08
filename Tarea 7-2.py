# Autor: Mónica Monserrat Palacios Rodríguez
# encoding: UTF-8
# Tarea 7.2

#Función que crea una lista con solo los pares a través de un for y un if
def crearListaConPares(lista):
    nuevaLista=[]
    for dato in lista:
        if dato%2==0:
            nuevaLista.append(dato)
    return nuevaLista

#Función que encuentra el mayor de los pares y regresa una nueva lista con datos invertidos
def encontrarMayorPrevio(lista):
    nuevaLista = []
    for dato in range(0, len(lista) -1):
        if lista[dato] < lista[dato+1]:
            nuevaLista.append(lista[dato +1])
    return nuevaLista

#Función que intercambia los datos de una lista dependiendo de si es par o impar para el último elemento
def crearListaConIntercambioDeDatos(lista):
    nuevaLista = []
    impar = 0
    par = 1
    if len(lista) % 2 == 0:
        for k in range(len(lista) // 2):
            nuevaLista.append(lista[par])
            nuevaLista.append(lista[impar])
            impar += 2
            par += 2
    else:
        for k in range(len(lista) // 2):
            nuevaLista.append(lista[par])
            nuevaLista.append(lista[impar])
            impar += 2
            par += 2
        nuevaLista.append(lista[-1])
    return nuevaLista

#Función que intercambia el mayor y el menor de los datos de la lista creando una nueva lista
def intercambiarMayorYMenor(lista):
    nuevaLista = []
    for dato  in range(0,len(lista)):
        if max(lista) == lista[dato]:
            nuevaLista.append(min(lista))
        elif min(lista) == lista[dato]:
            nuevaLista.append(max(lista))
        else:
            nuevaLista.append(lista[dato])
    return nuevaLista

#Función que calulca el promedio de una lista y checa cuántas veces se encuentra un dato mayor o igual al promedio
def calcularPromedioDeLista(lista):
    veces = 0
    promedio = sum(lista) / len(lista)

    for dato in range(0,len(lista)):
        if lista[dato] >= promedio:
            veces += 1
    return veces

#Función que calcula la media y la deviación de una lista
def calcularMediaYDeviacion(lista):
    media = (sum(lista)/len(lista))
    sumatoria = 0
    for dato in lista:
        sumatoria = sumatoria + (dato - media)**2
    deviacion = (sumatoria/(len(lista)-1))**0.5

    return media, deviacion

def main():
#Se establecen las listas que se usarán como parámetros en las funciones
    pruebaA1 = [1,2,3,22,4,60,5,18,53,82,50,30]
    pruebaA2 = [5,7,3]

    pruebaB1 =[1,2,3,2,4,60,5,8,3,22,44,55]
    pruebaB2 =[5,4,3,2]

    pruebaC1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    pruebaC2 = [1,2,3]
    pruebaC3 = [7]

    pruebaD1 = [5,9,3,22,19,31,10,7]
    pruebaD2 = [1,2,3]

    pruebaE1 = [70, 80, 90]
    pruebaE2 = [95,21,73,24,15,69,71,80,49,100,85]
    promedioE1 = sum(pruebaE1) // len(pruebaE1)
    promedioE2 = sum(pruebaE2) // len(pruebaE2)

    pruebaF1 = [1,2,3,4,5,6]
    pruebaF2 = [95,21,73,24,15,69,71,80,49,100,85]

#Se imprimen los resultados como se describió en la tarea

    print("Bienvenido al programa de listas")
    print("Problema 1. Regresa una lista con valores pares de la lista original")
    print("Con la lista:",pruebaA1,"regresa",crearListaConPares(pruebaA1))
    print("Con la lista:",pruebaA2,"regresa",crearListaConPares(pruebaA2))
    print(" ")

    print("Problema 2. Regresa una nueva lista, con los valores que son mayores a un elemento previo.")
    print("Con la lista:", pruebaB1, "regresa", encontrarMayorPrevio(pruebaB1))
    print("Con la lista:", pruebaB2, "regresa", encontrarMayorPrevio(pruebaB2))
    print(" ")

    print("Problema 3. Regresa una nueva lista con cada pareja de datos intercambiados")
    print("Con la lista:", pruebaC1, "regresa", crearListaConIntercambioDeDatos(pruebaC1))
    print("Con la lista:", pruebaC2, "regresa", crearListaConIntercambioDeDatos(pruebaC2))
    print("Con la lista:", pruebaC3,"regresa", crearListaConIntercambioDeDatos(pruebaC3))
    print(" ")

    print("Problema 4. Regresa una nueva lista con el valor menor y mayor intercambiados")
    print("Con la lista:", pruebaD1, "regresa", intercambiarMayorYMenor(pruebaD1))
    print("Con la lista:", pruebaD2, "regresa", intercambiarMayorYMenor(pruebaD2))
    print(" ")

    print("Problema 5. Regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.")
    print("Con la lista:", pruebaE1, "regresa", calcularPromedioDeLista(pruebaE1),"porque el promedio es",promedioE1,"y hay",calcularPromedioDeLista(pruebaE1), "valores mayores o iguales a", promedioE1)
    print("Con la lista:", pruebaE2, "regresa", calcularPromedioDeLista(pruebaE2),"porque el promedio es",promedioE2,"y hay",calcularPromedioDeLista(pruebaE2), "valores mayores o iguales a", promedioE2)
    print(" ")

    print("Problema 6. Regresa una dupla con la media y la desviación estándar")
    print("Con la lista:", pruebaF1, "regresa", calcularMediaYDeviacion(pruebaF1) )
    print("Con la lista:", pruebaF2, "regresa", calcularMediaYDeviacion(pruebaF2))
    print("")

    print("¡Gracias por tu tiempo!")


main() #Se llama a la función main