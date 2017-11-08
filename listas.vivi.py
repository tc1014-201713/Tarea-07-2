# encoding: utf-8
#Autor: viviana osorio nieto
#tarea 7.2
def SaberPares (lista,lista3,lista5): # regresa una nueva lista con los numeros pares de otra.
    lista2 =[]
    lista4 = []
    lista6= []
    for elemento in lista:
        if elemento %2 == 0:
            lista2.append(elemento)
    print("con la lista",lista,"regresa",lista2)
    for elemento in lista3:
        if elemento %2 == 0:
            lista4.append(elemento)
    print("con la lista",lista3,"regresa",lista4)
    for elemento in lista5:
        if elemento %2 == 0:
            lista6.append(elemento)
    print("con la lista",lista5,"regresa",lista6)

def calcularMayor(lista,lista3,lista5): #Calcula si el numero anterior es mayor o no y si no, lo pone en una nueva lista.
    lista2 = []
    lista4 = []
    lista6 = []
    for elemento in range(0, len(lista) - 1):
        primero = lista[elemento]
        segundo = lista[elemento + 1]
        if primero < segundo:
            lista2.append(segundo)

    print("con la lista",lista,"regresa",lista2)

    for elemento in range(0, len(lista3) - 1):
        primero = lista3[elemento]
        segundo = lista3[elemento + 1]
        if primero < segundo:
            lista4.append(segundo)

    print("con la lista",lista3,"regresa",lista4)

    for elemento in range(0, len(lista5) - 1):
        primero = lista5[elemento]
        segundo = lista5[elemento + 1]
        if primero < segundo:
            lista6.append(segundo)

    print("con la lista",lista5,"regresa",lista6)



def CalcularParesIntercam(lista,lista3,lista5): # intercambia de lugar pres de numeros.
    lista2 = []
    lista4 = []
    lista6 = []
    if len(lista) % 2 == 0:
        for i in range(0, len(lista), 2):
            lista2.append(lista[i + 1])
            lista2.append(lista[i])
        else:
            if len(lista) % 2 != 0:
                for i in range(0, len(lista) - 1, 2):
                    lista2.append(lista[i + 1])
                    lista2.append(lista[i])
                for i in range(0, len(lista)):
                    lista2.append(lista[len(lista)])
    print("con la lista",lista,"regresa",lista2)

    if len(lista3) % 2 == 0:
        for i in range(0, len(lista3), 2):
            lista4.append(lista3[i + 1])
            lista4.append(lista3[i])
        else:
            if len(lista3) % 2 != 0:
                for i in range(0, len(lista3) - 1, 2):
                    lista4.append(lista3[i + 1])
                    lista4.append(lista3[i])
                for i in range(0, len(lista3)):
                    lista4.append(lista3[len(lista3)])
    print("con la lista",lista3,"regresa",lista4)

    if len(lista5) % 2 == 0:
        for i in range(0, len(lista5), 2):
            lista6.append(lista5[i + 1])
            lista6.append(lista5[i])
        else:
            if len(lista5) % 2 != 0:
                for i in range(0, len(lista) - 1, 2):
                    lista6.append(lista5[i + 1])
                    lista6.append(lista5[i])
                for i in range(0, len(lista5)):
                    lista6.append(lista5[len(lista5)])
    print("con la lista",lista5,"regresa",lista6)

def CalcularMayorMinimo(lista,lista3): #regresa un anueva lista con los valores mayores y minimos intercambiados.
    lista2 = []
    lista4 = []
    for i in range(len(lista) - 1, len(lista)):
        lista2.append(lista[i])
    for i in range(1, len(lista) - 1):
        lista2.append(lista[i])

    lista2.append(lista[0])

    print("con la lista",lista,"regresa",lista2)

    for i in range(len(lista3) - 1, len(lista3)):
        lista4.append(lista3[i])
    for i in range(1, len(lista3) - 1):
        lista4.append(lista3[i])

    lista4.append(lista3[0])

    print("con la lista",lista3,"regresa",lista4)





