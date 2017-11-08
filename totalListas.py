#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#HJunta todos los ejercicios de listas en uno.

def calcularPar(lista):
    par=[]
    for i in lista:
        if i %2==0:
            par.append(i)
    return par

def calcularLista(lista):
    parametro=[]
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            parametro.append(lista[i+1])
    return parametro

def intercambiarDatos(lista):
    Lista=[]
    if len(Lista)%2==0:

        for i in range(0,len(lista)-1,2):
            Lista.append(lista[i+1])
            Lista.append((lista[i]))

        else:

            Lista.append(lista[-1])

    return Lista



def intercambiarMm(lista):
    if len(lista) >= 1:
        Mm =lista [:]
        M = max(lista)
        m = min(lista)
        intercambioM = Mm.index(M)
        intercambiom = Mm.index(m)
        Mm.remove(M)
        Mm.remove(m)
        Mm.insert(intercambiom, M)
        Mm.insert(intercambioM, m)
    else:
        Mm = []
    return Mm



def calcularPromedio(lista):
    promedio = sum(lista) / len(lista)
    suma = 0
    for i in lista:
        if i>=promedio:
            suma += 1
    return suma

def calcularProm(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma= suma + lista[i]

    return suma / len(lista)
def calcularDesviacion(lista):
    Sumatoria=0
    for i in lista:
        suma = (i - calcularProm(lista))**2
        Sumatoria = Sumatoria + suma
    varianza=Sumatoria/(len(lista)-(1))
    desviacion= (varianza)**0.5
    return desviacion


def main():
    print("Problema 1.")
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista1 = [5, 7, 3]
    print("De la lista dada", lista, "los números pares son:", calcularPar(lista))
    print("De la lista dada", lista1, "los números pares son:", calcularPar(lista1))

    print("Problema 2.")
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista1 = [5, 4, 3, 2]
    print("De la lista dada", lista, "regresa los mayores los cuales son:", calcularLista(lista))
    print("De la lista dada", lista1, "regresa los mayores los cuales son:", calcularLista(lista1))

    print("Problema 3.")

    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista1 = [1, 2, 3]
    lista2 = [7]
    print("De la lista dada", lista, "el intercambio es:", intercambiarDatos(lista))
    print("De la lista dada", lista1, "el intercambio es:", intercambiarDatos(lista1))
    print("De la lista dada", lista2, "el intercambio es:", intercambiarDatos(lista2))


    print("Problema 4.")
    lista = [5, 9, 3, 22, 19, 31, 10, 7]
    lista1 = [1, 2, 3]
    print("De  la lista dada", lista, "la lista con el mayor y menor intercambiados es:", intercambiarMm(lista))
    print("De la lista dada", lista1, "la lista con el mayor y menor intercambiados es:", intercambiarMm(lista1))

    print("Problema 5.")
    lista = [70, 80, 90]
    lista1 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    print("De la lista dada", lista, "los números que son mayores o iguales al promedio son:", calcularPromedio(lista))
    print("De la lista dada", lista1, "los números que son mayores o iguales al promedio son:",calcularPromedio(lista1))

    print("Problema 6.")
    lista = [1, 2, 3, 4, 5, 6]
    lista1 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]

    print("De la lista dada el promedio es:", calcularPromedio(lista), "la desviacion estándar es:",
          calcularDesviacion(lista))
    print("De la lista dada el promedio es:", calcularPromedio(lista1), "la desviacion estándar es:",
          calcularDesviacion(lista1))


main()