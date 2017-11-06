#Encoding: UTF-8
#Autor Aaron Villanueva

#listas a utilizar en las pruebas de cada función
listaA=[1,2,3,4,5,6]
listaB=[5,7,1,6,9,12,4]
listaC=[2,6,3,4]
listaD=[5]
listaE=[55,44,77]
listaF=[]
listaDeListas=[listaA,listaB,listaC,listaD,listaE,listaF]

#Esta función crea una nueva lista con los valores pares de una lista provista
def crearListaConPares(listaOriginal):
    listaPares=[]
    for i in listaOriginal:
        if i%2==0:
            listaPares.append(i)
    return(listaPares)

#Esta función crea una nueva lista con los valores que sean mayores al anterior
def crearListaMayores(listaOriginal):
    listaMayores=[]
    anterior=0
    for i in listaOriginal:
        if i > anterior:
            listaMayores.append(i)
        anterior=i
    return(listaMayores)

#Esta función intercambia la posición de cada par de datos de una lista provista. Si la lista tiene un
#numero impar de datos, el último no se mueve.
def intercambiarPares(listaOriginal):    
    listaNueva=[]
    contador=0
    if len(listaOriginal)>1:
        for j in listaOriginal:
            posicion=listaOriginal.index(j)
            if posicion==len(listaOriginal):
                listaNueva.append(j)
            elif posicion%2==1:
                listaNueva.insert(contador-1,j)
            else:
                listaNueva.insert(contador,j)
            contador+=1
    return(listaNueva)

#Esta función calcula el promedio de un lista y regresa una lista nueva con los valores que superen el promedio.
def definirNumerosMayoresAlPromedio(listaOriginal):
    lenOriginal=len(listaOriginal)
    if lenOriginal>0:
        promedio= sum(listaOriginal) / lenOriginal
        listaFinal=[]
        contador=0
        for j in listaOriginal:
            if j >= promedio:
                contador+=1
                listaFinal.append(j)
        return(contador, promedio,listaFinal)
    else:
        return(0,0,listaOriginal)

#Esta función intercambia la posición del valor mínimo y máximo de una lista provista
def cambiarPosicionMinMax(listaOriginal):
    listaIntercambiada = listaOriginal[:]
    if len(listaOriginal)>1:
        valormin=min(listaOriginal)
        valormax=max(listaOriginal)
        posicionmin=listaOriginal.index(valormin)
        posicionmax=listaOriginal.index(valormax)
        listaIntercambiada.remove(valormax)
        listaIntercambiada.insert(posicionmin,valormax)
        listaIntercambiada.remove(valormin)
        listaIntercambiada.insert(posicionmax,valormin)
    return(listaIntercambiada)
  
#Esta función calcula el promedio y la desviación estandar de una lista.
def calcularMediaYDesviacionEstandar(listaOriginal):
    lenOriginal=len(listaOriginal)
    media=0
    if lenOriginal>1:
        media = sum(listaOriginal) / lenOriginal
        sumatoria=0
        for i in listaOriginal:
            sumatoria+=(i-media)**2
        adentro=sumatoria/ (lenOriginal-1)
        desviacion=adentro**.5
    else:
        desviacion=0
    return(media,desviacion)


def main():
    print("Ejercicio 1. Crear lista con solo números pares")
    for k in listaDeListas:
        print("Si recibe",k,",regresa",crearListaConPares(k))
    print("")
    print("Ejercicio 2. Crear lista con los valores mayores al anterior")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", crearListaMayores(k))
    print("")
    print("Ejercicio 3. Intercambiar pareja de datos")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", intercambiarPares(k))
    print("")
    print("Ejercicio 4. Intercambiar mayor con menor")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", cambiarPosicionMinMax(k))
    print("")
    print("Ejercicio 5. Encontrar valores mayores al promedio")
    for k in listaDeListas:
        cont, prome, listFinal= definirNumerosMayoresAlPromedio(k)
        print("Si recibe", k, ",regresa %d. El promedio es %.2f y hay %d valores iguales o mayores que %.2f" %(cont,prome,cont,prome), listFinal )
    print("")
    print("Ejercicio 6. Encontrar la desviación estandar")
    for j in listaDeListas:
        final=calcularMediaYDesviacionEstandar(j)
        print("Si recibe",j,"regresa",final)

main()