#encoding UTF-8
#Autor: Alejandro Valenzuela Guerrero
#Tarea 7-02

#Encontrar numeros pares
def numPares(lista):
    pares=[]
    for par in lista:
        if par%2==0:
            pares.append(par)
    return pares

#Encontar numeros mayores
def numMayor(lista):
    maximos = []
    for maximo in range(0, len(lista) -1):
        if lista[maximo] < lista[maximo+1]:
            maximos.append(lista[maximo +1])
    return maximos

#Intercambia datos
def intDatos(lista):
    intercambiar = []
    i = 0 #Numeros impares
    p = 1 #Numeros pares
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
        intercambiar.append(lista[-1])

    return intercambiar

#Intercambio numero mayor y menor
def interMenorMayor(lista):
    menormayor = []
    for m in range(0,len(lista)):
        if min(lista) == lista[m]:
            menormayor.append(max(lista))
        elif max(lista) == lista[m]:
            menormayor.append(min(lista))
        else:
            menormayor.append(lista[m])
    return menormayor

#Numeros mayores o iguales al promedio de la misma
def promList(lista):
    igualmayor = 0
    for dato in range(0,len(lista)):
        if lista[dato] >= (sum(lista) / len(lista)):
            igualmayor += 1
    return igualmayor

#Sacar dulpla, media y desviación estándar
def duplaMD(lista):
    if lista == [3] or lista == []:
        return 0,0
    else:
        media = sum(lista)/len(lista)
        suma = 0
        for dato in lista:
            suma = suma + (dato - media)**2
        desvE = (suma/(len(lista)-1))**0.5
        return media, desvE

def main():
    print("---------------------------Problema 1---------------------------")
    print("Regresa una lista con valores pares de la lista original")
    print("_________________________________________________________________")
    list1=[2,3,4,24,5,50,4,9,35,70,52,90]
    print("Si recibe:",list1,"regresa:",numPares(list1))
    list2=[7,35,83]
    print("Si recibe:",list2,"regresa:",numPares(list2))
    print("---------------------------Problema 2---------------------------")
    print(" Regresa una lista con los valores que son mayores a un elemento previo")
    print("_________________________________________________________________")
    list3=[7,10,8,11,12,7,16,20,4]
    print("Si recibe:", list3, "regresa:", numMayor(list3))
    list4=[10,7,3,1]
    print("Si recibe", list4, "regresa", numMayor(list4))
    print("---------------------------Problema 3---------------------------")
    print("Regresa una lista con cada pareja de datos intercambiados")
    print("_________________________________________________________________")
    list5=[8,11,9,8,5,4,48,7]
    print("Si recibe:", list5, "regresa:", intDatos(list5))
    list6=[8]
    print("Si recibe:", list6, "regresa:", intDatos(list6))
    list7=[7,15,5,12,8,9,1,5,14,50,26,78,5]
    print("Si recibe:", list7,"Regresa:", intDatos(list7))
    print("---------------------------Problema 4---------------------------")
    print("Regresa una lista con el valor menor y el mayor intercambiados ")
    print("_________________________________________________________________")
    list8=[40,15,37,29,22,9,18,32]
    print("Si recibe:", list8, "regresa:", interMenorMayor(list8))
    print("---------------------------Problema 5---------------------------")
    print("Regresa una lista con el número de datos que son mayores o iguales al promedio de todos los valores de la lista")
    print("_________________________________________________________________")
    list9=[5,5,50,40]
    promedio=sum(list9)//len(list9)
    print("Al recibir la lista:", list9, "regresa:", promList(list9),",porque es el número de datos que son mayores o iguales al promedio que es:",promedio)
    list10=[30,20,10,40,50,5,5,20,20]
    promedio1=sum(list10)//len(list10)
    print("Al recibir la lista:",list10, "regresa:", promList(list10),",porque es el número de datos que son mayores o iguales al promedio que es:", promedio1)
    print("---------------------------Problema 6---------------------------")
    print("Regresa una dupla con la media y la desviación estándar")
    print("_________________________________________________________________")
    list11=[]
    print("Al recibir la lista:", list11, "regresa:", duplaMD(list11) )
    list12=[3]
    print("Al recibir la lista:", list12, "regresa:", duplaMD(list12))
    list13=[32,22,45,56,34,56,7,22,55,10,100]
    print("Al recibir la lista:", list13, "regresa: ",duplaMD(list13))
main()