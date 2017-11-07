#encoding: UTF-8
#Autor: Maria Fernanda Torres Velazquez A01746537
#Tarea 7.2 Ejercicios con listas



def menu(): #Funcion menu
    print ("-------------------------------------------------------")
    print ("                    M  E  N  U                         ")
    print ("-------------------------------------------------------")
    print ("1. Problema 1")
    print ("2. Problema 2")
    print ("3. Problema 3")
    print ("4. Problema 4")
    print ("5. Problema 5")
    print ("6. Problema 6")
    print ("0. S A L I R ")
    print ("")
    opcion=int(input("Por favor ingrese el numero de la opcion que desea:"))
    return (opcion)



def calcularPares(lista): #Funcion que recibe como parametro una lista y devuelve en una nueva los valores pares de la original
    nueva=[]
    for x in lista:
        if x%2==0:
            nueva.append(x)
    return (nueva)


def calcularMayores(lista): #Funcion que recibe una lista y devuelve una nueva con los numeros mayores a los previos
    nueva= []
    for x in range(len(lista)-1):
        if lista[x] < lista[x+1]:
            nueva.append(lista[x+1])

    return (nueva)

def intercambiarValores(lista): #Recibe una lista, y regresa una nueva con las parejas de datos intercambiados, si la longitud de la lista es impar, el ultimo elemento no cambia
    nueva=[]

    if len(lista)%2 == 0:
        for x in range (0,len(lista)-1,2):
            nueva.append(lista[x+1])
            nueva.append(lista[x])
    else:
        for x in range(0,len(lista)-1,2):
            nueva.append(lista[x+1])
            nueva.append(lista[x])
        nueva.append(lista[-1])


    return (nueva)

def intercambiarMayor(lista): #Funcion que recibe una lista e intercambia (en posicion) al numero mayor y menor
    if len(lista)>=1:
        nueva=lista[:]
        mayor= max(lista)
        menor= min(lista)
        ubicacionmayor=nueva.index(mayor)
        ubicacionmenor=nueva.index(menor)
        nueva.remove(mayor)
        nueva.remove(menor)
        nueva.insert(ubicacionmenor,mayor)
        nueva.insert(ubicacionmayor,menor)
    else:
        nueva=[]
    return (nueva)


def compararPromedio(lista): #Funcion que calcula el promedio de la lista recibida y regresa la cantidad de datos iguales o mayores a el
    nueva=[]
    suma= sum(lista)
    promedio= suma/len(lista)
    for x in lista:
        if x>= promedio:
            nueva.append(x)

    datosiguales= len(nueva)

    return (datosiguales)

def calcularMedia(lista): #Funcion que calcula y devuelve la media y desviacion estandar de la lista recibida
    if lista==[3] or lista==[]:
        tupla=(0,0)
    else:
        suma = sum(lista)
        media = suma / len(lista)
        sumatoria=0
        for x in lista:
            sumatoria=sumatoria + (x-media)**2
        desviacionEstandar=(sumatoria/(len(lista)-1))**.5

        tupla=(media,desviacionEstandar)

    return (tupla)


def main (): #Funcion principal
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            print ("")
            print ("Problema 1: Regresa una lista con los valores pares de la lista original")
            print ("")
            lista= [1,2,3,2,4,60,5,8,3,22,44,55]
            nueva= calcularPares(lista)
            print ("Los valores pares de la lista", lista, "son: ",nueva)
            lista2 = [5,7,3]
            nueva2 = calcularPares(lista2)
            print("Los valores pares de la lista", lista2, "son: ", nueva2)
            lista18= []
            nueva18=calcularPares(lista18)
            print("Los valores pares de la lista", lista18, "son: ", nueva18)

        elif opcion == 2:
            print("")
            print("Problema 2: Regresa una lista con los valores que son mayores a los previos en la lista original")
            print("")
            lista3 = [1,2,3,2,4,60,5,8,3,22,44,55]
            nueva3 = calcularMayores(lista3)
            print("Para la lista:", lista3, "los valores mayores a los previos son: ", nueva3)
            lista4 = [5,4,3,2]
            nueva4 = calcularMayores(lista4)
            print("Para la lista:", lista4, "los valores mayores a los previos son: ", nueva4)
            lista19=[]
            nueva19=calcularMayores(lista19)
            print("Para la lista:", lista19, "los valores mayores a los previos son: ", nueva19)


        elif opcion == 3:
            print("")
            print("Problema 3: Recibe una lista de valores y regresa una nueva con las parejas de datos intercambiadas, si la lista es impar")
            print("el ultimo dato no cambia")
            print("")
            lista5= [1,2,3,2,4,60,5,8,3,22,44,55]
            nueva5 = intercambiarValores(lista5)
            print ("De la lista",lista5,"se crea la lista:",nueva5)
            lista6 = [1,2,3]
            nueva6 = intercambiarValores(lista6)
            print("De la lista", lista6, "se crea la lista:", nueva6)
            lista7 = [7]
            nueva7 = intercambiarValores(lista7)
            print("De la lista", lista7, "se crea la lista:", nueva7)
            lista17= []
            nueva17= intercambiarValores(lista17)
            print("De la lista", lista17, "se crea la lista:", nueva17)



        elif opcion == 4:
            print("")
            print("Problema 4: Recibe una lista de valores y regresa una nueva lista con el	valor menor	y mayor	intercambiados")
            print("")
            lista8= [5,9,3,22,19,31,10,7]
            nueva8= intercambiarMayor(lista8)
            print ("De la lista", lista8,"se crea la lista:",nueva8)
            lista9 = [1,2,3]
            nueva9 = intercambiarMayor(lista9)
            print("De la lista", lista9, "se crea la lista:", nueva9)
            lista21=[]
            nueva21=intercambiarMayor(lista21)
            print("De la lista", lista21, "se crea la lista:", nueva21)


        elif opcion==5:
            print("")
            print("Problema 5: Recibe una lista de valores y regresa el número de datos que son")
            print ("mayores o iguales	al	promedio	de	todos	los	valores	de	la	lista.")
            print("")
            lista10 = [70,80,90]
            nueva10 = compararPromedio(lista10)
            print("De la lista", lista10, "hay",nueva10,"dato(s) mayores o iguales al promedio de la lista")
            lista11 = [95,21,73,24,15,69,71,80,49,100,85]
            nueva11 = compararPromedio(lista11)
            print("De la lista", lista11, "hay", nueva11, "dato(s) mayores o iguales al promedio de la lista")




        elif opcion==6:
            print("")
            print("Problema 6: Recibe una lista y regresa una tupla con la media y desviacion estandar de la misma")
            print("")
            lista12 = [1,2,3,4,5,6]
            nueva12 = calcularMedia(lista12)
            print("De la lista", lista12, "la media y desviacion estandar son:", nueva12)
            lista13 = [95,21,73,24,15,69,71,80,49,100,85]
            nueva13 = calcularMedia(lista13)
            print("De la lista", lista13,"la media y desviacion estandar son:", nueva13)
            lista14 = []
            nueva14= calcularMedia(lista14)
            print("De la lista", lista14, "la media y desviacion estandar son:", nueva14)
            lista15= [3]
            nueva15= calcularMedia(lista15)
            print("De la lista", lista15, "la media y desviacion estandar son:", nueva15)

        print("")
        print("")


        opcion = menu()

main()