def CalcularMayorAlProm(lista,lista3,lista5): # regresa el numero de numeros que son mayores al promedio.
    lista2 = []
    lista4 = []
    lista6 = []
    for i in range(0, len(lista)):
        prom = sum(lista) / len(lista)
        if lista[i] >= prom:
            lista2.append(lista[i])
            print("los numeros mayores o iguales al promedio son:",len(lista2))

    for i in range(0, len(lista3)):
        prom = sum(lista3) / len(lista3)
        if lista3[i] >= prom:
            lista4.append(lista3[i])
            print("los numeros mayores o iguales al promedio son:",len(lista4))

    for i in range(0, len(lista5)):
        prom = sum(lista5) / len(lista5)
        if lista5[i] >= prom:
            lista6.append(lista5[i])
            print("los numeros mayores o iguales al promedio son:",len(lista6))



def CalcularMedia(lista,lista3,lista5): # calcula la desviacion de una lista.
    media = 0
    if len(lista) > 1:
        media = sum(lista) / len(lista)
        suma = 0
        for i in lista:
            suma += (i- media)**2
        x = suma / (len(lista) - 1)
        print("la desviacion con la lista",lista,"es: ",x**.5)

    else:
       print("la desviasion con la lista",lista,"es 0 ")

    if len(lista3) > 1:
        media = sum(lista3) / len(lista3)
        suma = 0
        for i in lista3:
            suma += (i - media) ** 2
        x = suma / (len(lista3) - 1)
        print("la desviacion con la lista", lista3,"es: ", x ** .5)

    else:
        print("la desviasion con la lista", lista3,"es: 0")

    if len(lista5) > 1:
        media = sum(lista5) / len(lista5)
        suma = 0
        for i in lista5:
            suma += (i - media) ** 2
        x = suma / (len(lista5) - 1)
        print("la desviacion con la lista", lista5, "es: ", x ** .5)

    else:
        print("la desviasion con la lista", lista5, "es: 0")




def main ():
    print("1- regresa los valores pares de una lista en otra lista")  # menu para elegir numero
    print("2- regresa los valores mayor al ultimo en una nueva lista")
    print("3- regresa una nueva lista con los pares intercambiados")
    print("4-regresa un anueva lista con los valores mayores y minimos intercambiados ")
    print("5-regresa na nueva lista con los valores igual o mayores del promedio")
    print("6- regresa la medio y derivacion estandar ")
    print("7-salir")
    numero= int(input("teclea un numero: "))
    lista = [1,2,3,4,5,6,7]   # lista ejemplo
    lista3 =[34,56,24,3,7]     #lista ejemplo
    lista5 = []               # lista ejemplo
    while numero !=7:  #mientras no ha salido el usuario
        if numero == 1:
            SaberPares(lista,lista3,lista5)
        elif numero == 2:
            calcularMayor(lista,lista3,lista5)
        elif numero == 3:
            CalcularParesIntercam(lista,lista3,lista5)
        elif numero == 4:
            CalcularMayorMinimo (lista,lista3)
        elif numero == 5:
            CalcularMayorAlProm(lista,lista3,lista5)
        elif numero == 6:
            CalcularMedia(lista,lista3,lista5)
        print("1- regresa los valores pares de una lista en otra lista")    # se repite el menu para que no acabe hasta que se le de 7.
        print("2- regresa los valores mayor al ultimo en una nueva lista")
        print("3- regresa una nueva lista con los pares intercambiados")
        print("4-regresa un anueva lista con los valores mayores y minimos intercambiados ")
        print("5-regresa na nueva lista con los valores igual o mayores del promedio")
        print("6- regresa la medio y derivacion estandar ")
        print("7-salir")
        numero = int(input("teclea un numero: "))
    if numero == 7:        # el usuario quiere salir
        print("gracias vuelva pronto \(^.^)/ ")

main()