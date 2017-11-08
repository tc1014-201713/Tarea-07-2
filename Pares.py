#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y regrese solo los números pares de la lista.


def calcularPar(lista):
    par=[]
    for i in lista:
        if i %2==0:
            par.append(i)
    return par

def main():
    lista=	[1,2,3,2,4,60,5,8,3,22,44,55]
    lista1= [5,7,3]
    print("De la lista dada",lista,"los números pares son:",calcularPar(lista))
    print("De la lista dada", lista1, "los números pares son:", calcularPar(lista1))










main()

