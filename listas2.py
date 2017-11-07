# Autor: Saúl rodrigo Toral Luna.
# Matrícula: A01745007

# El porgrama prueba distintos ejercicios en base a problemas relacionados con listas.


#Definimos listas de prueba (constantes)
# Ejercicio 1, listas de prueba
LISTA1 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA2 = [5,7,3]
LISTA3 =[2]
LISTA4 = []
#Ejercicio 2, listas de prueba
LISTA5 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA6 = [5,4,3,2]
LISTA7 = [8]
LISTA8 = []
# Ejercicio 3, listas de prueba
LISTA9 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA10 = [1,2,3]
LISTA11 = [7]
LISTA12 = []
# Ejercicio 4, listas de prueba
LISTA13 = [5,9,3,22,19,31,10,7]
LISTA14 = [1,2,3]
LISTA15 = [3]
LISTA16 = []
# Ejercicio 5, listas de prueba
LISTA17 = [70, 80, 90]
LISTA18 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA19 = [2]
LISTA20 = []
# Ejercicio 6, listas de prueba
LISTA21 = [1,2,3,4,5,6]
LISTA22 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA23 = [3]
LISTA24 = []

# 1.- La función recibe una lista de números enteros y regresa otra lista con los valores pares de la lista original.
def enlistarPares(lista):
    #Se crea una nueva lista
    nueva_Lista = []
    # Ciclo FOR en donde analiza cada elemento de la lista
    for i in range(0, len(lista)):
        # Toma de decisión: de cada valor en la lista, si es par entonces agrega el dato a la nueva lista.
        if lista[i] % 2 == 0:
            nueva_Lista.append(lista[i])
    return nueva_Lista

# 2.- La función recibe una lista y regresa otra con los valores que son mayores a un elemento previo.
def calcularMayoresAPrevio(lista):
    #Se crea una nueva lista
    nueva_Lista2 = []
    for i in range (0,len(lista) -1):
        # Toma de decisión: si el elemento siguiente  es mayor al previo entonces ese mismo dato se agrega a la nueva lista.
        if lista[i+1] > lista[i]:
            nueva_Lista2.append(lista[i+1])
    return nueva_Lista2

# 3.- La función  recibe una lista y regresa una nueva con parejas de datos intercambiados.
def emparejarIntercambiados(lista):
    #Se crea una nueva lista
    nueva_Lista3 = []
    # Ciclo FOR: Analiza los elementos de la lista en parejas
    for i in range(0,len(lista) -1,2):
        # De los elementos de la lista se agrega a la nueva lista el segundo valor primero.
        nueva_Lista3.append(lista[i+1])
        # De los elementos de la lista se agrega a la nueva lista el primer valor despues.
        nueva_Lista3.append(lista[i])
    # Toma de decisión: Si la cantidad de elementos en la lista no es par entonces se agrega el ultimo elemento pues no cambia.
    if  len(lista) % 2 != 0:
        nueva_Lista3.append(lista[-1])
    return nueva_Lista3


# 4.- La función recibe una lista  y regresa otra con el valor menor y mayor intercambiados.
def intercambiarMayoresYMenores(lista):
    # Se hace una subcopia de la lista
    nueva_lista4 = lista[:]
    # Toma de decisión: si la cantidad de elementos en la lista es menor igual a 1 regresa la misma lista.
    if len(lista) <= 1:
        nueva_lista4 = lista[:]
    else:
        # Ubica el valor máximo en índice de la lista
        Indica_Mayor = lista.index(max(lista))
        # Ubica el valor mínimo en indice de la lista
        Indica_Menor = lista.index(min(lista))
        # De la lista nueva se le remueve el mínimo
        nueva_lista4.remove(min(lista))
        # De la lista nueva se le remueve el mínimo
        nueva_lista4.remove(max(lista))
        # A la nueva lista se le inserta aquel valor guardado en previas variables, (cambia el lugar) (donde estaba el menor se agrega el valor mayor y visceversa)
        nueva_lista4.insert(Indica_Mayor - 1, min(lista))
        nueva_lista4.insert(Indica_Menor, max(lista))
    return nueva_lista4


# 5.- L función recibe una lista y regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.
def calcularMayoresIguales(lista):
    # Inicializa un contador
    contador = 0
    #Toma de decisión: Si la cantidad de elementos en la lista es igual a 0
    if len(lista) == 0:
        contador = 0
    else:
        # Si no, entonces realiza una operación para calcular el promedio
        promedio_de_Lista = sum(lista) / len(lista)
        #Ciclo FOR: analiza cada elemento de la lista
        for i in range(0,len(lista)):
            # Si el elemento de las lista es mayor al promedio entonces se le suma al contador 1
            if lista[i] >= promedio_de_Lista:
                contador += 1
    return contador



