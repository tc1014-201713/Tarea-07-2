#Encoding: UTF-8
#Autor: Juan Sebastián Lozano Derbez
#Listas 2

def solopares(listauno):
    pares = []
    for numero in listauno:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def eliminarmenores(listauno):

    lista = []

    counter1 = 0
    counter2 = 1

    while counter2 <= len(lista):
        if listauno[counter2] > listauno[counter1]:
            lista.append(listauno[counter2])
            counter1 += 1
            counter2 += 1

    return lista

def intercambiar(lista):
    pares =



def main():
    listauno = [1,2,3,2,4,60,5,8,3,22,44,55]


    print("Problema 1:")
    print(solopares(listauno))

    print("Problema 2:")
    print(eliminarmenores(listauno))



main()



