
# Autor: Pedro Cortés Soberanes // A01374919
# Tarea 7.2


#############################################################################


def calcularNumPares(lista):
    listaPares = []
    for x in range (len(lista)):
        if x%2==0:
            listaPares.append(x)
    return listaPares

#############################################################################

def calcularValoresPrevio(lista):
    lista1=[]
    for x in range (0,len(lista1)-1):
        if lista [x]<lista[x+1]:
            lista1.append(lista[x+1])
    return lista1


#############################################################################

def calcularParejasDatos(lista):
    listaDInter = []
    if len(listaDInter)%2==0:

        for x in range (0,len(lista)-1,2):
            listaDInter.append(lista[x+1])
            listaDInter.append((lista[x]))

        else:
            for x in range (0,len(lista)-1,2):
                listaDInter.append(lista[x+1])
                listaDInter.append((lista[x]))
                listaDInter.append(lista[-1])
    return listaDInter



#############################################################################

def calcularMayorYMenorInter(lista):
    if len(lista) >= 1:
        lista1 = lista[:]
        mayor = max(lista)
        menor = min(lista)
        ubimayor = lista1.index(mayor)
        ubimenor = lista1.index(menor)
        lista1.remove(mayor)
        lista1.remove(menor)
        lista1.insert(ubimenor,mayor)
        lista1.insert(ubimayor,menor)
    else:
        lista1 = []
    return (lista1)

#############################################################################

def main():

    print("Problema 1")
    lista=[1,2,3,2,4,60,5,8,3,22,44,55]
    print("Con la lista ", lista, "regresa", calcularNumPares(lista))
    lista1 = [5,7,3]
    print("Con la lista ", lista1, "regresa", calcularNumPares(lista1))

    print("Problema 2")
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    print("Con la lista ", lista, "regresa", calcularNumPares(lista))
    lista1 = [5, 4, 3, 2]
    print("Con la lista ", lista1, "regresa", calcularNumPares(lista1))

    print("Problema 3")
    lista=[1,2,3,2,4,60,5,8,3,22,44,55]
    print("Con la lista ", lista, "regresa", calcularNumPares(lista))
    lista1 = [1,2,3]
    print("Con la lista ", lista1, "regresa", calcularNumPares(lista1))
    lista2 = [7]
    print("Con la lista ", lista2, "regresa", calcularNumPares(lista2))

    print("Problema 4")
    lista = [5,9,3,22,19,31,10,7]
    print("Con la lista ", lista, "regresa", calcularNumPares(lista))
    lista1 = [1,2,3]
    print("Con la lista ", lista1, "regresa", calcularNumPares(lista1))


main()