#  6.- La función recibe una lista y regresa una dupla con la media y la desviación estándar.
def regresarDuplas(lista):
    #Se crea una nueva lista
    nueva_Lista6 = []
    sumatoria = 0
    # Toma de decisión: si la cantidad de elementos de la lista es igual a 0 o a 1 entonces a la nueva lista se le agrega 0 en media y desviación
    if len(lista) == 0 or len(lista) == 1:
        nueva_Lista6 = [0,0]
    else:
        # Calcula la media por medio de la formula
        media_Lista6 = sum(lista) / len(lista)
        # Ciclo FOR:elementos en la lista.
        for i in lista:
            # Se hace la sumatoria de los elementos de la lista
            sumatoria += (i-media_Lista6)**2
        # se saca la desviación típica de los elementos
        desviacion_Lista6 = (sumatoria / (len(lista)-1))**(1/2)
        # A la nueva lista se le agrega la media y desviación estandar
        nueva_Lista6.append(media_Lista6)
        nueva_Lista6.append(desviacion_Lista6)

    return nueva_Lista6

# Función principal donde se llama a las demas funciones
def main():
        # Mientras el ejercicio siga teniendo el valor de verdadero este seguira repitiendo procesos hasta que se vuelva falso
        ejercicio = True
        # Ciclo "while" permite repetir los procesos "n" cantidad de veces hasta que deje de cumplir la condición
        while ejercicio == True:
            # Se muestran los ejercicios a resolver
            print("Tarea 7.2.- Seleccione que quiere hacer.")
            print("")
            print("1. Lista: Valores pares.")
            print("2. Lista: Valores que son mayores al elemento previo.")
            print("3. Lista: Pareja de datos intercambiados.")
            print("4. Lista: Intercambio de mayor y menor.")
            print("5. Lista: Datos mayores o iguales al promedio.")
            print("6. Lista: Desviación y media.")
            print("0. Salir.")

            # Ingresa lo que el usuario desea hacer
            hacer = int(input("¿Qué desea hacer?: "))
            print("")

            # Por medio de decisiones se evalua y muestra el ejercicio deseado
            if hacer == 1:
                print("Problema 1. Regresa una lista con los valores pares de la lista original.")
                print("")
                print("Con la lista", LISTA1, "regresa", enlistarPares(LISTA1))
                print("Con la lista", LISTA2, "regresa", enlistarPares(LISTA2))
                print("Con la lista", LISTA3, "regresa", enlistarPares(LISTA3))
                print("Con la lista", LISTA4, "regresa", enlistarPares(LISTA4))
                print("---------------------------------------------------------")
                print("")

            elif hacer == 2:
                print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo.")
                print("")
                print("Con la lista", LISTA5, "regresa", calcularMayoresAPrevio(LISTA5))
                print("Con la lista", LISTA6, "regresa", calcularMayoresAPrevio(LISTA6))
                print("Con la lista", LISTA7, "regresa", calcularMayoresAPrevio(LISTA7))
                print("Con la lista", LISTA8, "regresa", calcularMayoresAPrevio(LISTA8))
                print("---------------------------------------------------------")
                print("")

            elif hacer == 3:
                print("Problema 3. Regresa una lista con cada pareja de datos intercambiados.")
                print("")
                print("Con la lista", LISTA9, "regresa", emparejarIntercambiados(LISTA9))
                print("Con la lista", LISTA10, "regresa", emparejarIntercambiados(LISTA10))
                print("Con la lista", LISTA11, "regresa", emparejarIntercambiados(LISTA11))
                print("Con la lista", LISTA12, "regresa", emparejarIntercambiados(LISTA12))
                print("---------------------------------------------------------")
                print("")

            elif hacer == 4:
                print("Problema 4. Regresa una lista con el valor menor y mayor intercambiados.")
                print("")
                print("Con la lista", LISTA13, "regresa", intercambiarMayoresYMenores(LISTA13))
                print("Con la lista", LISTA14, "regresa", intercambiarMayoresYMenores(LISTA14))
                print("Con la lista", LISTA15, "regresa", intercambiarMayoresYMenores(LISTA15))
                print("Con la lista", LISTA16, "regresa", intercambiarMayoresYMenores(LISTA16))
                print("---------------------------------------------------------")
                print("")

            elif hacer == 5:
                print("Problema 5. Regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.")
                print("")
                print("Con la lista", LISTA17, "regresa", calcularMayoresIguales(LISTA17), "elementos que son mayores o iguales al promedio.")
                print("Con la lista", LISTA18, "regresa", calcularMayoresIguales(LISTA18), "elementos que son mayores o iguales al promedio.")
                print("Con la lista", LISTA19, "regresa", calcularMayoresIguales(LISTA19), "elementos que son mayores o iguales al promedio.")
                print("Con la lista", LISTA20, "regresa", calcularMayoresIguales(LISTA20), "elementos que son mayores o iguales al promedio.")
                print("---------------------------------------------------------")
                print("")
            elif hacer == 6:
                print("Problema 6. Regresa una dupla con la media y la desviación estándar.")
                print("")
                print("Con la lista", LISTA21, "regresa", regresarDuplas(LISTA21))
                print("Con la lista", LISTA22, "regresa", regresarDuplas(LISTA22))
                print("Con la lista", LISTA23, "regresa", regresarDuplas(LISTA23))
                print("Con la lista", LISTA24, "regresa", regresarDuplas(LISTA24))
                print("---------------------------------------------------------")
                print("")
            elif hacer > 6 or hacer < 0:
                print("ERROR: ")
                print("La opción %d es invalida, escoge un número del menú" % hacer)
                print("")
            else:
                ejercicio = False
                print("Gracias por consultar")

main()