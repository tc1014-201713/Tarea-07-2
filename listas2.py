#encoding: UTF-8
# Autor: Eduardo Gallegos Solís
# Tarea 7 de listas

lista1 = [1,2,3,2,4,60,5,8,3,22,44,55]
lista2 = [5,7,3]
lista3 = [5,4,3,2]
lista4 = [5,9,3,22,19,31,10,7]

def calcularPrimeroProblema1():
    listaBuena = []
    for dato in lista1:
        if dato%2 == 0:
            listaBuena.append(dato)
    return listaBuena

def calcularPrimeroProblema2():
    listaBuenaDos = []
    for dato2 in lista2:
        if dato2 % 2 == 0:
            listaBuenaDos.append(dato2)
    return listaBuenaDos

def segundoProblema1():
    lista = []
    for h in range (len(lista1)-1):
        if lista1[h] < lista1[h+1]:
            lista.append(lista1[h+1])
    return lista


def segundoProblema2():
    lista = []
    for h in range(len(lista3) - 1):
        if lista3[h] < lista3[h + 1]:
            lista.append(lista3[h + 1])
    return lista
def tercerProblema(listaB):
    lista = []
    if len(listaB)%2 == 0:
        for x in range(0,len(listaB),2):
            par = listaB[x]
            impar = listaB[x+1]
            lista.append(impar)
            lista.append(par)
            return lista
    elif len(listaB)//2 == 0:
        lista.append(listaB[-1])
        return lista
    elif len(listaB)%2 !=0:
        for x in range (0,len(listaB)-1,2):
            par = listaB[x]
            impar = listaB[x + 1]
            lista.append(impar)
            lista.append(par)
            lista.append(listaB[-1])
            return lista

def cuartoProblema(listaA):
    if len(listaA)!=0:
        lista = listaA
        mayor = max(lista)
        menor = min(lista)
        lugarMayor = lista.index(mayor)
        lugarMenor = lista.index(menor)
        lista.remove(mayor)
        lista.remove(menor)
        lista.insert(lugarMayor,menor)
        lista.insert(lugarMenor,mayor)
    return lista

def problemaCinco(listaA):
    promedio = (sum(listaA)//len(listaA))
    lista =[]
    for i in listaA:
        contador = 1
        if i >= promedio:
            lista.append(i)
            contador += 1
    print("regresa",contador,"El promedio es",promedio,"y hay",contador,"valores mayores o iguales a", promedio,lista)

def problemaSeis(listaA):
    if len(listaA) > 1:
        media = (sum(listaA)/len(listaA))
        a = 0
        for i in listaA:
            a += (i - media)**2
        desviacion = (a/(len(listaA)-1))**.5
        print(media ,",", desviacion)
    else:
        print("0,0")

def main():
    print("""Problema 1. Regresa una lista con los valores pares de la lista original.
Con la lista""",lista1 ,",regresa",calcularPrimeroProblema1(),"""
Con la lista""", lista2, ", regresa", calcularPrimeroProblema2())
    print("""Problema 2. Regresa una lista con los valores que son mayores a su elemento previo dentro de una lista.
Con la lista""", lista1, ",regresa", segundoProblema1(), """
Con la lista""", lista3, ", regresa", segundoProblema2())
    print("""Problema 3. Regresa una lista con los pares de valores intercalados, a menos que el último valor de la lista sea impar.
Con la lista""",lista1 ,",regresa",tercerProblema(lista1),"""
Con la lista""", [1,2,3], ", regresa", tercerProblema([1,2,3]),"""
Con la lista""", [7], ", regresa", tercerProblema([7]))
    print("""Problema 4. Regresa una lista con el valor mayor y el menor intercambiados.
Con la lista""", lista4, ",regresa", cuartoProblema(lista4), """
Con la lista""", [1,2,3], ", regresa", cuartoProblema([1,2,3]))
    print("""Problema 5. Regresa una lista con los datos mayores o iguales al promedio de los datos de la lista original.
Con la lista""", [70,80,90])
    problemaCinco([70,80,90])
    print("Con la lista", [95,21,73,24,15,69,71,80,49,100,85])
    problemaCinco([95,21,73,24,15,69,71,80,49,100,85])
    print("""Problema 6. Regresa una dupla con la media y la desviación estandar de los elementos de una lista.
Con la lista""", [1,2,3,4,5,6], ",regresa"), problemaSeis([1,2,3,4,5,6])
    print ("Con la lista", [95,21,73,24,15,69,71,80,49,100,85], ", regresa"), problemaSeis([95,21,73,24,15,69,71,80,49,100,85])
    print ("Con la lista", [3], ", regresa"), problemaSeis([3])
main()