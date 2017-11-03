#Encoding: UTF-8
#Autor Aaron Villanueva

listaA=[1,2,3,4,5]
listaB=[5,7,1,6,9,12,4]
listaC=[2,6,3,4]
listaD=[5]
listaE=[55,44,77]
listaDeListas=[listaA,listaB,listaC,listaD,listaE]

def crearListaConPares(listaOriginal):
    listaPares=[]
    for i in listaOriginal:
        if i%2==0:
            listaPares.append(i)
    return(listaPares)

def crearListaMayores(listaOriginal):
    listaMayores=[]
    anterior=0
    for i in listaOriginal:
        if i > anterior:
            listaMayores.append(i)
        anterior=i
    return(listaMayores)

def intercambiarPares(listaOriginal):    
    listaNueva=[]
    contador=0
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


def definirNumerosMayoresAlPromedio(listaOriginal):
    lenOriginal=len(listaOriginal)
    promedio= sum(listaOriginal) / lenOriginal
    listaFinal=[]
    contador=0
    for j in listaOriginal:
        if j >= promedio:
            contador+=1
            listaFinal.append(j)
    return(contador, promedio,listaFinal)

def cambiarPosicionMinMax(listaOriginal):
    valormin=min(listaOriginal)
    valormax=max(listaOriginal)
    posicionmin=listaOriginal.index(valormin)
    posicionmax=listaOriginal.index(valormax)
    listaIntercambiada=listaOriginal[:]
    listaIntercambiada.remove(valormax)
    listaIntercambiada.insert(posicionmin,valormax)
    listaIntercambiada.remove(valormin)
    listaIntercambiada.insert(posicionmax,valormin)
    return(listaIntercambiada)
  
  
  

def calcularMediaYDesviacionEstandar(listaOriginal):
    lenOriginal=len(listaOriginal)
    print("la len es",lenOriginal)
    media=sum(listaOriginal) / lenOriginal
    print("la media es",media)
    if lenOriginal>1:
        sumatoria=0
        for i in listaOriginal:
            sumatoria+=(i-media)**2
            print(sumatoria)

        sumatoria=sumatoria**2
        adentro=sumatoria/ (lenOriginal-1)
        desviacion=adentro**.5
    else:
        desviacion=0
    return(media,desviacion)


def main():

    print("Ejercicio 1. Crear lista con solo números pares")
    for k in listaDeListas:
        print("Si recibe",k,",regresa",crearListaConPares(k))

    print("Ejercicio 2. Crear lista con los valores mayores al anterior")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", crearListaMayores(k))

    print("Ejercicio 3. Intercambiar pareja de datos")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", intercambiarPares(k))

    print("Ejercicio 4. Intercambiar mayor con menor")
    for k in listaDeListas:
        print("Si recibe", k, ",regresa", cambiarPosicionMinMax(k))

    print("Ejercicio 5. Encontrar valores mayores al promedio")
    for k in listaDeListas:
        cont, prome, listF= definirNumerosMayoresAlPromedio(k)
        print("Si recibe", k, ",regresa %d. El promedio es %.2f y hay %d valores iguales o mayores que %.2f" %(cont,prome,cont,prome))

    print("Ejercicio 6. Encontrar la desviación estandar")
    for k in listaDeListas:
        print("Si recibe",k,"regresa",calcularMediaYDesviacionEstandar(k))

main()