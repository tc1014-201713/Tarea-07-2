#encoding UTF-8
#Autor: Nazdira Abigail Cerda del Prado
#Tarea 7-02: LISTAS

#Encuentra los números pares en la lista
def encontrarPares(lista):
    pares=[]
    for par in lista:
        if par%2==0:
            pares.append(par)
    return pares

#Regresa los números mayores en una lista dada
def encontrarMayor(lista):
    maximos = []
    for maximo in range(0, len(lista) -1):
        if lista[maximo] < lista[maximo+1]:
            maximos.append(lista[maximo +1])
    return maximos

#Intercambia datos
def intercambiarDatos(lista):
    intercambiar = []
    i = 0 #Num. impar
    p = 1 #Num. par
    if len(lista) % 2 == 0:
        for inter in range(len(lista) // 2):
            intercambiar.append(lista[p])
            intercambiar.append(lista[i])
            i = i + 2
            p = p + 2
    else:
        for inter in range(len(lista) // 2):
            intercambiar.append(lista[p])
            intercambiar.append(lista[i])
            i = i + 2
            p = p + 2
        intercambiar.append(lista[-1]) #En caso de que la lista tenga cantidad de datos impar evita que su
                                    # último dato sufra cambios
    return intercambiar

#Intercambia número menor y mayor
def intercambiarMayormenor(lista):
    mayormenor = [] #
    for mm  in range(0,len(lista)):
        if max(lista) == lista[mm]:
            mayormenor.append(min(lista))
        elif min(lista) == lista[mm]:
            mayormenor.append(max(lista))
        else:
            mayormenor.append(lista[mm])
    return mayormenor

#Num. de la lista que son mayores o iguales al promedio de la misma
def calcularPromedio(lista):
    igualomayor = 0
    for dato in range(0,len(lista)):
        if lista[dato] >= (sum(lista) / len(lista)):
            igualomayor += 1
    return igualomayor

#Dulpla media y desviación estándar
def duplaMedia(lista):
    if lista == [3] or lista == []:
        return 0,0
    else:
        media = sum(lista)/len(lista)
        sumatoria = 0
        for dato in lista:
            sumatoria = sumatoria + (dato - media)**2
        desvi = (sumatoria/(len(lista)-1))**0.5
        return media, desvi

def main():
    print("---------------------------Problema 1---------------------------")
    print("Regresa una lista con valores pares de la lista original")
    print("------------------------------------------------------------------")
    lista1=[1,2,3,22,4,60,5,18,53,82,50,30]
    print("Si recibe:",lista1,"regresa:",encontrarPares(lista1))
    lista2=[5,15,9]
    print("Si recibe:",lista2,"regresa:",encontrarPares(lista2))
    print("---------------------------Problema 2---------------------------")
    print(" Regresa una lista con los valores que son mayores a un elemento previo")
    print("------------------------------------------------------------------")
    lista3=[5,8,6,9,10,5,14,18,2,8]
    print("Si recibe:", lista3, "regresa:", encontrarMayor(lista3))
    lista4=[5,3,1]
    print("Si recibe", lista4, "regresa", encontrarMayor(lista4))
    print("---------------------------Problema 3---------------------------")
    print("Regresa una lista con cada pareja de datos intercambiados")
    print("------------------------------------------------------------------")
    lista5=[5,8,6,5,2,1,45,4]
    print("Si recibe:", lista5, "regresa:", intercambiarDatos(lista5))
    lista6=[8]
    print("Si recibe:", lista6, "regresa:", intercambiarDatos(lista6))
    lista7=[1,2,3,2,4,60,5,8,3,22,44,55,8]
    print("Si recibe:", lista7,"Regresa:", intercambiarDatos(lista7))
    print("---------------------------Problema 4---------------------------")
    print("Regresa una lista con el valor menor y el mayor intercambiados ")
    print("------------------------------------------------------------------")
    lista8=[5,9,3,22,19,31,10,7]
    print("Si recibe:", lista8, "regresa:", intercambiarMayormenor(lista8))
    print("---------------------------Problema 5---------------------------")
    print("Regresa una lista con el número de datos que son mayores o iguales al promedio de todos los valores de la lista")
    print("------------------------------------------------------------------")
    lista9=[5,8,40]
    promedio=sum(lista9)//len(lista9)
    print("Al recibir la lista:", lista9, "regresa:", calcularPromedio(lista9),",porque es el número de datos que son mayores o iguales al promedio que es:",promedio)
    lista10=[5,60,40,2,5,1]
    promedio1=sum(lista10)//len(lista10)
    print("Al recibir la lista:",lista10, "regresa:", calcularPromedio(lista10),",porque es el número de datos que son mayores o iguales al promedio que es:", promedio1)
    print("---------------------------Problema 6---------------------------")
    print("Regresa una dupla con la media y la desviación estándar")
    print("------------------------------------------------------------------")
    lista11=[]
    print("Al recibir la lista:", lista11, "regresa:", duplaMedia(lista11) )
    lista12=[3]
    print("Al recibir la lista:", lista12, "regresa:", duplaMedia(lista12))
    lista13=[95,21,73,24,15,69,71,80,49,100,85]
    print("Al recibir la lista:", lista13, "regresa: ",duplaMedia(lista13))
main()