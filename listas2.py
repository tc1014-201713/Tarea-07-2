#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que realiza diversas funciones con listas
import math
def listaPar(lista):
    listaPar=[]
    for dato in lista:
        if dato%2==0:
            listaPar.append(dato)
    print(listaPar)


def mayorAlPrevio(lista):
    listaMayor= []
    for i in range(0,len(lista)):
        if lista[i]>lista[i-1]:
            listaMayor.append(lista[i])
    print(listaMayor)

def voltearNumeros(lista):
    listaNumeros= []
    if len(lista)%2==0:
        for dato in range (0,len(lista),2):
            listaNumeros.append(lista[dato+1])
            listaNumeros.append(lista[dato])
        print(listaNumeros)
    else:
        for dato in range(0,len(lista)-1,2):
            listaNumeros.append(lista[dato + 1])
            listaNumeros.append(lista[dato])
        listaNumeros.append(lista[len(lista)-1])
        print(listaNumeros)

def intercambiarMenorMayor(lista):
    listaInter= lista[:]
    indiceMax=0
    indiceMin=0
    for i in range (len(listaInter)):
        if listaInter[i]==max(listaInter):
            indiceMax= i
        elif listaInter[i]==min(listaInter):
            indiceMin= i
    indice= listaInter[indiceMax]
    listaInter[indiceMax]=listaInter[indiceMin]
    listaInter[indiceMin]=indice
    print(listaInter)

def valoresArribaPromedio(lista):
    contador=0
    for dato in lista:
        if dato>=(sum(lista)//len(lista)):
            contador+=1
    print (contador)

def calcularMediaYDesviacion(lista):
    if len(lista)==0 or len(lista)==1:
        lista=[0,0]
    media= sum(lista)/len(lista)
    sumatoria=0
    for dato in (lista):
        desviacion=(dato-media)**2
        sumatoria+=desviacion
    desviacionE=math.sqrt((sumatoria)/(len(lista)-1))
    print("(",media,")","(",desviacionE,")")



def main():
    print("1.- La lista (1,3,5,7,9) produce : ")
    listaPar([1,3,5,7,9])
    print("1.- La lista (1,2,3,2,4,60,5,8,3,22,44,55) produce : ")
    listaPar([1,2,3,2,4,60,5,8,3,22,44,55])
    print("2.- La lista (1,1,33,2,5,4,7,8,9,10) produce: ")
    mayorAlPrevio([1,1,33,2,5,4,7,8,9,10])
    print("2.- La lista (5,4,3,2) produce: ")
    mayorAlPrevio([5,4,3,2])
    print("3.- La lista (1,2,3,5,6) produce:")
    voltearNumeros([1,2,3,5,6])
    print("3.- La lista (1,2,3,4,6,8) produce: ")
    voltearNumeros([1,2,3,4,6,8])
    print("4.- La lista (1,2,3) produce: ")
    intercambiarMenorMayor([1,2,3])
    print("4.- La lista (5,9,3,22,19,31,10,7) produce:")
    intercambiarMenorMayor([5,9,3,22,19,31,10,7])
    print("5.- El número de datos arriba del promedio en la lista (70,80,90) es: ")
    valoresArribaPromedio([70,80,90])
    print("6.- La media y la desviación estándar de (1,2,3,4,5,6) es: ")
    calcularMediaYDesviacion([1,2,3,4,5,6])

main()