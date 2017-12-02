#encoding: UTF-8
#Autor: Jean Paul Esquivel Lobato
#Matrícula: A01376152
#Descripción: Realiza diferentes operaciones con listas

def devuelvePares(lista):
    nuevalista = []
    for i in range (0,len(lista)):
        if lista[i] % 2 == 0:
            nuevalista.append(lista[i])
    return nuevalista


def mayor(mayor):
    mayor = []
    for i in range(0, len(mayor) -1):
        if mayor[i] < mayor[i +1]:
            mayor.append(mayor[i +1])
    return mayor


def juntarIntercambiar(lista):
    nuevalista = []
    for i in range(0, len(lista) -1, 2):
        nuevalista.append(lista[i +1])
        nuevalista.append(lista[i])
    if len(lista) % 2 !=0:
        nuevalista.append(lista[-1])
    return nuevalista


def cambiarLista(lista):
    nuevalista = []
    for i in range(0,len(lista)):
        if max(lista) == lista[i]:
            nuevalista.append(min(lista))
        elif min(lista) == lista[1]:
            nuevalista.append(max(lista))
        else:
            nuevalista.append(lista[i])
        return nuevalista


def calcularlista(lista):
    contador = 0
    for i in range(0,len(lista)):
        if lista[1] >= (sum(lista)/len(lista)):
            contador += 1
    return contador


def hacerDesviacion(lista):
    regreso = []
    mean = 0
    desviacion = 0
    if len(lista) > 2:
        for i in range(0,len(lista)):
            mean += lista[i]
        mean = mean / len(lista)
        regreso.append(mean)
        for i in range(0,len(lista)):
            desviacion += (lista[i] - mean) **2
        desviacion = (desviacion / (len(lista)-1))**(1/2)
        regreso.append(desviacion)
        return regreso
    else:
        return [0,0]


def menu():
    print('''
         1. Regresar una lista con los valores pares.
         2. Regresar una lista con los valores mayores al interior.
         3. Regresar una lista con los valores se intercambiados de dos en dos.
         4. Regresar una lista con valores donde mayor y menor se intercambian.
         5. Función que decuelve un numero, el cual es la cantidad de elementos mayores al promedio
         6.Función que regresa una dupla, la cual devuelve la media y la desviacion estandar.
         0.- salir
         ''' )
    respuesta = int(input("Elige una opción:"))
    print ("")
    return respuesta

def main():
    lista = [[], [1,2,3,2,4,60,5,8,3,22,44,55],[5,7,3], [5,4,3,2],[1,2,3],[7],[5,9,3,22,15,31,10,7], [70,80,90]]
    x = menu()
    while x != 0:
        if x == 1:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], devuelvePares(lista[i])))
                print ("")
        elif x == 2:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i],mayor(lista[i])))
                print ("")
        elif x == 3:
                for i in range(0, len(lista)):
                    print("si recibe %s, regresa %s" % (lista[i],juntarIntercambiar(lista[i])))
                    print ("")
        elif x == 4:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i],cambiarLista(lista[i])))
                print ("")
        elif x == 5:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i],calcularlista(lista[i])))
                print ("")
        elif x == 6:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i],hacerDesviacion(lista[i])))
                print ("")
        else:
            print("Error, da un valor valido")
            print("")
            x = menu()

main()











