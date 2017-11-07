#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas
#Descripcion: Programa que ejecuta ciertas instrucciones con listas

def listaPares():
    largo1 = 12
    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]

    largo2 = 3
    lista2 = [5,7,3]

    listaPar1 = []
    listaPar2 = []

    for x in range(largo1):
        if lista1[x]%2 == 0:
            a = lista1[x]
            listaPar1.append(a)

    for x in range(largo2):
        if lista2[x]%2 == 0:
            a2 = lista2[x]
            listaPar2.append(a2)

    print("Con la lista",lista1,",regresa ",listaPar1)
    print("Con la lista",lista2,",regresa ",listaPar2)

def elementoPrevioLista():
    largo1 = 12
    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]

    largo2 = 4
    lista2 = [5,4,3,2]

    listaMayor1 = []
    listaMayor2 = []

    n1 = 1
    n2 = 0

    na1 = 1
    na2 = 0

    for x in range(0,largo1-1):
        if lista1[n2] < lista1[n1]:
            a = lista1[n1]
            listaMayor1.append(a)
            n1 += 1
            n2 +=1
        else:
            n1 += 1
            n2 += 1

    for x in range(0,largo2-1):
        if lista2[na2] < lista2[na1]:
            a2 = lista2[na1]
            listaMayor2.append(a2)
            na1 += 1
            na2 +=1
        else:
            na1 += 1
            na2 += 1

    print("Con la lista",lista1," regresa",listaMayor1)
    print("Con la lista",lista2," regresa",listaMayor2)

def listasIntercalada():
    largo1 = 12
    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]

    lista2 = [1,2,3]
    largo2 = len(lista2) +2
    ultimo = lista2[-1]

    largo3 = 1
    lista3 = [7]

    listaIntercalada = []
    listaIntercalada2 = []
    listaIntercalada3 = []

    n1 = 1
    n2 = 0

    na1 = 1
    na2 = 0

    na3 = 1
    na4 = 0

    if len(lista1) == 1:
        listaIntercalada = lista1
    else:
        if largo1 %2 == 0:
            for x in range(0,int(largo1/2)):
                a = lista1[n1]
                b = lista1[n2]
                listaIntercalada.append(a)
                listaIntercalada.append(b)
                n1 += 2
                n2 += 2

        else:
            for x in range(0,largo1):
                a = lista1[n1]
                b = lista1[n2]
                listaIntercalada.append(a)
                listaIntercalada.append(b)
                n1 += 1
                n2 += 1
    print("Con la lista ",lista1,", regresa",listaIntercalada)

    if len(lista2) == 1:
        listaIntercalada2 = lista2
    else:
        if largo2 %2 == 0:
            for x in range(0,int(largo2/2)):
                a2 = lista2[n1]
                b2 = lista2[n2]
                listaIntercalada2.append(a2)
                listaIntercalada2.append(b2)
                na1 += 2
                na2 += 2

        else:
            for z in range(0,int((largo2+1)/2)):
                if na1 <= z :
                    a2 = lista2[na1]
                    b2 = lista2[na2]
                    listaIntercalada2.append(a2)
                    listaIntercalada2.append(b2)
                    na1 += 2
                    na2 += 2
            listaIntercalada2.append(ultimo)
    print("Con la lista ",lista2,", regresa",listaIntercalada2)

    if len(lista3) == 1:
        listaIntercalada3 = lista3
    else:
        if largo3 %2 == 0:
            for x in range(0,int(largo3/2)):
                a3 = lista3[n1]
                b3 = lista3[n2]
                listaIntercalada3.append(a3)
                listaIntercalada3.append(b3)
                na3 += 2
                na4 += 2

        else:
            for x in range(0,largo3):
                a3 = lista3[n1]
                b3 = lista3[n2]
                listaIntercalada3.append(a3)
                listaIntercalada3.append(b3)
                na3 += 1
                na4 += 1
    print("Con la lista ",lista3,", regresa",listaIntercalada3)

