#encoding: UTF-8
#Autor: Omar Israel Galván García
#Matrícula: A01745810
#Tarea 07-2

def ejercicioUno(lista):      #función ejercicio 1
    listaA = lista      #se asigna la lista a una nueva lista
    listaB = []     #se crea una lista vacía
    for dato in listaA: #se visita cada uno de los datos
        if dato%2 == 0: #si el dato leído el la lista es par:
            listaB.append(dato)  #agrega el número par a la nueva lista
    return listaB   #regresa la nueva lista con los números pares


def ejercicioDos(lista):        #función ejercicio 2
    listaA = lista  #se asigna la lista de entrada a una nueva variable
    listaB = []     #se crea una nueva lista vacía

    for i in range(0,len(listaA)-1):        #se crea un ciclo for para visitar cada dato por medio de los índices
        if listaA[i] < listaA[i+1]:     #si el valor contenido en el índice i es menor al del índice i+1:
            listaB.append(listaA[i+1])   #agrega el valor mayor a la nueva lista
    return listaB       #regresa una nueva lista

def ejercicioTres(lista):       #funciín ejercicio 3
    listaA = lista      #se asigna la lista a una variable
    listaB = []     #se crea una lista vacía
    indiceImpar = 0     #se crea una variable para controlar el salto de índices impar
    indicePar  = 1      #se crea una variable para controlar el salto de índices par

    if len(listaA)%2 == 0:  #si la longitud de la lista es par:

        for i in range(len(listaA)//2):     #visita cada índice
            listaB.append(listaA[indicePar])        #agrega el nuevo índice impar a la lista
            listaB.append(listaA[indiceImpar])      #agrega el nuevo índice par a la lista
            indicePar += 2      #se incrementa la variable en 2 para hacer el siguiente salto
            indiceImpar += 2        #se incrementa la variable en 2 para hacer el siguiente salto
        return listaB       #regresa la nueva lista con los valores intercambiados

    else:       #si el número de datos es impar invierte los primeros y el último dígito lo deja igual
        for k in range(len(listaA)//2):
            listaB.append(listaA[indicePar])
            listaB.append(listaA[indiceImpar])
            indicePar += 2
            indiceImpar += 2
        listaB.append(listaA[-1])
        return listaB       #regresa la nuevqa lista con los valores intercambiados, menos el último

def ejercicioCuatro(lista):     #función ejercicio 4
    listaA = lista      #se asigna la lista a una nueva variable
    listaB = list(listaA)       #se hace una copia de la lista de entrada

    if len(listaA) >1:      #solo si la longitud de la lista es mayor a 1:
        maximo = max(listaB)        #obtiene el valor mayor de la lista
        minimo = min((listaB))      #obtiene el valor mínimo de la lista
        indiceA = listaB.index(minimo)      #obtiene el índice del valor mayor
        indiceB = listaB.index(maximo)      #obtiene el índice del valor menor
        listaB.remove(maximo)       #borra el valor mayor de la lista
        listaB.remove(minimo)       #borra el valor menor de la lista
        listaB.insert(indiceA,maximo)       #inserta el valor máximo en el lugar donde antes estaba el mímimo en la  nueva lista
        listaB.insert(indiceB,minimo)       #inserta el valor mínimo en el lugar donde antes estaba el máximo en la nueva lista
        return listaB       #regresa una nueva lista con los valores máximos y mínimos intercambiados
    else:
        return listaA       #regresa la lista original


def ejercicioCinco(lista):      #función ejercicio 5
    listaA = lista      #se asigna la lista a una variable
    suma = sum(listaA)      #suma los valores contenidos en la lista original
    if len(listaA)>=1:      #solo si la longitud de la lista es mayor o igual a 1
        promedio = suma//len(listaA)        #obtiene el promedio de los valores contenidos en la lista
        regreso = 0     #variable con el valor deseado
        for dato in listaA:     #visita cada uno de los datos contenidos en la lista
            if dato >= promedio:        #si algún dato es mayor que el promedio
                regreso += 1        #aumenta la variable en 1
        return regreso      #regresa el número de valores que son mayores al promedio de la lista
    else:
        return []   #regresa una lista vacía

def ejercicioSeis(lista):       #función ejercicio 6
    listaA = lista      #se asigna la lista original a una variable

    suma = sum(listaA)      #suma los valores contenidos en la lista
    n = len(listaA)     #cuenta el número de datos que tiene la lista

    if n != 0 and n >1:     #solo si la longitud de la lista es diferente de 0 y mayor a 1:

        desviacionMedia = suma/n    #divide la suma de los valores entre la longitud de la lista
        a = 0   #variable para almacenar los valores

        for numero in listaA:       #visita cada uno de los valores contenidos en la lista
            a += (numero-desviacionMedia)**2        #suma a la variabel "a" la resta de el número contenido en la lista menos el promedio, al cuadrado
        desviacionEstandar = (a/(n-1))**0.5     #calcula la desviación estándar

        return desviacionMedia,desviacionEstandar       #regresa la desviación media y estándar

    else:
        return 0,0      #si no cumple con las condiciones, regresa 0 para ambos casos





def main():     #función principal main
            #ejecuta y prueba cada  uno de los problemas
    print("\n")
    print("Problema 1. Regresa una lista con los valores pares de la lista original")
    print("Con la lista",[1,2,3,2,4,60,5,8,3,22,44,55],"regresa",ejercicioUno([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista",[5,7,3],"regresa",ejercicioUno([5,7,3]))
    print("Con la lista", [1,2,3,4,5,6,7], "regresa", ejercicioUno([1,2,3,4,5,6,7]))
    print("Con la lista", [], "regresa", ejercicioUno([]))
    print("Con la lista", [2], "regresa", ejercicioUno([2]))
    print("\n")
    print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo")
    print("Con la lista",[1,2,3,2,4,60,5,8,3,22,44,55],"regresa",ejercicioDos([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista",[5,4,3,2],"regresa",ejercicioDos([5,4,3,2]))
    print("Con la lista",[1,2,3,4,5],"regresa",ejercicioDos([1,2,3,4,5]))
    print("Con la lista",[10,9,8,1,2,3],"regresa",ejercicioDos([10,9,8,1,2,3]))
    print("Con la lista",[],"regresa",ejercicioDos([]))
    print("\n")
    print("Problema 3. Recibe una lista de valores y regresa una lista con cada pareja de datos intercambiados")
    print("Con la lista",[1,2,3,2,4,60,5,8,3,22,44,55],"regresa",ejercicioTres([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista",[],"regresa",ejercicioTres([]))
    print("Con la lista",[1,2,3],"regresa",ejercicioTres([1,2,3]))
    print("Con la lista",[7],"regresa",[7])
    print("Con la lista",[1,2,3,4,5],"regresa",ejercicioTres([1,2,3,4,5]))
    print("\n")
    print("Problema 4. Recibe una lista y regresa una lista con los valores mayor y menor intercambiados")
    print("Con la lista",[5,9,3,22,19,31,10,7],"regresa",ejercicioCuatro([5,9,3,22,19,31,10,7]))
    print("Con la lista",[1,2,3],"regresa",ejercicioCuatro([1,2,3]))
    print("Con la lista",[2,4,6,8,10],"regresa",ejercicioCuatro([2,4,6,8,10]))
    print("Con la lista",[],"regresa",ejercicioCuatro([]))
    print("Con la lista",[7],"regresa",ejercicioCuatro([7]))
    print("Con la lista",[10,20],"regresa",ejercicioCuatro([10,20]))
    print("\n")
    print("Problema 5. Recibe una lista de valores y regresa una lista con los valores que son iguales o mayores al promedio de todos los valores de la lista")
    print("Con la lista",[70,80,90],"regresa",ejercicioCinco([70,80,90]))
    print("Con la lista",[95,21,73,24,15,69,71,80,49,100,85],"regresa",ejercicioCinco([95,21,73,24,15,69,71,80,49,100,85]))
    print("Con la lista",[4],"regresa",ejercicioCinco([4]))
    print("Con la lista",[],"regresa",ejercicioCinco([]))
    print("Con la lista",[2,4],"regresa",ejercicioCinco([2,4]))
    print("\n")
    print("Problema 6. Recibe una lista de datos y regresa la desviación media y estándar")
    print("Con la lista",[1,2,3,4,5,6],"regresa",ejercicioSeis([1,2,3,4,5,6]))
    print("Con la lista",[95,21,73,24,15,69,71,80,49,100,85],"regresa",ejercicioSeis([95,21,73,24,15,69,71,80,49,100,85]))
    print("Con la lista",[],"regresa",ejercicioSeis([]))
    print("Con la lista",[3],"regresa",ejercicioSeis([3]))
    print("Con la lista",[2,5],"regresa",ejercicioSeis([2,5]))
main()