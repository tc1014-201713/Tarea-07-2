#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219

def listasPares(lista):
    global a
    global listaPar
    listaoriginal = []
    if len(lista) != 0:
        for n in range(0, len(lista)):
            a = int(lista[n])
            listaoriginal.append(a)
        listaPar = []
        for n2 in range(0, len(listaoriginal)):
            a = int(listaoriginal[n2])
        if a / 2 == a // 2:
            listaPar.append(a)
        print(listaPar)

def valoresMayores(lista):
    listaoriginal = []
    if len(lista) != 0:
        for n in range(0, len(lista)):
            a = lista[n]
            listaoriginal.append(a)
    listademayores = []
    for n in range(0, (len(listaoriginal) - 1)):
        a = listaoriginal[n]
        b = listaoriginal[n + 1]
        if b > a:
            listademayores.append(b)
    print(listademayores)


def datosInvertidos(lista):
    listaoriginal = []
    listanueva = []
    if len(lista) > 2:
        for n in range(0, len(lista)):
            a = int(lista[n])
            listaoriginal.append(a)
        for n2 in range(0, (len(listaoriginal) - 1), 2):
            a = listaoriginal[n2]
            b = listaoriginal[n2 + 1]
            listanueva.append(b)
            listanueva.append(a)
        print(listanueva)
    elif len(lista) == 2:
        a = lista[0]
        b = lista[1]
        listanueva.append(b)
        listanueva.append(a)
    elif len(lista) == 1:
        print(lista)




def mayor_Menor(lista):
    listaoriginal = []
    if len(lista) != 0:
        for n in range(0, len(lista)):
            a = int(lista[n])
            listaoriginal.append(a)
        a = max(listaoriginal)
        b = min(listaoriginal)
        x = listaoriginal.index(a)
        y = listaoriginal.index(b)
        listaoriginal.remove(a)
        listaoriginal.remove(b)
        listaoriginal.insert(x, b)
        listaoriginal.insert(y, a)
        print(listaoriginal)


def mayoralpromedio(lista):
    listaoriginal = []
    if len(lista) != 0:
        for n in range(0, len(lista)):
            a = int(lista[n])
            listaoriginal.append(a)
        a = sum(listaoriginal)
        n = len(listaoriginal)
        promedio = a / n
        listaMayor = []
        for b in range(0, n):
            a = listaoriginal[b]
            if a >= promedio:
                listaMayor.append(a)
        print(listaMayor)


def promedioydesviacion(lista):
    listaoriginal = []
    if len(lista) != 0:
        for n in range(0, len(lista)):
            a = int(lista[n])
            listaoriginal.append(a)
        a = sum(listaoriginal)
        n = len(listaoriginal)
        promedio = a / n
        b = n - 1
        listadesviada = []
        for x in range(0, n):
            j = listaoriginal[x]
            f = (j - promedio) ** 2
            listadesviada.append(f)
        k = sum(listadesviada)
        desviacion = ((k ** .5) / b)
        print("(", promedio, ",", desviacion, ")")



def main():
    print("Tarea 7.2")

    print("Problema 1: Regresa una lista con los numeros pares de la lista original")
    print("De la lista [1,2, 3 ,2, 4, 60, 5, 8, 3, 22, 44, 55], el programa regresa ", listasPares([1,2, 3 ,2, 4, 60, 5, 8, 3, 22, 44, 55]))
    print("De la lista [1, 3], el programa regresa", listasPares([1 , 3]))
    print("De una lista vacía, el programa regresa", listasPares([]))

    print("Problema 2: Regresa una lista de los valores que son mayores al valor anterior")
    print("De la lista [1, 2, 5, 4, 3, 21, 12, 3], el programa regresa ", valoresMayores([1, 2, 5, 4, 3, 21, 12, 3]))
    print("De una lista vacía, el programa regresa", valoresMayores([]))

    print("Problema 3: Regresa una lista con los valores invertidos de dos en dos")
    print("De la lista [1, 2, 3, 4, 5, 6, 7, 8], el programa regresa ", datosInvertidos([1, 2, 3, 4, 5, 6, 7, 8]))
    print("De una lista vacía, el programa regresa", datosInvertidos([]))

    print("Problema 4: El programa regresa una lista con el valor mayor y el valor menor de la lista original intercambiados de lugar ")
    print("De la lista [1, 2, 5, 51, 2, 3, 5, 9, 7, -1], el programa regresa", mayor_Menor([1, 2, 5, 51, 2, 3, 5, 9, 7, -1]))
    print("De la lista [1, 4], el programa regresa", mayor_Menor([1, 4]))
    print("De una lista vacía, el programa regresa", mayor_Menor([]))

    print("Problema 5: El programa recibe una lista y regresa una nueva con los valores mayores al promedio de la lista original")
    print("De la lista [1, 2, 3, 12, 5, 2, 8], el programa regresa", mayoralpromedio([1, 2, 3, 12, 5, 2, 8]))
    print("De la lista [1], el programa regresa", mayoralpromedio([1]))
    print("De una lista vacía, el programa regresa", mayoralpromedio([]))

    print("Problema 6: El programa recibe una lista y calcula la media aricmética y la desviación estandar")
    print("De la lista [1, 2, 3, 6, 5, 7, 8, 10, 21, 15, 45, 87, 96], el programa regresa", promedioydesviacion([1, 2, 3, 6, 5, 7, 8, 10, 21, 15, 45, 87, 96]))
    print("De la lista [1, 2], el programa regresa", promedioydesviacion([1, 2]))
    print("De una lista vacía, el programa regresa", promedioydesviacion([]))

main()