def intercalarMayorYMenor():
    lista1 = [5,9,3,22,19,31,10,7]
    lista11 = lista1[::1]

    posicionMayor = lista11.index(max(lista11))
    posicionMenor = lista11.index(min(lista11))

    mayor1 = lista11[posicionMayor]
    menor1 = lista11[posicionMenor]

    lista11.insert(posicionMenor,mayor1)
    lista11.pop(posicionMenor+1)
    lista11.insert(posicionMayor,menor1)
    lista11.pop(posicionMayor+1)

    print("Con la lista ",lista1,", regresa",lista11)

    #Lista 2

    lista2 = [1,2,3]
    lista22 = lista2[::1]

    posicionMayor = lista22.index(max(lista22))
    posicionMenor = lista22.index(min(lista22))

    mayor2 = lista22[posicionMayor]
    menor2 = lista22[posicionMenor]

    lista22.insert(posicionMenor,mayor2)
    lista22.pop(posicionMenor+1)
    lista22.insert(posicionMayor,menor2)
    lista22.pop(posicionMayor+1)

    print("Con la lista ",lista2,", regresa",lista22)

def promedioLista():
    lista1 = [70,80,90]
    lista2 = [95,21,73,24,15,69,71,80,49,100,85]

    lista1A = []
    lista2A = []

    promedioLista1 = int(sum(lista1) / len(lista1))
    promedioLista2 = int(sum(lista2) / len(lista2))

    contador1 = 0
    contador2 = 0
    for x in range(len(lista1)):
        if lista1[x] >= promedioLista1:
            contador1 += 1
            lista1A.append(x)

    for y in range(len(lista2)):
        if lista2[y] >= promedioLista2:
            contador2 += 1
            lista2A.append(y)

    print("Con la lista", lista1, "regresa" ,contador1)
    print("Con la lista", lista2, "regresa" ,contador2)

def desviacionYMedia():
    lista1 = [1,2,3,4,5,6]
    lista2 = [95,21,73,24,15,69,71,80,49,100,85]
    lista3 = [3]
    lista4 = []


    listasuma1 = []
    listasuma2 = []

    promedio1 = float(sum(lista1)/len(lista1))
    promedio2 = int(sum(lista2) / len(lista2))


    for x in range(len(lista1)):
        a = lista1[x]
        valorNoRaiz = ((a-promedio1)**2/(len(lista1)-1))
        listasuma1.append(valorNoRaiz)
    sinRaiz = sum(listasuma1)
    desviacion = float((sinRaiz)**(.5))

    for y in range(len(lista2)):
        a2 = lista2[y]
        valorNoRaiz1 = ((a2-promedio2)**2/(len(lista2)-1))
        listasuma2.append(valorNoRaiz1)
    sinRaiz1 = sum(listasuma2)
    desviacion1 = float((sinRaiz1)**(.5))

    if lista3.index(3) == 0:
        promedio3 = 0
        desviacion3 = 0
        promedio4 = 0
        desviacion4 = 0

    print("Con la lista",lista1, "regresa" ,"(",promedio1,",",desviacion,")")
    print("Con la lista",lista2, "regresa" ,"(",promedio2,",",desviacion1%6,")")
    print("Con la lista", lista3, "regresa", "(",promedio3, ",",desviacion3,")")
    print("Con la lista", lista4, "regresa", "(",promedio4, ",",desviacion4,")")

def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original")
    listaPares()
    print("")

    print("Problema 2. Regresa una lista con los valores mayores a un elemento previo de la lista")
    elementoPrevioLista()
    print("")

    print("Problema 3. Regresa una lista con pareja de datos intercalada, si la lista tiene de largo un numero impar, el ultimo no se intercala")
    listasIntercalada()
    print("")

    print("Problema 4. Regresa el numero de datos que son mayores o iguales al promedio de todos los valores de la lista")
    intercalarMayorYMenor()
    print("")

    print("Problema 5. Regresa una dupla de datos con la media y desviacion estandar a partir de una lista de datos")
    promedioLista()
    print("")

    print("Problema 6.")
    desviacionYMedia()

main()
