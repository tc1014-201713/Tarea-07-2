#encoding: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Descripción: Genera listas a partir de otras listas

from random import randint

lista1 = []
lista2 = []
lista3 = []
listaPar = []
listaN = []
listaR = []

# Genera listas
def generaListas():
    # Genera lista con 25 valores aleatorios entre 0 y 100
    for k in (range (25)):
        lista1.append(randint(0, 100))
    # Genera una lista de 24 valores aleatorios entre 0 y 100
    for k in (range (24)):
        listaPar.append(randint(0, 100))
    # Genera una lista sin valores repetidos a partir de "lista1"
    for dato in lista1:
        if dato not in listaN:
            listaN.append(dato)
    # Genera una lista de un solo valor aleatorio entre 0 y 100
    lista3.append(randint(0,100))

# Saca los números pares de la lista que se procesa
def sacarPares(lista):
    listaR.clear()
    for dato in range(len(lista)):
        if (lista[dato])%2 == 0:
            listaR.append(lista[dato])
    return listaR

# Genera una lista con valores cuyos antecesores inmediatos son menores
def sacarElementoPrevioMayor(lista):
    listaR.clear()
    for dato in range(1,len(lista)):
        if lista[dato]>lista[dato-1]:
            listaR.append(lista[dato])
    return listaR

# Genera una lista con cada pareja de datos invertida
def reacomodarParejas(lista):
    listaR.clear()
    for dato in range(0, len(lista)-1, 2):
        listaR.append(lista[dato+1])
        listaR.append(lista[dato])
    if len(lista)%2 !=0:
        listaR.append(lista[len(lista)-1])
    return listaR

# Intercambia los valores máximo y mínimo de posición
def intercambiarMayorYMenor (lista):
    if len(lista)>1:
        maximo = max(lista)
        minimo = min(lista)
        posMax = lista.index(maximo)
        posMin = lista.index(minimo)
        if posMin<posMax :
            lista.remove(maximo)
            lista.remove(minimo)
            lista.insert(posMin, maximo)
            lista.insert(posMax, minimo)
        else:
            lista.remove(maximo)
            lista.remove(minimo)
            lista.insert(posMin-1, maximo)
            lista.insert(posMax, minimo)

    elif len(lista)==0:
        lista = []
    return lista


# Cuenta los datos mayores o iguales al promedio
def contarDatosMayoresOIguales(lista):
    contador = 0
    if len(lista)>0:
        promedio = sum(lista)/len(lista)
        for dato in lista:
            if dato >= promedio:
                contador+=1
    return contador

# Calcula la desviación estandar y la media aritmética
def calcularMedia(lista):
    sumatoria = 0
    desviacion = 0
    media = 0
    if len(lista)>1:
        media = sum(lista)/len(lista)
        for dato in lista:
            sumatoria = sumatoria + (dato-media)**2
        desviacion = (sumatoria/(len(lista)-1))**.5
    return (media, desviacion)
            
def main():
    generaListas()

    print("Problema 1. Regresa una lista con los valores pares de la lista original. ")
    print("Con la lista ", lista1, ", regresa ", sacarPares(lista1))
    print("Con la lista ", lista2, ", regresa ", sacarPares(lista2))
    print("Con la lista ", lista3, ", regresa ", sacarPares(lista3))
    print()
    print("Problema 2. Regresa una lista con los valores que son mayores al elemento previo. ")
    print("Con la lista ", lista1, ", regresa ", sacarElementoPrevioMayor(lista1))
    print("Con la lista ", lista2, ", regresa ", sacarElementoPrevioMayor(lista2))
    print("Con la lista ", lista3, ", regresa ", sacarElementoPrevioMayor(lista3))
    print()
    print("Problema 3. Regresa una lista con cada par de datos intercambiados. ")
    print("Con la lista ", lista1, ", regresa ", reacomodarParejas(lista1))
    print("Con la lista ", listaPar, ", regresa ", reacomodarParejas(listaPar))
    print("Con la lista ", lista2, ", regresa ", reacomodarParejas(lista2))
    print("Con la lista ", lista3, ", regresa ", reacomodarParejas(lista3))
    print()
    print("Problema 4. Regresa una lista con el valor máximo y mínimo intercambiados. ")
    print("Con la lista ", listaN, ", regresa ", intercambiarMayorYMenor(listaN))
    print("Con la lista ", lista2, ", regresa ", intercambiarMayorYMenor(lista2))
    print("Con la lista ", lista3, ", regresa ", intercambiarMayorYMenor(lista3))
    print()
    print("Problema 5. Regresa el número de valores que son mayores o iguales al promedio de la lista. ")
    print("Con la lista ", lista1, ", regresa ", contarDatosMayoresOIguales(lista1))
    print("Con la lista ", lista2, ", regresa ", contarDatosMayoresOIguales(lista2))
    print("Con la lista ", lista3, ", regresa ", contarDatosMayoresOIguales(lista3))
    print()
    print("Problema 6. Regresa la media y la desviación estandar de la lista. ")
    print("Con la lista ", lista1, ", regresa ", calcularMedia(lista1))
    print("Con la lista ", lista2, ", regresa ", calcularMedia(lista2))
    print("Con la lista ", lista3, ", regresa ", calcularMedia(lista3))

main()

# Prueba de función "intercambiarMayorYMenor(lista)". Aquí sirve pero en el "main()" no sirve.
print()
print(listaN)
print(intercambiarMayorYMenor(listaN))
