#encoding: UTF-8
#Javier Martínez Hernández
#Tarea de listas 2
import math


def regresarPares():
    lista=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista2=[5,7,3]
    listNueva=list()
    listaNueva2=list()
    for valor in lista:
        if valor%2==0:
            listNueva.append(valor)
    for valor in lista2:
        if valor%2==0:
            listaNueva2.append(valor)
    print(listNueva)
    print(listaNueva2)

def regresarMayores():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2=[5,4,3,2]
    listaNueva=list()
    listaNueva2=list()
    for valor in range(0,len(lista)):
        if valor !=0:
            if lista[valor]>lista[valor-1]:
                listaNueva.append(lista[valor])
    print(listaNueva)
    for valor in range(0,len(lista2)):
        if valor !=0:
            if lista2[valor]>lista2[valor-1]:
                listaNueva2.append(lista2[valor])
    print(listaNueva2)

def paresIntercambiados():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2=[1,2,3]
    listaNueva=[]
    listaNueva2=[]

    if len(lista)%2==0:
        valor = 0
        valorDos = 1
        while len(listaNueva)!=len(lista):
            listaNueva.append(lista[valorDos])
            listaNueva.append(lista[valor])
            valor+=2
            valorDos+=2
        print(listaNueva)

    if len(lista2)%2!=0 :
        cambiante=0
        while cambiante<len(lista2) :
            if cambiante+1<len(lista2):
                listaNueva2.append(lista2[cambiante+1])
                if len(listaNueva2)<len(lista2):
                    listaNueva2.append(lista2[cambiante])
            cambiante+=1
        print(listaNueva2)

def mayorYmenorCambiados():
    lista=[5,9,3,22,19,31,10,7]
    lista2=[1,2,3]
    numMax=max(lista)
    numMin=min(lista)
    maximoPosicion=lista.index(numMax)
    minimoPosicion=lista.index(numMin)
    lista.remove(numMax)
    lista.remove(numMin)
    lista.insert(minimoPosicion,numMax)
    lista.insert(maximoPosicion,numMin)
    print(lista)

    numMax2= max(lista2)
    numMin2 = min(lista2)
    maximoPosicion2= lista2.index(numMax2)
    minimoPosicion2 = lista2.index(numMin2)
    lista2.remove(numMax2)
    lista2.remove(numMin2)
    lista2.insert(minimoPosicion2, numMax2)
    lista2.insert(maximoPosicion2, numMin2)
    print(lista2)

def regresoDeMayoresAlpromedio():
    lista=[95,21,73,24,15,69,71,80,49,100,85]
    listaVacia=[]
    lista2=[70,80,90]
    listaVacia2 = []
    promedioLista=sum(lista)/len(lista)
    for variable in lista:
        if variable>=promedioLista:
            listaVacia.append(variable)
    print("Existen %d numeros mayores al promedio que es %d"%(len(listaVacia),promedioLista))
    promedioLista2 = sum(lista2) / len(lista2)
    for variable in lista2:
        if variable >= promedioLista2:
            listaVacia2.append(variable)
    print("Existen %d numeros mayores al promedio que es %d" % (len(listaVacia2), promedioLista2))

def mediaEstandarYDesviación():
    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    if len(lista)!=0 and len(lista)!=1:
        suma=[]
        promedioLista = sum(lista) / len(lista)
        for cambiante in range(len(lista)):
            suma.append(((lista[cambiante]-promedioLista)**2 /(len(lista)-1)))
        desviacionEstandar=math.sqrt(sum(suma))
        print("promedio es %d, desviación Estandar %.4f"%(promedioLista,desviacionEstandar))
    else:
        print("promedio es %d, desviación Estandar %d" % (0,0))


def main():
    entrada=int(input("""Bienvenido al menú principal
    ¿Qué desea hacer?
    1. Regresar números pares
    2. Regresar mayores a un elemento previo
    3. Pares intercambiados
    4. Mayor y menor cambiados
    5. Regreso de mayores que el promedio
    6. media estandar y desviación estandar
    0.Salir
    : """))
    while entrada!=0:
        if entrada==1:
            regresarPares()
            entrada = int(input("¿Que desea hacer?: "))
        elif entrada==2:
            regresarMayores()
            entrada = int(input("¿Que desea hacer?: "))
        elif entrada==3:
            paresIntercambiados()
            entrada = int(input("¿Que desea hacer?: "))
        elif entrada==4:
            mayorYmenorCambiados()
            entrada = int(input("¿Que desea hacer?: "))
        elif entrada==5:
            regresoDeMayoresAlpromedio()
            entrada = int(input("¿Que desea hacer?: "))
        elif entrada==6:
            mediaEstandarYDesviación()
            entrada = int(input("¿Que desea hacer?: "))
        else:
            entrada=int(input("Numero no valido, ingrese un numero válido: "))
            
main()