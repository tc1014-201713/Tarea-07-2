#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y regrese los números mayores a los elementos previos.
def calcularLista(lista):
    parametro=[]
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            parametro.append(lista[i+1])
    return parametro

def main():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista1=	[5,4,3,2]
    print("De la lista dada", lista, "regresa los mayores los cuales son:", calcularLista(lista))
    print("De la lista dada", lista1, "regresa los mayores los cuales son:", calcularLista(lista1))

main()