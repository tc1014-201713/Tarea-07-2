# encoding: UTF-8
# Autor: Gabriela Mariel Vargas Franco

#Ejercicio1. 	Escribe	una	función	que	recibe	como	parámetro	una	lista	de	números	enteros	y	regresa	UNA	NUEVA	lista	con	los	valores	pares	de	la	lista	original
def regresarPares(lista):
    nueva=[]

    for dato in lista:
        if dato%2==0:  #Si el dato es par
            nueva.append(dato) #Lo agrega a la lista
        return nueva



#Ejercicio2.Escribe	una	función	que	recibe	como	parámetro	una	lista	y	regresa	una	nueva	lista,	con	los	valores	que	son	mayores	a	un	elemento	previo.

def regresarMayores(lista):
    nueva=[]
    for i in range(len(lista)-1):
       if lista[i]<lista[i+1]: #Si lista indice 0< lista indice 1 entoces
           nueva.append(lista[i+1]) #se agrega el elemento mayor
    return nueva


#Ejercicio3. Escribe	una	función	que	recibe	una	lista	de	valores	y	regresa	una	nueva	lista	con	cada	pareja	de	datos	intercambiados.	Si	el	número	de	datos	es	impar,	el	último	elemento	no	cambia
def regresarIntercambiados(lista):
    nueva=[]
    indexImpar=0 #Elimpar se inicializará en el indice 0 y el par en el 1
    indexPar=1
    if len(lista)%2==0: #Si es par
        for i in range (len(lista)//2): #Para las listas con número total de valores par
            nueva.append(lista[indexPar]) #Primero se agrega el par, de ese modo se intercambian (en lugar de empezar con un valor correspondiente al indice 0, se pondra el valor correspondiente al indice 1 antes.)
            nueva.append(lista[indexImpar])
            indexImpar +=2
            indexPar +=2
    else:
        for i in range(len(lista)//2): #Para las listas con número total de valores impar
            nueva.append(lista[indexPar])    #agrega a la nueva lista el indice par
            nueva.append(lista[indexImpar])
            indexImpar +=2 #El impar se aumenta de 2 en dos, de ese modo tomará los valores del indice 0,2,4 correspondientes a las posiciones impares
            indexPar +=2  # Para que tome valores del indice 1,3,5.. correspondientes a las posiciones pares
        nueva.append(lista[-1]) # para que no tome el ultimo valor, ya que por se impar no tendrá otro numero para intercambiarse
    return nueva


#Ejercicio4. Escribe una función que recibe una lista de valores y regresa una nueva lista con el valor menor y mayor intercambiados. Suponga que los valores son únicos.
def regresarMenoryMayor(lista):
    maximo=max(lista)  #El maximo de la lista
    minimo=min(lista)  #El minimo de la lista
    indexMax=lista.index(maximo)  #El indice del maximo
    indexMin=lista.index(minimo)  #Indice del minimo

    lista.remove(maximo)   #Quita el maximo
    lista.remove(minimo)   #Quita el minimo


    lista.insert(indexMin,maximo)  # En lista.insert se pone(el indice en el que queremos poner algún valor , y el valor)
    lista.insert(indexMax,minimo)

    return lista


#Ejercicio5. Función que recibe una lista de valores y regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.
def regresarPromedio(lista):
    nueva=[]
    promedio=sum(lista)/len(lista)  #Suma entre el numero de datos
    for dato in lista:
        if dato>=promedio:  #Si  dato es mayor o igual al promedio entonces agrega el dato
            nueva.append(dato)
    valores=len(nueva) #regresa el numero total de valores que son mayor o igual al promedio
    valoresEnLetra=(str(valores))
    print("Si recibe",lista, "regresa",valores,".El promedio es ",promedio,"y hay",valoresEnLetra,"valores mayores o iguales a ", promedio,".(",nueva,")" )


#Ejercicio6. Función que recibe una lista de números y regresa una dupla con la media y la desviación estandar
def regresarDesviacion(lista):
    nueva=[]
    sumaDatos=sum(lista) #Sacar la suma
    n=len(lista) #Numero de valores en lista
    sumatoriaResultante=0
    desviacionEstandar=0
    if n>1 and n!=0:  #Si n es mayor a uno y diferente de cero entonces:
        media=sumaDatos/n
        for dato in lista:
            sumatoriaResultante=sumatoriaResultante+(dato-media)**2  #Con la formula para evitar errores primero saco el total de arriba
            desviacionEstandar=(sumatoriaResultante/(n-1))**0.5  #Posteriormente lo divido entre n-1 y le saco raíz
        return media,desviacionEstandar



    else: #si no, entonces
        return 0,0   #se regresa una dupla 0,0

def main():
    print("Problema1. Regresa una lista con los valores pares de la lista original")
    lista1=[1,2,3,2,4,60,5,8,3,22,44,55]
    nueva1=regresarPares(lista1)
    lista2=[5,7,3]
    nueva2=regresarPares(lista2)
    print("Con la lista",lista1, "regresa", nueva1)
    print("Con la lista",lista2, "regresa", nueva2)



    print("Problema2. Regresa una nueva lista con los valores que son mayores a un elemento previo")
    lista1=[1,2,3,2,4,60,5,8,3,22,44,55]
    nueva1=regresarMayores(lista1)
    lista2=[5,4,3,2]
    nueva2=regresarMayores(lista2)
    print("Con la lista",lista1, "regresa", nueva1)
    print("Con la lista",lista2, "regresa", nueva2)


    print("Problema3. Regresa una lista con cada pareja de datos intercambiado")
    lista1=[1,2,3,2,4,60,5,8,3,22,44,55]
    nueva1=regresarIntercambiados(lista1)
    lista2=[1,2,3]
    nueva2=regresarIntercambiados(lista2)
    lista3=[7]
    nueva3=regresarIntercambiados(lista3)
    print("Con la lista",lista1, "regresa", nueva1)
    print("Con la lista",lista2, "regresa", nueva2)
    print("Con la lista",lista3, "regresa", nueva3)


    print("Problema4. regresa una nueva lista con el valor menor y mayor intercambiados.")
    lista1=[5,9,3,22,19,31,10,7]
    prueba1=[5,9,3,22,19,31,10,7]
    nueva1=regresarMenoryMayor(lista1)
    print("Si recibe",prueba1,"regresa", nueva1)
    lista2=[1,2,3]
    prueba2=[1,2,3]
    nueva2=regresarMenoryMayor(lista2)
    print("Si recibe", prueba2,"regresa", nueva2)


    print("Problema5. Regresa el número de datos que son mayores o iguales al promedio de todos los valores en la lista")
    lista1=[70,80,90]
    regresarPromedio(lista1)
    lista2=[95,21,73,24,15,69,71,80,49,100,85]
    regresarPromedio(lista2)
    print("\n")


    print("Problema6. Regresa una dupla con la media y la desviación estándar.")
    lista1=[1,2,3,4,5,6]
    nueva1=regresarDesviacion(lista1)
    lista2=[95,21,73,24,15,69,71,80,49,100,85]
    nueva2=regresarDesviacion(lista2)
    lista3=[]
    nueva3=regresarDesviacion(lista3)
    lista4=[3]
    nueva4=regresarDesviacion(lista4)
    print("Si recibe",lista1,"regresa(%d,%.6f)"%nueva1)
    print("Si recibe",lista2,"regresa (%d,%.6f)"% nueva2)
    print("Si recibe", lista3,"regresa", nueva3)
    print("Si recibe",lista4,"regresa",nueva4)
main()
