#encoding UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa tiene distintas funciones que actúan sobre distintas listas ya asignadas en el programa.
def resolverListaValoresPares(): #Esta función regresa los valores pares de listas ya dadas
    lista1= [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    x=0
    listaNueva = []
    while not (x>=(len(lista1))):

        if lista1[x]%2==0:
            valorPar=lista1[x]

            listaNueva.append(valorPar)
        x+=1

    lista2 = [5,7,3]
    x = 0
    listaNueva2 = []
    while not (x >= (len(lista2))):

        if lista2[x] % 2 == 0:
            valorPar = lista2[x]

            listaNueva2.append(valorPar)
        x += 1
    lista3 = [4]
    x = 0
    listaNueva3 = []
    while not (x >= (len(lista3))):

        if lista3[x] % 2 == 0:
            valorPar = lista3[x]

            listaNueva3.append(valorPar)
        x += 1

    lista4 = []
    x = 0
    listaNueva4 = []
    while not (x >= (len(lista4))):

        if lista4[x] % 2 == 0:
            valorPar = lista4[x]

            listaNueva4.append(valorPar)
        x += 1

    print ("Problema 1. Regresa una lista con los valores pares de la lista original")
    print ("Con la lista {} regresa {}".format(lista1,listaNueva))
    print("Con la lista {} regresa {}".format(lista2,listaNueva2))
    print("Con la lista {} regresa {}". format(lista3,listaNueva3))
    print("Con la lista {} regresa {}".format(lista4,listaNueva4))


def resolverValoresMayores():#Esta función regresa los valores mayores a su valor anterior en una nueva lista
    lista1=	[1,2,3,2,4,60,5,8,3,22,44,55]
    listaNueva=[]
    x=1
    while not x>=len(lista1):
        if lista1[x]>lista1[x-1]:
            listaNueva.append(lista1[x])

        x+=1

    lista2 = 	[5,4,3,2]
    listaNueva2 = []
    x = 1
    while not x >= len(lista2):
        if lista2[x] > lista2[x - 1]:
            listaNueva2.append(lista2[x])

        x += 1

    lista3 = [5]
    listaNueva3 = []
    x = 1
    while not x >= len(lista3):
        if lista3[x] > lista3[x - 1]:
            listaNueva3.append(lista3[x])

        x += 1

    lista4 = []
    listaNueva4 = []
    x = 1
    while not x >= len(lista4):
        if lista4[x] > lista4[x - 1]:
            listaNueva4.append(lista4[x])

        x += 1

    print("Problema 2. Regresa una lista con los valores que son mayores al valor anterior.")
    print("Con la lista {} regresa {}".format(lista1,listaNueva))
    print("Con la lista {} regresa {}".format(lista2,listaNueva2))
    print("Con la lista {} regresa {}". format(lista3,listaNueva3))
    print("Con la lista {} regresa {}". format(lista4,listaNueva4))

def resolverListaParejasCambiadas(): #Esta función regresa las parejas de números en orden invertido
    lista1=[1,2,3,2,4,60,5,8,3,22,44,55]
    nuevaLista=[]
    x=1
    if len(lista1)%2==0:
        while not x>=(len(lista1)) :
            nuevaLista.insert((x-1),lista1[x])
            nuevaLista.insert((x),lista1[x-1])

            x+=2
    elif len(lista1)%2==1:
        while not x>=(len(lista1)-1):
            nuevaLista.insert((x-1),lista1[x])
            nuevaLista.insert((x),lista1[x-1])

            x+=2
        nuevaLista.insert(len(nuevaLista),lista1[len(lista1)-1])
    nuevaLista2=[]
    lista2=[1,2,3]
    x=1
    if len(lista2) % 2 == 0:
        while not x >= (len(lista2)):
            nuevaLista2.insert((x - 1), lista2[x])
            nuevaLista2.insert((x), lista2[x - 1])

            x += 2
    elif len(lista2) % 2 == 1:
        while not x > (len(lista2) - 1):
            nuevaLista2.insert((x - 1), lista2[x])
            nuevaLista2.insert((x), lista2[x - 1])

            x += 2
        nuevaLista2.insert(len(nuevaLista2), lista2[len(lista2) - 1])
    nuevaLista3 = []
    lista3 = []
    x=1
    if len(lista3) % 2 == 0:
        while not x >= (len(lista3)):
            nuevaLista3.insert((x - 1), lista3[x])
            nuevaLista3.insert((x), lista3[x - 1])

            x += 2
    elif len(lista3) % 2 == 1:
        while not x > (len(lista3) - 1):
            nuevaLista3.insert((x - 1), lista3[x])
            nuevaLista3.insert((x), lista3[x - 1])

            x += 2
        nuevaLista3.insert(len(nuevaLista3), lista3[len(lista3) - 1])
    nuevaLista4 = []
    lista4 = [7]
    x = 1
    if len(lista4) % 2 == 0:
        while not x >= (len(lista4)):
            nuevaLista4.insert((x - 1), lista4[x])
            nuevaLista4.insert((x), lista4[x - 1])

            x += 2
    elif len(lista4) % 2 == 1:
        while not x > (len(lista4) - 1):
            nuevaLista4.insert((x - 1), lista4[x])
            nuevaLista4.insert((x), lista4[x - 1])

            x += 2
        nuevaLista4.insert(len(nuevaLista4), lista4[len(lista4) - 1])
    print("Problema 3. Intercambia el orden de las parejas de los datos de la lista.")
    print("Con la lista {} regresa {}".format(lista1, nuevaLista))
    print("Con la lista {} regresa {}".format(lista2, nuevaLista2))
    print("Con la lista {} regresa {}".format(lista3, nuevaLista3))
    print("Con la lista {} regresa {}".format(lista4, nuevaLista4))

def resolverListaIntercambiarMinimosYMaximos(): #Esta función intercambia el orden de los valores mínimos y máximos
    nuevaLista1= []
    lista1=	[5,9,3,22,19,31,10,7]
    x=0
    while not x>=(len(lista1)):
        nuevaLista1.append(lista1[x])
        if lista1[x]==max(lista1):
            valorMax= x

        if lista1[x]==min(lista1):
            valorMin= x


        x+=1
    if len(lista1)>0:
        nuevaLista1.remove(nuevaLista1[valorMax])
        nuevaLista1.insert(valorMax, min(lista1))
        nuevaLista1.remove(nuevaLista1[valorMin])
        nuevaLista1.insert(valorMin, max(lista1))
    else:
        nuevaLista1=[]

    nuevaLista2 = []
    lista2 = [1,2,3]
    x = 0
    while not x >= (len(lista2)):
        nuevaLista2.append(lista2[x])
        if lista2[x] == max(lista2):
            valorMax = x

        if lista2[x] == min(lista2):
            valorMin = x


        x += 1
    if len(lista2)>0:
        nuevaLista2.remove(nuevaLista2[valorMax])
        nuevaLista2.insert(valorMax, min(lista2))
        nuevaLista2.remove(nuevaLista2[valorMin])
        nuevaLista2.insert(valorMin, max(lista2))
    else:
        nuevaLista2=[]

    nuevaLista3 = []
    lista3 = [7]
    x = 0
    while not x >= (len(lista3)):
        nuevaLista3.append(lista3[x])
        if lista3[x] == max(lista3):
            valorMax = x

        if lista3[x] == min(lista3):
            valorMin = x


        x += 1
    if len(lista3)>0:
        nuevaLista3.remove(nuevaLista3[valorMax])
        nuevaLista3.insert(valorMax, min(lista3))
        nuevaLista3.remove(nuevaLista3[valorMin])
        nuevaLista3.insert(valorMin, max(lista3))
    else:
        nuevaLista3=[]

    nuevaLista4 = []
    lista4 = []
    x = 0
    while not x >= (len(lista4)):
        nuevaLista4.append(lista4[x])
        if lista4[x] == max(lista4):
            valorMax = x

        if lista4[x] == min(lista4):
            valorMin = x
        x += 1


    if len(lista4)>0:
        nuevaLista4.remove(nuevaLista4[valorMax])
        nuevaLista4.insert(valorMax, min(lista4))
        nuevaLista4.remove(nuevaLista4[valorMin])
        nuevaLista4.insert(valorMin, max(lista4))
    else:
        nuevaLista4=[]

    print("Problema 4. Intercambia el lugar del valor mínimo y máximo.")
    print("Con la lista {} regresa {}".format(lista1,nuevaLista1))
    print("Con la lista {} regresa {}".format(lista2,nuevaLista2))
    print("Con la lista {} regresa {}".format(lista3,nuevaLista3))
    print("Con la lista {} regresa {}". format(lista4, nuevaLista4))


def resolverListaNumerosMayoresAlPromedio(): #Esta función regresa el número de valores mayores al promedio, de los valores de la lista.
    lista1=[70,	80,	90]
    nuevaLista1=[]
    promedio=sum(lista1)/len(lista1)
    print("Problema 5. Regresa de una lista el número de datos mayores o iguales al promedio")
    x=0
    while not x>=len(lista1):
        if lista1[x]>=promedio:
            nuevaLista1.append(lista1[x])

        x+=1
    print("Si recibe {} regresa {}. Porque el promedio es {} y hay {} valores mayores o iguales a {}, {}".format((lista1),len(nuevaLista1), promedio, len(nuevaLista1), promedio,nuevaLista1))

    lista2 = 	[95,21,73,24,15,69,71,80,49,100,85]
    nuevaLista2 = []
    promedio = sum(lista2) / len(lista2)

    x = 0
    while not x >= len(lista2):
        if lista2[x] >= promedio:
            nuevaLista2.append(lista2[x])

        x += 1
    print("Si recibe {} regresa {}. Porque el promedio es {} y hay {} valores mayores o iguales a {}, {}".format((lista2),len(nuevaLista2), promedio, len(nuevaLista2), promedio,nuevaLista2))
    lista3 = [3]
    nuevaLista3 = []
    promedio = sum(lista3) / len(lista3)

    x = 0
    while not x >= len(lista3):
        if lista3[x] >= promedio:
            nuevaLista3.append(lista3[x])

        x += 1
    print(
        "Si recibe {} regresa {}. Porque el promedio es {} y hay {} valores mayores o iguales a {}, {}".format((lista3),len(nuevaLista3),promedio,len(nuevaLista3),promedio,nuevaLista3))

    lista4 = []
    nuevaLista4 = []
    if not len(lista4)>0:
        promedio =0
    else:
        promedio = sum(lista4) / len(lista4)

        x = 0

        while not x >= len(lista4):
            if lista4[x] >= promedio:
                nuevaLista4.append(lista4[x])

            x += 1
    print("Si recibe {} regresa {}. Porque el promedio es {} y hay {} valores mayores o iguales a {}, {}".format(( lista4),len(nuevaLista4), promedio,len(nuevaLista4),promedio,nuevaLista4))


def resolverPromedioYDesviaciónEstándar(): #Esta función da el promedio y la desviación estándar.
    lista1=	[1,2,3,4,5,6]
    nuevaLista1=[]
    promedio=0
    desviacion =0
    for x in range (0,len(lista1)):
        promedio=promedio+ lista1[x]
    promedio=promedio/len(lista1)
    nuevaLista1.append(promedio)
    for x in range (0, len(lista1)):
        desviacion= desviacion+(lista1[x]-promedio)**2

    desviacion=((desviacion)/(len(lista1)-1))**0.5
    nuevaLista1.append(desviacion)

    lista2 = 	[95,21,73,24,15,69,71,80,49,100,85]
    nuevaLista2 = []
    promedio = 0
    desviacion = 0
    for x in range(0, len(lista2)):
        promedio = promedio + lista2[x]
    promedio = promedio / len(lista2)
    nuevaLista2.append(promedio)
    for x in range(0, len(lista2)):
        desviacion = desviacion + (lista2[x] - promedio) ** 2

    desviacion = ((desviacion) / (len(lista2) - 1)) ** 0.5
    nuevaLista2.append(desviacion)

    lista3 = [3]
    nuevaLista3 = []
    promedio = 0
    desviacion = 0
    for x in range(0, len(lista3)):
        promedio = promedio + lista3[x]
    promedio = promedio / len(lista3)
    nuevaLista3.append(promedio)
    if len(lista3)>1:
        for x in range(0, len(lista3)):
            desviacion = desviacion + (lista3[x] - promedio) ** 2

        desviacion = ((desviacion) / (len(lista3) - 1)) ** 0.5
        nuevaLista3.append(desviacion)
    else:
        desviacion =0
        nuevaLista3.append(desviacion)

    lista4 = []
    nuevaLista4 = []
    promedio = 0
    desviacion = 0
    if len(lista4)>0:
        for x in range(0, len(lista4)):
            promedio = promedio + lista4[x]
        promedio = promedio / len(lista4)
    else:
        promedio=0
    nuevaLista4.append(promedio)
    if len(lista4) > 1:
        for x in range(0, len(lista4)):
            desviacion = desviacion + (lista4[x] - promedio) ** 2

        desviacion = ((desviacion) / (len(lista4) - 1)) ** 0.5
        nuevaLista4.append(desviacion)
    else:
        desviacion = 0
        nuevaLista4.append(desviacion)
    print("Problema 6. Regresa el promedio y la desviación estándar")
    print("Si recibe {} regresa {}".format(lista1,nuevaLista1))
    print("Si recibe {} regresa {}".format(lista2, nuevaLista2))
    print("Si recibe {} regresa {}".format(lista3, nuevaLista3))
    print("Si recibe {} regresa{}".format(lista4,nuevaLista4))


def main(): #Programa principal
    resolverListaValoresPares()
    print ()
    resolverValoresMayores()
    print()
    resolverListaParejasCambiadas()
    print()
    resolverListaIntercambiarMinimosYMaximos()
    print()
    resolverListaNumerosMayoresAlPromedio()
    print()
    resolverPromedioYDesviaciónEstándar()

main()