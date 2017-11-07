#encoding: UTF-8
#Luis Fernando Figueroa Rendon, A01746139
# Programa el cual soluciona diferentes ejercicios utilizando listas.

#Definimos listas de prueba (constantes)
LISTA1 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA2 = [5,7,3]
LISTA3 =[5]
LISTA4 = []
LISTA5 = [5,4,3,2]
LISTA6 = [8]
LISTA7 = [1,2,3]
LISTA8 = [7]
LISTA9 = [5,9,3,22,19,31,10,7]
LISTA10 = [3]
LISTA11 = [70, 80, 90]
LISTA12 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA13 = [2]
LISTA14 = [1,2,3,4,5,6]
LISTA15 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA16= [1, 2]

#Funcion que recibe una lista y regresa los numeros pares.
def sacarPares(lista):
    newlista= []
    for i in range (0,len(lista)):
        if lista[i]%2 == 0:
            newlista.append(lista[i])
    return newlista

#Funcion que regresa los numeros que son mayores al su sucesor.
def calcularMayores(lista):
    nuevalista = []
    for i in range(0, len(lista)-1):
        if lista[i] < lista[i+1]:
            nuevalista.append(lista[i+1])
    return nuevalista

#Funcion que intercambia las duplas de la lista.
def intercambiarDuplas(lista):
    nuevalista = []
    for i in range (0, len(lista)-1, 2):
        nuevalista.append(lista[i+1])
        nuevalista.append(lista[i])
    if len(lista)%2 != 0:
        nuevalista.append(lista[-1])
    return nuevalista

#Funcion que pone al numero mayor de la lista en la posicion del menor y viceversa.
def intercambiarMayoresyMenores(lista):
    nuevalista = lista[:]
    if len(lista)<= 1:
        nuevalista= lista[:]
    else:
        indicemayor=lista.index(max(lista))
        indicemenor=lista.index(min(lista))
        nuevalista.remove(min(lista))
        nuevalista.remove(max(lista))
        nuevalista.insert(indicemayor - 1, min(lista))
        nuevalista.insert(indicemenor, max(lista))
    return nuevalista


#Funcion que saca el promedio de una lista y regresa los valores de la lista que sean mayores o iguales al promedio.
def calcularMedia(lista):
    nuevalista=[]
    if len(lista)> 0:
        promedio= sum(lista)/len(lista)
        for i in range (0, len(lista)):
            if lista[i] >= promedio:
                nuevalista.append(lista[i])
    else:
        nuevalista=[]
    return nuevalista

#Funcion que determina la media y desviacion de una lista.
def calcularMediayDesviacion(lista):
    nuevalista = []
    suma= 0
    if len(lista) > 1:
        promedio = sum(lista) / len(lista)
        for i in lista:
            suma += (i - promedio)**2
        desviacion= suma /(len(lista)-1)
        desviacionraiz=desviacion**.5
        nuevalista.append(promedio)
        nuevalista.append(desviacionraiz)
    else:
        nuevalista=[0, 0]
    return nuevalista




def main():
    #Ejemplos del ejercicio 1.
    print("Ejercicio 1: ")
    print("Con la lista " , LISTA1, ", regresa " ,sacarPares(LISTA1))
    print("Con la lista ", LISTA2, ", regresa ", sacarPares(LISTA2))
    print("Con la lista " , LISTA9, ", regresa " ,sacarPares(LISTA9))
    print("Con la lista ", LISTA10, ", regresa ", sacarPares(LISTA10))
    print("Con la lista ", LISTA4, ", regresa ", sacarPares(LISTA4))
    print("")

    # Ejemplos del ejercicio 2.
    print("Ejercicio 2: ")
    print("Con la lista " , LISTA5, ", regresa " ,calcularMayores(LISTA5))
    print("Con la lista ", LISTA12, ", regresa ", calcularMayores(LISTA12))
    print("Con la lista " , LISTA7, ", regresa " ,calcularMayores(LISTA7))
    print("Con la lista ", LISTA8, ", regresa ", calcularMayores(LISTA8))
    print("Con la lista ", LISTA4, ", regresa ", calcularMayores(LISTA4))
    print("")

    # Ejemplos del ejercicio 3.
    print("Ejercicio 3: ")
    print("Con la lista ", LISTA9, ", regresa ", intercambiarDuplas(LISTA9))
    print("Con la lista ", LISTA10, ", regresa ", intercambiarDuplas(LISTA10))
    print("Con la lista ", LISTA11, ", regresa ", intercambiarDuplas(LISTA11))
    print("Con la lista ", LISTA12, ", regresa ", intercambiarDuplas(LISTA12))
    print("Con la lista ", LISTA4, ", regresa ", intercambiarDuplas(LISTA4))
    print("")

    # Ejemplos del ejercicio 4.
    print("Ejercicio 4: ")
    print("Con la lista ", LISTA12, ", regresa ", intercambiarMayoresyMenores(LISTA12))
    print("Con la lista ", LISTA13, ", regresa ", intercambiarMayoresyMenores(LISTA13))
    print("Con la lista ", LISTA14, ", regresa ", intercambiarMayoresyMenores(LISTA14))
    print("Con la lista ", LISTA9, ", regresa ", intercambiarMayoresyMenores(LISTA9))
    print("Con la lista ", LISTA4, ", regresa ", intercambiarMayoresyMenores(LISTA4))
    print("")

    # Ejemplos del ejercicio 5.
    print("Ejercicio 5: ")
    print("Con la lista ", LISTA1, ", regresa ", calcularMedia(LISTA1))
    print("Con la lista ", LISTA6, ", regresa ", calcularMedia(LISTA6))
    print("Con la lista ", LISTA9, ", regresa ", calcularMedia(LISTA9))
    print("Con la lista ", LISTA12, ", regresa ", calcularMedia(LISTA12))
    print("Con la lista ", LISTA4, ", regresa ", calcularMedia(LISTA4))
    print("")

    #Ejemplos del ejercicio 6.
    print("Ejercicio 6: ")
    print("Con la lista ", LISTA12, ", regresa ", calcularMediayDesviacion(LISTA12))
    print("Con la lista ", LISTA2, ", regresa ", calcularMediayDesviacion(LISTA2))
    print("Con la lista ", LISTA9, ", regresa ", calcularMediayDesviacion(LISTA9))
    print("Con la lista ", LISTA14, ", regresa ", calcularMediayDesviacion(LISTA14))
    print("Con la lista ", LISTA4, ", regresa ", calcularMediayDesviacion(LISTA4))
    print("Con la lista ", LISTA6, ", regresa ", calcularMediayDesviacion(LISTA6))
    print("")


main()