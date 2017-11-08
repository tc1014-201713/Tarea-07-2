#encoding:UTF-8
#José Antonio Gómez Mora
#Tarea 2

from math import sqrt


def imprimrResulatado(problema,listaOriginal,listaNueva):
    print("\nProblema",problema)
    print("Prueba la lista",listaOriginal,"regresa la lista",listaNueva)


def calcularProblema1(lista):
    nuevaLista=[]
    for i in range(0, len(lista)):
        if lista[i]%2==0:
            nuevaLista.append(lista[i])
    imprimrResulatado(1,lista,nuevaLista)


def calcularProblema2(lista):
    nuevaLista=[]
    for i in range(0,len(lista)-1):
        if lista[i+1]>lista[i]:
            nuevaLista.append(lista[i+1])

    imprimrResulatado(2, lista, nuevaLista)


def calcularProblema3(lista):
    nuevaLista=[]
    if len(lista)%2==0:
        for i in range (0,len(lista),2):
            if lista[i+1]%2==0:
                nuevaLista.append(lista[i + 1])
                nuevaLista.append(lista[i])
            else:
                nuevaLista.append(lista[i])
                nuevaLista.append(lista[i + 1])

    elif len(lista)==1:
        nuevaLista.append(lista[0])

    else:
        for k in range(0,len(lista)-1):
            if lista[k+1]%2==0:
                nuevaLista.append(lista[k + 1])
                nuevaLista.append(lista[k])
            else:

                nuevaLista.append(lista[k + 1])

    imprimrResulatado(3, lista, nuevaLista)


def calcularProblema4(lista):
    nuevaLista=[]
    mayor=max(lista)
    menor=min(lista)
    indiceMax=lista.index(mayor)
    indiceMin=lista.index(menor)
    lista.remove(mayor)
    lista.remove(menor)
    for i in range (0,len(lista)):
        nuevaLista.append(lista[i])

    nuevaLista.insert(indiceMin,mayor)
    nuevaLista.insert(indiceMax,menor)

    imprimrResulatado(4, lista, nuevaLista)


def calcularProblema5(lista):
    promedio=sum(lista)/len(lista)
    print("\nProblema 5")
    print("Prueba la lista",lista,"regresa los valores: ")
    for i in range(0,len(lista)):
        if lista[i]>=promedio:
            print(lista[i])


def calcularProblema6(lista):
    print("\nProblema 6")
    if len(lista)>1:
        promedio=sum(lista)/len(lista)
        restaXyMedia=0
        for i in range(0,len(lista)):
            suma=(lista[i]-promedio)**2
            restaXyMedia+=suma
        desviacion=sqrt(restaXyMedia/(len(lista)-1))
        print("Prueba la lista",lista,"regresa:(%.2f,%f)"%(promedio,desviacion))
    else:
        print("Prueba la lista", lista, "regresa: (%d,%d)"%(0,0))


def main():
    # LISTAS
    #Problema 1
    lista1P1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2P1 = [5, 7, 3]
    #Problema 2
    lista1P2 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2P2 = [5, 4, 3, 2]
    #Problema 3
    lista1P3 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2P3 = [1, 2, 3]
    lista3P3 = [7]
    #Problema 4
    lista1P4 = [5, 9, 3, 22, 19, 31, 10, 7]
    lista2P4 = [1, 2, 3]
    #Problema 5
    lista1P5 = [70, 80, 90]
    lista2P5 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    #Problema 6
    lista1P6 = [1,2,3,4,5,6]
    lista2P6 = [95,21,73,24,15,69,71,80,49,100,85]
    lista3P6 = [3]

    calcularProblema1(lista1P1)
    calcularProblema1(lista2P1)

    calcularProblema2(lista1P2)
    calcularProblema2(lista2P2)

    calcularProblema3(lista1P3)
    calcularProblema3(lista2P3)
    calcularProblema3(lista3P3)

    calcularProblema4(lista1P4)
    calcularProblema4(lista2P4)

    calcularProblema5(lista1P5)
    calcularProblema5(lista2P5)

    calcularProblema6(lista1P6)
    calcularProblema6(lista2P6)
    calcularProblema6(lista3P6)

main()