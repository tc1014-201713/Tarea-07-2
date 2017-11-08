#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y regrese cada pareja de datos intercambiados.

def intercambiarDatos(lista):
    Lista=[]
    if len(Lista)%2==0:

        for i in range(0,len(lista)-1,2):
            Lista.append(lista[i+1])
            Lista.append((lista[i]))

        else:

            Lista.append(lista[-1])

    return Lista



def main():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista1 = [1, 2, 3]
    lista2 = [7]
    print("Dada la lista", lista, "regresa", intercambiarDatos(lista))
    print("Dada la lista", lista1, "regresa", intercambiarDatos(lista1))
    print("Dada la lista", lista2, "regresa", intercambiarDatos(lista2))


main()