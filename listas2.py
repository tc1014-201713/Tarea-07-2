# enconding: UTF-8
# Autor: Dora Gabriela Lizárraga González
# Con este programa se probaran diferentes aplicaciones de las listas

def crearListaPares(listaPares):
    listaParesArreglo= []
    leng= len(listaPares)
    for i in range(leng):
        if listaPares[0]%2==0:
            listaParesArreglo.append(listaPares[0])
            del listaPares[0]
        else:
            del listaPares[0]
    return listaParesArreglo

def crearListaMayores(listaElementosM):
    leng = len(listaElementosM)
    listaElementos=[]
    for i in range(1,leng):
        if listaElementosM[i-1] < listaElementosM[i]:
            listaElementos.append(listaElementosM[i])
    return listaElementos

def crearListaIntercambiados(listaIntercambio):
    listaCambiada= []
    leng= len(listaIntercambio)
    if leng == 1:
        listaCambiada = listaIntercambio
    for i in range(0,leng-1,2):
        listaCambiada.append(listaIntercambio[i + 1])
        listaCambiada.append(listaIntercambio[i])
        if leng%2!=0:
            listaCambiada.append(listaIntercambio[-1])
    return listaCambiada

def intercambiarValoresExtremos(listaExtremos):
    valorMax= max(listaExtremos)
    valorMin= min(listaExtremos)
    indexMax= listaExtremos.index(valorMax)
    indexMin= listaExtremos.index(valorMin)
    listaExtremos.insert(indexMax,valorMin)
    del listaExtremos[indexMax+1]
    listaExtremos.insert(indexMin,valorMax)
    del listaExtremos[indexMin + 1]
    return listaExtremos

def calcularValoresPromedio(listaPromedio):
    cantidadElementos = len(listaPromedio)
    listaSuma = sum(listaPromedio)
    promedio = listaSuma/cantidadElementos
    contadorMayorPromedio=0
    for i in range(cantidadElementos):
        if listaPromedio[i] >= promedio:
            contadorMayorPromedio += 1
    return contadorMayorPromedio

def calcularDesvyMedi(listaDupla):
    sumatoria = sum(listaDupla)
    n = len(listaDupla)
    if listaDupla == [] or listaDupla ==[3]:
        media = 0
        desviacionEstandar=0
    else:
        media = (float(sumatoria/n))
        desviacion = 0
        for i in range(n):
            desviacion += ((listaDupla[i] - media) ** 2)
        desviacionEstandar = (desviacion / (n - 1)) ** 0.5
    return (media, desviacionEstandar)

def main():
    print("Tarea 07-2")
    print("Dora Gabriela Lizárraga González")
    print()
    # Problema 1
    print("1. Regresa una lista que regresa solamente los pares.")
    listaPares = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("Si recibe", [1,2,3,2,4,60,5,8,3,22,44,55], ", regresa", crearListaPares(listaPares))
    listaPares = [5, 7, 3]
    print("Si recibe", [5, 7, 3], ", regresa", crearListaPares(listaPares))
    print()
    # Problema 2
    print("2. Regresa una lista que regresa el mayor de dos elementos consecutivos.")
    listaElementosM = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("Si recibe", listaElementosM, ", regresa", crearListaMayores(listaElementosM))
    listaElementosM=[5,4,3,2]
    print("Si recibe", listaElementosM, ", regresa", crearListaMayores(listaElementosM))
    print()
    # Problema 3
    print("3. Regresa una lista que intercambia valores.")
    listaIntercambio = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("Si recibe", listaIntercambio, ", regresa", crearListaIntercambiados(listaIntercambio))
    listaIntercambio = [1,2,3]
    print("Si recibe", listaIntercambio, ", regresa", crearListaIntercambiados(listaIntercambio))
    listaIntercambio = [7]
    print("Si recibe", listaIntercambio, ", regresa", crearListaIntercambiados(listaIntercambio))
    print()
    # Problema 4
    print("4. Regresa una lista que cambia de lugar los valores mayor y menor.")
    listaExtremos = [5, 9, 3, 22, 19, 31, 10, 7]
    print("Si recibe", listaExtremos, ", regresa", intercambiarValoresExtremos(listaExtremos))
    listaExtremos = [1,2,3]
    print("Si recibe", listaExtremos, ", regresa", intercambiarValoresExtremos(listaExtremos))
    print()
    # Problema 5
    print("5. Regresa una lista que cuenta cuantos valores existen igual o mayor al promedio de la lista original.")
    listaPromedio = [70, 80, 90]
    print("Si recibe", listaPromedio, ", regresa", calcularValoresPromedio(listaPromedio))
    listaPromedio = [95,21,73,24,15,69,71,80,49,100,85]
    print("Si recibe", listaPromedio, ", regresa", calcularValoresPromedio(listaPromedio))
    print()
    # Problema 6
    print("6. Regresa los valores de la media y desviacion estandar que se obtienen a partir de los datos.")
    listaDupla = [1, 2, 3, 4, 5, 6]
    print("Si recibe", listaDupla, ", regresa", calcularDesvyMedi(listaDupla))
    listaDupla = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    print("Si recibe", listaDupla, ", regresa", calcularDesvyMedi(listaDupla))
    listaDupla = []
    print("Si recibe", listaDupla, ", regresa", calcularDesvyMedi(listaDupla))
    listaDupla = [3]
    print("Si recibe", listaDupla, ", regresa", calcularDesvyMedi(listaDupla))

main()